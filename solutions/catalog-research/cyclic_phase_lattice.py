#!/usr/bin/env python3
"""Exact low-degree phase-fibre diagnostics for real cyclic signals.

Requires SymPy. The support must be invariant under k -> -k modulo n.
DC is recovered at degree one and omitted from the phase lattice. Diagnostics
start at degree two, where the power spectrum fixes support and amplitudes.
"""

import argparse
from itertools import combinations_with_replacement
import json
from math import gcd, prod

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def relation_columns(n, support, degree):
    support = tuple(sorted(set(support) - {0}))
    if n < 2 or any(k < 1 or k >= n for k in support):
        raise ValueError("n >= 2 and frequencies in [0,n) are required")
    if set(support) != {(-k) % n for k in support}:
        raise ValueError("real signals require conjugate-symmetric support")
    if degree < 2:
        raise ValueError("the phase criterion starts at degree two")
    position = {k: i for i, k in enumerate(support)}
    relations = set()
    for k in support:
        row = [0] * len(support)
        row[position[k]] += 1
        row[position[(-k) % n]] += 1
        relations.add(tuple(row))
    for size in range(1, degree + 1):
        for frequencies in combinations_with_replacement(support, size):
            if sum(frequencies) % n:
                continue
            row = [0] * len(support)
            for k in frequencies:
                row[position[k]] += 1
            relations.add(tuple(row))
    return support, sorted(relations)


def profile(n, support, degree):
    support, columns = relation_columns(n, support, degree)
    r = len(support)
    if r:
        matrix = Matrix(r, len(columns), lambda i, j: columns[j][i])
        normal = smith_normal_form(matrix, domain=ZZ)
        factors = [abs(int(normal[i, i])) for i in range(min(normal.shape))
                   if normal[i, i] != 0]
    else:
        factors = []
    dimension = r - len(factors)
    index = prod(factors) if dimension == 0 else None
    orbit_size = n // gcd(n, *support)
    assert index is None or index % orbit_size == 0
    return {
        "n": n, "support_without_dc": list(support), "degree": degree,
        "relation_count": len(columns), "smith_factors": factors,
        "torus_dimension": dimension, "translation_orbit_size": orbit_size,
        "phase_fibre_size": index,
        "orbit_count": index // orbit_size if index is not None else None,
        "list_resolves": dimension == 0,
        "uniquely_resolves": index == orbit_size,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("--support", required=True,
                        help="comma-separated nonzero Fourier frequencies")
    parser.add_argument("--max-degree", type=int, default=4)
    args = parser.parse_args()
    support = [int(k) for k in args.support.split(",") if k.strip()]
    print(json.dumps([profile(args.n, support, d)
                      for d in range(2, args.max_degree + 1)], indent=2))


if __name__ == "__main__":
    main()
