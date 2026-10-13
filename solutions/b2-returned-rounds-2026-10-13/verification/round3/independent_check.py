#!/usr/bin/env python3
"""Independent, bounded round-III controls; standard library only.

No imports from submission scripts. Affine flats are generated from line
directions and hyperplane equations rather than the submission's closure
algorithm. Entropy intervals are recomputed without rounded log caches.
These finite controls do not prove the infinite-tail or all-size theorems.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib
import json


def plus(x, y):
    return tuple((a+b) % 3 for a, b in zip(x, y))


def minus(x, y):
    return tuple((a-b) % 3 for a, b in zip(x, y))


def midpoint(x, y):
    return tuple(2*(a+b) % 3 for a, b in zip(x, y))


def scale(a, x):
    return tuple(a*b % 3 for b in x)


def geometry(n):
    points = tuple(product(range(3), repeat=n))
    zero = (0,)*n
    directions = {min(v, scale(2, v)) for v in points if v != zero}
    lines = {frozenset(plus(a, scale(t, v)) for t in range(3))
             for a in points for v in directions}
    flats = {frozenset({p}) for p in points} | lines | {frozenset(points)}
    if n == 3:
        planes = {frozenset(x for x in points
                            if sum(a*b for a, b in zip(v, x)) % 3 == level)
                  for v in directions for level in range(3)}
        assert len(planes) == 39
        flats |= planes
    assert len(lines) == (12 if n == 2 else 117)
    index = {p:i for i,p in enumerate(points)}
    mids = tuple(tuple(index[midpoint(x,y)] for y in points) for x in points)
    return points, flats, mids


def audit(labels, points, flats, mids):
    R = {p for p, lab in zip(points, labels) if lab == 2}
    if not R:
        return 0
    col = dict(zip(points, labels))
    largest = max(len(f) for f in flats if f <= R)
    directions = {frozenset(minus(x, min(f)) for x in f)
                  for f in flats if len(f) == largest and f <= R}
    cases = 0
    for V in directions:
        fibres = sorted({frozenset(plus(a, v) for v in V) for a in points},
                        key=lambda f: min(f))
        q_of = {p:q for q,f in enumerate(fibres) for p in f}
        reps = [min(f) for f in fibres]
        qm = [[q_of[midpoint(x,y)] for y in reps] for x in reps]
        S = {q for q,f in enumerate(fibres) if f <= R}
        D = {q for q,f in enumerate(fibres) if f & R}
        assert len(S) in (1,2,4)
        assert all(qm[q][t] not in S for q in S for t in S if q != t)
        isolated = []
        for q,f in enumerate(fibres):
            if q in S:
                continue
            neighbours = [t for t in range(len(fibres))
                          if t not in S and t != q and qm[q][t] in S]
            if neighbours:
                C = f - R
                assert C and len({col[x] for x in C}) == 1
                assert all(midpoint(x,y) in C for x in C for y in C)
                assert len(C) in [3**j for j in range(4)]
            else:
                isolated.append(q)
                assert {q_of[minus(scale(2,reps[q]), reps[s])] for s in S} == S
        assert len(isolated) == (0 if len(S) == 1 else 1)
        qcolors = {q:col[min(f)] for q,f in enumerate(fibres) if q not in D}
        assert all(qm[q][t] not in D for q in qcolors for t in qcolors
                   if qcolors[q] == qcolors[t])
        if largest == 3 and not any(len(f) == 9 and f <= R for f in flats):
            assert len(R) <= 2*len(D)+len(S)
            if len(points) == 27:
                assert len(D) < 9
        cases += 1
    return cases


@lru_cache(None)
def log_interval(n):
    """35-term atanh bounds, exactly retained as fractions (no rounding)."""
    assert n >= 1
    def reduced(r):
        t = (r-1)/(r+1)
        lo = sum((2*t**(2*j+1)/F(2*j+1) for j in range(35)), F(0))
        return lo, lo + 2*t**71/(71*(1-t*t))
    k = n.bit_length()-1
    lo,hi = reduced(F(n, 2**k))
    l2,u2 = reduced(F(2))
    return lo+k*l2, hi+k*u2


def entropy_interval(weights):
    W = sum(weights)
    lo,hi = log_interval(W)
    for w in weights:
        if w:
            a,b = log_interval(w)
            lo -= F(w,W)*b
            hi -= F(w,W)*a
    return lo,hi


def ratio_interval(weights):
    q,r = Counter(),Counter()
    for x,a in enumerate(weights):
        for y,b in enumerate(weights):
            q[x+y] += a*b
            r[x-y] += a*b
    h = entropy_interval(weights)
    s = entropy_interval(tuple(q.values()))
    d = entropy_interval(tuple(r.values()))
    ds = s[0]-h[1], s[1]-h[0]
    dd = d[0]-h[1], d[1]-h[0]
    assert min(ds+dd) > 0
    return dd[0]/ds[1], dd[1]/ds[0]


def gradient_controls():
    cases = 0
    for support in [(0,1), (0,1,2), (0,2,5,9), (-8,-1,3,11,13)]:
        for ws in [tuple(range(1,len(support)+1)), (2,)*len(support)]:
            p = dict(zip(support, (F(w,sum(ws)) for w in ws)))
            for base in support:
                for target in support:
                    if base == target:
                        continue
                    v = {x:F((x==target)-(x==base)) for x in support}
                    q,r,dq,dr = [defaultdict(F) for _ in range(4)]
                    for x in support:
                        for y in support:
                            q[x+y] += p[x]*p[y]
                            r[x-y] += p[x]*p[y]
                            dq[x+y] += v[x]*p[y]+p[x]*v[y]
                            dr[x-y] += v[x]*p[y]+p[x]*v[y]
                    rho=F(19,13)
                    direct=defaultdict(F)
                    for out,deriv,mult in [(r,dr,-1),(q,dq,rho),(p,v,-(rho-1))]:
                        for x,w in deriv.items():
                            direct[out[x]] += mult*w
                    expected=defaultdict(F)
                    for n,sign in [(target,1),(base,-1)]:
                        for j in support:
                            expected[r[n-j]] -= sign*2*p[j]
                            expected[q[n+j]] += sign*2*rho*p[j]
                        expected[p[n]] -= sign*(rho-1)
                    clean=lambda a:{x:w for x,w in a.items() if x!=1 and w}
                    assert clean(direct)==clean(expected)
                    cases += 1
    return cases


def main():
    points, flats, mids = geometry(2)
    p3,f3,m3 = geometry(3)
    valid,plane_audits,lift_audits = 0,0,0
    for lab in product(range(3),repeat=9):
        if any(lab[mids[i][j]] == 2 for i in range(9) for j in range(9)
               if lab[i] == lab[j] and lab[i] != 2):
            continue
        valid += 1
        plane_audits += audit(lab,points,flats,mids)
        lookup=dict(zip(points,lab))
        lifted=tuple(lookup[x[:2]] for x in p3)
        lift_audits += audit(lifted,p3,f3,m3)
    sharp=tuple(0 if x[0]==0 else 1 if x[1:]==(0,0) else 2 for x in p3)
    assert not any(sharp[m3[i][j]] == 2 for i in range(27) for j in range(27)
                   if sharp[i]==sharp[j] and sharp[i]!=2)
    R={x for x,l in zip(p3,sharp) if l==2}
    assert len(R)==16 and max(len(f) for f in f3 if f<=R)==3
    sharp_audits=audit(sharp,p3,f3,m3)
    E={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}
    sumsizes=[]
    for v in p3:
        if v not in E:
            A=E|{v}
            sumsizes.append(len({plus(x,y) for x in A for y in A}))
    assert len(sumsizes)==23 and min(sumsizes)>=11
    weights=[2**(64-n*n) for n in range(9)]
    before=ratio_interval(weights)
    after_ws=[w*10**12 for w in weights]
    after_ws[0]-=sum(weights); after_ws[6]+=sum(weights)
    after=ratio_interval(after_ws)
    assert after[0] > before[1]
    result={
        'status':'passed',
        'scope':'Independent finite controls only; analytic review is ROUND3-REVIEW.md.',
        'submission_code_imported':False,
        'plane_labelings_examined':3**9,
        'admissible_plane_labelings':valid,
        'plane_maximum_flat_directions_checked':plane_audits,
        'three_space_lifted_partitions_checked':valid,
        'lifted_maximum_flat_directions_checked':lift_audits,
        'sharp_construction_size':len(R),
        'sharp_construction_maximum_flat_size':3,
        'sharp_maximum_flat_directions_checked':sharp_audits,
        'normalized_spanning_five_sets_checked':len(sumsizes),
        'normalized_spanning_five_set_minimum_sumset_size':min(sumsizes),
        'independent_gradient_controls':gradient_controls(),
        'entropy_interval_method':'35 atanh terms, geometric upper remainder, unrounded fractions',
        'finite_ascent_certified':True,
        'finite_ascent_gap_lower_rational':str(
            F(int((after[0]-before[1])*10**40), 10**40)),
    }
    home=Path(__file__).resolve().parent
    preservation=json.loads((home/'PRESERVATION.json').read_text())
    source=home.parent.parent/'round3'
    after_hashes={str(p.relative_to(source)):hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted(source.rglob('*')) if p.is_file()}
    if (source/'BASELINE-TARGETS.json').exists():
        assert after_hashes == preservation['source_sha256_before']
        result['submission_files_preserved']=True
        result['submission_file_count']=len(after_hashes)
    else:
        result['submission_files_preserved']='historical private-source audit'
        result['submission_file_count']=None
        result['preservation_note']='Private snapshots omitted and public links adapted; original-byte audit retained in PRESERVATION.json.'
    comparisons={}
    for name in ['MIDPOINT-CHECKS.json','ENTROPY-VARIATION-CHECKS.json']:
        copied=json.loads((home/name).read_text())
        original=json.loads((source/name).read_text())
        assert copied==original
        comparisons[name]='identical JSON content'
    result['copied_replay_receipts']=comparisons
    (home/'INDEPENDENT-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k!='finite_ascent_gap_lower_rational'},indent=2))


if __name__=='__main__':
    main()
