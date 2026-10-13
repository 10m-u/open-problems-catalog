#!/usr/bin/env python3
"""Bounded actual-input screen for Q1249, with exact counterexample gate."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,random
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
def real_negative(c):
    while c and c[0]==0:c=c[1:]
    if len(c)<=2:return True
    roots=np.roots([float(x) for x in c[::-1]])
    return all(abs(z.imag)<1e-6*max(1,abs(z.real)) and z.real<0 for z in roots)
def a_coeff(q):
    c=[F(1),F(1)]
    for v in q:c.append(c[-1]*c[-1]/(c[-2]*v))
    return c
def b_coeff(n,zeros,poles):
    b=[F(1)]+[F(0)]*n
    for t in zeros:
        for j in range(n,0,-1):b[j]+=t*b[j-1]
    for t in poles:
        for j in range(1,n+1):b[j]+=t*b[j-1]
    return b
def main():
    rng=random.Random(1249);degrees={};accepted=0;tests=0;counter=None
    z=s.symbols('z')
    for trial in range(1800):
        n=rng.choice([5,6,7]);q=[F(rng.randrange(31,66),10) for _ in range(n-1)]
        q[-1]=F(rng.randrange(40,111),10)
        a=a_coeff(q)
        if all(v>=4 for v in q) or not all(real_negative(a[j:]) for j in range(n+1)):continue
        accepted+=1;degrees[n]=degrees.get(n,0)+1
        for _ in range(80):
            zeros=[F(rng.randrange(1,31),rng.randrange(1,8)) for _ in range(rng.randrange(0,5))]
            poles=[F(rng.randrange(1,31),rng.randrange(1,8)) for _ in range(rng.randrange(1,6))]
            b=b_coeff(n,zeros,poles);c=[a[j]*b[j] for j in range(n+1)];tests+=1
            if not real_negative(c):
                tails=[s.Poly(sum(s.Rational(v.numerator,v.denominator)*z**j
                         for j,v in enumerate(a[l:])),z) for l in range(n+1)]
                output=s.Poly(sum(s.Rational(v.numerator,v.denominator)*z**j
                               for j,v in enumerate(c)),z)
                if all(p.count_roots(-s.oo,0)==p.degree() for p in tails) \
                   and output.count_roots(-s.oo,0)<output.degree():
                    counter={'a':list(map(str,a)),'zeros':list(map(str,zeros)),
                         'poles':list(map(str,poles)),'output':list(map(str,c))}
                    break
        if counter:break
    receipt={'status':'EXACT_COUNTEREXAMPLE' if counter else 'BOUNDED_SCREEN_NO_COUNTEREXAMPLE',
      'a_trials':1800,'numerically_accepted_all_tail_inputs':accepted,
      'degrees':degrees,'actual_edrei_input_tests':tests,'counterexample':counter,
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Floating screening; any promoted counterexample passes exact all-tail/output root counts. No proof follows from a negative screen.'}
    (HERE/'SCREEN.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
