#!/usr/bin/env python3
"""Exact finite transcription controls for the all-parameter pairing proof."""
from fractions import Fraction as F
from math import comb, factorial
from itertools import combinations
from pathlib import Path
import hashlib
import json


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i+j] += u*v
    return c


def sub(a, b):
    c = [0] * max(len(a), len(b))
    for i, u in enumerate(a): c[i] += u
    for i, u in enumerate(b): c[i] -= u
    while len(c) > 1 and c[-1] == 0: c.pop()
    return c


def rows(r, nmax, family):
    p = r-1
    t = [[1]]
    for n in range(1, nmax+1):
        row = [0] * (n+1)
        for k in range(1, n+1):
            top = n+p*k-1
            u = comb(top, p) * (factorial(p) if family == 'C' else 1)
            v = top if family == 'C' else k
            row[k] = u*t[-1][k-1] + (v*t[-1][k] if k < n else 0)
        t.append(row)
    return t


def assembly(r, n, k, family):
    if not k: return int(n == 0)
    e = n-k
    atom = [F(1, r+j if family == 'C' else factorial(r+j)) for j in range(e+1)]
    power = [F(1)]
    for _ in range(k): power = mul(power, atom)[:e+1]
    v = power[e]*F(factorial(n+(r-1)*k), factorial(k))
    assert v.denominator == 1
    return v.numerator


def coefficient(r, n, k, birth, family):
    if birth:
        return comb(n+(r-1)*k-1, r-1) * (factorial(r-1) if family == 'C' else 1)
    return n+(r-1)*k-1 if family == 'C' else k


def run():
    counts = dict(assembly_entries=0, normalization_defects=0,
                  triangle_minors=0, paired_terms=0, recurrence_differences=0,
                  arbitrary_gap_hankel_minors=0)
    params = [1,2,3,4,5,6,7,11,16,32]
    for r in params:
        p = r-1
        for fam in ['C','S']:
            tab = rows(r, 18, fam)
            for n in range(9):
                for k in range(n+1):
                    assert tab[n][k] == assembly(r,n,k,fam)
                    counts['assembly_entries'] += 1
            # Rational identities used in the all-r normalized-row induction.
            for n in range(2,15):
                for k in range(1,n):
                    N = n+p*k
                    Q = N*N*(N-p)*(N+p)
                    c = lambda h: F(h,n+p*h)
                    d = lambda h: F(n+p*h-1,n+p*h)
                    assert d(k)**2-d(k-1)*d(k+1) == F(p*p*(2*N-1),Q)
                    assert c(k)**2-c(k-1)*c(k+1) == F(n*(2*N-n),Q)
                    assert 2*c(k)*d(k)-c(k-1)*d(k+1)-c(k+1)*d(k-1) == F(2*p*((n+1)*N-n),Q)
                    counts['normalization_defects'] += 3
            # T2 across arbitrary numerical rows/columns, including zero column.
            for m,n in combinations(range(10),2):
                am = tab[m]+[0]*(10-len(tab[m]))
                an = tab[n]+[0]*(10-len(tab[n]))
                for i,j in combinations(range(10),2):
                    assert am[i]*an[j]-am[j]*an[i] >= 0
                    counts['triangle_minors'] += 1
            # Individual PAIR contributions and the expansion identity E.
            for m,n in combinations(range(10),2):
                am = tab[m]+[0]*(n+1-len(tab[m]))
                an = tab[n]
                expanded = [0]*(m+n+2)
                for birth in [False,True]:
                    h = lambda z,k: coefficient(r,z+1,k+int(birth),birth,fam)
                    shift = int(birth)
                    for i in range(n+1):
                        diag = am[i]*an[i]*(h(n,i)-h(m,i))
                        assert diag >= 0
                        if diag: expanded[2*i+shift] += diag
                        for j in range(i+1,n+1):
                            w,z = am[i]*an[j],am[j]*an[i]
                            d1,d2 = h(n,j)-h(m,i),h(n,i)-h(m,j)
                            assert w >= z >= 0 and d1 >= 0 and d1+d2 >= 0
                            pair = w*d1+z*d2
                            assert pair == (w-z)*d1+z*(d1+d2) >= 0
                            if pair: expanded[i+j+shift] += pair
                            counts['paired_terms'] += 1
                got = sub(mul(tab[m],tab[n+1]),mul(tab[m+1],tab[n]))
                assert sub(got,expanded) == [0]
                assert all(v >= 0 for v in got)
                counts['recurrence_differences'] += 1
            for I in combinations(range(10),2):
                for J in combinations(range(10),2):
                    a = I[0]+J[0]
                    u,v = sorted([I[1]-I[0],J[1]-J[0]])
                    got = sub(mul(tab[a],tab[a+u+v]),mul(tab[a+u],tab[a+v]))
                    telescoped = [0]
                    for t in range(u):
                        piece = sub(mul(tab[a+t],tab[a+u+v-t]),
                                    mul(tab[a+t+1],tab[a+u+v-t-1]))
                        assert all(x >= 0 for x in piece)
                        telescoped = sub(telescoped,[-x for x in piece])
                    assert got == telescoped and all(x >= 0 for x in got)
                    counts['arbitrary_gap_hankel_minors'] += 1
    out = dict(schema='b3-hankel-tn2-controls-v1',date='2026-10-13',passed=True,
               r_values=params,counts=counts,
               scope='Finite identity/sign controls; universal theorem rests on HANKEL-TN2.md.',
               checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    dest = Path(__file__).with_name('HANKEL-TN2-CHECK-RESULTS.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__ == '__main__': run()
