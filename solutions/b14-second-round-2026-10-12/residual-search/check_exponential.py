#!/usr/bin/env python3
"""Realizable exponential state quotient, with certified residual integration."""
from pathlib import Path
from itertools import combinations, product
import json
import sys
from hamilton_dp import solve

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from one_tree import snapshot, exact_tour, edge
from check_certificate import kruskal


def family(t):
    n = t+6
    internal = list(range(6,n))
    prefix = {(0,1),(2,3),(4,5)}
    prefix |= set(combinations(internal,2))
    prefix |= {edge(v,w) for v in internal for w in (2,3,4,5)}
    future = {(1,2),(3,4),(0,5)}|{(0,v) for v in internal}
    allowed = prefix|future
    c = [[0 if a==b else 1 if edge(a,b) in allowed else 2
          for b in range(n)] for a in range(n)]
    return c,prefix,future


def main():
    rows = []
    for t in range(1,6):
        c,prefix,future = family(t); n = len(c)
        full_keys = set(); end_keys = set()
        for assignments in product((1,2),repeat=t):
            paths = [[0,1],[2,3],[4,5]]
            for v,owner in zip(range(6,n),assignments):
                paths[owner].insert(-1,v)
            chosen = {edge(a,b) for p in paths for a,b in zip(p,p[1:])}
            assert chosen <= prefix and len(chosen)==t+3
            partition = tuple(next(i for i,p in enumerate(paths) if v in p) for v in range(n))
            degrees = tuple(1 if v<6 else 2 for v in range(n))
            full_keys.add((degrees,partition))
            end_keys.add((degrees,partition[:6]+(-1,)*t))
            completed = chosen|{(1,2),(3,4),(0,5)}
            assert len(completed)==n
            assert all(sum(v in e for e in completed)==2 for v in range(n))
            # Connectedness: explicit concatenate the three paths.
            tour = paths[0]+paths[1]+paths[2]
            assert sum(c[tour[i]][tour[(i+1)%n]] for i in range(n))==n
        assert len(full_keys)==2**t and len(end_keys)==1
        cert,bounds,_ = snapshot(c,0,[0]*n)
        assert cert['bound_numerator']==16*n
        residual = {e for e,bound in bounds.items() if bound<=16*n}
        assert residual==prefix|future
        # Independent forced-tree calculations check the entire residual.
        w = [[16*v for v in row] for row in c]
        vertices = list(range(1,n))
        for e,bound in bounds.items():
            if 0 in e:
                other = e[1]
                value = kruskal(w,vertices)+w[0][other]+min(w[0][v] for v in vertices if v!=other)
            else:
                value = kruskal(w,vertices,e)+sum(sorted(w[0][v] for v in vertices)[:2])
            assert value==bound
        order = sorted(prefix)+sorted(future)
        value,_,full_work = solve(c,residual,upper=n,edge_order=order)
        compact,_,compact_work = solve(c,residual,upper=n,edge_order=order,drop_saturated=True)
        oracle,_,oracle_work = exact_tour(c,residual)
        assert value==compact==oracle==n
        rows.append({'n':n,'saturated_vertices':t,'witnessed_full_partition_states':len(full_keys),
                     'witnessed_endpoint_states':len(end_keys),'residual_edges':len(residual),
                     'full_partition_dp':full_work,'endpoint_dp':compact_work,
                     'subset_dp':oracle_work,'optimum':n})
    result = {'status':'passed','rows':rows,
              'scope':'explicit exponential collapse of one realizable boundary class; no universal speed guarantee'}
    (HERE/'EXPONENTIAL-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
