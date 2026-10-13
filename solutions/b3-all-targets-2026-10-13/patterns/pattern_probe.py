#!/usr/bin/env python3
"""Distinct classical patterns, fresh interval constructions and matching probes."""
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
from hashlib import sha256
import json, random
HERE=Path(__file__).resolve().parent

def standardize(p):
    ranks={v:i+1 for i,v in enumerate(sorted(p))}
    return tuple(ranks[v] for v in p)

@lru_cache(None)
def downset(p):
    out={p}
    if p:
        for i in range(len(p)):out.update(downset(standardize(p[:i]+p[i+1:])))
    return frozenset(out)

def literal_downset(p):
    return frozenset(standardize(tuple(p[i] for i in inds))
                    for k in range(len(p)+1) for inds in combinations(range(len(p)),k))

def interval(s,t):
    return {p for p in downset(t) if s in downset(p)}

def rankrow(s,t):
    cnt=Counter(map(len,interval(s,t)))
    return [cnt[k] for k in range(len(s),len(t)+1)]

def unimodal(a):
    falling=False
    for x,y in zip(a,a[1:]):
        if y<x:falling=True
        elif y>x and falling:return False
    return True

def lc(a):
    return all(a[i]**2>=a[i-1]*a[i+1] for i in range(1,len(a)-1))

def layered(parts):
    p=[];shift=0
    for a in parts:
        p.extend(range(shift+a,shift,-1));shift+=a
    return tuple(p)

def match_smaller(left,right):
    """Return an explicit deficient Hall subset if no matching saturates smaller rank."""
    if len(left)>len(right):left,right=right,left
    edges={a:{b for b in right if (a in downset(b) if len(a)<len(b) else b in downset(a))}
           for a in left}
    matched={}
    def augment(a,seen):
        for b in sorted(edges[a]):
            if b in seen:continue
            seen.add(b)
            if b not in matched or augment(matched[b],seen):
                matched[b]=a;return True
        return False
    for a in sorted(left):augment(a,set())
    if len(matched)==len(left):return None
    unmatched=set(left)-set(matched.values());aa=set(unmatched);bb=set();todo=list(unmatched)
    while todo:
        a=todo.pop()
        for b in edges[a]:
            if b in bb:continue
            bb.add(b)
            if b in matched and matched[b] not in aa:
                aa.add(matched[b]);todo.append(matched[b])
    assert len(bb)<len(aa)
    return {'smaller_rank':len(next(iter(left))), 'left':sorted(aa),'neighbors':sorted(bb),
            'left_size':len(left),'right_size':len(right),'matched':len(matched)}

def main():
    rng=random.Random(1366)
    tops=set()
    for n in range(8,13):
        for _ in range(8):
            p=list(range(1,n+1));rng.shuffle(p);tops.add(tuple(p))
        for a in range(2,n-1):tops.add(layered((a,n-a)))
        tops.add(tuple(range(2,n+1,2))+tuple(range(1,n+1,2)))
    rows=[]
    for t in sorted(tops,key=lambda p:(len(p),p)):
        assert downset(t)==literal_downset(t)
        for s in sorted(p for p in downset(t) if 1<=len(p)<=4):
            a=rankrow(s,t)
            rows.append({'bottom':s,'top':t,'row':a,'unimodal':unimodal(a),'LC':lc(a)})
    # A separate stronger cover-matching route; old rank-unimodality controls are not recounted.
    hall=None;tested=0
    for n in range(4,8):
        for t in permutations(range(1,n+1)):
            for s in sorted(p for p in downset(t) if p and len(p)<=n-2):
                inter=interval(s,t);ranks={k:{p for p in inter if len(p)==k} for k in range(len(s),n+1)}
                for k in range(len(s),n):
                    tested+=1;h=match_smaller(ranks[k],ranks[k+1])
                    if h:
                        hall={'bottom':s,'top':t,'row':rankrow(s,t),'witness':h};break
                if hall:break
            if hall:break
        if hall:break
    receipt={'status':'PASS','fresh_top_lengths':[8,12],'actual_tops':len(tops),
             'actual_intervals':len(rows),'unimodal_failures':[r for r in rows if not r['unimodal']],
             'records':rows,'adjacent_rank_matchings_tested':tested,'Hall_obstruction':hall,
             'scope':'Fresh bounded counter-constructions and separate actual cover-matching contract; no infinite closure.',
             'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'PATTERN-PROBE.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='records'},indent=2))
if __name__=='__main__':main()
