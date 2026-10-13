#!/usr/bin/env python3
"""Exact finite BGW inclusion couplings via integer max flow."""
from collections import deque
from functools import lru_cache
from itertools import product
import json
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent

@lru_cache(None)
def forests(n):
    if n==0:return ((),)
    return tuple((t,)+f for k in range(1,n+1) for t in trees(k) for f in forests(n-k))

@lru_cache(None)
def trees(n):return forests(n-1)

@lru_cache(None)
def deletions(t):
    out=set()
    if t and not t[-1]:out.add(t[:-1])
    for i,c in enumerate(t):
        for d in deletions(c):out.add(t[:i]+(d,)+t[i+1:])
    return frozenset(out)

def weight(t,w):
    if len(t)>=len(w):return 0
    v=w[len(t)]
    for c in t:v*=weight(c,w)
    return v

def maxflow(ad,s,t):
    total=0
    while True:
        levels=[-1]*len(ad);levels[s]=0;q=deque([s])
        while q:
            v=q.popleft()
            for dest,rev,cap in ad[v]:
                if cap and levels[dest]<0:levels[dest]=levels[v]+1;q.append(dest)
        if levels[t]<0:return total
        curs=[0]*len(ad)
        def push(v,limit):
            if v==t:return limit
            while curs[v]<len(ad[v]):
                e=ad[v][curs[v]];dest,rev,cap=e
                if cap and levels[dest]==levels[v]+1:
                    sent=push(dest,min(limit,cap))
                    if sent:e[2]-=sent;ad[dest][rev][2]+=sent;return sent
                curs[v]+=1
            return 0
        while True:
            sent=push(s,sum(e[2] for e in ad[s]))
            if not sent:break
            total+=sent

def couple(n,w):
    left={t:weight(t,w) for t in trees(n) if weight(t,w)}
    right={t:weight(t,w) for t in trees(n+1) if weight(t,w)}
    zn=sum(left.values());zp=sum(right.values());assert zn and zp
    li={v:i+1 for i,v in enumerate(left)}
    ri={v:i+1+len(left) for i,v in enumerate(right)}
    sink=1+len(left)+len(right);ad=[[] for _ in range(sink+1)]
    def edge(a,b,c):
        ad[a].append([b,len(ad[b]),c]);ad[b].append([a,len(ad[a])-1,0])
    for t,v in left.items():edge(0,li[t],v*zp)
    for t,v in right.items():
        edge(ri[t],sink,v*zn)
        for d in deletions(t):
            if d in li:edge(li[d],ri[t],zn*zp)
    flow=maxflow(ad,0,sink)
    return {'n':n,'Z_n':zn,'Z_next':zp,'left_trees':len(left),'right_trees':len(right),
            'flow':flow,'required':zn*zp,'feasible':flow==zn*zp}

def main():
    for n in range(1,10):assert len(trees(n))==comb(2*(n-1),n-1)//n
    # Every deletion is a literal Ulam-Harris inclusion, not a relabelled embedding.
    def vertices(t,prefix=()):
        return {prefix}.union(*(vertices(c,prefix+(i+1,)) for i,c in enumerate(t)))
    for n in range(2,9):
        for t in trees(n):
            vt=vertices(t)
            expected={d for d in trees(n-1) if vertices(d)<=vt}
            assert deletions(t)==expected
    controls=[]
    for w in [(1,1,2),(1,2,1),(1,2,3,5),(1,1,2,4),(1,1,2,2)]:
        rec=[couple(n,w) for n in range(1,12 if w==(1,2,3,5) else 8)]
        controls.append({'weights':list(w),'log_concave':all(w[k]**2>=w[k-1]*w[k+1] for k in range(1,len(w)-1)),
                         'pairs':rec,'passes_all_tested':all(r['feasible'] for r in rec)})
    assert not controls[0]['pairs'][2]['feasible']
    assert all(r['feasible'] for r in controls[1]['pairs'])
    payload={'status':'PASS','tree_counts_verified_through_n':9,
             'all_literal_deletion_relations_verified_through_n':8,
             'controls':controls,'scope':'Finite pairs n=1..11 for (1,2,3,5), n=1..7 for the controls. No infinite coupling is claimed for non-log-concave weights.'}
    (HERE/'TRANSPORT-CHECK.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps({**{k:v for k,v in payload.items() if k!='controls'},
                      'summary':[{'weights':r['weights'],'passes':r['passes_all_tested'],
                                  'first_obstruction':next((p['n'] for p in r['pairs'] if not p['feasible']),None)} for r in controls]}))

if __name__=='__main__':main()
