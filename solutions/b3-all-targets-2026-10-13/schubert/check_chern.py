#!/usr/bin/env python3
"""Exact Chern-plethysm controls; signed extraction is not a positive rule."""
from functools import cache
from fractions import Fraction
from math import factorial
from itertools import permutations
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent

def partitions(d, limit=None):
    if not d:
        yield ()
        return
    limit=d if limit is None else min(d,limit)
    for first in range(limit,0,-1):
        for rest in partitions(d-first,first):
            yield (first,)+rest

def contains(lam,nu):
    return len(lam)>=len(nu) and all(a>=b for a,b in zip(lam,nu))

@cache
def fskew(lam,nu):
    if not contains(lam,nu):return 0
    if lam==nu:return 1
    answer=0
    for i,a in enumerate(lam):
        below=lam[i+1] if i+1<len(lam) else 0
        protected=nu[i] if i<len(nu) else 0
        if a>below and a>protected:
            smaller=list(lam);smaller[i]-=1
            if not smaller[-1]:smaller.pop()
            answer+=fskew(tuple(smaller),nu)
    return answer

def signed_terms(lam,mu,n):
    terms=[]
    for d in range(sum(lam)+1):
        for nu in partitions(d):
            if not contains(lam,nu) or not contains(mu,nu):continue
            content=1
            for i,a in enumerate(lam):
                lower=nu[i] if i<len(nu) else 0
                for j in range(lower,a):
                    content*=n-i+j
            term=Fraction(fskew(lam,nu)*fskew(mu,nu)*content,
                          factorial(sum(lam)-d))
            if d%2:term=-term
            if term:terms.append((nu,term))
    return terms

def coefficient(lam,mu,n):
    total=sum((v for _,v in signed_terms(lam,mu,n)),Fraction())
    assert total.denominator==1
    return int(total)

def expansion(lam,n,stable=False):
    return {mu:coefficient(lam,mu,n) for mu in partitions(sum(lam))
            if stable or len(mu)<=n}

def monomials(lam,n):
    """Enumerate SSYT and independently decorate each box j!=i."""
    cells=[(i,j) for i,a in enumerate(lam) for j in range(a)]
    labels={}
    answer={}
    def decorate(k,weight):
        if k==len(cells):
            t=tuple(weight);answer[t]=answer.get(t,0)+1;return
        for color in range(n):
            if color==labels[cells[k]]:continue
            weight[color]+=1
            decorate(k+1,weight)
            weight[color]-=1
    def tableau(k):
        if k==len(cells):
            decorate(0,[0]*n);return
        i,j=cells[k]
        low=0
        if j:low=max(low,labels[(i,j-1)])
        if i:low=max(low,labels[(i-1,j)]+1)
        for value in range(low,n):
            labels[(i,j)]=value;tableau(k+1)
    tableau(0)
    return answer

def times_s1(coeffs):
    out={}
    for lam,coeff in coeffs.items():
        for i in range(len(lam)+1):
            v=list(lam)
            if i==len(lam):v.append(1)
            else:
                if i and v[i]==v[i-1]:continue
                v[i]+=1
            key=tuple(v)
            out[key]=out.get(key,0)+coeff
    return out

def frozen_row_fibre(row):
    polynomial={(0,0,0):1}
    for missing in row:
        nxt={}
        for color in range(1,4):
            if color==missing:continue
            for exponents,coeff in polynomial.items():
                key=list(exponents);key[color-1]+=1;key=tuple(key)
                nxt[key]=nxt.get(key,0)+coeff
        polynomial=nxt
    total=0
    for perm in permutations((2,1,0)):
        inversions=sum(perm[i]<perm[j] for i in range(3) for j in range(i+1,3))
        exponents=tuple(a-b for a,b in zip((3,2,0),perm))
        total+=(-1)**inversions*polynomial.get(exponents,0)
    return total

