#!/usr/bin/env python3
"""Independent finite-set controls for the Q2212 maximum theorem and routes."""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
def subsets(positive):
    positive=sorted(positive)
    for k in range(1,len(positive)+1):
        for c in combinations(positive,k):yield frozenset((0,*c))
def decompositions(l):
    sets=list(subsets(range(1,l+1)));out=defaultdict(list)
    for i,B in enumerate(sets):
        for C in sets[i:]:
            if max(B)+max(C)<=l:
                out[frozenset(b+c for b in B for c in C)].append((B,C))
    return out
def row(positive,l,dec):
    out=[0]*(l+2)
    for A in subsets(set(positive)&set(range(1,l+1))):
        if A not in dec:out[len(A)]+=1
    return out
def main():
    controls=0;boundary=0
    for l in range(13):
        dec=decompositions(l)
        for bits in range(1<<l):
            positive={i+1 for i in range(l) if bits>>i&1}
            H={0}|positive
            if any(a+b<=l and a+b not in H for a in H for b in H):continue
            m=min(positive) if positive else l+1
            if l>2*m:continue
            actual=row(positive,l,dec);h=len(positive)
            expected=[0,0]+[comb(h,k-1) if k-1<=h else 0 for k in range(2,l+2)]
            if l==0:expected=[0,0]
            if l==2*m:
                expected[3]-=1;boundary+=1
            assert actual==expected,(l,positive,actual,expected)
            assert all(actual[k]**2>=actual[k-1]*actual[k+1] for k in range(1,len(actual)-1))
            controls+=1
    d3=decompositions(3);d4=decompositions(4)
    assert frozenset((0,1,3)) not in d3
    assert frozenset((0,1,2,3)) in d3
    assert row(range(1,5),4,d4)==[0,0,4,4,2,0]
    distinct=Counter(len(A) for A in d4)
    pairs=Counter()
    for A,fac in d4.items():pairs[len(A)]+=len(fac)
    assert dict(distinct)=={3:2,4:2,5:1}
    assert dict(pairs)=={3:2,4:3,5:5}
    assert len(d4[frozenset(range(5))])==5
    assert row({2,4},3,d3)==row({3,4},3,d3)==[0,0,1,0,0]
    assert row({2,4},4,d4)==[0,0,2,0,0,0]
    assert row({3,4},4,d4)==[0,0,2,1,0,0]
    for h in range(3,101):
        assert (comb(h,2)-1)**2-h*comb(h,3)==h*(h-1)*(h*(h+1)-12)//12+1>=1
    receipt={'status':'PASS','multiplicity_formula_controls':controls,
      'boundary_controls':boundary,'all_boundary_defect_identity_controls':98,
      'N_cutoff4_row':[0,0,4,4,2,0],'nonzero_factor_discriminant':-4,
      'distinct_decomposable_rank_counts':dict(distinct),'factor_pair_rank_counts':dict(pairs),
      'rank_state_transition_rows':[[0,0,2,0,0],[0,0,2,1,0]],
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Finite controls through12 and exact in-class route obstructions; all-size l<=2m proof is separate.'}
    (HERE/'ROUTE-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
