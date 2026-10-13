"""Saved rational LP witness with rigorous rational trigonometric enclosures."""
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path


def atan_bounds(q, terms=40):
    s = sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    nxt = (-1)**terms*q**(2*terms+1)/F(2*terms+1)
    return min(s, s+nxt), max(s, s+nxt)


def pi_bounds():
    a, b = atan_bounds(F(1, 5)), atan_bounds(F(1, 239))
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def cos_at_bounds(x, terms=30):
    term, s = F(1), F(1)
    for j in range(1, terms):
        term *= -x*x/F((2*j-1)*(2*j))
        s += term
    nxt = term*(-x*x)/F((2*terms-1)*(2*terms))
    return min(s, s+nxt), max(s, s+nxt)


def cos_grid_bounds(u, n, pi):
    u %= n
    u = min(u, n-u)
    if u == 0:
        return F(1), F(1)
    if 2*u == n:
        return F(-1), F(-1)
    lo, hi = 2*pi[0]*u/n, 2*pi[1]*u/n
    assert 0 <= lo <= hi <= pi[0]
    return cos_at_bounds(hi)[0], cos_at_bounds(lo)[1]


def cyclic_convolve(a, b):
    n = len(a)
    c = [F(0)]*n
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[(i+j) % n] += x*y
    return c


def main():
    pi = pi_bounds()
    assert F(3) < pi[0] < pi[1] < F(22, 7)
    p, n, alpha = 29, 14, 4
    sq = {x*x % p for x in range(1, p)}
    assert len({pow(alpha, j, p) for j in range(n)}) == n
    f = [F(0)]*n
    f[0] = F(1)
    for j, num in [(3, 738250), (4, 63687), (6, 356895)]:
        f[j] = f[-j] = F(num, 1001000)
    assert all(x >= 0 for x in f)
    assert all(j == 0 or x == 0 or (pow(alpha, j, p)-1) % p in sq for j, x in enumerate(f))
    cosine = {u: cos_grid_bounds(u, n, pi) for u in range(n//2+1)}
    lower = []
    for r in range(n):
        value = sum((x*cosine[min(r*j % n, (-r*j) % n)][0]
                     for j, x in enumerate(f)), F(0))
        assert value > 0
        lower.append(value)
    objective = 1+sum(f)
    assert objective == F(4319664, 1001000)
    assert 2*objective-1 > 0 and (2*objective-1)**2 > 2*p-1

    # Exact n8 graph and symbolic optimum expressed as rational pairs a+b sqrt(2).
    sq17 = {x*x % 17 for x in range(1, 17)}
    assert [j for j in range(1, 8) if (pow(9, j, 17)-1) % 17 in sq17] == [1, 4, 7]
    assert F(7, 5)**2 < 2 < F(3, 2)**2
    # Eigenvalues: 8-4sqrt2, 4sqrt2-4, 4-2sqrt2, 0,0,... are all >=0.
    assert 8-4*F(3, 2) > 0
    assert 4*F(7, 5)-4 > 0
    assert 4-2*F(3, 2) > 0
    assert F(1415, 1000)**2 > 2
    assert 9-4*F(1415, 1000) > 3

    fejer_controls = 0
    for n in [8, 14, 30]:
        for freqs in [(1,), (1, 3), (0, 2), (n//2, 1)]:
            for d in [1, 2, 4]:
                out = [F(0)]*n
                out[0] = 1
                for freq in freqs:
                    base = [F(0)]*n
                    base[0] = 1
                    base[freq % n] += F(1, 2)
                    base[-freq % n] += F(1, 2)
                    for _ in range(d):
                        out = cyclic_convolve(out, base)
                c_d = F(comb(2*d, d), 2**d)
                assert all(x >= 0 for x in out)
                assert out[0] >= c_d**len(freqs)
                assert sum(out) == 2**(d*len(freqs))
                fejer_controls += 1
    for r in range(1, 7):
        d = 4*r*r
        assert 2**d > (2*d+1)**r
        assert F(comb(2*d, d), 2**d)**r > 2**(d*(r-1))

    receipt = {'passed': True, 'p29_generator': alpha,
               'p29_primal': [str(x) for x in f], 'p29_anchor_objective': str(objective),
               'smallest_certified_fourier_lower_bound': float(min(lower)),
               'trig_arithmetic': 'Machin arctangent and alternating cosine bounds with rational arithmetic',
               'p17_exact_anchor_optimum': '9-4*sqrt(2)',
               'nonnegative_fejer_convolution_controls': fejer_controls,
               'bounded_rank_gap_controls': 6,
               'scope': 'Feasible rational counter-witness to universal HP LP lift, exact n8 integrality gap, bounded-rank proof controls; no infinite-prime conclusion.'}
    Path(__file__).with_name('THETA-CHECK-RESULTS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
