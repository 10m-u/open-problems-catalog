#!/usr/bin/env python3
"""Exact certificates for Chebikin Question 4.3.4; Python standard library only.

Discovery used a bounded SAT search. Verification here uses no solver: it
checks the literal axioms and every circular order on the seven vertices.
Run from any directory; pass --write to save the checked results alongside it.
"""
import argparse
from itertools import combinations, permutations
import json
from pathlib import Path


VERTICES = tuple(range(7))
R = {
    (0, 1, 4), (0, 2, 1), (0, 2, 4), (0, 2, 5), (0, 2, 6),
    (0, 3, 4), (0, 3, 6), (0, 5, 6), (1, 3, 2), (1, 3, 6),
    (1, 4, 2), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 5, 3),
    (2, 5, 6), (3, 4, 5), (4, 5, 6),
}
REMOVED = (0, 3, 4)
S = R - {REMOVED}
EXPECTED_EXTENSION = (0, 2, 1, 4, 5, 3, 6)
EXPECTED_RULE_SUPPORTS = {(0, 1, 2, 4), (0, 2, 5, 6), (1, 4, 5, 6)}


def cyclic(triple):
    return min(triple, triple[1:] + triple[:1], triple[2:] + triple[:2])


def check_axioms(relation):
    """Cyclic notation implements rotations; test asymmetry and all B rules."""
    assert all(len(set(t)) == 3 and set(t) <= set(VERTICES) for t in relation)
    assert all(cyclic(t) == t for t in relation)
    for x, y, z in relation:
        assert cyclic((x, z, y)) not in relation
    supports = set()
    firings = 0
    for x, y, z, w in permutations(VERTICES, 4):
        if cyclic((x, y, z)) in relation and cyclic((x, z, w)) in relation:
            assert cyclic((x, y, w)) in relation
            assert cyclic((y, z, w)) in relation
            supports.add(tuple(sorted((x, y, z, w))))
            firings += 1
    assert supports == EXPECTED_RULE_SUPPORTS
    return {"asymmetry": True, "transitivity": True,
            "ordered_quadruples_checked": 840, "rule_firings": firings,
            "four_element_rule_supports": sorted(supports)}


def clockwise(order, triple):
    """Independent position-based orientation check, without normalization."""
    pos = {x: i for i, x in enumerate(order)}
    a, b, c = (pos[x] for x in triple)
    return a < b < c or b < c < a or c < a < b


def extensions(relation):
    # Rotation fixes 0 first. Reflection is distinct and must remain included.
    return [(0,) + tail for tail in permutations(VERTICES[1:])
            if all(clockwise((0,) + tail, t) for t in relation)]


def run():
    r_axioms, s_axioms = check_axioms(R), check_axioms(S)
    r_extensions, s_extensions = extensions(R), extensions(S)
    assert r_extensions == []
    assert s_extensions == [EXPECTED_EXTENSION]
    forced = {cyclic(t) for t in combinations(EXPECTED_EXTENSION, 3)}
    missing = forced - S
    assert len(forced) == 35 and len(missing) == 18
    assert (0, 4, 3) in missing and REMOVED not in forced
    assert all(clockwise(EXPECTED_EXTENSION, t) for t in forced)
    return {
        "statement_id": "049cdbf27846a9b67646",
        "checked_on": "2026-09-30", "vertices": VERTICES,
        "circular_orders_checked_per_relation": 720,
        "nonextendible": {"relations": sorted(R), "axioms": r_axioms,
                          "extensions": r_extensions},
        "extendible_incomplete": {"relations": sorted(S), "axioms": s_axioms,
                                  "extensions": s_extensions,
                                  "forced_missing_triples": sorted(missing)},
        "answers": {"axioms_guarantee_an_extension": False,
                    "axioms_guarantee_completeness_when_extendible": False},
        "formal_proof_assistant_checked": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write:
        Path(__file__).with_name("circular-orders-checks.json").write_text(
            json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS: both relations satisfy A/B; 720 orders each; "
          "R has 0 extensions; S has 1 extension and 18 missing consequences.")
