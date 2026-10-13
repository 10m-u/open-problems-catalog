"""Bounded exact controls for Q2187 A1; no clique upper-bound search."""
from itertools import combinations
import json
from pathlib import Path


def character(p):
    squares = {x*x % p for x in range(1, p)}
    return [0 if x == 0 else 1 if x in squares else -1 for x in range(p)]


def check_clique(p, chi, clique):
    k = len(clique)
    assert all(chi[(a-b) % p] == 1 for a, b in combinations(clique, 2))
    vals = [sum(chi[(x-a) % p] for a in clique) for x in range(p)]
    second = sum(y*y for y in vals)
    fourth = sum(y**4 for y in vals)
    collective = 0
    for d in combinations(clique, 4):
        w = sum(chi[(x-d[0]) % p]*chi[(x-d[1]) % p]*
                chi[(x-d[2]) % p]*chi[(x-d[3]) % p] for x in range(p))
        assert w*w <= 9*p
        collective += w
    rhs = p*(3*k*k-2*k)-12*k**3+26*k*k-15*k+24*collective
    assert second == k*(p-k)
    assert fourth == rhs
    assert k*(k-1)**4 <= fourth
    return int(k >= 4)


def main():
    cases = quartic_cases = 0
    by_prime = {}
    for p in [5, 13, 17, 29, 37, 41, 61]:
        chi = character(p)
        cliques = set()
        if p <= 29:
            for k in range(1, 5):
                for c in combinations(range(p), k):
                    if all(chi[(a-b) % p] == 1 for a, b in combinations(c, 2)):
                        cliques.add(c)
        else:
            # At most p greedily constructed cliques and all their subsets.
            for start in range(p):
                c = []
                for step in range(p):
                    x = (start+step) % p
                    if all(chi[(x-a) % p] == 1 for a in c):
                        c.append(x)
                for k in range(1, min(len(c), 6)+1):
                    cliques.update(tuple(sorted(d)) for d in combinations(c, k))
        for c in sorted(cliques):
            quartic_cases += check_clique(p, chi, c)
            cases += 1
        by_prime[str(p)] = len(cliques)
    # Even a putative k=floor(sqrt(p)) is not excluded by the A1 envelope.
    # Use square p only as a real-parameter scale check, not a prime instance.
    scale_controls = 0
    for r in [10, 100, 1000, 10000]:
        p, k = r*r, r
        envelope = p*(3*k*k-2*k)-12*k**3+26*k*k-15*k
        envelope += 3*k*(k-1)*(k-2)*(k-3)*r
        assert k*(k-1)**4 <= envelope
        scale_controls += 1
    receipt = {'passed': True, 'exact_clique_controls': cases,
               'controls_with_quartic_terms': quartic_cases,
               'by_prime': by_prime, 'scale_controls': scale_controls,
               'scope': 'Exact finite identities and compatibility of the individual-Weil envelope; not an asymptotic theorem or recovery of old certificates.'}
    path = Path(__file__).with_name('MOMENT-CHECK-RESULTS.json')
    path.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
