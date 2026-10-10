#!/usr/bin/env python3
"""Exact finite-alphabet enumeration for twice-hare-sortable words.

This supplies a general finite-state counting algorithm and the four-letter
rational slice; it does not claim a closed unrestricted generating function.
Python standard library only.
"""

import argparse
import json
from math import comb
from pathlib import Path


FOUR_TRANSITIONS = [
    [0, 1, 2, 0],
    [1, 1, 3, 1],
    [2, 3, 2, 0],
    [3, 3, 3, 4],
    [5, 4, 4, 4],
    [5, 5, 5, 5],
]


def feed(second, last, value):
    """Feed one distinct value to a compressed second stack."""
    lower = second & ((1 << value) - 1)
    if lower:
        if (lower & -lower).bit_length() - 1 < last:
            return None
        last = lower.bit_length() - 1
    return (second & ~((1 << value) - 1)) | (1 << value), last


def transition(state, value):
    if state is None:
        return None
    first, second, last = state
    for popped in range(value):
        if first >> popped & 1:
            result = feed(second, last, popped)
            if result is None:
                return None
            second, last = result
    first = (first & ~((1 << value) - 1)) | (1 << value)
    return first, second, last


def accepting(state, alphabet_size):
    if state is None:
        return False
    first, second, last = state
    for popped in range(alphabet_size):
        if first >> popped & 1:
            result = feed(second, last, popped)
            if result is None:
                return False
            second, last = result
    return not second or (second & -second).bit_length() - 1 >= last


def automaton(alphabet_size):
    states = [(0, 0, -1)]
    indices = {states[0]: 0}
    rows = []
    accept = []
    for state in states:
        accept.append(accepting(state, alphabet_size))
        row = []
        for value in range(alphabet_size):
            result = transition(state, value)
            if result is not None and result not in indices:
                indices[result] = len(states)
                states.append(result)
            row.append(indices[result] if result is not None else -1)
        rows.append(row)
    return states, rows, accept


def counts(alphabet_size, largest_length):
    states, rows, accept = automaton(alphabet_size)
    distribution = [0] * len(states)
    distribution[0] = 1
    result = []
    for _ in range(largest_length + 1):
        result.append(sum(count for count, good in zip(distribution, accept) if good))
        following = [0] * len(states)
        for count, row in zip(distribution, rows):
            if count:
                for successor in row:
                    if successor >= 0:
                        following[successor] += count
        distribution = following
    return result, len(states)


def four_letter_quotient_certificate():
    states, _, _ = automaton(4)
    mapping = {(0, 0, -1): 0}
    queue = [(0, 0, -1)]
    for state in queue:
        small = mapping[state]
        assert accepting(state, 4) == (small != 5)
        for value in range(4):
            successor = transition(state, value)
            small_successor = FOUR_TRANSITIONS[small][value]
            if successor not in mapping:
                mapping[successor] = small_successor
                queue.append(successor)
            assert mapping[successor] == small_successor
    assert len(mapping) == len(states) + 1
    return [{"compressed_state": list(state) if state is not None else None,
             "four_letter_state": small} for state, small in mapping.items()]


def build_certificate(max_length):
    table, state_counts = [], []
    for k in range(max_length + 1):
        values, number_of_states = counts(k, max_length)
        table.append(values)
        state_counts.append(number_of_states)
    exact_maximum = [[sum((-1) ** (k - j) * comb(k, j) * table[j][n]
                         for j in range(k + 1))
                      for k in range(n + 1)]
                     for n in range(max_length + 1)]
    total = [sum(row[1:]) for row in exact_maximum]
    known = [1, 3, 13, 73, 483, 3547, 27939, 231395]
    assert total[1:min(max_length, 8) + 1] == known[:max_length]
    four_counts, _ = counts(4, 30)
    exactly_four = [four_counts[n] - 4 * 3 ** n + 6 * 2 ** n - 4
                    + int(n == 0) for n in range(31)]
    return {
        "problem": "Q3480",
        "date": "2026-10-09",
        "scope": "Finite-alphabet rational enumeration; unrestricted question remains open",
        "largest_length_general_table": max_length,
        "counts_F_k_n_rows_k_columns_n": table,
        "reachable_compressed_state_counts": state_counts,
        "counts_by_exact_maximum_rows_n_columns_k": exact_maximum,
        "cayley_totals_n_1_onward": total[1:],
        "four_letter_transition_table_columns_1_2_3_4": FOUR_TRANSITIONS,
        "four_letter_quotient_map": four_letter_quotient_certificate(),
        "four_letter_counts_n_0_through_30": four_counts,
        "exactly_four_symbol_counts_n_0_through_30": exactly_four,
        "F4_numerator_ascending": [1, -9, 30, -42, 19],
        "F4_denominator_ascending": [1, -13, 66, -162, 189, -81],
        "exactly_four_numerator_ascending": [0, 0, 0, 0, 22, -119, 162],
        "exactly_four_denominator_ascending": [1, -15, 92, -294, 513, -459, 162],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-length", type=int, default=8,
                        help="Largest unrestricted length; automata grow exponentially in the alphabet.")
    arguments = parser.parse_args()
    if arguments.max_length < 1:
        parser.error("--max-length must be positive")
    certificate = build_certificate(arguments.max_length)
    destination = Path(__file__).with_name("q3480_certificate.json")
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Q3480 Cayley counts:", certificate["cayley_totals_n_1_onward"])
    print("The four-letter quotient has 5 accepting states and 1 rejecting sink.")
    print(f"Wrote {destination.name}")
