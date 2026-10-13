#!/usr/bin/env python3
"""Exact witnesses and formula controls; no extrapolation to Q4429."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
from itertools import product
import hashlib
import json
from check_hankel_tn2 import rows


def signs(a):
    return [(a[k]**2>a[k-1]*a[k+1])-(a[k]**2<a[k-1]*a[k+1])
            for k in range(2,len(a)-1)]


def advance(a,r,fam):
    n=len(a);p=r-1;b=[0]*(n+1)
    for k in range(1,n+1):
        top=n+p*k-1
        u=comb(top,p)*(factorial(p) if fam=='C' else 1)
        v=top if fam=='C' else k
        b[k]=u*a[k-1]+(v*a[k] if k<n else 0)
    return b


def ff(k,h):
    v=1
    for j in range(h):v*=k-j
    return v


def run():
    count=dict(actual_operator_witnesses=0,strict_normalized_LC_witnesses=0,
               actual_curvature_drops=0,fixed_excess_formula_entries=0)
    witnesses=[('C',6,[0,7,4,4,5,8],[0,70,2522580,7442000,25502525,85503840,311646720]),
               ('S',7,[0,6,3,3,4,7],[0,6,74262,302850,1425076,6492675,31474716])]
    for fam,r,a,b in witnesses:
        assert signs(a)==[-1,-1,-1]
        assert advance(a,r,fam)==b and signs(b)==[1,-1,1,-1]
        count['actual_operator_witnesses']+=1
        n=6;p=r-1
        W=[F(factorial(n+p*k),factorial(k)) for k in range(n+1)]
        h=[F(0),F(1),F(1)]
        for k in range(2,n):
            q=W[k]**2/(W[k-1]*W[k+1])
            assert 0<q<F(10,11)
            t=F(11,10) if k in [2,4] else 2/q
            h.append(h[k]**2/(h[k-1]*t))
        assert signs(h)==[1,1,1,1]
        assert signs([x*y for x,y in zip(W,h)])==[-1,1,-1,1]
        count['strict_normalized_LC_witnesses']+=1
        tab=rows(r,4,fam)
        q3=F(tab[3][2]**2,tab[3][1]*tab[3][3])
        q4=F(tab[4][2]**2,tab[4][1]*tab[4][3])
        expected=(F(5148,5831),F(762047,1012928)) if fam=='C' else (F(6435,10336),F(40625,69768))
        assert (q3,q4)==expected and q4<q3
        count['actual_curvature_drops']+=1
    # Fixed-excess finite partition identity used by both endpoint arguments.
    for r in range(1,9):
        for fam in ['C','S']:
            tab=rows(r,12,fam)
            g0=F(1,r if fam=='C' else factorial(r))
            for n in range(2,13):
                for t in range(1,min(4,n)):
                    k=n-t
                    z=F(0)
                    for ms in product(range(t+1),repeat=t):
                        if sum((i+1)*m for i,m in enumerate(ms))!=t:continue
                        ell=sum(ms)
                        term=F(ff(k,ell))
                        for j,m in enumerate(ms,1):
                            gj=F(1,r+j if fam=='C' else factorial(r+j))
                            term*=F(1,factorial(m))*(gj/g0)**m
                        z+=term
                    value=F(factorial(n+(r-1)*k),factorial(k))*g0**k*z
                    assert value==tab[n][k]
                    count['fixed_excess_formula_entries']+=1
    out=dict(schema='b3-row-pattern-controls-v1',date='2026-10-13',passed=True,
             counts=count,scope='Exact route witnesses and finite formula controls; asymptotics rest on written proof.',
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('ROW-PATTERN-CHECK-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':run()
