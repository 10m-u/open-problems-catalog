#!/usr/bin/env python3
"""Literal proved KLG Pieri counts; exact coefficient reconstruction."""
from itertools import combinations,product
from pathlib import Path
from hashlib import sha256
import json,runpy

HERE=Path(__file__).resolve().parent
g=runpy.run_path(str(HERE/'check_q_genomic.py'))
def cells(shape):return {(r,c) for r,l in enumerate(shape,1) for c in range(r,r+l)}
def contains(outer,inner):return cells(inner)<=cells(outer)
def parts(n):
    return [tuple(sorted(s,reverse=True)) for k in range(n+1)
            for s in combinations(range(1,n+1),k)]
def klg_count(outer,inner,p):
    shape=sorted(cells(outer)-cells(inner))
    if not contains(outer,inner):return 0
    if any(r<i and c<j for r,c in shape for i,j in shape):return 0
    if not shape:return int(p==0)
    if p<=0 or len(shape)<p:return 0
    total=0
    for values in product(range(1,2*p+1),repeat=len(shape)):
        if {(a+1)//2 for a in values}!=set(range(1,p+1)):continue
        T=dict(zip(shape,values));valid=True
        for (r,c),a in T.items():
            if r==c and a%2:valid=False;break
            for (i,j),b in T.items():
                if (r,c)==(i,j):continue
                if ((r==i and c<j) or (c==j and r<i)) and a>=b:
                    valid=False;break
                if i>=r and j<=c:
                    if (a%2 and a>b) or (a%2==0 and a<b):
                        valid=False;break
            if not valid:break
        total+=valid
    return total
def pieri(inner,p,outer):
    c=klg_count(outer,inner,p)
    return c*(-1)**(sum(outer)-sum(inner)-p)
def leading_q31():
    # Four boxes, content 31, four genes: every gene is singleton.
    accepted=[]
    for letters in product(range(1,5),repeat=4):
        T=dict(zip(g['POSITIONS'],letters))
        if not g['q_tableau'](T):continue
        if sum((a+1)//2==1 for a in letters)!=3:continue
        if not g['every_genotype'](T,[[p] for p in T]):continue
        accepted.append(list(letters))
    assert len(accepted)==4,accepted
    return accepted
def main():
    n=2;P=parts(n)
    # Recover every rank-two product with a special input via proved Pieri.
    rank2={}
    for inner in P:
        for p in (1,2):
            rank2[str((inner,p))]={str(outer):pieri(inner,p,outer)
               for outer in P if pieri(inner,p,outer)}
    assert pieri((1,),1,(2,))==2
    assert pieri((1,),1,(2,1))==-1
    assert pieri((2,),1,(2,1))==1
    assert all(pieri((2,),2,t)==0 for t in P)
    # In the codimension filtration:
    # O21 = O1 O2 - 2 O3 + O4 + 2 O31 modulo codimension >=5.
    expansion={nu:pieri((2,),1,nu) for nu in parts(4) if sum(nu)<=4}
    assert {k:v for k,v in expansion.items() if v} == {
        (3,):2,(2,1):1,(4,):-1,(3,1):-2}
    lam=(3,1);nu=(4,3,1)
    product_terms=[]
    for rho in parts(4):
        if not contains(nu,rho) or not contains(rho,lam):continue
        a=pieri(lam,1,rho);b=pieri(rho,2,nu)
        if a and b:product_terms.append({'rho':rho,'first':a,'second':b,'term':a*b})
    mixed=sum(t['term'] for t in product_terms)
    c3=pieri(lam,3,nu);c4=pieri(lam,4,nu)
    leading=len(leading_q31())
    answer=mixed-2*c3+c4+2*leading
    assert answer==-5,(mixed,c3,c4,leading,answer)
    receipt={'status':'PASS','rank_two_special_products':rank2,
       'O2_times_O1_through_codimension_four':{str(k):v for k,v in expansion.items() if v},
       'reconstruction_terms':product_terms,'O31_O1_O2_coefficient':mixed,
       'O31_O3_coefficient':c3,'O31_O4_coefficient':c4,
       'O31_O31_cohomological_coefficient':leading,
       'c31_21_to_431':answer,'signed_positive_value':-answer,
       'leading_q31_objects':leading_q31(),
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Literal proved KLG Pieri rule plus primary leading-degree Q rule; no full LR rule inferred.'}
    (HERE/'LG-PIERI-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()

