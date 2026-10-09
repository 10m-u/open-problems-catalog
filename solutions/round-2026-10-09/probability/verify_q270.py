"""Exact Q270 checks: count chain versus explicit edge-subset enumeration.

The proof in Q270-transitive-tournament-bunkbed.md is for all n; these finite
checks independently validate the source-model interpretation and cancellation.
No third-party dependencies are required.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json


def transitions(a, b, p, q):
    alpha, beta = (1-p)**a, (1-p)**b
    result = {
        (0, 0): alpha*beta,
        (1, 0): (1-q)*(1-alpha)*beta,
        (0, 1): (1-q)*alpha*(1-beta),
        (1, 1): (1-alpha)*(1-beta)+q*((1-alpha)*beta+alpha*(1-beta)),
    }
    assert sum(result.values()) == 1 and min(result.values()) >= 0
    return result


def propagate(distribution, p, q):
    out = defaultdict(F)
    for (a, b, hit), mass in distribution.items():
        if not mass:
            continue
        for (da, db), probability in transitions(a, b, p, q).items():
            if probability:
                out[a+da, b+db, hit or a+da == b+db] += mass*probability
    assert sum(out.values()) == 1
    return dict(out)


def count_chain(n, p=F(1, 2), qs=None):
    qs = [F(1, 2)]*n if qs is None else qs
    if n == 1:
        return {'lower': F(1), 'upper': qs[0], 'difference': 1-qs[0],
                'diagonal_contribution': F(0), 'survivor_contribution': 1-qs[0]}
    distribution = {(1, 0, False): 1-qs[0], (1, 1, True): qs[0]}
    for j in range(1, n-1):
        distribution = propagate(distribution, p, qs[j])
    lower = upper = diagonal = survivor = F(0)
    for (a, b, hit), mass in distribution.items():
        row = transitions(a, b, p, qs[-1])
        lower += mass*(row[1, 0]+row[1, 1])
        upper += mass*(row[0, 1]+row[1, 1])
        delta = (1-qs[-1])*((1-p)**b-(1-p)**a)
        assert delta == row[1, 0]-row[0, 1]
        if hit:
            diagonal += mass*delta
        else:
            assert a > b
            survivor += mass*delta
    assert diagonal == 0
    assert survivor >= 0
    assert lower-upper == diagonal+survivor
    lower_bound = (1-qs[0])*(1-qs[-1])*p*(1-p)**(n-2)
    assert lower-upper >= lower_bound
    return {'lower': lower, 'upper': upper, 'difference': lower-upper,
            'diagonal_contribution': diagonal, 'survivor_contribution': survivor,
            'explicit_lower_bound': lower_bound}


def enumerate_edges(n):
    # One Bernoulli bit controls BOTH directions of a vertical edge.
    edges = [((2*i, 2*i+1), (2*i+1, 2*i)) for i in range(n)]
    edges += [((2*i+layer, 2*j+layer),) for i in range(n)
              for j in range(i+1, n) for layer in (0, 1)]
    assert len(edges) == n*n
    count = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for mask in range(1 << len(edges)):
        adjacency = [0]*(2*n)
        for edge_index, arcs in enumerate(edges):
            if mask & (1 << edge_index):
                for a, b in arcs:
                    adjacency[a] |= 1 << b
        # Generic graph search, independent of the count-chain compression.
        for u in range(n):
            reachable = frontier = 1 << (2*u)
            while frontier:
                bit = frontier & -frontier
                frontier -= bit
                vertex = bit.bit_length()-1
                fresh = adjacency[vertex] & ~reachable
                reachable |= fresh
                frontier |= fresh
            for v in range(n):
                for layer in (0, 1):
                    count[u][v][layer] += bool(reachable & (1 << (2*v+layer)))
    total = 1 << len(edges)
    comparisons = {}
    for u in range(n):
        for v in range(n):
            actual = [F(x, total) for x in count[u][v]]
            if u > v:
                expected = [F(0), F(0)]
            else:
                dp = count_chain(v-u+1)
                expected = [dp['lower'], dp['upper']]
            assert actual == expected, (n, u, v, actual, expected)
            assert actual[0] >= actual[1]
            comparisons[f'{u+1},{v+1}'] = list(map(str, actual))
    return {'graphs_enumerated': total, 'all_pairs_match': True,
            'reachability_probabilities': comparisons}


def general_parameter_checks():
    tested = 0
    for p in (F(0), F(1, 7), F(1, 3), F(1, 2), F(4, 5), F(1)):
        for q in (F(0), F(2, 7), F(1, 2), F(1)):
            for a in range(7):
                for b in range(7):
                    first, reverse = transitions(a, b, p, q), transitions(b, a, p, q)
                    assert all(first[da, db] == reverse[db, da] for da, db in first)
                    tested += 1
        qs = [F(2, 7), F(0), F(1, 3), F(3, 5), F(1), F(2, 9), F(1, 2)]
        for n in range(2, len(qs)+1):
            count_chain(n, p, qs[:n])
        # An explicitly diagonal start has a symmetric law at every stage.
        distribution = {(3, 3, True): F(1)}
        for q in qs:
            distribution = propagate(distribution, p, q)
            for (a, b, hit), mass in distribution.items():
                assert distribution.get((b, a, hit), 0) == mass
    return {'transition_symmetry_cases': tested,
            'inhomogeneous_vertical_checks': True,
            'diagonal_start_symmetry_checks': True}


if __name__ == '__main__':
    explicit = {str(n): enumerate_edges(n) for n in range(1, 5)}
    chain = {str(n): {k: str(v) for k, v in count_chain(n).items()}
             for n in range(1, 17)}
    output = {'explicit_graphs': explicit, 'count_chain': chain,
              'general_parameters': general_parameter_checks()}
    destination = Path(__file__).with_name('Q270-certificates.json')
    destination.write_text(json.dumps(output, indent=2)+'\n')
    total_graphs = sum(item['graphs_enumerated'] for item in explicit.values())
    print(f'Q270: {total_graphs} explicit graphs; every ordered vertex pair matches the exact count chain.')
    print('Q270: diagonal cancellation, strict lower bounds, and general-parameter symmetries passed.')
    print(destination.name)
