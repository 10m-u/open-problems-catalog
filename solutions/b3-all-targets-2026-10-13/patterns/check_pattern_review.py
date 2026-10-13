#!/usr/bin/env python3
"""Independent Q1366 audit: no imports of either root implementation."""
from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def normalize(word):
    answer = [0] * len(word)
    for rank, index in enumerate(sorted(range(len(word)), key=word.__getitem__), 1):
        answer[index] = rank
    return tuple(answer)


@lru_cache(None)
def patterns(top):
    return frozenset(normalize(tuple(top[i] for i in idx))
                     for k in range(len(top) + 1)
                     for idx in combinations(range(len(top)), k))


@lru_cache(None)
def small_patterns(top):
    return frozenset(normalize(tuple(top[i] for i in idx))
                     for k in range(1, min(4, len(top)) + 1)
                     for idx in combinations(range(len(top)), k))


def contains(bottom, top):
    # Independent relation-comparison test, rather than standardizing subsets.
    for idx in combinations(range(len(top)), len(bottom)):
        if all((bottom[i] < bottom[j]) == (top[idx[i]] < top[idx[j]])
               for i in range(len(bottom)) for j in range(i)):
            return True
    return False


def interval(bottom, top):
    return {p for p in patterns(top) if contains(bottom, p)}


def ranks(bottom, top):
    count = Counter(map(len, interval(bottom, top)))
    return [count[k] for k in range(len(bottom), len(top) + 1)]


def unimodal(row):
    return any(all(row[i] <= row[i + 1] for i in range(peak))
               and all(row[i] >= row[i + 1] for i in range(peak, len(row) - 1))
               for peak in range(len(row)))


def lc(row):
    return all(row[i] ** 2 >= row[i - 1] * row[i + 1]
               for i in range(1, len(row) - 1))


def layers(parts):
    word = []
    base = 0
    for size in parts:
        word.extend(reversed(range(base + 1, base + size + 1)))
        base += size
    return tuple(word)


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def maximum_matching(left, right, edges):
    # Subset dynamic programming, independent of root's augmenting-path code.
    choices = {0}
    for a in left:
        following = set(choices)
        for mask in choices:
            for i, b in enumerate(right):
                if b in edges[a] and not mask & (1 << i):
                    following.add(mask | (1 << i))
        choices = following
    return max(mask.bit_count() for mask in choices)


