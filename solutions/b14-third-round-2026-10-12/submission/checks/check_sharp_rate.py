#!/usr/bin/env python3
"""Finite, exact-arithmetic checks supporting the sharp-rate proof.

This file imports none of the handoff's research implementations. It is not
an all-n formal verification. Run with Python 3.10+; no third-party packages.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path
from random import Random
import time

Edge = tuple[int, int]

def edge(u: int, v: int) -> Edge:
    return (min(u, v), max(u, v))

def exchange_data(n: int) -> list[tuple[tuple[int, int], tuple[Edge, Edge]]]:
    return [((i, j), (edge(i, j), edge((i + 1) % n, (j + 1) % n)))
            for i, j in combinations(range(n), 2)
            if len({i, (i + 1) % n, j, (j + 1) % n}) == 4]

def is_cycle(n: int, edges: set[Edge]) -> bool:
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    if len(edges) != n or any(len(adj[i]) != 2 for i in range(n)):
        return False
    todo, seen = [0], {0}
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v); todo.append(v)
    return len(seen) == n

def structural_checks() -> dict:
    total = legal_reconnection_checks = 0
    component_counts = {}
    for n in range(3, 101):
        rows = exchange_data(n)
        assert len(rows) == n * (n - 3) // 2
        uses = defaultdict(list)
        for k, (_, chords) in enumerate(rows):
            for c in chords:
                uses[c].append(k)
        assert len(uses) == len(rows)
        assert all(len(v) == 2 for v in uses.values())
        neighbors = [set() for _ in rows]
        for inds in uses.values():
            a, b = inds
            neighbors[a].add(b); neighbors[b].add(a)
        if n >= 5:
            assert all(len(v) == 2 for v in neighbors)
            assert all(len(set(rows[k][1]) & set(rows[j][1])) == 1
                       for k in range(len(rows)) for j in neighbors[k])
        remaining = set(range(len(rows)))
        sizes = []
        while remaining:
            first = remaining.pop(); todo = [first]; size = 1
            while todo:
                for j in neighbors[todo.pop()]:
                    if j in remaining:
                        remaining.remove(j); todo.append(j); size += 1
            sizes.append(size)
        expected = ([n] * ((n - 3) // 2) if n % 2
                    else [n] * max(0, n // 2 - 2) + [n // 2])
        if n == 3:
            expected = []
        assert sorted(sizes) == sorted(expected), (n, sizes, expected)
        component_counts[str(n)] = sorted(sizes)
        if n <= 16:
            original = {edge(i, (i + 1) % n) for i in range(n)}
            for (i, j), chords in rows:
                a, b, c, d = i, (i + 1) % n, j, (j + 1) % n
                residual = original - {edge(a, b), edge(c, d)}
                alternative = {edge(a, d), edge(b, c)}
                assert is_cycle(n, residual | set(chords))
                assert not is_cycle(n, residual | alternative)
                legal_reconnection_checks += 1
        total += len(rows)
    return {'n_range': [3, 100], 'exchange_constraints': total,
            'independent_reconnection_checks': legal_reconnection_checks,
            'component_sizes': component_counts}

def discrete_correlation_checks() -> dict:
    """Check Harris and each exact conditional step underlying Janson."""
    all_rows = []
    for n, q in [(4, 4), (5, 3), (6, 2)]:
        exchanges = exchange_data(n)
        chords = sorted({c for _, cc in exchanges for c in cc})
        pos = {c: k for k, c in enumerate(chords)}
        constraints = [(i, j, pos[a], pos[b]) for (i, j), (a, b) in exchanges]
        neighbors = [{j for j in range(k)
                      if set(exchanges[k][1]) & set(exchanges[j][1])}
                     for k in range(len(exchanges))]
        chord_assignments = list(product(range(q), repeat=len(chords)))
        denominator = len(chord_assignments)
        counts_by_x = {}
        chain_checks = 0
        for x in product(range(q), repeat=n):
            frequency = Counter()
            for y in chord_assignments:
                bad = sum((1 << k) for k, (i, j, a, b) in enumerate(constraints)
                          if y[a] + y[b] < x[i] + x[j])
                frequency[bad] += 1
            good = frequency[0]
            counts_by_x[x] = good
            product_marginals = F(1)
            for k in range(len(exchanges)):
                bad_k = sum(c for mask, c in frequency.items() if mask & (1 << k))
                p_k = F(bad_k, denominator)
                product_marginals *= 1 - p_k
                previous_mask = (1 << k) - 1
                surviving = sum(c for mask, c in frequency.items() if not mask & previous_mask)
                surviving_bad = sum(c for mask, c in frequency.items()
                                    if not mask & previous_mask and mask & (1 << k))
                assert surviving > 0  # All chords at the largest grid value suffice.
                conditional = F(surviving_bad, surviving)
                correction = sum((F(sum(c for mask, c in frequency.items()
                                             if mask & (1 << k) and mask & (1 << j)), denominator)
                                  for j in neighbors[k]), F(0))
                assert conditional >= p_k - correction
                chain_checks += 1
            assert F(good, denominator) >= product_marginals
        cap = (q - 1) // 2
        for x, good in counts_by_x.items():
            clipped = tuple(min(t, cap) for t in x)
            assert counts_by_x[clipped] >= good
        all_rows.append({'n': n, 'grid_size': q, 'tour_assignments': q ** n,
                         'chord_assignments_per_tour': denominator,
                         'exact_conditional_chain_checks': chain_checks,
                         'harris_and_clipping_checks': q ** n})
    return {'rows': all_rows,
            'tour_assignments': sum(r['tour_assignments'] for r in all_rows),
            'joint_assignments': sum(r['tour_assignments'] * r['chord_assignments_per_tour'] for r in all_rows),
            'exact_conditional_chain_checks': sum(r['exact_conditional_chain_checks'] for r in all_rows)}

def analytic_identity_checks() -> dict:
    overlap_cases = 0
    for delta in [F(1, 100), F(1, 20), F(1, 5), F(1, 3), F(49, 100)]:
        for i, j in product(range(21), repeat=2):
            s, t = 2 * delta * F(i, 20), 2 * delta * F(j, 20)
            m, M = min(s, t), max(s, t)
            integral = s*t*m - (s+t)*m*m/2 + m**3/3
            formula = m*m*M/2 - m**3/6
            assert integral == formula
            assert formula <= delta * (s*s/2 + t*t/2)
            overlap_cases += 1
    rng = Random(14101203)
    quadratic_cases = 0
    for n in range(3, 151):
        for _ in range(4):
            x = [F(rng.randrange(101), 100) for _ in range(n)]
            A, S = sum(t*t for t in x), sum(x)
            B = sum(x[i]*x[(i+1) % n] for i in range(n))
            Q = sum((x[i]+x[j])**2 for (i,j), _ in exchange_data(n))
            assert Q == (n-4)*A + S*S - 2*B
            assert (n-6)*A + S*S <= Q <= n*A + S*S
            quadratic_cases += 1
    a = F(3, 5)
    integral_lower = a - a**3/6 + a**5/40 - a**7/336
    assert F(627, 500)**2 > F(11, 7)
    rho_upper = (1-F(7,50)+F(7,50)**2/2) * (F(627,500)-integral_lower)
    assert rho_upper < F(3,5)
    return {'exact_overlap_cases': overlap_cases, 'exact_quadratic_cases': quadratic_cases,
            'quadratic_n_range': [3, 150], 'rho_rational_upper': str(rho_upper),
            'rho_rational_upper_decimal': float(rho_upper),
            'rho_rational_upper_less_than_3_over_5': True}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('EXACT-CHECK-RESULTS.json'))
    args = parser.parse_args()
    start = time.perf_counter()
    result = {'status': 'passed', 'structural': structural_checks(),
              'discrete_correlation': discrete_correlation_checks(),
              'analytic_identities': analytic_identity_checks(),
              'scope': 'Finite exact checks, not a formal verification of the all-size asymptotic theorem.'}
    result['elapsed_seconds'] = time.perf_counter() - start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    summary = {k:v for k,v in result.items() if k != 'structural'}
    summary['structural'] = {k:v for k,v in result['structural'].items() if k != 'component_sizes'}
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
