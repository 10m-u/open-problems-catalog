"""Exact bounded controls of new Paley proof-route obstructions."""
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from pathlib import Path


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, int(n**0.5)+1))


def odd_factors(n):
    out = set()
    while n % 2 == 0:
        n //= 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0:
                n //= d
        d += 2
    if n > 1:
        out.add(n)
    return out


def chi_list(p):
    sq = {x*x % p for x in range(1, p)}
    return [0 if x == 0 else 1 if x in sq else -1 for x in range(p)]


def main():
    sidon = []
    for k in range(1, 11):
        c = [4**j for j in range(k)]
        diffs = [a-b for a in c for b in c if a != b]
        assert len(set(diffs)) == k*(k-1)
        sums = {}
        for a in c:
            for b in c:
                sums[a+b] = sums.get(a+b, 0)+1
        assert sum(v*v for v in sums.values()) == 2*k*k-k
        if k <= 5:
            modulus = 8
            factors = set().union(*(odd_factors(d) for d in diffs if d > 0))
            for q in factors:
                modulus *= q
            p = next(modulus*t+1 for t in range(1, 201)
                     if modulus*t+1 > 2*c[-1] and prime(modulus*t+1))
            assert all(pow(d % p, (p-1)//2, p) == 1 for d in diffs)
            assert len({d % p for d in diffs}) == len(diffs)
            sidon.append({'k': k, 'modulus': modulus, 'prime': p})

    # Exact positivity controls for the signed K3 degree-four pseudoexpectation.
    points = list(product([0, 1], repeat=3))
    monomials = [()] + [(i,) for i in range(3)] + list(combinations(range(3), 2))
    masses = [Fraction(-1, 48) if a == (1, 1, 1) else Fraction(7, 48) for a in points]
    assert sum(masses) == 1
    moments = {}
    for size in range(4):
        for s in combinations(range(3), size):
            moments[s] = sum(w*all(a[i] for i in s) for w, a in zip(masses, points))
    assert moments[(0,)] == Fraction(5, 12)
    assert moments[(0, 1)] == Fraction(1, 8)
    assert moments[(0, 1, 2)] == Fraction(-1, 48)
    assert moments[(0, 1, 2)]/moments[(0, 1)] == Fraction(-1, 6)
    squared_controls = 0
    evaluations = [[int(all(a[i] for i in s)) for s in monomials] for a in points]
    for coeff in product([-1, 0, 1], repeat=7):
        vals = [sum(c*v for c, v in zip(coeff, row)) for row in evaluations]
        assert sum(w*v*v for w, v in zip(masses, vals)) >= 0
        squared_controls += 1

    # Exact affine orbit and noncommuting moment-coordinate controls.
    p = 37
    chi = chi_list(p)
    edges = [e for e in combinations(range(p), 2) if chi[(e[1]-e[0]) % p] == 1]

    def key(vertices):
        u = tuple(sorted(set(vertices)))
        if not all(chi[(b-a) % p] == 1 for a, b in combinations(u, 2)):
            return None
        return min(tuple(sorted((x-a)*pow(b-a, -1, p) % p for x in u))
                   for a, b in permutations(u, 2))

    key_tri = (0, 1, 4)
    key_quad = (0, 1, 4, 11)
    assert key(key_tri) == key_tri
    assert key((0, 1, 11)) != key_tri
    assert key(key_quad) == key_quad
    u, v = (0, 1), (0, 4)
    ab = ba = 0
    for edge in edges:
        left, right = key(u+edge), key(edge+v)
        ab += int(left == key_quad and right == key_tri)
        ba += int(left == key_tri and right == key_quad)
    assert ab-ba == 1
    affine_controls = 0
    images = set()
    for a in range(1, p):
        if chi[a] != 1:
            continue
        for b in range(p):
            image = tuple(sorted((a*x+b) % p for x in key_tri))
            images.add(image)
            assert key(image) == key_tri
            assert key(tuple((a*x+b) % p for x in key_quad)) == key_quad
            affine_controls += 2
    assert (0, 1, 11) not in images

    # Q^2=pI-J is the exact spectral input to the local PSD witness and diamond repair.
    spectral_entries = 0
    for p in [5, 13, 17, 29, 37, 41, 61]:
        chi = chi_list(p)
        for x in range(p):
            for y in range(p):
                val = sum(chi[(x-z) % p]*chi[(z-y) % p] for z in range(p))
                assert val == (p-1 if x == y else -1)
                spectral_entries += 1
        q = [x for x in range(1, p) if chi[x] == 1]
        assert all(sum(chi[(x-y) % p] == 1 for y in q) == (p-5)//4 for x in q)

    receipt = {'passed': True, 'integer_sidon_sizes': list(range(1, 11)),
               'prime_sidon_examples': sidon, 'signed_pseudo_square_controls': squared_controls,
               'signed_pair_conditional_first_moment': '-1/6',
               'noncommuting_union_moment_witness': {'p': 37, 'edge_count': len(edges),
                   'A_key': list(key_quad), 'B_key': list(key_tri), 'row': list(u),
                   'column': list(v), 'AB_entry': ab, 'BA_entry': ba},
               'triangle_orbit_size': len(images), 'affine_key_controls': affine_controls,
               'exact_quadratic_character_matrix_entries': spectral_entries,
               'scope': 'Bounded exact controls; infinite claims use the written proofs and stated external inputs, not extrapolation.'}
    Path(__file__).with_name('ROUTE-CHECK-RESULTS.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__':
    main()
