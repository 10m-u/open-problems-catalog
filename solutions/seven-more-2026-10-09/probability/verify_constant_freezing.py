#!/usr/bin/env python3
"""Exact polynomial certificates for finite constant-freezing percolation.

Uses the Python standard library only. Polynomials are integer coefficient tuples,
in ascending order. No floating point arithmetic enters the certificates.
"""

from functools import lru_cache
from itertools import combinations, permutations, product
from fractions import Fraction
import argparse
import hashlib
import json
import time


def trim(p):
    p = list(p)
    while len(p) > 1 and not p[-1]:
        p.pop()
    return tuple(p)


def add(p, q):
    r = list(p) + [0] * max(0, len(q) - len(p))
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)


def neg(p):
    return tuple(-x for x in p)


def mul(p, q):
    if p == (0,) or q == (0,):
        return (0,)
    r = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                r[i + j] += x * y
    return trim(r)


def derivative(p):
    return trim(tuple(i * p[i] for i in range(1, len(p))) or (0,))


def value(p, a):
    r = 0
    for x in reversed(p):
        r = r * a + x
    return r


def polynomial_product(factors):
    r = (1,)
    for f in factors:
        r = mul(r, f)
    return r


def canonical(n, edges):
    """Canonicalize within degree classes; returns consecutive vertex labels."""
    edges = set(tuple(sorted(e)) for e in edges)
    degree = [sum(v in e for e in edges) for v in range(n)]
    classes = [[v for v in range(n) if degree[v] == d]
               for d in sorted(set(degree))]
    best = None
    for blocks in product(*(permutations(c) for c in classes)):
        ordering = sum((tuple(b) for b in blocks), ())
        relabel = {v: i for i, v in enumerate(ordering)}
        candidate = tuple(sorted(tuple(sorted((relabel[u], relabel[v])))
                                 for u, v in edges))
        if best is None or candidate < best:
            best = candidate
    return n, best


def connected_graphs(max_edges):
    """Generate all connected simple graphs using an edge/leaf augmentation."""
    levels = {0: {(1, ())}}
    for m in range(1, max_edges + 1):
        out = set()
        for n, edges in levels[m - 1]:
            existing = set(edges)
            for e in combinations(range(n), 2):
                if e not in existing:
                    out.add(canonical(n, edges + (e,)))
            for u in range(n):
                out.add(canonical(n + 1, edges + ((u, n),)))
        levels[m] = out
    return [(n, e) for m in range(1, max_edges + 1)
            for n, e in sorted(levels[m])]


@lru_cache(None)
def upsets(m):
    """Bitset truth tables for every increasing Boolean function of m bits."""
    if m == 0:
        return (0, 1)
    smaller = upsets(m - 1)
    width = 1 << (m - 1)
    return tuple(low | (high << width) for low in smaller for high in smaller
                 if low & high == low)


def transitions(n, edges, opened, warm):
    """Ignore warm components unable to affect any final edge."""
    components = []
    todo = warm
    while todo:
        component = todo & -todo
        while True:
            grown = component
            for i, (u, v) in enumerate(edges):
                pair = (1 << u) | (1 << v)
                if opened >> i & 1 and component & pair:
                    grown |= pair
            if grown == component:
                break
            component = grown
        assert component & warm == component
        todo &= ~component
        components.append(component)
    active = tuple(i for i, (u, v) in enumerate(edges)
                   if not (opened >> i & 1)
                   and warm >> u & 1 and warm >> v & 1)
    relevant = tuple(c for c in components
                     if any(c & ((1 << edges[i][0]) | (1 << edges[i][1]))
                            for i in active))
    return active, relevant


def symbolic_law(n, edges):
    """Return D and N_s such that final P(s)=N_s(alpha)/D(alpha)."""
    m = len(edges)
    linear = {e: tuple((e, k) for k in range(1, min(n, 2 * e) + 1))
              for e in range(1, m + 1)}
    layer = {e: polynomial_product(linear[e]) for e in linear}
    denominator = [(1,)]
    for e in range(1, m + 1):
        denominator.append(mul(denominator[-1], layer[e]))

    @lru_cache(None)
    def multiplier(e, k, next_e):
        assert 0 <= next_e < e
        factors = [f for f in linear[e] if f != (e, k)]
        factors.extend(layer[j] for j in range(next_e + 1, e))
        return polynomial_product(factors)

    @lru_cache(None)
    def visit(opened, warm):
        active, relevant = transitions(n, edges, opened, warm)
        e, k = len(active), len(relevant)
        if e == 0:
            return {opened: (1,)}
        output = {}
        successors = [(opened | (1 << i), warm, (1,)) for i in active]
        successors += [(opened, warm & ~c, (0, 1)) for c in relevant]
        for next_opened, next_warm, rate in successors:
            next_e = len(transitions(n, edges, next_opened, next_warm)[0])
            factor = mul(rate, multiplier(e, k, next_e))
            for mask, p in visit(next_opened, next_warm).items():
                output[mask] = add(output.get(mask, (0,)), mul(p, factor))
        return output

    law = visit(0, (1 << n) - 1)
    numerators = tuple(law.get(s, (0,)) for s in range(1 << m))
    assert sum_polynomials(numerators) == denominator[m]
    assert all(all(c >= 0 for c in p) for p in numerators)
    return denominator[m], numerators, visit.cache_info().currsize


