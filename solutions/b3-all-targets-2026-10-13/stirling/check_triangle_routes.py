#!/usr/bin/env python3
"""Bounded exact controls for five distinct triangle proof routes."""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
from check_hankel_tn2 import rows


def det(m):
    n = len(m)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               * product(m[i][p[i]] for i in range(n)) for p in permutations(range(n)))


def product(xs):
    v = 1
    for x in xs: v *= x
    return v


def minors(m, order):
    for I in combinations(range(len(m)),order):
        for J in combinations(range(len(m[0])),order):
            yield I,J,det([[m[i][j] for j in J] for i in I])


def run():
    c = dict(lift_witnesses=0, original_staircase_minors=0, atom_toeplitz_witnesses=0,
             hadamard_input_minors=0, recurrence_extensions=0,
             tn_prefix_minors=0, symbolic_three_minor_substitutions=0,
             rank_three_perturbation_minors=0)
    # Complete small staircase control including isolated zeroth column.
    r = 2
    D = [[int(N==0) if k==0 else F(1,2**(N*N))*int(N>=r*k)
          for k in range(4)] for N in range(7)]
    for z in range(1,5):
        for _,_,d in minors(D,z):
            assert d>=0
            c['original_staircase_minors'] += 1
    U = [[2,3,4],[3,5,7],[4,7,10]]
    V = [[2,6,7],[3,11,13],[5,21,25]]
    for z in range(1,4):
        for m in [U,V]:
            for _,_,d in minors(m,z):
                assert d>=0
                c['hadamard_input_minors'] += 1
    assert det([[u*v for u,v in zip(a,b)] for a,b in zip(U,V)]) == -4
    prefix = [[1,0,0,0],[0,1,0,0],[0,1,1,0],[0,1,1,1]]
    for z in range(1,5):
        for _,_,d in minors(prefix,z):
            assert d>=0
            c['tn_prefix_minors'] += 1
    samples = list(range(2,18))+[32,64,100]
    for r in samples:
        p = r-1
        x = F(1,2**((r+1)**2+(2*r+1)**2))-F(1,2**((r+2)**2+(2*r)**2))
        assert x<0
        c['lift_witnesses'] += 1
        gc = [F(1,r+j) for j in range(4)]
        gs = [F(1,factorial(r+j)) for j in range(4)]
        assert gc[1]**2-gc[0]*gc[2] == -F(1,r*(r+1)**2*(r+2))
        d = det([[gs[j-i] if j>=i else F(0) for j in [1,2,3]] for i in [0,1,2]])
        assert d == F(1-r,factorial(r)**3*(r+1)**3*(r+2)*(r+3)) <0
        c['atom_toeplitz_witnesses'] += 2
        B = F(factorial(2*r),2*factorial(r)**2)
        T = F(factorial(3*r),6*factorial(r)**3)
        for fam in ['C','S']:
            u = comb(2*r+1,p)*(factorial(p) if fam=='C' else 1)
            v1,v2 = (r+2,2*r+1) if fam=='C' else (1,2)
            v3 = 3*r if fam=='C' else 3
            u3 = comb(3*r,p)*(factorial(p) if fam=='C' else 1)
            extended = [[1,1,0],[1,1,1],[v1,u+v2,u3+v3]]
            assert det(extended) == (-p-u if fam=='C' else -1-u) <0
            c['recurrence_extensions'] += 1
            a = rows(r,4,fam)
            got = det([[a[n][k] if k<=n else 0 for k in [1,2,3]] for n in [2,3,4]])
            if fam=='C':
                poly = 4*r**4+5*r**3-8*r*r-r+2
                t = r-2
                assert poly == 4*t**4+37*t**3+118*t*t+155*t+72
                want = factorial(p)**6*B*T*F(2*r*(2*r+1)*poly,(r+1)**2*(r+2))
            else:
                want = B*T*F(2*r*(8*r*r+21*r+7),(r+1)**2*(r+2))
            assert got == want >0
            c['symbolic_three_minor_substitutions'] += 1
    M = [[F(1+i*j+i*i*j*j) for j in range(1,5)] for i in range(1,5)]
    assert det(M)==0
    M[0][0] -= F(1,1000)
    for z in range(1,4):
        for _,_,d in minors(M,z):
            assert d>0
            c['rank_three_perturbation_minors'] += 1
    assert det(M)<0
    receipt=dict(date='2026-10-13',schema='b3-triangle-routes-v1',passed=True,
                 counts=c,perturbed_order_four_determinant=str(det(M)),
                 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 scope='Route obstructions and all-r formula transcription controls; no catalog counterexample.')
    Path(__file__).with_name('TRIANGLE-CHECK-RESULTS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))


if __name__=='__main__':run()
