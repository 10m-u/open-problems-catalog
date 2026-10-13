#!/usr/bin/env python3
"""Bounded exact-coefficient search for an actual rectangular counterexample."""
from fractions import Fraction
from functools import reduce
from hashlib import sha256
import json
from math import lcm
from pathlib import Path
import random
from flint import ctx, fmpz_poly

HERE=Path(__file__).resolve().parent

def elementary(roots):
    p=[Fraction(1)]
    for r in roots:
        q=p+[Fraction(0)]
        for k in range(1,len(q)):q[k]+=r*p[k-1]
        p=q
    return p

def falling(x,k):
    result=Fraction(1)
    for j in range(k):result*=x-j
    return result

def rectangular(ep,eq,alpha):
    m=len(ep)-1
    scale=[falling(m,k)*falling(m+alpha,k) for k in range(m+1)]
    return [scale[k]*sum(ep[i]*eq[k-i]/(scale[i]*scale[k-i])
                        for i in range(k+1)) for k in range(m+1)]

def main():
    ctx.prec=128
    rng=random.Random(3437)
    alphas=[Fraction(-99,100),Fraction(-9,10),Fraction(-3,4),
            Fraction(-1,2),Fraction(-1,4),Fraction(1,4),Fraction(3,2)]
    counts=[];bad=[]
    for m in range(3,13):
        checked=0
        for iteration in range(120):
            alphabet=[0,1,1,2,3,8,25,100]
            pp=[rng.choice(alphabet) for _ in range(m)]
            qq=[rng.choice(alphabet) for _ in range(m)]
            ep,eq=elementary(pp),elementary(qq)
            for alpha in alphas:
                e=rectangular(ep,eq,alpha)
                denominator=lcm(*(v.denominator for v in e))
                coefficients=[int(v*denominator)*(-1)**k for k,v in enumerate(e)]
                roots=fmpz_poly(coefficients[::-1]).complex_roots()
                if any(not root.imag.contains(0) or root.real.upper()<0 for root,mult in roots):
                    bad.append({'m':m,'alpha':str(alpha),'p_roots':pp,'q_roots':qq,
                                'output_elementary':[str(v) for v in e]})
                    break
                assert sum(mult for root,mult in roots)==m
                checked+=1
            if bad:break
        counts.append({'m':m,'cases':checked})
        print('m',m,'checked',checked,'counterexamples',len(bad),flush=True)
        if bad:break
    result={'status':'COUNTEREXAMPLE_CANDIDATE' if bad else 'NO_COUNTEREXAMPLE_FOUND',
            'seed':3437,'alphas':[str(a) for a in alphas],'counts':counts,
            'candidates':bad,'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Bounded search with exact coefficients and Arb root enclosures; no all-size proof. A candidate requires independent exact verification.'}
    (HERE/'RECTANGULAR-SCREEN.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
