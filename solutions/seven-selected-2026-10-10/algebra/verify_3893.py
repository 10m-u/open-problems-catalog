#!/usr/bin/env python3
"""Exact original-basis kernel/cokernel certificates for problem 3893."""

from collections import defaultdict
from itertools import combinations
from math import comb
from random import Random


class Quotient:
    """Squarefree monomials are bit masks: x first, then y."""

    def __init__(self, n, edges):
        self.n = n
        self.xmask = (1 << n) - 1
        self.edges = tuple((1 << i) | (1 << j) for i, j in edges)

    def survives(self, mask):
        x = mask & self.xmask
        y = mask >> self.n
        return not (x & y) and not any(x & e == e for e in self.edges)

    def multiply(self, a, b):
        out = defaultdict(int)
        for u, c in a.items():
            for v, d in b.items():
                if not (u & v) and self.survives(u | v):
                    out[u | v] += c * d
        return {u: c for u, c in out.items() if c}

    def linear(self, terms):
        out = defaultdict(int)
        for variable, coefficient in terms:
            out[1 << variable] += coefficient
        return {u: c for u, c in out.items() if c}

    def derivative_sum(self, a):
        out = defaultdict(int)
        for u, c in a.items():
            for j in range(2 * self.n):
                if u >> j & 1:
                    out[u ^ (1 << j)] += c
        return {u: c for u, c in out.items() if c}

    def shear(self, a, sign=-1):
        out = defaultdict(int)
        for mask, coefficient in a.items():
            term = {mask & self.xmask: coefficient}
            for j in range(self.n):
                if mask >> (self.n + j) & 1:
                    factor = self.linear(((self.n + j, 1), (j, sign)))
                    term = self.multiply(term, factor)
            for u, c in term.items():
                out[u] += c
        return {u: c for u, c in out.items() if c}


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def check_certificates(n, edges, triple):
    q = Quotient(n, edges)
    assert len(triple) == 3
    assert q.survives(sum(1 << i for i in triple))
    d = (n + 1) // 2
    L = q.linear((j, 1) for j in range(2 * n))
    P = {0: 1}
    for j in range(n // 2):
        a, b = 2 * j, 2 * j + 1
        factor = q.linear(((a, 1), (n + a, 1), (b, -1), (n + b, -1)))
        P = q.multiply(P, factor)
    if n % 2:
        P = q.multiply(P, q.linear(((n - 1, 1), (2 * n - 1, 1))))
    assert P and all(mask.bit_count() == d for mask in P)
    assert any(not (mask & q.xmask) and abs(c) == 1 for mask, c in P.items())
    assert not q.multiply(L, P)

    complement = [j for j in range(n) if j not in triple]
    Q = {0: 1}
    for a, b in zip(complement[::2], complement[1::2]):
        Q = q.multiply(Q, q.linear(((n + a, 1), (n + b, -1))))
    for j in triple:
        Q = q.multiply(Q, q.linear(((j, 1), (n + j, -1))))
    assert Q and all(mask.bit_count() == d + 1 for mask in Q)
    assert all(abs(c) == 1 for c in Q.values())
    assert not q.derivative_sum(Q)

    # Strict block-dimension inequalities, including n=3 and n=4.
    assert choose(n, d) > choose(n, d + 1)
    assert choose(n - 3, d - 3) < choose(n - 3, d - 2)


def check_shear_on_entire_basis(n, edges):
    q = Quotient(n, edges)
    L = q.linear((j, 1) for j in range(2 * n))
    Y = q.linear((j, 1) for j in range(n, 2 * n))
    assert q.shear(L) == Y
    count = 0
    for mask in range(1 << (2 * n)):
        if not q.survives(mask):
            continue
        monomial = {mask: 1}
        transformed = q.shear(monomial)
        assert q.shear(transformed, sign=1) == monomial
        assert q.shear(q.multiply(L, monomial)) == q.multiply(Y, transformed)
        count += 1
    return count


checked_graphs = 0
# Every labelled graph through four vertices with an independent triple.
for n in (3, 4):
    pairs = list(combinations(range(n), 2))
    for code in range(1 << len(pairs)):
        edges = [e for j, e in enumerate(pairs) if code >> j & 1]
        edge_set = set(edges)
        triple = next((c for c in combinations(range(n), 3)
                       if not any(e in edge_set for e in combinations(c, 2))), None)
        if triple is not None:
            check_certificates(n, edges, triple)
            checked_graphs += 1

# Deterministic larger cases: empty graphs, dense graphs with one independent
# triple, and mixed graphs. Every check uses the original x,y quotient.
rng = Random(3893)
for n in range(5, 13):
    triple = (0, 1, 2)
    allowed = [e for e in combinations(range(n), 2)
               if not (e[0] in triple and e[1] in triple)]
    cases = [[], allowed, [e for e in allowed if rng.randrange(2)]]
    for edges in cases:
        check_certificates(n, edges, triple)
        checked_graphs += 1

shear_basis_count = 0
for n, edges in (
    (3, []),
    (4, [(0, 3), (1, 3), (2, 3)]),
    (5, [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]),
    (8, [e for e in combinations(range(8), 2) if not (e[0] < 3 and e[1] < 3)]),
):
    shear_basis_count += check_shear_on_entire_basis(n, edges)

print(f"PASS: exact kernel/cokernel certificates for {checked_graphs} graphs; "
      f"shear inverse and intertwining on {shear_basis_count} basis monomials.")
