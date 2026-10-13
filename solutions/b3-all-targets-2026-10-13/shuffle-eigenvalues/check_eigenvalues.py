#!/usr/bin/env python3
"""Exact horizontal-strip eigenvalue arithmetic and proposed-route controls."""
from collections import Counter
from hashlib import sha256
from itertools import product, combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
def partitions(n,m=None):
    if n==0:yield ();return
    for a in range(min(n,m or n),0,-1):
        for tail in partitions(n-a,a):yield (a,)+tail
def add(a,b):
    out=[0]*max(len(a),len(b))
    for j,v in enumerate(a):out[j]+=v
    for j,v in enumerate(b):out[j]+=v
    while len(out)>1 and out[-1]==0:out.pop()
    return out
def shift(a,k):return [0]*k+a if any(a) else [0]
def uniform(a,r):
    assert r>0
    out=[];running=0
    for i in range(len(a)+r-1):
        if i<len(a):running+=a[i]
        if 0<=i-r<len(a):running-=a[i-r]
        out.append(running)
    return out
def modes(a):
    return [i for i,v in enumerate(a) if v==max(a)] if any(a) else []
def unimodal(a):
    falling=False
    for x,y in zip(a,a[1:]):
        if y<x:falling=True
        if falling and y>x:return False
    return True
def contents(lam,mu):
    return [col-row for row,(a,b) in enumerate(zip(lam,mu),1) for col in range(b+1,a+1)]
def eigenvalues(j,cs):
    E=[[1]]
    for s,c in enumerate(cs,1):
        n=j+s;new=[[1]]
        for k in range(1,s+1):
            a=shift(E[k],k) if k<len(E) else [0]
            b=uniform(E[k-1],n+1-k+c)
            new.append(add(a,b))
        E=new
    return E
def summands(j,cs,k):
    n=j+len(cs);out=[]
    for sel in combinations(range(len(cs)),k):
        p=[1];ls=[j+i+1 for i in sel]
        for m,(i,l) in enumerate(zip(sel,ls),1):p=uniform(p,l+1-m+cs[i])
        out.append({'labels':ls,'coefficients':shift(p,n*k-k*(k-1)//2-sum(ls))})
    return out
def main():
    count=polys=endpoint_controls=0;bad=None;common=None;recursion_modes=None
    for n in range(15):
        for lam in partitions(n):
            bounds=[range((lam[i+1] if i+1<len(lam) else 0),a+1) for i,a in enumerate(lam)]
            for mu in product(*bounds):
                j=sum(mu);cs=contents(lam,mu);E=eigenvalues(j,cs);count+=1
                for k,p in enumerate(E):
                    polys+=1
                    if not unimodal(p):bad={'lambda':lam,'mu':mu,'k':k,'coefficients':p};break
                if bad:break
                N=len(cs)
                if N:
                    one=[0]
                    for s,c in enumerate(cs,1):one=add(one,shift([1]*(j+s+c),N-s))
                    assert one==E[1]
                    assert all(n+c-1>=N-1 for c in cs)
                    full=[1]
                    for c in cs:full=uniform(full,j+1+c)
                    assert full==E[N];endpoint_controls+=2
                if common is None and 1< N<=7:
                    for k in range(2,N):
                        ss=summands(j,cs,k)
                        mm=set(modes(ss[0]['coefficients']))
                        for term in ss[1:]:mm&=set(modes(term['coefficients']))
                        if not mm:
                            total=[0]
                            for term in ss:total=add(total,term['coefficients'])
                            assert total==E[k]
                            common={'lambda':lam,'mu':mu,'k':k,'contents':cs,
                              'summands':ss,'sum_coefficients':E[k]};break
                if recursion_modes is None and N>=3:
                    prev=eigenvalues(j,cs[:-1])
                    for k in range(2,N):
                        A=shift(prev[k],k);B=uniform(prev[k-1],n+1-k+cs[-1])
                        if not set(modes(A))&set(modes(B)):
                            recursion_modes={'lambda':lam,'mu':mu,'k':k,'left':A,'right':B,'sum':E[k]};break
            if bad:break
        if bad:break
    p=eigenvalues(2,[1,-2])[1]
    assert p==[1,2,1,1,1] and p[2]**2<p[1]*p[3]
    assert p!=p[::-1]
    synthetic=add(shift([1],2),uniform(shift([1],5),3))
    assert not unimodal(synthetic)
    receipt={'status':'PASS' if bad is None else 'ACTUAL_COUNTEREXAMPLE',
      'all_horizontal_strips_through_n':14,'horizontal_strips':count,'polynomials':polys,
      'endpoint_identity_controls':endpoint_controls,'unimodality_counterexample':bad,
      'actual_log_concavity_and_symmetry_obstruction':p,
      'actual_summands_without_common_mode':common,
      'actual_recursion_terms_without_common_mode':recursion_modes,
      'unrestricted_unimodal_recursion_obstruction':synthetic,
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Exact bounded strip enumeration and endpoint identities; no arbitrary-n full closure.'}
    (HERE/'CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ['actual_summands_without_common_mode','actual_recursion_terms_without_common_mode']},indent=2))
    print('mode_control',common)
    print('recursion_control',recursion_modes)
if __name__=='__main__':main()
