#!/usr/bin/env python3
"""Exact Bernstein and exponential certificates for the one-sided theorem."""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial,comb
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent

def exp_upper(x,n=40):
    # Sum through n, then bound the remaining positive series geometrically.
    total=sum((x**j/F(factorial(j)) for j in range(n+1)),F(0))
    first=x**(n+1)/factorial(n+1)
    return total+first/(1-x/F(n+2))

def main():
    r,u,z,y=s.symbols('r u z y')
    lower=1/r+s.Rational(1,2)+r*(1+u)/12-r**3*(1+u)*(1+2*u)*(1+3*u)/720
    L=s.expand(r**4*(lower**4-lower**2-2*(1-u)*lower/r**3
                    +(1-2*u)*(1/r**2-(1-u)/12)**2))
    poly=s.Poly(s.expand(L.subs({r:1+z,u:y/2})),z,y)
    m,n=poly.degree(z),poly.degree(y);assert (m,n)==(16,12)
    powers=poly.as_dict();bernstein={}
    for i in range(m+1):
        for j in range(n+1):
            b=sum(a*s.Rational(comb(i,k),comb(m,k))*s.Rational(comb(j,l),comb(n,l))
                  for (k,l),a in powers.items() if k<=i and l<=j)
            assert b>0
            bernstein[i,j]=b
    # Independent triangular identity from Bernstein back to power coefficients.
    for k in range(m+1):
        for l in range(n+1):
            restored=sum(bernstein[i,j]*comb(m,i)*comb(n,j)*comb(m-i,k-i)
                         *comb(n-j,l-j)*(-1)**(k-i+l-j)
                         for i in range(k+1) for j in range(l+1))
            assert restored==powers.get((k,l),0)
    exp_controls=[]
    for exponent,bound in [(F(165,64),F(53,4)),(F(45,16),F(50,3)),
                            (F(15,4),F(43)),(F(9,2),F(100))]:
        upper=exp_upper(exponent);assert upper<bound
        exp_controls.append({'exponent':str(exponent),'upper':str(upper),
                             'comparison_bound':str(bound)})
    H=lambda q:(2-q)/(1-q)**2
    B=lambda a:1+1/a+2/a**2+2/a**3
    assert H(F(4,53))>B(F(2))
    assert H(F(3,50))>B(F(33,16))
    assert H(F(1,43))>B(F(9,4))
    assert H(F(1,100))>F(129,64)
    assert B(F(3))<2
    # Uniform upper estimate at u>=1/4,r>=2, used through r=3.
    R=(1-u)*(1+1/r+2/r**2+2/r**3+u*(1+1/r+2/r**2)-u*u)
    assert R.subs({r:2,u:s.Rational(1,4)})==s.Rational(129,64)
    assert s.simplify(R-(1+1/r+2/r**2+2/r**3)+2*u/r**3
                     +(2+1/r+2/r**2)*u**2-u**3)==0
    # Algebra linking one-sided bounds to the full two-sided inequality.
    a,b,A1,A2,k,D=s.symbols('a b A1 A2 k D')
    F1,F2,T=1+a,1+b,1+a+b
    substituted=T**4-T**2-T*(F1**3-F1+F2**3-F2
                      +k*A1**2/F1+k*A2**2/F2)+k*(A1-A2)**2
    bracket=b*A1**2/F1+a*A2**2/F2+2*A1*A2
    assert s.simplify(substituted-3*T*a*b*(T+1)+k*bracket)==0
    assert s.expand(a*F1+b*F2+2*F1*F2-T*(T+1))==0
    assert s.simplify(bracket.subs({A1:D*a*F1,A2:D*b*F2})
                      -D**2*a*b*T*(T+1))==0
    assert s.simplify(((1-u)**2*(1-2*u))/(1-u)**2-(1-2*u))==0
    # Independently check the displayed kernel series coefficient formula.
    for j in range(3,81):
        coefficient=F(1,factorial(2*j))-F(1,factorial(2*j+1)) \
                    -F(1,3*factorial(2*j-1))+F(1,45*factorial(2*j-3))
        expected=F(16*j*(j-1)*(j-2)*(j+2),45*factorial(2*j+1))
        assert coefficient==expected and coefficient>0
    certificate={'scope':'All r in [1,2] and u in [0,1/2], exact bivariate Bernstein positivity.',
       'degree':[m,n],'coordinates':{'r':'1+z','u':'y/2'},
       'positive_bernstein_coefficients':[{ 'i':i,'j':j,'value':str(b)} for (i,j),b in bernstein.items()],
       'minimum':str(min(bernstein.values())),
       'exponential_upper_controls':exp_controls}
    (HERE/'ONE-SIDED-CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
    receipt={'status':'PASS','bernstein_coefficients':len(bernstein),
       'independent_power_coefficient_reconstruction':(m+1)*(n+1),
       'exact_exponential_bounds':len(exp_controls),'parameter_interval_inequalities':5,
       'two_sided_algebra_identities':4,'kernel_coefficient_controls':78,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'certificate_sha256':sha256((HERE/'ONE-SIDED-CERTIFICATE.json').read_bytes()).hexdigest(),
       'scope':'Exact uniform controls used in ONE-SIDED.md; proof review still required.'}
    (HERE/'ONE-SIDED-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
