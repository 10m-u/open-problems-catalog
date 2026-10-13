#!/usr/bin/env python3
"""Exact finite controls for the continuation-III midpoint proofs.

Python standard library only. The all-dimension results use the manuscript's
proofs; no finite enumeration is presented as an all-dimension certificate.
"""
from __future__ import annotations
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def geometry(n: int):
    points = list(product(range(3), repeat=n))
    index = {x:i for i,x in enumerate(points)}
    add = [[index[tuple((a+b)%3 for a,b in zip(x,y))] for y in points] for x in points]
    neg = [index[tuple(-a%3 for a in x)] for x in points]
    mid = [[neg[add[i][j]] for j in range(len(points))] for i in range(len(points))]
    return points, index, add, neg, mid


def affine_flats(n: int):
    P,ix,add,neg,mid = geometry(n)
    linear = {frozenset({0})}
    pending = [frozenset({0})]
    for H in pending:
        for v in range(len(P)):
            if v in H:
                continue
            new = frozenset(H | {add[x][v] for x in H} | {add[x][neg[v]] for x in H})
            if new not in linear:
                linear.add(new)
                pending.append(new)
    cosets = {}
    for H in linear:
        fibres = {frozenset(add[x][v] for x in H) for v in range(len(P))}
        cosets[H] = sorted(fibres, key=lambda z:min(z))
    flats = {K for fibres in cosets.values() for K in fibres}
    return P,ix,add,neg,mid,cosets,flats


def admissible(labels, mid):
    colours = [[i for i,c in enumerate(labels) if c==a] for a in (0,1)]
    return all(labels[mid[x][y]] != 2 for C in colours for x in C for y in C)


def audit_partition(labels, geom):
    P,ix,add,neg,mid,cosets,flats = geom
    R={i for i,c in enumerate(labels) if c==2}
    if not R:
        return (0,0,0)
    size=max(len(F) for F in flats if F<=R)
    cases=occupied_cases=plane_projection_cases=0
    for H,fibres in cosets.items():
        if len(H)!=size or not any(F<=R for F in fibres):
            continue
        cases+=1
        q_of={x:q for q,F in enumerate(fibres) for x in F}
        reps=[min(F) for F in fibres]
        qm=[[q_of[mid[x][y]] for y in reps] for x in reps]
        S={q for q,F in enumerate(fibres) if F<=R}
        D={q for q,F in enumerate(fibres) if F&R}
        assert len(S) in (1,2,4)
        assert all(qm[x][y] not in S for x,y in combinations(S,2))
        isolated=[]
        for q,F in enumerate(fibres):
            if q in S:
                continue
            neighbours=[t for t in range(len(fibres)) if t not in S and qm[q][t] in S]
            if not neighbours:
                isolated.append(q)
                reflected={q_of[mid[reps[q]][reps[s]]] for s in S}
                # In characteristic three midpoint(q,s)=2q-s.
                assert reflected==S
            C=F-R
            if neighbours:
                assert len({labels[x] for x in C})==1
                assert all(mid[x][y] in C for x in C for y in C)
        assert len(isolated)<=1
        assert len(isolated)==(0 if len(S)==1 else 1)
        qlabels=[]
        for q,F in enumerate(fibres):
            qlabels.append(2 if q in D else labels[min(F)])
        assert admissible(qlabels,qm)
        occupied_cases+=1
        if size==3 and not any(len(F)==9 and F<=R for F in flats):
            # Pullbacks of quotient planes are affine 3-flats containing H.
            for W in flats:
                if len(W)!=27:
                    continue
                qset={q_of[x] for x in W}
                if len(qset)==9 and all(fibres[q]<=W for q in qset):
                    if qset<=D:
                        assert len(R&W)>=17
                        raise AssertionError('Plane-free remainder has an occupied quotient plane.')
            assert len(R)<=2*len(D)+len(S)
            plane_projection_cases+=1
    return cases,occupied_cases,plane_projection_cases


