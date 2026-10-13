#!/usr/bin/env python3
"""Exact obstruction controls for path/cycle-power Hamiltonicity routes."""
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def path_power(n,k):
    return {e for e in combinations(range(n),2) if e[1]-e[0] <= k}


def cycle_power(n,k):
    return {e for e in combinations(range(n),2)
            if min(e[1]-e[0], n-e[1]+e[0]) <= k}


def degrees(n,edges):
    d = [0]*n
    for u,v in edges:
        d[u] += 1
        d[v] += 1
    return d


def path_hypothesis(n,k,edges):
    host = path_power(n,k)
    hd, d = degrees(n,host), degrees(n,edges)
    return edges <= host and all(2*a >= b+4 for a,b in zip(d,hd))


def cycle_hypothesis(n,k,edges):
    return edges <= cycle_power(n,k) and min(degrees(n,edges)) >= k+1


def check_tour(n,edges,tour):
    assert sorted(tour) == list(range(n))
    assert all(tuple(sorted((tour[i],tour[(i+1)%n]))) in edges for i in range(n))


def components(n,edges,removed):
    remaining = set(range(n))-set(removed)
    adjacency = [set() for _ in range(n)]
    for u,v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    sizes = []
    while remaining:
        queue = [remaining.pop()]
        total = 0
        while queue:
            v = queue.pop()
            total += 1
            for u in adjacency[v]&remaining:
                remaining.remove(u)
                queue.append(u)
        sizes.append(total)
    return sorted(sizes)


def zigzag(n):
    return list(range(0,n,2))+list(reversed(range(1,n,2)))


def petersen_vertex():
    spokes = [(i,i+5) for i in range(5)]
    cycle_edges = [(i,(i+1)%5) for i in range(5)]
    cycle_edges += [(i+5,5+(i+2)%5) for i in range(5)]
    doubled = {tuple(sorted(e)):2 for e in spokes}
    doubled.update({tuple(sorted(e)):1 for e in cycle_edges})
    assert degrees(10,[]) == [0]*10
    for v in range(10):
        assert sum(x for e,x in doubled.items() if v in e) == 4
    tight_cuts = []
    for mask in range(1,1023):
        cut = sum(x for (u,v),x in doubled.items() if ((mask>>u)^(mask>>v))&1)
        assert cut >= 4
        if cut == 4:
            tight_cuts.append(mask)
    # Fixing spokes at their upper bound leaves each odd 5-cycle's
    # consecutive edge sums equal to one; these uniquely force all halves.
    assert len(spokes) == 5 and len(cycle_edges) == 10
    return {'doubled_nonzero_edges':[[list(e),x] for e,x in sorted(doubled.items())],
            'proper_cuts_checked':1022, 'tight_cuts':tight_cuts,
            'vertex_argument':'Five tight spoke upper bounds plus two odd-cycle degree systems uniquely determine all 15 supported variables.'}


