#!/usr/bin/env python3
"""Exact, dependency-free polynomial checks for the problem 212 example."""


def trim(p):
    p = tuple(p)
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p or (0,)


def add(p, q):
    return trim(
        (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
        for i in range(max(len(p), len(q)))
    )


def neg(p):
    return tuple(-x for x in p)


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def mmul(a, b):
    return tuple(
        tuple(add(mul(a[i][0], b[0][j]), mul(a[i][1], b[1][j]))
              for j in range(2))
        for i in range(2)
    )


def madd(a, b):
    return tuple(tuple(add(a[i][j], b[i][j]) for j in range(2))
                 for i in range(2))


def mneg(a):
    return tuple(tuple(neg(p) for p in row) for row in a)


def mod_t2(a):
    return tuple(tuple(trim(p[:2]) for p in row) for row in a)


Z = (0,)
O = (1,)
IDENTITY = ((O, Z), (Z, O))
ZERO = ((Z, Z), (Z, Z))
E11 = ((O, Z), (Z, Z))
E12 = ((Z, O), (Z, Z))
E21 = ((Z, Z), (O, Z))
E22 = ((Z, Z), (Z, O))

S = (((1, 1), (0, 0, 1)), ((0, 0, -1), (1, -1, 1, -1)))
S_INV = ((S[1][1], neg(S[0][1])), (neg(S[1][0]), S[0][0]))
det = add(mul(S[0][0], S[1][1]), neg(mul(S[0][1], S[1][0])))
assert det == O
assert mmul(S, S_INV) == IDENTITY == mmul(S_INV, S)


def conjugate(a):
    return mmul(mmul(S, a), S_INV)


e = conjugate(E11)
f = madd(IDENTITY, mneg(e))
expected_e = (
    ((1, 0, 0, 0, -1), (0, 0, -1, -1)),
    ((0, 0, -1, 1, -1, 1), (0, 0, 0, 0, 1)),
)
assert e == expected_e
assert f == conjugate(E22)
assert mmul(e, e) == e
assert mmul(f, f) == f
assert mmul(e, f) == ZERO == mmul(f, e)
assert madd(e, f) == IDENTITY
assert all(len(p) < 2 or p[1] == 0 for a in (e, f) for row in a for p in row)
assert mod_t2(conjugate(E11)) == E11
assert mod_t2(conjugate(E22)) == E22
assert mod_t2(conjugate(E12)) == ((Z, (1, 2)), (Z, Z))
assert mod_t2(conjugate(E21)) == ((Z, Z), ((1, -2), Z))

# These two basis cases verify the coefficient condition for arbitrary
# u = u_0 + u_1 t modulo t^2 by linearity.
t_E12 = ((Z, (0, 1)), (Z, Z))
assert mod_t2(conjugate(t_E12)) == t_E12

# A concrete Bezout certificate for B L_{-2}=B:
# (1+2t)(1-2t) + 4t^2 = 1.
assert add(mul((1, 2), (1, -2)), (0, 0, 4)) == O
assert (1, -2)[1] + 2 * (1, -2)[0] == 0

print("PASS: determinant, idempotents, primitive-corner reductions, "
      "cross-corner reductions, and Bezout certificate (exact integers).")
