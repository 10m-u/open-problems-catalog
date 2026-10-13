#!/usr/bin/env python3
"""Descent polynomial of actual Boolean-poset linear extensions by ideal DP."""
from pathlib import Path
from collections import defaultdict
from math import comb
from hashlib import sha256
import sympy as sp,json
HERE=Path(__file__).resolve().parent
t=sp.Symbol('t')
def boolean_h(n):
    if n<=1:return [1],{'internal_elements':max(0,2**n-2),'ideal_states':1}
    nodes=sorted(range(1,2**n-1),key=lambda a:(a.bit_count(),a))
    index={a:i for i,a in enumerate(nodes)};N=len(nodes)
    pred=[]
    for a in nodes:
        pred.append(sum(1<<index[a^(1<<b)] for b in range(n)
                        if a&(1<<b) and (a^(1<<b)) in index))
    # Removing the unique minimum and maximum leaves h* unchanged.
    current={0:{-1:[1]}};states=1;transitions=0
    for size in range(N):
        nxt={}
        for mask,lasts in current.items():
            for v in range(N):
                if mask>>v&1 or pred[v]&mask!=pred[v]:continue
                newmask=mask|(1<<v)
                out=nxt.setdefault(newmask,{}).setdefault(v,[0]*(size+1))
                for last,p in lasts.items():
                    shift=int(last>v)
                    for j,c in enumerate(p):out[j+shift]+=c
                transitions+=1
        states+=len(nxt);current=nxt
    assert list(current)==[(1<<N)-1]
    h=[sum(p[j] for p in current[(1<<N)-1].values()) for j in range(N)]
    while len(h)>1 and h[-1]==0:h.pop()
    assert len(h)-1==2**n-n-1
    assert h==h[::-1] and all(c>0 for c in h)
    return h,{'internal_elements':N,'ideal_states':states,'append_transitions':transitions}
def gamma(h):
    D=len(h)-1;rem=h[:];g=[]
    for j in range(D//2+1):
        c=rem[j];g.append(c)
        for k in range(D-2*j+1):rem[j+k]-=c*comb(D-2*j,k)
    assert not any(rem)
    return g
def main():
    cases=[]
    for n in range(6):
        h,stats=boolean_h(n);g=gamma(h)
        p=sp.Poly(sum(c*t**i for i,c in enumerate(g)),t)
        roots=int(p.count_roots(-sp.oo,0))
        assert roots==p.degree() and all(c>=0 for c in g)
        cases.append({'n':n,'hstar':h,'gamma':g,'negative_gamma_roots':roots,**stats})
        print('n',n,'degree',len(h)-1,'ideals',stats['ideal_states'],'negative gamma roots',roots,flush=True)
    result={'status':'PASS','cases':cases,
            'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Actual Boolean lattices n<=5 only; no induction to arbitrary n.'}
    (HERE/'BOOLEAN-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
