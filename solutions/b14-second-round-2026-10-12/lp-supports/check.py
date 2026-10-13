#!/usr/bin/env python3
"""Exact cut, gap and parity certificates for one-spoke Petersen subdivisions."""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json
import sys

HERE = Path(__file__).resolve().parent
FIRST = HERE.parent.parent/'b14-first-round-2026-10-12'/'elimination'
sys.path.insert(0,str(FIRST))
from one_tree import exact_tour, prim


def edge(a,b): return tuple(sorted((a,b)))


def petersen():
    x = {}
    for i in range(5):
        x[edge(i,(i+1)%5)] = 1
        x[edge(5+i,5+(i+2)%5)] = 1
        x[edge(i,5+i)] = 2
    return x


def base_path():
    adj = {v:[] for v in range(10)}
    support = petersen()
    for a,b in support:
        adj[a].append(b); adj[b].append(a)
    def search(path):
        if len(path)==10:
            a,b = path[0],path[-1]
            if edge(a,b) in support: return None
            mid = next((v for v in adj[a] if edge(v,b) in support and
                        edge(a,v)!=(0,5) and edge(v,b)!=(0,5)),None)
            if mid is not None and (0,5) in {edge(a,b) for a,b in zip(path,path[1:])}:
                return path,mid
            return None
        for v in sorted(adj[path[-1]]):
            if v not in path:
                answer = search(path+[v])
                if answer: return answer
    for start in range(10):
        answer = search([start])
        if answer: return answer
    raise AssertionError('no required path')


def family(length):
    n = length+9
    x = petersen(); del x[0,5]
    chain = [0]+list(range(10,n))+[5]
    for a,b in zip(chain,chain[1:]): x[edge(a,b)] = 2
    costs = [[0 if a==b else (1 if edge(a,b) in x else 10**6)
              for b in range(n)] for a in range(n)]
    for k in range(n):
        for a in range(n):
            for b in range(n):
                costs[a][b] = min(costs[a][b],costs[a][k]+costs[k][b])
    path,mid = base_path()
    i = next(i for i in range(9) if edge(path[i],path[i+1])==(0,5))
    internal = chain[1:-1]
    if path[i]==5: internal = internal[::-1]
    path = path[:i+1]+internal+path[i+1:]
    assert sorted(path)==list(range(n))
    assert all(costs[a][b]==1 for a,b in zip(path,path[1:]))
    assert costs[path[0]][path[-1]]==2
    return x,costs,path,mid


def minimum_matching(c,odd):
    @lru_cache(None)
    def solve(vertices):
        if not vertices: return 0,()
        a = vertices[0]
        choices = []
        for b in vertices[1:]:
            rest = tuple(v for v in vertices if v not in (a,b))
            value,pairs = solve(rest)
            choices.append((value+c[a][b],((a,b),)+pairs))
        return min(choices)
    return solve(tuple(sorted(odd)))


def shortcut(n,edges):
    adj = {v:[] for v in range(n)}
    for i,(a,b) in enumerate(edges):
        adj[a].append((b,i)); adj[b].append((a,i))
    used = set(); stack = [0]; reverse = []
    while stack:
        v = stack[-1]
        while adj[v] and adj[v][-1][1] in used: adj[v].pop()
        if adj[v]:
            w,i = adj[v].pop(); used.add(i); stack.append(w)
        else: reverse.append(stack.pop())
    assert len(used)==len(edges)
    seen = set(); tour = []
    for v in reversed(reverse):
        if v not in seen: seen.add(v); tour.append(v)
    assert len(tour)==n
    return tour


def main():
    rows = []
    for length in range(1,6):
        x,c,path,mid = family(length); n = len(c)
        assert sum(x.values())==2*n
        assert all(sum(w for e,w in x.items() if v in e)==4 for v in range(n))
        cuts = {}; minimum = 100
        for mask in range(1,1<<(n-1)):
            value = sum(w for (a,b),w in x.items() if ((mask>>a)&1)!=((mask>>b)&1))
            assert value>=4
            minimum = min(minimum,value)
            cuts[value] = cuts.get(value,0)+1
        assert minimum==4
        optimum,tour,work = exact_tour(c)
        assert optimum==n+1
        assert sum(c[path[i]][path[(i+1)%n]] for i in range(n))==optimum
        mst = prim(c,list(range(n)))
        degree = [sum(v in e for e in mst) for v in range(n)]
        odd = [v for v,d in enumerate(degree) if d%2]
        matching_cost,matching = minimum_matching(c,odd)
        christofides = shortcut(n,mst+list(matching))
        actual = sum(c[christofides[i]][christofides[(i+1)%n]] for i in range(n))
        rows.append({'subdivided_spoke_length':length,'n':n,
            'support_twice_x':[[a,b,w] for (a,b),w in sorted(x.items())],
            'costs':c,'lp_value':n,'lp_dual':'degree multipliers 1/2; all c_e>=1',
            'optimal_cost':optimum,'optimal_tour':tour,'rounding_path':path,
            'closing_two_hop_midpoint':mid,'gap':f'{n+1}/{n}',
            'exact_cut_capacity_histogram_twice_x':cuts,'min_cut_twice_x':minimum,
            'tight_cuts_up_to_complement':cuts[4],
            'mst_edges':mst,'mst_cost':n-1,'mst_odd_vertices':odd,
            'minimum_matching_edges':matching,'minimum_matching_cost':matching_cost,
            'tree_plus_parity_cost':n-1+matching_cost,
            'shortcut_tour':christofides,'shortcut_cost':actual,'subset_dp':work})
    result = {'status':'passed','family':'one-spoke Petersen subdivisions',
              'rows':rows,'scope':'exact bounded checks and all-size lemma; not worst-case support gaps'}
    (HERE/'CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','rows':[{k:r[k] for k in
          ('n','gap','tight_cuts_up_to_complement','minimum_matching_cost','shortcut_cost')}
          for r in rows]},indent=2))


if __name__=='__main__': main()
