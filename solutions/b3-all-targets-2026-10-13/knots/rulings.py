#!/usr/bin/env python3
"""Exact Definition 2.1 permutation walks, using LEFT simple reflections."""
from collections import Counter
from itertools import permutations
from functools import lru_cache

@lru_cache(None)
def actions(n):
    states=tuple(permutations(range(1,n+1)))
    index={p:j for j,p in enumerate(states)}
    data={}
    for i in range(1,n):
        data[i]=[]
        for p in states:
            q=tuple(i+1 if a==i else i if a==i+1 else a for a in p)
            data[i].append((index[q],p.index(i)>p.index(i+1)))
    return states,index,data

def endpoint_rows(n,word):
    states,index,data=actions(n)
    w0=tuple(range(n,0,-1));current={index[w0]:Counter({0:1})}
    for i in word:
        assert 1<=i<n
        new={}
        for j,row in current.items():
            k,descent=data[i][j]
            dest=new.setdefault(k,Counter())
            for d,c in row.items():dest[d]+=c
            if descent:
                dest=new.setdefault(j,Counter())
                for d,c in row.items():dest[d+1]+=c
        current=new
    return {states[j]:dict(row) for j,row in current.items()}

def components(n,word):
    p=tuple(range(1,n+1))
    for i in word:p=tuple(i+1 if a==i else i if a==i+1 else a for a in p)
    seen=set();count=0
    for i in range(1,n+1):
        if i in seen:continue
        count+=1;j=i
        while j not in seen:seen.add(j);j=p[j-1]
    return count

def row(n,word):
    b=components(n,word)
    raw=endpoint_rows(n,word).get(tuple(range(n,0,-1)),{})
    normalized={}
    for s,c in raw.items():
        assert s-n+b>=0 and (s-n+b)%2==0,(n,word,s,b)
        normalized[(s-n+b)//2]=c
    return [normalized.get(j,0) for j in range(max(normalized,default=-1)+1)]

def violations(a):
    local=[j for j in range(1,len(a)-1) if a[j]**2<a[j-1]*a[j+1]]
    positive=[j for j,c in enumerate(a) if c]
    holes=[j for j in range(min(positive,default=0),max(positive,default=-1)+1) if not a[j]]
    return local,holes

def dense_parity(raw):
    if not raw:return []
    low=min(raw);high=max(raw)
    assert all((j-low)%2==0 for j in raw)
    return [raw.get(j,0) for j in range(low,high+1,2)]
