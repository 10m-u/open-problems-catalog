#!/usr/bin/env python3
"""Exact first-forbidden-rank RSK kernel controls; not a Hankel disproof."""
from collections import defaultdict
from itertools import permutations
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent


def rsk(word):
    P, Q = [], []
    for time, value in enumerate(word, 1):
        row = 0
        while True:
            if row == len(P):
                P.append([])
                Q.append([])
            col = next((i for i, old in enumerate(P[row]) if old > value), len(P[row]))
            if col == len(P[row]):
                P[row].append(value)
                Q[row].append(time)
                break
            P[row][col], value = value, P[row][col]
            row += 1
    return tuple(map(tuple, P)), tuple(map(tuple, Q))


def inverse(word):
    out = [0] * len(word)
    for i, value in enumerate(word, 1):
        out[value - 1] = i
    return tuple(out)


def standard(tableau):
    values = sorted(x for row in tableau for x in row)
    assert values == list(range(1, len(values) + 1))
    assert all(all(a < b for a, b in zip(row, row[1:])) for row in tableau)
    assert all(tableau[r][c] < tableau[r + 1][c]
               for r in range(len(tableau) - 1) for c in range(len(tableau[r + 1])))


def main():
    controls = involutions = nonsymmetric = 0
    explicit = None
    for n in range(2, 7):
        groups = defaultdict(dict)
        for word in permutations(range(1, n + 1)):
            P, Q = rsk(word)
            standard(P)
            standard(Q)
            assert rsk(inverse(word)) == (Q, P)
            shape = tuple(map(len, P))
            assert shape == tuple(map(len, Q))
            assert (P, Q) not in groups[shape]
            groups[shape][P, Q] = word
        for shape, pairs in groups.items():
            tableaux = {P for P, Q in pairs}
            assert tableaux == {Q for P, Q in pairs}
            assert set(pairs) == {(P, Q) for P in tableaux for Q in tableaux}
            for (P, Q), beta in pairs.items():
                monotone = beta in (tuple(range(1, n + 1)), tuple(range(n, 0, -1)))
                if monotone:
                    assert len(tableaux) == 1
                    continue
                assert len(tableaux) >= 2
                if P != Q:
                    assert beta != inverse(beta)
                    assert pairs[Q, P] != beta
                    nonsymmetric += 1
                else:
                    assert beta == inverse(beta)
                    S = next(T for T in tableaux if T != P)
                    assert all(pairs[A, B] != beta for A, B in [(P, S), (S, P), (S, S)])
                    assert 0 * 1 - 1 * 1 == -1
                    involutions += 1
                    if beta == (1, 3, 2, 4):
                        explicit = {'beta': beta, 'shape': shape, 'tableau_T': P,
                            'tableau_S': S, 'four_permutations': {
                                'TT': pairs[P, P], 'TS': pairs[P, S],
                                'ST': pairs[S, P], 'SS': pairs[S, S]},
                            'principal_avoidance_kernel': [[0, 1], [1, 1]],
                            'determinant': -1}
                controls += 1
    assert explicit is not None
    receipt = {'status': 'PASS', 'n_range': [2, 6],
        'nonmonotone_beta_first_rank_controls': controls,
        'noninvolution_nonsymmetric_kernels': nonsymmetric,
        'involution_negative_principal_minors': involutions,
        'actual_1324_witness': explicit,
        'scope': 'Failure of the literal RSK positive-kernel construction; not a negative avoidance Hankel minor.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'RSK-KERNEL-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
