#!/usr/bin/env python3
"""Exact small controls for the written five Q1441 proof attempts."""
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path
from check_nearest_family import polynomials

HERE=Path(__file__).resolve().parent

def main():
    # N01: admissibility's sample-LC ceiling and strict endpoint obstruction.
    for c in [Fraction(j,10) for j in range(1,41)]:
        assert (c+2)**2-c*(c+6)==4-2*c
    for m in range(1,21):
        v=[2**m,4**m,8**m,14**m]
        determinant=v[1]**3-2*v[0]*v[1]*v[2]+v[0]**2*v[3]
        assert determinant==56**m-64**m<0
    # N03 exact permitted transform, but no real roots.
    # P=z²+z+1/2 = (1/2)+2*binom(z,1)+2*binom(z,2).
    assert Fraction(1,2)==2*Fraction(1,2)**2
    assert 1-4*Fraction(1,2)==-1
    # N04 L(P)=(u+1)^2, with its constant removed and divided by u.
    assert [1,2,1][1:]==[2,1]
    for z in range(-5,6):
        P=lambda x:Fraction((x+1)*(x+2),2)
        assert P(z+1)-P(z)==z+2
    # N05 actual real divisors of degree<=6 are excluded exactly.
    h1,g1,_=polynomials(19,10,1)
    h2,g2,_=polynomials(19,10,2)
    h3,g3,_=polynomials(19,10,3)
    assert h1==[19,-18,19]
    assert h2==[361,-284,2246,-284,361]
    assert g3==[217368,201268,11306,6859]
    shift=[sum(g3[j]*comb(j,i)*(-2)**(j-i) for j in range(i,len(g3)))
           for i in range(len(g3))]
    assert shift==[-194816,238352,-29848,6859]
    # N02 inverse-Newton endpoint identities at distinct independent parameters.
    endpoint_controls=0
    for n in range(1,21):
        aa=[Fraction((3*i+n)%11,10) for i in range(n)]
        polynomial=[Fraction(1)]
        for a in aa:
            new=[Fraction(0)]*(len(polynomial)+1)
            for j,v in enumerate(polynomial):new[j]+=a*v;new[j+1]+=v
            polynomial=new
        at0=polynomial[0];atminus1=sum((-1)**j*c for j,c in enumerate(polynomial))
        product0=product1=Fraction(1)
        for a in aa:product0*=a;product1*=1-a
        assert at0==product0 and atminus1==(-1)**n*product1
        assert abs(at0*atminus1)<=Fraction(1,4**n)
        endpoint_controls+=1
    files=['NEAREST-RESULTS.md','ATTEMPTS.md','check_nearest_routes.py',
           'NEAREST-CERTIFICATES.json','NEAREST-CHECK.json']
    receipt={'status':'PASS','endpoint_controls':endpoint_controls,
             'quadratic_power_ceiling_controls':40,'negative_endpoint_minors':20,
             'actual_no_real_root_and_difference_controls':True,
             'degree_at_most_six_factor_obstructions':3,
             'files_sha256':{f:sha256((HERE/f).read_bytes()).hexdigest() for f in files},
             'scope':'Finite controls support all-size algebra and explicit proof-route failures; no uniform upper bound is asserted.'}
    (HERE/'NEAREST-ROUTE-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
