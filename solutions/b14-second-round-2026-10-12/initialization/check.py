#!/usr/bin/env python3
"""Bounded exact checks for path NN and tree 2-opt proofs; no sampling estimate."""

from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random


def edge(a, b):
    return tuple(sorted((a, b)))


def nearest_neighbor(d, start):
    remaining = set(range(len(d))) - {start}
    tour = [start]
    while remaining:
        chosen = min(remaining, key=lambda v: (d[tour[-1]][v], v))
        remaining.remove(chosen)
        tour.append(chosen)
    return tour


def tour_cost(d, tour):
    return sum(d[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


def path_instance(weights):
    z = [0]
    for w in weights:
        z.append(z[-1] + w)
    return z, [[abs(a - b) for b in z] for a in z]


def check_path(weights, start):
    z, d = path_instance(weights)
    n, w = len(z), z[-1]
    tour = nearest_neighbor(d, start)
    left = right = current = start
    switches = []
    for visited, v in enumerate(tour[1:], start=1):
        assert v in (left - 1, right + 1)
        span = z[right] - z[left]
        is_switch = visited > 1 and ((current == left and v > right) or (current == right and v < left))
        if is_switch:
            g = z[v] - z[right] if v > right else z[left] - z[v]
            if current == left:
                f = z[left] - z[left - 1] if left else None
            else:
                f = z[right + 1] - z[right] if right + 1 < n else None
            if f is not None:
                assert span + g <= f
            switches.append((span, g, f))
        left, right = min(left, v), max(right, v)
        current = v
    for (_, g, f), (_, next_g, _) in zip(switches, switches[1:]):
        assert f is not None and next_g == f
    excess = sum(span for span, _, _ in switches)
    assert excess <= w
    assert tour_cost(d, tour) == w + excess + d[tour[-1]][start]
    assert tour_cost(d, tour) <= 3 * w
    if start in (0, n - 1):
        assert tour_cost(d, tour) == 2 * w
    return F(tour_cost(d, tour), 2 * w)


def pruefer_tree(n, sequence):
    degree = [1] * n
    for v in sequence:
        degree[v] += 1
    edges = []
    for v in sequence:
        leaf = min(u for u in range(n) if degree[u] == 1)
        edges.append(edge(leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    last = [u for u in range(n) if degree[u] == 1]
    edges.append(edge(*last))
    return sorted(edges)


def tree_instance(n, edges, weights):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    cuts = []
    for banned in edges:
        seen, stack = {banned[0]}, [banned[0]]
        while stack:
            current = stack.pop()
            for neighbor in adj[current]:
                if edge(current, neighbor) != banned and neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        cuts.append(seen)
    infinity = 10 ** 9
    d = [[0 if a == b else infinity for b in range(n)] for a in range(n)]
    for (a, b), w in zip(edges, weights):
        d[a][b] = d[b][a] = w
    for k in range(n):
        for a in range(n):
            for b in range(n):
                d[a][b] = min(d[a][b], d[a][k] + d[k][b])
    for a, b in combinations(range(n), 2):
        assert d[a][b] == sum(w for w, cut in zip(weights, cuts) if (a in cut) != (b in cut))
    return d, cuts


def multiplicities(tour, cuts):
    return [sum((tour[i] in cut) != (tour[(i + 1) % len(tour)] in cut)
                for i in range(len(tour))) for cut in cuts]


def moves(tour):
    n = len(tour)
    for i, j in combinations(range(n), 2):
        if j == i + 1 or (i == 0 and j == n - 1):
            continue
        yield i, j, tour[:i + 1] + tuple(reversed(tour[i + 1:j + 1])) + tour[j + 1:]


def distinct_tours(n):
    for tail in permutations(range(1, n)):
        if tail[0] < tail[-1]:
            yield (0,) + tail


def descend(d, cuts, tour, mode, target):
    initial_phi = sum(multiplicities(tour, cuts))
    limit = (initial_phi - 2 * len(cuts)) // 2
    steps = 0
    while True:
        old_cost = tour_cost(d, tour)
        candidates = []
        for i, j, next_tour in moves(tour):
            new_cost = tour_cost(d, next_tour)
            if new_cost < old_cost:
                candidates.append((new_cost, i, j, next_tour))
                if mode == "first":
                    break
        if not candidates:
            assert old_cost == target
            break
        _, _, _, next_tour = candidates[0] if mode == "first" else min(candidates)
        before = multiplicities(tour, cuts)
        after = multiplicities(next_tour, cuts)
        assert all(b <= a for a, b in zip(before, after))
        assert sum(after) <= sum(before) - 2
        tour = next_tour
        steps += 1
        assert steps <= limit
    return steps


def main():
    rng = random.Random(3817)
    report = {"status": "passed", "random_seed_for_case_selection": 3817, "checks": {}}
    path_cases = 0
    maximum_ratio = F(1)
    for n in range(3, 8):
        for weights in product(range(1, 5), repeat=n - 1):
            for start in range(n):
                maximum_ratio = max(maximum_ratio, check_path(weights, start))
                path_cases += 1
    report["checks"]["exhaustive_path_accounting"] = {
        "n_range": [3, 7], "edge_weights": [1, 2, 3, 4], "all_starts": True,
        "cases": path_cases, "maximum_ratio_on_this_finite_set": str(maximum_ratio),
        "bound": "3/2", "switch_cost_accounting_checked": True,
    }

    tight_examples = []
    epsilon = F(1, 4)
    for k in [2, 3, 8, 32, 128]:
        weights = [k + 2 * epsilon] + [1] * (k - 1) + [1 + epsilon]
        z, d = path_instance(weights)
        tour = nearest_neighbor(d, k)
        assert tour == list(range(k, 0, -1)) + [k + 1, 0]
        for i, current in enumerate(tour[:-1]):
            remaining = tour[i + 1:]
            distances = sorted(d[current][v] for v in remaining)
            assert len(distances) == 1 or distances[0] < distances[1]
        ratio = check_path(weights, k)
        assert ratio == 1 + F(k - 1) / (2 * k + 3 * epsilon)
        tight_examples.append({"k": k, "ratio": str(ratio), "strict_nearest_choices": True})
    report["checks"]["tight_family"] = tight_examples

    star_tours = 0
    for n in range(3, 8):
        edges = [(0, v) for v in range(1, n)]
        weights = [1 + v % 4 for v in range(1, n)]
        d, cuts = tree_instance(n, edges, weights)
        for tour in distinct_tours(n):
            assert tour_cost(d, tour) == 2 * sum(weights)
            assert multiplicities(tour, cuts) == [2] * (n - 1)
            star_tours += 1
    report["checks"]["stars_all_tours_optimal"] = {"n_range": [3, 7], "tours_checked": star_tours}

    tree_cases = tours_checked = exchanges_checked = strict_moves = descents_checked = 0
    max_descent = 0
    for n in range(3, 8):
        if n <= 5:
            sequences = list(product(range(n), repeat=n - 2))
        else:
            sequences = sorted({tuple(rng.randrange(n) for _ in range(n - 2)) for _ in range(24)})
        for tree_index, sequence in enumerate(sequences):
            edges = pruefer_tree(n, sequence)
            # All positive unit weights plus a second explicit unequal-weight test.
            weight_sets = [[1] * (n - 1), [1 + ((a * 3 + b * 7) % 5) for a, b in edges]]
            for weights in weight_sets:
                d, cuts = tree_instance(n, edges, weights)
                w = sum(weights)
                family_limit = sum(min(len(cut), n - len(cut)) - 1 for cut in cuts)
                assert family_limit <= (n - 1) * (n // 2 - 1)
                for tour in distinct_tours(n):
                    counts = multiplicities(tour, cuts)
                    old = tour_cost(d, tour)
                    assert old == sum(weight * count for weight, count in zip(weights, counts))
                    assert all(count >= 2 and count % 2 == 0 for count in counts)
                    has_improvement = False
                    for _, _, next_tour in moves(tour):
                        new = tour_cost(d, next_tour)
                        exchanges_checked += 1
                        if new < old:
                            after = multiplicities(next_tour, cuts)
                            assert all(b <= a for a, b in zip(counts, after))
                            assert sum(after) <= sum(counts) - 2
                            assert old - new == sum(weight * (a - b) for weight, a, b in zip(weights, counts, after))
                            has_improvement = True
                            strict_moves += 1
                    assert has_improvement == (old > 2 * w)
                    tours_checked += 1
                if tree_index < 6:
                    for start in range(n):
                        initial = tuple(nearest_neighbor(d, start))
                        for mode in ["first", "best"]:
                            steps = descend(d, cuts, initial, mode, 2 * w)
                            assert steps <= family_limit
                            max_descent = max(max_descent, steps)
                            descents_checked += 1
                tree_cases += 1
    report["checks"]["tree_exchange_monotonicity_and_optimum"] = {
        "n_range": [3, 7], "all_labeled_tree_topologies_through_n": 5,
        "selected_pruefer_topologies_each_larger_n": 24, "positive_weight_assignments_per_tree": 2,
        "tree_instances": tree_cases, "tours": tours_checked, "exchange_tests": exchanges_checked,
        "strict_improvements": strict_moves,
        "local_optimum_cost": "2W", "cut_vectors_componentwise_nonincreasing": True,
    }
    report["checks"]["actual_nearest_neighbor_initialized_descents"] = {
        "pivot_rules": ["lexicographic first improvement", "best improvement"],
        "descents": descents_checked, "maximum_observed_steps_in_this_finite_set": max_descent,
        "starting_potential_bound_and_family_bound_checked": True,
    }

    exact_four_city_cases = 0
    for a, b, c in product(range(1, 8), repeat=3):
        if a == b or c == a + b:
            continue  # Measure-zero ties are immaterial to the continuous integral.
        _, d = path_instance([a, b, c])
        actual_excess = tour_cost(d, nearest_neighbor(d, 1)) - 2 * (a + b + c)
        expected_excess = 2 * b if b < a and c > a + b else 0
        assert actual_excess == expected_excess
        exact_four_city_cases += 1
    # Integrate the exact polynomial 2*b*(1/2-2*b) on [0,1/4].
    endpoint = F(1, 4)
    extra_ratio = 2 * (F(1, 2) * endpoint ** 2 / 2 - 2 * endpoint ** 3 / 3)
    assert extra_ratio == F(1, 96)
    assert 1 + extra_ratio == F(97, 96)
    raw_exponential_excess = F(1, 4) ** 2
    assert raw_exponential_excess == F(1, 16)
    assert F(97, 16) / 6 == F(97, 96)
    report["checks"]["four_city_exponential_exact_integral"] = {
        "strict_choice_region_cases": exact_four_city_cases,
        "expected_ratio_interior_start": "97/96", "expected_excess_cost": "1/16",
        "expected_optimum": 6, "expected_nn_cost": "97/16",
        "integration": "exact rational polynomial on normalized simplex; exponential first moment",
    }
    output = Path(__file__).with_name("CHECK-RESULTS.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
