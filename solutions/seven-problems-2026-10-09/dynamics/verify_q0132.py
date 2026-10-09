#!/usr/bin/env python3
"""Exact finite controls for Q132. Infinite convergence is proved in Q0132.md."""

from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
import random


def compositions(total, length):
    if length == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, length - 1):
                yield (first,) + rest


def tv(left, right):
    return sum((abs(x - y) for x, y in zip(left, right)), F(0)) / 2


def best_response(weights, external, budget):
    """Solve the scalar water-level equation by sorted breakpoints."""
    active = sorted(
        (external[x] / weights[x], x)
        for x in range(len(weights))
        if weights[x]
    )
    sum_weight = F(0)
    sum_external = F(0)
    for position, (_, x) in enumerate(active):
        sum_weight += weights[x]
        sum_external += external[x]
        level = (budget + sum_external) / sum_weight
        if position + 1 == len(active) or level <= active[position + 1][0]:
            answer = tuple(
                max(F(0), level * w - b) if w else F(0)
                for w, b in zip(weights, external)
            )
            assert sum(answer) == budget
            return answer
    raise AssertionError("Every donor must have a nonempty support")


def active_set_response(weights, external, budget):
    """Independent control: enumerate feasible active sets and KKT equalities."""
    support = tuple(x for x, w in enumerate(weights) if w)
    answers = set()
    for size in range(1, len(support) + 1):
        for active_tuple in combinations(support, size):
            active = set(active_tuple)
            level = (
                budget + sum((external[x] for x in active), F(0))
            ) / sum((weights[x] for x in active), F(0))
            row = tuple(
                level * weights[x] - external[x] if x in active else F(0)
                for x in range(len(weights))
            )
            if any(z < 0 for z in row):
                continue
            if any(
                external[x] < level * weights[x]
                for x in support
                if x not in active
            ):
                continue
            assert sum(row) == budget
            answers.add(row)
    assert len(answers) == 1
    return answers.pop()


def aggregate(rows):
    return tuple(map(sum, zip(*rows)))


def external_to(rows, donor):
    total = aggregate(rows)
    return tuple(s - x for s, x in zip(total, rows[donor]))


def residuals(rows, weights, budgets):
    return tuple(
        tv(row, best_response(weights[i], external_to(rows, i), budgets[i]))
        for i, row in enumerate(rows)
    )


def update(rows, weights, budgets, donor):
    answer = list(rows)
    answer[donor] = best_response(
        weights[donor], external_to(rows, donor), budgets[donor]
    )
    return tuple(answer)


def weighted_gini(total, weights):
    return sum(
        (
            abs(weights[y] * total[x] - weights[x] * total[y])
            for x, y in combinations(range(len(total)), 2)
        ),
        F(0),
    )


def random_row(rng, budget, support, dimensions):
    parts = [0] * dimensions
    for _ in range(budget):
        parts[rng.choice(support)] += 1
    return tuple(map(F, parts))


