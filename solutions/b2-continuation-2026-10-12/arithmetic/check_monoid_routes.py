#!/usr/bin/env python3
"""Complete bounded power-set/S3 controls and rational MCD checks."""
from functools import lru_cache
from itertools import permutations, product
from fractions import Fraction
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def power_sets(limit=12):
    by_max = [[1]] + [[m for m in range(1 << n, 1 << (n+1)) if m & 1]
                     for n in range(1, limit+1)]
    decompositions = {}
    pairs = 0
    for a in range(1, limit):
        for b in range(1, limit-a+1):
            for A in by_max[a]:
                for B in by_max[b]:
                    if A > B:
                        continue
                    C = 0
                    for j in range(b+1):
                        if B >> j & 1:
                            C |= A << j
                    decompositions.setdefault(C, []).append((A, B))
                    pairs += 1
    lengths = {1: {0}}
    witnesses = {}
    for group in by_max[1:]:
        for A in group:
            factors = decompositions.get(A, [])
            lengths[A] = {x+y for B,C in factors for x in lengths[B] for y in lengths[C]} if factors else {1}
            key = tuple(sorted(lengths[A]))
            witnesses.setdefault(key, [j for j in range(limit+1) if A >> j & 1])
    def mask(values):
        return sum(1 << v for v in values)
    assert lengths[mask([0,1,3])] == lengths[mask([0,2,3])] == {1}
    assert 2 in lengths[mask(range(7))] and 6 in lengths[mask(range(7))]
    assert lengths[mask([0,1,2])] == lengths[mask([0,2,4])] == {2}
    assert lengths[mask([0,1,2,4])] == {1}
    return dict(maximum=limit, normalized_sets=len(lengths), decompositions=pairs,
                distinct_length_sets=len(witnesses),
                atom_sum_lengths=sorted(lengths[mask(range(7))]),
                union_control_lengths=sorted(lengths[mask([0,1,2,4])]),
                length_set_witnesses={','.join(map(str,k)):v for k,v in sorted(witnesses.items())})


def vectors(total, dimensions=6):
    if dimensions == 1:
        yield (total,)
    else:
        for n in range(total+1):
            for tail in vectors(total-n, dimensions-1):
                yield (n,) + tail


def s3():
    group = list(permutations(range(3)))
    identity = group.index((0,1,2))
    table = [[group.index(tuple(a[b[i]] for i in range(3))) for b in group] for a in group]

    @lru_cache(None)
    def ordering_products(counts):
        if not any(counts):
            return frozenset([identity])
        possible = set()
        for g, count in enumerate(counts):
            if count:
                old = list(counts)
                old[g] -= 1
                possible.update(table[x][g] for x in ordering_products(tuple(old)))
        return frozenset(possible)

    def contained(a, b):
        return all(x <= y for x,y in zip(a,b))

    product_one = {n:[v for v in vectors(n) if identity in ordering_products(v)] for n in range(1,7)}
    def free(c):
        return not any(contained(t,c) for n in range(1,sum(c)+1) for t in product_one[n])
    free3 = [c for c in vectors(3) if free(c)]
    assert free3 and not any(free(c) for c in vectors(4))
    bad8 = [c for c in vectors(8) if not any(contained(t,c) for t in product_one[6])]
    assert bad8 and all(any(contained(t,c) for t in product_one[6]) for c in vectors(9))
    tau = group.index((1,0,2))
    sigma = group.index((1,2,0))
    seq = [identity]*5 + [sigma]
    counts = tuple(seq.count(g) for g in range(6))
    assert identity not in ordering_products(counts)
    assert not any(sum(x)==6 for x in product([0,2],[0,2],[0,3]))
    value = identity
    for g in (tau,tau,tau,sigma,tau,sigma):
        value = table[value][g]
    assert value == identity
    return dict(davenport_small=3, gao_constant=9, group_order=6,
                permutations=[list(g) for g in group],
                all_length4_multisets=sum(1 for _ in vectors(4)),
                all_length8_multisets=sum(1 for _ in vectors(8)),
                all_length9_multisets=sum(1 for _ in vectors(9)),
                product_one_free_length3=list(free3[0]),
                no_length6_product_one_witness=list(bad8[0]),
                checked_ordering_states=ordering_products.cache_info().currsize,
                greedy_block_countercontrol=True, quotient_countercontrol=True)


def reciprocal_mcd():
    primes = (3,5,7)
    denominator = 105
    def canon(q):
        numerator = q * denominator
        assert numerator.denominator == 1
        residues = tuple(int(numerator)*pow(denominator//p,-1,p)%p for p in primes)
        integer = q - sum((Fraction(r,p) for r,p in zip(residues,primes)),Fraction(0))
        assert integer.denominator == 1
        return int(integer),residues
    def member(q):
        return canon(q)[0] >= 0
    def value(r):
        return sum((Fraction(x,p) for x,p in zip(r,primes)),Fraction(0))
    rng = random.Random(221713)
    cases = 0
    for _ in range(400):
        S = [Fraction(rng.randrange(4))+value(tuple(rng.randrange(p) for p in primes))
             for _ in range(rng.randrange(1,6))]
        h = min(canon(q)[0] for q in S)
        residual = [q-h for q in S]
        q0 = next(q for q in residual if canon(q)[0] == 0)
        residues = canon(q0)[1]
        divisors = [value(r) for r in product(*(range(x+1) for x in residues))]
        common = [e for e in divisors if all(member(q-e) for q in residual)]
        e = max(common)
        assert all(member(q-h-e) for q in S)
        assert not any(c>0 and all(member(q-e-c) for q in residual) for c in divisors)
        for d in divisors:
            assert member(d) and member(q0-d)
        cases += 1
    return dict(primes=list(primes),finite_sets_checked=cases,
                canonical_divisor_and_mcd_controls=True,
                scope='Finite residue controls for the written all-prime MCD theorem.')


def half_factorial():
    def minimal(sequence):
        return sum(sequence)%3 == 0 and not any(sum(sequence[i] for i in range(len(sequence)) if mask>>i&1)%3 == 0
            for mask in range(1,(1<<len(sequence))-1))
    assert all(minimal(x) for x in ((1,1,1),(2,2,2),(1,2)))
    assert sorted((1,1,1)+(2,2,2)) == sorted((1,2)*3)
    return dict(c3_atoms_verified=3, unequal_lengths=[2,3],
                all_countable_scope='Sourced prior theorem, not established by this finite check.')


def main():
    result = dict(status='passed', power=power_sets(), s3=s3(),
                  reciprocal_mcd=reciprocal_mcd(), half_factorial=half_factorial(),
                  scope='Complete stated finite domains and rational controls; universal targets remain unresolved.')
    (HERE/'MONOID-CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    brief = {**result,'power':{k:v for k,v in result['power'].items() if k!='length_set_witnesses'}}
    print(json.dumps(brief,indent=2))


if __name__ == '__main__':
    main()
