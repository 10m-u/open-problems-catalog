#!/usr/bin/env python3
"""Exact integer sign certificates for TP interpolation gap witnesses.

Generation uses Arb to propose brackets. Verification uses only integer
arithmetic, disjoint negative intervals and the intermediate value theorem.
"""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / 'GAP-CERTIFICATES.json'

def numerator(a, b, M):
    n = M + 4
    value = lambda k: (2*k+1)**M * ((b*k-b+a)*(b*k-b-a))**2
    values = [value(k) for k in range(n+1)]
    h = [sum((-1)**(j-k)*comb(n+1,j-k)*values[k]
             for k in range(j+1)) for j in range(n+1)]
    return h, value

def sign_at(h, x):
    """Sign of q^degree h(p/q), evaluated without rational division."""
    p, q = x.numerator, x.denominator
    acc, power = h[-1], q
    for c in reversed(h[:-1]):
        acc = acc*p + c*power
        power *= q
    return (acc > 0) - (acc < 0)

def generate(cases):
    from flint import ctx, fmpz_poly
    ctx.prec = 160
    out = []
    for a,b,M in cases:
        h,_ = numerator(a,b,M)
        assert min(h) > 0
        proposed = fmpz_poly(h).complex_roots()
        assert len(proposed) == len(h)-1
        intervals = []
        for root,m in proposed:
            assert m == 1 and root.imag == 0 and root.real < 0
            c = Fraction(str(root.real.mid().fmpq()))
            radius = abs(c)/2**40
            lo,hi = c-radius,c+radius
            assert sign_at(h,lo)*sign_at(h,hi) == -1
            intervals.append([str(lo),str(hi)])
        intervals.sort(key=lambda t:Fraction(t[0]))
        out.append({'a':a,'b':b,'M':M,'degree':M+4,
                    'gap':str(Fraction(2*a,b)),
                    'numerator_coefficients':[str(c) for c in h],
                    'negative_sign_change_intervals':intervals})
        print('generated',a,b,M,'intervals',len(intervals),flush=True)
    CERT.write_text(json.dumps({'certificates':out},indent=2)+'\n')

def verify():
    out = []
    for record in json.loads(CERT.read_text())['certificates']:
        a,b,M = (record[k] for k in ('a','b','M'))
        h,value = numerator(a,b,M)
        assert [str(c) for c in h] == record['numerator_coefficients']
        n = M+4
        assert len(h)-1 == n == record['degree'] and min(h)>0
        # Independent Newton-difference expression of the same numerator.
        values = [value(k) for k in range(n+1)]
        differences = []
        while values:
            differences.append(values[0])
            values = [y-x for x,y in zip(values,values[1:])]
        alternate = [sum(differences[j]*(-1)**(i-j)*comb(n-j,i-j)
                         for j in range(i+1)) for i in range(n+1)]
        assert alternate == h
        # Extra coefficient identity beyond the interpolation samples.
        for k in (n+1,n+2):
            assert value(k) == sum(h[j]*comb(n+k-j,n) for j in range(n+1))
        intervals = record['negative_sign_change_intervals']
        assert len(intervals) == n
        previous = None
        for x,y in intervals:
            lo,hi = Fraction(x),Fraction(y)
            assert lo < hi < 0 and (previous is None or previous < lo)
            assert sign_at(h,lo)*sign_at(h,hi) == -1
            previous = hi
        assert Fraction(record['gap']) == Fraction(2*a,b)
        assert 0 < a and 2*a < 3*b and Fraction(-1,2) < 1-Fraction(a,b)
        out.append({'a':a,'b':b,'M':M,'degree':n,'gap':record['gap'],
                    'exact_disjoint_negative_sign_changes':n,
                    'positive_coefficients':len(h),
                    'independent_newton_numerator':True})
    receipt = {'status':'PASS','certificates':out,
               'certificate_sha256':sha256(CERT.read_bytes()).hexdigest(),
               'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
               'scope':'Exact IVT certificates prove these bases in U_n. Their consecutive root gap is 2a/b. The base (a,b,M)=(7,5,32) disproves Q1443 with gap 14/5. Product closure also gives each fixed-gap family for every M at least its certified base.'}
    receipt_name = 'Q1443-COUNTEREXAMPLE-CHECK.json' if 'COUNTEREXAMPLE' in CERT.name else 'GAP-CHECK.json'
    (HERE/receipt_name).write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate',action='store_true')
    parser.add_argument('--largest',action='store_true')
    parser.add_argument('--counterexample',action='store_true')
    args = parser.parse_args()
    if args.counterexample:
        CERT = HERE/'Q1443-COUNTEREXAMPLE-CERTIFICATE.json'
    if args.generate:
        cases = [(7,5,32)] if args.counterexample else [(9,10,64),(19,20,96),(99,100,160),(999,1000,256)]
        if args.largest and not args.counterexample: cases.append((9999,10000,384))
        generate(cases)
    verify()
