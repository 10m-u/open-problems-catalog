"""Exact small controls and source examples, never global tuple exclusions."""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
from pathlib import Path
import json


def square(q):
    q = F(q)
    return q >= 0 and isqrt(q.numerator)**2 == q.numerator and isqrt(q.denominator)**2 == q.denominator


def main():
    sextuple = [F(34440), F(23001,280), F(840,68921), F(1121,11480), F(19383,1640), F(2530,287)]
    assert all(square(a*b+1) for a,b in combinations(sextuple,2))
    partitions = []
    for tail in combinations(range(1,6),2):
        left = (0,)+tail
        right = tuple(i for i in range(6) if i not in left)
        cross = [sextuple[i]*sextuple[j] for i in left for j in right]
        partitions.append({'left':left,'all_cross_products_integral':all(q.denominator==1 for q in cross)})
    assert not any(row['all_cross_products_integral'] for row in partitions)
    almost = [F(243,560),F(1147,5040),F(1100,63),F(7820,567),F(95,112),F(38269,6480),F(196,45)]
    missing = [[i,j,str(almost[i]*almost[j]+1)] for i,j in combinations(range(7),2) if not square(almost[i]*almost[j]+1)]
    assert [row[:2] for row in missing]==[[5,6]]
    # Original 2008 primary paper has denominator 30464; cached supplement
    # extraction drops its final digit and fails the other square conditions.
    strong = [F(140,51),F(2223,30464),F(278817,33856),F(3182740,17661)]
    strong_missing = [[i,j,str(strong[i]*strong[j]+1)] for i in range(4) for j in range(i,4) if not square(strong[i]*strong[j]+1)]
    assert [row[:2] for row in strong_missing]==[[2,3]]
    n=300
    masks=[0]*(n+1)
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a!=b and square(a*b+1):masks[a]|=1<<(b-1)
    tested=0
    for a,b,c in combinations(range(1,n+1),3):
        common=masks[a]&masks[b]&masks[c]
        common &= ~((1<<(a-1))|(1<<(b-1))|(1<<(c-1)))
        assert common.bit_count()<3
        tested+=1
    dmax=5000
    ext=[]
    for a in range(n+1):
        ext.append({d for d in range(1,dmax+1) if square(a*d+1)})
    checked=0
    for a,b,c in combinations(range(1,n+1),3):
        if all(square(x*y-1) for x,y in combinations([a,b,c],2)):
            for d in ext[a]&ext[b]&ext[c]:
                assert (d+a+b-c)**2==4*(a*b-1)*(c*d+1)
                checked+=1
    five=[4,8,17,89,4870844]
    assert all(square((x+1)*(55*x+1)*(276*x+1)) for x in five)
    out={'status':'passed','sextuple_cross_scaling_partitions':partitions,
         'almost_septuple_missing':missing,'almost_strong_missing':strong_missing,
         'K33_bound_all_six':n,'K33_left_triples':tested,
         'Dminus1_triple_max':n,'extension_max':dmax,'regularity_extensions_checked':checked,
         'elliptic_five_integer_x':five,
         'scope':'Bounded exact controls and source example verification; no full catalog solution'}
    Path(__file__).with_name('TUPLE-CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='sextuple_cross_scaling_partitions'}))


if __name__=='__main__':main()
