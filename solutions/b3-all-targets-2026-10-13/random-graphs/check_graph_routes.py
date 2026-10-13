#!/usr/bin/env python3
"""Exact Bonferroni inequalities and stronger-certificate obstructions."""
from fractions import Fraction as F
from itertools import combinations
from math import comb,log,floor
from pathlib import Path
from hashlib import sha256
import json
from graph_probe import graph,independent_row,violations,tree_344
HERE=Path(__file__).resolve().parent

def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):out[i+j]+=u*v
    return out

def power(a,k):
    out=[1]
    for _ in range(k):out=conv(out,a)
    return out

def main():
    sample=json.loads((HERE/'GRAPH-PROBE.json').read_text())
    for rec in sample['records']:
        a,_=independent_row(graph(rec['n'],rec['edges']))
        assert a==rec['row'] and violations(a)==rec['LC_failures']
    n=5;possible=list(combinations(range(n),2));criteria=0
    for mask in range(1<<len(possible)):
        edges=[e for j,e in enumerate(possible) if mask>>j&1];adj=graph(n,edges)
        actual=[0]*(n+1)
        for vertices in range(1<<n):
            if all(not(vertices>>i&1 and vertices>>j&1) for i,j in edges):actual[vertices.bit_count()]+=1
        a,_=independent_row(adj);assert a+[0]*(n+1-len(a))==actual
        m=len(edges);W=sum(comb(v.bit_count(),2) for v in adj)
        def mu(l):return F(m*comb(l,2),comb(n,2))
        def nu(l):return F(W*comb(l,3),comb(n,3))+F((comb(m,2)-W)*comb(l,4),comb(n,4))
        for l in range(n+1):assert 1-mu(l)<=F(actual[l],comb(n,l))<=1-mu(l)+nu(l)
        for k in range(1,n):
            alpha=F(m,n*(n-1));L=1-mu(k)
            assert L**2-(1-mu(k-1))*(1-mu(k+1))==2*alpha*L+4*alpha**2*k*(k-1)
            if mu(k+1)<=F(1,2) and nu(k+1)<=F(1,12*(k+1)):
                assert actual[k]**2>=actual[k-1]*actual[k+1];criteria+=1
    claw=graph(4,[(0,1),(0,2),(0,3)]);a,_=independent_row(claw)
    assert a==[1,4,3,1] and violations(a)==[]
    disc=3**2*4**2-4*4**3-4*3**3-27+18*3*4
    assert disc==-31
    weighted=[1,13,3,1];assert violations(weighted)==[2]
    # Support exchange: center singleton versus two leaves, slack exponent n-size.
    u=(3,1,0,0,0);v=(2,0,1,1,0)
    legal={(4-mask.bit_count(),)+tuple(mask>>j&1 for j in range(4))
           for mask in range(16) if all(not(mask>>i&1 and mask>>j&1) for i,j in [(0,1),(0,2),(0,3)])}
    assert u in legal and v in legal
    for j in (2,3):
        uu=list(u);vv=list(v);uu[1]-=1;uu[j]+=1;vv[1]+=1;vv[j]-=1
        assert tuple(uu) in legal and tuple(vv) not in legal
    T,edges=tree_344();row,_=independent_row(T);formula=[1]
    for k in (3,4,4):
        b=[comb(k,j)*2**j for j in range(k+1)]+[0]
        for j in range(k+1):b[j+1]+=comb(k,j)
        formula=conv(formula,b)
    add=[0]+[comb(11,j)*2**j for j in range(12)]
    for j,v in enumerate(add):formula[j]+=v
    assert formula==row and row[-3:]==[2979,51,1] and violations(row)==[13]
    # The isolated-tree second moment counts are checked exactly in small cases.
    tree_prob=[]
    for h,aut in ((4,6),(26,6912)):
        for n,d in ((100,2),(100,8),(1000,16)):
            p=F(d,n);q=1-p;fall=1
            for j in range(h):fall*=n-j
            B=h*(n-h)+comb(h,2)-(h-1)
            EX=F(fall,aut)*p**(h-1)*q**B
            assert EX>0 and B>=0
            # Cross absent edges counted twice give exactly q^(-h*h).
            assert (p**(2*(h-1))*q**(2*B-h*h))/(p**(h-1)*q**B)**2==q**(-h*h)
            tree_prob.append({'h':h,'n':n,'d':d,'positive_expectation':True})
    receipt={'status':'PASS','actual_random_samples_replayed':len(sample['records']),
        'all_five_vertex_graphs_literal_checked':1024,'deterministic_criterion_indices_checked':criteria,
        'claw_row':a,'claw_discriminant':disc,'weighted_claw_failure':[1,13,3,1],
        'actual_M_convex_exchange_failure':True,'known_tree_top_coefficients':[2979,51,1],
        'known_tree_defect':51**2-2979,'known_tree_formula_independently_matches_deletion':True,
        'isolated_tree_joint_absent_edge_counts':tree_prob,
        'scope':'Exact finite witnesses and algebraic controls; all-size prefix/probability proofs live in the accompanying documents.',
        'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'GRAPH-ROUTES-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
