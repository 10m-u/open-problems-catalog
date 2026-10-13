#!/usr/bin/env python3
"""Construct and independently check CP addition-only tree Tseitin proofs."""
from itertools import product
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def cnf(n, edges, charge):
    clauses = []
    for v in range(n):
        incident = [i for i, (a, b) in enumerate(edges) if v in (a, b)]
        for bits in product((0, 1), repeat=len(incident)):
            if sum(bits) % 2 != charge[v]:
                clauses.append([(i, 1 if bit == 0 else -1)
                                for i, bit in zip(incident, bits)])
    return clauses


def inequality(clause, m):
    coefficients = [0] * m
    for i, sign in clause:
        coefficients[i] = sign
    return [coefficients, 1 - sum(sign < 0 for _, sign in clause)]


def proof(n, edges, charge):
    clauses = cnf(n, edges, charge)
    lines = [dict(inequality=inequality(c, len(edges)), axiom=i)
             for i, c in enumerate(clauses)]
    assigned = {}
    unit_lines = {}
    while True:
        changed = False
        for original, clause in enumerate(clauses):
            if any(i in assigned and (assigned[i] == 1) == (sign == 1)
                   for i, sign in clause):
                continue
            remaining = [(i, sign) for i, sign in clause if i not in assigned]
            if len(remaining) > 1:
                continue
            index = original
            for i, _ in clause:
                if i in assigned:
                    other = unit_lines[i]
                    a, b = lines[index]["inequality"]
                    c, d = lines[other]["inequality"]
                    lines.append({"inequality": [[x+y for x,y in zip(a,c)], b+d],
                                  "sum": [index, other]})
                    index = len(lines) - 1
            if not remaining:
                assert lines[index]["inequality"] == [[0] * len(edges), 1]
                return {"n": n, "edges": edges, "charge": charge,
                        "lines": lines, "conclusion": index}
            i, sign = remaining[0]
            assert i not in assigned
            assigned[i] = int(sign > 0)
            unit_lines[i] = index
            changed = True
        assert changed, "Odd tree should propagate to contradiction"


def verify(packet):
    edges = packet["edges"]
    n = packet["n"]
    assert len(edges) == n-1 and sum(packet["charge"]) % 2 == 1
    vertices = {0}
    while True:
        nxt = vertices | {a for a,b in edges if b in vertices} | {
            b for a,b in edges if a in vertices}
        if nxt == vertices: break
        vertices = nxt
    assert len(vertices) == n
    axioms = [inequality(c, len(edges)) for c in cnf(n, edges, packet["charge"])]
    for i, line in enumerate(packet["lines"]):
        if "axiom" in line:
            expected = axioms[line["axiom"]]
        else:
            left, right = line["sum"]
            assert left < i and right < i
            a,b = packet["lines"][left]["inequality"]
            c,d = packet["lines"][right]["inequality"]
            expected = [[x+y for x,y in zip(a,c)], b+d]
        assert line["inequality"] == expected
    assert packet["lines"][packet["conclusion"]]["inequality"] == [[0]*len(edges), 1]


if __name__ == "__main__":
    rng = random.Random(20261012)
    checks = 0
    maximum = 0
    exemplar = None
    for n in range(2, 9):
        trees = [
            [(i-1, i) for i in range(1,n)],
            [(0, i) for i in range(1,n)],
            [(rng.randrange(i), i) for i in range(1,n)]]
        for edges in trees:
            for charge in product((0, 1), repeat=n):
                if sum(charge) % 2 == 0: continue
                packet = json.loads(json.dumps(proof(n, edges, charge)))
                verify(packet)
                checks += 1
                maximum = max(maximum, len(packet["lines"]))
                if n == 8 and edges == trees[0]: exemplar = packet
    (HERE / "TREE-CP-CERTIFICATE.json").write_text(json.dumps(exemplar, indent=2)+"\n")
    result = {"odd_charge_tree_refutations_checked": checks,
              "vertices": [2,8], "largest_line_count": maximum,
              "rules_used": ["input_CNF_inequality", "addition"],
              "all_graph_polynomial_line_bound": False}
    (HERE / "TREE-CP-CHECK.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result))
