#!/usr/bin/env python3
"""Exact graph controls for four additional Haar proof routes."""
from itertools import combinations
from math import gcd
from pathlib import Path
import json
from check_initial_routes import haar_components

HERE = Path(__file__).resolve().parent


def graph(m,offsets):
    adj = [set() for _ in range(2*m)]
    for u in range(m):
        for s in offsets:
            v = m+(u+s)%m
            adj[u].add(v)
            adj[v].add(u)
    return adj


def nonclosing_path(adj):
    n = len(adj)
    start = 0
    calls = 0
    def visit(path,seen):
        nonlocal calls
        calls += 1
        if len(path) == n:
            return path if path[-1] not in adj[start] else None
        for v in sorted(adj[path[-1]]-seen):
            found = visit(path+[v],seen|{v})
            if found:
                return found
        return None
    found = visit([start],{start})
    assert found
    return found,calls


def main():
    rows = []
    for primes in [(3,5,7,11),(3,5,7,13),(3,5,11,13)]:
        m = 1
        for p in primes:
            m *= p
        offsets = [0]+[m//p for p in primes]
        assert haar_components(m,offsets) == [2*m]
        triples = []
        for chosen in combinations(offsets,3):
            g = m
            for a,b in combinations(chosen,2):
                g = gcd(g,b-a)
            assert g > 1
            assert len(haar_components(m,chosen)) == g
            triples.append({'offsets':chosen,'components':g})
        rows.append({'attempt':2,'m':m,'offsets':offsets,
                     'all_cubic_offset_subgraphs_disconnected':triples})
    for m in (24,48,72):
        offsets = [0,1,4,10]
        adj = graph(m,offsets)
        assert haar_components(m,offsets) == [2*m]
        assert haar_components(m,[0,4]) == [m//2]*4
        four_cycles = sum(len(adj[u]&adj[v])*(len(adj[u]&adj[v])-1)//2
                          for u,v in combinations(range(m),2))
        assert four_cycles == 0
        assert haar_components(m,[0,1]) == [2*m]
        rows.append({'attempt':3,'m':m,'offsets':offsets,
                     'initial_cycle_cover_components':4,'four_cycles':0,
                     'hamilton_two_offset_witness':[0,1]})
    for p,q in ((3,5),(3,7),(5,7),(5,11)):
        m = p*q
        offsets = [0,p,q]
        assert haar_components(m,offsets) == [2*m]
        assert haar_components(q,[0,p%q]) == [2*q]
        lifted = haar_components(m,[0,p])
        assert lifted == [2*q]*p
        rows.append({'attempt':4,'m':m,'quotient_modulus':q,'offsets':offsets,
                     'quotient_cycle_offsets':[0,p%q],
                     'lift_components':p,'lift_component_size':2*q})
    m, offsets = 5,[0,1,2]
    adj = graph(m,offsets)
    path,calls = nonclosing_path(adj)
    assert sorted(path) == list(range(2*m)) and path[-1] not in adj[path[0]]
    for shift in range(m):
        shifted = [(v+shift)%m if v<m else m+(v-m+shift)%m for v in path]
        assert shifted[-1] not in adj[shifted[0]]
    assert haar_components(m,[0,1]) == [2*m]
    rows.append({'attempt':5,'m':m,'offsets':offsets,
                 'nonclosing_hamilton_path':path,'dfs_calls':calls,
                 'all_simultaneous_shifts_remain_nonclosing':True,
                 'hamilton_cycle_offsets':[0,1]})
    (HERE/'HAAR-ROUTE-CHECK-RESULTS.json').write_text(json.dumps(
        {'status':'passed','attempt_controls':rows,
         'scope':'Proposed construction/lifting lemmas fail; Q1953 is not refuted.'},
        indent=2)+'\n')
    print(json.dumps({'status':'passed','controls':len(rows),'catalog_question_refuted':False}))


if __name__ == '__main__':
    main()
