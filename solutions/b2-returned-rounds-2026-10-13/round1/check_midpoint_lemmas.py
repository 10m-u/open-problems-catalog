#!/usr/bin/env python3
"""Exhaustive finite controls for elementary steps of the midpoint proof.

These checks do NOT replace the all-dimension proof, and do NOT independently
verify the cited polynomial Freiman--Ruzsa theorem. Python standard library only.
"""
from __future__ import annotations
from itertools import product
from fractions import Fraction as F
import json
from pathlib import Path

POINTS = [(x, y) for y in range(3) for x in range(3)]
INDEX = {p: i for i, p in enumerate(POINTS)}
FULL = (1 << len(POINTS)) - 1
POPCOUNT = [s.bit_count() for s in range(FULL + 1)]


def mask_of(indices) -> int:
    return sum(1 << i for i in indices)


def hyperplanes() -> list[int]:
    lines = set()
    for a, b in product(range(3), repeat=2):
        if a == b == 0:
            continue
        for c in range(3):
            lines.add(mask_of(i for i, (x, y) in enumerate(POINTS) if (a*x+b*y-c) % 3 == 0))
    assert len(lines) == 12 and all(POPCOUNT[v] == 3 for v in lines)
    return sorted(lines)


def midpoint_masks() -> list[int]:
    mids = []
    for mask in range(FULL+1):
        points = [POINTS[i] for i in range(9) if (mask >> i) & 1]
        mids.append(mask_of(set(INDEX[((2*(x+u)) % 3, (2*(y+v)) % 3)]
                                     for x,y in points for u,v in points)))
    return mids


def check_partitions() -> dict:
    lines = hyperplanes()
    mids = midpoint_masks()
    best = [max(POPCOUNT[r & line] for line in lines) for r in range(FULL+1)]
    records = []
    for k in (1, 2, 3):
        total = admissible = proper = 0
        for labels in product(range(k+1), repeat=9):
            total += 1
            masks = [0]*(k+1)
            for i, colour in enumerate(labels):
                masks[colour] |= 1 << i
            r = masks[0]
            if r == 0 or any(mids[a] & r for a in masks[1:]):
                continue
            admissible += 1
            if r == FULL:
                continue
            proper += 1
            a = POPCOUNT[r]
            b = max(POPCOUNT[c] for c in masks[1:])
            c = best[r]
            # c/3 >= (a/9)*(1 + (b/9)/2).
            assert 54*c >= a*(18+b)
            # Odds multiplier at least 1 + 1/(2k); full fibres terminate.
            if c != 3:
                assert 2*k*c*(9-a) >= (2*k+1)*a*(3-c)
        records.append({'k':k, 'all_labelled_partitions':total,
                        'admissible_nonempty_R':admissible,
                        'proper_R_increment_checks':proper})
    return {'field':3, 'dimension':2, 'empty_colour_classes_allowed':True,
            'records':records, 'arithmetic':'integer inequalities only'}


def check_avoidance() -> dict:
    records = []
    for d, flats in [(1, hyperplanes()), (2, [1 << i for i in range(9)])]:
        q = 3**d
        n = len(flats)
        size = 9//q
        # Exact uniform point inclusion and unconditional density expectation.
        assert all(sum(bool(v & (1 << i)) for v in flats)*q == n for i in range(9))
        for b in range(FULL+1):
            assert sum(POPCOUNT[b & v] for v in flats)*q == n*POPCOUNT[b]
        set_pairs = weight_cases = cover_sets = 0
        for cover in range(FULL+1):
            m = POPCOUNT[cover]
            if m >= q:
                continue
            cover_sets += 1
            good = [v for v in flats if not (v & cover)]
            assert len(good)*q >= n*(q-m) and good
            for b in range(FULL+1):
                values = [POPCOUNT[b & v] for v in good]
                # Conditional expectation and existence bounds, cleared of denominators.
                assert sum(values)*(q-m) <= len(good)*POPCOUNT[b]
                assert min(values)*(q-m) <= POPCOUNT[b]
                set_pairs += 1
            for seed in range(12):
                weights = [((seed+3)*(i+1)**2+5*i+seed**2) % 17 for i in range(9)]
                values = [sum(w for i,w in enumerate(weights) if v & (1 << i)) for v in good]
                assert sum(values)*(q-m) <= len(good)*sum(weights)
                assert min(values)*(q-m) <= sum(weights)
                weight_cases += 1
        records.append({'codimension':d, 'affine_flats':n, 'flat_size':size,
                        'cover_sets':cover_sets, 'all_cover_test_set_pairs':set_pairs,
                        'additional_nonnegative_weight_cases':weight_cases})
    return {'field':3, 'quotient_dimension':2, 'records':records,
            'arithmetic':'integer inequalities only'}


def check_scalar_bounds() -> dict:
    count = 0
    for k in range(1, 101):
        survival = (1-F(1, 2*k))**k
        assert survival >= F(1, 2)
        for a in range(1, 100):
            alpha = F(a, 100)
            new = alpha*(1+(1-alpha)/(2*k))
            assert new < 1
            assert (new/(1-new))/(alpha/(1-alpha)) >= 1+F(1,2*k)
            count += 1
    return {'k_range':[1,100], 'alpha_grid':'1/100 through 99/100',
            'odds_checks':count, 'cumulative_loss_checks':100,
            'arithmetic':'exact fractions'}


def main() -> None:
    receipt = {'status':'passed', 'partition_increment':check_partitions(),
               'quotient_avoidance':check_avoidance(),
               'scalar_bounds':check_scalar_bounds(),
               'scope':'Finite controls of elementary lemmas only; all-dimension theorem is proved in the manuscript using cited PFR.'}
    out = Path(__file__).with_name('MIDPOINT-CHECKS.json')
    out.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__ == '__main__':
    main()
