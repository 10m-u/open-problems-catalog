#!/usr/bin/env python3
"""Checks for the proposed proofs of catalog questions 3982 and 3983.

Default: exact rational arithmetic, Python standard library only.
--numeric: also compare the transform with an independent Gaussian product
and invert its contour integral. Requires NumPy and SciPy. Those numerical
diagnostics are not proof certificates or certified interval computations.
"""

from __future__ import annotations

import argparse
import cmath
from fractions import Fraction as F
import json
import math
from pathlib import Path


def multiply(left, right, order=4):
    return [sum(left[j] * right[k - j] for j in range(k + 1))
            for k in range(order + 1)]


def inverse(series, order=4):
    answer = [1 / series[0]] + [F(0)] * order
    for k in range(1, order + 1):
        answer[k] = -sum(series[j] * answer[k - j]
                         for j in range(1, k + 1)) / series[0]
    return answer


def square_root_about_saddle(lam, order=4):
    """Exact coefficients of sqrt(lam**2 + 2*delta), through order 4."""
    answer = [lam] + [F(0)] * order
    for k in range(1, order + 1):
        target = F(2) if k == 1 else F(0)
        answer[k] = (target - sum(answer[j] * answer[k - j]
                                  for j in range(1, k))) / (2 * lam)
    assert multiply(answer, answer) == [lam**2, F(2), F(0), F(0), F(0)]
    return answer


def exact_checks():
    """Coefficient identities and rational parametrizations of the contour."""
    saddle_cases = 0
    contour_cases = 0
    generator_cases = 0
    for theta in [F(1, 3), F(1, 2), F(1), F(3, 2), F(2)]:
        for factor in [F(1), F(5, 4), F(3, 2), F(2), F(3)]:
            lam = factor / (2 * theta)
            r = 2 * theta * lam**3 - lam**2
            assert r >= 0
            assert theta == 1 / (2 * lam) + r / (2 * lam**3)
            root = square_root_about_saddle(lam)
            invroot = inverse(root)
            h = [-root[k] / 2 + r * invroot[k] / 2 for k in range(5)]
            h[0] += theta * lam**2 / 2
            h[1] += theta
            assert h[1] == 0
            curvature = 1 / (2 * lam**3) + 3 * r / (2 * lam**5)
            assert curvature > 0
            assert 2 * h[2] == curvature
            assert 6 * h[3] == -3 / (2 * lam**5) - 15 * r / (2 * lam**7)
            assert 24 * h[4] == 15 / (2 * lam**7) + 105 * r / (2 * lam**9)
            if r == 0:
                assert h[0] == -1 / (8 * theta)
                assert curvature == 4 * theta**3
            saddle_cases += 1

            for parameter in [F(0), F(1, 10), F(1, 3), F(1, 2), F(3, 4), F(9, 10)]:
                # Rational parametrization of alpha**2-beta**2=lam**2.
                alpha = lam * (1 + parameter**2) / (1 - parameter**2)
                beta = 2 * lam * parameter / (1 - parameter**2)
                imaginary_s = alpha * beta
                assert alpha**2 - beta**2 == lam**2
                assert alpha >= lam
                real_inverse = alpha / (alpha**2 + beta**2)
                assert real_inverse <= 1 / lam
                real_h_difference = -(alpha - lam) / 2 + r / 2 * (real_inverse - 1 / lam)
                assert real_h_difference <= -(alpha - lam) / 2
                # Check the rationalization used for the small-frequency bound.
                assert alpha - lam == 2 * imaginary_s**2 / (
                    (alpha + lam) * (alpha**2 + beta**2 + lam**2))
                contour_cases += 1

            for x in [F(-3), F(-1, 2), F(0), F(2, 3), F(4)]:
                # h''(x)/h(x)=lam**2*x**2-lam for h=exp(-lam*x**2/2).
                killed_generator_ratio = (lam**2 * x**2 - lam) / 2 - lam**2 * x**2 / 2
                assert killed_generator_ratio == -lam / 2
                generator_cases += 1

    return {
        "arithmetic": "fractions.Fraction, exact",
        "saddle_series_cases": saddle_cases,
        "whole_contour_identity_cases": contour_cases,
        "killed_generator_identity_cases": generator_cases,
        "all_passed": True,
    }


def saddle(theta, r):
    low = 1 / (2 * theta)
    high = max(1.0, 2 * low)
    while 2 * theta * high**3 - high**2 - r < 0:
        high *= 2
    for _ in range(100):
        mid = (low + high) / 2
        if 2 * theta * mid**3 - mid**2 - r < 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def log_mehler(length, start, tilt, s):
    """Stable evaluation of the exact endpoint-tilted transform (6)."""
    g = cmath.sqrt(2 * s)
    q = cmath.exp(-2 * g * length)
    tanh = (1 - q) / (1 + q)
    sech = 2 * cmath.exp(-g * length) / (1 + q)
    return (-g * length / 2 + math.log(2) / 2 - cmath.log(1 + q) / 2
            - g * start**2 * tanh / 2 + tilt * start * sech
            + tilt**2 * tanh / (2 * g))


