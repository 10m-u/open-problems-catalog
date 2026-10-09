#!/usr/bin/env python3
"""Exact primal/dual and independent Gaussian polygon controls."""

from itertools import product
import json
from pathlib import Path
import random

from sympy import Matrix, simplify

from gaussian_affine_coupling import json_result, shared_separator_optimum, solve


def validate(A, variances, result):
    assert result["status"] == "feasible"
    C, F = result["covariance"], result["factor"]
    n = len(variances)
    A = Matrix(A) if A else Matrix.zeros(0, n)
    assert C == C.T
    assert [C[i, i] for i in range(n)] == list(variances)
    assert A * C == Matrix.zeros(A.rows, n)
    assert A * F == Matrix.zeros(A.rows, F.cols)
    assert (F * F.T - C).applyfunc(simplify) == Matrix.zeros(n)


def main():
    # Independently known feasibility: weighted normal joint mixability is
    # equivalent to the closed-polygon inequality for |a_i| sigma_i.
    polygon_checks = 0
    for coefficients, levels in [([1, 1, 1], range(5)), ([-2, 1, 3], range(4))]:
        for sigmas in product(levels, repeat=3):
            lengths = [abs(a) * s for a, s in zip(coefficients, sigmas)]
            expected = 2 * max(lengths) <= sum(lengths)
            variances = [s * s for s in sigmas]
            result = solve([coefficients], [0], [0] * 3, variances)
            assert (result["status"] == "feasible") == expected
            if expected:
                validate([coefficients], variances, result)
            polygon_checks += 1

    rng = random.Random(20260930)
    generated_checks = 0
    for n in range(2, 9):
        for r in (1, 2):
            for _ in range(12):
                while True:
                    known_factor = Matrix(n, r, [rng.randint(-3, 3) for _ in range(n * r)])
                    if known_factor.rank() == r:
                        break
                annihilators = known_factor.T.nullspace()
                A = Matrix.vstack(*(v.T for v in annihilators)) if annihilators else Matrix.zeros(0, n)
                means = Matrix([rng.randint(-3, 3) for _ in range(n)])
                variances = [sum(known_factor[i, j] ** 2 for j in range(r)) for i in range(n)]
                result = solve(A.tolist(), list(A * means), list(means), variances)
                validate(A.tolist(), variances, result)
                generated_checks += 1

    A = Matrix([[1, 1, 1, 0], [0, 1, 1, 1]])
    variances = Matrix([1, 4, 4, 4])
    result = solve(A.tolist(), [0, 0], [0] * 4, list(variances))
    assert result["status"] == "infeasible"
    # Each constraint alone has an explicit Gaussian factor.
    # Use exact algebraic rows with squared norms 1,4,4 and sum zero.
    from sympy import Rational, sqrt
    first = Matrix([[-1, 0], [Rational(1, 2), sqrt(15) / 2],
                    [Rational(1, 2), -sqrt(15) / 2]])
    second = Matrix([[2, 0], [-1, sqrt(3)], [-1, -sqrt(3)]])
    for F, diagonal in [(first, [1, 4, 4]), (second, [4, 4, 4])]:
        assert (Matrix([[1, 1, 1]]) * F).applyfunc(simplify) == Matrix.zeros(1, 2)
        assert list((F * F.T).diagonal()) == diagonal
    y = Matrix([1, 0, 0, -1])
    N = Matrix.hstack(*A.nullspace())
    assert N.T * Matrix.diag(*y) * N == Matrix.zeros(2)
    assert (y.T * variances)[0] == -3

    protected_mean = solve([[1, 1]], [1], [0, 0], [1, 1])
    assert protected_mean["status"] == "infeasible"
    fixed = solve([[1, 0], [0, 1]], [2, 3], [2, 3], [0, 0])
    validate([[1, 0], [0, 1]], [0, 0], fixed)
    assert solve([[1, 0], [0, 1]], [2, 3], [2, 3], [0, 1])["status"] == "infeasible"

    # Rank-two variance equations can leave one free covariance parameter.
    unconstrained = solve([], [], [0, 0], [2, 3])
    validate([], [2, 3], unconstrained)
    boundary = solve([[1, 1, 1]], [0], [0, 0, 0], [1, 1, 4])
    validate([[1, 1, 1]], [1, 1, 4], boundary)
    assert boundary["covariance"].rank() == 1

    residual_checks = 0
    for sigmas in product(range(5), repeat=4):
        optimum = shared_separator_optimum(sigmas)
        F, C = optimum["factor"], optimum["covariance"]
        assert list(C.diagonal()) == [s * s for s in sigmas]
        residual_factor = A * F
        attained = simplify(sum(entry ** 2 for entry in residual_factor))
        assert attained == optimum["minimum_residual"]
        # Verify the independently stated L2 bound and projection condition.
        a, b, c, d = sigmas
        s = optimum["separator_standard_deviation"]
        lo, hi = abs(b - c), b + c
        assert lo <= s <= hi
        derivative = 4 * s - 2 * (a + d)
        assert derivative == 0 or (s == lo and derivative >= 0) or (s == hi and derivative <= 0)
        exact = solve(A.tolist(), [0, 0], [0] * 4, [q * q for q in sigmas])
        assert (exact["status"] == "feasible") == (attained == 0)
        residual_checks += 1
    obstruction_optimum = shared_separator_optimum([1, 2, 2, 2])
    assert obstruction_optimum["minimum_residual"] == Rational(1, 2)

    report = {
        "date": "2026-09-30", "status": "all assertions passed",
        "independent_weighted_polygon_cases": polygon_checks,
        "generated_exact_primal_cases": generated_checks,
        "shared_separator_residual_cases": residual_checks,
        "seed": 20260930,
        "shared_separator_obstruction": {
            "A": A.tolist(), "variances": list(variances),
            "separate_constraints_feasible": True, "joint_constraints_feasible": False,
            "dual_y": list(y), "restricted_dual_form": [[0, 0], [0, 0]],
            "dual_dot_variances": -3,
            "optimal_residual": str(obstruction_optimum["minimum_residual"]),
            "optimal_factor": json_result(obstruction_optimum)["factor"],
        },
        "boundary_example": json_result(boundary),
        "limits": "Exact certificate audits, not sampling estimates or general SDP implementation.",
    }
    path = Path(__file__).with_name("gaussian-affine-checks.json")
    path.write_text(json.dumps(report, indent=2, default=int) + "\n")
    print(json.dumps(report, indent=2, default=int))


if __name__ == "__main__":
    main()