def main():
    controls=0
    for d in range(7):
        for lam in partitions(d):
            if len(lam)>2:continue
            for mu in partitions(d):
                if len(mu)<=2:
                    assert coefficient(lam,mu,2)==int(lam==mu)
                    controls+=1
    # A1 canonical lifted vector-crystal witness.
    n=3
    missing=[2,2];colors=[1,1]
    copies=[[i for i in range(1,n+1) if i!=j].index(i)+1
            for i,j in zip(missing,colors)]
    assert copies==[1,1]
    changed=[1,2]
    lifted=[[i for i in range(1,n+1) if i!=j][a-1]
            for j,a in zip(changed,copies)]
    assert lifted==[2,1]
    h2=expansion((2,),3)
    assert h2=={(2,):3,(1,1):2}
    direct=monomials((2,),3)
    assert direct[(2,0,0)]==3 and direct[(1,1,0)]==5 and sum(direct.values())==24
    # A2: exact separating functional for every degree-three generator product.
    basis=((3,),(2,1),(1,1,1))
    h3=expansion((3,),3)
    e3=expansion((1,1,1),3)
    h2h1={k:2*v for k,v in times_s1(h2).items()}
    e2h1={k:2*v for k,v in times_s1(expansion((1,1),3)).items()}
    h1cubed={k:8*v for k,v in times_s1(times_s1({(1,):1})).items()}
    vectors=[[d.get(k,0) for k in basis] for d in (h3,e3,h2h1,e2h1,h1cubed)]
    assert vectors==[[4,5,0],[0,1,0],[6,10,4],[2,6,4],[8,16,8]]
    assert all(v[1]-v[0]-v[2]>=0 for v in vectors)
    target=[coefficient((2,1),mu,3) for mu in basis]
    assert target==[2,5,4] and target[1]-target[0]-target[2]==-1
    # A3 stable character has a negative coefficient outside finite n.
    stable=expansion((3,),2,stable=True)
    assert stable=={(3,):1,(2,1):0,(1,1,1):-2}
    # A4 exact Young-lattice kernel and positive actual perturbation.
    shapes=list(partitions(6));previous=list(partitions(5))
    kernel=[0,0,-1,1,2,-1,0,1,0,0,0]
    assert all(sum(v for lam,v in zip(shapes,kernel) if contains(lam,nu))==0
               for nu in previous)
    assert kernel[0]==kernel[-1]==0
    column=[coefficient(lam,(3,2,1),6) for lam in shapes]
    assert column==[2310,5400,5949,4491,2597,4879,1565,975,1071,204,6]
    assert min(a+b for a,b in zip(column,kernel))>0
    fibres=[frozen_row_fibre(row) for row in ((1,1),(1,2),(1,3),(2,2),(2,3),(3,3))]
    assert fibres==[0,1,1,-1,0,1]
    assert sum(fibres)==coefficient((2,),(1,1),3)==2
    pieri_checks=0
    for lam in previous:
        for mu in shapes:
            lhs=sum(coefficient(rho,mu,6) for rho in shapes if contains(rho,lam))
            rhs=5*sum(coefficient(lam,nu,6) for nu in previous if contains(mu,nu))
            assert lhs==rhs
            pieri_checks+=1

    receipt={"status":"PASS","n2_identity_coefficient_controls":controls,
             "crystal_witness":{"missing_indices":missing,"colors":colors,
              "copies":copies,"new_colors":changed,"new_missing_indices":lifted},
             "actual_n3_row2_schur_coefficients":{str(k):v for k,v in h2.items()},
             "independent_decorated_tableaux_dimension":sum(direct.values()),
             "degree_three_generator_vectors":vectors,
             "degree_three_actual_target_vector":target,
             "stable_n2_row3_character":{str(k):v for k,v in stable.items()},
             "pieri_input_column_kernel":kernel,
             "actual_degree_six_column":column,
             "exact_forward_pieri_controls":pieri_checks,
             "frozen_tableau_signed_fibres":fibres,
             "scope":"Exact signed extraction and decorated monomial controls; not a general cancellation-free coefficient rule."}
    (HERE/"CHERN-CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))

if __name__=="__main__":main()

