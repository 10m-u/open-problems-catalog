"""Controls for research/quick-closures.md, section 3 (Martinez 2013, Conjectures 6.100-6.105).

theta_n = i cot(pi/2n) = (1 + z)/(1 - z) with z = exp(i pi / n).  Its minimal polynomial is
P_n(x) = c (x+1)^phi(2n) Phi_2n((x-1)/(x+1)), c = 1/Phi_2n(1) (Mobius image of the cyclotomic
polynomial, hence irreducible of degree phi(2n)).  Checks, n <= 60:
  * theta_n is a root and P_n has integer coefficients (monic);
  * 6.100: delta_{n,1} + prod of conjugates == lcm(odd <= n) / lcm(odd <= n-1);
  * 6.104(a): P_n == sum_k C(n,2k) x^(phi-2k) for n an odd prime or a power of two;
  * 6.104(b): for n > 1 not an odd prime power: P_n even, monic, P(+-1) a power of 2;
    palindromic exactly when n is even (the 'reflexive' reading that fails for odd n);
  * 6.105: for 2 <= n, m <= 16, the Galois orbit of -cot(pi/2n)cot(pi/2m) under (Z/2L)^x
    (L = lcm(n,m)) equals the claimed root set {k <= L : gcd(k, 2nm) = 1} and has size
    phi(2nm) / (2 gcd(n,m)).
Writes martinez-cot-checks.json.
"""
import json
import pathlib
from functools import reduce
from math import gcd, lcm

import mpmath as mp
import sympy as sp

OUT = pathlib.Path(__file__).with_name("martinez-cot-checks.json")
mp.mp.dps = 80
x = sp.symbols('x')


def odd_lcm(m):
    return reduce(lcm, range(1, m + 1, 2), 1)


def minpoly(n):
    ph = int(sp.totient(2 * n))
    a = sp.Poly(sp.cyclotomic_poly(2 * n, x), x).all_coeffs()[::-1]   # a[j] = coeff of z^j
    xm, xp = sp.Poly(x - 1, x), sp.Poly(x + 1, x)
    P = sp.Poly(0, x)
    for j, c in enumerate(a):
        if c:
            P += c * xm ** j * xp ** (ph - j)
    return P.monic(), ph


def main():
    issues, notes = [], {"palindromic_fails_at": [], "checked_n": 60}
    for n in range(1, 61):
        P, ph = minpoly(n)
        co = [sp.Rational(c) for c in P.all_coeffs()]
        if not all(c.q == 1 for c in co):
            issues.append(("non-integer", n))
        if n > 1:
            th = mp.mpc(0, mp.cot(mp.pi / (2 * n)))
            val = mp.polyval([mp.mpf(int(c)) for c in co], th)
            if abs(val) > mp.mpf(10) ** -40 * max(abs(int(c)) for c in co) * max(1, abs(th)) ** ph:
                issues.append(("not-a-root", n))
        norm = (-1) ** ph * co[-1]
        lhs = 1 if n == 1 else norm
        if lhs != sp.Rational(odd_lcm(n), odd_lcm(n - 1)):
            issues.append(("6.100", n, str(lhs)))
        f = sp.factorint(n)
        odd_prime_power = n > 1 and n % 2 == 1 and len(f) == 1
        if (n % 2 == 1 and sp.isprime(n)) or (n & (n - 1)) == 0:
            F = [sp.binomial(n, j) if j % 2 == 0 else 0 for j in range(ph + 1)]
            if co != F:
                issues.append(("6.104a", n))
        elif not odd_prime_power:
            even = all(c == 0 for c in co[1::2])
            v1, vm1 = sum(co), sum(c * (-1) ** (ph - i) for i, c in enumerate(co))
            pow2 = v1 == vm1 and v1 > 0 and (int(v1) & (int(v1) - 1)) == 0
            if not (even and pow2):
                issues.append(("6.104b", n, even, str(v1)))
            if co != co[::-1]:
                notes["palindromic_fails_at"].append(n)
    res = []
    for n in range(2, 17):
        for m in range(2, 17):
            L = lcm(n, m)
            orbit = {mp.nstr(-mp.cot(mp.pi * k / (2 * n)) * mp.cot(mp.pi * k / (2 * m)), 50)
                     for k in range(1, 2 * L) if gcd(k, 2 * L) == 1}
            claimed = {mp.nstr(-mp.cot(mp.pi * k / (2 * n)) * mp.cot(mp.pi * k / (2 * m)), 50)
                       for k in range(1, L + 1) if gcd(k, 2 * n * m) == 1}
            ncl = sum(1 for k in range(1, L + 1) if gcd(k, 2 * n * m) == 1)
            deg = sp.Rational(int(sp.totient(2 * n * m)), 2 * gcd(n, m))
            if not (orbit == claimed and len(orbit) == deg == ncl):
                res.append((n, m, len(orbit), str(deg), ncl, orbit == claimed))
    out = {"issues_6_100_6_104": issues, "notes": notes, "6_105_mismatches_2_to_16": res}
    OUT.write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
