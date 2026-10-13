#!/usr/bin/env python3
"""Exact finite controls for continuum proofs and failed rainbow routes."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent


def rectangle(a,b,c,d,t):
    pos=lambda x:max(x,F(0))**2
    return (pos(t-a-c)-pos(t-b-c)-pos(t-a-d)+pos(t-b-d))/2


def complement(intervals):
    result=[];last=F(0)
    for a,b in intervals:
        if last<a:result.append((last,a))
        last=b
    if last<1:result.append((last,F(1)))
    return result


def measure(intervals):
    return sum((b-a for a,b in intervals),F(0))


def area(first,second):
    return sum((rectangle(a,b,c,d,F(1)) for a,b in first for c,d in second),F(0))


def gradient(intervals,x):
    a=measure(intervals)
    partial=sum((max(F(0),min(b,1-x)-aa) for aa,b in intervals),F(0))
    return 1-2*a+(1-x)-2*partial


def rainbow(c,shift=0):
    n=len(c)-1
    return sum(len({c[a],c[b],c[a+b-shift]})==3
               for a in range(1,n+1) for b in range(1,n+1)
               if 1<=a+b-shift<=n)


def source(n):
    return [0]+[3 if i%2==0 else 1 if 11*i<=4*n or 11*i>10*n else 2
                for i in range(1,n+1)]


def prefix_value(a,b):
    A=rectangle(F(0),a,a,b,F(1))-rectangle(F(0),a,a,b,b)
    B=rectangle(F(0),b,b,F(1),F(1))
    return 4*A+2*B


def main():
    stationary=[]; gradient_checks=0
    for j in range(21):
        q=F(1,12*j+11);intervals=[]
        for r in range(j+1):
            for lo,hi in [(12*r*q,(12*r+4)*q),((12*r+10)*q,(12*r+12)*q)]:
                if lo<1:intervals.append((lo,min(F(1),hi)))
        other=complement(intervals);a=measure(intervals)
        value=a*(1-a)+area(intervals,other)
        assert value==3*(1+q)/8 and value<=F(9,22)
        assert a==F(6*j+5,12*j+11)
        points={F(0),F(1)}
        for aa,bb in intervals:
            points.update([aa,bb,1-aa,1-bb])
        points=sorted(points)
        for left,right in zip(points,points[1:]):
            x=(left+right)/2
            u,v=gradient(intervals,x),gradient(intervals,1-x)
            assert abs(u)+abs(v)==3*q
            assert (u>0)==any(aa<x<bb for aa,bb in intervals)
            gradient_checks+=1
        assert gradient(intervals,F(0))==2*q
        assert gradient(intervals,F(1))==q
        stationary.append({'j':j,'q':str(q),'F':str(value)})
    maxima=[];parity_checks=0
    for n in range(2,27):
        odds=list(range(1,n+1,2));m=len(odds);best=0
        for mask in range(1<<m):
            a={odds[i] for i in range(m) if mask>>i&1}
            b=set(odds)-a
            direct=2*len(a)*len(b)+2*sum(x+y<=n for x in a for y in b)
            if n<=10:
                c=[0]+[3 if i%2==0 else 1 if i in a else 2 for i in range(1,n+1)]
                assert rainbow(c)==direct
            best=max(best,direct);parity_checks+=1
        maxima.append([n,best])
    base=source(22);r=rainbow(base);s=rainbow(base,1)
    assert r==102 and s==0
    dilation=[]
    for t in [2,3,5,8]:
        lifted=[0]+[base[(i-1)//t+1] for i in range(1,22*t+1)]
        exact=rainbow(lifted)
        assert exact==r*t*(t+1)//2+s*t*(t-1)//2
        dilation.append([t,exact])
    increment_checks=0
    for n in range(2,101,2):
        c=[0]+[1 if i%2 else 2 for i in range(1,n+1)]
        assert rainbow(c)==0
        c.append(3);assert rainbow(c)==n
        increment_checks+=1
    prefix_checks=0;best=(F(0),None);branch_checks=[0]*5
    for ai in range(57):
        for bi in range(ai,57):
            a,b=F(ai,56),F(bi,56);value=prefix_value(a,b)
            assert value<=F(3,7)
            if value>best[0]:best=(value,(a,b))
            if b>=F(1,2):
                if a>=F(1,2):idx=0;bound=F(1,3);p=4*(b-a)*(1-b)+(1-b)**2
                elif a+b<=1 and b>=2*a:idx=1;bound=F(3,8);p=2*a*a+(1-b)**2
                elif a+b<=1:idx=2;bound=F(5,12);p=8*a*b-6*a*a-b*b-2*b+1
                elif b>=2*a:idx=3;bound=F(1,3);p=4*a*(1-b)-(1-b)**2
                else:idx=4;bound=F(2,5);p=4*a*b-8*a*a-3*b*b+4*a+2*b-1
                assert p==value and p<=bound
                branch_checks[idx]+=1
            prefix_checks+=1
    assert best==(F(3,7),(F(2,7),F(3,7)))
    S=[(F(0),F(4,11)),(F(10,11),F(1))];T=complement(S)
    assert measure(S)==F(5,11) and area(S,S)==F(17,121)
    assert measure(T)==F(6,11) and area(T,T)==F(9,242)
    gains=[(measure(z)**2+area(z,z))/4 for z in [S,T]]
    assert gains==[F(21,242),F(81,968)]
    assert F(9,22)+gains[0]==F(60,121)
    assert F(9,22)+gains[1]==F(477,968)
    assert max(F(3,7),F(60,121))<F(50368,90905)
    # Independently enumerate every splitting assignment on a small instance.
    c=source(12);old=rainbow(c);split_checks=0
    for colour in [1,2,3]:
        positions=[i for i in range(1,13) if c[i]==colour]
        total=0
        for mask in range(1<<len(positions)):
            new=c[:]
            for j,i in enumerate(positions):
                if mask>>j&1:new[i]=4
            total+=rainbow(new);split_checks+=1
        repeated=0
        for x in range(1,13):
            for y in range(1,13-x):
                if x==y:continue
                cs=[c[x],c[y],c[x+y]]
                if len(set(cs))==2 and cs.count(colour)==2:repeated+=1
        assert F(total,1<<len(positions))==old+F(repeated,2)
    # Histogram arrangement's exact continuum count.
    first=[(F(0),F(5,22))];second=[(F(5,22),F(1,2))]
    cross=sum((rectangle(a,b,c,d,F(1))-rectangle(a,b,c,d,F(1,2)) for a,b in first for c,d in second),F(0))
    assert cross==F(25,968) and 4*cross==F(25,242)
    out={'status':'passed','stationary_family':stationary,
         'reflected_gradient_piece_controls':gradient_checks,
         'parity_colourings_exhausted':parity_checks,'bounded_parity_maxima':maxima,
         'carry_base':[r,s],'block_dilation_controls':dilation,
         'append_increment_controls':increment_checks,
         'two_prefix_grid_controls':prefix_checks,'two_prefix_branch_controls':branch_checks,
         'two_prefix_exact_optimum':str(best[0]),
         'independent_split_assignments':split_checks,
         'parity_split_limiting_values':['60/121','477/968','9/22'],
         'scope':'Exact finite controls of local restricted proofs and failed full-target methods; prior four-colour lower bound retained, no unrestricted closure.'}
    (HERE/'COLOUR-CHECK-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'stationary_family','bounded_parity_maxima'}}))


if __name__=='__main__':main()
