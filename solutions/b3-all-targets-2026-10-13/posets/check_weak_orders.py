#!/usr/bin/env python3
from pathlib import Path
from math import comb
from hashlib import sha256
import sympy as sp,json
HERE=Path(__file__).resolve().parent
t=sp.Symbol('t')
def main():
    cases=0;examples=[]
    for N in range(1,25):
        for k in range(N//2+1):
            b=N-k;x=t+sp.Rational(b-1,2)
            Q0=sp.Integer(1);Q1=2*x
            if k==0:Q=Q0
            elif k==1:Q=Q1
            else:
                for r in range(1,k):Q0,Q1=Q1,sp.expand(2*x*Q1+r*(r+b)*Q0)
                Q=Q1
            pref=sp.prod(t+s for s in range(b))
            direct=sum(comb(k,j)*sp.prod(t+s for s in range(-j,N-j)) for j in range(k+1))
            assert sp.expand(direct-pref*Q)==0
            coeffs=sp.Poly(direct,t).all_coeffs()
            assert all(c>=0 for c in coeffs)
            cases+=1
            if (N,k) in [(2,1),(4,2),(6,3),(10,5)]:
                examples.append({'N':N,'k':k,'factorization':str(sp.factor(direct))})
    receipt={'status':'PASS','exact_factor_and_recurrence_controls':cases,
       'N_range':[1,24],'k_range':'0,...,floor(N/2)','examples':examples,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Bounded exact controls for a separately proved all-size weak-order theorem; not all width-two posets.'}
    (HERE/'WEAK-ORDER-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
