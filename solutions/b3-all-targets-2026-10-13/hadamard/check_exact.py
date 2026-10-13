#!/usr/bin/env python3
"""Exact controls for Q1249 route obstructions and single-pole identity."""
import sympy as s
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
def main():
    z=s.symbols('z');A=1+z+s.Rational(27,100)*z**2+s.Rational(1,100)*z**3
    assert s.discriminant(A,z)==s.Rational(17,250000)
    assert s.discriminant(1+s.Rational(27,100)*z+s.Rational(1,100)*z**2,z)==s.Rational(329,10000)
    tails=[]
    for l in range(4):
        p=s.Poly(sum(s.expand(A).coeff(z,j)*z**(j-l) for j in range(l,4)),z)
        assert p.count_roots(-s.oo,0)==p.degree();tails.append(p.degree())
    assert s.discriminant(1+z+s.Rational(101,10)*z**2,z)==-s.Rational(197,5)
    assert s.discriminant(1+z+s.Rational(5,18)*z**2,z)==-s.Rational(1,9)
    controls=0
    for n in range(1,9):
        cs=s.symbols('c:'+str(n+1));C=sum(cs[j]*z**j for j in range(n+1))
        for m in range(1,9):
            p=C
            for h in range(1,m):p=s.expand(z*s.diff(p,z)+h*p)
            p/=s.factorial(m-1)
            assert s.expand(p-sum(s.binomial(j+m-1,m-1)*cs[j]*z**j for j in range(n+1)))==0
            controls+=1
    receipt={'status':'PASS','all_tail_cubic_exact_root_counts':tails,
        'single_pole_operator_identities':controls,
        'exact_auxiliary_counterexamples':3,
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Controls for RESULTS.md; no full conjecture closure.'}
    (HERE/'EXACT-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
