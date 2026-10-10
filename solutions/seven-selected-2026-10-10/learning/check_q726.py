#!/usr/bin/env python3
"""Exact finite controls for Q726; Python standard library only.

The proof covers all admissible histories and action spaces. This checker
independently solves finite max-min games, and compares kernel and feature
posterior formulas, using rational arithmetic throughout.
"""

from fractions import Fraction as F
from itertools import product
import argparse
import json
from pathlib import Path


def probabilities(scores):
    """If g_i=log(scores_i), sigmoid(g_i-g_j) is exactly rational."""
    return [[F(a, a + b) for b in scores] for a in scores]


def solve_all_pairs(predicted, distance, beta):
    n = len(predicted)
    lcb = [[predicted[i][j] - beta * distance[i][j]
            for j in range(n)] for i in range(n)]
    values = [min(row) for row in lcb]
    optimum = max(values)
    return [(i, j, optimum) for i in range(n) if values[i] == optimum
            for j in range(n) if lcb[i][j] == optimum]


def finite_games():
    scenarios = pairs = zero_width = ties = 0
    largest_fraction_of_bound = F(0)
    position_sets = [tuple(map(F, [-1, 0, 1])),
                     (F(0), F(1, 4), F(1)),
                     tuple(map(F, [0, 0, 1]))]
    score_sets = list(product([1, 2, 4], repeat=3))
    for positions in position_sets:
        distance = [[abs(a - b) for b in positions] for a in positions]
        for estimated_scores in score_sets:
            # Equal feature points must have equal utilities.
            if any(positions[i] == positions[j]
                   and estimated_scores[i] != estimated_scores[j]
                   for i in range(3) for j in range(3)):
                continue
            predicted = probabilities(estimated_scores)
            low, high = min(estimated_scores), max(estimated_scores)
            slope = F(low * high, (low + high)**2)
            constant = 1 + 1 / (4 * slope)
            assert constant >= 2
            for true_scores in score_sets:
                if any(positions[i] == positions[j]
                       and true_scores[i] != true_scores[j]
                       for i in range(3) for j in range(3)):
                    continue
                true = probabilities(true_scores)
                beta_min = max(
                    [abs(predicted[i][j] - true[i][j]) / distance[i][j]
                     for i in range(3) for j in range(3) if distance[i][j]]
                    + [F(0)])
                best = max(range(3), key=true_scores.__getitem__)
                for beta in [beta_min, beta_min + F(1, 12), beta_min + F(1, 3)]:
                    assert all(abs(predicted[i][j] - true[i][j])
                               <= beta * distance[i][j]
                               for i in range(3) for j in range(3))
                    solutions = solve_all_pairs(predicted, distance, beta)
                    scenarios += 1
                    ties += len(solutions) > 1
                    for leader, follower, value in solutions:
                        width = beta * distance[leader][follower]
                        deficit = F(1, 2) - value
                        first = true[best][leader] - F(1, 2)
                        second = true[best][follower] - F(1, 2)
                        regret = (first + second) / 2
                        assert 0 <= deficit <= constant * width
                        assert 0 <= first <= deficit
                        assert 0 <= second <= max(deficit, 2 * width)
                        assert regret <= constant * width
                        if width:
                            largest_fraction_of_bound = max(
                                largest_fraction_of_bound, regret / (constant * width))
                        else:
                            assert regret == 0
                            zero_width += 1
                        pairs += 1

    # Every assumption except the triangle inequality holds in this control.
    # The unique leader is 0, its unique follower is 1, and their width is zero
    # despite positive regret. Thus symmetry and a zero diagonal are insufficient.
    scores = [1, 2, 1]
    probability = probabilities(scores)
    invalid_distance = [[F(0), F(0), F(0)],
                        [F(0), F(0), F(1)],
                        [F(0), F(1), F(0)]]
    bad_solutions = solve_all_pairs(probability, invalid_distance, F(1))
    assert bad_solutions == [(0, 1, F(1, 3))]
    bad_regret = (probability[1][0] + probability[1][1] - 1) / 2
    assert bad_regret == F(1, 12) > 0
    assert invalid_distance[1][2] > invalid_distance[1][0] + invalid_distance[0][2]
    return {
        "scenarios": scenarios,
        "all_optimizing_pairs_checked": pairs,
        "scenarios_with_ties": ties,
        "zero_width_pairs": zero_width,
        "largest_regret_divided_by_proved_bound": str(largest_fraction_of_bound),
        "nonmetric_negative_control": {
            "detected": True,
            "leader": 0, "follower": 1, "width": "0", "regret": str(bad_regret),
        },
        "all_passed": True,
    }


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def matvec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def inverse(matrix):
    n = len(matrix)
    augmented = [list(row) + ident for row, ident in zip(matrix, identity(n))]
    for col in range(n):
        pivot = next(row for row in range(col, n) if augmented[row][col])
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        scale = augmented[col][col]
        augmented[col] = [x / scale for x in augmented[col]]
        for row in range(n):
            if row != col:
                scale = augmented[row][col]
                augmented[row] = [x - scale * y for x, y in
                                  zip(augmented[row], augmented[col])]
    return [row[n:] for row in augmented]


