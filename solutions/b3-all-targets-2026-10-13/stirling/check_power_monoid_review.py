#!/usr/bin/env python3
"""Independent Q2212 checker: test decompositions inside each proposed atom."""
from itertools import combinations
from collections import Counter
from math import comb
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
def subsets(A):
    positive=sorted(set(A)-{0})
    for k in range(1,len(positive)+1):
        for S in combinations(positive,k):yield frozenset((0,*S))
def factorisations(A):
    factors=list(subsets(A));answer=[]
    for i,B in enumerate(factors):
        for C in factors[i:]:
            if max(B)+max(C)==max(A) and {b+c for b in B for c in C}==A:
                answer.append((B,C))
    return answer
def row(H,l):
    answer=[0]*(l+2)
    for A in subsets(H):
        if not factorisations(A):answer[len(A)]+=1
    return answer
def main():
    controls=boundary=0
    for l in range(11):
        for bits in range(1<<l):
            H={0}|{j+1 for j in range(l) if bits>>j&1}
            if any(a+b<=l and a+b not in H for a in H for b in H):continue
            m=min(H-{0},default=l+1)
            if l>2*m:continue
            actual=row(H,l);h=len(H)-1
            expected=[0 if k<2 else comb(h,k-1) if k-1<=h else 0
                      for k in range(l+2)]
            if l==2*m:expected[3]-=1;boundary+=1
            assert actual==expected
            assert all(actual[k]**2>=actual[k-1]*actual[k+1]
                       for k in range(1,len(actual)-1))
            controls+=1
    assert not factorisations({0,1,3})
    assert factorisations({0,1,2,3})
    assert row(set(range(5)),4)==[0,0,4,4,2,0]
    distinct=Counter();pair_counts=Counter()
    for A in subsets(set(range(5))):
        fs=factorisations(A)
        if fs:distinct[len(A)]+=1;pair_counts[len(A)]+=len(fs)
    assert distinct==Counter({3:2,4:2,5:1})
    assert pair_counts==Counter({3:2,4:3,5:5})
    assert row({0,2},3)==row({0,3},3)
    assert row({0,2,4},4)==[0,0,2,0,0,0]
    assert row({0,3,4},4)==[0,0,2,1,0,0]
    receipt={'status':'PASS','maximum_formula_controls':controls,
       'boundary_controls':boundary,'distinct_decomposable_rank_counts':dict(distinct),
       'unordered_factor_pair_rank_counts':dict(pair_counts),
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Per-target-set factor search through cutoff10; no large cutoff18 replay or all-cutoff claim.'}
    (HERE/'POWER-MONOID-REVIEW-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

