#!/usr/bin/env python3
"""Parent audit: distinct enumeration and exact symbolic/definition controls.

Written proofs supply infinite quantifiers. This script audits formulas and
the completeness of the finite interval certificate; it does not infer new
infinite theorems from finite cases.
"""
from collections import deque
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations
from math import factorial, prod
from pathlib import Path
import json
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def interval_audit(n):
    """Breadth-first closure, rather than the branch's generator-by-generator DP."""
    masks = set()
    for lo in range(n):
        for hi in range(lo + 1, n + 1):
            size = hi - lo
            for bound in range(size % 2, size, 2):
                mask = 0
                for word in range(2**n):
                    count = sum((word >> i) & 1 for i in range(lo, hi))
                    if abs(2*count-size) <= bound:
                        mask |= 1 << word
                masks.add(mask)
    cube = (1 << 2**n) - 1
    seen, queue = {cube}, deque([cube])
    while queue:
        family = queue.popleft()
        for predicate in masks:
            new = family & predicate
            if new not in seen:
                seen.add(new)
                queue.append(new)
    q = n // 2
    equalities = 0
    for family in seen:
        counts = [0] * (n+1)
        for word in range(2**n):
            if family & (1 << word):
                counts[word.bit_count()] += 1
        slack = q*counts[q] - (q+1)*counts[q-1]
        assert slack >= 0
        equalities += slack == 0
    digest = sha256(('\n'.join(format(f, 'x') for f in sorted(seen))+'\n').encode()).hexdigest()
    branch = next(r for r in json.loads((ROOT/'compositions/checks.json').read_text())['exhaustive_certificates'] if r['dimension'] == n)
    assert len(seen) == branch['distinct_nonempty_families']
    assert digest == branch['sorted_family_hex_sha256']
    assert equalities == branch['equality_cases']
    return {'dimension': n, 'families': len(seen), 'equalities': equalities,
            'family_set_sha256': digest, 'matched_branch': True}


def stirling_audit():
    r, B, T, U, y = s.symbols('r B T U y')
    f = [1, y, r*y+B*y**2,
         r*(r+1)*y+2*r*(2*r+1)*B*y**2/(r+1)+T*y**3,
         r*(r+1)*(r+2)*y+2*r*(2*r+1)*(3*r*r+6*r+2)*B*y**2/((r+1)*(r+2))
         +3*r*(3*r+1)*T*y**3/(r+1)+U*y**4]
    A = 7*r**4+20*r**3+9*r*r-8*r-4
    D = 4*r**4+6*r**3-14*r*r-16*r-4
    E = 5*r**4+16*r**3+19*r*r+8*r
    expected = [0,0,r*r*(r+1),r*(B*(5*r**4+8*r**3+5*r*r+8*r+4)-(r**3+5*r*r+8*r+4))/((r+1)*(r+2)),
                r*(A*T-D*B*B-E*B)/((r+1)**2*(r+2)),
                r*(B*B*(5*r+1)+B*T*(r-1)-T*(7*r+1)+U*(r+1))/(r+1),
                B*U-T*T-B**3+2*B*T-U]
    p = s.Poly(s.Matrix([[f[i+j] for j in range(3)] for i in range(3)]).det(), y)
    assert p.degree() == 6
    for j, c in enumerate(expected):
        assert s.factor(p.nth(j)-c) == 0
    assert s.expand(5*A-3*D-E) == 18*r**4+66*r**3+68*r*r-8
    assert s.expand(3*(3*r+1)*(3*r+2)-4*(2*r+1)**2) == 11*r*r+11*r+2
    # Gamma-product moment consecutive ratios, without numerical integration.
    for rr in range(2,10):
        for nn in range(6):
            gamma_ratio = Q(rr**(rr-1),factorial(rr-1))*prod(Q(nn*rr+j,rr) for j in range(1,rr))
            factorial_ratio = Q(prod(rr*nn+j for j in range(1,rr+1)),(nn+1)*factorial(rr))
            assert gamma_ratio == factorial_ratio
    return {'symbolic_determinant_coefficients': 7, 'factorial_bound_identities': True,
            'gamma_moment_ratio_controls': 48, 'passed': True}


def det_integer(matrix):
    # Literal determinant of small integer matrices: no symbolic polynomial code.
    n = len(matrix)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               *prod(matrix[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def interpolation_audit():
    checked = 0
    definition_checks = 0
    for n in range(2,6):
        payload = json.loads((ROOT/f'interpolation/degree-{n}-certificate.json').read_text())
        vectors = [(0,)*n, (1,)*n, tuple(range(n)), tuple((2*i+1)%4 for i in range(n))]
        for xs in vectors:
            es = [1]+[sum(prod(xs[i] for i in chosen) for chosen in combinations(range(n),k)) for k in range(1,n+1)]
            ascending = [0]*(n+1)
            for k in range(n+1):
                row = [1]
                for j in range(n):
                    c,d = n+k-j-1,n-k+j
                    new = [0]*(len(row)+1)
                    for i,v in enumerate(row):
                        new[i] += c*v
                        new[i+1] += d*v
                    row = new
                for i,v in enumerate(row):
                    ascending[i] += es[k]*v
            bs = list(reversed(ascending))
            def b(i):
                return bs[i] if 0<=i<=n else 0
            for record in payload['determinants']:
                rr = record['r']
                actual = det_integer([[b(2*j-i+1) for j in range(rr)] for i in range(rr)])
                certificate = 0
                for orbit in record['symmetric_orbit_coefficients']:
                    certificate += int(orbit['coefficient'])*sum(prod(x**d for x,d in zip(xs,exponents))
                        for exponents in set(permutations(orbit['sorted_exponents'])))
                assert actual == certificate
                checked += 1
            # Independently check the Cayley transform against original P,
            # not the branch's Bernoulli-shift formula for F.
            aa = [Q(x,1+x) for x in xs]
            ee = [Q(1)]+[sum(prod(aa[i] for i in chosen) for chosen in combinations(range(n),k)) for k in range(1,n+1)]
            for t in (Q(-2),Q(-1),Q(0),Q(1,3),Q(2)):
                z = Q(-1,2)+Q(2*n-1,2)*(1+t)/(1-t)
                P = sum(ee[n-j]*prod(z-l for l in range(j))/factorial(j) for j in range(n+1))
                transformed = factorial(n)*prod(1+x for x in xs)*(1-t)**n*P
                assert transformed == sum(v*t**i for i,v in enumerate(ascending))
                definition_checks += 1
    return {'integer_determinant_vs_certificate_evaluations': checked,
            'original_P_vs_Cayley_F_exact_controls': definition_checks,
            'passed': True, 'policy': 'Coefficient positivity itself is exhaustively regenerated by interpolation/checks.py.'}


def main():
    result = {'schema': 'b3-parent-independent-audit-v1', 'date': '2026-10-07',
              'interval_breadth_first_audit': [interval_audit(n) for n in (2,4,6,8)],
              'stirling_symbolic_audit': stirling_audit(),
              'interpolation_definition_and_certificate_audit': interpolation_audit(),
              'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(), 'passed': True}
    (HERE/'independent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed': True, 'output': str(HERE/'independent_checks.json')}))


if __name__ == '__main__':
    main()
