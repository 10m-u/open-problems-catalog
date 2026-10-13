#!/usr/bin/env python3
"""Independent bounded controls for certificate, Haar and frontier reviews.

The matching oracle enumerates vertex-disjoint odd cycles and integral edges,
not the parent checker's full half-integral grid. Frontier equivalence is tested
by literal suffix enumeration with a key reconstructed from the selected graph.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from math import gcd
from pathlib import Path
import importlib.util
import json
import random
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def odd_cycles(n, edges):
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    cycles = set()
    for start in range(n):
        def visit(path):
            last = path[-1]
            if len(path) >= 3 and len(path) % 2 and start in adjacency[last]:
                if path[1] < last:
                    cycles.add(tuple(path))
            for nxt in adjacency[last]:
                if nxt > start and nxt not in path:
                    visit(path + [nxt])
        visit([start])
    return sorted(cycles)


def matching_vertices(n, edges):
    index = {e: i for i, e in enumerate(edges)}
    cycles = odd_cycles(n, edges)
    by_vertex = [[] for _ in range(n)]
    for cycle in cycles:
        for v in cycle:
            by_vertex[v].append(cycle)
    vertices = set()

    def visit(available, x):
        if not available:
            vertices.add(tuple(x))
            return
        v = min(available)
        visit(available - {v}, x)
        for u in sorted(available - {v}):
            e = tuple(sorted((u, v)))
            if e in index:
                nxt = x[:]
                nxt[index[e]] = 2
                visit(available - {u, v}, nxt)
        for cycle in by_vertex[v]:
            if set(cycle) <= available:
                nxt = x[:]
                for j, u in enumerate(cycle):
                    e = tuple(sorted((u, cycle[(j+1) % len(cycle)])))
                    nxt[index[e]] = 1
                visit(available - set(cycle), nxt)
    visit(set(range(n)), [0] * len(edges))
    return sorted(vertices)


def synthesize(n, edges, deficiency):
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    vertices = matching_vertices(n, edges)
    cutoff = n - deficiency + 1  # doubled objective threshold
    @lru_cache(None)
    def feasible(state):
        return any(sum(x) >= cutoff and all(s < 0 or x[i] == 2*s
                   for i, s in enumerate(state)) for x in vertices)
    @lru_cache(None)
    def proof(state):
        if not feasible(state):
            return 1, 0
        sizes, depths = [], []
        for i, s in enumerate(state):
            if s < 0:
                left = proof(state[:i] + (0,) + state[i+1:])
                right = proof(state[:i] + (1,) + state[i+1:])
                sizes.append(left[0] + right[0])
                depths.append(1 + max(left[1], right[1]))
        assert sizes
        return min(sizes), min(depths)
    leaves, depth = proof((-1,) * len(edges))
    return {'n': n, 'delta': deficiency, 'vertices_enumerated': len(vertices),
            'minimum_leaves': leaves, 'minimum_depth': depth,
            'proof_states': proof.cache_info().currsize}


def certificate_controls():
    normal_checks = 0
    for nscale in (4, 9, 20):
        witnesses = [F(nscale*j) + F(1, 2) for j in range(nscale+1)]
        for a, b in product(range(2-nscale, nscale-1), repeat=2):
            values = [a*x + b*j for j, x in enumerate(witnesses)]
            bins = {}
            for v in values:
                if v.denominator != 1:
                    key = v.numerator // v.denominator
                    bins[key] = bins.get(key, 0) + 1
            assert max(bins.values(), default=0) <= 1
            normal_checks += 1
        two_leaf = []
        for a, b in product(range(-nscale, nscale+1), repeat=2):
            if gcd(a, b) != 1:
                continue
            end = nscale * (a*nscale+b)
            lo = min(0, end) + min(F(a,3), F(2*a,3))
            hi = max(0, end) + max(F(a,3), F(2*a,3))
            threshold = lo.numerator // lo.denominator
            if threshold < lo <= hi < threshold+1:
                two_leaf.append((a, b, threshold))
        assert sorted(two_leaf) == [(-1, nscale, -1), (1, -nscale, 0)]
        for a, b in ((1,0), (1,-6*nscale), (1,6*nscale)):
            assert (F(a)*0 + F(b,2)).denominator == 1
        assert (F(1)+F(-1))/2 == 0 and (F(0)+F(-1))/2 == F(-1,2)
    rows = []
    cycle5 = [(i,(i+1)%5) for i in range(5)]
    bowtie = [(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]
    for n, edges, expected in [(5,cycle5,2),(5,bowtie,3)]:
        row = synthesize(n, edges, 1)
        assert row['minimum_leaves'] == expected
        rows.append(row)
    for q in range(1,4):
        friend = [(0,2*i+1) for i in range(q)]
        friend += [(0,2*i+2) for i in range(q)]
        friend += [(2*i+1,2*i+2) for i in range(q)]
        row = synthesize(2*q+1, friend, 1)
        assert (row['minimum_leaves'],row['minimum_depth']) == (q+1,q)
        rows.append(row)
        separate = [tuple(3*i+v for v in e) for i in range(q)
                    for e in ((0,1),(0,2),(1,2))]
        for delta, leaves in [(1,2),(q,2**q)]:
            row = synthesize(3*q, separate, delta)
            assert row['minimum_leaves'] == leaves
            rows.append(row)
    return {'restricted_normal_checks':normal_checks,
            'independent_matching_proofs':rows}


def haar(m, offsets):
    adjacency = [set() for _ in range(2*m)]
    for i in range(m):
        for s in offsets:
            j = m + (i+s) % m
            adjacency[i].add(j)
            adjacency[j].add(i)
    return adjacency


def component_sizes(adjacency):
    unseen = set(range(len(adjacency)))
    sizes = []
    while unseen:
        stack = [unseen.pop()]
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            found = adjacency[v] & unseen
            unseen.difference_update(found)
            stack.extend(found)
        sizes.append(size)
    return sorted(sizes)


def haar_controls():
    rows = []
    for primes in [(3,5,7), (3,5,7,11)]:
        m = 1
        for p in primes:
            m *= p
        offsets = [0] + [m//p for p in primes]
        assert component_sizes(haar(m,offsets)) == [2*m]
        arity = len(primes)-1
        for chosen in combinations(offsets,arity):
            g = m
            for a,b in combinations(chosen,2):
                g = gcd(g,b-a)
            assert g > 1
            assert component_sizes(haar(m,chosen)) == [2*m//g]*g
        rows.append({'m':m,'connected':True,'extraction_arity':arity,
                     'failed_selections':len(list(combinations(offsets,arity)))})
    switches = 0
    for m in (24,48):
        offsets = (0,1,4,10)
        differences = [(a-b)%m for a,b in permutations(offsets,2)]
        assert len(set(differences)) == len(differences)
        adjacency = haar(m,offsets)
        assert max((len(adjacency[u]&adjacency[v])
                    for u,v in combinations(range(m),2)),default=0) <= 1
        assert component_sizes(haar(m,(0,4))) == [m//2]*4
        cover = {(i,m+(i+s)%m) for i in range(m) for s in (0,4)}
        for (a,b),(c,d) in combinations(sorted(cover),2):
            if len({a,b,c,d}) < 4:
                continue
            assert not (d in adjacency[a] and b in adjacency[c])
            switches += 1
        assert component_sizes(haar(m,(0,1))) == [2*m]
    for p,q in [(3,5),(5,7)]:
        m = p*q
        assert component_sizes(haar(m,(0,p,q))) == [2*m]
        assert component_sizes(haar(q,(0,p%q))) == [2*q]
        assert component_sizes(haar(m,(0,p))) == [2*q]*p
    path = [0,5,3,8,2,7,1,6,4,9]
    adjacency = haar(5,(0,1,2))
    assert sorted(path) == list(range(10))
    assert all(v in adjacency[u] for u,v in zip(path,path[1:]))
    assert path[-1] not in adjacency[path[0]]
    return {'selection_controls':rows,'two_edge_switches_rejected':switches,
            'nonclosing_hamilton_path':path,'quotient_lift_controls':2}


def selected_graph(n, edges, mask):
    adjacency = [set() for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        if mask >> i & 1:
            adjacency[a].add(b)
            adjacency[b].add(a)
    return adjacency


def hamiltonian(n, edges, mask):
    adjacency = selected_graph(n,edges,mask)
    return all(len(a)==2 for a in adjacency) and component_sizes(adjacency)==[n]


def literal_equivalence(n, edges):
    first = {v:min(i for i,e in enumerate(edges) if v in e) for v in range(n)}
    last = {v:max(i for i,e in enumerate(edges) if v in e) for v in range(n)}
    tests, collisions, saturation_collisions = 0,0,0
    for cut in range(len(edges)+1):
        active = [v for v in range(n) if first[v] < cut <= last[v]]
        forgotten = [v for v in range(n) if last[v] < cut]
        future_degree = [sum(v in e for e in edges[cut:]) for v in range(n)]
        groups = {}
        for prefix in range(1<<cut):
            adjacency = selected_graph(n,edges[:cut],prefix)
            degrees = list(map(len,adjacency))
            if max(degrees)>2 or any(degrees[v]!=2 for v in forgotten):
                continue
            if any(degrees[v]+future_degree[v]<2 for v in range(n)):
                continue
            components, unseen = [],{v for v in range(n) if degrees[v]}
            while unseen:
                stack = [unseen.pop()]
                comp = set(stack)
                while stack:
                    found = adjacency[stack.pop()] & unseen
                    unseen.difference_update(found)
                    comp.update(found)
                    stack.extend(found)
                components.append(comp)
            closed = [c for c in components if all(degrees[v]==2 for v in c)]
            if closed:
                if closed != [set(range(n))]:
                    continue
                key, full = ('finished',),('finished',)
            else:
                pairings = []
                for comp in components:
                    endpoints = tuple(sorted(v for v in comp if degrees[v]==1))
                    assert len(endpoints)==2 and set(endpoints)<=set(active)
                    pairings.append(endpoints)
                degree_key = tuple(degrees[v] for v in active)
                key = degree_key,tuple(sorted(pairings))
                full = degree_key,tuple(sorted(tuple(sorted(c & set(active)))
                                              for c in components))
            groups.setdefault(key,[]).append((prefix,full))
        for histories in groups.values():
            if len(histories)<2:
                continue
            collisions += 1
            saturation_collisions += len({x[1] for x in histories})>1
            for suffix in range(1<<(len(edges)-cut)):
                values = [hamiltonian(n,edges,prefix | (suffix<<cut))
                          for prefix,_ in histories]
                assert len(set(values)) == 1
                tests += len(values)-1
    return {'n':n,'edges':len(edges),'collision_groups':collisions,
            'distinct_saturated_partitions':saturation_collisions,
            'literal_suffix_comparisons':tests}


def tour_oracle(costs, edges):
    n = len(costs)
    allowed = set(edges)
    best = None
    for perm in permutations(range(1,n)):
        if perm[0] > perm[-1]:
            continue
        tour = (0,)+perm
        chosen = [tuple(sorted((tour[i],tour[(i+1)%n]))) for i in range(n)]
        if all(e in allowed for e in chosen):
            value = sum(costs[a][b] for a,b in chosen)
            if best is None or value < best:
                best = value
    return best


def frontier_controls():
    spec = importlib.util.spec_from_file_location('review_hamilton',
                  HERE.parent/'residual-search'/'hamilton_dp.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    edges = list(combinations(range(5),2))
    instances = 0
    for mask in range(1<<len(edges)):
        allowed = [e for i,e in enumerate(edges) if mask>>i&1]
        costs = [[0]*5 for _ in range(5)]
        for a,b in edges:
            costs[a][b]=costs[b][a]=((a+1)*(b+3)+mask)%7
        reference = tour_oracle(costs,allowed)
        for kwargs in [{},{'drop_saturated':True},{'compress':False}]:
            result,_,_ = module.solve(costs,allowed,**kwargs)
            assert result == reference
        instances += 1
    schedules = [list(combinations(range(5),2)),list(combinations(range(6),2))]
    random.Random(82).shuffle(schedules[1])
    literal = [literal_equivalence(len({v for e in order for v in e}),order)
               for order in schedules]
    assert sum(x['distinct_saturated_partitions'] for x in literal)>0
    receipt = json.loads((HERE.parent/'residual-search'/'CHECK-RESULTS.json').read_text())
    rows = [r for r in receipt['rows'] if r['kind']=='certified_residual']
    assert len(rows)==16
    full = sum(r['frontier']['states'] for r in rows)
    reduced = sum(r['end_matching']['states'] for r in rows)
    assert (full,reduced)==(14808,13932)
    return {'all_five_vertex_graphs':instances,'literal_equivalence':literal,
            'checked_receipt_states':[full,reduced],
            'scope':'Nonnegative costs; bounded exact correctness, no speed claim.'}


def main():
    receipt = {'status':'passed','certificates':certificate_controls(),
               'haar':haar_controls(),'frontier':frontier_controls(),
               'scope':'Independent controls on failed intermediate routes and exact frontier quotient.'}
    (HERE/'FINAL-REVIEW-CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
