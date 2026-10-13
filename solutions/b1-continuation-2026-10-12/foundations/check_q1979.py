"""Exact finite controls for the Q1979 route packet; no all-model claim."""
from itertools import combinations
import json
from pathlib import Path


def interval_traces(sample, h):
    lo, hi = min(sample) - h - 2, max(sample) + h + 2
    return {tuple(x for x in sample if y <= x <= z)
            for y in range(lo, hi + 1) for z in range(y, y + h + 1)}


def main():
    interval_cases = 0
    for h in range(5):
        for t in range(1, 8):
            predicted = 1 + sum(t - ell + 1 for ell in range(1, min(t, h + 1) + 1))
            assert len(interval_traces(tuple(range(t)), h)) == predicted
            for a in combinations(range(9), t):
                assert len(interval_traces(a, h)) <= predicted
                interval_cases += 1

    quotient_cases = 0
    for t in range(1, 16):
        # Distinct cosets and within-coset singleton traces are both t+1.
        # A full singleton has only t+1 traces, not their product.
        sample = tuple((i // 3, i % 3) for i in range(t))
        full = {frozenset()} | {frozenset([point]) for point in sample}
        assert len(full) == t + 1 < (t + 1) ** 2
        quotient_cases += 1

    rank_cases = 0
    for t in range(1, 15):
        a = tuple((i, i) for i in range(t))
        crosses = {frozenset(p for p in a if p[0] == x or p[1] == y)
                   for x in range(-1, t + 1) for y in range(-1, t + 1)}
        assert len(crosses) == 1 + t + t * (t - 1) // 2
        pairs = {frozenset(p for p in a if p in {(x, y), (x + 1, y)})
                 for x in range(-1, t + 1) for y in range(-1, t + 1)}
        assert len(pairs) == t + 1
        rank_cases += 1

    # All samples in the four-cube; edge counts use exact bit operations.
    adjacency = [sum(1 << (x ^ (1 << j)) for j in range(4)) for x in range(16)]
    maxima = [0] * 17
    for mask in range(1 << 16):
        t = mask.bit_count()
        edges = sum((mask & adjacency[x]).bit_count()
                    for x in range(16) if mask & (1 << x)) // 2
        # Equivalent to e <= t*log2(t)/2 without logarithmic rounding.
        assert t == 0 or (1 << (2 * edges)) <= t ** t
        maxima[t] = max(maxima[t], edges)
    for k in range(1, 5):
        assert maxima[1 << k] == k * (1 << (k - 1))
    receipt = dict(status="passed", interval_sample_checks=interval_cases,
                   quotient_controls=quotient_cases, rank_controls=rank_cases,
                   cube_samples=1 << 16, cube_maxima=maxima,
                   scope="finite controls only; five route failures do not refute Q1979")
    Path(__file__).with_name("Q1979-CHECK-RESULTS.json").write_text(
        json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k:v for k,v in receipt.items() if k != "cube_maxima"}))


if __name__ == "__main__":
    main()
