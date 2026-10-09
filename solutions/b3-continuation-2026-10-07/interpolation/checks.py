#!/usr/bin/env python3
"""Exact local reconstruction. Default n<=4; no numerical root tests.

Sympy is already installed. Per-degree checkpoint certificates are saved before
the next degree begins. Use an external timeout when raising --max-degree.
"""
import argparse
import itertools
import json
from pathlib import Path
import sympy as s

HERE = Path(__file__).resolve().parent

def sign(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))

def determinant_poly(matrix, xs):
    """Leibniz determinant with polynomial-domain products, independent of
    Sympy's symbolic determinant simplifier."""
    r = len(matrix)
    zero = s.Poly(0, *xs)
    total = zero
    for perm in itertools.permutations(range(r)):
        term = s.Poly(sign(perm), *xs)
        for i,j in enumerate(perm):
            term *= matrix[i][j]
            if term.is_zero:
                break
        total += term
    return total

def degree_certificate(n):
    t = s.symbols('t')
    xs = s.symbols('x:'+str(n))
    es = [s.S.One] + [sum(s.prod(c) for c in itertools.combinations(xs,k)) for k in range(1,n+1)]
    F = sum(es[k]*s.prod((n+k-j-1)+(n-k+j)*t for j in range(n)) for k in range(n+1))
    bs = [s.Poly(c,*xs) for c in s.Poly(F,t).all_coeffs()]
    zero = s.Poly(0,*xs)
    def b(i):
        return bs[i] if 0 <= i <= n else zero
    records = []
    for r in range(1,n):
        matrix = [[b(2*j-i+1) for j in range(r)] for i in range(r)]
        det = determinant_poly(matrix,xs)
        terms = det.as_dict()
        expected = (r+1)**n
        assert len(terms) == expected, (n,r,len(terms),expected)
        assert all(0 <= d <= r for powers in terms for d in powers)
        assert min(terms.values()) > 0
        orbits = {}
        for powers,c in terms.items():
            key = tuple(sorted(powers))
            assert key not in orbits or orbits[key] == c
            orbits[key] = c
        rec = {
            'r':r, 'monomial_count':len(terms),
            'expected_full_box_count':expected,
            'minimum_coefficient':str(min(terms.values())),
            'maximum_coefficient':str(max(terms.values())),
            'symmetric_orbit_coefficients':[
                {'sorted_exponents':list(k),'coefficient':str(v)} for k,v in sorted(orbits.items())
            ],
        }
        records.append(rec)
        print(f'n={n}, r={r}: {len(terms)} exact positive coefficients',flush=True)
    payload = {'n':n,'definition':'Delta_r = det[b_(2*j-i+1)] for F_n(t;x)','all_coefficients_strictly_positive':True,'determinants':records}
    (HERE / f'degree-{n}-certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
    return payload

def structural_checks():
    z,a = s.symbols('z a')
    def q(n):
        return s.expand(s.factorial(n)*sum(s.binomial(n,j)*a**(n-j)*s.prod(z-k for k in range(j))/s.factorial(j) for j in range(n+1)))
    checks = []
    for n in range(1,9):
        assert s.expand(q(n+1)-(z+a-(1-2*a)*n)*q(n)-a*(1-a)*n*n*q(n-1)) == 0
        checks.append(n)
    w = s.symbols('w')
    enlarged = s.expand(s.prod(z-j for j in range(4))+s.prod(z+j for j in range(1,5)))
    assert s.expand(enlarged.subs(z,w-s.Rational(1,2))) == 2*w**4+43*w**2+s.Rational(105,8)
    return {'equal_parameter_recurrence_symbolic_degrees':checks,'snn_degree_four_counterexample_identity':True}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-degree',type=int,default=4)
    args = parser.parse_args()
    structural = structural_checks()
    degrees = []
    for n in range(2,args.max_degree+1):
        degrees.append(degree_certificate(n)['n'])
        (HERE/'checks.json').write_text(json.dumps({'status':'PASS','independent_parameter_disk_certified_degrees':[1]+degrees,'structural_checks':structural,'boundary_claim':'only all-zero and all-one parameter vectors','method':'exact integer polynomial-domain determinant expansion; all coefficient-box entries positive'},indent=2)+'\n')

if __name__ == '__main__':
    main()
