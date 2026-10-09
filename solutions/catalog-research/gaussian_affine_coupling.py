#!/usr/bin/env python3
"""Exact Gaussian marginal coupling on an affine subspace of nullity <= 2.

Requires SymPy. Rational input is recommended (JSON fractions may be strings).
The general criterion is an SDP; this solver handles its low-nullity cases
using exact linear equations and at most one quadratic inequality in one
variable. Feasible results include a Gaussian sampling factor.
"""

import argparse
import json

from sympy import (EmptySet, FiniteSet, Interval, Matrix, Rational, Union,
                   linsolve, oo, reduce_inequalities, simplify, sqrt, symbols)


def choose_point(feasible):
    if feasible == EmptySet:
        return None
    if isinstance(feasible, Union):
        return choose_point(feasible.args[0])
    if isinstance(feasible, FiniteSet):
        return next(iter(feasible))
    if isinstance(feasible, Interval):
        lo, hi = feasible.start, feasible.end
        if lo == -oo and hi == oo:
            return Rational(0)
        if lo == -oo:
            return hi - 1
        if hi == oo:
            return lo + 1
        return (lo + hi) / 2
    raise ValueError(f"unsupported exact feasible set: {feasible}")


def solve(A, b, means, variances):
    means = Matrix([Rational(x) for x in means])
    variances = Matrix([Rational(x) for x in variances])
    n = len(means)
    A = Matrix([[Rational(x) for x in row] for row in A]) if A else Matrix.zeros(0, n)
    b = Matrix([Rational(x) for x in b]) if b else Matrix.zeros(0, 1)
    if A.cols != n or A.rows != b.rows or len(variances) != n:
        raise ValueError("inconsistent input dimensions")
    if any(v < 0 for v in variances):
        raise ValueError("variances must be nonnegative")
    if A * means != b:
        return {"status": "infeasible", "reason": "mean constraint fails"}
    basis = A.nullspace()
    r = len(basis)
    if all(v == 0 for v in variances):
        return {"status": "feasible", "nullity": r,
                "covariance": Matrix.zeros(n), "factor": Matrix.zeros(n, 0)}
    if r == 0:
        return {"status": "infeasible", "reason": "subspace fixes all coordinates"}
    if r > 2:
        raise NotImplementedError("general criterion requires an SDP; exact solver covers nullity <= 2")
    N = Matrix.hstack(*basis)
    if r == 1:
        t = symbols("t", real=True)
        design = Matrix([N[i, 0] ** 2 for i in range(n)])
        solutions = linsolve((design, variances), (t,))
        if solutions == EmptySet:
            return {"status": "infeasible", "reason": "variance equations inconsistent"}
        value = next(iter(solutions))[0]
        if value < 0:
            return {"status": "infeasible", "reason": "negative covariance scale"}
        Q = Matrix([[value]])
        B = Matrix([[sqrt(value)]])
    else:
        u, v, w = symbols("u v w", real=True)
        design = Matrix([[N[i, 0] ** 2, 2 * N[i, 0] * N[i, 1], N[i, 1] ** 2]
                         for i in range(n)])
        solutions = linsolve((design, variances), (u, v, w))
        if solutions == EmptySet:
            return {"status": "infeasible", "reason": "variance equations inconsistent"}
        solution = next(iter(solutions))
        parameters = set().union(*(expr.free_symbols for expr in solution))
        assert len(parameters) <= 1  # N has two independent rows.
        uu, vv, ww = solution
        inequalities = [uu >= 0, ww >= 0, uu * ww - vv ** 2 >= 0]
        if parameters:
            parameter = next(iter(parameters))
            condition = reduce_inequalities(inequalities, parameter)
            point = choose_point(condition.as_set())
            if point is None:
                return {"status": "infeasible", "reason": "covariance line misses PSD cone"}
            uu, vv, ww = (simplify(expr.subs(parameter, point)) for expr in solution)
        elif not all(bool(test) for test in inequalities):
            return {"status": "infeasible", "reason": "unique covariance is not PSD"}
        Q = Matrix([[uu, vv], [vv, ww]])
        if uu == 0:
            assert vv == 0
            B = Matrix([[0, 0], [0, sqrt(ww)]])
        else:
            B = Matrix([[sqrt(uu), 0], [vv / sqrt(uu), sqrt(simplify(ww - vv ** 2 / uu))]])
    C = (N * Q * N.T).applyfunc(simplify)
    factor = (N * B).applyfunc(simplify)
    return {"status": "feasible", "nullity": r, "covariance": C, "factor": factor}


def json_result(result):
    return {key: [[str(value[i, j]) for j in range(value.cols)]
                  for i in range(value.rows)] if isinstance(value, Matrix) else value
            for key, value in result.items()}


def shared_separator_optimum(sigmas):
    """Minimum E[(X1+X2+X3)^2 + (X2+X3+X4)^2] for centred normals.

    Returns an exact factor F: X=F G, G~N(0,I_2), and the optimal value.
    Standard deviations are nonnegative rationals; singular cases are allowed.
    """
    a, b, c, d = [Rational(x) for x in sigmas]
    if min(a, b, c, d) < 0:
        raise ValueError("standard deviations must be nonnegative")
    lo, hi = abs(b - c), b + c
    centre = (a + d) / 2
    s = max(lo, min(centre, hi))
    if s == 0:
        assert b == c
        F = Matrix([[a, 0], [0, b], [0, -c], [d, 0]])
    else:
        alpha = (s ** 2 + b ** 2 - c ** 2) / (2 * s)
        height = sqrt(simplify(b ** 2 - alpha ** 2))
        F = Matrix([[a, 0], [-alpha, height], [alpha - s, -height], [d, 0]])
    value = (s - a) ** 2 + (s - d) ** 2
    return {"minimum_residual": value, "separator_standard_deviation": s,
            "factor": F, "covariance": (F * F.T).applyfunc(simplify)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON with A, b, means, variances")
    args = parser.parse_args()
    with open(args.input) as stream:
        problem = json.load(stream)
    print(json.dumps(json_result(solve(**problem)), indent=2))


if __name__ == "__main__":
    main()
