#!/usr/bin/env python3
"""Bounded held-out policy experiment; correctness comes from checked bounds."""
from pathlib import Path
from time import perf_counter
import json
import platform
import random
import sys

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent / 'b14-first-round-2026-10-12' / 'elimination'
sys.path.insert(0, str(FIRST))
from one_tree import snapshot, incumbent, exact_tour, width_upper_bound
from check_certificate import verify

SCALE = 16
BUDGET = .05


def features(state, upper, n):
    return [1., (SCALE * upper - state['bound']) / max(1, SCALE * upper),
            state['norm'] / (n*n), state['iteration'] / 100,
            state['gain'] / max(1, SCALE * upper), state['iteration'] == 0]


def evaluate(c, root, state, upper):
    cert, forced, gradient = snapshot(c, root, state['p'], SCALE)
    old = state['bound']
    state['bound'] = cert['bound_numerator']
    state['gain'] = state['bound'] - old if state['iteration'] else 0
    state['norm'] = sum(g*g for g in gradient)
    if state['norm'] and state['bound'] < SCALE*upper:
        factor = 2 if state['iteration'] < 12 else 1
        step = max(1, factor*(SCALE*upper-state['bound']) // state['norm'])
        state['p'] = [a+step*g for a,g in zip(state['p'],gradient)]
    state['iteration'] += 1
    return cert, forced


def initial(n):
    return {'p':[0]*n, 'bound':0, 'gain':0, 'norm':0, 'iteration':0}


def ridge(samples):
    size = len(samples[0][0])
    a = [[sum(x[i]*x[j] for x,y in samples) + (1e-4 if i==j else 0)
          for j in range(size)] for i in range(size)]
    b = [sum(x[i]*y for x,y in samples) for i in range(size)]
    for i in range(size):
        pivot = max(range(i,size), key=lambda j:abs(a[j][i]))
        a[i],a[pivot] = a[pivot],a[i]
        b[i],b[pivot] = b[pivot],b[i]
        value = a[i][i]
        a[i] = [v/value for v in a[i]]
        b[i] /= value
        for j in range(size):
            if j==i: continue
            value = a[j][i]
            a[j] = [v-value*w for v,w in zip(a[j],a[i])]
            b[j] -= value*b[i]
    return b


def train(instances):
    start = perf_counter()
    samples = []
    for instance in instances:
        c = instance['costs']
        n = len(c)
        _,upper = incumbent(c)
        for root in sorted({0,n//4,n//2,3*n//4}):
            state = initial(n)
            evaluate(c,root,state,upper)
            for _ in range(12):
                x = features(state,upper,n)
                old = state['bound']
                evaluate(c,root,state,upper)
                samples.append((x,(state['bound']-old)/max(1,SCALE*upper)))
    weights = ridge(samples)
    return weights, perf_counter()-start, len(samples)


def produce(instance, policy, weights, training_debit, repeat, predictor=None):
    query_start = perf_counter()
    c = instance['costs']; n = len(c)
    clock = perf_counter()
    tour,upper = incumbent(c)
    incumbent_seconds = perf_counter()-clock
    roots = sorted({0,n//4,n//2,3*n//4})
    states = {r:initial(n) for r in roots}
    rng = random.Random(91000 + repeat*100 + instance['seed'])
    start = perf_counter()
    learned = policy.startswith('learned')
    deadline = start + BUDGET - (training_debit if learned else 0)
    certs, best = [], {}
    global_best = (-10**100,0)
    calls = 0
    while perf_counter() < deadline:
        if calls < len(roots):
            root = roots[calls]
        elif policy=='ordinary' or (learned and calls%5==0):
            root = roots[calls%len(roots)]
        elif policy=='random':
            root = rng.choice(roots)
        elif policy=='manual':
            root = max(roots, key=lambda r:
                ((SCALE*upper-states[r]['bound']) /
                 max(1,states[r]['norm']) / (1+states[r]['iteration']),-r))
        else:
            root = max(roots,key=lambda r:
                ((predictor(features(states[r],upper,n)) if predictor else
                  sum(w*x for w,x in zip(weights,features(states[r],upper,n)))),-r))
        cert,forced = evaluate(c,root,states[root],upper)
        owner = len(certs); certs.append(cert)
        global_best = max(global_best,(cert['bound_numerator'],owner))
        for e,value in forced.items():
            if e not in best or value > best[e][0]:
                best[e] = value,owner
        calls += 1
    elimination_seconds = perf_counter()-start
    assert certs, 'training debit consumed entire budget'
    used = sorted({owner for _,owner in best.values()}|{global_best[1]})
    remap = {owner:i for i,owner in enumerate(used)}
    removed = sorted(e for e,(value,_) in best.items() if value>SCALE*upper)
    allowed = set(best)-set(removed)
    packet = {
        'schema':'b14-one-tree-certificate-v1','instance':instance,'method':policy,
        'incumbent':{'tour':tour,'cost':upper}, 'certificates':[certs[i] for i in used],
        'global_lower_bound':{'numerator':global_best[0],'scale':SCALE,
                              'certificate':remap[global_best[1]]},
        'forced_bounds':[{'edge':e,'numerator':value,'scale':SCALE,
                          'certificate':remap[owner]} for e,(value,owner) in sorted(best.items())],
        'eliminated_edges':removed,'residual_edges':sorted(allowed)}
    clock = perf_counter(); audit = verify(packet)
    verification_seconds = perf_counter()-clock
    clock = perf_counter(); optimum,answer,work = exact_tour(c,allowed)
    exact_seconds = perf_counter()-clock
    assert sorted(answer)==list(range(n))
    assert sum(c[answer[i]][answer[(i+1)%n]] for i in range(n))==optimum
    width,order = width_upper_bound(n,allowed)
    degrees = [sum(v in e for e in allowed) for v in range(n)]
    debit = training_debit if learned else 0
    query_seconds = perf_counter()-query_start
    result = {
        'instance':instance['id'],'family':instance['family'],'n':n,
        'seed':instance['seed'],'repeat':repeat,'policy':policy,
        'budget_seconds':BUDGET,'training_debit_seconds':debit,
        'elimination_and_inference_seconds':elimination_seconds,
        'overrun_seconds':max(0,elimination_seconds+debit-BUDGET),
        'incumbent_seconds':incumbent_seconds,'snapshot_calls':calls,
        'verification_seconds':verification_seconds,'exact_seconds':exact_seconds,
        'summed_timed_stages_seconds':incumbent_seconds+elimination_seconds+debit+
                                     verification_seconds+exact_seconds,
        'total_proof_seconds':query_seconds+debit,
        'query_wall_seconds':query_seconds,
        'incumbent_cost':upper,'optimal_cost':optimum,'certified_tour':answer,
        'pre_exact_gap':upper/(global_best[0]/SCALE)-1,
        'post_exact_gap':0,'residual_edges':len(allowed),
        'residual_degrees':degrees,'min_fill_width_upper_bound':width,
        'min_fill_order':order,'residual_dp':work,'independent_bound_audit':audit}
    packet['measurements'] = result
    name = f"{instance['id']}-{policy}-r{repeat}.json"
    (HERE/'certificates'/name).write_text(json.dumps(packet,indent=2)+'\n')
    return result


def main():
    from one_tree import instances
    pool = instances()
    training = [i for i in pool if i['family']=='euclidean-ceil' and
                len(i['costs']) in (8,10) and i['seed'] in (0,1)]
    testing = [i for i in pool if i['seed'] in (2,3) and
               (i['family']!='euclidean-ceil' or len(i['costs'])==12)]
    weights,seconds,samples = train(training)
    runs = len(testing)*2
    debit = seconds/runs
    (HERE/'certificates').mkdir(exist_ok=True)
    rows = []
    for repeat in range(2):
        for i,instance in enumerate(testing):
            # Counterbalance policy order to reduce simple execution-order bias.
            policies = ['ordinary','random','manual','learned']
            shift = (i+repeat)%4
            for policy in policies[shift:]+policies[:shift]:
                rows.append(produce(instance,policy,weights,debit,repeat))
    reference = {}
    for instance in testing:
        value,_,work = exact_tour(instance['costs'])
        reference[instance['id']] = {'optimum':value,'work':work}
    assert all(r['optimal_cost']==reference[r['instance']]['optimum'] for r in rows)
    summaries = {}
    for policy in ('ordinary','random','manual','learned'):
        subset = [r for r in rows if r['policy']==policy]
        summaries[policy] = {
            'runs':len(subset),
            'mean_residual_edges':sum(r['residual_edges'] for r in subset)/len(subset),
            'mean_width_upper_bound':sum(r['min_fill_width_upper_bound'] for r in subset)/len(subset),
            'total_proof_seconds':sum(r['total_proof_seconds'] for r in subset),
            'total_dp_transitions':sum(r['residual_dp']['transitions'] for r in subset),
            'max_budget_overrun_seconds':max(r['overrun_seconds'] for r in subset)}
    result = {'status':'passed','budget_seconds':BUDGET,
        'clock':'perf_counter wall time; a final started snapshot may overrun',
        'hardware':platform.platform(),'python':sys.version,
        'training_instances':[i['id'] for i in training],
        'test_instances':[i['id'] for i in testing],
        'training_seconds':seconds,'training_examples':samples,
        'training_charge':'total training time divided across all learned test queries',
        'weights':weights,'summary':summaries,'rows':rows,'full_dp_controls':reference,
        'scope':'bounded controlled first deliverables for P1/P6; no universal superiority claim'}
    (HERE/'EXPERIMENT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','training_seconds':seconds,
                      'test_queries_per_policy':runs,'summary':summaries},indent=2))


if __name__=='__main__':
    main()
