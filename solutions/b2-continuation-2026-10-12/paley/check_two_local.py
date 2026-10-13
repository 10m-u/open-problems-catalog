"""Exact two-local graph, cubic character and feasible-dual controls."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json
from pathlib import Path


def assert_psd(matrix):
    a = [[F(x) for x in row] for row in matrix]
    for i in range(len(a)):
        assert a[i][i] >= 0
        if a[i][i] == 0:
            assert all(a[i][j] == 0 for j in range(i+1, len(a)))
            continue
        pivot = a[i][i]
        for j in range(i+1, len(a)):
            for k in range(j, len(a)):
                value = a[j][k]-a[j][i]*a[i][k]/pivot
                a[j][k] = a[k][j] = value


def main():
    degree_controls = symmetry_controls = duals = 0
    p37 = None
    for p in [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109]:
        sq = {x*x % p for x in range(1, p)}
        chi = [0 if x == 0 else 1 if x in sq else -1 for x in range(p)]
        t = [x for x in range(p) if chi[x] == chi[(x-1) % p] == 1]
        assert len(t) == (p-5)//4
        h = [[int(x != y and chi[(x-y) % p] == -1) for y in t] for x in t]
        degrees = [sum(row) for row in h]
        for x, deg in zip(t, degrees):
            w = sum(chi[z]*chi[(z-1) % p]*chi[(z-x) % p] for z in range(p))
            assert w*w <= 4*p
            assert deg == (p-3-w)//8
            degree_controls += 1
        transforms = [lambda x: (1-x) % p, lambda x: pow(x, -1, p)]
        for transform in transforms:
            assert {transform(x) for x in t} == set(t)
            for i, x in enumerate(t):
                for j, y in enumerate(t):
                    assert h[i][j] == int(x != y and chi[(transform(x)-transform(y)) % p] == -1)
                    symmetry_controls += 1
        if t:
            # Rationally enlarged spectral/degree errors preserve the exact dual proof.
            upper_root = isqrt(p)+1
            n, b = len(t), F(p-3, 8)
            a, gamma = F(upper_root, 4), F(3*upper_root, 4)+F(1, 2)
            s = F(n)/(b+gamma)
            bound = s*(gamma+a)
            z = [[(bound if i == j else 0)+s*h[i][j]-1 for j in range(n)] for i in range(n)]
            assert_psd(z)
            duals += 1
        if p == 37:
            o = {4, 10, 12, 26, 28, 34}
            other = {11, 27}
            assert set(t) == o | other
            assert {x: sum(chi[(x-y) % p] == 1 for y in t) for x in t} == {
                x: (2 if x in o else 4) for x in t}
            assert 4*10 % p not in t
            b_matrix = [[int((x in o) != (y in o) and chi[(x-y) % p] == 1) for y in t] for x in t]
            i, j = t.index(4), t.index(11)
            comm = (int(4 in o)-int(11 in o))*b_matrix[i][j]
            assert comm == 1
            p37 = {'vertices': t, 'H_degrees': dict(zip(map(str, t), degrees)),
                   'S3_orbits': [sorted(o), sorted(other)], 'commutator_entry_4_11': comm}

    points = list(product([0, 1], repeat=2))
    masses = [F(-1, 8) if x == (1, 1) else F(3, 8) for x in points]
    assert sum(masses) == 1
    y1 = sum(w*x[0] for w, x in zip(masses, points))
    y12 = sum(w*x[0]*x[1] for w, x in zip(masses, points))
    assert y1 == F(1, 4) and y12 == F(-1, 8)
    square_controls = 0
    for c in product(range(-3, 4), repeat=3):
        assert sum(w*(c[0]+c[1]*x[0]+c[2]*x[1])**2 for w, x in zip(masses, points)) >= 0
        square_controls += 1
    assert_psd([[1, F(1, 4), F(1, 4)], [F(1, 4), F(1, 4), F(-1, 8)],
                [F(1, 4), F(-1, 8), F(1, 4)]])
    assert y12/y1 == F(-1, 2)
    assert F(3, 4) > F(1, 2)  # Squares of the two constants in A1.
    receipt = {'passed': True, 'exact_cubic_degree_controls': degree_controls,
               'projective_graph_symmetry_controls': symmetry_controls,
               'exact_rational_corrected_theta_duals': duals,
               'degree_two_signed_square_controls': square_controls,
               'degree_two_conditional_first_moment': '-1/2', 'p37_witness': p37,
               'scope': 'Finite exact controls of identities, invariant directions and corrected PSD duals; no asymptotic theta upper bound at the requested constant.'}
    Path(__file__).with_name('TWO-LOCAL-CHECK-RESULTS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
