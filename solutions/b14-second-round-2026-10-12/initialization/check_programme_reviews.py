#!/usr/bin/env python3
"""Independent finite controls for P2, the P4 family, and guidance accounting."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
from check_final_reviews import component_sizes, selected_graph, hamiltonian
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from one_tree import snapshot
from check_certificate import verify


def edge(a,b):
    return tuple(sorted((a,b)))


def subset_optimum(c, allowed=None):
    n=len(c)
    allowed=set(combinations(range(n),2)) if allowed is None else set(allowed)
    table={(1,0):0}
    for mask in range(1,1<<n,2):
        for last in range(n):
            if (mask,last) not in table:
                continue
            value=table[mask,last]
            for nxt in range(1,n):
                if mask>>nxt&1 or edge(last,nxt) not in allowed:
                    continue
                key=(mask|1<<nxt,nxt)
                candidate=value+c[last][nxt]
                if key not in table or candidate<table[key]:
                    table[key]=candidate
    answers=[table[(1<<n)-1,last]+c[last][0] for last in range(1,n)
             if ((1<<n)-1,last) in table and edge(last,0) in allowed]
    return min(answers) if answers else None


def mst(c, vertices, forced=None):
    vertices=set(vertices)
    parent={v:v for v in vertices}
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    chosen=[]
    if forced:
        a,b=forced
        assert a in vertices and b in vertices
        parent[find(a)]=find(b)
        chosen.append(forced)
    for _,a,b in sorted((c[a][b],a,b) for a,b in combinations(sorted(vertices),2)):
        if find(a)!=find(b):
            parent[find(a)]=find(b)
            chosen.append((a,b))
    assert len(chosen)==len(vertices)-1
    return sum(c[a][b] for a,b in chosen)


def p2_controls():
    spec=importlib.util.spec_from_file_location('review_ordered_dp',HERE.parent/'residual-search'/'hamilton_dp.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    bounds,suffixes,forests=0,0,0
    rows=[]
    for t in range(1,5):
        n=t+6
        z=list(range(6,n))
        prefix={(0,1),(2,3),(4,5)}|set(combinations(z,2))
        prefix|={edge(v,w) for v in z for w in (2,3,4,5)}
        future={(1,2),(3,4),(0,5)}|{(0,v) for v in z}
        allowed=prefix|future
        c=[[0 if a==b else 1 if edge(a,b) in allowed else 2 for b in range(n)] for a in range(n)]
        for root in range(n):
            cert,values,_=snapshot(c,root,[0]*n)
            assert cert['bound_numerator']==16*n
            vertices=set(range(n))-{root}
            base=mst(c,vertices)
            for e,value in values.items():
                if root in e:
                    other=next(v for v in e if v!=root)
                    independent=base+c[root][other]+min(c[root][v] for v in vertices-{other})
                else:
                    independent=mst(c,vertices,e)+sum(sorted(c[root][v] for v in vertices)[:2])
                assert 16*independent==value
                assert (value<=16*n)==(e in allowed)
                bounds+=1
        partitions=set()
        histories=[]
        for assignment in product((1,2),repeat=t):
            paths=[[0,1],[2,3],[4,5]]
            for v,owner in zip(z,assignment):
                paths[owner].insert(-1,v)
            chosen={edge(a,b) for path in paths for a,b in zip(path,path[1:])}
            assert chosen<=prefix and len(chosen)==n-3
            parts=tuple(next(j for j,path in enumerate(paths) if v in path) for v in range(n))
            partitions.add(parts)
            assert all(sum(v in e for e in chosen)==(1 if v<6 else 2) for v in range(n))
            histories.append(chosen)
            forests+=1
        assert len(partitions)==2**t
        future_order=sorted(future)
        for mask in range(1<<len(future_order)):
            extra={e for i,e in enumerate(future_order) if mask>>i&1}
            results=[]
            for chosen in histories:
                es=sorted(chosen|extra)
                results.append(hamiltonian(n,es,(1<<len(es))-1))
                suffixes+=1
            assert len(set(results))==1
            assert results[0]==(extra=={(1,2),(3,4),(0,5)})
        if t<=3:
            order=sorted(prefix)+sorted(future)
            exact=subset_optimum(c,allowed)
            for compressed in (False,True):
                value,_,_=module.solve(c,allowed,upper=n,edge_order=order,drop_saturated=compressed)
                assert value==exact==n
        rows.append({'t':t,'partition_class':len(partitions),'residual_edges':len(allowed)})
    try:
        module.solve(c,allowed,edge_order=sorted(allowed)[:-1])
    except ValueError:
        pass
    else:
        raise AssertionError('missing edge-order entry accepted')
    return {'rows':rows,'all_root_forced_bounds':bounds,'path_forests':forests,
            'literal_suffixes':suffixes,'scope':'One exponential class; dense residuals, no universal runtime factor.'}


def rational_rank(a):
    a=[list(map(F,row)) for row in a]
    r=0
    for col in range(len(a[0])):
        pivot=next((j for j in range(r,len(a)) if a[j][col]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        divisor=a[r][col]
        a[r]=[v/divisor for v in a[r]]
        for j in range(len(a)):
            if j!=r and a[j][col]:
                multiplier=a[j][col]
                a[j]=[v-multiplier*w for v,w in zip(a[j],a[r])]
        r+=1
    return r


def matching_options(vertices):
    if not vertices:
        yield []
        return
    a=vertices[0]
    for b in vertices[1:]:
        rest=[v for v in vertices if v not in (a,b)]
        for matching in matching_options(rest):
            yield [(a,b)]+matching


def p4_controls():
    data=json.loads((HERE.parent/'lp-supports'/'CHECK-RESULTS.json').read_text())
    rows=[]
    cut_checks=0
    for row in data['rows']:
        n=row['n']; length=row['subdivided_spoke_length']
        support={}
        for i in range(5):
            support[edge(i,(i+1)%5)]=1
            support[edge(5+i,5+(i+2)%5)]=1
            if i:
                support[i,5+i]=2
        chain=[0]+list(range(10,n))+[5]
        for a,b in zip(chain,chain[1:]):
            support[edge(a,b)]=2
        assert len(chain)-1==length
        assert support=={(a,b):w for a,b,w in row['support_twice_x']}
        adjacency=[set() for _ in range(n)]
        for a,b in support:
            adjacency[a].add(b); adjacency[b].add(a)
        distances=[]
        for start in range(n):
            dist=[None]*n; dist[start]=0; queue=[start]
            for v in queue:
                for u in adjacency[v]:
                    if dist[u] is None:
                        dist[u]=dist[v]+1; queue.append(u)
            distances.append(dist)
        assert distances==row['costs']
        for v in range(n):
            assert sum(w for e,w in support.items() if v in e)==4
        histogram={}
        for mask in range(1,1<<(n-1)):
            value=sum(w for (a,b),w in support.items() if ((mask>>a)&1)!=((mask>>b)&1))
            assert value>=4
            histogram[value]=histogram.get(value,0)+1
            cut_checks+=1
        assert histogram=={int(k):v for k,v in row['exact_cut_capacity_histogram_twice_x'].items()}
        es=sorted(support)
        equations=[[int(v in e) for e in es] for v in range(n)]
        equations += [[int(e==fixed) for e in es] for fixed in es if support[fixed]==2]
        rank=rational_rank(equations)
        assert rank==len(es)
        assert subset_optimum(distances)==n+1==row['optimal_cost']
        path=row['rounding_path']; mid=row['closing_two_hop_midpoint']
        assert sorted(path)==list(range(n))
        assert all(distances[a][b]==1 for a,b in zip(path,path[1:]))
        assert distances[path[0]][path[-1]]==2
        assert distances[path[0]][mid]==distances[mid][path[-1]]==1
        tree=[tuple(e) for e in row['mst_edges']]
        assert len(tree)==n-1 and all(distances[a][b]==1 for a,b in tree)
        graph=selected_graph(n,tree,(1<<len(tree))-1)
        assert component_sizes(graph)==[n]
        odd=[v for v in range(n) if len(graph[v])%2]
        assert odd==row['mst_odd_vertices']
        minimum=min(sum(distances[a][b] for a,b in m) for m in matching_options(odd))
        assert minimum==row['minimum_matching_cost']
        shortcut=row['shortcut_tour']
        assert sorted(shortcut)==list(range(n))
        cost=sum(distances[shortcut[i]][shortcut[(i+1)%n]] for i in range(n))
        assert cost==row['shortcut_cost']<=n-1+minimum
        rows.append({'n':n,'active_support_rank':rank,'optimum':n+1,'matching_cost':minimum})
    return {'rows':rows,'cut_checks_up_to_complement':cut_checks}


def guidance_controls():
    data=json.loads((HERE.parent/'guidance'/'EXPERIMENT.json').read_text())
    rows=data['rows']
    assert len(rows)==160 and len(data['training_instances'])==4
    assert len(data['test_instances'])==20 and data['training_examples']==192
    assert not set(data['training_instances'])&set(data['test_instances'])
    assert set(data['summary'])=={'ordinary','random','manual','learned'}
    packets={}
    audits={'certificates_checked':0,'forced_bounds_checked':0}
    instances={}
    for row in rows:
        name=f"{row['instance']}-{row['policy']}-r{row['repeat']}.json"
        p=json.loads((HERE.parent/'guidance'/'certificates'/name).read_text())
        audit=verify(p)
        for k in audits:
            audits[k]+=audit[k]
        c=p['instance']['costs']; n=len(c)
        if row['instance'] in instances:
            assert instances[row['instance']]==c
        instances[row['instance']]=c
        for tour_key,cost_key in [('certified_tour','optimal_cost')]:
            tour=row[tour_key]
            assert sorted(tour)==list(range(n))
            assert sum(c[tour[i]][tour[(i+1)%n]] for i in range(n))==row[cost_key]
        assert len(p['residual_edges'])==row['residual_edges']
        allowed={tuple(e) for e in p['residual_edges']}
        graph=[set() for _ in range(n)]
        for a,b in allowed:
            graph[a].add(b); graph[b].add(a)
        assert list(map(len,graph))==row['residual_degrees']
        order=row['min_fill_order']
        assert sorted(order)==list(range(n))
        width=0
        for v in order:
            neighbors=graph[v].copy()
            width=max(width,len(neighbors))
            for a,b in combinations(neighbors,2):
                graph[a].add(b); graph[b].add(a)
            for u in neighbors:
                graph[u].remove(v)
            graph[v].clear()
        assert width==row['min_fill_width_upper_bound']
        assert row['post_exact_gap']==0
        debit=row['training_debit_seconds']
        assert abs(row['overrun_seconds']-max(0,row['elimination_and_inference_seconds']+debit-data['budget_seconds']))<1e-10
        assert bool(debit)==(row['policy']=='learned')
        assert abs(row['total_proof_seconds']-row['query_wall_seconds']-debit)<1e-10
        stage_sum=row['incumbent_seconds']+row['elimination_and_inference_seconds']+debit+row['verification_seconds']+row['exact_seconds']
        assert abs(row['summed_timed_stages_seconds']-stage_sum)<1e-10
        assert row['total_proof_seconds']>=stage_sum
        packets[row['instance'],row['policy'],row['repeat']]=p
    for policy,summary in data['summary'].items():
        subset=[r for r in rows if r['policy']==policy]
        assert len(subset)==40
        assert len({(r['instance'],r['repeat']) for r in subset})==40
        assert abs(sum(r['residual_edges'] for r in subset)/40-summary['mean_residual_edges'])<1e-10
        assert sum(r['residual_dp']['transitions'] for r in subset)==summary['total_dp_transitions']
    debit_sum=sum(r['training_debit_seconds'] for r in rows)
    assert abs(debit_sum-data['training_seconds'])<1e-10
    reference={name:subset_optimum(c) for name,c in instances.items()}
    assert all(reference[r['instance']]==r['optimal_cost'] for r in rows)
    return {'queries':len(rows),'policies':4,'independent_complete_metric_optima':len(reference),
            **audits,'amortized_training_debit_correct':True,
            'timing_scope':'Corrected outer query timer includes setup and packet construction; amortized training charged once.'}


def main():
    result={'status':'passed','p2':p2_controls(),'p4':p4_controls(),'guidance':guidance_controls()}
    (HERE/'PROGRAMME-REVIEW-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
