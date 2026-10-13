#!/usr/bin/env python3
"""Bounded exact circuit axioms and root-lattice Ehrhart controls for A1."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def circuits(n):
    return [tuple(int(k == i)-int(k == j) for k in range(n))
            for i in range(n) for j in range(n) if i != j]


def circuit_axioms(c):
    c = set(c)
    assert (0,)*len(next(iter(c))) not in c
    assert all(tuple(-a for a in v) in c for v in c)
    support = {v: {i for i, a in enumerate(v) if a} for v in c}
    controls = 0
    for x, y in product(c, repeat=2):
        if support[x] <= support[y]:
            assert x == y or x == tuple(-a for a in y)
        if x == tuple(-a for a in y):
            continue
        for e, (a, b) in enumerate(zip(x, y)):
            if a != 1 or b != -1:
                continue
            positive = {i for i, (a, b) in enumerate(zip(x, y))
                        if i != e and (a == 1 or b == 1)}
            negative = {i for i, (a, b) in enumerate(zip(x, y))
                        if i != e and (a == -1 or b == -1)}
            assert any(all((a != 1 or i in positive) and
                           (a != -1 or i in negative)
                           for i, a in enumerate(z)) for z in c)
            controls += 1
    return controls


def literal_lattice_count(n, m):
    out = 0
    for prefix in product(range(-m, m+1), repeat=n-1):
        z = prefix+(-sum(prefix),)
        out += sum(max(a, 0) for a in z) <= m
    return out


def support_composition_count(n, m):
    out = 1
    for a in range(1, m+1):
        for positive in range(1, n):
            for negative in range(1, n-positive+1):
                out += (comb(n, positive)*comb(n-positive, negative)*
                        comb(a-1, positive-1)*comb(a-1, negative-1))
    return out


def numerator(counts, d):
    return [sum((-1)**j*comb(d+1, j)*counts[i-j]
                for j in range(i+1)) for i in range(d+1)]


def main():
    axioms, rows = 0, []
    for n in range(2, 10):
        c = circuits(n)
        axioms += circuit_axioms(c)
        face = [v for v in c if v[0] == 1]
        assert len(face) == n-1
        assert face == [tuple(int(k == 0)-int(k == j) for k in range(n))
                        for j in range(1, n)]
        assert all(sum(v) == 0 for v in c)
        d = n-1
        counts = [support_composition_count(n, m) for m in range(d+1)]
        if n <= 6:
            assert counts == [literal_lattice_count(n, m)
                              for m in range(d+1)]
        h = numerator(counts, d)
        assert h == [comb(d, k)**2 for k in range(d+1)]
        assert all(h[k]**2 > h[k-1]*h[k+1] for k in range(1, d))
        rows.append({'N': n, 'dimension': d, 'circuits': len(c),
                     'ehrhart_counts': counts, 'h_star': h,
                     'literal_box_control': n <= 6})
    # At N4 an exposed triangular face cannot be centrally symmetric:
    # reflection of a vertex in the centroid is not any face vertex.
    triangle = [v for v in circuits(4) if v[0] == 1]
    centroid3 = tuple(sum(v[k] for v in triangle) for k in range(4))
    assert all(tuple(2*s-3*a for s, a in zip(centroid3, v))
               not in [tuple(3*a for a in z) for z in triangle]
               for v in triangle)
    result = {'status': 'PASS', 'N_range': [2, 9],
        'literal_box_N_range': [2, 6], 'circuit_elimination_controls': axioms,
        'exact_rows': rows, 'actual_non_zonotope_N4_face': triangle,
        'lattice': 'sum(z)=0 saturated root lattice; delete-last-coordinate isomorphism',
        'full_target_outcome': 'one failed connected-zonotope reduction; full Q3678 unresolved',
        'all_size_proof': 'Q3678-ATTEMPTS.md#q3678-a1',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'CIRCUIT-A1-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'families': len(rows),
                      'circuit_elimination_controls': axioms,
                      'actual_triangular_face': triangle}, indent=2))


if __name__ == '__main__':
    main()
