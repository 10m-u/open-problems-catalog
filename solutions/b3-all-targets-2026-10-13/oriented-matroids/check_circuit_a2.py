#!/usr/bin/env python3
"""Complete exact facet/lattice construction for cographic 8--10-edge cases.

Every potential facet is obtained from every affinely independent d-tuple
of vertices, so no floating hull or unverified facet completeness is used.
"""
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, gcd
from functools import reduce
from pathlib import Path
import json

from check_circuit_a1 import circuit_axioms

HERE = Path(__file__).resolve().parent


def connected(subset, edges):
    if not subset:
        return False
    seen = {min(subset)}
    while True:
        nxt = seen | {v for a, b in edges for u, v in [(a, b), (b, a)]
                      if u in seen and v in subset}
        if nxt == seen:
            return seen == subset
        seen = nxt


def bonds(n, edges):
    points, signed = [], []
    vertices = set(range(n))
    for mask in range(1, (1 << n)-1):
        s = {j for j in range(n) if mask >> j & 1}
        if not connected(s, edges) or not connected(vertices-s, edges):
            continue
        p = tuple(int(j in s)-int(n-1 in s) for j in range(n-1))
        c = tuple(int(a in s)-int(b in s) for a, b in edges)
        points.append(p)
        signed.append(c)
    assert len(set(points)) == len(points)
    return points, signed


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def complete_facets_4(points):
    facets = set()
    for selected in combinations(points, 4):
        diffs = [[b-a for a, b in zip(selected[0], v)] for v in selected[1:]]
        normal = [(-1)**j*det3([[a for k, a in enumerate(r) if k != j]
                              for r in diffs]) for j in range(4)]
        if not any(normal):
            continue
        g = reduce(gcd, map(abs, normal))
        normal = [a//g for a in normal]
        b = sum(a*v for a, v in zip(normal, selected[0]))
        if not b:
            continue  # origin is interior, so it is not a supporting plane
        if b < 0:
            normal, b = [-a for a in normal], -b
        key = tuple(normal)+(b,)
        if key in facets:
            continue
        if all(sum(a*x for a, x in zip(normal, v)) <= b for v in points):
            facets.add(key)
    return sorted(facets)


def count_lattice(m, facets):
    return sum(all(sum(a*x for a, x in zip(f[:-1], z)) <= m*f[-1]
                   for f in facets)
               for z in product(range(-m, m+1), repeat=4))


def main():
    n = 5
    all_edges = list(combinations(range(n), 2))
    missing_cases = [[], [(0, 1)], [(0, 1), (0, 2)], [(0, 1), (2, 3)]]
    cases = []
    for missing in missing_cases:
        edges = [e for e in all_edges if e not in missing]
        points, signed = bonds(n, edges)
        axiom_controls = circuit_axioms(signed)
        facets = complete_facets_4(points)
        assert facets and all(f[-1] >= 1 for f in facets)
        counts = [count_lattice(m, facets) for m in range(5)]
        h = [sum((-1)**j*comb(5, j)*counts[i-j] for j in range(i+1))
             for i in range(5)]
        defects = [h[i]**2-h[i-1]*h[i+1] for i in range(1, 4)]
        assert all(x >= 0 for x in h)
        cases.append({'n': n, 'edges': edges, 'missing': missing,
                      'circuit_vectors': signed, 'potential_vertices': points,
                      'complete_primitive_facet_inequalities': facets,
                      'ehrhart_counts_0_to_4': counts, 'h_star': h,
                      'log_concavity_defects': defects,
                      'circuit_elimination_controls': axiom_controls})
    assert cases[0]['h_star'] == [1, 26, 66, 26, 1]
    # Exactly the four isomorphism types among all labelled five-vertex graphs
    # with at least eight edges; this does not inflate the attempt count.
    counts_by_type = [0]*4
    for size in range(8, 11):
        for chosen in combinations(all_edges, size):
            missing = set(all_edges)-set(chosen)
            if not missing:
                ix = 0
            elif len(missing) == 1:
                ix = 1
            else:
                a, b = missing
                ix = 2 if set(a) & set(b) else 3
            assert connected(set(range(5)), chosen)
            counts_by_type[ix] += 1
    assert counts_by_type == [1, 10, 30, 15]
    result = {'status': 'PASS', 'construction_outcome':
        'All rows pass; no full-target counterexample or asymptotic theorem.',
        'number_of_actual_isomorphism_types': len(cases),
        'labelled_graphs_covered': sum(counts_by_type),
        'labelled_multiplicities': counts_by_type,
        'already_known_complete_graph_family_counts_zero_new_attempts': True,
        'lattice': 'anchored integer potentials; saturated gradient lattice',
        'cases': cases,
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'CIRCUIT-A2-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'labelled_graphs': sum(counts_by_type),
        'rows': [c['h_star'] for c in cases],
        'minimum_defect': min(x for c in cases for x in c['log_concavity_defects'])}, indent=2))


if __name__ == '__main__':
    main()
