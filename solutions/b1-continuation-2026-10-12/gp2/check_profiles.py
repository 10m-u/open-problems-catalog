#!/usr/bin/env python3
"""Bounded independent semantic controls for the Q2777 profile proof."""
from __future__ import annotations

import itertools
import json
from pathlib import Path
import random


def u(name, var):
    return ("u", name, var)


def edge(left, right):
    return ("r", left, right)


def neg(child):
    return ("not", child)


def conj(*children):
    return ("and", *children)


def disj(*children):
    return ("or", *children)


def exists(var, child):
    return ("exists", var, child)


def forall(var, child):
    return neg(exists(var, neg(child)))


def count(retained, bound, terms, relation, target):
    # Each term is (integer coefficient, positive guard, counted body).
    return ("count", retained, bound, tuple(terms), relation, target)


TOP = ("true",)
EQ = ("eq", "x", "y")
P = exists("x", u("P", "x"))
Q = exists("x", u("Q", "x"))
out = edge("x", "y")
inc = edge("y", "x")
degree_y = count("y", "x", [(2, edge("y", "x"), u("P", "x")),
                                 (-1, edge("x", "y"), TOP)], "le", 1)
FORMULAS = [
    disj(conj(P, neg(Q)), conj(neg(P), Q)),
    exists("x", count("x", "y", [(-3, out, u("P", "y")),
                                      (2, inc, u("Q", "y"))], "eq", 0)),
    forall("x", disj(neg(u("P", "x")),
                     count("x", "y", [(1, out, u("Q", "y"))], "ge", 1))),
    exists("x", count("x", "y", [(1, out, degree_y),
                                      (-2, inc, neg(degree_y))], "le", -1)),
    forall("x", disj(Q, count("x", "y", [(1, out, conj(P, u("P", "y"))),
                                            (-1, inc, conj(neg(P), u("Q", "y")))],
                               "eq", 0))),
    exists("x", conj(u("P", "x"), neg(Q),
                     count("x", "y", [(1, out, neg(EQ))], "eq", 1))),
    forall("x", count("x", "y", [(1, out, disj(EQ, neg(u("P", "y"))))],
                       "le", 2)),
    neg(exists("x", count("x", "y", [(2, out, conj(Q, degree_y)),
                                          (-3, inc, conj(P, neg(degree_y)))],
                            "ge", 2))),
    exists("x", count("x", "y", [(1, out, conj(P, Q, degree_y))], "mod", (1, 2))),
    # Equality guard is an optional local shorthand, tested separately from
    # the source's binary-relation guard constructors.
    forall("x", count("x", "y", [(1, EQ, disj(u("P", "y"), neg(P)))], "eq", 1)),
]


def children(node):
    op = node[0]
    if op == "not":
        return (node[1],)
    if op in ("and", "or"):
        return node[1:]
    if op == "exists":
        return (node[2],)
    if op == "count":
        return tuple(t for _, guard, body in node[3] for t in (guard, body))
    return ()


def subformulas(node):
    found = {node}
    for child in children(node):
        found.update(subformulas(child))
    return found


def free(node):
    op = node[0]
    if op == "true":
        return frozenset()
    if op == "u":
        return frozenset([node[2]])
    if op in ("eq", "r"):
        return frozenset(node[1:])
    total = frozenset().union(*(free(child) for child in children(node)))
    if op == "exists":
        return total - {node[1]}
    if op == "count":
        return total - {node[2]}
    return total


class Evaluator:
    def __init__(self, model):
        self.n, self.predicates, self.edges = model
        self.cache = {}

    def evaluate(self, node, x=None, y=None):
        key = (node, x, y)
        if key in self.cache:
            return self.cache[key]
        env = {"x": x, "y": y}
        op = node[0]
        if op == "true":
            result = True
        elif op == "u":
            result = env[node[2]] in self.predicates[node[1]]
        elif op == "r":
            result = (env[node[1]], env[node[2]]) in self.edges
        elif op == "eq":
            result = env[node[1]] == env[node[2]]
        elif op == "not":
            result = not self.evaluate(node[1], x, y)
        elif op in ("and", "or"):
            values = [self.evaluate(child, x, y) for child in children(node)]
            result = all(values) if op == "and" else any(values)
        elif op == "exists":
            result = False
            for value in range(self.n):
                bound = dict(env, **{node[1]: value})
                if self.evaluate(node[2], **bound):
                    result = True
                    break
        elif op == "count":
            value = 0
            for coefficient, guard, body in node[3]:
                amount = 0
                for target in range(self.n):
                    bound = dict(env, **{node[2]: target})
                    if self.evaluate(guard, **bound) and self.evaluate(body, **bound):
                        amount += 1
                value += coefficient * amount
            relation, target = node[4:]
            if relation == "eq":
                result = value == target
            elif relation == "le":
                result = value <= target
            elif relation == "ge":
                result = value >= target
            elif relation == "mod":
                result = value % target[1] == target[0]
            else:
                raise AssertionError(relation)
        else:
            raise AssertionError(op)
        self.cache[key] = result
        return result


