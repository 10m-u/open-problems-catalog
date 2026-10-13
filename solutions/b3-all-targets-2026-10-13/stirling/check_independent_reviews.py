#!/usr/bin/env python3
"""Independent exact interval witnesses and bounded ceiling/path controls."""
from functools import lru_cache
from itertools import product
from math import comb, factorial
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sympy as S


def lc(c):
    return all(c[i]**2 >= c[i-1]*c[i+1] for i in range(1,len(c)-1))


def ulc(c, d=None):
    if d is None:
        d=len(c)-1
    return all(i*(d-i)*c[i]**2 >= (i+1)*(d-i+1)*c[i-1]*c[i+1]
               for i in range(1,d))


def bounded(length, cap, horizontal=False, riordan=False, weights=()):
    @lru_cache(None)
    def ways(left, height):
        if left==0:
            return int(height==0)
        ans=0
        if height<cap:
            w=weights[height] if height<len(weights) else 1
            ans+=w*ways(left-1,height+1)
        if height:
            ans+=ways(left-1,height-1)
        if horizontal and (height or not riordan):
            ans+=ways(left-1,height)
        return ans
    return ways(length,0)


def heights(length, horizontal=False, riordan=False, weights=()):
    vals=[bounded(length,h,horizontal,riordan,weights) for h in range(length//2+1)]
    return [v-(vals[i-1] if i else 0) for i,v in enumerate(vals)]


def groups(n, kind, weights=()):
    z=heights(2*n if kind=='A' else 2*(n-1),weights=weights)
    at=lambda i:z[i] if 0<=i<len(z) else 0
    return [0]+[at(2*i-1)+at(2*i) if kind=='A' else at(2*i-2)+at(2*i-1)
                for i in range(1,(n+1)//2+1)]


def tail(n,i,kind):
    if kind=='A':
        return F(4*(2*i+1)*(8*i*(i+1)-3*(n+1))*factorial(2*n+1),
                 factorial(n-2*i+1)*factorial(n+2*i+3))
    return F(8*i*(8*i*i*(2*n-1)-(6*n*n+n-2))*factorial(2*n-2),
             factorial(n-2*i+1)*factorial(n+2*i+1))


def dyck_words(m):
    def rec(up,down,word):
        if down==m:
            yield word
            return
        if up<m:
            yield from rec(up+1,down,word+(1,))
        if down<up:
            yield from rec(up,down+1,word+(-1,))
    yield from rec(0,0,())


def run():
    counts=dict(interval_rounding_pairs=0, single_interval_band_controls=0,
                actual_root_controls=0, tail_formula_controls=0,
                symbolic_tail_ratios=0, endpoint_formula_controls=0,
                dyck_component_controls=0)
    family={(0,0,1,1),(1,1,0,0),(1,0,0,0),(0,1,1,1)}
    band={w for w in product([0,1],repeat=4) if w[0]+w[1]==1}
    rank=lambda f:[sum(sum(w)==j for w in f) for j in range(5)]
    assert rank(family)==[0,1,2,1,0] and ulc(rank(family))
    assert rank(family&band)==[0,1,0,1,0] and not ulc(rank(family&band))
    counts['single_interval_band_controls']+=1
    # Check midpoint feasibility independently for every pair and interval at n=6.
    words=list(product([0,1],repeat=6))
    outputs=set()
    for x,y in product(words,repeat=2):
        hx=[0];hy=[0]
        for u,v in zip(x,y):
            hx.append(hx[-1]+u);hy.append(hy[-1]+v)
        lo=[(u+v)//2 for u,v in zip(hx,hy)]
        hi=[(u+v+1)//2 for u,v in zip(hx,hy)]
        for a in range(6):
            for b in range(a+1,7):
                low,high=sorted([hx[b]-hx[a],hy[b]-hy[a]])
                assert low<=lo[b]-lo[a]<=high
                assert low<=hi[b]-hi[a]<=high
        assert all(z[i+1]-z[i] in [0,1] for z in [lo,hi] for i in range(6))
        counts['interval_rounding_pairs']+=1
        if sum(x)==2 and all(u+v==1 for u,v in zip(x,y)):
            outputs.add((tuple(lo[i+1]-lo[i] for i in range(6)),
                         tuple(hi[i+1]-hi[i] for i in range(6))))
    assert outputs=={((0,1,0,1,0,1),(1,0,1,0,1,0))}
    # Explicit homogeneous M-convex failure in domination support.
    def dominates(v):
        return all(set(v)&set(range(max(1,i-1),min(5,i+1)+1)) for i in range(1,6))
    A,B={2,5},{1,3,5}
    assert dominates(A) and dominates(B)
    assert not dominates({1,5}) and not dominates({3,5})
    assert ulc([0,0,10,1],3) and ulc([0,10,1],2) and ulc([10,1],1)
    assert not ulc([0,10,11,11,1],4)
    assert ulc([1,2,1],2) and ulc([0,0,1],2) and not ulc([1,2,1,1],3)
    X=S.Symbol('X')
    assert S.discriminant(X**3+5*X**2+8*X+3,X)==-31
    assert S.discriminant(15+20*X+15*X**2,X)==-500

    for n in range(1,31):
        for kind in ['A','B']:
            c=groups(n,kind)
            threshold=(n+5)//4 if kind=='A' else (n+2)//4+1
            for i in range(threshold,len(c)):
                assert c[i]==tail(n,i,kind)
                counts['tail_formula_controls']+=1
            assert ulc(c)
    # Exact polynomial ratio identities for each parity/sigma.
    i,d=S.symbols('i d')
    for even in [True,False]:
        n=2*d if even else 2*d-1
        for sigma in [1,3]:
            raw=i*(n-2*i+3)*(n-2*i+2)/((d-i+1)*(n+2*i+sigma)*(n+2*i+sigma-1))
            if even:
                proposed=2*i*(2*d-2*i+3)/((2*d+2*i+sigma-1)*(2*d+2*i+sigma))
                numerator=i*(2*d-2*i+3)
                assert S.expand(numerator.subs(i,i+1)-numerator)==2*d+1-4*i
            else:
                proposed=2*i*(2*d-2*i+1)/((2*d+2*i+sigma-2)*(2*d+2*i+sigma-1))
                numerator=i*(2*d-2*i+1)
                assert S.expand(numerator.subs(i,i+1)-numerator)==2*d-1-4*i
            assert S.cancel(raw-proposed)==0
            counts['symbolic_tail_ratios']+=1

    actuals=[('A17',groups(17,'A'),8,6),('B16',groups(16,'B'),7,5),
             ('M11',[0]+heights(11,True),5,3),
             ('R12',[0]+heights(12,True,True),5,3)]
    for name,c,degree,reals in actuals:
        start=next(j for j,v in enumerate(c) if v)
        p=S.Poly(sum(v*X**(j-start) for j,v in enumerate(c)),X)
        assert p.degree()==degree and p.count_roots(-S.oo,S.oo)==reals
        assert S.gcd(p,p.diff()).degree()==0
        counts['actual_root_controls']+=1
    assert heights(14)==[0,1,63,169,132,52,11,1] and not ulc(heights(14))
    assert groups(7,'A',(1,1,1,1,1,1,10000))==[0,64,301,63,10000]
    assert not ulc(groups(7,'A',(1,1,1,1,1,1,10000)))
    assert [0]+heights(6,True,False,(1,1,100))==[0,1,31,18,100]
    assert [0]+heights(6,True,True,(1,1,100))==[0,0,5,9,100]
    assert not lc([0,1,31,18,100]) and not lc([0,0,5,9,100])

    m,u=S.symbols('m u')
    choose=lambda n,k:S.prod(n-j for j in range(k))/factorial(k)
    H=2*m*m-7*m+3
    endpoint={
      'Meven':(1,2*m*m+m-3,H+(2*m-5)*choose(2*m,2)+choose(2*m,4)),
      'Modd':(2*m+1,(2*m-3)*(2*m+1)+choose(2*m+1,3),
              H*(2*m+1)+(2*m-5)*choose(2*m+1,3)+choose(2*m+1,5)),
      'Reven':(1,m*(2*m-3),H+(2*m-7)*choose(2*m-2,2)+2*choose(2*m-3,2)+choose(2*m-2,4)),
      'Rodd':(2*m-1,(2*m-5)*(2*m-1)+4*m-4+choose(2*m-1,3),
              (2*m-1)*(2*m*m-11*m+12)+(2*m-2)*(4*m-12)+3*(2*m-3)
              +(2*m-7)*choose(2*m-1,3)+2*choose(2*m-2,3)+choose(2*m-1,5))}
    expected={
      'Meven':[F(10,3),F(206,3),F(3163,6),F(10709,6),F(2251)],
      'Modd':[F(56,45),F(656,15),F(5704,9),F(4838),F(1845853,90),F(1374593,30),F(42229)],
      'Reven':[F(10,3),F(166,3),F(2071,6),F(5767,6),F(1011)],
      'Rodd':[F(56,45),F(544,15),F(3952,9),F(2822),F(912793,90),F(579847,30),F(15283)]}
    for name,(a,b,c) in endpoint.items():
        defect=S.Poly(S.expand((b*b-a*c).subs(m,u+5)),u)
        assert defect.all_coeffs()==[S.Rational(v.numerator,v.denominator) for v in expected[name]]
        for q in range(5,13):
            length=2*q+int('odd' in name)
            z=heights(length,True,name.startswith('R'))
            assert z[-1:-4:-1]==[int(S.sympify(v).subs(m,q)) for v in [a,b,c]]
            counts['endpoint_formula_controls']+=1
    for q in range(5,9):
        by_components={}
        for word in dyck_words(q):
            h=mx=k=0
            for step in word:
                h+=step;mx=max(mx,h);k+=int(h==0)
            if mx==q-2:
                by_components[k]=by_components.get(k,0)+1
        assert by_components=={1:2*q*q-11*q+12,2:4*q-12,3:3}
        counts['dyck_component_controls']+=1
    for length in range(10):
        for riordan in [False,True]:
            z=heights(length,True,riordan)
            if len(z)>=3:
                assert z[-2]**2>=z[-1]*z[-3]

    receipt=dict(schema='b3-independent-interval-path-audit-v1',passed=True,
                 counts=counts,midpoint_output_count=len(outputs),
                 single_band_intersection_rank_counts=rank(family&band),
                 scope='Independent bounded arithmetic/transcription controls; all-size proofs reviewed in INTERVAL-PATH-REVIEW.md.',
                 checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_name('INDEPENDENT-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))


if __name__=='__main__':
    run()

