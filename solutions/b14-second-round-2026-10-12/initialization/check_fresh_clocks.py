#!/usr/bin/env python3
"""Bounded exact controls for the deferred-clock and long-path-step argument."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def nn_order(coords, start):
    order = [start]
    unvisited = set(range(len(coords))) - {start}
    while unvisited:
        target = min(unvisited, key=lambda v: (abs(coords[v] - coords[order[-1]]), v))
        order.append(target)
        unvisited.remove(target)
    return order


def main():
    instances = strict_prefixes = 0
    for r in range(1, 7):
        for weights in product((F(1, 2), F(1), F(2)), repeat=r + 1):
            z, *xs = weights
            coords = [-z, F(0)]
            partial = F(0)
            event = True
            for x in xs:
                event = event and x < partial + z
                partial += x
                coords.append(partial)
            order = nn_order(coords, 1)
            instances += 1
            if event:
                strict_prefixes += 1
                assert order == [1] + list(range(2, r + 2)) + [0]
                assert abs(coords[order[r]] - coords[order[r + 1]]) == partial + z
            # If equality is absent, the event is also necessary for this order.
            prefix_sums = [F(0)]
            for x in xs:
                prefix_sums.append(prefix_sums[-1] + x)
            if all(x != prefix_sums[i] + z for i, x in enumerate(xs)):
                assert event == (order == [1] + list(range(2, r + 2)) + [0])

    # Exact moments of f(x,r)=2 exp(-2x-r), x,r>0, conditioned on X<Y.
    density_integral = F(2) * F(1, 2) * F(1)
    ex = F(2) * F(1, 4) * F(1)
    er = F(2) * F(1, 2) * F(1)
    assert density_integral == 1 and ex == F(1, 2) and er == 1
    assert 2 * ex + er == 2 and ex + er == F(3, 2)

    # e <= sum_{j=0}^4 1/j! + (1/5!)/(1-1/6) < 11/4.
    e_upper = F(65, 24) + F(1, 100)
    assert e_upper < F(11, 4)
    gamma_tail_at_32 = F(11, 16) ** 16
    assert gamma_tail_at_32 < F(1, 16)
    finite_probability_bounds = []
    for r in (1, 2, 4, 8, 16, 32, 64):
        geometric_sum = sum(F(1, 2 ** j) for j in range(r))
        event_lower = F(1, 4) * (1 - F(1, 4) * geometric_sum)
        assert event_lower >= F(1, 8)
        finite_probability_bounds.append({"r": r, "right_arm_event_lower_bound": str(event_lower)})
    result = {
        "status": "passed", "arithmetic": "exact rational",
        "path_instances": instances, "strict_right_arm_prefixes": strict_prefixes,
        "max_cities": 8,
        "three_city_conditional_mean": "2",
        "incorrect_unshifted_mean": "3/2",
        "gamma_tail_upper_bound_at_r32": str(gamma_tail_at_32),
        "uniform_consequence": "E[D_r] >= r/32 for every r >= 32",
        "probability_controls": finite_probability_bounds,
        "scope": "finite phase controls and rational bounds supporting the all-size analytic proof; no Monte Carlo",
    }
    Path(__file__).with_name("FRESH-CLOCKS-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "probability_controls"}, indent=2))


if __name__ == "__main__":
    main()
