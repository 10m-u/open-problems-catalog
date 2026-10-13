#!/usr/bin/env python3
"""Finite controls for the explicit lower construction; no external libraries."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path


def setup(n: int):
    points = list(product(range(3), repeat=n))
    index = {x:i for i,x in enumerate(points)}
    plus = [[index[tuple((a+b)%3 for a,b in zip(x,y))] for y in points] for x in points]
    return points, index, plus


def all_affine_subspaces(n: int, plus: list[list[int]]) -> list[tuple[frozenset[int], int]]:
    size = 3**n
    levels: list[set[frozenset[int]]] = [{frozenset([0])}]
    for dim in range(n):
        enlarged: set[frozenset[int]] = set()
        for space in levels[-1]:
            for x in range(size):
                if x in space:
                    continue
                twice = plus[x][x]
                enlarged.add(frozenset(set(space) | {plus[a][x] for a in space} | {plus[a][twice] for a in space}))
        levels.append(enlarged)
    flats = []
    for dim, spaces in enumerate(levels):
        for space in spaces:
            translates = {frozenset(plus[a][t] for a in space) for t in range(size)}
            flats.extend((flat,dim) for flat in translates)
    return flats


def main() -> None:
    results = []
    for n in (3,4):
        points, index, plus = setup(n)
        flats = all_affine_subspaces(n, plus)
        cases = [(k,1) for k in range(1,n+1)] + ([(2,2)] if n == 4 else [])
        for k,d in cases:
            colours = [[] for _ in range(k)]
            remainder = set()
            for idx,x in enumerate(points):
                zero_blocks = [i for i in range(k) if all(v == 0 for v in x[i*d:(i+1)*d])]
                if zero_blocks:
                    colours[zero_blocks[0]].append(idx)
                else:
                    remainder.add(idx)
            assert len(remainder) == (3**d-1)**k*3**(n-k*d)
            checks = 0
            for colour in colours:
                for x in colour:
                    for y in colour:
                        s = plus[x][y]
                        midpoint = plus[s][s]
                        assert midpoint not in remainder
                        checks += 1
            maximum = max(dim for flat,dim in flats if flat <= remainder)
            assert maximum == n-k
            results.append({'n':n,'k':k,'block_dimension':d,
                            'ambient_size':len(points),'remainder_size':len(remainder),
                            'all_affine_subspaces_examined':len(flats),
                            'monochromatic_ordered_pair_checks':checks,
                            'largest_affine_subspace_dimension':maximum})
    receipt = {'status':'passed', 'field':3,'cases':results,
               'scope':'Finite controls only. The manuscript proves the block construction for all admissible n,k,d.'}
    output = Path(__file__).with_name('BLOCK-CONSTRUCTION-CHECKS.json')
    output.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__ == '__main__':
    main()
