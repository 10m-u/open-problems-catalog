#!/usr/bin/env python3
"""Independent finite exact controls for the written all-horizon argument."""

from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

from q964 import estimates_from_averages, explore, grid_plan, run_policy


def trajectory(r, b, lam, actions, start=F(1)):
    """Direct recurrence, independent of the learner and its internal grid."""
    q, states, means = start, [], []
    for i in actions:
        states.append(q)
        means.append(r[i] * q)
        q = (1 - lam) * q + lam * b[i]
    return states + [q], means


def reward(r, b, lam, actions, start=F(1)):
    return sum(trajectory(r, b, lam, actions, start)[1], F(0))


def exact_mean_estimates(r, b, lam, length, perturbation=F(0)):
    """Use exact block means, with specified signed errors on measured blocks."""
    k, q, clock = len(r), F(1), 0
    observed, mean_records, actions = [], [], []

    def average(i, measured=True):
        nonlocal q, clock
        means = []
        for _ in range(length):
            means.append(r[i] * q)
            actions.append(i)
            q = (1 - lam) * q + lam * b[i]
            clock += 1
        mean = sum(means, F(0)) / length
        if not measured:
            return mean
        sign = 1 if len(observed) % 2 else -1
        value = min(F(1), max(F(0), mean + sign * perturbation))
        observed.append(value)
        mean_records.append(mean)
        return value

    pilots = [average(i) for i in range(k)]
    j = max(range(k), key=lambda i: pilots[i])
    calibration = [average(j), average(j)]
    probes = []
    for i in range(k):
        before = average(j)
        average(i, measured=False)
        after = average(j)
        probes.append((before, after))
    result = estimates_from_averages(pilots, calibration, probes, lam, length)
    assert result["reference"] == j
    assert clock == result["observations_used"] == (4 * k + 2) * length
    assert len(observed) == 3 * k + 2
    assert all(abs(x - y) <= perturbation for x, y in zip(observed, mean_records))
    return result, tuple(actions)


