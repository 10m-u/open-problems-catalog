#!/usr/bin/env python3
"""Read-only independent Q4082 middle-region certificate audit, stdlib only."""
from fractions import Fraction as Q
from collections import defaultdict
from math import comb, factorial
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/"concave-laws"

def clean(p):
    return {a:Q(b) for a,b in p.items() if b}

def add(*ps):
    out=defaultdict(Q)
    for p in ps:
        for a,b in p.items():out[a]+=b
    return clean(out)

def scale(p,c):return clean({a:b*c for a,b in p.items()})
def mul(p,q):
    out=defaultdict(Q)
    for (i,j),a in p.items():
        for (k,l),b in q.items():out[i+k,j+l]+=a*b
    return clean(out)

def power(p,n):
    out={(0,0):Q(1)}
    for _ in range(n):out=mul(out,p)
    return out

def mono(i,j=0,c=1):return {(i,j):Q(c)}

def shift(p):
    # Independent direct substitution r=1+z, u=y/2.
    out=defaultdict(Q)
    for (i,j),a in p.items():
        assert i>=0 and j>=0
        for k in range(i+1):out[k,j]+=a*comb(i,k)/2**j
    return clean(out)

def bernstein_basis(i,j,m,n):
    out={}
    for k in range(m-i+1):
        for l in range(n-j+1):
            out[i+k,j+l]=Q(comb(m,i)*comb(n,j)*comb(m-i,k)
                              *comb(n-j,l)*(-1)**(k+l))
    return out

def exp_upper(x,order=40):
    term=Q(1);partial=term
    for j in range(1,order+1):
        term*=x/j
        partial+=term
    first=term*x/(order+1)
    # Subsequent ratios are bounded by x/(order+2)<1.
    assert x/(order+2)<1
    return partial+first/(1-x/(order+2))

def main():
    one={(0,0):Q(1)}
    u=mono(0,1)
    # Derive the actual lower-bound polynomial independently of Sympy.
    f=add(mono(-1),mono(0,c=Q(1,2)),
          scale(mul(mono(1),add(one,u)),Q(1,12)),
          scale(mul(mono(3),mul(add(one,u),
                   mul(add(one,scale(u,2)),add(one,scale(u,3))))),Q(-1,720)))
    termA=add(mono(-2),scale(add(one,scale(u,-1)),Q(-1,12)))
    p=mul(mono(4),add(power(f,4),scale(power(f,2),-1),
              scale(mul(mono(-3),mul(add(one,scale(u,-1)),f)),-2),
              mul(add(one,scale(u,-2)),power(termA,2))))
    assert min(i for i,j in p)>=0
    expected=shift(p)
    cert_path=SOURCE/"ONE-SIDED-CERTIFICATE.json"
    cert=json.loads(cert_path.read_text())
    assert cert["degree"]==[16,12]
    bs={(row["i"],row["j"]):Q(row["value"])
             for row in cert["positive_bernstein_coefficients"]}
    assert len(bs)==221 and set(bs)=={(i,j) for i in range(17) for j in range(13)}
    restored=add(*(scale(bernstein_basis(i,j,16,12),b) for (i,j),b in bs.items()))
    assert restored==expected
    assert all(b>0 for b in bs.values())
    assert min(bs.values())==Q("386066666641/268738560000")
    exp_receipts=[]
    for x,bound in [(Q(165,64),Q(53,4)),(Q(45,16),Q(50,3)),
                     (Q(15,4),Q(43)),(Q(9,2),Q(100))]:
        computed=exp_upper(x)
        assert computed<bound
        matching=[row for row in cert["exponential_upper_controls"]
                   if Q(row["exponent"])==x]
        assert len(matching)==1 and Q(matching[0]["upper"])==computed
        exp_receipts.append({"argument":str(x),"bound":str(bound)})
    h=lambda q:(2-q)/(1-q)**2
    b=lambda r:1+1/r+2/r**2+2/r**3
    assert h(Q(4,53))>b(Q(2))
    assert h(Q(3,50))>b(Q(33,16))
    assert h(Q(1,43))>b(Q(9,4))
    assert h(Q(1,100))>Q(129,64)
    assert b(Q(3))<2
    # Taylor coefficient formula checked directly; zeros j=0,1,2 included.
    for j in range(41):
        actual=Q(1,factorial(2*j))-Q(1,factorial(2*j+1))
        if j>=1:actual-=Q(1,3*factorial(2*j-1))
        if j>=2:actual+=Q(1,45*factorial(2*j-3))
        claimed=Q(16*j*(j-1)*(j-2)*(j+2),45*factorial(2*j+1))
        assert actual==claimed and actual>=0
    # Check the gluing algebra on exact, deliberately unsaturated moment data.
    controls=0
    for a in [Q(0),Q(1,5),Q(1),Q(3)]:
        for b2 in [Q(0),Q(2,7),Q(2)]:
            for u0 in [Q(1,10),Q(1,3),Q(49,100)]:
                F1,F2,T=1+a,1+b2,1+a+b2
                D=1/(1-u0);k=(1-u0)**2*(1-2*u0)
                A1=D*a*F1/Q(2);A2=D*b2*F2/Q(3)
                replacement=T**4-T**2-T*(F1**3-F1+F2**3-F2+
                             k*A1*A1/F1+k*A2*A2/F2)+k*(A1-A2)**2
                bracket=b2*A1*A1/F1+a*A2*A2/F2+2*A1*A2
                assert replacement==3*T*a*b2*(T+1)-k*bracket
                assert bracket<=D*D*a*b2*T*(T+1)
                assert replacement>=(3-k*D*D)*a*b2*T*(T+1)>=0
                controls+=1
    receipt={
        "status":"PASS",
        "review_contract":"Independent exact certificate and algebra controls; analytic arguments reviewed separately.",
        "method":"stdlib Fraction Laurent-polynomial convolution; direct Bernstein-basis expansion",
        "positive_bernstein_coefficients":221,
        "power_coefficient_slots_compared":221,
        "nonzero_power_coefficients":len(expected),
        "minimum_bernstein_coefficient":str(min(bs.values())),
        "exact_exponential_bounds":exp_receipts,
        "parameter_comparisons":5,
        "kernel_coefficient_controls_including_three_zeros":41,
        "exact_gluing_controls":controls,
        "source_certificate_sha256":sha256(cert_path.read_bytes()).hexdigest(),
        "checker_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope":"Full Q4082 proof passes mathematical review at alpha in (-1/3,0), subject to the companion review."
    }
    (HERE/"Q4082-REVIEW-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))
if __name__=="__main__":main()