def sum_polynomials(polys):
    answer = (0,)
    for p in polys:
        answer = add(answer, p)
    return answer


def event_polynomials(numerators, events):
    return {event: sum_polynomials(p for s, p in enumerate(numerators)
                                   if event >> s & 1)
            for event in events}


def rational_law(n, edges, alpha):
    """Independent forward mass propagation, retaining all freezing clocks."""
    m = len(edges)
    pending = {(0, (1 << n) - 1): Fraction(1)}
    final = [Fraction(0)] * (1 << m)
    # Each event opens an edge or freezes at least one vertex, so this rank rises.
    for rank in range(m + n + 1):
        states = [s for s in pending if s[0].bit_count() + n - s[1].bit_count() == rank]
        for opened, warm in states:
            mass = pending.pop((opened, warm))
            if warm == 0:
                final[opened] += mass
                continue
            active = tuple(i for i, (u, v) in enumerate(edges)
                           if not (opened >> i & 1)
                           and (warm & (1 << u)) and (warm & (1 << v)))
            components = []
            unseen = warm
            while unseen:
                component = unseen & -unseen
                while True:
                    grown = component
                    for i, (u, v) in enumerate(edges):
                        pair = (1 << u) | (1 << v)
                        if opened >> i & 1 and component & pair:
                            grown |= pair
                    if grown == component:
                        break
                    component = grown
                unseen &= ~component
                components.append(component)
            total = len(active) + alpha * len(components)
            successors = [(opened | (1 << i), warm, Fraction(1)) for i in active]
            successors += [(opened, warm & ~c, alpha) for c in components]
            for next_opened, next_warm, rate in successors:
                state = (next_opened, next_warm)
                pending[state] = pending.get(state, Fraction(0)) + mass * rate / total
    assert not pending
    assert sum(final) == 1
    return tuple(final)


def controls():
    """Closed-form positive control and an actual failed lattice inequality."""
    for alpha in [Fraction(1, 7), Fraction(1), Fraction(11, 3)]:
        assert rational_law(2, ((0, 1),), alpha) == (
            2 * alpha / (1 + 2 * alpha), 1 / (1 + 2 * alpha))
    path_law = rational_law(4, ((0, 1), (1, 2), (2, 3)), Fraction(1))
    expected = (Fraction(34, 105), Fraction(1, 7), Fraction(13, 105),
                Fraction(8, 105), Fraction(1, 7), Fraction(2, 35),
                Fraction(8, 105), Fraction(2, 35))
    assert path_law == expected
    lattice_difference = path_law[0] * path_law[5] - path_law[1] * path_law[4]
    assert lattice_difference == -Fraction(1, 525)
    # Independent-edge reference has nonnegative association certificates.
    independent_weights = tuple((1,) for _ in range(8))
    independent_sums = event_polynomials(independent_weights, upsets(3))
    for first in upsets(3):
        for second in upsets(3):
            assert independent_sums[first & second][0] * 8 >= (
                independent_sums[first][0] * independent_sums[second][0])
    # A deliberately negatively associated law must fail the same event test.
    anti_sums = event_polynomials(((0,), (1,), (1,), (0,)), upsets(2))
    assert anti_sums[0b1000][0] * 2 - anti_sums[0b1010][0] * anti_sums[0b1100][0] == -1
    return {"single_edge_formula": "P(open)=1/(1+2*alpha)",
            "path_4_alpha_1_law_mask_order": list(map(str, path_law)),
            "path_4_FKG_lattice_difference_masks_1_4": str(lattice_difference),
            "independent_and_anticorrelated_controls": "passed"}


