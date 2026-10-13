#!/usr/bin/env python3
"""Exact controls for cube proof-route obstructions; no asymptotic search."""
from itertools import combinations_with_replacement, product
from pathlib import Path
from collections import Counter
import json

HERE = Path(__file__).resolve().parent


def cube(xs, modulus=None):
    sums, nonempty = {0}, set()
    for x in xs:
        new = {s+x if modulus is None else (s+x) % modulus for s in sums}
        nonempty |= new
        sums |= new
    return nonempty


def free(a, d, modulus=None):
    return all(not cube(xs, modulus) <= a
               for xs in combinations_with_replacement(sorted(a), d))


def edges(d, modulus):
    return {frozenset(cube(xs, modulus))
            for xs in combinations_with_replacement(range(modulus), d)}


def main():
    counts = Counter()
    interval_totals = []
    for n in range(1, 73):
        # Twice the displayed fractional weights, all integer arithmetic.
        weights = {t: 0 if n < 4*t and 3*t <= n else 1 if 2*t <= n else 2
                   for t in range(1, n+1)}
        assert sum(weights.values()) == 2*n-n//2-(n//3-n//4)
        interval_totals.append([n, sum(weights.values()), 2])
        for xs in combinations_with_replacement(range(1, n+1), 3):
            if sum(xs) > n:
                continue
            c = cube(xs)
            assert sum(weights[t] for t in c) <= 2*(len(c)-1), (n,xs)
            if len(c) == 3:
                assert len(set(xs)) == 1
            proper = c - {sum(xs)}
            assert {sum(xs)-s for s in proper} == proper
            counts['integer_cube_fractional_constraints'] += 1
    for q in range(1, 13):
        n = 6*q
        a = set(range(2*q+1, n+1))
        assert free(a,3)
        assert cube((5*q,)*3,n) <= a
        low = {2*q,4*q,6*q-1}
        assert free(low,3)
        assert cube((2*q,)*3) <= {2*q,4*q,6*q}
        counts['integer_wrap_and_shift_families'] += 1
    residue_counts = {}
    for d, modulus in [(3,3),(3,4),(4,5)]:
        xs_good = [xs for xs in product(range(modulus),repeat=d)
                   if 0 not in cube(xs,modulus)]
        assert len(xs_good) == {(3,3):0,(3,4):2,(4,5):4}[d,modulus]
        residue_counts[f'd{d}-mod{modulus}'] = xs_good
        counts['ordered_residue_sequences'] += modulus**d
    b = {0,4,12,20,24,28,36}
    a = set(range(40))-b
    assert len(a) == 33
    assert all(any(k*x % 40 in b for k in range(1,5)) for x in range(40))
    assert cube((1,1,1,5,8),40) <= a
    for q in range(1,13):
        modulus = 40*q
        lifted_b = {x for x in range(modulus) if x % 40 in b}
        assert len(lifted_b) == 7*q
        for x in range(modulus):
            assert any(k*x % modulus in lifted_b for k in range(1,5))
            counts['diagonal_d5_lift_checks'] += 1
    assert free({1,4,7,10},4,12)
    assert not free(set(range(4)),4,4)
    a5 = {x for x in range(10) if x % 5}
    assert free(a5,5,10)
    assert {x % 2 for x in a5} == {0,1}
    e4 = edges(4,12)
    assert len(e4) == 433
    b4 = {0,2,10}
    assert all(c & b4 for c in e4)
    assert all(not {r,r+4,r+8} <= b4 for r in range(4))
    # Any free set omits0. No complement of size2 can cover all cubes,
    # certifying that the noncoset example really is maximum-cardinality.
    for other in range(1,12):
        assert any(not c.intersection({0,other}) for c in e4)
        counts['d4_maximum_upper_controls'] += 1
    counts['d4_full_distinct_cube_constraints'] = len(e4)
    for n in [8,16,32]:
        e3 = edges(3,n)
        for c in e3:
            if 0 not in c:
                assert len(c) >= 3
            assert 2*len(c-{0}) <= 3*(len(c)-1)
            counts['cyclic_fractional_constraints'] += 1
        if n <= 16:
            masks = [sum(1<<x for x in c) for c in e3]
            for mask in range(0,1<<n,2):
                if any(mask & edge == edge for edge in masks):
                    continue
                aa = {x for x in range(n) if mask >> x & 1}
                odd = {x for x in aa if x%2}
                even = aa-odd
                if 4*len(odd)>3*(n//2):
                    assert not any((u+v)%n in even for u in even for v in even)
                    assert len({x for x in even if x%4==2}) <= n//2-len(odd)
                    assert 8*len({x for x in even if x%4==0}) <= n
                    assert 8*len(aa) <= 5*n
                    counts['high_odd_exhaustive_controls'] += 1
                counts['small_cyclic_free_sets'] += 1
    for n in [8,16,32,64]:
        c3 = {x for x in range(n) if x%2 or x%8==4}
        assert len(c3) == 5*n//8 and free(c3,3,n)
        incidences = Counter()
        for x in range(1,n,2):
            incidences[x] += 1
            incidences[3*x % n] += 1
        assert all(v==2 for v in incidences.values())
        counts['tripling_incidence_vertices'] += len(incidences)
    odd = set(range(1,32,2))-{1,3,9,11}
    even = {4,16,20}
    assert free(even,3,32)
    assert not {x for x in odd if all((x+s)%32 in odd for s in [0,4,16,20])}
    assert cube((4,21,27),32) <= odd|even
    centered = set(range(1,32,2))|{2,6,10,14}
    assert cube((1,1,1),32) <= centered
    diagonal_a = {x for x in range(32) if x%2 or x%8==4}|{16}
    assert len(diagonal_a) == 21
    assert cube((1,4,12),32) <= diagonal_a
    for n in range(5,10):
        modulus=1<<n
        lifted_a={x for x in range(modulus) if x%32 in diagonal_a}
        for x in range(modulus):
            assert not {x,2*x % modulus,3*x % modulus} <= lifted_a
            counts['diagonal_d3_lift_checks'] += 1
    out={'status':'passed','counts':dict(counts),
         'interval_fractional_total_at_N72':[sum(0 if 72<4*t and 3*t<=72 else 1 if 2*t<=72 else 2 for t in range(1,73)),2],
         'ordered_zero_sum_free_residue_sequences':residue_counts,
         'noncoset_d4_extremizer_complement':sorted(b4),
         'd5_diagonal_complement':sorted(b),
         'scope':'Exact finite controls for all-size proofs and proposed-route obstructions; no conjecture counterexample or extrapolated solution.'}
    (HERE/'CUBE-CHECK-RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
