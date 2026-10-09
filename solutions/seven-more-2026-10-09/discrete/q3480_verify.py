#!/usr/bin/env python3
"""Independent exact controls for Q3480; imports no enumeration code."""

from collections import deque
from itertools import product
import json
from pathlib import Path


def hare(word):
    stack, output = [], []
    for value in word:
        while stack and stack[-1] < value:
            output.append(stack.pop())
        stack.append(value)
    output.extend(reversed(stack))
    return output


def literal_accepts(word):
    output = hare(hare(word))
    return all(a <= b for a, b in zip(output, output[1:]))


def compact_accepts(word, transitions):
    state = 0
    for value in word:
        state = transitions[state][value]
    return state != 5


def poly_multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def poly_add(a, b, multiplier=1):
    result = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        result[i] += x
    for i, x in enumerate(b):
        result[i] += multiplier * x
    return result


def series(numerator, denominator, length):
    assert denominator[0] == 1
    result = []
    for n in range(length):
        value = numerator[n] if n < len(numerator) else 0
        value -= sum(denominator[j] * result[n - j]
                     for j in range(1, min(n + 1, len(denominator))))
        result.append(value)
    return result


def tuple_step(first, second, last, x):
    """Reconstruct a certificate transition using tuples, not bit operations."""
    first, second = list(first), list(second)
    while first and first[0] < x:
        value = first.pop(0)
        while second and second[0] < value:
            popped = second.pop(0)
            if popped < last:
                return None
            last = popped
        if value not in second:
            second.insert(0, value)
    if x not in first:
        first.insert(0, x)
    return first, second, last


def encode(state):
    if state is None:
        return None
    first, second, last = state
    return (sum(2 ** i for i in first), sum(2 ** i for i in second), last)


def main():
    certificate = json.loads(Path(__file__).with_name("q3480_certificate.json").read_text())
    transitions = certificate["four_letter_transition_table_columns_1_2_3_4"]
    quotient = {tuple(entry["compressed_state"]) if entry["compressed_state"] is not None else None:
                entry["four_letter_state"] for entry in certificate["four_letter_quotient_map"]}
    assert quotient[(0, 0, -1)] == 0 and quotient[None] == 5
    assert len(quotient) == 175
    checked_transitions = 0
    for state, small in quotient.items():
        first = [] if state is None else [i for i in range(4) if state[0] // (2 ** i) % 2]
        second = [] if state is None else [i for i in range(4) if state[1] // (2 ** i) % 2]
        last = -1 if state is None else state[2]
        # Flush uses literal lists, which also independently verifies acceptance.
        output = []
        if state is not None:
            second_stack = list(reversed(second))
            for value in first:
                while second_stack and second_stack[-1] < value:
                    output.append(second_stack.pop())
                second_stack.append(value)
            output.extend(reversed(second_stack))
            accepted = all(a <= b for a, b in zip([last] + output, output))
        else:
            accepted = False
        assert accepted == (small != 5)
        for x in range(4):
            successor = None if state is None else encode(tuple_step(first, second, last, x))
            assert quotient[successor] == transitions[small][x]
            checked_transitions += 1
    # Every supplied state is reachable, so the finite certificate is exhaustive.
    reached, queue = {(0, 0, -1)}, deque([(0, 0, -1)])
    while queue:
        state = queue.popleft()
        if state is None:
            continue
        first = [i for i in range(4) if state[0] // (2 ** i) % 2]
        second = [i for i in range(4) if state[1] // (2 ** i) % 2]
        for x in range(4):
            successor = encode(tuple_step(first, second, state[2], x))
            if successor not in reached:
                reached.add(successor)
                queue.append(successor)
    assert reached == set(quotient)

    # Independent literal full-multiplicity words: 87,381 cases over four letters.
    word_count = 0
    for n in range(9):
        accepted = 0
        for word in product(range(4), repeat=n):
            literal = literal_accepts(word)
            assert literal == compact_accepts(word, transitions)
            accepted += literal
            word_count += 1
        assert accepted == certificate["four_letter_counts_n_0_through_30"][n]

    numerator = certificate["F4_numerator_ascending"]
    denominator = certificate["F4_denominator_ascending"]
    assert series(numerator, denominator, 31) == certificate["four_letter_counts_n_0_through_30"]
    # A matrix polynomial identity certifies the rational recurrence for ALL n.
    matrix = [[sum(successor == j for successor in row) for j in range(5)]
              for row in transitions[:5]]
    identity = [[int(i == j) for j in range(5)] for i in range(5)]
    powers = [identity]
    for _ in range(5):
        powers.append([[sum(powers[-1][i][k] * matrix[k][j] for k in range(5))
                        for j in range(5)] for i in range(5)])
    assert all(sum(denominator[r] * powers[5 - r][i][j] for r in range(6)) == 0
               for i in range(5) for j in range(5))

    # Verify the exact rational inclusion-exclusion identity, coefficient by coefficient.
    cube = poly_multiply(poly_multiply([1, -3], [1, -3]), [1, -3])
    fourth = poly_multiply(cube, [1, -3])
    common = poly_multiply(poly_multiply([1, -1], [1, -2]), fourth)
    surjective_numerator = poly_multiply(numerator, [1, -2])
    surjective_numerator = poly_add(surjective_numerator,
                                   poly_multiply(poly_multiply([1, -1], [1, -2]), cube), -4)
    surjective_numerator = poly_add(surjective_numerator, poly_multiply([1, -1], fourth), 6)
    surjective_numerator = poly_add(surjective_numerator, poly_multiply([1, -2], fourth), -4)
    surjective_numerator = poly_add(surjective_numerator, common)
    assert surjective_numerator == certificate["exactly_four_numerator_ascending"]
    assert common == certificate["exactly_four_denominator_ascending"]
    assert series(surjective_numerator, common, 31) == certificate["exactly_four_symbol_counts_n_0_through_30"]
    assert certificate["cayley_totals_n_1_onward"][:8] == [1, 3, 13, 73, 483, 3547, 27939, 231395]
    assert literal_accepts([2, 3, 1, 3, 0])  # 34241: an equal top value rescues 3241.
    assert not literal_accepts([2, 1, 3, 0])  # 3241.
    print(f"PASS Q3480: {checked_transitions} quotient transitions and all acceptance labels.")
    print(f"PASS Q3480: {word_count} literal two-stack words, including repeated letters.")
    print("PASS Q3480: matrix polynomial and rational inclusion-exclusion identities hold exactly.")
    print("PASS Q3480: all eight primary-source unrestricted coefficients agree.")


if __name__ == "__main__":
    main()
