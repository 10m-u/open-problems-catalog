#!/usr/bin/env python3
"""Exact controls for the all-size non-LC increasing-tree counterexample."""
from itertools import combinations
from fractions import Fraction as R
from pathlib import Path
import hashlib
import json

W=(1,2,3,5)


def mul(a,b,limit=None):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if limit is None or i+j<=limit:
                c[i+j]+=x*y
    return c if limit is None else c[:limit+1]


def p(j,k):
    t=j-k+1
    return W[t] if 0<=t<len(W) else 0


def q(j,k):
    return sum(p(j,i)*p(i,k) for i in range(1,j+2))


def all_minor_controls(a):
    count=0
    for i,j in combinations(range(len(a)),2):
        for k,l in combinations(range(len(a[0])),2):
            assert a[i][k]*a[j][l]-a[i][l]*a[j][k]>=0,(i,j,k,l)
            count+=1
    return count


def run():
    counts=dict(square_production_entries=0, square_TN2_minors=0,
                independent_Lagrange_forest_entries=0, forest_TN2_minors=0,
                ratio_controls=0, composition_criterion_controls=0)
    c=mul(W,W)
    assert c==[1,4,10,22,29,30,25]
    assert [c[i]**2-c[i-1]*c[i+1] for i in range(1,6)]==[6,12,194,181,175]
    first=[q(j,1) for j in range(1,9)]
    assert first==[7,17,29,30,25,0,0,0]
    adj=[q(j,1)*q(j+1,2)-q(j,2)*q(j+1,1) for j in range(1,9)]
    assert adj==[2,84,181,175,625,0,0,0]
    for j in range(1,19):
        for k in range(1,19):
            ix=j-k+2
            expected=c[ix] if 0<=ix<len(c) else 0
            if k==1 and j+1<len(W):
                expected-=W[j+1]
            assert q(j,k)==expected
            counts['square_production_entries']+=1
    Q=[[q(j,k) for k in range(1,19)] for j in range(1,19)]
    counts['square_TN2_minors']=all_minor_controls(Q)

    N=44
    forest=[[0]*(N+1) for _ in range(N+1)]
    forest[0][0]=1
    b=[0]*(N+1)
    for n in range(1,N+1):
        b[n]=sum(W[k]*forest[n-1][k] for k in range(4))
        forest[n][1]=b[n]
        for k in range(2,n+1):
            forest[n][k]=sum(b[j]*forest[n-j][k-1] for j in range(1,n))
    assert b[1:9]==[1,2,7,31,146,727,3774,20169]
    assert [forest[n][1:n+1] for n in range(1,5)]==[
        [1],[2,1],[7,4,1],[31,18,6,1]]
    # Independently, Lagrange inversion: [z^n]B^k=k/n*[u^(n-k)]phi^n.
    phi_power=[1]
    for n in range(1,26):
        phi_power=mul(phi_power,W,25)
        for k in range(1,n+1):
            assert R(k*phi_power[n-k],n)==forest[n][k]
            counts['independent_Lagrange_forest_entries']+=1
    for n in range(1,24):
        for k in range(1,26):
            assert sum(forest[n][j]*p(j,k) for j in range(1,n+1))==forest[n+1][k]
            assert sum(forest[n][j]*q(j,k) for j in range(1,n+1))==forest[n+2][k]
    rows=[forest[n][1:21] for n in range(1,21)]
    counts['forest_TN2_minors']=all_minor_controls(rows)
    assert all(2*forest[n][2]>=forest[n][1] for n in range(2,N+1))
    h=[3,5,0,0,0]
    v=[7,17,29,30,25]
    assert [h[i]*v[j]-h[j]*v[i] for i,j in combinations(range(5),2)][0]==16
    assert all(h[i]*v[j]>=h[j]*v[i] for i,j in combinations(range(5),2))

    z=[2]+[3*b[n]+5*forest[n][2] for n in range(1,N+1)]
    s=[3]+[5*b[n] for n in range(1,N+1)]
    root=[b[n+1] for n in range(N)]
    assert z[:3]==[2,3,11] and b[1:4]==[1,2,7]
    assert R(z[2],z[1])>R(b[3],b[2])
    ratios=[None]+[R(b[n+1],b[n]) for n in range(1,N)]
    for n in range(1,41):
        assert ratios[n]<=ratios[n+1]
        assert ratios[n]<=R(z[n+1],z[n])<=ratios[n+2]
        counts['ratio_controls']+=3
        for m in range(1,n+1):
            rem=n-m
            assert R(s[rem+1],s[rem])<=R(z[n+1],z[n])
            assert ratios[m]<=R(z[n+1],z[n])
            assert R(z[rem+1],z[rem])<=R(root[n+1],root[n])
            assert ratios[m]<=R(root[n+1],root[n])
            counts['composition_criterion_controls']+=4
    assert W[2]**2<W[1]*W[3]
    proof=Path(__file__).with_name('Q4666-RESULT.md')
    receipt=dict(schema='b3-q4666-two-step-tree-controls-v1',date='2026-10-13',
                 passed=True,offspring_numerators=list(W),offspring_denominator=11,
                 counts=counts,Cor2_9_failure={'shift':1,'n':1,'ratio':'11/3','upper':'7/2'},
                 scope='Finite exact controls support the written all-size two-step proof; not an enumeration-based all-size inference.',
                 checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest())
    Path(__file__).with_name('Q4666-CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt))


if __name__=='__main__':
    run()

