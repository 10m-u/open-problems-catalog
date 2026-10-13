"""Exact sparse derivatives, independent of the claimed source rank bounds."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import random


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for j in range(n + 1):
            for tail in compositions(n - j, k - 1):
                yield (j,) + tail


def derivative(poly, alpha):
    out = {}
    for mon, value in poly.items():
        if all(a <= b for a, b in zip(alpha, mon)):
            fac = product_factor(mon, alpha)
            out[tuple(b-a for a, b in zip(alpha, mon))] = value * fac
    return out


def product_factor(mon, alpha):
    result = 1
    for b, a in zip(mon, alpha):
        result *= factorial(b) // factorial(b-a)
    return result


def rank(rows):
    pivots = {}
    for raw in rows:
        row = {k: Fraction(v) for k, v in raw.items() if v}
        while row:
            p = min(row)
            if p not in pivots:
                scale = row[p]
                pivots[p] = {k: v/scale for k, v in row.items()}
                break
            scale = row[p]
            for k, v in pivots[p].items():
                w = row.get(k, 0) - scale*v
                if w:
                    row[k] = w
                elif k in row:
                    del row[k]
    return len(pivots)


def level_ranks(W, e, m):
    out = []
    for i in range(e+2):
        rows = []
        for alpha in compositions(i, m):
            rows.append({(j, mon): val for j, p in enumerate(W)
                         for mon, val in derivative(p, alpha).items()})
        out.append(rank(rows))
    return out


def hilbert(W, G, e, m):
    # All nonzero operators have at most one X derivative. No formula for
    # their ranks, no assumed block independence, and no source lower bound.
    q = len(W)
    F = {}
    for j, p in enumerate(W):
        x = tuple(int(k == j) for k in range(q))
        for mon, val in p.items():
            F[x + mon] = val
    for mon, val in G.items():
        F[(0,)*q + mon] = val
    out = []
    for i in range(e+2):
        rows = [derivative(F, (0,)*q + a) for a in compositions(i, m)]
        if i:
            for j in range(q):
                x = tuple(int(k == j) for k in range(q))
                rows.extend(derivative(F, x+a) for a in compositions(i-1, m))
        out.append(rank(rows))
    return out


def binary_plus_pure(e):
    return [{(e-j, j, 0): 1} for j in range(e+1)] + [{(0, 0, e): 1}]


def full_cubic_plus_pure(r):
    return [{mon+(0,): 1} for mon in compositions(3, r)] + [{(0,)*r+(3,): 1}]


def unimodal(h):
    return all(h[i] <= h[i+1] for i in range(len(h)//2))


def main():
    flat = []
    for e in range(3, 9):
        W = binary_plus_pure(e)
        G = {(0, 0, e+1): 1}
        h = hilbert(W, G, e, 3)
        rr = level_ranks(W, e, 3)
        assert rr == [1] + list(range(3, e+3)) + [0]
        assert h == [1] + [e+5]*e + [1]
        assert hilbert(W, {}, e, 3) == h
        # Literal directional derivative, including nongeneric directions.
        for direction in [(1, 1, 1), (2, -3, 5), (1, 0, 0), (0, 0, 1)]:
            rows = []
            for p in W:
                row = defaultdict(int)
                for k, b in enumerate(direction):
                    alpha = tuple(int(j == k) for j in range(3))
                    for mon, val in derivative(p, alpha).items():
                        row[mon] += b*val
                rows.append(row)
            assert rank(rows) <= e+1 < len(W)
        flat.append({"e": e, "h": h, "r": rr,
                     "claimed_minimum_h2": min(2*(e+2), 6+e+2,
                                               6+comb(e+1, 2))})
    quartic = []
    for r in range(3, 6):
        W = full_cubic_plus_pure(r)
        q = len(W)
        for rho in range(r+1):
            G = {(0,)*r+(4,): 1}
            for j in range(rho):
                G[tuple(2*int(j == k) for k in range(r))+(2,)] = 1
            h = hilbert(W, G, 3, r+1)
            expected = [1, q+r+1, 2*(comb(r+1, 2)+1)+rho, q+r+1, 1]
            assert h == expected
            assert unimodal(h) == (rho >= comb(r, 3))
            quartic.append({"r": r, "rank_Q": rho, "h": h})
    # Exact deformation into a maximal-rank nonunimodal degree-six form.
    rng = random.Random(2508)
    mons = list(compositions(5, 3))
    W0 = binary_plus_pure(5)
    W1 = [{a: rng.randrange(-5, 6) for a in mons} for _ in range(7)]
    expected_r = [1, 3, 6, 10, 15, 7, 0]
    assert level_ranks(W1, 5, 3) == expected_r
    deformation = []
    for t in [0, 1, 2, -1]:
        Wt = []
        for a, b in zip(W0, W1):
            Wt.append({mon: a.get(mon, 0)+t*b.get(mon, 0) for mon in mons})
        h = hilbert(Wt, {(0, 0, 6): 1}, 5, 3)
        rr = level_ranks(Wt, 5, 3)
        if t == 0:
            assert h == [1, 10, 10, 10, 10, 10, 1]
        else:
            assert rr == expected_r
            assert h == [1, 10, 21, 20, 21, 10, 1]
        deformation.append({"t": t, "r": rr, "h": h})
    result = {"result": "PASS", "scope": "exact derivative controls; all-size claims require proof",
              "flat_families": flat, "quartic_families": quartic,
              "degree6_deformation": deformation,
              "generic_quintic_basis": {"monomial_order": mons,
                                        "coefficients": [[p[a] for a in mons] for p in W1]},
              "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name('PERAZZO-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({"result": "PASS", "flat_controls": len(flat),
                      "quartic_controls": len(quartic), "deformations": len(deformation)}))


if __name__ == '__main__':
    main()
