#!/usr/bin/env python3
"""Compare frontier quotient against full prefix histories and subset DP."""
from itertools import combinations
from pathlib import Path
import json
import random
import sys
from time import perf_counter
from hamilton_dp import solve

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from one_tree import exact_tour
from check_certificate import verify


def main():
    rows = []
    for seed in range(8):
        rng = random.Random(seed)
        n = 6
        edges = set(combinations(range(n),2))
        if seed%2:
            mandatory = {tuple(sorted((i,(i+1)%n))) for i in range(n)}
            edges = mandatory|{e for e in edges if rng.randrange(2)}
        costs = [[0]*n for _ in range(n)]
        for u,v in combinations(range(n),2):
            costs[u][v] = costs[v][u] = rng.randrange(0,20)
        reference,_,_ = exact_tour(costs,edges)
        value,tour,work = solve(costs,edges,upper=reference)
        raw,_,raw_work = solve(costs,edges,upper=reference,compress=False)
        matched,_,matched_work = solve(costs,edges,upper=reference,drop_saturated=True)
        assert value == raw == matched == reference
        rows.append({'kind':'prefix_equivalence_control','seed':seed,
                     'optimum':value,'compressed':work,'raw':raw_work,
                     'end_matching':matched_work,'tour':tour})
    for path in sorted((FIRST/'certificates').glob('*n8*-four-roots.json')):
        data = json.loads(path.read_text())
        audit = verify(data)
        costs = data['instance']['costs']
        allowed = {tuple(e) for e in data['residual_edges']}
        clock = perf_counter()
        value,tour,work = solve(costs,allowed,upper=data['incumbent']['cost'])
        elapsed = perf_counter()-clock
        match_clock = perf_counter()
        matched,_,matched_work = solve(costs,allowed,upper=data['incumbent']['cost'],drop_saturated=True)
        matched_elapsed = perf_counter()-match_clock
        oracle,_,oracle_work = exact_tour(costs,allowed)
        assert value == matched == oracle == data['measurements']['optimal_cost']
        rows.append({'kind':'certified_residual','instance':data['instance']['id'],
                     'certificate':str(path.relative_to(HERE.parents[4])),
                     'independent_bound_audit':audit,'optimum':value,
                     'residual_edges':len(allowed),'frontier':work,'subset_dp':oracle_work,
                     'frontier_seconds':elapsed,'end_matching':matched_work,
                     'end_matching_seconds':matched_elapsed,'tour':tour})
    # Two disjoint triangles must be rejected despite every vertex degree two.
    n = 6
    edges = {(0,1),(0,2),(1,2),(3,4),(3,5),(4,5)}
    costs = [[0 if i==j else 1 for j in range(n)] for i in range(n)]
    value,_,_ = solve(costs,edges,drop_saturated=True)
    assert value is None
    receipt = {'status':'passed','rows':rows,
               'raw_prefix_controls':8,'certified_residuals':sum(r['kind']=='certified_residual' for r in rows),
               'disjoint_cycles_rejected':True,
               'scope':'Exact state-equivalence baseline and bounded P1 integration; no general performance claim.'}
    (HERE/'CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'passed','prefix_controls':8,'residuals':receipt['certified_residuals'],
                      'compressed_control_states':sum(r['compressed']['states'] for r in rows if 'compressed' in r),
                      'raw_control_states':sum(r['raw']['states'] for r in rows if 'raw' in r),
                      'end_matching_control_states':sum(r['end_matching']['states'] for r in rows if 'raw' in r),
                      'residual_full_partition_states':sum(r['frontier']['states'] for r in rows if 'frontier' in r),
                      'residual_end_matching_states':sum(r['end_matching']['states'] for r in rows if 'frontier' in r)}))


if __name__ == '__main__':
    main()
