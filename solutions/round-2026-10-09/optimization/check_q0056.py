#!/usr/bin/env python3
"""Exact finite controls for the Q56 reduction; not the NP-hardness proof itself."""
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import isqrt, prod
from pathlib import Path
import json


def check_instance(values):
    total = prod(values)
    root = isqrt(total)
    square = root * root == total
    entries = {}
    witnesses = []
    for bits in product((0, 1), repeat=len(values)):
        first = prod(Fraction(1, a) if bit else Fraction(1)
                     for a, bit in zip(values, bits))
        second = prod(Fraction(1) if bit else Fraction(1, a)
                      for a, bit in zip(values, bits))
        entry = (first + second) / 2
        selected = prod(a for a, bit in zip(values, bits) if bit)
        complement = prod(a for a, bit in zip(values, bits) if not bit)
        assert selected * complement == total
        assert entry == Fraction(selected + complement, 2 * total)
        entries[bits] = entry
        if selected == complement:
            witnesses.append(bits)
    optimum = min(entries.values())
    cmax = max(entries.values())
    assert cmax == Fraction(total + 1, 2 * total)
    assert Fraction(1, 2) <= cmax <= 1
    for bits, value in entries.items():
        reflected = tuple(1 - bit for bit in bits)
        assert value == entries[reflected]
        # Each reflected pair has exactly uniform marginal mass in every mode.
        assert all(Fraction(a + b, 2) == Fraction(1, 2)
                   for a, b in zip(bits, reflected))
    if square:
        eps = Fraction(1, 8 * total)
        threshold = Fraction(1, root) + Fraction(1, 4 * total)
        assert cmax / eps == 4 * (total + 1)
        if witnesses:
            assert optimum == Fraction(1, root)
            assert optimum + eps < threshold
        else:
            assert optimum >= Fraction(1, root) + Fraction(1, 2 * total)
            assert optimum - eps > threshold
    else:
        assert not witnesses
    return len(entries), square, bool(witnesses), str(optimum)


def main():
    counts = {"instances": 0, "tensor_entries": 0, "square_products": 0,
              "yes_instances": 0, "square_no_instances": 0,
              "nonsquare_no_instances": 0}
    for length in range(1, 7):
        for values in combinations_with_replacement(range(1, 9), length):
            entries, square, yes, _ = check_instance(values)
            counts["instances"] += 1
            counts["tensor_entries"] += entries
            counts["square_products"] += square
            counts["yes_instances"] += yes
            counts["square_no_instances"] += square and not yes
            counts["nonsquare_no_instances"] += not square
    examples = {}
    for values in [(2, 3, 6), (2, 2, 9), (1,), (2,), (4,)]:
        _, square, yes, minimum = check_instance(values)
        examples[str(values)] = {"square_product": square,
                                 "partition_exists": yes, "minimum": minimum}
    result = {"problem": "Q56", "arithmetic": "exact rational/integer",
              "domain": "all nondecreasing lists of length 1..6 over 1..8",
              "checks": counts, "examples": examples,
              "result": "all assertions passed",
              "scope": "finite controls for the written general reduction"}
    target = Path(__file__).with_name("q0056-checks.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
