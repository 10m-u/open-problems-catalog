#!/usr/bin/env python3
"""Literal subsum polynomials and independent moment/boundary controls."""
from functools import cache
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

@cache
def partitions(n):
    if not n:return ((),)
    return tuple((n-2*t,)+p for t in range(n//2+1) for p in partitions(t))

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        if v:
            for j,w in enumerate(b):
                if w:c[i+j]+=v*w
    return c

def binomial_factor(r,m):
    c=[0]*(r*m+1)
    for k in range(m+1):c[r*k]=comb(m,k)
    return c

def product(n):
    c=[1]
    for i in range(1,n+1):c=multiply(c,binomial_factor(i,(n//i).bit_length()))
    return c

def binary_sum(n):
    out=[0]*(sum((1<<j)*(n//(1<<j)) for j in range(n.bit_length()))-n+1)
    for p in partitions(n):
        c=[1]
        for j in range(n.bit_length()):
            r=1<<j;m=p[j] if j<len(p) else 0
            c=multiply(c,binomial_factor(r,n//r-m))
        assert len(c)==len(out)
        out=[v+w for v,w in zip(out,c)]
    return out

def lc(c):return all(c[i]**2>=c[i-1]*c[i+1] for i in range(1,len(c)-1))
def ulc(c):
    d=len(c)-1
    return all(i*(d-i)*c[i]**2>=(i+1)*(d-i+1)*c[i-1]*c[i+1] for i in range(1,d))

def main():
    b=[1]
    for n in range(1,10001):b.append(b[-1]+(b[n//2] if not n%2 else 0))
    s1=[];s2=[];sm1=[];v1=v2=vm=0
    for n,bn in enumerate(b):
        v1+=n*bn;v2+=n*n*bn;s1.append(v1);s2.append(v2)
        vm+=n*bn-2*s1[n//2];sm1.append(vm)
    boundary_cases=0
    for n in range(4,10001):
        N=n//2;B=b[n];first=2*s1[N]
        second=2*s2[N]-s1[N]+N*B-sm1[N]
        assert 2*first>=(2*N+1)*B
        assert first*first>B*second
        boundary_cases+=1
    controls=[]
    for n in range(1,41):
        p=product(n);assert p==p[::-1]
        L=n.bit_length();m2=(n//2).bit_length();m3=(n//3).bit_length()
        assert p[1]==L
        if len(p)>2:assert p[2]==comb(L,2)+m2
        if len(p)>3:assert p[3]==comb(L,3)+L*m2+m3
        if n>=8:assert p[1]**2>p[0]*p[2] and p[2]**2>p[1]*p[3]
        assert lc(p)==(n not in [3,5,6,7]),n
        sigma=F(sum((n//i).bit_length()*i*i for i in range(1,n+1)),4)
        degree=len(p)-1
        assert F(sum((2*i-degree)**2*v for i,v in enumerate(p)),4*sum(p))==sigma
        controls.append({'n':n,'product_variance':str(sigma)})
        if n<=20:
            chain=[1]
            for j in range(1,n+1,2):
                for q in range((n//j).bit_length()):
                    factor=[0]*(((1<<(q+1))-1)*j+1)
                    for k in range(1<<(q+1)):factor[k*j]=1
                    chain=multiply(chain,factor)
            assert chain==p
            recurrence=product(n-1) if n>1 else [1]
            r=n
            while True:
                recurrence=multiply(recurrence,binomial_factor(r,1))
                if r%2:break
                r//=2
            assert recurrence==p
    literal=0;non_ulc=[]
    for n in range(2,33):
        h=binary_sum(n);assert h==h[::-1] and len(partitions(n))==b[n]
        N=n//2
        assert h[0]==b[n] and h[1]==2*s1[N]
        assert h[2]==2*s2[N]-s1[N]+N*b[n]-sm1[N]
        if n>=6:assert lc(h)
        if n>=4:assert h[1]**2>h[0]*h[2]
        weights=[F(1,2**sum(p)) for p in partitions(n)]
        weighted_square=sum(w*sum(m*(1<<j)**2 for j,m in enumerate(p)) for p,w in zip(partitions(n),weights))/sum(weights)
        S=sum((1<<j)**2*(n//(1<<j)) for j in range(n.bit_length()))
        variance=(S-weighted_square)/4
        degree=len(h)-1
        assert F(sum((2*i-degree)**2*v for i,v in enumerate(h)),4*sum(h))==variance
        if n>=4 and n&(n-1)==0:
            assert variance>=F(n*n-n,4)>F(degree,4) and not ulc(h)
            non_ulc.append({'n':n,'degree':degree,'variance':str(variance),'ULC_variance_ceiling':str(F(degree,4))})
        literal+=1
    h=binary_sum(6);altered=h[:]
    for i,v in zip(range(3,8),[1,-4,6,-4,1]):altered[i]+=10*v
    assert min(altered)>0 and altered==altered[::-1] and lc(h) and not lc(altered)
    for power in range(3):assert sum(i**power*v for i,v in enumerate(h))==sum(i**power*v for i,v in enumerate(altered))
    assert altered[:3]==h[:3]
    # Actual nonreal factor controls, not new root-property claims.
    # Evaluating at z^2+1=0 amounts to alternating even/odd coefficient sums.
    p=product(8);assert sum(v*((-1)**(i//2)) for i,v in enumerate(p) if not i%2)==0
    assert sum(v*((-1)**(i//2)) for i,v in enumerate(p) if i%2)==0
    # Reduction modulo 1+x+x^2 for the actual H6.
    rem=[0,0,0]
    for i,v in enumerate(h):rem[i%3]+=v
    assert rem[0]==rem[1]==rem[2]
    generic=multiply([1,100,1],[1,0,1]);assert not lc(generic)
    extended=multiply([1,100,10000,1000000,10000,100,1],[1,0,1])
    assert not lc(extended)
    uniform=multiply([1,1,1,1],[1,0,0,1]);assert not lc(uniform)
    normal_controls=0
    for m in range(2,33):
        p=[F(comb(2*m,i)) for i in range(2*m+1)]
        p[m]*=1-F(2,m+1)
        assert min(p)>0 and not lc(p)
        normal_controls+=1
    receipt={'status':'PASS','binary_boundary_controls':boundary_cases,'literal_binary_sum_controls':literal,
             'product_controls_through_n':40,'actual_ULC_obstructions':non_ulc,
             'same_moment_control':{'actual_H6':h,'altered_auxiliary_array':altered,'degree':10,'variance':'176/39'},
             'generic_gapped_convolution_control':generic,
             'extended_support_convolution_control':extended,
             'uniform_geometric_control':uniform,
             'regrouping_and_n_recurrence_controls':20,
             'same_normal_limit_obstruction_controls':normal_controls,
             'scope':'All-size boundary inequalities, binary ULC obstruction and product CLT rely on written proofs; finite full-array LC is only evidence.'}
    (HERE/'BOUNDARY-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))

if __name__=='__main__':main()
