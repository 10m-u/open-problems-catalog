#!/usr/bin/env python3
"""Exact literal controls and Hall certificate, separate from search/matching DP."""
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from pattern_probe import standardize,literal_downset,layered,unimodal,lc
HERE=Path(__file__).resolve().parent

def contains(s,t):
    return any(standardize(tuple(t[i] for i in inds))==s for inds in combinations(range(len(t)),len(s)))

def literal_interval(s,t):
    return {p for p in literal_downset(t) if contains(s,p)}

def row(s,t):
    cnt=Counter(map(len,literal_interval(s,t)))
    return [cnt[k] for k in range(len(s),len(t)+1)]

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]+=v*w
    return c

def main():
    probe=json.loads((HERE/'PATTERN-PROBE.json').read_text())
    assert len(probe['records'])==1573 and not probe['unimodal_failures']
    h=probe['Hall_obstruction'];s=tuple(h['bottom']);t=tuple(h['top'])
    inter=literal_interval(s,t);assert row(s,t)==[1,3,7,7,1]
    ranks={k:{p for p in inter if len(p)==k} for k in range(3,8)}
    subset=set(map(tuple,h['witness']['left']))
    neighbors={p for p in ranks[6] if any(contains(a,p) for a in subset)}
    assert subset<=ranks[5] and neighbors==set(map(tuple,h['witness']['neighbors']))
    assert len(subset)==5 and len(neighbors)==4 and len(ranks[5])==len(ranks[6])==7
    # A reciprocal/unimodal chain decomposition must pair every tied rank;
    # this actual Hall deficit is independently certified by literal subsets.
    literal_two=0;formula_two=0
    for a in range(1,41):
        for b in range(a,41):
            for ss in range(1,b+1):
                actual=Counter({r:1 for r in range(ss,b+1)})
                for i in range(1,a+1):
                    for j in range(1,b+1):
                        if max(i,j)>=ss:actual[i+j]+=1
                arr=[]
                for r in range(ss,a+b+1):
                    if ss<=a:v=1+2*(r-ss)-max(r-a-1,0)-max(r-b,0)-max(r-2*ss+1,0)
                    else:v=1+r-ss-max(r-b,0)-max(r-a-ss,0)
                    assert v==actual[r]>0;arr.append(v)
                assert lc(arr) and all(arr[j-1]+arr[j+1]<=2*arr[j] for j in range(1,len(arr)-1))
                formula_two+=1
                if a+b<=8:
                    assert row(tuple(range(ss,0,-1)),layered((a,b)))==arr;literal_two+=1
    equal_layers=0
    for L in range(1,5):
        for top in product(range(1,4),repeat=L):
            if sum(top)>9:continue
            for bot in product(*(range(1,a+1) for a in top)):
                expected=[1]
                for a,b in zip(top,bot):expected=conv(expected,[1]*(a-b+1))
                assert row(layered(bot),layered(top))==expected and lc(expected)
                equal_layers+=1
    fiber=[]
    for p in range(5):
        for q in range(5):
            t=tuple(range(1,p+1))+(p+2,p+1)+tuple(range(p+3,p+q+3))
            expected=conv([1]*(p+1),[1]*(q+1));assert row((2,1),t)==expected
            reps=Counter()
            for k in range(2,len(t)+1):
                for inds in combinations(range(len(t)),k):
                    perm=standardize(tuple(t[i] for i in inds))
                    if contains((2,1),perm):reps[perm]+=1
            for u in range(p+1):
                for v in range(q+1):
                    perm=tuple(range(1,u+1))+(u+2,u+1)+tuple(range(u+3,u+v+3))
                    assert reps[perm]==comb(p,u)*comb(q,v)
            fiber.append({'p':p,'q':q,'row':expected})
    t=(2,1,4,3);E=(0,1)
    fixed={standardize(tuple(t[i] for i in inds)) for k in range(2,5)
           for inds in combinations(range(4),k) if set(E)<=set(inds)}
    actual=literal_interval((2,1),t)
    assert (1,3,2) in actual-fixed and row((2,1),t)==[1,2,1]
    assert Counter(map(len,fixed))=={2:1,3:1,4:1}
    t=(2,4,1,3);deleted=[standardize(t[:i]+t[i+1:]) for i in range(4)]
    ds=[literal_interval((1,),p) for p in deleted]
    common=ds[0]&ds[-1]
    assert common=={(1,),(1,2),(2,1)}
    assert row((1,),t)==[1,2,4,1]
    A=[1,3,3,3,1];H=[1,1,3,1,1];union=[2*a-h for a,h in zip(A,H)]
    assert unimodal(A) and unimodal(H) and union==[1,5,3,5,1] and not unimodal(union)
    receipt={'status':'PASS','fresh_construction_intervals':len(probe['records']),
        'actual_Hall_certificate':h,'two_layer_formula_controls':formula_two,
        'two_layer_literal_controls':literal_two,'equal_layer_literal_controls':equal_layers,
        'unique_inversion_fiber_controls':fiber,'fixed_occurrence_missing_pattern':[1,3,2],
        'actual_deletion_intersection_maxima':[[1,2],[2,1]],
        'formal_unimodal_gluing_failure':{'A':A,'B':A,'H':H,'union':union},
        'scope':'Named actual intervals and all-size partial proof controls; formal gluing row is not an actual permutation counterexample.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
        'probe_sha256':sha256((HERE/'pattern_probe.py').read_bytes()).hexdigest()}
    (HERE/'PATTERN-ROUTES-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='unique_inversion_fiber_controls'},indent=2))
if __name__=='__main__':main()
