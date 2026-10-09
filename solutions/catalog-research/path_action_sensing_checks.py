#!/usr/bin/env python3
"""Independent finite audits of the cyclic-partition interval-sensing theorem.

Compare the solver against every interval menu up to an independently checked
full-recovery bound, and every cyclic cut set. Use only the standard library.
"""
import argparse
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path
from random import Random

from path_action_sensing import optimal_design, solve


def intersection(values):
    answer = values[0]
    for value in values[1:]:
        answer &= value
    return answer


@lru_cache(None)
def menu_catalogue(physical_count, include_empty):
    size = physical_count + include_empty
    intervals = [sum(1 << v for v in range(left, right + 1))
                 for left in range(physical_count)
                 for right in range(left, physical_count)]
    # Earlier one-defect full-recovery bounds give this finite ceiling. The
    # singleton partition is independently required to occur below that bound.
    cap = (size + 1) // 2
    best = {}
    menus = 0
    for count in range(cap + 1):
        for chosen in combinations(intervals, count):
            cells = {}
            for vertex in range(size):
                code = sum(((row >> vertex) & 1) << j for j, row in enumerate(chosen))
                cells.setdefault(code, []).append(vertex)
            partition = tuple(sorted(tuple(cell) for cell in cells.values()))
            if partition not in best:
                best[partition] = count
            menus += 1
    assert tuple((v,) for v in range(size)) in best
    return sorted(best.items(), key=lambda item: item[1]), menus


def menu_optimum(masks, catalogue):
    for partition, count in catalogue:
        if all(intersection([masks[v] for v in cell]) for cell in partition):
            return count
    raise AssertionError("Full-recovery menu must permit an acceptable action")


def cyclic_optimum_by_cuts(masks):
    size = len(masks)
    if intersection(masks):
        return 1
    best = size
    # A cut at i is the boundary after state i in the cyclic order.
    for cut_mask in range(1, 1 << size):
        count = cut_mask.bit_count()
        if count >= best:
            continue
        cuts = [i for i in range(size) if cut_mask >> i & 1]
        valid = True
        for left, right in zip(cuts, cuts[1:] + cuts[:1]):
            length = (right - left) % size or size
            block = [masks[(left + step) % size] for step in range(1, length + 1)]
            if not intersection(block):
                valid = False
                break
        if valid:
            best = count
    return best


