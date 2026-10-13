#!/usr/bin/env python3
"""Actual rank-two realization, sign-circuit basis and saturated lattice."""
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json

from check_circuit_a1 import circuit_axioms

HERE = Path(__file__).resolve().parent


def sign_circuit(n, i, j, k):
    return tuple(int(a == i)-int(a == j)+int(a == k) for a in range(n))


def determinant(a):
    a = [list(r) for r in a]
    sign, last = 1, 1
    for k in range(len(a)-1):
        if not a[k][k]:
            j = next((j for j in range(k+1, len(a)) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                v = pivot*a[i][j]-a[i][k]*a[k][j]
                assert v % last == 0
                a[i][j] = v//last
            a[i][k] = 0
        last = pivot
    return sign*a[-1][-1]


def main():
    controls = []
    for n in range(4, 21):
        positive = [sign_circuit(n, i, j, k)
                    for i, j, k in combinations(range(n), 3)]
        for i, j, k in combinations(range(n), 3):
            coeff = (k-j, -(k-i), j-i)
            assert sum(coeff) == 0
            assert coeff[0]*i+coeff[1]*j+coeff[2]*k == 0
            assert coeff[0] > 0 and coeff[1] < 0 and coeff[2] > 0
        basis = [sign_circuit(n, 0, 1, 2), sign_circuit(n, 0, 1, 3),
                 sign_circuit(n, 0, 2, 3), sign_circuit(n, 1, 2, 3)]
        basis += [sign_circuit(n, 0, 1, j) for j in range(4, n)]
        det = determinant(basis)
        assert abs(det) == 1
        assert all(sum(v) == 1 for v in positive)
        axiom_count = None
        if n <= 6:
            signed = positive+[tuple(-a for a in v) for v in positive]
            axiom_count = circuit_axioms(signed)
        controls.append({'N': n, 'matrix_rank': 2,
                         'true_kernel_dimension': n-2,
                         'signed_circuit_span_dimension': n,
                         'unimodular_circuit_basis_determinant': det,
                         'circuit_elimination_controls': axiom_count})
    counts = [sum(sum(map(abs, z)) <= m for z in product(range(-m,m+1),repeat=4))
              for m in range(5)]
    h = [sum((-1)**j*comb(5,j)*counts[i-j] for j in range(i+1))
         for i in range(5)]
    assert h == [1,4,6,4,1]
    result = {
        'status': 'PASS', 'N_range': [4, 20], 'all_N_basis_controls': controls,
        'N4_actual_polytope': 'unimodular four-dimensional crosspolytope',
        'N4_h_star': h,
        'scope': 'All-size dimension/lattice obstruction to flow-kernel identification; full LC unresolved.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'CIRCUIT-A5-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','families':len(controls),
        'all_basis_determinants_have_absolute_value_one':True,
        'N4_h_star':h},indent=2))


if __name__ == '__main__':
    main()
