#!/usr/bin/env python3
"""Exact full independent-set rows on deterministic G(n,d/n) samples."""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
from hashlib import sha256
import json,random
HERE=Path(__file__).resolve().parent

def graph(n,edges):
    adj=[0]*n
    for i,j in edges:adj[i]|=1<<j;adj[j]|=1<<i
    return tuple(adj)

def independent_row(adj):
    @lru_cache(None)
    def solve(mask):
        if not mask:return (1,)
        verts=[i for i in range(len(adj)) if mask>>i&1]
        # Isolated vertices are an exact (1+x) factor, avoiding needless branches.
        isolated=[i for i in verts if not adj[i]&mask]
        if isolated:
            other=mask
            for i in isolated:other^=1<<i
            a=solve(other);b=[comb(len(isolated),j) for j in range(len(isolated)+1)]
            out=[0]*(len(a)+len(b)-1)
            for i,u in enumerate(a):
                for j,v in enumerate(b):out[i+j]+=u*v
            return tuple(out)
        v=max(verts,key=lambda i:(adj[i]&mask).bit_count())
        a=solve(mask^(1<<v));b=solve(mask&~((1<<v)|adj[v]))
        return tuple((a[j] if j<len(a) else 0)+(b[j-1] if 1<=j<=len(b) else 0)
                     for j in range(max(len(a),len(b)+1)))
    out=list(solve((1<<len(adj))-1))
    assert out[:2]==[1,len(adj)]
    if len(out)>2:assert out[2]==comb(len(adj),2)-sum(x.bit_count() for x in adj)//2
    return out,solve.cache_info().currsize

def violations(a):
    return [i for i in range(1,len(a)-1) if a[i]**2<a[i-1]*a[i+1]]

def tree_344():
    edges=[(0,i) for i in (1,2,3)];nextv=4
    for root,arms in zip((1,2,3),(3,4,4)):
        for _ in range(arms):edges.extend([(root,nextv),(nextv,nextv+1)]);nextv+=2
    assert nextv==26
    return graph(26,edges),edges

def main():
    rng=random.Random(2400);records=[]
    for n in (24,32,40,48):
        for d in (8,12,16):
            for trial in range(12):
                edges=[(i,j) for i,j in combinations(range(n),2) if rng.random()<d/n]
                a,states=independent_row(graph(n,edges))
                records.append({'n':n,'d':d,'trial':trial,'edges':edges,'row':a,
                                'LC_failures':violations(a),'memo_states':states})
    tree,edges=tree_344();t,states=independent_row(tree)
    assert t==[1,26,300,2040,9142,28551,63933,103736,121376,100144,55499,18683,2979,51,1]
    assert violations(t)==[13]
    receipt={'status':'PASS','samples':len(records),'records':records,
        'non_LC_samples':[r for r in records if r['LC_failures']],
        'known_26_vertex_tree':{'edges':edges,'row':t,'failure':13,'defect':51**2-2979},
        'scope':'Finite actual Erdős–Rényi samples; known tree independently constructed. No asymptotic catalog closure.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'GRAPH-PROBE.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ('records','known_26_vertex_tree')},indent=2))
if __name__=='__main__':main()