def main():
    counts = {
        "best_response_active_set_comparisons": 0,
        "nonexpansiveness_comparisons": 0,
        "residual_step_comparisons": 0,
        "complete_interval_mass_bounds": 0,
        "weighted_transfer_bounds": 0,
        "weighted_best_response_bounds": 0,
        "weighted_cumulative_variation_bounds": 0,
    }
    for dimensions in (2, 3):
        inputs = [
            tuple(map(F, b)) for b in compositions(3, dimensions)
        ]
        for raw_weights in product(range(4), repeat=dimensions):
            if not any(raw_weights):
                continue
            weights = tuple(map(F, raw_weights))
            for budget in map(F, (1, 2)):
                responses = []
                for external in inputs:
                    answer = best_response(weights, external, budget)
                    assert answer == active_set_response(weights, external, budget)
                    responses.append(answer)
                    counts["best_response_active_set_comparisons"] += 1
                for a, b in product(range(len(inputs)), repeat=2):
                    assert tv(responses[a], responses[b]) <= tv(inputs[a], inputs[b])
                    counts["nonexpansiveness_comparisons"] += 1

    rng = random.Random(132)
    for _ in range(240):
        dimensions = rng.randrange(2, 5)
        donors = rng.randrange(2, 5)
        weights = []
        budgets = []
        rows = []
        for _ in range(donors):
            raw = [rng.randrange(4) for _ in range(dimensions)]
            raw[rng.randrange(dimensions)] = rng.randrange(1, 4)
            support = [x for x, w in enumerate(raw) if w]
            budget = rng.randrange(1, 4)
            weights.append(tuple(map(F, raw)))
            budgets.append(F(budget))
            rows.append(random_row(rng, budget, support, dimensions))
        rows = tuple(rows)
        for _ in range(4):
            start_residual = max(residuals(rows, weights, budgets))
            moved = F(0)
            order = list(range(donors))
            rng.shuffle(order)
            for donor in order:
                before = residuals(rows, weights, budgets)
                after_rows = update(rows, weights, budgets, donor)
                after = residuals(after_rows, weights, budgets)
                movement = tv(aggregate(rows), aggregate(after_rows))
                assert before[donor] == movement
                assert after[donor] == 0
                for old, new in zip(before, after):
                    assert abs(new - old) <= movement
                    counts["residual_step_comparisons"] += 1
                moved += movement
                rows = after_rows
            assert moved >= start_residual
            counts["complete_interval_mass_bounds"] += 1

    weight_choices = (F(1, 2), F(1), F(3, 2))
    for weights in product(weight_choices, repeat=3):
        for raw_total in product(range(4), repeat=3):
            total = tuple(map(F, raw_total))
            for x, y in product(range(3), repeat=2):
                if x == y:
                    continue
                gap = total[x] / weights[x] - total[y] / weights[y]
                if gap <= 0:
                    continue
                endpoint = gap / (1 / weights[x] + 1 / weights[y])
                for fraction in (F(1, 2), F(1)):
                    transfer = fraction * endpoint
                    changed = list(total)
                    changed[x] -= transfer
                    changed[y] += transfer
                    assert changed[x] >= 0
                    assert changed[x] / weights[x] >= changed[y] / weights[y]
                    decrease = weighted_gini(total, weights) - weighted_gini(
                        changed, weights
                    )
                    assert decrease >= (weights[x] + weights[y]) * transfer
                    counts["weighted_transfer_bounds"] += 1

    for _ in range(80):
        dimensions = rng.randrange(2, 5)
        donors = rng.randrange(2, 5)
        project_weights = tuple(F(rng.randrange(1, 5), 2) for _ in range(dimensions))
        weights, budgets, rows = [], [], []
        for donor in range(donors):
            support = [x for x in range(dimensions) if rng.randrange(2)]
            if not support:
                support = [rng.randrange(dimensions)]
            factor = F(rng.randrange(1, 5))
            weights.append(
                tuple(factor * w if x in support else F(0)
                      for x, w in enumerate(project_weights))
            )
            budget = rng.randrange(1, 4)
            budgets.append(F(budget))
            rows.append(random_row(rng, budget, support, dimensions))
        rows = tuple(rows)
        initial = weighted_gini(aggregate(rows), project_weights)
        moved = F(0)
        # Increasing finite complete intervals; no finite run proves fairness.
        for epoch in range(1, 7):
            order = [j for _ in range(epoch) for j in range(donors - 1)]
            order.append(donors - 1)
            for donor in order:
                new_rows = update(rows, weights, budgets, donor)
                movement = tv(aggregate(rows), aggregate(new_rows))
                decrease = (
                    weighted_gini(aggregate(rows), project_weights)
                    - weighted_gini(aggregate(new_rows), project_weights)
                )
                assert decrease >= 2 * min(project_weights) * movement
                counts["weighted_best_response_bounds"] += 1
                moved += movement
                rows = new_rows
                assert moved <= initial / (2 * min(project_weights))
                counts["weighted_cumulative_variation_bounds"] += 1

    certificate = {
        "problem": 132,
        "arithmetic": "exact rational (fractions.Fraction)",
        "passed": True,
        "counts": counts,
        "scope": (
            "Finite controls for best-response formulas, total-variation "
            "nonexpansiveness, residual bounds, and weighted potential inequalities. "
            "Infinite convergence is established analytically in Q0132.md."
        ),
    }
    destination = Path(__file__).with_name("q0132-checks.json")
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps(certificate, indent=2))


if __name__ == "__main__":
    main()
