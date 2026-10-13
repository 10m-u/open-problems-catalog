#!/usr/bin/env python3
"""Exact rational certificates for entropy-increment witnesses.

No numerical library is used. The output intervals are certified using the
positive atanh series, its geometric tail bound, and outward rounding.
The optimization that suggested these laws is not part of the proof.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path

TERMS = 90
LOG_SCALE = 10**65
DISPLAY_SCALE = 10**40
F = Fraction


def floor_fraction(x: F) -> int:
    return x.numerator // x.denominator


def ceil_fraction(x: F) -> int:
    return -((-x.numerator) // x.denominator)


def unit_log(r: F) -> tuple[F, F]:
    if not F(1) <= r <= F(2):
        raise ValueError('The reduced logarithm argument must lie in [1, 2].')
    t = (r - 1) / (r + 1)
    t2 = t * t
    power, lower = t, F(0)
    for j in range(TERMS):
        lower += 2 * power / (2*j + 1)
        power *= t2
    tail = 2 * power / ((2*TERMS + 1) * (1 - t2))
    return lower, lower + tail


@lru_cache(maxsize=None)
def log_integer(n: int) -> tuple[F, F]:
    if n < 1:
        raise ValueError('A positive integer logarithm argument is required.')
    exponent = n.bit_length() - 1
    low, high = unit_log(F(n, 1 << exponent))
    low2, high2 = unit_log(F(2))
    low += exponent * low2
    high += exponent * high2
    # Outward rounding here keeps later rational sums small without losing rigor.
    return F(floor_fraction(low * LOG_SCALE), LOG_SCALE), F(ceil_fraction(high * LOG_SCALE), LOG_SCALE)


def entropy(counts: list[int]) -> tuple[F, F]:
    if not counts or min(counts) < 0 or sum(counts) <= 0:
        raise ValueError('Nonnegative counts of positive total mass are required.')
    total = sum(counts)
    low, high = log_integer(total)
    for c in counts:
        if c:
            cl, ch = log_integer(c)
            low -= F(c, total) * ch
            high -= F(c, total) * cl
    return low, high


def difference(a: tuple[F,F], b: tuple[F,F]) -> tuple[F,F]:
    return a[0] - b[1], a[1] - b[0]


def decimal_integer(n: int, digits: int = 40) -> str:
    sign = '-' if n < 0 else ''
    value = str(abs(n)).zfill(digits + 1)
    return sign + value[:-digits] + '.' + value[-digits:]


def interval_record(interval: tuple[F,F]) -> dict:
    lo = floor_fraction(interval[0] * DISPLAY_SCALE)
    hi = ceil_fraction(interval[1] * DISPLAY_SCALE)
    return {'lower': decimal_integer(lo), 'upper': decimal_integer(hi),
            'scaled_lower_integer': str(lo), 'scaled_upper_integer': str(hi),
            'decimal_scale': str(DISPLAY_SCALE)}


def certify(name: str, weights: list[int], threshold: F,
            support: list[int] | None = None) -> dict:
    support = list(range(len(weights))) if support is None else list(support)
    if len(support) != len(weights) or len(set(support)) != len(support):
        raise ValueError('Distinct support points matching the weight vector are required.')
    if not weights or any(not isinstance(w, int) or w <= 0 for w in weights):
        raise ValueError('Strictly positive integer weights are required.')
    sums: dict[int,int] = defaultdict(int)
    diffs: dict[int,int] = defaultdict(int)
    for x, a in zip(support, weights):
        for y, b in zip(support, weights):
            sums[x+y] += a*b
            diffs[x-y] += a*b
    total = sum(weights)
    assert sum(sums.values()) == total**2 == sum(diffs.values())
    h = entropy(weights)
    s = entropy(list(sums.values()))
    d = entropy(list(diffs.values()))
    ds = difference(s, h)
    dd = difference(d, h)
    assert ds[0] > 0 and dd[0] > 0
    ratio = dd[0] / ds[1], dd[1] / ds[0]
    assert ratio[0] > threshold
    assert F(floor_fraction(ratio[0]*DISPLAY_SCALE), DISPLAY_SCALE) < ratio[0]
    assert F(ceil_fraction(ratio[1]*DISPLAY_SCALE), DISPLAY_SCALE) > ratio[1]
    gap = (dd[0] - threshold*ds[1], dd[1] - threshold*ds[0])
    assert gap[0] > 0
    return {
        'name': name, 'status': 'passed', 'support': support,
        'probability_numerators': weights, 'probability_denominator': total,
        'sum_weights': {str(i): v for i, v in sorted(sums.items())},
        'difference_weights': {str(i): v for i, v in sorted(diffs.items())},
        'output_denominator': total**2,
        'entropy_nats': interval_record(h),
        'sum_increment_nats': interval_record(ds),
        'difference_increment_nats': interval_record(dd),
        'ratio': interval_record(ratio),
        'strict_lower_bound': str(threshold),
        'positive_gap_nats': interval_record(gap),
    }


def main() -> None:
    laws = [
        ('twelve_point', [88162313713840, 10154514342618, 1485728499913, 177389643984, 18240191721, 1665031585, 137417507, 10383619, 725058, 47123, 2867, 165], F(14051810329, 10**10)),
        ('prior_eight_point_control', [88162304, 10154519, 1485728, 177393, 18242, 1665, 138, 11], F(70259, 50000)),
    ]
    results = [certify(name, w, threshold) for name, w, threshold in laws]
    receipt = {
        'status': 'passed', 'arithmetic': 'exact integers and fractions only',
        'logarithm': 'range reduction to [1,2]; positive atanh series; rigorous tail bound; outward rounding',
        'series_terms': TERMS, 'intermediate_log_scale': str(LOG_SCALE),
        'scope': 'Explicit lower bounds only, not a global optimum or sharpness of 2.',
        'laws': results,
    }
    path = Path(__file__).with_name('ENTROPY-CERTIFICATE.json')
    path.write_text(json.dumps(receipt, indent=2) + '\n')
    for result in results:
        print(result['name'], result['ratio']['lower'], result['ratio']['upper'])
    print('Wrote', path.name)


if __name__ == '__main__':
    main()
