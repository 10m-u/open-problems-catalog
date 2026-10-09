#!/usr/bin/env python3
"""Q3188 scan (preregistered): z(h) vs o1_AvA(h)-o2_AvA(h) for S={a<b}, b<=60, h<=4000."""
import json, sys
from subtraction import zero_sum

def ava(S, H):
    a, b = sorted(S)
    o1 = [0]*(H+1); o2 = [0]*(H+1)
    for h in range(a, H+1):
        best = None; other = None
        for s in (a, b):
            if s > h: continue
            mine = s + o2[h-s]; theirs = o1[h-s]
            if best is None or mine > best or (mine == best and theirs < other):
                best, other = mine, theirs
        o1[h], o2[h] = best, other
    return o1, o2

H, B = 4000, 60
mism = []
for b in range(2, B+1):
    for a in range(1, b):
        o1, o2 = ava((a, b), H)
        z = zero_sum((a, b), H)
        bad = [h for h in range(H+1) if z[h] != o1[h]-o2[h]]
        if bad: mism.append({'S': [a, b], 'first_h': bad[0], 'count': len(bad), 'z': z[bad[0]], 'ava': [o1[bad[0]], o2[bad[0]]]})
print(json.dumps({'pairs': B*(B-1)//2, 'H': H, 'mismatching_pairs': len(mism), 'first': mism[:10]}, indent=1))
json.dump({'pairs_tested': B*(B-1)//2, 'H': H, 'mismatches': mism}, open('q3188_scan.json','w'), indent=1)
