#!/usr/bin/env python3
"""Certify the saved small-law witness using rational logarithm intervals."""
from fractions import Fraction as F
from math import log
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
TERMS = 60
SCALE = 10**35


def unit_log(r):
    assert 1 <= r <= 2
    t = (r-1)/(r+1)
    power = t
    total = F(0)
    for j in range(TERMS):
        total += 2*power/(2*j+1)
        power *= t*t
    remainder = 2*power/((2*TERMS+1)*(1-t*t))
    return total, total+remainder


def integer_log(n):
    assert n >= 1
    e = n.bit_length()-1
    lo, hi = unit_log(F(n, 2**e))
    l2, h2 = unit_log(F(2))
    return lo+e*l2, hi+e*h2


def entropy(counts):
    total = sum(counts)
    lower, upper = integer_log(total)
    for count in counts:
        lo, hi = integer_log(count)
        lower -= F(count,total)*hi
        upper -= F(count,total)*lo
    return lower, upper


def scaled_interval(interval):
    lo, hi = interval
    lower = lo*SCALE
    upper = hi*SCALE
    return [lower.numerator//lower.denominator,
            -((-upper.numerator)//upper.denominator)]


def main():
    support = [1,3,5]
    counts = [913,79,8]
    sums, differences = {}, {}
    for i, x in enumerate(support):
        for j, y in enumerate(support):
            weight = counts[i]*counts[j]
            sums[x+y] = sums.get(x+y,0)+weight
            differences[x-y] = differences.get(x-y,0)+weight
    h, s, d = entropy(counts), entropy(list(sums.values())), entropy(list(differences.values()))
    ds = (s[0]-h[1], s[1]-h[0])
    dd = (d[0]-h[1], d[1]-h[0])
    assert ds[0] > 0 and dd[0] > 0
    ratio = (dd[0]/ds[1], dd[1]/ds[0])
    assert ratio[0] > F(139,100)
    result = {'status':'passed', 'support':support, 'probability_numerators':counts,
              'probability_denominator':sum(counts),
              'sum_counts':{str(x):c for x,c in sorted(sums.items())},
              'difference_counts':{str(x):c for x,c in sorted(differences.items())},
              'output_count_denominator':sum(counts)**2,
              'logarithm_method':'range reduction and positive atanh series with rational tail bound',
              'series_terms':TERMS, 'interval_scale':str(SCALE),
              'sum_entropy_increment_scaled_interval':[str(x) for x in scaled_interval(ds)],
              'difference_entropy_increment_scaled_interval':[str(x) for x in scaled_interval(dd)],
              'ratio_scaled_interval':[str(x) for x in scaled_interval(ratio)],
              'certified_lower_bound':'139/100',
              'scope':'An admissible lower-bound witness, not a global optimum or sharpness of 2.'}
    (HERE/'CERTIFIED-LAW-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
