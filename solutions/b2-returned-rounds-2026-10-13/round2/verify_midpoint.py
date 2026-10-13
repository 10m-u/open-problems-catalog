#!/usr/bin/env python3
"""Exact finite controls for the all-dimensional midpoint proofs.

The dimension-free statements are proved in RESEARCH-NOTE.pdf; these checks
independently validate their finite incidence and quotient ingredients.
Requires only the Python standard library. Writes MIDPOINT-CHECKS.json.
"""
from __future__ import annotations
from collections import Counter, deque
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
import json

Point = tuple[int, ...]

def midpoint(x: Point, y: Point) -> Point:
    return tuple(-(a+b) % 3 for a,b in zip(x,y))

def geometry(n: int):
    points = list(product(range(3), repeat=n))
    index = {p:i for i,p in enumerate(points)}
    mid = [[index[midpoint(x,y)] for y in points] for x in points]
    return points, mid

def admissible(labels: tuple[int,...] | list[int], mid: list[list[int]]) -> bool:
    return all(labels[x] == 0 or labels[x] != labels[y] or labels[mid[x][y]] != 0
               for x,y in combinations(range(len(labels)),2))

def bipartite(remainder: set[int], mid: list[list[int]]) -> bool:
    colours = {}
    for seed in range(len(mid)):
        if seed in remainder or seed in colours:
            continue
        colours[seed] = 1
        queue = deque([seed])
        while queue:
            x = queue.popleft()
            for y in range(len(mid)):
                if x == y or y in remainder or mid[x][y] not in remainder:
                    continue
                if y not in colours:
                    colours[y] = 3 - colours[x]
                    queue.append(y)
                elif colours[y] == colours[x]:
                    return False
    return True

def closure(indices: set[int], mid: list[list[int]]) -> set[int]:
    out = set(indices)
    while True:
        larger = out | {mid[x][y] for x in out for y in out}
        if larger == out:
            return out
        out = larger

def plane_checks() -> dict:
    points, mid = geometry(2)
    cap_hist, admissible_hist = Counter(), Counter()
    for bits in range(1 << 9):
        r = {j for j in range(9) if bits >> j & 1}
        if any(mid[x][y] in r for x,y in combinations(r,2)):
            continue
        cap_hist[len(r)] += 1
        if bipartite(r,mid):
            admissible_hist[len(r)] += 1
    assert cap_hist == {0:1, 1:9, 2:36, 3:72, 4:54}
    assert admissible_hist == {0:1, 1:9, 2:36, 4:54}
    # Explicit triangle forced by the three-point remainder.
    index = {p:i for i,p in enumerate(points)}
    r = {index[x] for x in [(0,0),(1,0),(0,1)]}
    triangle = [index[x] for x in [(1,1),(1,2),(2,1)]]
    assert set(triangle).isdisjoint(r)
    assert {mid[x][y] for x,y in combinations(triangle,2)} == r
    return {'subsets_checked':512, 'cap_histogram':dict(cap_hist),
            'two_colour_cap_histogram':dict(admissible_hist),
            'three_point_triangle':'passed'}

def incidence_checks() -> dict:
    points, mid = geometry(3)
    normals = [v for v in points if any(v) and next(t for t in v if t) == 1]
    planes = [frozenset(i for i,p in enumerate(points)
                        if sum(a*b for a,b in zip(v,p)) % 3 == c)
              for v in normals for c in range(3)]
    assert len(set(planes)) == 39
    assert all(len(h) == 9 for h in planes)
    assert all(sum(i in h for h in planes) == 13 for i in range(27))
    assert all(sum(x in h and y in h for h in planes) == 4
               for x,y in combinations(range(27),2))
    triples = 0
    for x,y,z in combinations(range(27),3):
        if mid[x][y] == z:
            continue
        assert sum({x,y,z} <= h for h in planes) == 1
        triples += 1
    table = []
    allowed = []
    for s in range(13):
        n4 = F(comb(s,3),4)
        n2 = 4*comb(s,2)-6*n4
        n1 = 13*s-2*n2-4*n4
        n0 = 39-n1-n2-n4
        counts = [n0,n1,n2,n4]
        feasible = all(x >= 0 and x.denominator == 1 for x in counts)
        if feasible:
            allowed.append(s)
        table.append({'s':s, 'n0_n1_n2_n4':[str(x) for x in counts],
                      'nonnegative_integral':feasible})
    assert allowed == [0,1,2,4]
    assert table[4]['n0_n1_n2_n4'][-1] == '1'
    return {'planes':39, 'planes_per_point':13, 'planes_per_pair':4,
            'noncollinear_triples_checked':triples,
            'moment_feasible_sizes':allowed, 'moment_table':table}

def quotient_checks() -> dict:
    points, mid = geometry(2)
    normals = [(0,1),(1,0),(1,1),(1,2)]
    partitions = inherited = 0
    for labels in product(range(3),repeat=9):
        if not admissible(labels,mid):
            continue
        partitions += 1
        for v in normals:
            fibres = [[i for i,p in enumerate(points)
                       if sum(a*b for a,b in zip(v,p)) % 3 == c] for c in range(3)]
            options = []
            for fibre in fibres:
                outside = sorted({labels[x] for x in fibre if labels[x] != 0})
                options.append(outside or [0])
            # Enumerate every possible colour assignment produced by choosing
            # an arbitrary non-remainder representative in each partial fibre.
            for q in product(*options):
                assert all(q[x] == 0 or q[x] != q[y] or q[-(x+y)%3] != 0
                           for x,y in combinations(range(3),2))
                inherited += 1
    return {'labelled_partitions_tested':3**9,
            'admissible_partitions':partitions,
            'quotient_assignments_tested':inherited,
            'status':'passed'}

