#!/usr/bin/env python3
"""Exact identities and obstructions; the controls are not all-size proofs."""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import random
import sympy as s

HERE=Path(__file__).resolve().parent

def elementary(roots):
    answer=[F(1)]
    for r in roots:
        new=answer+[F(0)]
        for k in range(1,len(new)): new[k]+=r*answer[k-1]
        answer=new
    return answer

def falling(x,k):
    answer=1
    for i in range(k):answer*=x-i
    return answer

def additive(p,q):
    n=len(p)-1
    return [sum(F(factorial(n-i)*factorial(n-k+i),factorial(n)*factorial(n-k))
                  *p[i]*q[k-i] for i in range(k+1)) for k in range(n+1)]

def symmetrize(p):return additive(p,[v*(-1)**i for i,v in enumerate(p)])

def zn(n):
    result=[F(0)]*(n+1);result[0]=F(1)
    for k in range(1,n//2+1):
        result[2*k]=(-1)**k*F(comb(n,2*k)*falling(n,k)*factorial(k)*(n+1-k),
                              factorial(2*k)*(n+1))
    return result

def commutator(p,q):
    n=len(p)-1;pp,qq,z=symmetrize(p),symmetrize(q),zn(n)
    return [pp[k]*qq[k]*z[k]/comb(n,k)**2 for k in range(n+1)]

def rectangular(p,q,alpha):
    n=len(p)-1
    scale=[falling(n,k)*falling(n+alpha,k) for k in range(n+1)]
    return [scale[k]*sum(p[i]*q[k-i]/(scale[i]*scale[k-i])
                         for i in range(k+1)) for k in range(n+1)]

def moments(a):
    centered=[F(v)-F(sum(a),len(a)) for v in a]
    return sum(v*v for v in centered),sum(v**4 for v in centered)

def main():
    rng=random.Random(34363437);nchecks=0;dchecks=0
    for n in range(2,16):
        for _ in range(30):
            a=[rng.randrange(-9,10) for i in range(n)]
            b=[rng.randrange(-9,10) for i in range(n)]
            p,q=elementary(a),elementary(b);pp=symmetrize(p)
            A,T=moments(a);B,U=moments(b);out=commutator(p,q)
            assert pp[2]==-A and out[2]==-F(n,n*n-1)*A*B
            assert all(pp[k]==0 for k in range(1,n+1,2))
            if n>=4:
                assert pp[4]==F(n*n-3*n+3,2*n*(n-1))*A*A-T/2
            if n==4:
                assert out[2]**2-4*out[4]>=A*A*B*B/225
            if n==5:
                assert T>=F(7,30)*A*A
                assert out[2]**2-4*out[4]>=F(25,5184)*A*A*B*B
            nchecks+=1
    for n in range(2,13):
        for alpha in [F(-99,100),F(-3,4),F(-1,2),F(0),F(1,4),F(3,2)]:
            for _ in range(8):
                p=elementary([rng.randrange(0,11) for i in range(n)])
                q=elementary([rng.randrange(0,11) for i in range(n)])
                out=rectangular(p,q,alpha)
                dp=[F(n-k,n)*p[k] for k in range(n)]
                dq=[F(n-k,n)*q[k] for k in range(n)]
                assert [F(n-k,n)*out[k] for k in range(n)]==rectangular(dp,dq,alpha+1)
                if n==2:
                    c=F(1+alpha,2*(2+alpha));S,P=p[1:];T,Q=q[1:]
                    assert out==[1,S+T,P+Q+c*S*T]
                    assert out[1]**2-4*out[2]==S*S-4*P+T*T-4*Q+(2-4*c)*S*T
                dchecks+=1
    alpha=s.Symbol('alpha',real=True)
    S,T,P,Q=s.symbols('S T P Q',real=True)
    c=(1+alpha)/(2*(2+alpha))
    assert s.factor(2-4*c)==2/(alpha+2)
    # Forced ordinary-additive transfer, on an actual nonnegative input.
    disc=s.factor((2/(2+alpha))**2-4/((2+alpha)*(1+alpha)))
    assert disc==-4/((alpha+1)*(alpha+2)**2)
    # Stronger unrestricted real-root preservation fails at m=2.
    out=rectangular([F(1),F(-2),F(1)],[F(1),F(2),F(1)],F(-3,4))
    assert out==[1,0,F(8,5)]
    # Positive mixture of alpha=-1/2 and nonnegative integer cases cannot
    # generate alpha=-3/4 for these actual nonnegative inputs.
    e2=lambda a:rectangular([F(1),F(2),F(1)],[F(1),F(2),F(1)],a)[2]
    assert e2(F(-3,4))==F(12,5) and e2(F(-1,2))==F(8,3)
    assert s.factor(s.diff((6+4*alpha)/(2+alpha),alpha))==2/(alpha+2)**2
    # Expected real-rooted even polynomials need not be real rooted.
    x=s.Symbol('x',real=True)
    avg=s.expand(((x*x-1)**2+(x*x-9)**2)/2)
    assert avg==x**4-10*x*x+41 and 100-4*41==-64
    # m=2 multiplier forced by coefficient formula 5.4.
    p=elementary([-1,-1,1,1]);sy=symmetrize(p)
    assert sy==[1,0,-4,0,F(8,3)]
    z=zn(4);K=[F(1),F(16,15),F(3,5)]
    for k in range(3):
        assert K[k]==(-1)**k*z[2*k]*comb(2,k)**2/comb(4,2*k)**2
    assert K[1]**2-4*K[2]==-F(284,225)
    # Forced Hermite-factor quotient for the same admissible q.
    H=[F(1),F(3),F(3,4)]
    half=[(-1)**k*sy[2*k] for k in range(3)]
    quotient=[half[k]*comb(2,k)/H[k] for k in range(3)]
    assert quotient==[1,F(8,3),F(32,9)]
    assert quotient[1]**2-4*quotient[2]==-F(64,9)
    # Actual n=2 commutator coefficient, B-spectrum {0,1}.
    a1,a2=s.symbols('a1 a2')
    pp=[s.Integer(1),a1+a2,a1*a2]
    symbolic=commutator(pp,[s.Integer(1),s.Integer(1),s.Integer(0)])
    assert s.factor(symbolic[2])==-(a1-a2)**2/6
    Fjoint=x*x+symbolic[2]
    assert s.simplify(Fjoint.subs({a1:s.I,a2:3*s.I,x:s.I*s.sqrt(s.Rational(2,3))}))==0
    two_value=[F(25-15*a+3*a*a,5*a*(5-a)) for a in range(1,5)]
    assert two_value==[F(13,20),F(7,30),F(7,30),F(13,20)]
    receipt={'status':'PASS','seed':34363437,'moment_identity_controls':nchecks,
             'rectangular_derivative_controls':dchecks,
             'exact_obstructions':{'transfer_discriminant':str(disc),
                'unrestricted_real_input_output_e':list(map(str,out)),
                'commutator_kernel_e':list(map(str,K)),
                'hermite_quotient_e':list(map(str,quotient)),
                'generic_average':str(avg)},
             'file_sha256':{f.name:sha256(f.read_bytes()).hexdigest() for f in
                [Path(__file__),HERE/'MOMENT-RESULTS.md',HERE/'RECTANGULAR-RESULTS.md']},
             'scope':'Exact coefficient controls and route obstructions. All-size partial theorem proofs are in the result notes; no full conjecture closure.'}
    (HERE/'EXACT-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
