"""Littlewood--Richardson products by literal ballot skew tableaux."""
from functools import lru_cache


def partitions(n, cap=None, length=None):
    if n == 0:
        yield ()
        return
    cap = n if cap is None else cap
    length = n if length is None else length
    if length == 0:
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n-first, first, length-1):
            yield (first,)+rest


def trim(a):
    a = tuple(a)
    while a and a[-1] == 0:
        a = a[:-1]
    return a


def midpoint(a, b):
    m = max(len(a), len(b))
    sums = [(a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0) for i in range(m)]
    return trim([(x+1)//2 for x in sums]), trim([x//2 for x in sums])


@lru_cache(None)
def lr_coefficient(a, b, v):
    aa = a+(0,)*(len(v)-len(a))
    if len(v) < len(a) or any(x > y for x, y in zip(aa, v)):
        return 0
    cells = [(i, j) for i, row in enumerate(v) for j in range(row-1, aa[i]-1, -1)]
    if len(cells) != sum(b):
        return 0
    if not b:
        return int(not cells)
    if len(b) == 1:
        return int(len({j for i,j in cells}) == len(cells))
    filling, used = {}, [0]*len(b)

    def visit(pos):
        if pos == len(cells):
            return 1
        i, j = cells[pos]
        low = filling.get((i-1,j), 0)+1
        high = filling.get((i,j+1), len(b))
        total = 0
        for value in range(low, high+1):
            ix = value-1
            if used[ix] >= b[ix] or (ix and used[ix]+1 > used[ix-1]):
                continue
            filling[i,j] = value
            used[ix] += 1
            total += visit(pos+1)
            used[ix] -= 1
            del filling[i,j]
        return total

    return visit(0)


@lru_cache(None)
def product(a, b):
    # Fill the smaller content to limit branching, using LR symmetry.
    if sum(a) < sum(b):
        a, b = b, a
    if not b:
        return {a:1}
    total = sum(a)+sum(b)
    out = {}
    for v in partitions(total, a[0]+b[0], len(a)+len(b)):
        if len(v) < len(a) or any(v[i] < a[i] for i in range(len(a))):
            continue
        value = lr_coefficient(a,b,v)
        if value:
            out[v] = value
    return out
