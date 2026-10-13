#!/usr/bin/env python3
"""Exact OG(2,5) table from a monic Newton-basis quotient."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

HERE=Path(__file__).resolve().parent
def main():
    u,v,x=s.symbols('u v x')
    basis=[s.Integer(1),x,x*(x-u),x*(x-u)*(x-u-v)]
    relation=s.Poly(x*(x-u)*(x-u-v)*(x-2*u-v),x)
    def product(i,j):
        p=s.rem(s.Poly(basis[i]*basis[j],x),relation).as_expr()
        answer=[0]*4
        for k in range(3,-1,-1):
            answer[k]=s.expand(p).coeff(x,k)
            p=s.expand(p-answer[k]*basis[k])
        assert p==0
        return list(map(s.factor,answer))
    table={str((i,j)):list(map(str,product(i,j))) for i in range(4) for j in range(i,4)}
    expected={
       (1,1):[0,u,1,0],
       (1,2):[0,0,u+v,1],
       (1,3):[0,0,0,2*u+v],
       (2,2):[0,0,v*(u+v),2*(u+v)],
       (2,3):[0,0,0,(u+v)*(2*u+v)],
       (3,3):[0,0,0,u*(u+v)*(2*u+v)]}
    for ij,cs in expected.items():
        assert all(s.expand(a-b)==0 for a,b in zip(product(*ij),cs))
    assert s.expand(product(2,2)[2]).subs(v,0)==0
    assert s.expand(product(2,2)[2])!=0
    assert s.simplify(basis[1].subs(x,u+v)**2/basis[2].subs(x,u+v)-(1+u/v))==0
    assert s.simplify((basis[1]**2-u*basis[1]).subs(x,u+v)/basis[2].subs(x,u+v))==1
    receipt={'status':'PASS','rank_two_products':table,
       'independent_parameter_specialization_obstruction':str(s.expand(product(2,2)[2])),
       'raw_localization_quotient':'1+u/v','correct_localization_coefficient':1,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Exact low-rank controls; no general combinatorial closure.'}
    (HERE/'OG-RANK-TWO-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

