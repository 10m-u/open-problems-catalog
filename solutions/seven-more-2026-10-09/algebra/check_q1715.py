#!/usr/bin/env python3
"""Exact independent controls for the 13-dimensional Q1715 counterexample.

Python standard library only. No numerical rank decisions are used.
The all-generating-pairs argument is a theorem in Q1715.md, not an inference
from the finitely many generator pairs checked here.
"""

from fractions import Fraction
from itertools import product
import json


NAMES = "x y z u v a b c p q r s w".split()
N = len(NAMES)
DEGREE = [1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5]
INDEX = {name: i for i, name in enumerate(NAMES)}
ZERO = (0,) * N


def vector(**coefficients):
    out = [0] * N
    for name, coefficient in coefficients.items():
        out[INDEX[name]] = coefficient
    return tuple(out)


TABLE = {}


def put(left, right, **coefficients):
    value = vector(**coefficients)
    TABLE[INDEX[left], INDEX[right]] = value
    TABLE[INDEX[right], INDEX[left]] = tuple(-a for a in value)


put("x", "y", z=1)
put("x", "z", u=1)
put("y", "z", v=1)
put("x", "u", a=1)
put("x", "v", b=1)
put("y", "u", b=1)
put("y", "v", c=1)
put("x", "a", p=1)
put("x", "b", q=1)
put("x", "c", r=1, w=1)
put("y", "a", q=1)
put("y", "b", r=1)
put("y", "c", s=1)
put("z", "v", w=1)

BASIS = [tuple(int(i == j) for i in range(N)) for j in range(N)]


def add(*vectors):
    return tuple(sum(values) for values in zip(*vectors))


def scale(c, v):
    return tuple(c * a for a in v)


def bracket(a, b):
    out = [0] * N
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    for k, c in enumerate(TABLE.get((i, j), ZERO)):
                        out[k] += ai * bj * c
    return tuple(out)


def rref(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return a, []
    pivots = []
    row = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(row, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x / divisor for x in a[row]]
        for r in range(len(a)):
            if r != row and a[r][col]:
                multiple = a[r][col]
                a[r] = [x - multiple * y for x, y in zip(a[r], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots


def rank(matrix):
    return len(rref(matrix)[1])


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    answer = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            answer *= -1
        value = a[col][col]
        answer *= value
        for r in range(col + 1, n):
            multiple = a[r][col] / value
            a[r] = [x - multiple * y for x, y in zip(a[r], a[col])]
    assert answer.denominator == 1
    return int(answer)


def columns_to_rows(columns, rows):
    return [[column[row] for column in columns] for row in rows]


def f_matrix(x, y, input_indices, output_indices):
    columns = []
    for position in range(3):
        for index in input_indices:
            a, b, c = [ZERO] * 3
            if position == 0:
                a = BASIS[index]
            elif position == 1:
                b = BASIS[index]
            else:
                c = BASIS[index]
            first = add(bracket(x, a), bracket(y, b))
            second = add(bracket(x, b), bracket(y, c))
            columns.append(first + second)
    rows = list(output_indices) + [N + i for i in output_indices]
    return columns_to_rows(columns, rows)


def span_basis(vectors):
    rows, _ = rref(vectors)
    return [tuple(row) for row in rows if any(row)]


def check():
    # Every ordered basis triple, including repeated indices, is checked.
    for a, b, c in product(BASIS, repeat=3):
        assert add(bracket(a, bracket(b, c)), bracket(b, bracket(c, a)),
                   bracket(c, bracket(a, b))) == ZERO
    for (i, j), value in TABLE.items():
        for k, coefficient in enumerate(value):
            assert not coefficient or DEGREE[k] == DEGREE[i] + DEGREE[j]

    lower = [BASIS]
    while lower[-1]:
        lower.append(span_basis(bracket(a, b) for a in BASIS for b in lower[-1]))
    lower_dimensions = [len(space) for space in lower]
    assert lower_dimensions == [13, 11, 10, 8, 5, 0]

    # The centralizer of all basis elements computes the center without assuming
    # that the displayed degree-five vectors are the whole center.
    center_matrix = []
    for a in BASIS:
        columns = [bracket(a, b) for b in BASIS]
        center_matrix.extend(columns_to_rows(columns, range(N)))
    center_dimension = N - rank(center_matrix)
    assert center_dimension == 5

    x, y = BASIS[:2]
    certificates = []
    for degree in [2, 3, 4]:
        inputs = [i for i in range(N) if DEGREE[i] == degree]
        outputs = [i for i in range(N) if DEGREE[i] == degree + 1]
        matrix = f_matrix(x, y, inputs, outputs)
        selected_rows = rref(list(map(list, zip(*matrix))))[1]
        minor = [matrix[i] for i in selected_rows]
        value = determinant(minor)
        assert rank(matrix) == 3 * len(inputs)
        assert abs(value) == 1
        certificates.append({
            "input_degree": degree,
            "matrix": matrix,
            "shape": [len(matrix), len(matrix[0])],
            "rank": rank(matrix),
            "minor_row_indices_zero_based": selected_rows,
            "minor_determinant": value,
        })

    # A concrete control with both a nontrivial GL_2 change and higher-degree
    # perturbations. The proof handles all such pairs using its filtration lemma.
    perturbed_x = add(scale(2, x), y, BASIS[2], BASIS[5])
    perturbed_y = add(x, y, BASIS[3], BASIS[6])
    control_matrix = f_matrix(perturbed_x, perturbed_y, range(2, N), range(N))
    assert rank(control_matrix) == 18  # Kernel has dimension 3*dim Z = 15.

    # Negative control: deleting w gives the class-five metabelian quotient.
    # The explicit triple (c,-b,a) is a noncentral solution in that quotient.
    a, b, c = BASIS[5:8]
    first = add(bracket(x, c), bracket(y, scale(-1, b)))
    second = add(bracket(x, scale(-1, b)), bracket(y, a))
    assert first == BASIS[12] and second == ZERO

    return {
        "problem": "Q1715",
        "arithmetic": "exact integers and fractions; Python standard library",
        "dimension": N,
        "graded_dimensions": [DEGREE.count(i) for i in range(1, 6)],
        "ordered_jacobi_triples_verified": N ** 3,
        "lower_central_dimensions": lower_dimensions,
        "nilpotency_class": 5,
        "center_dimension": center_dimension,
        "property_f_graded_certificates": certificates,
        "perturbed_generator_control_rank": rank(control_matrix),
        "negative_control": "In the further quotient w=0, (c,-b,a) is noncentral and solves both equations.",
        "result": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
