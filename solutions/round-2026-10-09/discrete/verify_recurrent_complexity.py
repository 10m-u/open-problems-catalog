#!/usr/bin/env python3
"""Independent finite controls for the explicit Q1653 counterexample.

The proof is in Q1653-recurrent-complexity-counterexample.md. This script
enumerates actual binary words and all possible recurrent right-extension
rules relevant to the length-2/3/4 obstruction. No third-party packages.
"""

from itertools import combinations, product
import json
from pathlib import Path


def words(n):
    return ("".join(bits) for bits in product("01", repeat=n))


def in_explicit_language(word):
    # A word belongs to 0*1* exactly when no 0 follows any 1.
    seen_one = False
    for letter in word:
        if letter == "1":
            seen_one = True
        elif seen_one:
            return word == "10"
    return True


FORBIDDEN = ("010", "100", "101", "110")


def in_avoidance_language(word):
    return all(pattern not in word for pattern in FORBIDDEN)


def main():
    counts = []
    membership_checks = 0
    factor_checks = 0
    for n in range(15):
        accepted = []
        for word in words(n):
            explicit = in_explicit_language(word)
            assert explicit == in_avoidance_language(word), word
            membership_checks += 1
            if explicit:
                accepted.append(word)
                for left in range(n + 1):
                    for right in range(left, n + 1):
                        assert in_explicit_language(word[left:right]), (
                            word, left, right
                        )
                        factor_checks += 1
        expected = 1 if n == 0 else (4 if n == 2 else n + 1)
        assert len(accepted) == expected, (n, accepted, expected)
        counts.append({"length": n, "count": len(accepted)})

    bigrams = set(words(2))
    trigrams = list(words(3))
    tetragrams = list(words(4))
    candidates = []
    for choice in combinations(trigrams, 4):
        recurrent_trigrams = set(choice)
        if {word[:2] for word in choice} != bigrams:
            continue
        # Every recurrent tetragram has both contiguous trigrams recurrent.
        compatible = [
            word for word in tetragrams
            if word[:3] in recurrent_trigrams
            and word[1:] in recurrent_trigrams
        ]
        assert len(compatible) == 4, (choice, compatible)
        candidates.append({
            "trigrams": list(choice),
            "compatible_tetragrams": compatible,
        })
    assert len(candidates) == 16
    report = {
        "all_passed": True,
        "max_length_enumerated": 14,
        "membership_checks": membership_checks,
        "factor_closure_checks": factor_checks,
        "complexity_counts": counts,
        "right_extension_rules_checked": len(candidates),
        "compatible_tetragram_counts": sorted({
            len(row["compatible_tetragrams"]) for row in candidates
        }),
        "right_extension_rule_details": candidates,
        "scope": "Finite controls; the infinite impossibility is proved in the note.",
    }
    destination = Path(__file__).with_name("recurrent-complexity-checks.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        key: value for key, value in report.items()
        if key != "right_extension_rule_details"
    }, indent=2))


if __name__ == "__main__":
    main()
