#!/usr/bin/env python3
"""Four additional learned objectives/estimators, with full cost accounting."""
from pathlib import Path
from time import perf_counter
import json
from experiment import initial, evaluate, features, ridge, produce, SCALE, BUDGET
from one_tree import instances, incumbent, exact_tour

HERE = Path(__file__).resolve().parent


def quadratic(x):
    return x+[x[i]*x[j] for i in range(1,5) for j in range(i,5)]


def fit(training,mode):
    clock = perf_counter(); samples = []
    for instance in training:
        c = instance['costs']; n = len(c)
        _,upper = incumbent(c)
        for root in sorted({0,n//4,n//2,3*n//4}):
            state = initial(n)
            _,best = evaluate(c,root,state,upper)
            previous_work = exact_tour(c)[2]['transitions'] if mode=='work' else None
            for _ in range(12):
                x = features(state,upper,n); old = state['bound']
                _,new = evaluate(c,root,state,upper)
                old_deleted = sum(v>SCALE*upper for v in best.values())
                best = {e:max(value,best[e]) for e,value in new.items()}
                if mode=='edge':
                    y = (sum(v>SCALE*upper for v in best.values())-old_deleted)/len(best)
                elif mode=='work':
                    allowed = {e for e,v in best.items() if v<=SCALE*upper}
                    work = exact_tour(c,allowed)[2]['transitions']
                    y = (previous_work-work)/max(1,previous_work)
                    previous_work = work
                else:
                    y = (state['bound']-old)/max(1,SCALE*upper)
                samples.append((quadratic(x) if mode=='quadratic' else x,y))
    if mode=='neighbor':
        def predict(x):
            nearest = sorted((sum((a-b)**2 for a,b in zip(x,z)),y) for z,y in samples)[:5]
            return sum(y for _,y in nearest)/len(nearest)
        model = {'kind':'five-nearest-neighbor','samples':samples}
    else:
        weights = ridge(samples)
        def predict(x):
            z = quadratic(x) if mode=='quadratic' else x
            return sum(a*b for a,b in zip(weights,z))
        model = {'kind':mode+'-ridge','weights':weights}
    return predict,model,perf_counter()-clock,len(samples)


def main():
    pool = instances()
    training = [i for i in pool if i['family']=='euclidean-ceil' and
                len(i['costs']) in (8,10) and i['seed'] in (0,1)]
    testing = [i for i in pool if i['seed'] in (2,3) and
               (i['family']!='euclidean-ceil' or len(i['costs'])==12)]
    runs = len(testing)*2; rows = []; models = {}
    # Rotate the mode order over query blocks; fit once, before any test execution.
    for mode in ('edge','work','neighbor','quadratic'):
        predictor,model,seconds,samples = fit(training,mode)
        models[mode] = {'training_seconds':seconds,'examples':samples,'model':model}
        assert seconds/runs < BUDGET
        for repeat in range(2):
            for instance in testing:
                rows.append(produce(instance,'learned-'+mode,[],seconds/runs,repeat,predictor))
    baseline = json.loads((HERE/'EXPERIMENT.json').read_text())
    control = baseline['full_dp_controls']
    assert all(r['optimal_cost']==control[r['instance']]['optimum'] for r in rows)
    summary = {}
    for mode in models:
        selected = [r for r in rows if r['policy']=='learned-'+mode]
        summary[mode] = {'queries':len(selected),
            'mean_residual_edges':sum(r['residual_edges'] for r in selected)/len(selected),
            'total_dp_transitions':sum(r['residual_dp']['transitions'] for r in selected),
            'total_proof_seconds':sum(r['total_proof_seconds'] for r in selected),
            'max_overrun_seconds':max(r['overrun_seconds'] for r in selected),
            'training_seconds':models[mode]['training_seconds']}
    result = {'status':'passed','budget_seconds':BUDGET,'models':models,'summary':summary,'rows':rows,
        'training_instances':[i['id'] for i in training],'testing_instances':[i['id'] for i in testing],
        'baseline_receipt':'EXPERIMENT.json',
        'limitations':'No test-set tuning. Mode blocks are sequential; timing comparisons need stronger repetition for small effects.',
        'scope':'four specified further learned-policy attempts; no universal impossibility claim'}
    (HERE/'VARIATIONS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','summary':summary},indent=2))


if __name__=='__main__': main()
