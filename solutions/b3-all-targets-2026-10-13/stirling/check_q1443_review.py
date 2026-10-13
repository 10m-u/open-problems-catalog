#!/usr/bin/env python3
"""Independent exact certificate audit: direct homogeneous endpoint sums."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
HOME=HERE.parent
CERT=HOME/"interpolation/Q1443-COUNTEREXAMPLE-CERTIFICATE.json"

def sampled(k):
    return (2*k+1)**32*(5*k+2)**2*(5*k-12)**2

def direct_integer_evaluation(coefficients, point):
    """q^d H(p/q), by the defining homogeneous sum (no Horner call)."""
    p,q=point.numerator,point.denominator
    d=len(coefficients)-1
    return sum(c*pow(p,j)*pow(q,d-j) for j,c in enumerate(coefficients))

def main():
    records=json.loads(CERT.read_text())["certificates"]
    assert len(records)==1
    record=records[0]
    assert (record["a"],record["b"],record["M"],record["degree"])==(7,5,32,36)
    d=36
    # Multiplication by (1-t)^37, independently from the certificate list.
    h=[sum((-1)**r*comb(d+1,r)*sampled(j-r)
           for r in range(j+1)) for j in range(d+1)]
    assert h==[int(x) for x in record["numerator_coefficients"]]
    assert len(h)==37 and min(h)>0 and h[0]==576 and h[-1]==2601
    # Direct Newton sums rather than the root checker's difference-table loop.
    delta=[sum((-1)**(j-k)*comb(j,k)*sampled(k) for k in range(j+1))
           for j in range(d+1)]
    from_newton=[sum(delta[j]*(-1)**(i-j)*comb(d-j,i-j)
                     for j in range(i+1)) for i in range(d+1)]
    assert from_newton==h
    gf_checks=0
    for k in range(61):
        assert sampled(k)==sum(h[j]*comb(d+k-j,d)
                               for j in range(min(k,d)+1))
        gf_checks+=1
    endpoint_signs=[]
    previous=None
    for pair in record["negative_sign_change_intervals"]:
        left,right=map(Fraction,pair)
        assert left<right<0 and (previous is None or previous<left)
        values=[direct_integer_evaluation(h,x) for x in (left,right)]
        signs=[(v>0)-(v<0) for v in values]
        assert signs[0]*signs[1]==-1
        endpoint_signs.append(signs)
        previous=right
    assert len(endpoint_signs)==d
    roots=[Fraction(-1,2)]*32+[Fraction(-2,5)]*2+[Fraction(12,5)]*2
    assert len(roots)==d and roots==sorted(roots)
    assert roots[34]-roots[33]==Fraction(14,5)>2
    assert record["gap"]=="14/5"
    receipt={"status":"PASS","degree":d,"positive_numerator_coefficients":len(h),
             "disjoint_negative_root_brackets":len(endpoint_signs),
             "independent_integer_endpoint_signs":endpoint_signs,
             "direct_newton_and_convolution_identity":True,
             "generating_function_coefficients_checked":gf_checks,
             "one_based_consecutive_root_indices":[34,35],
             "exact_gap":"14/5","certificate_sha256":sha256(CERT.read_bytes()).hexdigest(),
             "scope":"Full counterexample to catalog Q1443's bound below 2; no claim that arbitrary finite dimension-free bounds are impossible."}
    (HERE/"Q1443-REVIEW-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items()
                      if k!="independent_integer_endpoint_signs"},indent=2))

if __name__=="__main__":main()

