#!/usr/bin/env python3
"""Self-interest cumulative subtraction games (Bhagat–Kulkarni–Larsson–Murali, arXiv:2510.24280v2).

Definition 2 of the source, as preregistered: profiles X in {FvF, FvA, AvF, AvA}; the first letter is the
tie-breaking rule of the player to move. Below min S both coordinates are 0. Otherwise the mover takes
o1_X(h) = max_s [s + o2_{d(X)}(h-s)], and among the maximizers breaks ties by minimizing (antagonistic) or
maximizing (friendly) the opponent's resulting cumulation o1_{d(X)}(h-s). z(h) is the zero-sum value.
"""
PROFILES = ('FvF', 'FvA', 'AvF', 'AvA')
DUAL = {'FvF': 'FvF', 'FvA': 'AvF', 'AvF': 'FvA', 'AvA': 'AvA'}


def outcomes(S, H):
    S = sorted(S)
    o = {X: [(0, 0)] * (H + 1) for X in PROFILES}
    for h in range(S[0], H + 1):
        for X in PROFILES:
            D = DUAL[X]
            moves = [s for s in S if s <= h]
            mine = {s: s + o[D][h - s][1] for s in moves}
            best = max(mine.values())
            tied = [s for s in moves if mine[s] == best]
            theirs = [o[D][h - s][0] for s in tied]
            other = min(theirs) if X[0] == 'A' else max(theirs)
            o[X][h] = (best, other)
    return o


def zero_sum(S, H):
    S = sorted(S)
    z = [0] * (H + 1)
    for h in range(S[0], H + 1):
        z[h] = max(s - z[h - s] for s in S if s <= h)
    return z


if __name__ == '__main__':
    o = outcomes({3, 5}, 15)
    table_ffv = [(0,0),(0,0),(0,0),(3,0),(3,0),(5,0),(5,0),(5,0),(5,3),(5,3),(5,5),(6,5),(6,5),(8,5),(8,6),(10,5)]
    table_ava = table_ffv[:14] + [(8, 5), (10, 5)]
    assert o['FvF'] == table_ffv, o['FvF']
    assert o['AvA'] == table_ava, o['AvA']
    print('Table 1 of the source reproduced for S={3,5}, h<=15.')