def numerical_checks():
    import numpy as np
    import scipy
    from scipy.integrate import quad

    product_checks = []
    for length, start, tilt, s in [
        (1.3, 0.2, 0.7, 0.8 + 0.35j),
        (0.8, -0.7, -1.1, 0.4 + 0.9j),
        (1.0, 0.5, -0.9, 1.2 + 0j),
    ]:
        exact_log = log_mehler(length, start, tilt, s)
        errors = []
        for modes in [4000, 8000]:
            k = np.arange(1, modes + 1)
            frequencies = (k - 0.5) * math.pi
            eigenvalues = length**2 / frequencies**2
            endpoint = np.sqrt(2 * length) * (-1.0)**(k + 1) / frequencies
            integral_coefficients = np.sqrt(2.0) * length**1.5 / frequencies**2
            linear = tilt * endpoint - 2 * s * start * integral_coefficients
            denominators = 1 + 2 * s * eigenvalues
            product_log = (-s * start**2 * length + tilt * start
                           - 0.5 * np.log(denominators).sum()
                           + (linear**2 / (2 * denominators)).sum())
            errors.append(abs(cmath.exp(product_log - exact_log) - 1))
        assert errors[1] < errors[0]
        assert errors[1] < 1e-4
        product_checks.append({
            "length": length, "start": start, "tilt": tilt,
            "s": [s.real, s.imag], "modes": [4000, 8000],
            "relative_errors": errors,
        })

    def scaled_inversion(T, theta, tilt, time, spent, start):
        """Invert exact Mehler transform; remove its common saddle exponent."""
        r = tilt**2 / T
        lam = saddle(theta, r)
        s0 = lam**2 / 2
        curvature = 1 / (2 * lam**3) + 3 * r / (2 * lam**5)
        phase = theta * s0 - lam / 2 + r / (2 * lam)
        scale = math.sqrt(T * curvature)

        def integrand(z):
            s = s0 + 1j * z / scale
            exponent = ((theta * T - spent) * s
                        + log_mehler(T - time, start, tilt, s) - T * phase)
            return (cmath.exp(exponent) / s).real / (math.pi * scale)

        value, estimated_error = quad(integrand, 0, np.inf,
                                      epsabs=2e-11, epsrel=2e-11, limit=400)
        assert value > 0
        return value, estimated_error

    time, spent, end, initial, theta = 0.75, 0.4, -0.35, 0.2, 1.0
    ratio_checks = []
    for regime in ["zero", "subcritical_T_to_3_over_8", "critical_plus", "critical_minus"]:
        results = []
        for T in [32, 128, 512]:
            tilt = {"zero": 0.0, "subcritical_T_to_3_over_8": T**(3 / 8),
                    "critical_plus": math.sqrt(T), "critical_minus": -math.sqrt(T)}[regime]
            lam = saddle(theta, tilt**2 / T)
            limit_lam = 0.5 if regime in ["zero", "subcritical_T_to_3_over_8"] else 1.0
            numerator, num_error = scaled_inversion(T, theta, tilt, time, spent, end)
            denominator, den_error = scaled_inversion(T, theta, tilt, 0, 0, initial)
            ratio = numerator / denominator
            prediction = math.exp(time * lam / 2 - spent * lam**2 / 2
                                  - lam * (end**2 - initial**2) / 2)
            limit = math.exp(time * limit_lam / 2 - spent * limit_lam**2 / 2
                             - limit_lam * (end**2 - initial**2) / 2)
            relative_error = abs(ratio / prediction - 1)
            assert relative_error < 0.03
            results.append({
                "T": T, "tilt": tilt, "lambda_T": lam,
                "exact_transform_density_ratio": ratio,
                "moving_saddle_prediction": prediction,
                "relative_error_to_moving_saddle": relative_error,
                "limiting_density_ratio": limit,
                "relative_error_to_limit": abs(ratio / limit - 1),
                "quadrature_estimated_absolute_errors": [num_error, den_error],
            })
        assert results[-1]["relative_error_to_moving_saddle"] < results[0]["relative_error_to_moving_saddle"]
        ratio_checks.append({"regime": regime, "checks": results})

    return {
        "arithmetic": "floating point; diagnostic, not certified interval bounds",
        "numpy_version": np.__version__, "scipy_version": scipy.__version__,
        "independent_Karhunen_Loeve_product_checks": product_checks,
        "exact_transform_contour_ratio_checks": ratio_checks,
        "all_passed": True,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--numeric", action="store_true")
    parser.add_argument("--output", type=Path, help="Write the full JSON result to this file.")
    args = parser.parse_args()
    result = {"problem_numbers": [3982, 3983], "exact_checks": exact_checks()}
    if args.numeric:
        result["numerical_checks"] = numerical_checks()
    serialized = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
        print(f"All checks passed; wrote {args.output}")
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