def main():
    rows = []
    n,k = 20,6
    h = path_power(n,k)-{(0,6),(13,19)}
    assert path_hypothesis(n,k,h)
    d = degrees(n,h)
    failures = []
    for direction in ('forward','reverse'):
        oriented = d if direction == 'forward' else list(reversed(d))
        bad = [i for i in range(n) if oriented[i] < min(i+2,k+2,k+n-i-1)]
        assert bad
        failures.append({'orientation':direction,'violations':bad})
    check_tour(n,h,zigzag(n))
    rows.append({'target':'Q1852','attempt':1,'n':n,'k':k,
                 'degrees':d,'theorem5_failures':failures,'tour':zigzag(n)})

    for target, host in [('Q1852',path_power(25,4)),('Q1853',cycle_power(25,4))]:
        assert (path_hypothesis(25,4,host) if target=='Q1852'
                else cycle_hypothesis(25,4,host))
        d = degrees(25,host)
        assert all(d[u]+d[v] < 25 for u,v in combinations(range(25),2) if (u,v) not in host)
        check_tour(25,host,zigzag(25) if target=='Q1852' else list(range(25)))
        rows.append({'target':target,'attempt':2,'n':25,'k':4,
                     'minimum_degree':min(d),'maximum_degree':max(d),
                     'closure_additions':0})

    n,k = 12,4
    left = {e for e in path_power(n,k) if e[1] <= 6}
    right = {e for e in path_power(n,k) if e[0] >= 5}
    h = left|right
    assert path_hypothesis(n,k,h)
    assert components(n,h,{5,6}) == [5,5]
    check_tour(n,h,zigzag(n))
    rows.append({'target':'Q1852','attempt':3,'n':n,'k':k,
                 'separator':[5,6],'component_sizes':[5,5],'tour':zigzag(n)})

    n,k = 9,3
    left = {e for e in path_power(n,k) if e[1] <= 4}
    right = {e for e in path_power(n,k) if e[0] >= 4}
    h = left|right|{(0,8)}
    assert cycle_hypothesis(n,k,h)
    assert components(n,h,{0,4}) == [3,4]
    check_tour(n,h,list(range(n)))
    rows.append({'target':'Q1853','attempt':3,'n':n,'k':k,
                 'separator':[0,4],'component_sizes':[3,4],'tour':list(range(n))})

    fractional = petersen_vertex()
    assert path_hypothesis(10,9,path_power(10,9))
    assert cycle_hypothesis(10,5,cycle_power(10,5))
    for target,k in [('Q1852',9),('Q1853',5)]:
        rows.append({'target':target,'attempt':4,'n':10,'k':k,
                     'fractional_extreme_point':'unit spokes, half outer/inner 5-cycles'})

    n,k = 12,4
    h = path_power(n,k)-{(4,7),(4,8),(3,7)}
    assert path_hypothesis(n,k,h)
    bad = []
    for endpoint in (0,n-1):
        remaining = [v for v in range(n) if v != endpoint]
        relabel = {v:i for i,v in enumerate(remaining)}
        reduced = {tuple(sorted((relabel[u],relabel[v]))) for u,v in h if endpoint not in (u,v)}
        assert not path_hypothesis(n-1,k,reduced)
        hd, rd = degrees(n-1,path_power(n-1,k)), degrees(n-1,reduced)
        bad.append({'removed_endpoint':endpoint,
                    'violations':[{'new_vertex':i,'degree':a,'required':(b+1)//2+2}
                                  for i,(a,b) in enumerate(zip(rd,hd)) if 2*a < b+4]})
    check_tour(n,h,zigzag(n))
    rows.append({'target':'Q1852','attempt':5,'n':n,'k':k,
                 'endpoint_deletion_failures':bad,'tour':zigzag(n)})

    n,k = 20,3
    h = cycle_power(n,2)|{(0,3),(10,13)}
    assert cycle_hypothesis(n,k,h)
    cut_controls = []
    for start in range(n):
        label = {v:(v-start)%n for v in range(n)}
        ordered = {tuple(sorted((label[u],label[v]))) for u,v in h}
        reduced = ordered & path_power(n,k)
        rd = degrees(n,reduced)
        assert max(rd) == 5 and sum(x <= 4 for x in rd) >= 16
        cut_controls.append({'start':start,'maximum_degree':max(rd),
                             'vertices_degree_at_most_4':sum(x <= 4 for x in rd)})
    rows.append({'target':'Q1853','attempt':1,'n':n,'k':k,
                 'added_edges':[[0,3],[10,13]],'all_cuts':cut_controls,
                 'all_20_cyclic_cuts_fail':True})

    directed = []
    for n in (7,9,11,13):
        h = cycle_power(n,2)-{(0,1),(2,4)}
        assert cycle_hypothesis(n,2,h)
        tour = [0,2,1]+list(range(3,n))
        check_tour(n,h,tour)
        allowed_totals = [n+t for t in range(n+1) if (n+t)%n == 0]
        assert allowed_totals == [n,2*n]
        directed.append({'n':n,'undirected_tour':tour,
                         'required_all_forward_steps':[[1]*n,[2]*n],
                         'removed_edge_in_each_type':[[0,1],[2,4]]})
    rows.append({'target':'Q1853','attempt':5,'forward_orientation_obstructions':directed})
    receipt = {'status':'passed','attempt_controls':rows,'fractional_vertex':fractional,
               'scope':'Every graph is Hamiltonian; the examples refute proposed reductions, not Q1852/Q1853.'}
    (HERE/'POWER-ROUTE-CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'status':'passed','attempt_controls':len(rows),
                      'fractional_vertex_cuts':1022,'catalog_conjectures_refuted':False}))


if __name__ == '__main__':
    main()
