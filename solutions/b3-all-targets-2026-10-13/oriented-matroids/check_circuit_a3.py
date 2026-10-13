#!/usr/bin/env python3
"""Exact all-size facet witness controls; no claimed global Ehrhart theorem."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
from check_circuit_a2 import bonds

HERE = Path(__file__).resolve().parent


def row_rank(rows):
    rows = [list(map(Fraction, r)) for r in rows]
    k = 0
    for c in range(len(rows[0]) if rows else 0):
        ix = next((i for i in range(k, len(rows)) if rows[i][c]), None)
        if ix is None:
            continue
        rows[k], rows[ix] = rows[ix], rows[k]
        s = rows[k][c]
        rows[k] = [v/s for v in rows[k]]
        for i in range(k+1, len(rows)):
            s = rows[i][c]
            rows[i] = [v-s*w for v, w in zip(rows[i], rows[k])]
        k += 1
    return k


def main():
    cases = []
    for n in range(4, 11):
        edges = [e for e in combinations(range(n), 2) if e != (0, 1)]
        vertices, _ = bonds(n, edges)
        normal = (n-3, 1)+(-1,)*(n-3)
        rhs = n-3
        assert all(sum(a*x for a, x in zip(normal, v)) <= rhs for v in vertices)
        ea = (1,)+(0,)*(n-2)
        face = [ea]
        for j in range(2, n-1):
            face.append(tuple(int(i in (0, 1, j)) for i in range(n-1)))
        face.append((0, 0)+(-1,)*(n-3))
        assert len(face) == n-1 and all(v in vertices for v in face)
        assert all(sum(a*x for a, x in zip(normal, v)) == rhs for v in face)
        assert row_rank([[v-a for v, a in zip(p, face[0])] for p in face[1:]]) == n-2
        polar = [str(Fraction(a, rhs)) for a in normal]
        assert (rhs == 1) == all(Fraction(a, rhs).denominator == 1 for a in normal)
        cases.append({'N': n, 'ground_set_size': len(edges),
                      'dimension': n-1, 'facet_normal': normal,
                      'facet_rhs': rhs, 'polar_vertex': polar,
                      'independent_face_vertices': face})
    result = {'status': 'PASS', 'families_N4_to_N10': cases,
              'all_size_obstruction': 'For every N>=5 the primitive facet has distance N-3>1.',
              'full_target_scope': 'Universal reflexive/gamma certificate fails; LC remains open.',
              'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'CIRCUIT-A3-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'PASS', 'families': len(cases),
                      'facet_distances': [r['facet_rhs'] for r in cases]}, indent=2))


if __name__ == '__main__':
    main()
