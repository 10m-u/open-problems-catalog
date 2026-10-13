#!/usr/bin/env python3
from pathlib import Path
from itertools import product
import json

HERE = Path(__file__).resolve().parent


def cubic_control(n=114, root_bound=1000):
    cubes = {i ** 3: i for i in range(-root_bound, root_bound + 1)}
    witness = None
    for x, u in cubes.items():
        for y, v in cubes.items():
            z = n - x - y
            if z in cubes:
                witness = [u, v, cubes[z]]
                break
        if witness:
            break
    # This is an exact bounded integer computation, not a decision procedure.
    return {"n": n, "root_bound": root_bound, "witness": witness,
            "cube_residues_mod9": sorted({(i ** 3) % 9 for i in range(9)}),
            "n_locally_admissible_mod9": n % 9 in {(a+b+c) % 9
                 for a,b,c in product({0,1,8},repeat=3)}}


def one_variable_curve_control():
    # R_f(2x+1) & R_g(3x-2) implies 3f(u)-2g(v)=7.
    f = lambda u: u ** 5 + u
    g = lambda v: v ** 4 + v
    pairs = []
    for u in range(-40, 41):
        for v in range(-40, 41):
            if 3 * f(u) - 2 * g(v) == 7:
                assert (f(u) - 1) % 2 == 0
                x = (f(u) - 1) // 2
                assert g(v) == 3 * x - 2
                pairs.append([u, v, x])
    return {"curve": "3(u^5+u)-2(v^4+v)=7",
            "root_box": [-40, 40], "witnesses": pairs,
            "unbounded_decision": False}


if __name__ == "__main__":
    result = {"three_cubes": cubic_control(),
              "one_variable_polynomial_images": one_variable_curve_control(),
              "predicate_vs_function_false_pair": {"index": 1, "power_value": 4,
                  "P2_value_true": True, "power_function_graph_true": False},
              "U_power_of_two_exponents": [2 ** k + k for k in range(14)]}
    (HERE / "EXPERIMENT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
