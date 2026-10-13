#!/usr/bin/env python3
"""Exact reciprocal-polynomial IVT certificates for nearest-root bases."""
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path
from check_gap_certificates import sign_at

HERE=Path(__file__).resolve().parent
CERT=HERE/'NEAREST-CERTIFICATES.json'

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def polynomials(a,b,m):
    n=2*m;value=lambda k:(b*k*k+b*k+a)**m
    vals=[value(k) for k in range(n+1)]
    h=[sum((-1)**(j-k)*comb(n+1,j-k)*vals[k]
           for k in range(j+1)) for j in range(n+1)]
    assert h==h[::-1]
    C0,C1=[2],[0,1]
    g=[h[m]]
    for j in range(1,m+1):
        g=add(g,[h[m+j]*c for c in C1])
        C0,C1=C1,add([0]+C1,[-c for c in C0])
    return h,g,value

def generate():
    from flint import fmpz_poly,ctx
    ctx.prec=160
    records=[]
    for a,b,m in [(19,10,128),(19,10,129)]:
        h,g,_=polynomials(a,b,m)
        assert min(h)>0
        roots=fmpz_poly(g).complex_roots()
        assert len(roots)==m
        brackets=[]
        for root,mult in roots:
            assert mult==1 and root.imag==0 and root.real<-2
            c=Fraction(str(root.real.mid().fmpq()))
            radius=min(abs(c)/2**40,abs(c+2)/2**40)
            lo,hi=c-radius,c+radius
            assert sign_at(g,lo)*sign_at(g,hi)==-1
            brackets.append([str(lo),str(hi)])
        brackets.sort(key=lambda t:Fraction(t[0]))
        records.append({'a':a,'b':b,'power':m,'degree':2*m,
                        'numerator':[str(c) for c in h],
                        'reciprocal_reduction':[str(c) for c in g],
                        'negative_below_minus_two_brackets':brackets})
        print('generated',m,'brackets',len(brackets),flush=True)
    CERT.write_text(json.dumps({'certificates':records},indent=2)+'\n')

def verify():
    rows=[]
    for r in json.loads(CERT.read_text())['certificates']:
        a,b,m=(r[k] for k in ('a','b','power'))
        h,g,value=polynomials(a,b,m)
        assert r['degree']==2*m
        assert r['numerator']==[str(c) for c in h] and min(h)>0
        assert r['reciprocal_reduction']==[str(c) for c in g]
        # Independent expansion of t^m g(t+t^-1) as an ordinary polynomial.
        reconstruction=[0]*(2*m+1)
        for j,c in enumerate(g):
            for k in range(j+1):reconstruction[m+j-2*k]+=c*comb(j,k)
        assert reconstruction==h
        previous=None
        brackets=r['negative_below_minus_two_brackets']
        assert len(brackets)==m and len(g)==m+1
        for pair in brackets:
            lo,hi=map(Fraction,pair)
            assert lo<hi<-2 and (previous is None or previous<lo)
            assert sign_at(g,lo)*sign_at(g,hi)==-1
            previous=hi
        for k in (2*m+1,2*m+2):
            assert value(k)==sum(h[j]*comb(2*m+k-j,2*m) for j in range(2*m+1))
        assert Fraction(a,b)>Fraction(1,4)
        rows.append({'a':a,'b':b,'power':m,'degree':2*m,
                     'exact_reciprocal_root_brackets':m,
                     'negative_numerator_roots':2*m,
                     'nearest_root_modulus_squared':str(Fraction(a,b))})
    assert [r['power'] for r in rows]==[128,129]
    # Every exponent m>=128*127 is 128u+129v with u,v>=0.
    for m in range(128*127,128*127+128):
        v=m%128;u=(m-129*v)//128
        assert u>=0 and v>=0 and m==128*u+129*v
    receipt={'status':'PASS','bases':rows,
             'all_even_degrees_from':2*128*127,
             'certificate_sha256':sha256(CERT.read_bytes()).hexdigest(),
             'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'scope':'Exact finite bases and product closure give r_n>=sqrt(19/10) for every even n>=32512, and for each nonzero nonnegative combination of256 and258. This is a lower bound, not the requested uniform upper bound.'}
    (HERE/'NEAREST-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--generate',action='store_true')
    args=parser.parse_args()
    if args.generate:generate()
    verify()