def determinant(matrix):
    matrix = [list(row) for row in matrix]
    result = F(1)
    for col in range(len(matrix)):
        pivot = next((row for row in range(col, len(matrix)) if matrix[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            result = -result
        scale = matrix[col][col]
        result *= scale
        for row in range(col + 1, len(matrix)):
            ratio = matrix[row][col] / scale
            for j in range(col + 1, len(matrix)):
                matrix[row][j] -= ratio * matrix[col][j]
    return result


def kernel_controls():
    # Rational features of norm <=1, including a duplicate and a zero point.
    features = [(F(1), F(0)), (F(0), F(1)),
                (F(3, 5), F(4, 5)), (F(0), F(0)), (F(1), F(0))]
    history = [(0, 1), (1, 2), (0, 4), (3, 2), (4, 1), (2, 0), (1, 3)]
    a0 = F(3, 2)
    past = []
    sequential_product = F(1)
    pairs = triangles = determinants = 0
    for current in history + [None]:
        dimension = len(features[0])
        v = [[a0 * F(i == j) + sum((z[i] * z[j] for z in past), F(0))
              for j in range(dimension)] for i in range(dimension)]
        vinv = inverse(v)
        gram = [[dot(a, b) for b in past] for a in past]
        regularized = [[gram[i][j] + a0 * F(i == j) for j in range(len(past))]
                       for i in range(len(past))]
        gram_inverse = inverse(regularized)
        squared = [[F(0) for _ in features] for _ in features]
        for i, a in enumerate(features):
            for j, b in enumerate(features):
                psi = [x - y for x, y in zip(a, b)]
                feature_variance = a0 * dot(psi, matvec(vinv, psi))
                covariances = [dot(z, psi) for z in past]
                kernel_variance = dot(psi, psi) - dot(
                    covariances, matvec(gram_inverse, covariances))
                assert feature_variance == kernel_variance
                assert 0 <= feature_variance <= 4
                squared[i][j] = feature_variance
                pairs += 1
        for i, j, k in product(range(len(features)), repeat=3):
            # Exact test of sqrt(a) <= sqrt(b)+sqrt(c), without square roots.
            difference = squared[i][j] - squared[i][k] - squared[k][j]
            assert difference <= 0 or difference**2 <= 4 * squared[i][k] * squared[k][j]
            triangles += 1
        det = determinant([[F(i == j) + gram[i][j] / a0 for j in range(len(past))]
                           for i in range(len(past))])
        assert det == sequential_product
        determinants += 1
        if current is not None:
            i, j = current
            sequential_product *= 1 + squared[i][j] / a0
            past.append([a - b for a, b in zip(features[i], features[j])])
    return {
        "posterior_feature_vs_kernel_pairs": pairs,
        "squared_triangle_inequalities": triangles,
        "sequential_determinant_identities": determinants,
        "final_determinant": str(sequential_product),
        "all_passed": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"problem_number": 726, "arithmetic": "exact fractions.Fraction",
              "finite_games": finite_games(), "posterior_controls": kernel_controls(),
              "evidence_limit": "Finite controls accompany, and do not replace, the written proof."}
    output = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"All Q726 checks passed; wrote {args.output}")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
