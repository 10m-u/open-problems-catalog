#!/usr/bin/env python3
"""Exact truncated numerical-monoid and power-set atom exploration for Q2212."""
from pathlib import Path
from hashlib import sha256
from math import comb
import json

HERE=Path(__file__).resolve().parent
def support(bits):return [i for i in range(bits.bit_length()) if bits>>i&1]
def sumset(a,b):
    out=0
    while b:
        bit=b&-b;out|=a<<(bit.bit_length()-1);b-=bit
    return out
def main():
    l=18;limit=(1<<(l+1))-1;decomposable=set()
    factor_pairs=0
    for bmax in range(1,l):
        for cmax in range(bmax,l-bmax+1):
            for lowb in range(1<<(bmax-1)):
                b=1|(1<<bmax)|(lowb<<1)
                for lowc in range(1<<(cmax-1)):
                    c=1|(1<<cmax)|(lowc<<1)
                    if bmax==cmax and b>c:continue
                    decomposable.add(sumset(b,c));factor_pairs+=1
    monoids=0;atom_subsets=0;bad=None;lc_bad=None
    for positive in range(1<<l):
        H=1|(positive<<1);ok=True
        for j in support(positive):
            if ((H<<(j+1))&limit)&~H:ok=False;break
        if not ok:continue
        # Extend by all integers >l. This is an actual cofinite additive monoid.
        row=[0]*(l+2);sub=positive
        while sub:
            A=1|(sub<<1)
            if A not in decomposable:row[A.bit_count()]+=1
            sub=(sub-1)&positive
        atom_subsets+=sum(row);monoids+=1
        falling=False
        for x,y in zip(row,row[1:]):
            if y<x:falling=True
            if falling and y>x:
                bad={'H_through_l':support(H),'row':row};break
        if bad:break
        if lc_bad is None:
            for k in range(1,len(row)-1):
                if row[k]**2<row[k-1]*row[k+1]:
                    lc_bad={'H_through_l':support(H),'row':row,'failed_index':k};break
    receipt={'status':'EXACT_COUNTEREXAMPLE' if bad else 'BOUNDED_COMPLETE_NO_UNIMODALITY_COUNTEREXAMPLE',
      'l':l,'actual_truncated_monoids':monoids,'nonunit_factor_pairs':factor_pairs,
      'distinct_decomposable_sets':len(decomposable),'atom_sets_across_monoids':atom_subsets,
      'unimodality_counterexample':bad,'stronger_log_concavity_obstruction':lc_bad,
      'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'Every truncated additive-closed subset through l=18; extension by all larger integers is a numerical monoid. No all-l conclusion.'}
    (HERE/'EXPLORATION.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
