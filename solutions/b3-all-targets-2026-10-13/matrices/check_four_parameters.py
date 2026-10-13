#!/usr/bin/env python3
"""Exact recurrence, production-matrix, and boundary-minor controls."""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

HERE=Path(__file__).resolve().parent
a,c,d,e=S.symbols('a c d e')
VARS=(a,c,d,e)

def rows(N):
    out=[[S.Integer(1)]]
    for n in range(1,N+1):
        p=out[-1]+[0]
        out.append([S.expand((a*(n-k)+c)*(p[k-1] if k else 0)+(d*k+e)*p[k])
                    for k in range(n+1)])
    return out

def nonnegative(f):return all(v>=0 for v in S.Poly(S.expand(f),*VARS).coeffs())

def main():
    T=rows(8)
    boundary_checks=0
    for n in range(1,9):
        formula=sum((a*j+c)*e**j*(d+e)**(n-1-j) for j in range(n))
        assert S.expand(T[n][1]-formula)==0
        for m in range(n):
            previous=T[m][1] if m else 0
            det=S.expand(e**m*T[n][1]-e**n*previous)
            expression=e**m*((d+e)**(n-m)-e**(n-m))*previous
            expression+=e**m*sum((a*j+c)*e**j*(d+e)**(n-1-j) for j in range(m,n))
            assert S.expand(det-expression)==0 and nonnegative(det)
            boundary_checks+=1
    L=S.Matrix([r+[0]*(3-len(r)) for r in T[:3]])
    R=S.Matrix([r[:3]+[0]*max(0,3-len(r)) for r in T[1:4]])
    P=L.inv()*R
    assert S.factor(P[2,1]+a*e*(a*e+c*d)/c**3)==0
    prefix=S.Matrix([[1,0,0],[1,1,0],[1,1,2]])
    for order in range(1,4):
        for I in combinations(range(3),order):
            for J in combinations(range(3),order):assert prefix.extract(I,J).det()>=0
    p=[1,1,2,0];n=3
    appended=[(n-k+1)*(p[k-1] if k else 0)+(k+1)*p[k] for k in range(4)]
    assert appended==[1,5,8,2]
    assert p[1]*appended[2]-p[2]*appended[1]==-2
    small=0
    for order in [1,2]:
        for I in combinations(range(6),order):
            for J in combinations(range(6),order):
                f=S.Matrix([[T[i][j] if j<=i else 0 for j in J] for i in I]).det()
                assert nonnegative(f),(I,J,f)
                small+=1
    for n in range(1,5):
        for k in range(n):
            f=S.Matrix([[T[i][j] if j<=i else 0 for j in range(k,k+3)]
                        for i in range(n,n+3)]).det()
            assert nonnegative(f),(n,k)
            small+=1
    receipt={'status':'PASS','boundary_minor_controls':boundary_checks,
             'production_P_2_1':str(S.factor(P[2,1])),
             'TN_prefix':[[int(v) for v in row] for row in prefix.tolist()],'recurrence_extension':appended,
             'negative_adjacent_minor':-2,'bounded_coefficient_minor_controls':small,
             'scope':'All-size leading-two-column theorem has a written proof; finite higher-minor checks do not solve Q3846.'}
    (HERE/'FOUR-PARAMETER-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__=='__main__':main()