def check_instance(masks, physical_count, include_empty, catalogue):
    assert len(masks) == physical_count + int(include_empty)
    result = optimal_design(masks, physical_count)
    actual = menu_optimum(masks, catalogue)
    cyclic = cyclic_optimum_by_cuts(masks)
    assert result["cyclic_block_count"] == cyclic
    assert result["minimum_tests"] == actual
    assert actual == (0 if cyclic == 1 else (cyclic + 1) // 2)
    # Independently recompute every observation fibre, including the empty
    # state, instead of trusting the solver's stored signatures or fibres.
    fibres = {}
    for vertex, acceptable in enumerate(masks):
        code = 0
        for j, (left, right) in enumerate(result["tests"]):
            assert 0 <= left <= right < physical_count
            outcome = vertex < physical_count and left <= vertex <= right
            code |= int(outcome) << j
        fibres.setdefault(code, []).append(vertex)
        assert result["decoder"][code] & acceptable
    for cell in fibres.values():
        assert intersection([masks[v] for v in cell])
    return actual


def adaptive_optimum(masks, physical_count):
    size = len(masks)
    rows = [sum(1 << v for v in range(left, right + 1))
            for left in range(physical_count) for right in range(left, physical_count)]

    @lru_cache(None)
    def cost(states):
        indices = [v for v in range(size) if states >> v & 1]
        if intersection([masks[v] for v in indices]):
            return 0
        choices = []
        for row in rows:
            yes, no = states & row, states & ~row
            if yes and no:
                choices.append(1 + max(cost(yes), cost(no)))
        assert choices
        return min(choices)

    return cost((1 << size) - 1)


def run():
    exhaustive, random_cases, catalogues = [], [], []
    total = 0
    for physical_count in range(1, 6):
        for include_empty in (False, True):
            size = physical_count + include_empty
            if size > 5:
                continue
            catalogue, menus = menu_catalogue(physical_count, include_empty)
            counts = {}
            for masks in product(range(1, 8), repeat=size):
                optimum = check_instance(masks, physical_count, include_empty, catalogue)
                counts[optimum] = counts.get(optimum, 0) + 1
                total += 1
            exhaustive.append({"physical_vertices": physical_count,
                               "include_empty_state": include_empty,
                               "action_alphabet_size": 3,
                               "assignments_checked": 7 ** size,
                               "optimal_test_count_histogram": counts})
            catalogues.append({"physical_vertices": physical_count,
                               "include_empty_state": include_empty,
                               "interval_menus_enumerated": menus,
                               "distinct_joint_partitions": len(catalogue)})
    rng = Random(20260930)
    for physical_count in range(5, 8):
        for include_empty in (False, True):
            catalogue, menus = menu_catalogue(physical_count, include_empty)
            size = physical_count + include_empty
            for action_count in (3, 4, 6):
                for _ in range(100):
                    masks = [rng.randrange(1, 1 << action_count) for _ in range(size)]
                    check_instance(masks, physical_count, include_empty, catalogue)
                random_cases.append({"physical_vertices": physical_count,
                                     "include_empty_state": include_empty,
                                     "action_alphabet_size": action_count,
                                     "assignments_checked": 100})
            if size > 5:
                catalogues.append({"physical_vertices": physical_count,
                                   "include_empty_state": include_empty,
                                   "interval_menus_enumerated": menus,
                                   "distinct_joint_partitions": len(catalogue)})
    # The existing action triangle has no bad pair, but one bad triple.
    triangle = [0b011, 0b110, 0b101]
    assert all(triangle[a] & triangle[b] for a, b in combinations(range(3), 2))
    assert not intersection(triangle)
    triangle_result = solve({"acceptable_actions": [["a", "b"], ["b", "c"], ["a", "c"]]})
    assert triangle_result["minimum_tests"] == 1
    # The extra no-defect world changes a constant physical decision target.
    without_empty = solve({"acceptable_actions": [["a"], ["a"], ["a"]]})
    with_empty = solve({"acceptable_actions": [["a"], ["a"], ["a"]], "empty_actions": ["b"]})
    assert without_empty["minimum_tests"] == 0 and with_empty["minimum_tests"] == 1
    # Equal cyclic partition counts do not determine adaptive costs.
    unique, alternating = [1 << v for v in range(6)], [1 << (v % 2) for v in range(6)]
    unique_fixed, alternate_fixed = optimal_design(unique, 6), optimal_design(alternating, 6)
    assert unique_fixed["cyclic_block_count"] == alternate_fixed["cyclic_block_count"] == 6
    assert unique_fixed["minimum_tests"] == alternate_fixed["minimum_tests"] == 3
    assert adaptive_optimum(unique, 6) == 3 and adaptive_optimum(alternating, 6) == 2
    # Applying a one-defect state-order formula to defective subsets is false.
    two_defect_worlds = [world for k in range(3) for world in combinations(range(3), k)]
    singleton_codes = {tuple(v in world for v in range(3)) for world in two_defect_worlds}
    assert len(two_defect_worlds) == len(singleton_codes) == 7
    assert (len(two_defect_worlds) + 1) // 2 == 4 > 3
    return {
        "checked_on": "2026-09-30", "statement_id": "a89c4a7fea1f6a2b1d26",
        "exhaustive_assignments_checked": total,
        "random_assignments_checked": sum(row["assignments_checked"] for row in random_cases),
        "random_seed": 20260930, "exhaustive": exhaustive, "random": random_cases,
        "independent_menu_catalogues": catalogues,
        "examples": {"pairwise_compatible_triangle": triangle_result,
                     "constant_target_without_empty": without_empty,
                     "constant_target_with_empty": with_empty},
        "adaptive_descriptor_boundary": {"cyclic_block_count": 6, "fixed_cost_both": 3,
                                         "unique_target_adaptive_cost": 3,
                                         "alternating_binary_target_adaptive_cost": 2},
        "outside_one_defect_promise": {"physical_vertices": 3, "allowed_defects": 2,
                                       "admitted_worlds": 7, "singleton_tests": 3,
                                       "distinct_signatures": len(singleton_codes),
                                       "cyclic_formula_if_misapplied": 4},
        "scope": "Independent finite controls; the hand proof establishes all finite sizes",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    results = run()
    if args.write:
        Path(__file__).with_name("path-action-sensing-checks.json").write_text(
            json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {results['exhaustive_assignments_checked']} exhaustive and "
          f"{results['random_assignments_checked']} seeded assignments; independent "
          "interval menus and cyclic cuts agree; constructions and boundary cases pass.")