def run(max_monotonicity_edges=5, max_association_edges=4):
    graphs = connected_graphs(max(max_monotonicity_edges, max_association_edges))
    expected = [1, 1, 3, 5, 12]
    assert [sum(len(e) == m for _, e in graphs) for m in range(1, len(expected) + 1)
            if m <= max(max_monotonicity_edges, max_association_edges)] == expected[:max(max_monotonicity_edges, max_association_edges)]
    assert [len(upsets(m)) for m in range(6)] == [2, 3, 6, 20, 168, 7581]
    report = {"checked_date": "2026-10-09", "arithmetic": "exact integers and fractions",
              "controls": controls(),
              "rational_crosscheck_parameters": ["1/7", "1", "11/3"],
              "graphs": [], "scope": {"monotonicity_max_component_edges": max_monotonicity_edges,
                                      "association_max_component_edges": max_association_edges}}
    laws = {"coefficient_order": "ascending powers of alpha", "graphs": []}
    for index, (n, edges) in enumerate(graphs, 1):
        started = time.monotonic()
        m = len(edges)
        d, weights, state_count = symbolic_law(n, edges)
        for alpha in [Fraction(1, 7), Fraction(1), Fraction(11, 3)]:
            assert tuple(value(p, alpha) / value(d, alpha) for p in weights) == rational_law(n, edges, alpha)
        events = upsets(m)
        sums = event_polynomials(weights, events)
        record = {"vertices": n, "edges": list(edges), "edge_count": m,
                  "symbolic_states": state_count, "increasing_events": len(events),
                  "denominator_degree": len(d) - 1,
                  "law_sha256": hashlib.sha256(repr((d, weights)).encode()).hexdigest()}
        laws["graphs"].append({"vertices": n, "edges": list(edges),
                               "denominator": d, "numerators_mask_order": weights})
        if m <= max_monotonicity_edges:
            failures = []
            digest = hashlib.sha256()
            zero_count = 0
            for event in events:
                c = sums[event]
                certificate = add(mul(c, derivative(d)), neg(mul(derivative(c), d)))
                digest.update(repr((event, certificate)).encode())
                zero_count += certificate == (0,)
                if any(x < 0 for x in certificate):
                    failures.append(event)
            record["monotonicity_certificates"] = len(events)
            record["monotonicity_coefficient_failures"] = failures
            record["monotonicity_zero_certificates"] = zero_count
            record["monotonicity_certificate_sha256"] = digest.hexdigest()
            assert not failures, (edges, "monotonicity coefficient failure", failures)
            assert zero_count == 2  # Only the empty and full events are constant.
        if m <= max_association_edges:
            scaled = {event: mul(sums[event], d) for event in events}
            failures = []
            checked = 0
            zero_count = 0
            digest = hashlib.sha256()
            for i, first in enumerate(events):
                for second in events[i:]:
                    certificate = add(scaled[first & second], neg(mul(sums[first], sums[second])))
                    checked += 1
                    zero_count += certificate == (0,)
                    digest.update(repr((first, second, certificate)).encode())
                    if any(x < 0 for x in certificate):
                        failures.append([first, second])
            record["association_certificates"] = checked
            record["association_coefficient_failures"] = failures
            record["association_zero_certificates"] = zero_count
            record["association_certificate_sha256"] = digest.hexdigest()
            assert not failures, (edges, "association coefficient failure", failures)
        report["graphs"].append(record)
        print(f"{index}/{len(graphs)}: n={n} m={m}, states={state_count}, "
              f"failures mono={len(record.get('monotonicity_coefficient_failures', []))} "
              f"assoc={len(record.get('association_coefficient_failures', []))}, "
              f"{time.monotonic() - started:.2f}s", flush=True)
    report["totals"] = {
        "connected_graphs": len(graphs),
        "monotonicity_certificates": sum(r.get("monotonicity_certificates", 0) for r in report["graphs"]),
        "association_certificates": sum(r.get("association_certificates", 0) for r in report["graphs"]),
        "rational_crosschecks": 3 * len(graphs),
        "all_certificates_passed": True,
    }
    return report, laws


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-monotonicity-edges", type=int, choices=range(1, 6), default=5)
    parser.add_argument("--max-association-edges", type=int, choices=range(1, 5), default=4)
    parser.add_argument("--output", default="constant_freezing_verification.json")
    parser.add_argument("--laws-output", default="constant_freezing_laws.json")
    args = parser.parse_args()
    result, laws = run(args.max_monotonicity_edges, args.max_association_edges)
    with open(args.output, "w") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
    with open(args.laws_output, "w") as handle:
        json.dump(laws, handle, indent=2)
        handle.write("\n")
