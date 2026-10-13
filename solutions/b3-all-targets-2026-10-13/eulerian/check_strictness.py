#!/usr/bin/env python3
"""Exact controls for the new strictness argument; no finite-to-infinite claim."""
from functools import lru_cache
from itertools import product
from math import ceil, prod
from pathlib import Path
import json
import sympy as S

X=S.symbols('x')
HERE=Path(__file__).resolve().parent


@lru_cache(None)
def refined(v):
    if not v:return (S.Poly(1,X),)
    if len(v)==1:return (S.Poly(1,X),)+(S.Poly(X,X),)*(v[0]-1)
    prev=refined(v[:-1]);a,b=v[-2:];f=sum(prev,S.Poly(0,X))
    return tuple((X*sum(prev[:(j*a+b-1)//b],S.Poly(0,X))+
                 sum(prev[(j*a+b-1)//b:],S.Poly(0,X))).as_poly(X)
                 for j in range(b))


def total(v):return sum(refined(v),S.Poly(0,X))


def literal(v):
    c=[0]*(len(v)+1)
    for e in product(*(range(s) for s in v)):
        a,b,d=0,1,0
        for f,g in zip(e,v):d+=a*g<f*b;a,b=f,g
        c[d]+=1
    return S.Poly.from_list(list(reversed(c)),X)


def main():
    tested=identity=literal_controls=0
    for n in range(1,6):
        for v in product(range(2,7),repeat=n):
            f=total(v);p=total(v[:-1])
            assert f.TC()==1 and f.eval(1)==prod(v)
            assert S.degree(S.gcd(f,f.diff()))==0
            assert S.degree(S.gcd(f,p))==0
            assert S.polys.polytools.count_roots(f,-S.oo,0)==f.degree()
            tested+=1
            if n<=3:assert f==literal(v);literal_controls+=1
            if n>=2:
                a,b=v[-2:];fs=refined(v[:-1]);prefix=S.Poly(0,X);parts=S.Poly(0,X)
                ws=[b+(X-1)*(b-1-i*b//a) for i in range(a)]
                for i in range(a-1):
                    prefix+=fs[i];parts+=(ws[i+1]-ws[i])*prefix
                assert (ws[-1]*p-parts).as_poly(X)==f
                assert (ws[-1]-ws[0]).expand()==(1-X)*((a-1)*b//a)
                identity+=1
    constructions=0
    for d in range(1,8):
        for u in range(1,8):
            v=tuple([u+1,1]*(d-1)+[u+1])
            assert total(v)==S.Poly((1+u*X)**d,X)
            assert len(v)==2*d-1;constructions+=1
    # Unit separation explains why the nonunit hypothesis is needed.
    assert total((2,1,2))==S.Poly((1+X)**2,X)
    out=dict(status='passed',nonunit_vectors_checked=tested,
        exact_prefix_gcd_and_root_counts=tested,literal_definition_controls=literal_controls,
        weighted_summation_by_parts_identities=identity,sharp_length_constructions=constructions,
        unit_separator_repeated_root_control=True,
        scope='Exact bounded controls of the written all-size proof; no full coloured Q1262 closure.')
    (HERE/'STRICTNESS-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
