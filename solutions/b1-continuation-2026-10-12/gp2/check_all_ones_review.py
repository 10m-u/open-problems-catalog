#!/usr/bin/env python3
"""Independent bounded controls of the finite greedy-orbit proof."""
from functools import lru_cache
from fractions import Fraction
import cmath
import json
import math
from pathlib import Path


def factorized(a, w):
    return math.prod(abs(math.sin(math.pi*a/(1 << j))) for j in range(1, w+1))


def greedy(t, h):
    product = 1.0
    for _ in range(h):
        product *= math.sin(math.pi*float(t))
        t = (1-t)/2
    return product


@lru_cache(None)
def optimal(t, h):
    factor = math.sin(math.pi*float(t))
    if h == 1:
        return factor
    return factor*max(optimal(t/2, h-1), optimal((1-t)/2, h-1))


def main():
    direct_checks = frequency_checks = dp_checks = branch_checks = 0
    maxima = []
    for w in range(1, 13):
        size = 1 << w
        a_star = (size+(-1)**(w-1))//3
        q = Fraction(1, 2)
        predicted = greedy(q, w)
        assert a_star % 2 == 1
        observed = max(factorized(a, w) for a in range(1, size))
        assert abs(predicted-observed) < 2e-12
        assert abs(predicted-factorized(a_star, w)) < 2e-12
        assert abs(predicted-factorized(size-a_star, w)) < 2e-12
        frequency_checks += size-1
        maxima.append({"w": w, "attaining_frequency": a_star, "maximum": predicted})
        if w <= 6:
            for a in range(size):
                direct = sum(cmath.exp(-2j*math.pi*a*x/size)*(-1)**x.bit_count()
                             for x in range(size))/size
                assert abs(abs(direct)-factorized(a, w)) < 2e-12
                direct_checks += 1
    for numerator in range(33):
        t = Fraction(numerator, 64)
        u, v = (1-t)/2, t/2
        for h in range(1, 10):
            assert abs(optimal(t, h)-greedy(t, h)) < 2e-13
            dp_checks += 1
            assert greedy(u, h)+2e-13 >= greedy(v, h)
            branch_checks += 1
    result = {
        "status": "passed",
        "direct_normalized_Fourier_sum_checks": direct_checks,
        "frequency_values_exhausted": frequency_checks,
        "all_widths": [1, 12],
        "rational_start_independent_DP_comparisons": dp_checks,
        "whole_continuation_branch_comparisons": branch_checks,
        "DP_states": optimal.cache_info().currsize,
        "maxima": maxima,
        "scope": "Floating-point finite controls supplement exact all-size mathematical review.",
    }
    Path(__file__).with_name("ALL-ONES-REVIEW-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "maxima"}, indent=2))


if __name__ == "__main__":
    main()
