#!/usr/bin/env python3
"""Exact controls for the low-degree coefficient-order classifications."""
import json
from pathlib import Path
from hashlib import sha256
from itertools import combinations_with_replacement,product
from fractions import Fraction as F
from math import comb,floor,ceil

HERE=Path(__file__).resolve().parent
def coefficients(r):
    c=[F(1)]
    for a in r:
        c.append(F(0))
        for i in range(len(c)-1,0,-1):c[i]+=a*c[i-1]
    return c
def compatible(c,pi):return all(c[i]<=c[j] for i,j in zip(pi,pi[1:]))
def main():
    d=json.loads((HERE/'BOUNDED-ORDERS.json').read_text())
    witnesses=0
    for n,rows in d['witnesses'].items():
        for row in rows:
            c=coefficients(row['r']);assert c==row['coefficients']
            assert compatible(c,row['permutation']);witnesses+=1
    expected={'012345','012354','012534','015234','015243','051243','051423',
              '051432','054123','054132','501423','501432','504123','504132'}
    assert {''.join(map(str,w['permutation'])) for w in d['witnesses']['5']}==expected
    for j in range(5):assert F(comb(j,2),4)+F(comb(j,3),8)-1-F(j,2)<0
    controls=0
    for r in combinations_with_replacement(range(1,25),5):
        c=coefficients(r)
        if c[4]<=c[2]:assert c[5]<c[1]
        if c[4]>=c[3]:assert c[5]>c[1]
        if c[3]>=c[4]:assert c[5]<c[2]
        controls+=1
    # A prefix permutation does not determine the next permutation.
    assert compatible(coefficients((1,2)),(0,2,1))
    assert compatible(coefficients((1,4)),(0,2,1))
    assert not compatible(coefficients((1,2,2)),(0,1,3,2))
    assert compatible(coefficients((1,4,2)),(0,1,3,2))
    # No coordinate floor/ceiling rounding preserves this real-root chamber.
    r=(F(1),F(1),F(5,3),F(5));pi=(0,4,1,2,3)
    assert compatible(coefficients(r),pi)
    neighbors=list(product(*[{floor(v),ceil(v)} for v in r]))
    assert len(neighbors)==2
    assert all(not compatible(coefficients(v),pi) for v in neighbors)
    left,right=(1,1,12,14),(1,2,4,21)
    a,b=coefficients(left),coefficients(right)
    assert (a[1],a[4])==(b[1],b[4])==(28,168)
    assert a[2]>a[4] and b[2]<b[4]
    assert compatible(a,(0,1,4,2,3)) and compatible(b,(0,1,2,4,3))
    receipt={'status':'PASS','degree_five_lemma_controls':controls,
      'exact_catalog_witnesses':witnesses,'rounding_neighbors':len(neighbors),
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Exact controls; all-integer exhaustion is the analytic proof in DEGREE-FIVE.md.'}
    (HERE/'ORDER-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
