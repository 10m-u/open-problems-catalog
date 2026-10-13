#!/usr/bin/env python3
"""Independent factorial-moment catalecticants and restricted-kernel audit.

No imports from the root checker. Full ranks use integer elimination, while
annihilator kernels use separate rational RREF. Matrix entries are coefficient
times monomial factorial, rather than a list of differentiated polynomials.
"""
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import product
from math import comb, factorial, gcd, lcm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def mons(d, m):
    if d < 0:
        return []
    if m == 1:
        return [(d,)]
    return [(k,)+a for k in range(d+1) for a in mons(d-k, m-1)]


def moment(poly, alpha):
    return poly.get(alpha, 0)*reduce(lambda x, y: x*y,
                                   (factorial(a) for a in alpha), 1)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def integer_pivots(matrix):
    """Forward fraction-free row elimination, normalizing by integer gcd."""
    pivots, original_rows = {}, []
    for ix, raw in enumerate(matrix):
        denom = lcm(*(getattr(x, 'denominator', 1) for x in raw))
        row = {j: int(x*denom) for j, x in enumerate(raw) if x}
        for p, pivot in pivots.items():
            if p not in row:
                continue
            a, b = pivot[p], row[p]
            keys = row.keys() | pivot.keys()
            row = {j: a*row.get(j, 0)-b*pivot.get(j, 0) for j in keys}
            row = {j: v for j, v in row.items() if v}
            g = reduce(gcd, map(abs, row.values()), 0)
            if g > 1:
                row = {j: v//g for j, v in row.items()}
        if row:
            p = min(row)
            g = reduce(gcd, map(abs, row.values()), 0)
            pivots[p] = {j: v//g for j, v in row.items()}
            original_rows.append(ix)
    return list(pivots), original_rows


def rank(matrix):
    return len(integer_pivots(matrix)[0])


def determinant(matrix):
    a = [list(r) for r in matrix]
    n = len(a)
    if not n:
        return 1
    sign, last = 1, 1
    for k in range(n-1):
        if not a[k][k]:
            j = next((j for j in range(k+1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                value = a[i][j]*p-a[i][k]*a[k][j]
                assert value % last == 0
                a[i][j] = value//last
            a[i][k] = 0
        last = p
    return sign*a[-1][-1]


def kernel(matrix, width):
    a = [list(map(Fraction, r)) for r in matrix]
    pivots, row_ix = [], 0
    for col in range(width):
        j = next((j for j in range(row_ix, len(a)) if a[j][col]), None)
        if j is None:
            continue
        a[row_ix], a[j] = a[j], a[row_ix]
        scale = a[row_ix][col]
        a[row_ix] = [x/scale for x in a[row_ix]]
        for j in range(len(a)):
            if j != row_ix and a[j][col]:
                scale = a[j][col]
                a[j] = [x-scale*y for x, y in zip(a[j], a[row_ix])]
        pivots.append(col)
        row_ix += 1
    result = []
    for col in sorted(set(range(width))-set(pivots)):
        v = [Fraction(0)]*width
        v[col] = 1
        for j, p in enumerate(pivots):
            v[p] = -a[j][col]
        assert all(sum(x*y for x, y in zip(r, v)) == 0 for r in matrix)
        result.append(v)
    return result


def w_map(W, e, m, i):
    domain = mons(i, m)
    rows = [[moment(p, add(a, b)) for a in domain]
            for p in W for b in mons(e-i, m)]
    return rows, domain


def hilbert(W, G, e, m):
    """Pair all potentially nonzero operators with complementary operators."""
    q, d = len(W), e+1
    F = {(tuple(int(k == j) for k in range(q))+a): v
         for j, p in enumerate(W) for a, v in p.items()}
    F.update({(0,)*q+a: v for a, v in G.items()})

    def operators(i):
        return ([(0,)*q+a for a in mons(i, m)] +
                [tuple(int(k == j) for k in range(q))+a
                 for j in range(q) for a in mons(i-1, m)])

    h = []
    for i in range(d+1):
        matrix = [[moment(F, add(a, b)) for b in operators(d-i)]
                  for a in operators(i)]
        h.append(rank(matrix))
    return h


def pairing_formula(W, G, e, m):
    d = e+1
    kernels, domains, r = [], [], []
    for i in range(d+1):
        a, domain = w_map(W, e, m, i)
        j = kernel(a, len(domain))
        assert len(domain)-len(j) == rank(a)
        kernels.append(j)
        domains.append(domain)
        r.append(rank(a))
    correction = []
    for i in range(d+1):
        pairing = [[sum(x*y*moment(G, add(a, b))
                        for x, a in zip(v, domains[i]) if x
                        for y, b in zip(w, domains[d-i]) if y)
                    for w in kernels[d-i]] for v in kernels[i]]
        correction.append(rank(pairing))
    assert correction == correction[::-1]
    return [r[i]+r[d-i]+correction[i] for i in range(d+1)], r, correction


def flat(e):
    return [{(e-j, j, 0): 1} for j in range(e+1)] + [{(0, 0, e): 1}]


def direction_rank(W, e, direction):
    m = len(direction)
    matrix = []
    for p in W:
        row = []
        for a in mons(e-1, m):
            row.append(sum(b*(a[k]+1)*p.get(
                tuple(v+int(j == k) for j, v in enumerate(a)), 0)
                           for k, b in enumerate(direction)))
        matrix.append(row)
    return rank(matrix)


def main():
    recorded = json.loads((HERE/'PERAZZO-CHECK.json').read_text())
    flat_controls, directions = [], 0
    for e in range(3, 9):
        W, G = flat(e), {(0, 0, e+1): 1}
        h = hilbert(W, G, e, 3)
        expected, r, correction = pairing_formula(W, G, e, 3)
        assert h == expected == [1]+[e+5]*e+[1]
        assert not any(correction)
        ranks = [direction_rank(W, e, b)
                 for b in [(1, 1, 1), (2, -3, 5), (1, 0, 0), (0, 0, 1)]]
        assert ranks[:2] == [e+1, e+1]
        assert all(x <= e+1 < len(W) for x in ranks)
        directions += len(ranks)
        assert h == recorded['flat_families'][e-3]['h']
        flat_controls.append({'e': e, 'h': h, 'r': r, 'directional_ranks': ranks})

    quartics = []
    for rvar in range(3, 6):
        m = rvar+1
        W = [{a+(0,): 1} for a in mons(3, rvar)] + [{(0,)*rvar+(3,): 1}]
        for rho in range(rvar+1):
            G = {(0,)*rvar+(4,): 1}
            for j in range(rho):
                G[tuple(2*int(j == k) for k in range(rvar))+(2,)] = 1
            h = hilbert(W, G, 3, m)
            formula, rr, correction = pairing_formula(W, G, 3, m)
            assert h == formula == [1, len(W)+m,
                2*(comb(rvar+1, 2)+1)+rho, len(W)+m, 1]
            assert correction == [0, 0, rho, 0, 0]
            assert (h[2] >= h[1]) == (rho >= comb(rvar, 3))
            quartics.append({'r': rvar, 'rank_Q': rho, 'h': h,
                             'restricted_pairing_ranks': correction})

    coefficients = recorded['generic_quintic_basis']
    order = list(map(tuple, coefficients['monomial_order']))
    W1 = [dict(zip(order, row)) for row in coefficients['coefficients']]
    W0 = flat(5)
    deformations, minors = [], []
    for t in [0, 1, 2, -1]:
        W = [{a: p.get(a, 0)+t*q.get(a, 0) for a in order}
             for p, q in zip(W0, W1)]
        G = {(0, 0, 6): 1}
        h = hilbert(W, G, 5, 3)
        formula, rr, correction = pairing_formula(W, G, 5, 3)
        assert h == formula
        assert not any(correction)
        if t:
            assert rr == [1, 3, 6, 10, 15, 7, 0]
            assert h == [1, 10, 21, 20, 21, 10, 1]
        else:
            assert h == [1, 10, 10, 10, 10, 10, 1]
        deformations.append({'t': t, 'h': h, 'r': rr})
        if t == 1:
            for i in range(1, 6):
                matrix, domain = w_map(W, 5, 3, i)
                columns, rows = integer_pivots(matrix)
                minor = [[matrix[j][k] for k in columns] for j in rows]
                det = determinant(minor)
                assert det != 0
                minors.append({'level': i, 'rank': len(rows),
                    'operator_monomials': [domain[k] for k in columns],
                    'row_indices': rows, 'determinant_at_t1': str(det)})

    h = [1, 8, 8, 8, 1]
    gamma = [1, h[1]-4, h[2]-6-2*(h[1]-4)]
    assert gamma == [1, 4, -6]
    result = {
        'status': 'PASS',
        'independent_method': 'factorial-moment catalecticants; integer elimination; rational annihilator kernels',
        'flat_families': flat_controls,
        'directional_map_controls': directions,
        'rank_Q_quartic_controls': quartics,
        'actual_deformations': deformations,
        'generic_stratum_nonzero_minor_certificates': minors,
        'source_minimum_h2': 10, 'actual_quartic_h2': 8,
        'flat_quartic_gamma': gamma,
        'all_size_analytical_scope': 'PERAZZO-INDEPENDENT-REVIEW.md',
        'reviewed_sha256': {f: sha256((HERE/f).read_bytes()).hexdigest()
            for f in ['DERIVATIVE-RANKS.md', 'Q2508-ATTEMPTS.md',
                      'check_perazzo.py', 'PERAZZO-CHECK.json']},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'PERAZZO-REVIEW-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'flat_controls': len(flat_controls),
        'quartic_controls': len(quartics), 'deformation_controls': len(deformations),
        'nonzero_generic_minor_certificates': len(minors), 'gamma': gamma}, indent=2))


if __name__ == '__main__':
    main()
