#!/usr/bin/env python3
"""Exhaustive finite controls for Q2305's all-fields structural theorem.

Reconstructs Inn(M_2(F_p)) directly from the paper's g,h generators for p=2,3,
then independently compares with the proposed rectangular-domain model.
Checks the complete domain semilattice in dimension three over F_2.
Python standard library only; all arithmetic is in exact finite fields.
"""

from itertools import product
import json


def matrix_mul(a, b, n, p):
    return tuple(sum(a[n * i + k] * b[n * k + j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def matrix_vec(a, v, n, p):
    return tuple(sum(a[n * i + k] * v[k] for k in range(n)) % p
                 for i in range(n))


def identity(n):
    return tuple(int(i == j) for i in range(n) for j in range(n))


def subspaces(n, p):
    zero = (0,) * n
    vectors = list(product(range(p), repeat=n))
    seen = {frozenset([zero])}
    queue = list(seen)
    for space in queue:
        for v in vectors:
            if v in space:
                continue
            enlarged = frozenset(tuple((a + c * b) % p for a, b in zip(w, v))
                                 for w in space for c in range(p))
            if enlarged not in seen:
                seen.add(enlarged)
                queue.append(enlarged)
    return sorted(seen, key=lambda s: (len(s), sorted(s)))


def rectangular_domain(matrices, u, w, n, p):
    zero = (0,) * n
    return tuple(index for index, a in enumerate(matrices)
                 if all(tuple(a[n * i + j] for i in range(n)) in u
                        for j in range(n))
                 and all(matrix_vec(a, v, n, p) == zero for v in w))


def direct_domain(a, matrices, n, p):
    return tuple(i for i, b in enumerate(matrices)
                 if matrix_mul(a, b, n, p) == b == matrix_mul(b, a, n, p))


def compose(f, g):
    # Standard function order: f after g. -1 means undefined.
    return tuple(-1 if j < 0 else f[j] for j in g)


def dimension_two(p):
    n = 2
    matrices = list(product(range(p), repeat=4))
    index = {a: i for i, a in enumerate(matrices)}
    unit = index[identity(n)]
    multiplication = [[index[matrix_mul(a, b, n, p)] for b in matrices]
                      for a in matrices]
    gl = [i for i, a in enumerate(matrices) if (a[0] * a[3] - a[1] * a[2]) % p]
    inverse = {a: next(b for b in gl if multiplication[a][b] == unit) for a in gl}

    domains = {t: tuple(a for a in range(len(matrices))
                        if multiplication[t][a] == a == multiplication[a][t])
               for t in range(len(matrices))}
    generators = set()
    for g, h in product(range(len(matrices)), repeat=2):
        out = [-1] * len(matrices)
        for a in domains[multiplication[g][h]]:
            out[a] = multiplication[multiplication[h][a]][g]
        generators.add(tuple(out))
    actual = {tuple(range(len(matrices)))}
    queue = list(actual)
    for current in queue:
        for generator in generators:
            result = compose(generator, current)
            if result not in actual:
                actual.add(result)
                queue.append(result)

    lines = [s for s in subspaces(n, p) if len(s) == p]
    pairs = [(u, w) for u in lines for w in lines]
    domain_list = [tuple(range(len(matrices))), (0,)]
    domain_list.extend(rectangular_domain(matrices, u, w, n, p) for u, w in pairs)
    assert len(set(domain_list)) == (p + 1) ** 2 + 2
    model = set()
    for domain, h in product(domain_list, gl):
        out = [-1] * len(matrices)
        for a in domain:
            out[a] = multiplication[multiplication[h][a]][inverse[h]]
        model.add(tuple(out))
    assert actual == model
    for f, g in product(model, repeat=2):
        assert compose(f, g) in model
    expected = p ** 4 + 4 * p ** 3 + 2 * p ** 2 - 2 * p
    assert len(model) == expected

    # Independent check of the explicit equality quotient. On a nonzero
    # rectangular domain, c acts trivially iff c=scalar*I+N with N(U)=0,
    # image(N) contained in W.
    quotient_checks = 0
    for u, w in pairs:
        domain = rectangular_domain(matrices, u, w, n, p)
        for ci in gl:
            c = matrices[ci]
            direct = all(multiplication[ci][a] == multiplication[a][ci] for a in domain)
            condition = False
            for scalar in range(1, p):
                difference = tuple((a - scalar * b) % p for a, b in zip(c, identity(n)))
                if (all(matrix_vec(difference, v, n, p) == (0,) * n for v in u)
                        and all(tuple(difference[n * i + j] for i in range(n)) in w
                                for j in range(n))):
                    condition = True
            assert direct == condition
            quotient_checks += 1
    return {
        "field_order": p,
        "matrix_count": len(matrices),
        "generator_pairs": len(matrices) ** 2,
        "distinct_generator_maps": len(generators),
        "generated_inverse_monoid_size": len(actual),
        "rectangular_model_size": len(model),
        "predicted_cardinality": expected,
        "domain_count": len(domain_list),
        "all_model_compositions_checked": len(model) ** 2,
        "explicit_quotient_checks": quotient_checks,
    }


def dimension_three_domains():
    n, p = 3, 2
    matrices = list(product(range(p), repeat=n * n))
    all_subspaces = subspaces(n, p)
    proper_nonzero = [s for s in all_subspaces if 1 < len(s) < p ** n]
    def mask(domain):
        return sum(1 << i for i in domain)
    generators = {mask(direct_domain(t, matrices, n, p)) for t in matrices}
    generated = set(generators)
    queue = list(generated)
    for current in queue:
        for domain in generators:
            result = current & domain
            if result not in generated:
                generated.add(result)
                queue.append(result)
    model = {mask(range(len(matrices))), 1}
    model.update(mask(rectangular_domain(matrices, u, w, n, p))
                 for u, w in product(proper_nonzero, repeat=2))
    assert generated == model
    assert len(generators) == 100 and len(model) == 198

    # A nonsemisimple eigenvalue-one control: ker(t-I) meets im(t-I).
    # Both g and h are singular. H is an invertible extension producing the
    # same conjugation on the entire original generator domain.
    t = (1, 1, 0, 0, 1, 0, 0, 0, 0)
    h_projection = (1, 0, 0, 0, 1, 0, 0, 0, 0)
    big_h = (0, 1, 0, 1, 0, 0, 0, 0, 1)  # Its own inverse.
    g = matrix_mul(t, big_h, n, p)
    h = matrix_mul(big_h, h_projection, n, p)
    assert matrix_mul(g, h, n, p) == t
    domain = direct_domain(t, matrices, n, p)
    assert len(domain) == 2
    for ai in domain:
        a = matrices[ai]
        assert matrix_mul(matrix_mul(h, a, n, p), g, n, p) == \
               matrix_mul(matrix_mul(big_h, a, n, p), big_h, n, p)
    return {
        "field_order": p,
        "dimension": n,
        "matrices": len(matrices),
        "all_subspace_count": len(all_subspaces),
        "initial_generator_domain_count": len(generators),
        "intersection_closure_domain_count": len(generated),
        "rectangular_domain_count": len(model),
        "nonsemisimple_singular_generator_control": "PASS",
    }


if __name__ == "__main__":
    print(json.dumps({
        "problem": "Q2305",
        "arithmetic": "exact finite fields; Python standard library",
        "dimension_two": [dimension_two(p) for p in [2, 3]],
        "dimension_three_domain_semilattice": dimension_three_domains(),
        "result": "PASS",
    }, indent=2))
