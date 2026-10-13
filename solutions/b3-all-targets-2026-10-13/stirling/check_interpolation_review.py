#!/usr/bin/env python3
"""Independent exact interpolation certificate controls; no root packet writes."""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_q1443_review import direct_integer_evaluation

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"interpolation"

def determinant(a):
    a=[list(map(Q,row)) for row in a]
    d=Q(1)
    for j in range(len(a)):
        pivot=next((i for i in range(j,len(a)) if a[i][j]),None)
        if pivot is None:return Q(0)
        if pivot!=j:a[pivot],a[j]=a[j],a[pivot];d=-d
        v=a[j][j];d*=v
        for i in range(j+1,len(a)):
            c=a[i][j]/v
            for k in range(j+1,len(a)):a[i][k]-=c*a[j][k]
    return d

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def vertex(n,k):
    out=[1]
    for j in range(n):out=multiply(out,[n+k-j-1,n-k+j])
    return out[::-1]

def hurwitz(b,r):
    get=lambda i:b[i] if 0<=i<len(b) else 0
    return determinant([[get(2*j-i+1) for j in range(r)] for i in range(r)])

def main():
    corner_controls=0
    for n in range(2,13):
        for k in range(n+1):
            b=vertex(n,k);get=lambda i:b[i] if 0<=i<len(b) else 0
            for r in range(1,n):
                d=hurwitz(b,r)
                assert d>0
                assert d==determinant([[get(r-2*i+j) for j in range(r)] for i in range(r)])
                if k==n:assert d==b[1]*hurwitz(b[1:],r-1)
                corner_controls+=1
    assert corner_controls==638
    assert determinant([[16,10,0,0],[10,16,10,0],
                        [0,10,16,10],[0,0,10,16]])==-1264
    b=[10,11,12,13,12,11,10]
    assert [hurwitz(b,r) for r in range(1,4)]==[11,2,-216]
    assert all(b[j]**2>b[j-1]*b[j+1] for j in range(1,6))
    cert=ROOT/"NEAREST-CERTIFICATES.json"
    base_controls=[]
    for record in json.loads(cert.read_text())["certificates"]:
        a,b,m=record["a"],record["b"],record["power"];n=2*m
        assert (a,b)==(19,10)
        value=lambda k:(b*k*k+b*k+a)**m
        vals=[value(k) for k in range(n+1)]
        h=[sum((-1)**d*comb(n+1,d)*vals[j-d] for d in range(j+1))
                 for j in range(n+1)]
        assert h==[int(c) for c in record["numerator"]] and min(h)>0 and h==h[::-1]
        # Derive g by descending elimination of t^m(t+t^-1)^j,
        # independently of the C_j/Chebyshev recurrence in the root checker.
        residual=h[:];g=[0]*(m+1)
        for j in range(m,-1,-1):
            c=residual[m+j];g[j]=c
            for k in range(j+1):residual[m+j-2*k]-=c*comb(j,k)
        assert not any(residual)
        assert g==[int(c) for c in record["reciprocal_reduction"]]
        previous=None;signs=[]
        for left,right in record["negative_below_minus_two_brackets"]:
            left,right=Q(left),Q(right)
            assert left<right<-2 and (previous is None or previous<left)
            lv=direct_integer_evaluation(g,left);rv=direct_integer_evaluation(g,right)
            ls=(lv>0)-(lv<0);rs=(rv>0)-(rv<0)
            assert ls*rs==-1
            signs.append([ls,rs]);previous=right
        assert len(signs)==m and len(g)==m+1
        for k in (n+1,n+2):
            assert value(k)==sum(h[j]*comb(n+k-j,n) for j in range(n+1))
        base_controls.append({"degree":n,"power":m,"positive_h_coefficients":n+1,
                              "g_below_minus_two_brackets":m,"endpoint_signs":signs})
    assert [r["power"] for r in base_controls]==[128,129]
    for m in range(16256,16384):
        v=m%128;u=(m-129*v)//128
        assert u>=0 and m==128*u+129*v
    small=[]
    for m in (1,2,3):
        n=2*m;vals=[(10*k*k+10*k+19)**m for k in range(n+1)]
        h=[sum((-1)**d*comb(n+1,d)*vals[j-d] for d in range(j+1))
                  for j in range(n+1)]
        small.append(h)
    assert small[0]==[19,-18,19]
    assert small[1]==[361,-284,2246,-284,361]
    g3=[small[2][3]-2*small[2][5],small[2][4]-3*small[2][6],
        small[2][5],small[2][6]]
    assert g3==[217368,201268,11306,6859]
    shifted=[sum(g3[j]*comb(j,k)*(-2)**(j-k) for j in range(k,4)) for k in range(4)]
    assert shifted==[-194816,238352,-29848,6859]
    receipt={"status":"PASS","all_order_corner_controls":corner_controls,
        "independent_det_method":"Fraction Gaussian elimination",
        "base_certificates":base_controls,"below_minus_two_brackets":257,
        "integer_endpoint_signs":514,
        "reciprocal_identity_method":"descending binomial elimination",
        "semigroup_residue_controls":128,
        "degree_six_generator_obstructions":small[:2]+[shifted],
        "source_certificate_sha256":sha256(cert.read_bytes()).hexdigest(),
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"Exact lower-family/corner proofs and restricted-route controls; no full disk or uniform nearest-root upper bound."}
    (HERE/"INTERPOLATION-REVIEW-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items() if k!="base_certificates"},indent=2))
if __name__=="__main__":main()

