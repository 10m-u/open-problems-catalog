#!/usr/bin/env python3
"""Exact bounded controls for Q2778's explicitly scoped routes."""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import check_profiles as semantics


def relativize(node):
    op = node[0]
    if op in ("u", "r", "eq", "true"):
        return node
    if op == "not":
        return ("not", relativize(node[1]))
    if op in ("and", "or"):
        return (op, *(relativize(child) for child in node[1:]))
    if op == "exists":
        return (op, node[1], semantics.conj(semantics.u("O", node[1]), relativize(node[2])))
    if op == "count":
        terms = tuple((coefficient, guard,
                       semantics.conj(semantics.u("O", node[2]), relativize(body)))
                      for coefficient, guard, body in node[3])
        return (op, node[1], node[2], terms, node[4], node[5])
    raise AssertionError(op)


def check_relativization():
    checks = 0
    for original in itertools.chain(semantics.structures(1), semantics.structures(2)):
        n, predicates, edges = original
        # Extra nodes carry adversarial unary labels and all edges incident
        # to them, so forgetting O in a count can change its value.
        enlarged_predicates = dict(predicates,
                                   P=predicates["P"] | frozenset([n, n+2]),
                                   Q=predicates["Q"] | frozenset([n+1, n+2]),
                                   O=frozenset(range(n)))
        enlarged_edges = edges | frozenset((i, j) for i in range(n+3)
                                           for j in range(n+3) if i >= n or j >= n)
        old = semantics.Evaluator(original)
        new = semantics.Evaluator((n+3, enlarged_predicates, enlarged_edges))
        for formula in semantics.FORMULAS:
            assert old.evaluate(formula) == new.evaluate(relativize(formula))
            checks += 1
    return checks


def check_tokens():
    construction_checks = 0
    bounds = 0
    for n in range(1, 4):
        for p_mask in range(1 << n):
            for q_mask in range(1 << n):
                predicates = [set(i for i in range(n) if p_mask >> i & 1),
                              set(i for i in range(n) if q_mask >> i & 1)]
                predicates.append(predicates[0] & predicates[1])
                for coefficients in ((2, -3, 1), (3, -2, -1), (-1, 2, -3), (1, 1, -2)):
                    next_token = n
                    tokens = []
                    owner_edges = []
                    positive, negative = [], []
                    for h, (coefficient, satisfied) in enumerate(zip(coefficients, predicates)):
                        group = []
                        owners = []
                        for original in sorted(satisfied):
                            owned = list(range(next_token, next_token+abs(coefficient)))
                            next_token += abs(coefficient)
                            group.extend(owned)
                            owners.extend((original, token) for token in owned)
                        assert all(sum(u == original for u, _ in owners) ==
                                   (abs(coefficient) if original in satisfied else 0)
                                   for original in range(n))
                        assert all(sum(v == token for _, v in owners) == 1 for token in group)
                        tokens.append(set(group))
                        owner_edges.append(owners)
                        (positive if coefficient > 0 else negative).extend(group)
                    assert all(not (a & b) for a, b in itertools.combinations(tokens, 2))
                    assert not set(positive) & set(negative)
                    value = sum(c*len(s) for c, s in zip(coefficients, predicates))
                    if value >= 0:
                        matching = dict(zip(negative, positive))
                        assert len(matching) == len(negative)
                        assert len(set(matching.values())) == len(negative)
                        unmatched = set(positive) - set(matching.values())
                        assert len(unmatched) == value
                        assert (len(unmatched) == 0) == (value == 0)
                        assert bool(unmatched) == (value > 0)
                        for k in range(4):
                            # Distinct local center witnesses exist exactly
                            # when at least k unmatched tokens exist.
                            chosen = sorted(unmatched)[:k]
                            assert (len(chosen) == k) == (value >= k)
                            bounds += 1
                    else:
                        reverse = dict(zip(positive, negative))
                        assert len(reverse) == len(positive)
                        assert len(set(reverse.values())) == len(positive)
                        assert len(set(negative)-set(reverse.values())) == -value
                    construction_checks += 1
    # Independently exhaust all total maps N→P in small sizes; injectivity
    # rather than a construction establishes necessity of each bound.
    map_checks = 0
    for p in range(5):
        for n in range(5):
            witnessed = {"ge": False, "eq": False, "gt": False}
            for targets in itertools.product(range(p), repeat=n):
                if len(set(targets)) == n:
                    witnessed["ge"] = True
                    witnessed["eq"] |= len(set(targets)) == p
                    witnessed["gt"] |= len(set(targets)) < p
                map_checks += 1
            assert witnessed == {"ge": p >= n, "eq": p == n, "gt": p > n}
    return construction_checks, bounds, map_checks