def main():
    probe = json.loads((HERE / 'PATTERN-PROBE.json').read_text())
    bytop = defaultdict(list)
    for record in probe['records']:
        bytop[tuple(record['top'])].append(record)
    rng = random.Random(1366)
    specified_tops = set()
    for n in range(8, 13):
        for i in range(8):
            top = list(range(1, n + 1))
            rng.shuffle(top)
            specified_tops.add(tuple(top))
        specified_tops.update(layers((a, n - a)) for a in range(2, n - 1))
        specified_tops.add(tuple(range(2, n + 1, 2)) + tuple(range(1, n + 1, 2)))
    assert set(bytop) == specified_tops and len(bytop) == 80
    interval_controls = 0
    top_subset_controls = 0
    for top, records in bytop.items():
        lower = patterns(top)
        top_subset_controls += 2 ** len(top)
        actual_rows = defaultdict(Counter)
        for p in lower:
            for s in small_patterns(p):
                actual_rows[s][len(p)] += 1
        assert {tuple(r['bottom']) for r in records} == {s for s in lower if 1 <= len(s) <= 4}
        for record in records:
            s = tuple(record['bottom'])
            actual = [actual_rows[s][k] for k in range(len(s), len(top) + 1)]
            assert actual == record['row']
            assert unimodal(actual) == record['unimodal']
            assert lc(actual) == record['LC']
            assert unimodal(actual)
            interval_controls += 1
    assert interval_controls == 1573

    hall = probe['Hall_obstruction']
    bottom, top = tuple(hall['bottom']), tuple(hall['top'])
    actual = interval(bottom, top)
    row = ranks(bottom, top)
    assert row == [1, 3, 7, 7, 1]
    left = sorted(p for p in actual if len(p) == 5)
    right = sorted(p for p in actual if len(p) == 6)
    edges = {p: {q for q in right if contains(p, q)} for p in left}
    witness = set(map(tuple, hall['witness']['left']))
    neighbors = set().union(*(edges[p] for p in witness))
    assert witness <= set(left)
    assert neighbors == set(map(tuple, hall['witness']['neighbors']))
    assert len(witness) == 5 and len(neighbors) == 4
    assert maximum_matching(left, right, edges) == 6

    equal_layer_controls = 0
    for count in range(1, 5):
        for a in product(range(1, 4), repeat=count):
            if sum(a) > 9:
                continue
            for b in product(*(range(1, x + 1) for x in a)):
                expected = [1]
                for x, y in zip(a, b):
                    expected = convolution(expected, [1] * (x - y + 1))
                assert ranks(layers(b), layers(a)) == expected and lc(expected)
                equal_layer_controls += 1

    formula_controls = literal_two_controls = 0
    for a in range(1, 31):
        for b in range(a, 31):
            for s in range(1, b + 1):
                actual = Counter(range(s, b + 1))
                actual.update(i + j for i in range(1, a + 1)
                              for j in range(1, b + 1) if max(i, j) >= s)
                expected = []
                for r in range(s, a + b + 1):
                    if s <= a:
                        coefficient = (1 + 2 * (r - s) - max(0, r - a - 1)
                            - max(0, r - b) - max(0, r - 2 * s + 1))
                    else:
                        coefficient = 1 + r - s - max(0, r - b) - max(0, r - a - s)
                    assert actual[r] == coefficient > 0
                    expected.append(coefficient)
                assert lc(expected)
                assert all(expected[i - 1] + expected[i + 1] <= 2 * expected[i]
                           for i in range(1, len(expected) - 1))
                formula_controls += 1
                if a + b <= 9:
                    assert ranks(layers((s,)), layers((a, b))) == expected
                    literal_two_controls += 1

    fiber_controls = 0
    for p in range(5):
        for q in range(5):
            top = tuple(range(1, p + 1)) + (p + 2, p + 1) + tuple(range(p + 3, p + q + 3))
            occurrences = Counter()
            for size in range(2, len(top) + 1):
                for idx in combinations(range(len(top)), size):
                    pattern = normalize(tuple(top[i] for i in idx))
                    if contains((2, 1), pattern):
                        assert {p, p + 1} <= set(idx)  # coverage is perfect
                        occurrences[pattern] += 1
            for u in range(p + 1):
                for v in range(q + 1):
                    pattern = tuple(range(1, u + 1)) + (u + 2, u + 1) + tuple(range(u + 3, u + v + 3))
                    assert occurrences[pattern] == comb(p, u) * comb(q, v)
                    fiber_controls += 1
            assert ranks((2, 1), top) == convolution([1] * (p + 1), [1] * (q + 1))

    top = (2, 1, 4, 3)
    missing = []
    actual = interval((2, 1), top)
    for occurrence in [(0, 1), (2, 3)]:
        fixed = {normalize(tuple(top[i] for i in idx))
                 for size in range(2, 5) for idx in combinations(range(4), size)
                 if set(occurrence) <= set(idx)}
        assert Counter(map(len, fixed)) == {2: 1, 3: 1, 4: 1}
        assert actual - fixed
        missing.append(sorted(actual - fixed))
    assert missing == [[(1, 3, 2)], [(2, 1, 3)]]

    top = (2, 4, 1, 3)
    deleted = [normalize(top[:i] + top[i + 1:]) for i in range(4)]
    downsets = [interval((1,), p) for p in deleted]
    assert len(set(deleted)) == 4
    for i, j in combinations(range(4), 2):
        assert downsets[i] & downsets[j] == {(1,), (1, 2), (2, 1)}
    assert ranks((1,), top) == [1, 2, 4, 1]
    A = [1, 3, 3, 3, 1]
    H = [1, 1, 3, 1, 1]
    union = [2 * a - h for a, h in zip(A, H)]
    assert unimodal(A) and unimodal(H) and all(h <= a for h, a in zip(H, A))
    assert union == [1, 5, 3, 5, 1] and not unimodal(union)

    files = ['Q1366-ATTEMPTS.md', 'LAYERED-INTERVALS.md', 'pattern_probe.py',
             'PATTERN-PROBE.json', 'check_pattern_routes.py', 'PATTERN-ROUTES-CHECK.json']
    receipt = {'status': 'PASS', 'independent_root_imports': False,
        'literal_top_subset_controls': top_subset_controls,
        'fresh_records_recomputed': interval_controls, 'actual_top_count': len(bytop),
        'actual_tops_above_original_published_length8_range': sum(len(t) > 8 for t in bytop),
        'Hall_rank_row': row, 'Hall_subset_size': 5, 'Hall_neighbor_size': 4,
        'Hall_maximum_matching_by_subset_DP': 6,
        'equal_layer_literal_controls': equal_layer_controls,
        'two_layer_formula_controls': formula_controls,
        'two_layer_literal_controls': literal_two_controls,
        'unique_inversion_individual_fibers_checked': fiber_controls,
        'both_fixed_occurrences_of2143_fail_coverage': True,
        'all_pairwise_deletion_intersections_of2413_checked': 6,
        'formal_gluing_row_not_claimed_actual': True,
        'scope': 'Independent bounded controls; written all-size proofs and route contracts reviewed separately.',
        'reviewed_sha256': {f: sha256((HERE / f).read_bytes()).hexdigest() for f in files},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'PATTERN-REVIEW-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'reviewed_sha256'}, indent=2))


if __name__ == '__main__':
    main()
