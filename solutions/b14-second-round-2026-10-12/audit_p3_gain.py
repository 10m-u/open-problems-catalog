#!/usr/bin/env python3
"""Independent exact audit of conditional one-edge 2-opt gain pieces."""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def path_masks(n,edges):
    adj = [[] for _ in range(n)]
    for i,(a,b) in enumerate(edges):
        adj[a].append((b,i)); adj[b].append((a,i))
    out = {}
    for start,end in combinations(range(n),2):
        paths = []
        def walk(v,seen,mask):
            if v==end: paths.append(mask); return
            for w,i in adj[v]:
                if w not in seen: walk(w,seen|{w},mask|(1<<i))
        walk(start,{start},0)
        assert paths
        out[start,end] = paths
    return out


def controls(n,edges,seed):
    paths = path_masks(n,edges); m = len(edges)
    rng = random.Random(seed)
    base = 1<<m
    weights = [base*rng.randrange(1,10)+(1<<i) for i in range(m)]
    chosen = {}
    for pair,options in paths.items():
        ranked = sorted((sum(w for i,w in enumerate(weights) if mask>>i&1),mask) for mask in options)
        assert len(ranked)==1 or ranked[0][0]<ranked[1][0]
        chosen[pair] = ranked[0]
    pieces,nonflat,positive,gradient_checks = 0,0,0,0
    normalized_pieces, eligible_normalized_pieces = 0,0
    eps = F(1,3)
    for a,b,c,d in permutations(range(n),4):
        pairs = [tuple(sorted(p)) for p in ((a,b),(c,d),(a,c),(b,d))]
        signs = [1,1,-1,-1]
        gain = sum(s*chosen[p][0] for s,p in zip(signs,pairs))
        coefficient = [sum(s*((chosen[p][1]>>i)&1) for s,p in zip(signs,pairs)) for i in range(m)]
        assert gain==sum(v*w for v,w in zip(coefficient,weights))
        if gain>0:
            assert any(coefficient); positive += 1
        gradient_checks += 1
        for e in range(m):
            lines = []
            breakpoints = {F(0)}
            for p in pairs:
                A = B = None
                for mask in paths[p]:
                    value = sum(w for i,w in enumerate(weights) if i!=e and mask>>i&1)
                    if mask>>e&1:
                        A = value if A is None else min(A,value)
                    else:
                        B = value if B is None else min(B,value)
                lines.append((A,B))
                if A is not None and B is not None and B>A:
                    breakpoints.add(F(B-A))
            ordered = sorted(breakpoints)
            assert len(ordered)<=5
            length = F(0)
            for j,left in enumerate(ordered):
                right = ordered[j+1] if j+1<len(ordered) else None
                midpoint = (left+right)/2 if right is not None else left+1
                slopes=[]; values=[]
                for A,B in lines:
                    use_edge = B is None or (A is not None and A+midpoint<B)
                    slopes.append(int(use_edge))
                    values.append(A+midpoint if use_edge else F(B))
                slope = sum(s*v for s,v in zip(signs,slopes))
                at = sum(s*v for s,v in zip(signs,values))
                intercept = at-slope*midpoint
                assert slope in (-2,-1,0,1,2)
                pieces += 1
                if not slope: continue
                nonflat += 1
                x,y = sorted((-intercept/slope,(eps-intercept)/slope))
                x = max(x,left); y = y if right is None else min(y,right)
                extent = max(F(0),y-x)
                assert extent<=eps/abs(slope)
                length += extent
            assert length<=5*eps
            # Independently condition on normalized ratios of the OTHER weights.
            other_total = sum(weights)-weights[e]
            normalized = [(None if A is None else F(A,other_total),
                           None if B is None else F(B,other_total)) for A,B in lines]
            endpoints = {F(0),F(1)}
            for A,B in normalized:
                if A is not None and B is not None and B>A:
                    endpoints.add((B-A)/(1+B-A))
            endpoints = sorted(endpoints)
            assert len(endpoints)<=6
            length = F(0)
            for left,right in zip(endpoints,endpoints[1:]):
                t = (left+right)/2
                raw_coefficient = 0; other_coefficient = F(0)
                for sign,(A,B) in zip(signs,normalized):
                    use_edge = B is None or (A is not None and (1-t)*A+t<(1-t)*B)
                    raw_coefficient += sign*int(use_edge)
                    other_coefficient += sign*(A if use_edge else B)
                slope = raw_coefficient-other_coefficient
                normalized_pieces += 1
                if not raw_coefficient: continue
                eligible_normalized_pieces += 1
                if not slope:
                    # Constant nonzero integer gain cannot be in (0,eps].
                    assert not 0<other_coefficient<=eps
                    continue
                x,y = sorted((-other_coefficient/slope,
                              (eps-other_coefficient)/slope))
                x=max(x,left);y=min(y,right)
                extent=max(F(0),y-x)
                if extent:
                    assert abs(slope)>=1-eps
                assert extent<=eps/(1-eps)
                length += extent
            assert length<=5*eps/(1-eps)
    return {'n':n,'m':m,'quadruples':gradient_checks,'positive_gains':positive,
            'conditional_pieces':pieces,'nonflat_pieces':nonflat,
            'normalized_pieces':normalized_pieces,
            'eligible_normalized_pieces':eligible_normalized_pieces}


def main():
    rows = []
    for n in (4,5,6):
        tree = [(i-1,i) for i in range(1,n)]
        cycle = tree+[(0,n-1)]
        graph = cycle+[(0,2),(1,n-1)]
        for i,edges in enumerate((tree,cycle,graph)):
            rows.append(controls(n,sorted(set(edges)),100*n+i))
    result = {'status':'passed','rows':rows,
              'scope':'exact finite conditional-piece controls; expectation theorem audited analytically'}
    (HERE/'P3-INDEPENDENT-CHECK-RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed',
        'quadruples':sum(r['quadruples'] for r in rows),
        'conditional_pieces':sum(r['conditional_pieces'] for r in rows),
        'nonflat_pieces':sum(r['nonflat_pieces'] for r in rows),
        'normalized_pieces':sum(r['normalized_pieces'] for r in rows),
        'eligible_normalized_pieces':sum(r['eligible_normalized_pieces'] for r in rows)},indent=2))


if __name__=='__main__': main()
