#!/usr/bin/env python3
"""Independent exact audit; imports none of the root's colored implementations.

Literal multiset-word recursion and literal inversion-sequence products replace
the root's permutation-set enumeration and refined ascent recurrence.  The
existing all-length compression theorem is a mathematical dependency, not
something established by these finite computations.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, factorial, isqrt, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def colored_words(m, r):
    """Yield each word once; symbols use 0-based indices and colors start at 1."""
    counts = list(m)
    word = []

    def visit():
        if not any(counts):
            yield tuple(word)
            return
        for symbol, left in enumerate(counts):
            if left:
                counts[symbol] -= 1
                for color in range(1, r[symbol] + 1):
                    word.append((color, symbol))
                    yield from visit()
                    word.pop()
                counts[symbol] += 1

    yield from visit()


def descents(word, n):
    following = word[1:] + ((1, n),)
    return sum(a > b for a, b in zip(word, following))


def row(words, n, degree):
    out = [0] * (degree + 1)
    for word in words:
        out[descents(word, n)] += 1
    return out


def trim(h):
    h = list(h)
    while len(h) > 1 and not h[-1]:
        h.pop()
    return h


def ehrhart_numerator(m, r):
    M = sum(m)
    values = [prod(comb(c * t + a, a) for a, c in zip(m, r))
              for t in range(M + 1)]
    return trim([sum((-1) ** j * comb(M + 1, j) * values[k - j]
                     for j in range(k + 1)) for k in range(M + 1)])


def canonical_vectors(volume, limit):
    """Build factor/unit strings directly; no cached ordered-factor list."""
    if volume == 1:
        yield (1,)  # constant numerator, separate from nonconstant 2d-1 bound
        return

    def extend(rem, prefix):
        if rem == 1:
            yield prefix
            return
        for factor in range(2, rem + 1):
            if rem % factor:
                continue
            for separator in ((), (1,)) if prefix else ((),):
                nxt = prefix + separator + (factor,)
                if len(nxt) <= limit:
                    yield from extend(rem // factor, nxt)

    yield from extend(volume, ())


@lru_cache(None)
def inversion_row(s):
    counts = [0] * (len(s) + 1)
    for e in product(*(range(a) for a in s)):
        asc = int(e[0] > 0)
        asc += sum(e[i - 1] * s[i] < e[i] * s[i - 1]
                   for i in range(1, len(s)))
        counts[asc] += 1
    return trim(counts)


def decomposition(h):
    """Divide h-xR_d(h) and R_d(h)-h by 1-x using coefficient sums."""
    D = len(h) - 1
    rev = list(reversed(h))
    a, b, carry_a, carry_b = [], [], 0, 0
    for i in range(D + 1):
        carry_a += h[i] - (rev[i - 1] if i else 0)
        a.append(carry_a)
    for i in range(D):
        carry_b += rev[i] - h[i]
        b.append(carry_b)
    assert a == a[::-1] and b == b[::-1]
    assert [a[i] + (b[i - 1] if i else 0) for i in range(D + 1)] == h
    return a, b


def gamma(h):
    if not h:
        return []
    D = len(h) - 1
    remainder = list(h)
    result = []
    for k in range(D // 2 + 1):
        count = remainder[k]
        result.append(count)
        for j in range(D - 2 * k + 1):
            remainder[j + k] -= count * comb(D - 2 * k, j)
    assert not any(remainder)
    return result


def growth(h, M, c):
    # Direct coefficient consequence of differentiating the Ehrhart series.
    return trim([(1 + c * j) * (h[j] if j < len(h) else 0)
                 + (c * (M + 2 - j) - 1) * (h[j - 1] if j else 0)
                 for j in range(len(h) + 1)])


def complement(word, N, R):
    return tuple((R + 1 - c, N - 1 - s) for c, s in word)


def main():
    packet = json.loads((HERE / 'COLORED-PROBE.json').read_text())
    candidate_controls = literal_word_controls = growth_controls = 0
    for case in packet['cases']:
        m, r = tuple(case['m']), tuple(case['r'])
        words = list(colored_words(m, r))
        h = trim(row(words, len(m), sum(m)))
        assert h == case['h'] == ehrhart_numerator(m, r)
        assert len(words) == factorial(sum(m)) // prod(map(factorial, m)) * prod(
            c ** a for a, c in zip(m, r)) == case['volume']
        literal_word_controls += len(words)
        candidates = list(canonical_vectors(sum(h), 2 * (len(h) - 1) - 1))
        assert len(candidates) == case['candidate_count']
        matches = sorted([list(s) for s in candidates if inversion_row(s) == h])
        assert matches == sorted(case['matches'])
        candidate_controls += len(candidates)
        for i, (a, c) in enumerate(zip(m, r)):
            new_m = list(m)
            new_m[i] += 1
            assert growth(h, sum(m), Fraction(c, a + 1)) == ehrhart_numerator(new_m, r)
            growth_controls += 1

    # The constant case must bypass the nonconstant representation bound.
    assert ehrhart_numerator((5,), (1,)) == [1]
    assert list(canonical_vectors(1, -1)) == [(1,)]
    assert inversion_row((1,)) == [1]

    assert inversion_row((3, 1, 2, 2)) == [1, 5, 6]
    assert inversion_row((1, 1, 6, 4)) == [1, 16, 7]
    assert inversion_row((2, 6)) == [1, 9, 2]
    assert inversion_row((2, 6, 3)) == [1, 19, 16]
    assert growth([1, 9, 2], 2, Fraction(1)) == [1, 20, 15]
    assert not any(inversion_row(s) == [1, 20, 15]
                   for s in canonical_vectors(36, 3))

    endpoint_cases = [(N, R) for N in range(1, 5) for R in range(2, 7)]
    endpoint_cases += [(5, 2), (5, 3)]
    endpoint_words = 0
    for N, R in endpoint_cases:
        words = list(colored_words((1,) * N, (R,) * N))
        extreme, interior = [], []
        for w in words:
            z = complement(w, N, R)
            assert complement(z, N, R) == w
            assert sorted(s for c, s in z) == list(range(N))
            assert all(1 <= c <= R for c, s in z)
            if w[-1][0] in (1, R):
                assert z[-1][0] in (1, R)
                assert descents(w, N) + descents(z, N) == N
                extreme.append(w)
            else:
                assert 1 < z[-1][0] < R
                assert descents(w, N) + descents(z, N) == N + 1
                interior.append(w)
            endpoint_words += 1
        h = row(words, N, N)
        a, b = decomposition(h)
        assert a == row(extreme, N, N)
        assert [0] + b == row(interior, N, N)

    square_orbits = pair_orbits = 0
    one_letter_controls = 0
    for R in range(2, 21):
        single = list(colored_words((1,), (R,)))
        a, b = decomposition(row(single, 1, 1))
        assert a == [1, 1] and b == [R - 2]
        assert gamma(a) == [1] and gamma(b) == [R - 2]
        one_letter_controls += 1
    for R in range(2, 11):
        words = list(colored_words((1, 1), (R, R)))
        square = {((c, 0), (c, 1)) for c in (1, R)}
        square |= {((c, 1), (c, 0)) for c in (1, R)}
        assert row(square, 2, 2) == [1, 2, 1]
        # These two commuting toggles give an actual transitive Boolean square.
        for w in square:
            symbol_toggle = tuple((c, 1 - s) for c, s in w)
            color_toggle = tuple((R + 1 - c, s) for c, s in w)
            assert symbol_toggle in square and color_toggle in square
            assert tuple((R + 1 - c, 1 - s) for c, s in w) in square
        square_orbits += 1
        rest = [w for w in words if w[-1][0] in (1, R) and w not in square]
        assert len(rest) == 4 * (R - 1) and all(descents(w, 2) == 1 for w in rest)
        unseen = {w for w in words if 1 < w[-1][0] < R}
        count = 0
        while unseen:
            w = unseen.pop()
            z = complement(w, 2, R)
            assert z != w and z in unseen
            unseen.remove(z)
            assert sorted([descents(w, 2), descents(z, 2)]) == [1, 2]
            count += 1
        assert count == R * (R - 2)
        pair_orbits += count
        a, b = decomposition(row(words, 2, 2))
        assert gamma(a) == [1, 4 * (R - 1)]
        assert gamma(b) == [R * (R - 2)]

    repeated = list(colored_words((2, 1), (3, 3)))
    a, b = decomposition(row(repeated, 2, 3))
    assert a == [1, 35, 35, 1] and b == [1, 7, 1]
    assert row([w for w in repeated if w[-1][0] in (1, 3)], 2, 3) == [1, 31, 22, 0]
    assert row([w for w in repeated if w[-1][0] == 2], 2, 3) == [0, 5, 20, 2]
    assert gamma(a) == [1, 32] and gamma(b) == [1, 5]
    two = list(colored_words((1, 1), (3, 3)))
    assert row([w for w in two if all(c == 1 for c, s in w)], 2, 2) == [1, 1, 0]
    a, b = decomposition(row(two, 2, 2))
    assert gamma(a) == [1, 8] and gamma(b) == [3]
    a, b = decomposition(ehrhart_numerator((1,) * 4, (2,) * 4))
    assert gamma(a) == [1, 72, 80] and not any(b)
    disc = 72 ** 2 - 4 * 80
    assert disc == 256 * 19 and isqrt(disc) ** 2 != disc
    formal = growth([1, 2, 1], 2, Fraction(3, 2))
    assert formal == [1, Fraction(17, 2), 8, Fraction(1, 2)]
    a, b = decomposition(formal)
    assert b == [Fraction(-1, 2), -1, Fraction(-1, 2)]
    assert gamma(b) == [Fraction(-1, 2), 0]

    reviewed = ['COLORED-RESULTS.md', 'Q1262-ATTEMPTS.md', 'Q1263-ATTEMPTS.md',
                'ENDPOINT-COLORS.md', 'colored_probe.py', 'check_colored_routes.py',
                'COLORED-PROBE.json', 'COLORED-ROUTES-CHECK.json']
    receipt = {
        'status': 'PASS',
        'independent_implementations': ['recursive colored multiset words',
            'literal inversion-sequence products', 'direct canonical factor/unit strings',
            'Fraction growth coefficients', 'wordwise endpoint involution and Boolean square'],
        'recorded_colored_cases': len(packet['cases']),
        'literal_colored_words': literal_word_controls,
        'canonical_candidates_recomputed': candidate_controls,
        'actual_multiplicity_growth_controls': growth_controls,
        'endpoint_cases': len(endpoint_cases), 'endpoint_wordwise_checks': endpoint_words,
        'two_letter_r_range': [2, 10], 'explicit_four_word_orbits': square_orbits,
        'explicit_interior_pair_orbits': pair_orbits,
        'one_letter_gamma_controls': one_letter_controls,
        'constant_case_checked_separately': True,
        'repeated_letter_extreme_row': [1, 31, 22, 0],
        'formal_basis_negative_gamma_eta0': '-1/2',
        'all_length_exclusions_depend_on_previously_reviewed_compression_theorem': True,
        'finite_checks_do_not_prove_full_classification_or_gamma_interpretation': True,
        'reviewed_sha256': {f: sha256((HERE / f).read_bytes()).hexdigest() for f in reviewed},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE / 'COLORED-REVIEW-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'reviewed_sha256'}, indent=2))


if __name__ == '__main__':
    main()
