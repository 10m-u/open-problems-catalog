#!/usr/bin/env python3
"""Exact finite controls for Q3569; the general proof is in the companion note.

Greedy maxima are computed by integer division. Membership is computed from
integer remainders, independently of the lexicographic suffix criterion.
"""

from itertools import product
import json
from pathlib import Path


def words(alphabet_size, maximum_length):
    return [
        word for length in range(maximum_length + 1)
        for word in product(range(alphabet_size), repeat=length)
    ]


def greedy_maximum(place_values, length):
    remainder = place_values[length] - 1
    digits = []
    for index in reversed(range(length)):
        digit, remainder = divmod(remainder, place_values[index])
        digits.append(digit)
    assert remainder == 0
    return tuple(digits)


def numeric_membership(place_values, word):
    remainder = 0
    for index, digit in enumerate(reversed(word)):
        remainder += digit * place_values[index]
        if remainder >= place_values[index + 1]:
            return False
    return True


def suffix_membership(maxima, word):
    return all(word[-k:] <= maxima[k] for k in range(1, len(word) + 1))


def main():
    test_words = words(4, 5)
    prefix_count = 0
    suffix_checks = 0
    local_equivalence_checks = 0
    membership_comparisons = 0
    positive_properties = 0
    negative_properties = 0
    examples = {}

    # Every such finite prefix extends to a positional system over {0,1,2,3}
    # by putting U[n+1] = 4 U[n] thereafter.
    for increments in product((1, 2, 3), repeat=6):
        values = [1]
        for increment in increments:
            values.append(values[-1] + increment)
        maxima = [greedy_maximum(values, k) for k in range(7)]
        assert maxima[0] == ()
        prefix_count += 1

        for word in test_words:
            numeric = numeric_membership(values, word)
            lexical = suffix_membership(maxima, word)
            assert numeric == lexical, (values, word, numeric, lexical)
            suffix_checks += 1

        for p in (1, 2, 3, 4):
            bound = 6 - p
            prefix_property = all(
                maxima[k + p][:k] == maxima[k]
                for k in range(bound + 1)
            )
            extension_property = True
            first_obstruction = None
            for word in test_words:
                if len(word) > bound:
                    continue
                before = numeric_membership(values, word)
                after = numeric_membership(values, word + (0,) * p)
                membership_comparisons += 1
                if before != after:
                    extension_property = False
                    first_obstruction = list(word)
                    break
            assert extension_property == prefix_property, (
                values, p, bound, first_obstruction
            )
            local_equivalence_checks += 1
            if extension_property:
                positive_properties += 1
            else:
                negative_properties += 1
            key = f"p={p}, holds={extension_property}"
            examples.setdefault(key, {
                "place_values": values,
                "maximum_word_length": bound,
                "first_obstruction": first_obstruction,
            })

    # A complete example with period two but not period one.
    alternating_values = [
        6 ** (n // 2) * (2 if n % 2 else 1) for n in range(11)
    ]
    alternating_maxima = [
        greedy_maximum(alternating_values, k) for k in range(11)
    ]
    for k, actual in enumerate(alternating_maxima):
        expected = ((1,) if k % 2 else ()) + (2, 1) * (k // 2)
        assert actual == expected, (k, actual, expected)
    alternating_extension_checks = 0
    for word in words(3, 8):
        assert numeric_membership(alternating_values, word) == (
            numeric_membership(alternating_values, word + (0, 0))
        ), word
        alternating_extension_checks += 1
    assert not numeric_membership(alternating_values, (2,))
    assert numeric_membership(alternating_values, (2, 0))

    # The two periodic infinite words swap under odd shifts.
    periodic_prefix = {0: (2, 1) * 30, 1: (1, 2) * 30}
    shift_checks = 0
    for residue in (0, 1):
        for shift in range(31):
            assert periodic_prefix[residue][shift:shift + 30] == (
                periodic_prefix[(residue - shift) % 2][:30]
            )
            shift_checks += 1

    report = {
        "all_passed": True,
        "finite_place_value_prefixes": prefix_count,
        "prefix_length_including_U0": 7,
        "increments_enumerated": [1, 2, 3],
        "alphabet": [0, 1, 2, 3],
        "p_values": [1, 2, 3, 4],
        "numeric_vs_suffix_checks": suffix_checks,
        "finite_equivalence_checks": local_equivalence_checks,
        "membership_comparisons_for_equivalence": membership_comparisons,
        "positive_finite_properties": positive_properties,
        "negative_finite_properties": negative_properties,
        "alternating_example": {
            "place_values": alternating_values,
            "maximal_words": [list(word) for word in alternating_maxima],
            "two_zero_extension_checks": alternating_extension_checks,
            "one_zero_counterexample": {"word": [2], "extended_word": [2, 0]},
            "periodic_shift_checks": shift_checks,
        },
        "representative_finite_cases": examples,
        "scope": "Finite indexing controls, not a substitute for the infinite proof.",
    }
    destination = Path(__file__).with_name("periodic-zero-checks.json")
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        key: value for key, value in report.items()
        if key not in {"representative_finite_cases", "alternating_example"}
    }, indent=2))
    print(json.dumps({
        "alternating_two_zero_extension_checks": alternating_extension_checks,
        "alternating_periodic_shift_checks": shift_checks,
        "one_zero_counterexample_verified": True,
    }, indent=2))


if __name__ == "__main__":
    main()
