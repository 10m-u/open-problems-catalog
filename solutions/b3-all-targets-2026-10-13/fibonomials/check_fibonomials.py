#!/usr/bin/env python3
"""Exact q-integer quotient arithmetic and the n=4 difference proof."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json
HERE=Path(__file__).resolve().parent
F=[0,1]
for i in range(2,35):F.append(F[-1]+F[-2])
def uniform(a,r):
    out=[];s=0
    for i in range(len(a)+r-1):
        if i<len(a):s+=a[i]
        if i>=r and i-r<len(a):s-=a[i-r]
        out.append(s)
    return out
def divide(a,r):
    if r==1:return a[:]
    degree=len(a)-r
    assert degree>=0
    out=[]
    for i in range(degree+1):
        out.append(a[i]-(a[i-1] if i else 0)+(out[i-r] if i>=r else 0))
    assert uniform(out,r)==a
    return out
def fibonomial(m,n):
    a=[1]
    for i in range(1,n+1):a=uniform(a,F[m+i])
    for i in range(1,n+1):a=divide(a,F[i])
    return a
def unimodal(a):
    return all(x<=y for x,y in zip(a[:len(a)//2],a[1:len(a)//2+1])) and a==a[::-1]
def partition123(n):
    return (n*n+6*n+12)//12 if n>=0 else 0
def main():
    for n in range(1001):
        direct=sum((n-3*c)//2+1 for c in range(n//3+1))
        assert partition123(n)==direct
        error=Fraction(n*n+6*n+12,12)-direct
        assert 0<=error<=Fraction(7,12)
    small=[];differences=0
    for m in range(1,19):
        p=fibonomial(m,4);A=F[m+1];B=F[m+2]
        assert len(p)-1==3*A+4*B-7
        assert unimodal(p) and min(p)>0
        for i in range((len(p)-1)//2+1):
            d=partition123(i)-partition123(i-A)-partition123(i-B)+partition123(i-2*A-B)
            assert d==p[i]-(p[i-1] if i else 0)
            assert d>=0
            differences+=1
        if m<=6:small.append({'m':m,'A':A,'B':B,'coefficients':p})
    obstruction=fibonomial(3,3)
    defects=[{'index':i,'defect':obstruction[i]**2-obstruction[i-1]*obstruction[i+1]}
             for i in range(1,len(obstruction)-1)
             if obstruction[i]**2<obstruction[i-1]*obstruction[i+1]]
    assert defects
    receipt={'status':'PASS','partition123_controls':1001,
       'n4_parameters_checked':list(range(1,19)),
       'n4_exact_difference_controls':differences,
       'small_n4_base_cases':small,
       'actual_B33_log_concavity_obstruction':{'coefficients':obstruction,'defects':defects},
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Exact controls for the separate all-m n=4 proof, not an all-n theorem.'}
    (HERE/'CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='small_n4_base_cases'},indent=2))
if __name__=='__main__':main()
