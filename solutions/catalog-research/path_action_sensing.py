#!/usr/bin/env python3
"""Optimal unit-cost fixed interval sensing for acceptable actions.

Input JSON has nonempty `acceptable_actions` lists for path vertices 1,...,n.
Optional `empty_actions` admits the no-defect state. Exactly one defect is
otherwise guaranteed. Action names are strings. Tests are noiseless intervals
with freely chosen endpoints. See path-acceptable-actions.md for the proof.

With no input file, solve the three-state overlapping-action example.
"""
import argparse
import json
from pathlib import Path
import sys


def cyclic_partition(masks):
    """Minimum compatible cyclic-arc partition, by n greedy linear scans."""
    if not masks or any(not isinstance(g, int) or g <= 0 for g in masks):
        raise ValueError("Every state must have a nonempty action bitmask")
    size = len(masks)
    best = None
    for start in range(size):
        blocks, block, common = [], [], 0
        for step in range(size):
            vertex = (start + step) % size
            if not block:
                block, common = [vertex], masks[vertex]
            elif common & masks[vertex]:
                block.append(vertex)
                common &= masks[vertex]
            else:
                blocks.append(tuple(block))
                block, common = [vertex], masks[vertex]
        blocks.append(tuple(block))
        if best is None or len(blocks) < len(best):
            best = blocks
    return best


def signature(pools, vertex):
    return sum(int(left <= vertex <= right) << j
               for j, (left, right) in enumerate(pools))


def optimal_design(masks, physical_count):
    """Bitmask API; vertices are 0-based and an optional empty state is last."""
    if physical_count < 1 or len(masks) not in (physical_count, physical_count + 1):
        raise ValueError("Supply n path states, optionally followed by the empty state")
    blocks = cyclic_partition(masks)
    count = len(blocks)
    if count == 1:
        pools = []
    else:
        # A block containing the empty state must have the all-zero signature.
        # Without that state, use the block containing physical vertex 0.
        root = physical_count if len(masks) > physical_count else 0
        zero_block = next(block for block in blocks if root in block)
        other = sorted((b for b in blocks if b != zero_block), key=min)
        # Complement of the root block is an ordinary physical path interval.
        # All other blocks are ordinary intervals inside that complement.
        width = (count + 1) // 2
        pools = [(min(other[j]), max(other[min(j + width - 1, len(other) - 1)]))
                 for j in range(width)]
    fibres = {}
    for vertex, acceptable in enumerate(masks):
        code = signature(pools, vertex)
        if code not in fibres:
            fibres[code] = {"states": [], "common_actions": acceptable}
        fibres[code]["states"].append(vertex)
        fibres[code]["common_actions"] &= acceptable
    decoder = {}
    for code, fibre in fibres.items():
        common = fibre["common_actions"]
        if not common:
            raise AssertionError("Construction produced an infeasible observation fibre")
        decoder[code] = common & -common
    return {"cyclic_block_count": count, "blocks": blocks, "tests": pools,
            "minimum_tests": len(pools), "fibres": fibres, "decoder": decoder}


def solve(data):
    sets = data.get("acceptable_actions")
    if not isinstance(sets, list) or not sets:
        raise ValueError("acceptable_actions must be a nonempty list")
    n = len(sets)
    include_empty = "empty_actions" in data
    if include_empty:
        sets = sets + [data["empty_actions"]]
    if any(not isinstance(g, list) or not g or
           any(not isinstance(a, str) for a in g) for g in sets):
        raise ValueError("Each state needs a nonempty list of string action names")
    names = sorted({a for g in sets for a in g})
    bits = {a: 1 << i for i, a in enumerate(names)}
    masks = [sum(bits[a] for a in set(g)) for g in sets]
    result = optimal_design(masks, n)

    def state_name(v):
        return "empty" if v == n else v + 1

    def code_name(code):
        return "".join(str((code >> j) & 1) for j in range(result["minimum_tests"]))

    return {
        "promise": "at-most-one-defect" if include_empty else "exactly-one-defect",
        "state_order": [state_name(v) for v in range(len(masks))],
        "acceptable_actions": sets[:n],
        **({"empty_actions": sets[-1]} if include_empty else {}),
        "cyclic_block_count": result["cyclic_block_count"],
        "compatible_blocks": [[state_name(v) for v in block] for block in result["blocks"]],
        "minimum_tests": result["minimum_tests"],
        "tests": [[a + 1, b + 1] for a, b in result["tests"]],
        "decoder": {code_name(code): names[bit.bit_length() - 1]
                    for code, bit in sorted(result["decoder"].items())},
        "observation_fibres": {
            code_name(code): [state_name(v) for v in fibre["states"]]
            for code, fibre in sorted(result["fibres"].items())},
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON file, or - for standard input")
    args = parser.parse_args()
    if args.input == "-":
        data = json.load(sys.stdin)
    elif args.input:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    else:
        data = {"acceptable_actions": [["a", "b"], ["b", "c"], ["a", "c"]]}
    print(json.dumps(solve(data), ensure_ascii=False, indent=2))
