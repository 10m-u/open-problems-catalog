#!/usr/bin/env python3
"""Exact controls for the four additional one-dimensional Hartigan proof routes."""
from fractions import Fraction as F
from math import isqrt
import json
from pathlib import Path


def objective(clusters):
    return sum(sum(x * x for x in c) - sum(c) ** 2 / F(len(c)) for c in clusters)


def mean(cluster):
    return sum(cluster) / F(len(cluster))


def transfers(clusters):
    out = []
    initial = objective(clusters)
    for source, c in enumerate(clusters):
        if len(c) <= 1:
            continue
        for x in c:
            for target, d in enumerate(clusters):
                if target == source:
                    continue
                new = [a[:] for a in clusters]
                new[source].remove(x); new[target].append(x)
                direct = objective(new) - initial
                formula = F(len(d), len(d) + 1) * (x - mean(d)) ** 2
                formula -= F(len(c), len(c) - 1) * (x - mean(c)) ** 2
                assert direct == formula
                out.append((source, target, x, direct, new))
    return out


def partitions(n, k):
    def generate(prefix, maximum):
        if len(prefix) == n:
            if maximum == k - 1:
                yield prefix
        else:
            for value in range(min(maximum + 1, k - 1) + 1):
                yield from generate(prefix + [value], max(maximum, value))
    return generate([0], 0)


def main():
    legal_transfers = 0
    initial = [[F(-3), F(-2)], [F(-4), F(-1), F(0)]]
    final = [[F(-4), F(-2)], [F(-3), F(-1), F(0)]]
    ms = transfers(initial); legal_transfers += len(ms)
    assert objective(initial) == F(55, 6) and objective(final) == F(20, 3)
    first_low = next(m for m in ms if m[:3] == (0, 1, F(-3)))
    first_high = next(m for m in ms if m[:3] == (1, 0, F(-4)))
    assert first_low[3] == F(5, 6)
    assert first_high[3] == F(-20, 3)
    assert objective(final) > objective(first_high[4])
    follow = transfers(first_high[4]); legal_transfers += len(follow)
    assert all(m[3] >= 0 for m in follow)

    threshold_rows = []
    smoothing_rows = []
    for digits in range(1, 13):
        scale = 10 ** digits
        below = F(isqrt(3 * scale * scale), scale)
        assert below * below < 3
        t = (1 + below) / 2
        cs = [[F(0), F(1)], [t, t + 1]]
        gain = (3 - below * below) / 6
        ms = transfers(cs); legal_transfers += len(ms)
        improving = [m for m in ms if m[3] < 0]
        assert len(improving) == 2 and all(-m[3] == gain for m in improving)
        assert objective(cs) == 1 and 0 < gain < F(1, 12)
        for m in improving:
            follow = transfers(m[4]); legal_transfers += len(follow)
            assert all(a[3] > 0 for a in follow)
        threshold_rows.append({"digits": digits, "gain": str(gain)})

        # A separate 8-point family satisfies the source condition 4kd<=n.
        root = isqrt(15 * scale * scale)
        rminus, rplus = F(root, 3 * scale), F(root + 1, 3 * scale)
        assert rminus * rminus < F(5, 3) < rplus * rplus
        h, a = F(1, 100), F(101, 200)
        tm, tp = a * (1 + rminus), a * (1 + rplus)
        original = [[F(0), h, F(1), 1 + h], [tm, tm + h, tm + 1, tm + 1 + h]]
        perturbed = [[F(0), h, F(1), 1 + h], [tp, tp + h, tp + 1, tp + 1 + h]]
        assert len(set(sum(original, []))) == len(set(sum(perturbed, []))) == 8
        om, pm = transfers(original), transfers(perturbed)
        legal_transfers += len(om) + len(pm)
        assert len([m for m in om if m[3] < 0]) == 2
        assert all(m[3] > 0 for m in pm)
        assert tp - tm == a / (3 * scale)
        # Fixed shared affine scale puts both configurations in [0,1].
        normalization = tp + 1 + h
        normalized = [[x / normalization for x in c] for c in original]
        nm = transfers(normalized); legal_transfers += len(nm)
        assert all(F(0) <= x <= 1 for c in normalized for x in c)
        assert [m[3] < 0 for m in nm] == [m[3] < 0 for m in om]
        smoothing_rows.append({"digits": digits, "coordinate_shift": str(tp - tm),
                               "smallest_worsening_increment_after_shift": str(min(m[3] for m in pm))})

    xs = list(map(F, (0, 1, 2, 3, 6, 9)))
    candidates = []
    for labels in partitions(6, 3):
        cs = [[x for x, label in zip(xs, labels) if label == i] for i in range(3)]
        candidates.append((objective(cs), cs))
    assert len(candidates) == 90
    optimum = min(p for p, _ in candidates)
    best = [cs for p, cs in candidates if p == optimum]
    assert optimum == 5 and len(best) == 1
    target = sorted(best[0], key=mean)
    assert target == [list(map(F, (0, 1, 2, 3))), [F(6)], [F(9)]]
    target_rank = {x: i for i, c in enumerate(target) for x in c}
    def disagreement(cs):
        assert len(set(map(mean, cs))) == 3
        ordered = sorted(cs, key=mean)
        return sum(i != target_rank[x] for i, c in enumerate(ordered) for x in c)
    cs = [list(map(F, (0, 1, 2))), [F(3)], list(map(F, (6, 9)))]
    ms = transfers(cs); legal_transfers += len(ms)
    im = [m for m in ms if m[3] < 0]
    assert len(im) == 1 and im[0][:3] == (0, 1, F(2))
    assert objective(cs) == F(13, 2) and objective(im[0][4]) == F(11, 2)
    assert disagreement(cs) == 2 and disagreement(im[0][4]) == 3
    follow = transfers(im[0][4]); legal_transfers += len(follow)
    assert all(m[3] >= 0 for m in follow)

    result = {"status": "passed", "arithmetic": "exact rational",
              "legal_transfers_with_independent_cost_recomputation": legal_transfers,
              "unlabeled_global_partitions": len(candidates),
              "unique_global_objective": "5",
              "four_point_threshold_controls": threshold_rows,
              "eight_point_smoothing_controls": smoothing_rows,
              "scope": "specified route obstructions only; no Q3819 shortest-path lower bound"}
    Path(__file__).with_name("Q3819-ROUTE-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if "controls" not in k}, indent=2))


if __name__ == "__main__":
    main()