def embed(base_labels: dict[Point,int], ambient_dimension: int) -> dict[Point,int]:
    base_dim = len(next(iter(base_labels)))
    assert ambient_dimension >= base_dim
    output = {}
    for x in product(range(3),repeat=ambient_dimension):
        q = x[base_dim:]
        if not any(q):
            output[x] = base_labels[x[:base_dim]]
        else:
            output[x] = next(c for c in q if c)
    return output

def check_label_map(labels: dict[Point,int]) -> int:
    assert all(labels[x] == 0 or labels[x] != labels[y] or labels[midpoint(x,y)] != 0
               for x,y in combinations(labels,2))
    return comb(len(labels),2)

def construction_checks() -> dict:
    bases = [
        ({():0},1,0),
        ({():0},2,0),
        ({(0,):0,(1,):0,(2,):1},3,0),
    ]
    square = {x:(0 if all(x) else 1 if x[0] == 0 else 2)
              for x in product(range(3),repeat=2)}
    bases.append((square,3,0))
    cylinder = {x:square[x[:2]] for x in product(range(3),repeat=3)}
    bases.append((cylinder,4,1))
    examples = []
    pair_total = 0
    for base,n,expected_dim in bases:
        labels = embed(base,n)
        pair_total += check_label_map(labels)
        points, mid = geometry(n)
        r = {i for i,p in enumerate(points) if labels[p] == 0}
        if expected_dim == 0:
            assert all(mid[x][y] not in r for x,y in combinations(r,2))
        else:
            assert any(mid[x][y] in r for x,y in combinations(r,2))
            for triple in combinations(r,3):
                h = closure(set(triple),mid)
                assert len(h) < 9 or not h <= r
        examples.append({'ambient_dimension':n, 'remainder_size':len(r),
                         'density':str(F(len(r),3**n)),
                         'largest_affine_dimension':expected_dim})
    # Exhaustive midpoint checks for a two-block construction with two added
    # ambient coordinates. The all-k dimension and density statements use
    # the proof, not this test instance.
    k,b,c = 2,2,2
    labels = {}
    for x in product(range(3),repeat=k*b+c):
        if any(x[k*b:]):
            labels[x] = next(t for t in x[k*b:] if t)
        else:
            zero_blocks = [i for i in range(k) if not any(x[i*b:(i+1)*b])]
            labels[x] = zero_blocks[0]+1 if zero_blocks else 0
    block_pairs = check_label_map(labels)
    density_checks = []
    for k in range(2,101):
        b = 1
        while 3**b < 10*k:
            b += 1
        numerator = (3**b-1)**k
        denominator = 9*3**(b*k)
        assert 10*numerator >= denominator
        density_checks.append({'k':k,'b':b})
    return {'embedded_examples':examples,'embedded_midpoint_pairs_checked':pair_total,
            'block_test':{'k':2,'b':2,'added_codimension':2,
                          'points':len(labels),'midpoint_pairs_checked':block_pairs},
            'density_formula_integer_checks_k': [2,100],
            'density_formula_instances':len(density_checks)}

def negative_control() -> dict:
    # A two-colour example whose remainder and first colour both affinely span
    # F_3^3. It rules out an overstrong affine-span removal strategy.
    a = {(0,1,2),(0,2,2),(1,1,0),(1,2,1),(2,0,0),(2,0,1)}
    b = {x for x in product(range(3),repeat=3) if (x[1]+x[2])%3 == 2}
    assert a.isdisjoint(b)
    labels = {x:1 if x in a else 2 if x in b else 0
              for x in product(range(3),repeat=3)}
    check_label_map(labels)
    points,mid = geometry(3)
    r = {i for i,p in enumerate(points) if labels[p] == 0}
    ai = {i for i,p in enumerate(points) if labels[p] == 1}
    assert len(closure(r,mid)) == 27 == len(closure(ai,mid))
    assert all(len(closure(set(t),mid)) != 9 or not closure(set(t),mid) <= r
               for t in combinations(r,3))
    return {'status':'passed','A':[list(x) for x in sorted(a)],
            'B':[list(x) for x in sorted(b)],
            'R':[list(points[i]) for i in sorted(r)],
            'A_and_R_affinely_span_ambient':True,'R_contains_no_affine_plane':True}

def main() -> None:
    results = {'status':'passed','arithmetic':'integers and exact fractions',
               'scope':'Finite independent controls; general theorems use the manuscript proofs.',
               'plane':plane_checks(),'incidence':incidence_checks(),
               'quotient':quotient_checks(),'constructions':construction_checks(),
               'negative_control':negative_control()}
    path = Path(__file__).with_name('MIDPOINT-CHECKS.json')
    path.write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:v for k,v in results.items() if k in ('status','plane','quotient')},indent=2))
    print('Wrote',path.name)

if __name__ == '__main__':
    main()
