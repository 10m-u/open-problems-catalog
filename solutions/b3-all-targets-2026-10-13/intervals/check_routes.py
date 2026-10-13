#!/usr/bin/env python3
"""Exact route obstructions and bounded path/cycle domination controls."""
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import sympy as S

HERE=Path(__file__).resolve().parent

def domination(n,ell,cycle=False):
    neighborhoods=[]
    for v in range(n):
        neighborhoods.append(sum(1<<u for u in range(n)
            if (min(abs(u-v),n-abs(u-v)) if cycle else abs(u-v))<=ell))
    c=[0]*(n+1)
    for mask in range(1<<n):
        if all(mask&a for a in neighborhoods):c[mask.bit_count()]+=1
    return c

def ulc(c,n):
    return all(k*(n-k)*c[k]**2 >= (k+1)*(n-k+1)*c[k-1]*c[k+1]
               for k in range(1,n))

def prefix(word):
    h=[0]
    for b in word:h.append(h[-1]+b)
    return h

def rounded_mean(x,y):
    a,b=prefix(x),prefix(y)
    lo=[(u+v)//2 for u,v in zip(a,b)]
    hi=[(u+v+1)//2 for u,v in zip(a,b)]
    return tuple(lo[i+1]-lo[i] for i in range(len(x))),tuple(hi[i+1]-hi[i] for i in range(len(x)))

def main():
    t=S.symbols('t')
    c=domination(5,1)
    assert c==[0,0,3,8,5,1]
    assert S.discriminant(t**3+5*t*t+8*t+3,t)==-31
    assert ulc(c,5)
    circuits=[{0,1},{1,2,3},{3,4}]
    union=(circuits[0]|circuits[1])-{1}
    assert not any(C<=union for C in circuits)
    band=[comb(6,k) if 2<=k<=4 else 0 for k in range(7)]
    assert S.discriminant(15+20*t+15*t*t,t)==-500
    assert ulc(band,6)
    words=[w for w in product([0,1],repeat=6)
           if w[0]+w[1]==w[1]+w[2]==w[3]+w[4]==w[4]+w[5]==1]
    assert len(words)==4
    bases=[{i for i,b in enumerate(w) if b} for w in words if sum(w)==3]
    assert len(bases)==2
    exchange_failures=[]
    for A,B in product(bases,repeat=2):
        for a in A-B:
            if not any((A-{a})|{b} in bases for b in B-A):exchange_failures.append((sorted(A),sorted(B),a))
    assert exchange_failures
    antipodal_outputs={rounded_mean(w,tuple(1-b for b in w))
                       for w in product([0,1],repeat=6) if sum(w)==2}
    assert len(antipodal_outputs)==1
    assert next(iter(antipodal_outputs))==((0,1,0,1,0,1),(1,0,1,0,1,0))
    A={(0,0,1,1),(1,1,0,0),(1,0,0,0),(0,1,1,1)}
    B={(0,1,0,1),(1,0,1,0),(1,0,0,0),(0,1,1,1)}
    counts=lambda F:[sum(sum(w)==k for w in F) for k in range(5)]
    ca,cb,ci=counts(A),counts(B),counts(A&B)
    assert ca==cb==[0,1,2,1,0] and ci==[0,1,0,1,0]
    assert ulc(ca,4) and ulc(cb,4) and not ulc(ci,4)
    w=(0,1,0,0,1,1);rot=w[1:]+w[:1]
    constraint=lambda x:x[0]+x[1]==x[1]+x[2]==1
    assert constraint(w) and not constraint(rot)
    recurrence_output=[0,10,11,11,1]
    assert ulc([0,0,10,1],3) and ulc([0,10,1],2) and ulc([10,1],1)
    assert not ulc(recurrence_output,4)
    cut_output=[1,2,1,1]
    assert ulc([1,2,1],2) and ulc([0,0,1],2) and not ulc(cut_output,3)
    examples=0
    for n in range(1,15):
        for ell in range(1,min(4,n)+1):
            for cycle in [False,True]:
                assert ulc(domination(n,ell,cycle),n),(n,ell,cycle)
                examples+=1
    receipt={'status':'PASS','actual_path5_coefficients':c,
             'actual_path5_reduced_discriminant':-31,
             'symmetric_global_band_coefficients':band,
             'symmetric_band_quadratic_discriminant':-500,
             'matroid_circuit_elimination_witness':[sorted(v) for v in circuits],
             'symmetric_interval_basis_exchange_failures':exchange_failures,
             'antipodal_midpoint_rank2_preimages':15,'antipodal_midpoint_outputs':1,
             'generic_APP_intersection_counts':[ca,cb,ci],
             'generic_recurrence_output':recurrence_output,'generic_cut_output':cut_output,
             'actual_domination_ULC_examples':examples,'maximum_graph_size':14,
             'scope':'Proof-method obstructions and finite unweighted controls, not counterexamples to either full target.'}
    (HERE/'CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k not in ['symmetric_interval_basis_exchange_failures']}))

if __name__=='__main__':main()
