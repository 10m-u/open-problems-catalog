#!/usr/bin/env python3
"""Independent formal-series difference and fixed-path weight controls."""
from pathlib import Path
from collections import Counter
from itertools import combinations
from fractions import Fraction
from hashlib import sha256
import json,runpy
HERE=Path(__file__).resolve().parent
root=runpy.run_path(str(HERE.parent/'fibonomials/check_fibonomials.py'))
F=[0,1]
for _ in range(30):F.append(F[-1]+F[-2])
def conv(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    return C
def exact_quotient(m,n):
    num=[1];den=[1]
    for k in range(1,n+1):
        num=conv(num,[1]*F[m+k]);den=conv(den,[1]*F[k])
    D=len(num)-len(den);Q=[0]*(D+1)
    for k in range(D+1):Q[k]=num[k]-sum(den[j]*Q[k-j] for j in range(1,min(k,len(den)-1)+1))
    assert conv(Q,den)==num
    return Q
def p123(t):
    return sum((t-3*z)//2+1 for z in range(t//3+1)) if t>=0 else 0
def main():
    bases=[];diffs=0
    for m in range(1,7):
        A=F[m+1];B=F[m+2];q=exact_quotient(m,4);D=3*A+4*B-7
        assert len(q)==D+1 and q==q[::-1] and min(q)>0
        ds=[]
        for i in range(D//2+1):
            d=p123(i)-p123(i-A)-p123(i-B)+p123(i-2*A-B)
            assert d==q[i]-(q[i-1] if i else 0) and d>=0
            ds.append(d);diffs+=1
        assert q==root['fibonomial'](m,4)
        bases.append({'m':m,'degree':D,'lower_half_differences':ds})
    residues=[Fraction(t*t+6*t+12,12)-p123(t) for t in range(6)]
    assert residues==[Fraction(0),Fraction(7,12),Fraction(1,3),Fraction(1,4),Fraction(1,3),Fraction(7,12)]
    # Compute the eight cancellation coefficients without the claimed formula.
    numerator=Counter({(0,0):1})
    for a,b in ((1,0),(0,1),(1,1),(1,2)):
        out=numerator.copy()
        for (u,v),c in numerator.items():out[u+a,v+b]-=c
        numerator=Counter({k:v for k,v in out.items() if v})
    expected={(0,0):1,(1,0):-1,(0,1):-1,(2,1):1,(1,3):1,(3,3):-1,(2,4):-1,(3,4):1}
    assert dict(numerator)==expected
    hall={i:[j for j in range(11,21) if F[j]%F[i]==0] for i in (4,6,8,9,10)}
    assert set().union(*(set(v) for v in hall.values()))=={12,16,18,20}
    input_poly=[1,1,1,9,1,1,1]
    actual=exact_quotient(3,2)
    assert len(actual)==len(input_poly) and sum(actual)==sum(input_poly)==15
    out=conv(input_poly,[1,0,1,0,1])
    out += [0]*max(0,13-len(out))
    for i,c in enumerate(input_poly):out[i+6]+=c
    assert out==[1,1,2,10,3,11,4,11,3,10,2,1,1]
    # Source coordinates: special domino at (i,j) has F_(i+1)F_j;
    # regular horizontal domino at (i,j) has F_i F_j.
    forced=F[2]*F[2]+F[3]*F[2];optional=F[2]*F[3]
    assert (forced,optional)==(3,2)
    receipt={'status':'PASS','n4_base_cases':bases,'base_difference_controls':diffs,
        'six_residue_errors':[str(x) for x in residues],
        'formal_numerator_terms':{str(k):v for k,v in sorted(numerator.items())},
        'Hall_neighbors':hall,'synthetic_recursion_output':out,
        'actual_NNEEN_forced_degree':forced,'actual_NNEEN_optional_degree':optional,
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Independent arithmetic controls for the all-m n4 proof and named sufficient-route obstructions, not an all-n theorem.'}
    (HERE/'FIBONOMIAL-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='n4_base_cases'},indent=2))
if __name__=='__main__':main()