def check_pseudomodel_capacity():
    # The directed-occurrence presentation corresponds to two parallel
    # mutual-E colored edges on the two P vertices.
    p, q = {0, 1}, {2, 3, 4, 5}
    repeated = [(0, 1), (0, 1), (1, 0), (1, 0),
                (0, 2), (0, 3), (1, 4), (1, 5)]
    assert all(sum(x == u and y in p for x, y in repeated) ==
               sum(x == u and y in q for x, y in repeated) == 2 for u in p)
    assert all(sum(y == v and x in p for x, y in repeated) == 1 for v in q)
    assert len(p) == 2 and len(q) == 4
    # Exhaust the only relevant possible simple E edges. Edges sourced
    # in Q are irrelevant to these constraints and cannot repair them.
    allowed = [(x, y) for x in p for y in p | q if x != y]
    simple_checks = 0
    feasible = 0
    for mask in range(1 << len(allowed)):
        edges = [e for i, e in enumerate(allowed) if mask >> i & 1]
        local_p = all(sum(x == u and y in p for x, y in edges) ==
                      sum(x == u and y in q for x, y in edges) for u in p)
        local_q = all(sum(y == v and x in p for x, y in edges) == 1 for v in q)
        feasible += local_p and local_q
        simple_checks += 1
    assert feasible == 0
    # Verify the explicit cardinality-changing lift at (|P|,|Q|)=(4,8).
    p, q = set(range(4)), set(range(4, 12))
    edges = {(i, j) for i in range(2) for j in range(2, 4)}
    edges |= {(j, i) for i, j in list(edges)}
    edges |= {(i, 4+2*i+h) for i in p for h in range(2)}
    assert all(x != y for x, y in edges)
    assert all(sum(x == u and y in p for x, y in edges) ==
               sum(x == u and y in q for x, y in edges) == 2 for u in p)
    assert all(sum(y == v and x in p for x, y in edges) == 1 for v in q)
    return simple_checks


def check_offset_period_counts():
    a, b, c = {0, 1}, {2, 3, 4}, {5}
    r, s = {(0, 2), (1, 3), (1, 4)}, {(1, 5)}
    behaviors = [(sum(x == u for x, _ in r), sum(x == u for x, _ in s)) for u in a]
    assert behaviors == [(1, 0), (2, 1)]
    assert all(sum(y == v for _, y in r) == 1 for v in b)
    assert all(sum(y == v for _, y in s) == 1 for v in c)
    assert len(b)-2*len(c) != len(a)
    assert behaviors[1][0]-2*behaviors[1][1] == 0
    assert behaviors[0][0]-2*behaviors[0][1] == 1
    # Exhaust all eligible R/S edges with the exact fixed unary counts.
    allowed_r = list(itertools.product(a, b))
    allowed_s = list(itertools.product(a, c))
    original_found = relaxed_found = 0
    checks = 0
    for r_mask in range(1 << len(allowed_r)):
        edges_r = [e for i, e in enumerate(allowed_r) if r_mask >> i & 1]
        for s_mask in range(1 << len(allowed_s)):
            edges_s = [e for i, e in enumerate(allowed_s) if s_mask >> i & 1]
            leaves = (all(sum(y == v for _, y in edges_r) == 1 for v in b) and
                      all(sum(y == v for _, y in edges_s) == 1 for v in c))
            degrees = [(sum(x == u for x, _ in edges_r), sum(x == u for x, _ in edges_s))
                       for u in a]
            original_found += leaves and all(x-2*y == 1 for x, y in degrees)
            relaxed_found += leaves and all(v in ((1, 0), (2, 1)) for v in degrees) and (1, 0) in degrees
            checks += 1
    assert original_found == 0
    assert relaxed_found == 6
    # Merging the two A elements keeps all leaf edges but changes |A|.
    merged_r, merged_s = {(0, v) for _, v in r}, {(0, v) for _, v in s}
    assert len(merged_r)-2*len(merged_s) == 1
    return checks, relaxed_found