def main():
    g2=affine_flats(2)
    totals=[0,0,0]
    valid=0
    sampled=[]
    for serial,lab in enumerate(product(range(3),repeat=9)):
        if not admissible(lab,g2[4]):
            continue
        valid+=1
        counts=audit_partition(lab,g2)
        totals=[a+b for a,b in zip(totals,counts)]
        if serial%37==0:
            sampled.append(lab)
    g3=affine_flats(3)
    for lab in sampled:
        lifted=[lab[g2[1][x[:2]]] for x in g3[0]]
        assert admissible(lifted,g3[4])
        counts=audit_partition(lifted,g3)
        totals=[a+b for a,b in zip(totals,counts)]
    # Sharp 16-point construction: first block has one coordinate,
    # second block has two coordinates.
    sharp=[]
    for x in g3[0]:
        sharp.append(0 if x[0]==0 else 1 if x[1:]==(0,0) else 2)
    assert admissible(sharp,g3[4])
    R={i for i,c in enumerate(sharp) if c==2}
    assert len(R)==16
    assert max(len(F) for F in g3[6] if F<=R)==3
    counts=audit_partition(sharp,g3)
    totals=[a+b for a,b in zip(totals,counts)]
    P,ix,add,neg,mid,cosets,flats=g3
    planes=[F for F in flats if len(F)==9]
    plane_masks=[sum(1<<x for x in F) for F in planes]
    small_blockers=0
    # Every set of at most six points misses an affine plane.
    # It suffices to check six-point sets, since smaller ones extend to them.
    for B in combinations(range(27),6):
        mask=sum(1<<x for x in B)
        assert any(mask&M==0 for M in plane_masks)
        small_blockers+=1
    def spans3(A):
        return not any(set(A)<=F for F in planes)
    five_spanning=0
    five_min=27
    for A in combinations(range(27),5):
        if not spans3(A):
            continue
        sums={add[x][y] for x in A for y in A}
        assert len(sums)>=11
        five_spanning+=1
        five_min=min(five_min,len(sums))
    four_classes=Counter()
    for A in combinations(range(27),4):
        sums={add[x][y] for x in A for y in A}
        if spans3(A):
            assert len(sums)==10
            four_classes['affine_basis']=four_classes['affine_basis']+1
        else:
            lines=[F for F in flats if len(F)==3 and F<=set(A)]
            if lines:
                assert len(sums)==7
                four_classes['line_and_point']+=1
            else:
                assert len(sums)==9
                four_classes['plane_cap']+=1
    # Exact arithmetic for the inherited cap-classification appendix.
    cap_moments={}
    for s in range(13):
        n4=Fraction(comb(s,3),4)
        n2=4*comb(s,2)-6*n4
        n1=13*s-8*comb(s,2)+2*comb(s,3)
        n0=39-13*s+4*comb(s,2)-3*n4
        feasible=all(Fraction(x).denominator==1 and x>=0 for x in (n0,n1,n2,n4))
        assert feasible == (s in (0,1,2,4))
        cap_moments[str(s)]={'n0':str(n0),'n1':str(n1),'n2':str(n2),'n4':str(n4),'feasible':feasible}
    bounds={str(n):20*2**(n-3)-4 for n in range(3,21)}
    assert bounds['3']==16
    for n in range(4,21):
        assert bounds[str(n)]==2*bounds[str(n-1)]+4
    assert 10*bounds['8']<3**8
    out={
      'status':'passed','arithmetic':'integer arithmetic and exact sets only',
      'scope':'Finite controls; general theorems are proved in RESEARCH-NOTE.tex.',
      'labelled_plane_partitions_examined':3**9,
      'admissible_labelled_plane_partitions':valid,
      'three_dimensional_product_partitions':len(sampled),
      'maximal_direction_fibre_audits':totals[0],
      'occupied_quotient_audits':totals[1],
      'plane_free_projection_audits':totals[2],
      'six_point_blocker_checks':small_blockers,
      'five_point_affinely_spanning_sets':five_spanning,
      'minimum_sumset_size_in_five_point_spanning_check':five_min,
      'four_point_classification_counts':dict(four_classes),
      'cap_incidence_moment_values':cap_moments,
      'sharp_three_space_construction':{'R':[P[x] for x in sorted(R)],'size':16,'maximum_affine_dimension':1},
      'plane_free_cardinality_upper_bounds':bounds
    }
    path=Path(__file__).with_name('MIDPOINT-CHECKS.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('sharp_three_space_construction','plane_free_cardinality_upper_bounds','cap_incidence_moment_values')},indent=2))
    print('Wrote',path.name)

if __name__=='__main__':
    main()
