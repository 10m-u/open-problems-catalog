"""Exact dyadic wrong-model and residue-automaton controls."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ZERO = (F(0), 0)
ONE = (F(0), 1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def scale(x, n):
    return (x[0] * n, x[1] * n)


def power(t):
    return F(2) ** t


def valuation_number(a):
    if not a:
        return 0
    a = F(abs(a))
    numerator = a.numerator
    count = 0
    while numerator % 2 == 0:
        numerator //= 2
        count += 1
    return power(count - (a.denominator.bit_length() - 1))


def val(x):
    if x == ZERO:
        return ZERO
    if x[1]:
        return (F(0), int(valuation_number(x[1])))
    return (valuation_number(x[0]), 0)


def digit(x, level, top=False):
    if not top:
        return (x[1] // (1 << level)) % 2
    ratio = x[0] / power(level)
    quotient = ratio.numerator // ratio.denominator
    if ratio.denominator == 1 and x[1] < 0:
        quotient -= 1
    return quotient % 2


def boolean(x, y, op):
    tail = op(int(x[1] < 0), int(y[1] < 0))
    a = tail * power(-8) + sum(op(digit(x, j, True), digit(y, j, True)) * power(j)
                                  for j in range(-8, 9))
    b = sum(op(digit(x, j), digit(y, j)) * (1 << j) for j in range(10)) - tail * (1 << 10)
    return (a, b)


def main():
    grid = [(F(n, 8), b) for n in range(25) for b in range(-4, 5)
            if (F(n, 8), b) >= ZERO]
    single_checks = pair_checks = 0
    for x in grid:
        assert val(scale(x, 2)) == scale(val(x), 2)
        assert val(val(x)) == val(x)
        quotient, remainder = (x[0] / 2, x[1] // 2), x[1] % 2
        assert quotient >= ZERO and add(scale(quotient, 2), scale(ONE, remainder)) == x
        if x > ZERO:
            z = add(x, scale(val(x), -1))
            assert z >= ZERO and (z == ZERO or val(z) > val(x))
            if x[0] == 0:
                d = (F(0), 1 << (x[1].bit_length() - 1))
            else:
                t = 0
                while power(t + 1) <= x[0]:
                    t += 1
                while power(t) > x[0]:
                    t -= 1
                d = (power(t), 0)
                if d > x:
                    d = (d[0] / 2, 0)
            assert val(d) == d and d <= x < scale(d, 2)
        single_checks += 1
    for x, y in product(grid, repeat=2):
        if x > ZERO and y > ZERO and val(x) < val(y):
            assert val(add(x, y)) == val(x)
        if x <= y:
            assert add(y, scale(x, -1)) >= ZERO
        pair_checks += 1

    small = [(a, b) for a in [F(0), F(1, 8), F(1, 2), F(1), F(2), F(3)]
             for b in range(-4, 5) if (a, b) >= ZERO]
    bool_checks = 0
    for x, y in product(small, repeat=2):
        inter = boolean(x, y, lambda u,v: u & v)
        union = boolean(x, y, lambda u,v: u | v)
        xor = boolean(x, y, lambda u,v: u ^ v)
        assert inter >= ZERO and union >= ZERO and xor >= ZERO
        assert boolean(x, x, lambda u,v: u ^ v) == ZERO
        assert boolean(inter, union, lambda u,v: u & v) == inter
        for j in range(10):
            assert digit(scale(x, 2), j) == (digit(x, j - 1) if j else 0)
        for j in range(-7, 9):
            assert digit(scale(x, 2), j, True) == digit(x, j - 1, True)
        bool_checks += 1
    for j in range(100):
        assert ((1 << j) - 1) % 3 == (0 if j % 2 == 0 else 1)
    for t in range(-30, 31):
        assert (power(t) / 3).denominator % 3 == 0

    residue_checks = 0
    for k in [2, 3, 4, 5, 6]:
        for r in [7, 11, 13, 17]:
            if r == k:
                continue
            # The normalized LSD remainder transition is (state+digit)/k.
            inv = pow(k, -1, r)
            states = {0}
            while True:
                new = states | {(s + a) * inv % r for s in states for a in range(k)}
                if new == states:
                    break
                states = new
            assert len(states) == r
            for a, b in product(states, repeat=2):
                if a != b:
                    suffix_value = (-a) % r
                    assert (a + suffix_value) % r == 0
                    assert (b + suffix_value) % r != 0
                    residue_checks += 1
    receipt = dict(status="passed", grid_elements=len(grid), core_single_checks=single_checks,
                   core_pair_checks=pair_checks, boolean_shift_checks=bool_checks,
                   alternating_finite_atoms=100, infinite_atom_nondivision_controls=61,
                   residue_distinctions=residue_checks,
                   scope="bounded exact controls; no finite-axiomatizability decision")
    Path(__file__).with_name("Q1377-CHECK-RESULTS.json").write_text(json.dumps(receipt, indent=2)+"\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
