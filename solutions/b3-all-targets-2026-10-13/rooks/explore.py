#!/usr/bin/env python3
"""Pinned actual-shape search and exact multivariate-model obstruction."""
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json
import random
from flint import ctx,fmpz_poly
import sympy as s

HERE=Path(__file__).resolve().parent

def placements(lam,mu):
    """Dual bases: occupied rows union unoccupied columns (source complements)."""
    r=len(lam);c=max(lam);answer=[]
    def rec(row,last,rows,cols):
        if row==r:
            answer.append(tuple(rows)+tuple(r+j for j in range(1,c+1) if j not in cols));return
        rec(row+1,last,rows,cols)
        for j in range(mu[row]+1,min(lam[row]+1,last)):
            rec(row+1,j,rows+[row+1],cols+[j])
    rec(0,c+1,[],[])
    assert len(answer)==len(set(answer))
    return answer

def coefficients(lam,mu):
    c=max(lam);dp={(c+1,0):1}
    for a,b in zip(lam,mu):
        out=dp.copy()
        for (last,k),v in dp.items():
            for j in range(b+1,min(a+1,last)):
                key=(j,k+1);out[key]=out.get(key,0)+v
        dp=out
    result=[0]*(min(len(lam),c)+1)
    for (last,k),v in dp.items():result[k]+=v
    while len(result)>1 and result[-1]==0:result.pop()
    return result

def contains332(lam,mu):
    c=max(lam)
    for i,j,k in combinations(range(len(lam)),3):
        # The absent NW corner and present middle-left corner force
        # col1 in (mu_j,mu_i]; absent SE and present middle-right force
        # col3 in (lam_k,lam_j]. The middle column is present in all rows.
        for a,b,d in combinations(range(1,c+1),3):
            rows=(i,j,k);cols=(a,b,d)
            bits=tuple(tuple(int(mu[row]<col<=lam[row]) for col in cols) for row in rows)
            if bits==((0,1,1),(1,1,1),(1,1,0)):
                return {'rows':[i+1,j+1,k+1],'columns':[a,b,d]}
    return None

def main():
    ctx.prec=128;rng=random.Random(183)
    lam=(6,6,6,3,3,3);mu=(0,)*6
    bases=placements(lam,mu);plain=coefficients(lam,mu)
    assert contains332(lam,mu) is None
    assert len(bases)==sum(plain)
    assignment=None
    for selected in combinations(range(1,13),6):
        subset=set(selected);vector=[0]*7
        for basis in bases:vector[len(subset.intersection(basis))]+=1
        if vector==[0,0,0,400,225,36,1] or vector==[1,36,225,400,0,0,0]:
            assignment={'t_elements':list(selected),'coefficients':vector};break
    assert assignment is not None
    x=s.Symbol('x');nonzero=assignment['coefficients'].copy()
    while nonzero[0]==0:nonzero.pop(0)
    witness=s.Poly(sum(v*x**i for i,v in enumerate(nonzero)),x)
    assert witness.count_roots(-s.oo,s.oo)<witness.degree()
    weighted={'lambda':list(lam),'mu':list(mu),'basis_count':len(bases),
       'ordinary_nn_coefficients':plain,'assignment':assignment,
       'reduced_discriminant':str(s.discriminant(witness.as_expr(),x)),
       'reduced_real_root_count':int(witness.count_roots(-s.oo,s.oo)),
       'reduced_degree':witness.degree(),
       'scope':'Weighted basis specialization fails; ordinary unweighted target is not refuted.'}
    checked=0;avoiding=0;bad=[]
    for _ in range(1600):
        r=rng.randrange(3,11);c=rng.randrange(3,13)
        lam=tuple(sorted([rng.randrange(1,c+1) for _ in range(r)],reverse=True))
        lower=sorted([rng.randrange(0,c) for _ in range(r)],reverse=True)
        mu=tuple(min(a-1,b) for a,b in zip(lam,lower))
        assert all(mu[i]>=mu[i+1] for i in range(r-1))
        checked+=1
        if contains332(lam,mu):continue
        avoiding+=1;coeff=coefficients(lam,mu)
        roots=fmpz_poly(coeff).complex_roots()
        if any(not root.imag.contains(0) for root,mult in roots):
            exact=s.Poly(sum(v*x**i for i,v in enumerate(coeff)),x)
            count=int(exact.count_roots(-s.oo,s.oo))
            if count<exact.degree():
                bad.append({'lambda':list(lam),'mu':list(mu),'coefficients':coeff,
                            'exact_real_root_count':count});break
    result={'status':'COUNTEREXAMPLE' if bad else 'NO_COUNTEREXAMPLE_FOUND',
       'seed':183,'sampled_shapes':checked,'avoiding_shapes_checked':avoiding,
       'counterexamples':bad,'weighted_obstruction':weighted,
       'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
       'scope':'Actual-shape bounded search; candidate exact controls do not prove the all-size assertion.'}
    (HERE/'EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
