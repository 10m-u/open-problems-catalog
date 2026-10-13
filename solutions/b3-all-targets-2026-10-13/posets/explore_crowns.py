#!/usr/bin/env python3
from pathlib import Path
from math import comb
from itertools import permutations,combinations,product
from collections import Counter
import sympy as sp,json
from hashlib import sha256
HERE=Path(__file__).resolve().parent
t=sp.Symbol('t')
def tracepower(k,n):
    e=[comb(k+j,2*j) if j<=k else 0 for j in range(n+1)]
    p=[0]*(n+1)
    for r in range(1,n+1):
        p[r]=sum((-1)**(i-1)*e[i]*p[r-i] for i in range(1,r))+(-1)**(r-1)*r*e[r]
    return p[n]
def hstar(n):
    E=[tracepower(m+1,n) for m in range(2*n+1)]
    h=[sum((-1)**i*comb(2*n+1,i)*E[j-i] for i in range(j+1)) for j in range(2*n+1)]
    assert h[-2:]==[0,0] and h[:-2]==h[-3::-1]
    return h[:-2]
def gamma(h):
    out=[];rem=h[:];D=len(h)-1
    for j in range(D//2+1):
        c=rem[j];out.append(c)
        for k in range(D-2*j+1):rem[j+k]-=c*comb(D-2*j,k)
    assert not any(rem)
    return out
def refinements(n):
    rel=[(i,n+i) for i in range(1,n+1)]+[((i%n)+1,n+i) for i in range(1,n+1)]
    counts=Counter()
    for p in permutations(range(1,2*n+1)):
        pos={v:i for i,v in enumerate(p)}
        if any(pos[a]>pos[b] for a,b in rel):continue
        # Descent-top values, rather than descent positions.
        counts[tuple(sorted(a for a,b in zip(p,p[1:]) if a>b))]+=1
    return counts
def rayleigh(counts,i,j,values):
    sums=[0,0,0,0]
    for S,c in counts.items():
        v=c
        for a in S:
            if a not in (i,j):v*=values.get(a,1)
        sums[(i in S)+2*(j in S)]+=v
    a,b,c,d=sums
    return b*c-a*d,sums
def main():
    cases=[];recurrence=None;witness=None
    H={}
    for n in range(2,21):
        h=hstar(n);g=gamma(h);H[n]=sp.Poly(sum(c*t**i for i,c in enumerate(h)),t)
        p=sp.Poly(sum(c*t**i for i,c in enumerate(g)),t)
        real=int(p.count_roots(-sp.oo,0))
        assert real==p.degree() and min(g)>=0
        cases.append({'n':n,'hstar':h,'gamma':g,'negative_gamma_roots':real})
        if n>=3 and recurrence is None:
            D=H[n-1].degree();b,u=sp.symbols('b u');prev=H[n-1].as_expr()
            candidate=(1+b*t+(1+u*D)*t*t)*prev+u*t*(1-t*t)*sp.diff(prev,t)
            diff=sp.Poly(candidate-H[n].as_expr(),t)
            fit=sp.solve([diff.nth(1),diff.nth(2)],(b,u),dict=True)
            if fit and sp.expand(diff.as_expr().subs(fit[0]))!=0:
                recurrence={'n':n,'parameters':{str(k):str(v) for k,v in fit[0].items()},
                            'residual':str(sp.expand(diff.as_expr().subs(fit[0])))}
    for n in (3,4):
        counts=refinements(n)
        assert sum(counts.values())==sum(hstar(n))
        assert [sum(c for S,c in counts.items() if len(S)==k) for k in range(2*n-1)]==hstar(n)
        for i,j in combinations(range(2,2*n+1),2):
            others=[k for k in range(2,2*n+1) if k not in (i,j)]
            for xs in product((-2,0,1,2),repeat=len(others)):
                vals=dict(zip(others,xs));delta,sums=rayleigh(counts,i,j,vals)
                if delta<0:
                    witness={'n':n,'pair':[i,j],'other_values':vals,'delta':delta,
                             'four_coefficients':sums,
                             'full_refined_polynomial':[{'S':list(S),'coefficient':c} for S,c in sorted(counts.items())]}
                    break
            if witness:break
        if witness:break
    result={'status':'PASS','cases':cases,'first_order_recurrence_obstruction':recurrence,
            'actual_descent_top_stability_obstruction':witness,
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Exact crown computations n2..20, with specified method obstructions. No all-n root proof.'}
    (HERE/'CROWN-EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'cases':len(cases),'recurrence':recurrence,
             'stability_obstruction':{k:v for k,v in (witness or {}).items() if k!='full_refined_polynomial'}},indent=2))
if __name__=='__main__':main()