def check_homogenized_matching():
    witnesses = 0
    for a in range(1, 5):
        for b in range(1, 5):
            matchings = list(itertools.permutations(range(b), a)) if a <= b else []
            feasible = any(len(set(values)) == b for values in matchings)
            assert feasible == (a == b)
            if feasible:
                t = a+b
                assert t != 1
                witnesses += 1
    assert math.gcd(math.gcd(1, 1), 2) == 1
    # Explicit enlarged model: A={0}, B={1}, T={2,3}; owner equality
    # pairs originals with T while original R matches 0→1.
    r = {(0, 1)}
    owner = {(0, 2), (1, 3)}
    assert len(r) == 1 and len(owner) == 2
    assert {x for x, _ in owner} == {0, 1}
    assert {y for _, y in owner} == {2, 3}
    return witnesses


def check_multivariate_generators():
    out = semantics.edge("x", "y")
    inc = semantics.edge("y", "x")
    formula = semantics.conj(
        semantics.forall("x", semantics.disj(
            semantics.conj(semantics.u("P", "x"), semantics.neg(semantics.u("Q", "x"))),
            semantics.conj(semantics.neg(semantics.u("P", "x")), semantics.u("Q", "x")))),
        semantics.forall("x", semantics.disj(semantics.neg(semantics.u("P", "x")),
            semantics.count("x", "y", [(1, out, semantics.u("P", "y")),
                                         (-1, out, semantics.u("Q", "y"))], "eq", 0))),
        semantics.forall("x", semantics.disj(semantics.neg(semantics.u("Q", "x")),
            semantics.count("x", "y", [(1, inc, semantics.u("P", "y"))], "eq", 1))),
        semantics.forall("x", semantics.count("x", "y", [(1, out, semantics.EQ)], "eq", 0)),
    )
    closed = sorted((node for node in semantics.subformulas(formula) if not semantics.free(node)), key=repr)
    common_profile = None
    realization_checks = 0
    for a in range(1, 8):
        eligible = [(x, y) for x in range(a) for y in range(a) if x != y]
        for b in range(a*(a-1)+1):
            internal = eligible[:b]
            edges = frozenset(internal + [(tail, a+h) for h, (tail, _) in enumerate(internal)])
            predicates = {"P": frozenset(range(a)), "Q": frozenset(range(a, a+b))}
            ev = semantics.Evaluator((a+b, predicates, edges))
            assert ev.evaluate(formula)
            profile = tuple(ev.evaluate(node) for node in closed)
            if common_profile is None:
                common_profile = profile
            assert profile == common_profile
            realization_checks += 1
    split_checks = 0
    for a in range(2, 31):
        for left in range(1, a):
            right = a-left
            maximum_sum = left*(left-1)+right*(right-1)
            assert maximum_sum == a*(a-1)-2*left*right
            assert maximum_sum < a*(a-1)
            split_checks += 1
    return realization_checks, split_checks, len(closed)


def main():
    relational = check_relativization()
    token_checks, bound_checks, map_checks = check_tokens()
    capacity_checks = check_pseudomodel_capacity()
    split_checks, relaxed_count = check_offset_period_counts()
    homogeneous_matching = check_homogenized_matching()
    realizations, indecomposable_splits, profile_size = check_multivariate_generators()
    result = {
        "question": "Q2778",
        "status": "passed",
        "completed_attempt_controls": ["A1", "A2", "A3", "A4", "A5"],
        "relativization_checks_with_adversarial_extra_nodes": relational,
        "weighted_overlapping_token_constructions": token_checks,
        "positive_surplus_bound_checks": bound_checks,
        "independent_total_matching_maps_exhausted": map_checks,
        "A2_simple_graph_false_positive_controls_exhausted": capacity_checks,
        "A2_scaled_simple_lift": "passed at (4,8)",
        "A3_typed_offset_period_edge_sets_exhausted": split_checks,
        "A3_original_models": 0,
        "A3_relaxed_models": relaxed_count,
        "A4_positive_even_scale_matching_families": homogeneous_matching,
        "A4_primitive_class_vector": [1, 1, 2],
        "A5_exact_vector_realizations_checked": realizations,
        "A5_common_closed_profile_coordinates": profile_size,
        "A5_boundary_indecomposable_split_checks": indecomposable_splits,
        "scope": "Restricted reduction controls; does not decide full Q2778.",
    }
    Path(__file__).with_name("GLOBAL-ROUTE-CHECK-RESULTS.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
