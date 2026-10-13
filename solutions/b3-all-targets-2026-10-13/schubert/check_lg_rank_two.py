#!/usr/bin/env python3
"""LG rank-two associativity and Euler-dual exact controls."""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s
HERE=Path(__file__).resolve().parent
def main():
    unit=[1,0,0,0];T={}
    for i in range(4):
        v=[0]*4;v[i]=1;T[0,i]=T[i,0]=v
    T[1,1]=[0,0,2,-1]
    T[1,2]=T[2,1]=[0,0,0,1]
    for i,j in [(1,3),(2,2),(2,3),(3,3)]:
        T[i,j]=T[j,i]=[0]*4
    def mul(a,b):
        return [sum(a[i]*b[j]*T[i,j][k] for i in range(4) for j in range(4)) for k in range(4)]
    basis=[list(s.eye(4).col(i)) for i in range(4)]
    controls=0
    for a in basis:
        for b in basis:
            for c in basis:
                assert mul(mul(a,b),c)==mul(a,mul(b,c));controls+=1
    G=s.Matrix([[sum(mul(a,b)) for b in basis] for a in basis])
    assert G==s.Matrix([[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,0]])
    dual=G.inv()
    assert list(dual.col(3))==[1,-1,0,0]
    assert G*dual==s.eye(4)
    a=basis[1];a2=mul(a,a);a3=mul(a2,a)
    assert sum(a2)==1 and sum(a3)==2
    assert sum(mul(a2,list(dual.col(3))))==-1
    receipt={'status':'PASS','associativity_basis_triples':controls,
       'Euler_Gram':[[int(v) for v in row] for row in G.tolist()],
       'Euler_dual_columns':[[int(v) for v in row] for row in dual.tolist()],
       'ordinary_complement_pairing':1,'correct_K_dual_pairing':-1,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Rank-two geometry and proved Pieri supply the table; this checker controls algebraic consistency and dual pairing.'}
    (HERE/'LG-RANK-TWO-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