def main():
    counts = {}
    state_count = 0
    for b in product([F(0), F(1, 3), F(1)], repeat=2):
        for lam in [F(1, 19), F(1, 2), F(1)]:
            for actions in product(range(2), repeat=6):
                states, _ = trajectory([F(1), F(1)], b, lam, actions)
                linear = F(1)
                for t, state in enumerate(states):
                    remainder = state - linear
                    assert 0 <= remainder <= lam**2 * t * (t - 1) / 2
                    assert 0 <= 1 - state <= lam * t
                    if t < len(actions):
                        linear += lam * (b[actions[t]] - 1)
                    state_count += 1
    counts["state_remainder_inequalities"] = state_count

    offset_count = 0
    for length in range(1, 8):
        for j in range(3):
            for i in range(3):
                probe = [j] * length + [i] * length + [j] * length
                calibration = [j] * (2 * length)
                for offset in range(length):
                    assert sorted(probe[offset:2 * length + offset]) == sorted(
                        [j] * length + [i] * length
                    )
                    assert calibration[offset:length + offset] == [j] * length
                    offset_count += 1
    counts["matched_probe_offsets"] = offset_count

    estimator_count = 0
    cases = [
        ((F(0), F(0)), (F(0), F(1))),
        ((F(1), F(0)), (F(0), F(1))),
        ((F(1, 10**6), F(0)), (F(1), F(0))),
        ((F(1, 4), F(1)), (F(1), F(0))),
        ((F(1, 2), F(1, 2)), (F(1, 3), F(2, 3))),
        ((F(1), F(1)), (F(1), F(1))),
        ((F(1), F(2, 3), F(0)), (F(0), F(1, 2), F(1))),
        ((F(1, 5), F(3, 4), F(1, 7)), (F(4, 5), F(1, 9), F(1))),
    ]
    nonvacuous_bounds = 0
    for r, b in cases:
        for lam in [F(1, 500000), F(1, 5000), F(1, 10)]:
            for length in [1, 4, 7]:
                for eta in [F(0), F(1, 10**8)]:
                    result, actions = exact_mean_estimates(r, b, lam, length, eta)
                    n = len(actions)
                    er = eta + lam * n
                    e = lam**2 * n * (n - 1) / 2
                    xi = (4 * eta + 4 * e) / (lam * length)
                    j = result["reference"]
                    assert max(abs(x - y) for x, y in zip(r, result["rhat"])) <= er
                    assert max(
                        abs(d - r[j] * (b_i - 1))
                        for d, b_i in zip(result["effects"], b)
                    ) <= xi
                    db = max(abs(x - y) for x, y in zip(b, result["bhat"]))
                    assert max(r) * db <= xi + 4 * er
                    nonvacuous_bounds += xi + 4 * er < 1
                    estimator_count += 1
    counts["estimator_scenarios"] = estimator_count
    counts["estimator_bounds_strictly_below_one"] = nonvacuous_bounds

    # Test the weighted clipping inequality on independent noisy inputs, not
    # only on estimator outputs generated from model trajectories.
    clipping_count = 0
    for actual_ref, estimate_ref, actual_b, estimated_effect in product(
        [F(0), F(1, 1000000), F(1, 3), F(1)], repeat=4
    ):
        for effect_sign in [-1, 1]:
            effect = effect_sign * estimated_effect
            br = (
                min(F(1), max(F(0), 1 + effect / estimate_ref))
                if estimate_ref else F(1)
            )
            er = abs(actual_ref - estimate_ref)
            xi = abs(effect - actual_ref * (actual_b - 1))
            assert actual_ref * abs(br - actual_b) <= xi + 2 * er
            clipping_count += 1
    counts["independent_clipping_cases"] = clipping_count

    planner_count, stability_count = 0, 0
    for r, b in cases:
        if len(r) != 2:
            continue
        for lam in [F(1, 7), F(1, 2), F(1)]:
            for horizon in range(1, 7):
                chosen, grid_value = grid_plan(r, b, lam, horizon, horizon**2)
                independent_opt = max(
                    reward(r, b, lam, a)
                    for a in product(range(2), repeat=horizon)
                )
                actual = reward(r, b, lam, chosen)
                assert grid_value <= actual <= independent_opt
                assert independent_opt - actual <= F(horizon * (horizon - 1), 2 * horizon**2)
                # Independent check of the state-initialization estimate used
                # for the full-horizon comparator, including zero rewards.
                for start in [F(0), F(1, 3), F(9, 10)]:
                    difference = actual - reward(r, b, lam, chosen, start)
                    assert 0 <= difference <= horizon * max(r) * (1 - start)
                    stability_count += 1
                planner_count += 1
    counts["planners_against_exhaustive_optima"] = planner_count
    counts["tail_initial_state_comparisons"] = stability_count

    # Verify the actual callback interface and schedule without giving the
    # learner any state, including a completely zero observed reward stream.
    seen = []
    result = explore(3, 2, F(1, 100), lambda i: seen.append(i) or 0)
    expected = [i for i in range(3) for _ in range(2)] + [0] * 4
    for i in range(3):
        expected += [0] * 2 + [i] * 2 + [0] * 2
    assert seen == expected
    assert result["bhat"] == (F(1),) * 3
    assert result["rhat"] == (F(0),) * 3
    seen = []
    actions, estimates = run_policy(2, 8, F(1), lambda i: seen.append(i) or 0)
    assert actions == tuple(seen) == (0,) * 8 and estimates is None
    counts["callback_schedule_and_fallback_checks"] = 2

    certificate = {
        "problem": 964,
        "date": "2026-10-09",
        "all_passed": True,
        "arithmetic": "Python standard-library Fraction; exact integer/rational comparisons",
        "counts": counts,
        "evidence_limit": "Finite controls supplement the written uniform proof; no Monte Carlo rate certification or formal proof is claimed.",
    }
    target = Path(__file__).with_name("q964-checks.json")
    target.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))


if __name__ == "__main__":
    main()
