#!/usr/bin/env python3
"""Independent multiplication-matrix check for Q3893's source example.

This constructs standard monomials as tuples of vertex states (none,x,y),
not by importing the solution's quotient/certificate implementation.
All ranks use exact finite-field elimination. The p=101 rank together
with the proof's kernel bound also determines the characteristic-zero rank.
"""
from itertools import product, combinations
import json


def monomials(n, edges, degree):
    result = []
    for word in product(range(3), repeat=n):
        if sum(state != 0 for state in word) != degree:
            continue
        if any(word[i] == word[j] == 1 for i, j in edges):
            continue
        result.append(word)
    return result


def multiplication_columns(n, edges, degree):
    source, target = monomials(n, edges, degree), monomials(n, edges, degree + 1)
    positions = {word: i for i, word in enumerate(target)}
    columns = []
    for word in source:
        column = {}
        for i in range(n):
            if word[i] != 0:
                continue
            for state in (1, 2):
                candidate = word[:i] + (state,) + word[i + 1:]
                if candidate in positions:
                    column[positions[candidate]] = 1
        columns.append(column)
    return len(source), len(target), columns


def rank_mod(columns, p):
    pivots = {}
    for initial in columns:
        column = dict(initial)
        while column:
            pivot = min(column)
            if pivot not in pivots:
                inverse = pow(column[pivot], -1, p)
                pivots[pivot] = {j: value * inverse % p for j, value in column.items()}
                break
            scale = column[pivot]
            for j, value in pivots[pivot].items():
                entry = (column.get(j, 0) - scale * value) % p
                if entry:
                    column[j] = entry
                else:
                    column.pop(j, None)
    return len(pivots)


def main():
    n = 8
    edges = tuple((i, j) for i, j in combinations(range(n), 2)
                  if not (i < 3 and j < 3))
    source_size, target_size, columns = multiplication_columns(n, edges, 4)
    if (source_size, target_size) != (400, 406):
        raise RuntimeError('source-example dimensions do not match')
    ranks = {str(p): rank_mod(columns, p) for p in (2, 3, 101)}
    if ranks['101'] != 386 or any(value >= min(source_size, target_size) for value in ranks.values()):
        raise RuntimeError('rank checks failed')
    print(json.dumps({'graph': 'K8 with the three edges on vertices 0,1,2 removed',
                      'source_degree': 4, 'dimensions': [source_size, target_size],
                      'ranks_mod_prime': ranks,
                      'char_zero_rank': 386,
                      'char_zero_rank_reason': 'rank mod 101 is 386; the proved 14-dimensional kernel gives the matching upper bound'}, indent=2))


if __name__ == '__main__':
    main()
