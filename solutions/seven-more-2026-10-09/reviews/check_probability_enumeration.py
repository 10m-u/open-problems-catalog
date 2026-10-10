#!/usr/bin/env python3
"""Independent exhaustive coverage control for the Q276/Q277 certificates.

Enumerates labeled edge subsets directly, instead of using edge/leaf
augmentation; enumerates Boolean truth tables instead of using sections.
The reviewed canonicalizer is reused solely for isomorphism comparison.
"""

import importlib.util
from itertools import combinations
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    spec = importlib.util.spec_from_file_location(
        "freezing", root / "probability/verify_constant_freezing.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    found, examined = set(), 0
    for n in range(2, 7):
        for edge_count in range(n - 1, 6):
            for edges in combinations(combinations(range(n), 2), edge_count):
                reached = {0}
                for _ in range(n):
                    for u, v in edges:
                        if u in reached or v in reached:
                            reached.update([u, v])
                if len(reached) == n:
                    examined += 1
                    found.add(module.canonical(n, edges))
    assert found == set(module.connected_graphs(5))
    truth_table_counts = []
    for bits in range(5):
        increasing = []
        for event in range(1 << (1 << bits)):
            valid = True
            for mask in range(1 << bits):
                if not (event >> mask & 1):
                    continue
                if any(not (event >> (mask | 1 << bit) & 1) for bit in range(bits)):
                    valid = False
                    break
            if valid:
                increasing.append(event)
        assert set(increasing) == set(module.upsets(bits))
        truth_table_counts.append(len(increasing))
    report = {
        "date": "2026-10-09",
        "all_passed": True,
        "labeled_connected_graphs_examined": examined,
        "isomorphism_classes_through_five_edges": len(found),
        "increasing_truth_table_counts_zero_through_four_bits": truth_table_counts,
        "scope": "Coverage cross-check only; the original checker certifies every polynomial sign through its stated ranges.",
    }
    Path(__file__).with_name("probability-enumeration-review.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