def structures(n):
    pairs = list(itertools.product(range(n), repeat=2))
    for mask_p in range(1 << n):
        for mask_q in range(1 << n):
            predicates = {"P": frozenset(i for i in range(n) if mask_p >> i & 1),
                          "Q": frozenset(i for i in range(n) if mask_q >> i & 1)}
            for edge_mask in range(1 << (n*n)):
                edges = frozenset(pair for i, pair in enumerate(pairs) if edge_mask >> i & 1)
                yield n, predicates, edges


def union(a, b):
    offset = a[0]
    predicates = {name: a[1][name] | frozenset(i+offset for i in b[1][name])
                  for name in ("P", "Q")}
    edges = a[2] | frozenset((i+offset, j+offset) for i, j in b[2])
    return a[0]+b[0], predicates, edges


def main():
    all_small = list(structures(1)) + list(structures(2))
    loop_free = [m for m in all_small if all(i != j for i, j in m[2])]
    with_loops = [m for m in all_small if any(i == j for i, j in m[2])]
    selected = loop_free + random.Random(2777).sample(with_loops, 24)
    evaluators = [Evaluator(m) for m in selected]
    nodes = [sorted(subformulas(f), key=repr) for f in FORMULAS]
    profiles = [[tuple(ev.evaluate(node) for node in ns if not free(node))
                 for ev in evaluators] for ns in nodes]
    matched = checks = 0
    for i, a in enumerate(selected):
        for j, b in enumerate(selected):
            joined = Evaluator(union(a, b))
            for h, ns in enumerate(nodes):
                if profiles[h][i] != profiles[h][j]:
                    continue
                matched += 1
                for model, ev, offset in ((a, evaluators[i], 0),
                                          (b, evaluators[j], a[0])):
                    for node in ns:
                        variables = sorted(free(node))
                        for assignment in itertools.product(range(model[0]), repeat=len(variables)):
                            original = dict(zip(variables, assignment))
                            moved = {v: value+offset for v, value in original.items()}
                            assert joined.evaluate(node, **moved) == ev.evaluate(node, **original), (h, i, j, node)
                            checks += 1
    # Different profiles can make a GP² sentence fail in a disjoint union.
    a = (1, {"P": frozenset([0]), "Q": frozenset()}, frozenset())
    b = (1, {"P": frozenset(), "Q": frozenset([0])}, frozenset())
    assert Evaluator(a).evaluate(FORMULAS[0])
    assert Evaluator(b).evaluate(FORMULAS[0])
    assert not Evaluator(union(a, b)).evaluate(FORMULAS[0])
    # Adding global fixed-threshold counting would break the lemma even
    # when the two singletons have the same full truth profile.
    assert len(a[1]["P"]) == 1
    assert len(union(a, a)[1]["P"]) == 2
    # Source's nonsemilinear vector-set additive closure, all bounded pairs.
    vectors = [(a, b) for a in range(8) for b in range(a*(a-1)+1)]
    vector_checks = 0
    for a, b in vectors:
        for c, d in vectors:
            assert b+d <= (a+c)*(a+c-1)
            vector_checks += 1
    # Residue minima characterize each generated numerical semigroup.
    semigroup_checks = 0
    for length in range(1, 4):
        for generators in itertools.combinations(range(1, 8), length):
            reached = {0}
            for value in range(1, 401):
                if any(value-g in reached for g in generators):
                    reached.add(value)
            positive = reached - {0}
            m = min(positive)
            minima = {r: min(v for v in positive if v % m == r)
                      for r in range(m) if any(v % m == r for v in positive)}
            for value in range(1, 401):
                predicted = value % m in minima and value >= minima[value % m]
                assert predicted == (value in positive)
                semigroup_checks += 1
    receipt = {
        "question": "Q2777",
        "status": "passed",
        "structures": len(selected),
        "exhaustive_loop_free_structures_n1_n2": len(loop_free),
        "additional_looped_structures": 24,
        "formulas": len(FORMULAS),
        "ordered_structure_pairs": len(selected)**2,
        "same_profile_formula_pairs": matched,
        "subformula_assignment_preservation_checks": checks,
        "quadratic_vector_addition_checks": vector_checks,
        "residue_minimum_membership_checks": semigroup_checks,
        "unequal_profile_and_global_counting_controls": "passed",
        "scope": "Finite semantic regression controls; all-size theorem requires proof review.",
    }
    target = Path(__file__).with_name("PROFILE-CHECK-RESULTS.json")
    target.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
