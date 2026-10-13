#!/usr/bin/env python3
"""Independent exact crown Sturm and weak-order factor controls."""
from pathlib import Path
from fractions import Fraction
from math import comb
from itertools import product
from collections import Counter
from hashlib import sha256
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/'posets'
def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p
def conv(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return trim(r)
def plus(p,q):
    r=p+[0]*max(0,len(q)-len(p))
    for i,c in enumerate(q):r[i]+=c
    return trim(r)
def sturm_negative(p):
    p=trim([Fraction(c) for c in p]);s=[p]
    if len(p)==1:return 0
    s.append([i*p[i] for i in range(1,len(p))])
    while len(s[-1])>1:
        a=s[-2][:];b=s[-1]
        while len(a)>=len(b) and any(a):
            c=a[-1]/b[-1];j=len(a)-len(b)
            for i,v in enumerate(b):a[i+j]-=c*v
            trim(a)
        if not any(a):break
        a=[-c for c in a];positive=abs(a[-1]);a=[c/positive for c in a];s.append(a)
    def changes(values):
        v=[1 if x>0 else -1 for x in values if x]
        return sum(a!=b for a,b in zip(v,v[1:]))
    at_minus_infinity=[p[-1]*(-1)**(len(p)-1) for p in s]
    at_zero=[p[0] for p in s]
    return changes(at_minus_infinity)-changes(at_zero)
def extensions(n):
    rel={(i,n+i) for i in range(1,n+1)}|{(i%n+1,n+i) for i in range(1,n+1)}
    out=Counter()
    def walk(prefix,remaining):
        if not remaining:
            S=tuple(sorted(a for a,b in zip(prefix,prefix[1:]) if a>b));out[S]+=1;return
        for v in sorted(remaining):
            if any(b==v and a in remaining for a,b in rel):continue
            walk(prefix+(v,),remaining-{v})
    walk((),set(range(1,2*n+1)))
    return out
def main():
    receipt_root=json.loads((ROOT/'CROWN-EXPLORATION.json').read_text())
    gamma_controls=[]
    for case in receipt_root['cases']:
        g=case['gamma'];assert g[0]==1
        roots=sturm_negative(g)
        assert roots==len(trim(g[:]))-1==case['negative_gamma_roots']
        D=len(case['hstar'])-1;rebuild=[0]*(D+1)
        for j,c in enumerate(g):
            for i in range(D-2*j+1):rebuild[i+j]+=c*comb(D-2*j,i)
        assert rebuild==case['hstar']
        gamma_controls.append({'n':case['n'],'negative_gamma_roots':roots})
    trace_controls=0
    for n in range(2,6):
        for m in range(4):
            direct=sum(__import__('functools').reduce(lambda x,y:x*y,
                       (m+1-max(a[i],a[(i+1)%n]) for i in range(n)),1)
                       for a in product(range(m+1),repeat=n))
            k=m+1;matrix=[[min(i+1,j+1) for j in range(k)] for i in range(k)]
            power=[[int(i==j) for j in range(k)] for i in range(k)]
            for _ in range(n):power=[[sum(power[i][h]*matrix[h][j] for h in range(k)) for j in range(k)] for i in range(k)]
            assert direct==sum(power[i][i] for i in range(k));trace_controls+=1
    counts=extensions(3)
    h=[sum(c for S,c in counts.items() if len(S)==j) for j in range(5)]
    assert h==receipt_root['cases'][1]['hstar']
    four=[0,0,0,0]
    for S,c in counts.items():
        if 5 in S or 6 in S:continue
        c*=(-2)**(4 in S)
        four[(2 in S)+2*(3 in S)]+=c
    assert four==[-1,-1,3,1] and four[1]*four[2]-four[0]*four[3]==-2
    weak_controls=0
    for N in range(1,13):
        for k in range(N//2+1):
            b=N-k;Q0=[1];Q1=[b-1,2]
            if k==0:Q=Q0
            elif k==1:Q=Q1
            else:
                for r in range(1,k):Q0,Q1=Q1,plus(conv([b-1,2],Q1),[r*(r+b)*c for c in Q0])
                Q=Q1
            pref=[1]
            for s in range(b):pref=conv(pref,[s,1])
            direct=[0]
            for j in range(k+1):
                term=[comb(k,j)]
                for s in range(-j,N-j):term=conv(term,[s,1])
                direct=plus(direct,term)
            assert direct==conv(pref,Q) and min(direct)>=0
            weak_controls+=1
    receipt={'status':'PASS','independent_gamma_Sturm':gamma_controls,
        'direct_assignment_and_matrix_trace_controls':trace_controls,
        'topological_extension_descent_row_C6':h,'actual_Rayleigh_coefficients':four,
        'weak_order_factor_controls':weak_controls,'weak_order_N_range':[1,12],
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Independent crown bounded roots and exact weak-order controls; all-size proofs assessed separately.'}
    (HERE/'POSET-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
