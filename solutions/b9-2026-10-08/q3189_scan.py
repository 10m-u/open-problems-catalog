#!/usr/bin/env python3
"""Q3189 (Problem 2 + Conjecture 17 of arXiv:2510.24280v2), as preregistered.

For every S in scope and every pair of profiles X != Y and both coordinates c, D(h) = O_X(h)_c - O_Y(h)_c.
Records: whether D(h + 2 max S) = D(h) for every h in the final third of [0, H]; the first h after which that
holds through H (onset); max |D| overall and over the final third; and, if 2 max S fails, the least period
that holds over the final third. D_{Y,X} = -D_{X,Y}, so unordered pairs cover the ordered ones.
"""
import itertools
import json
import sys
from subtraction import outcomes, PROFILES

PAIRS = list(itertools.combinations(PROFILES, 2))


def analyse(S, H):
    o = outcomes(S, H)
    P = 2 * max(S)
    lo = 2 * H // 3
    rows = []
    for X, Y in PAIRS:
        for c in (0, 1):
            D = [o[X][h][c] - o[Y][h][c] for h in range(H + 1)]
            ok = all(D[h + P] == D[h] for h in range(lo, H - P + 1))
            onset = None
            if ok:
                onset = H - P
                while onset > 0 and D[onset - 1 + P] == D[onset - 1]:
                    onset -= 1
            least = None
            if not ok:
                for q in range(1, (H - lo) // 3):
                    if all(D[h + q] == D[h] for h in range(lo, H - q + 1)):
                        least = q
                        break
            rows.append({'X': X, 'Y': Y, 'coord': c + 1, 'period_2maxS': ok, 'onset': onset,
                         'max_abs': max(abs(d) for d in D), 'max_abs_final_third': max(abs(d) for d in D[lo:]),
                         'nonzero': any(D), 'least_period_if_fail': least})
    return rows


def main(H=6000):
    sets = [(a, b) for b in range(2, 41) for a in range(1, b)]
    sets += [t for t in itertools.combinations(range(1, 19), 3)]
    summary = {'H': H, 'sets_two': 0, 'sets_three': 0, 'fail_sets': [], 'onset_max': 0, 'onset_argmax': None,
               'max_abs': 0, 'max_abs_set': None, 'growth_flags': [], 'sets_with_any_discrepancy': 0}
    detail = {}
    for S in sets:
        rows = analyse(S, H)
        key = ','.join(map(str, S))
        summary['sets_two' if len(S) == 2 else 'sets_three'] += 1
        if any(r['nonzero'] for r in rows):
            summary['sets_with_any_discrepancy'] += 1
        bad = [r for r in rows if not r['period_2maxS']]
        if bad:
            summary['fail_sets'].append({'S': S, 'rows': bad})
        for r in rows:
            if r['onset'] is not None and r['onset'] > summary['onset_max']:
                summary['onset_max'], summary['onset_argmax'] = r['onset'], (S, r['X'], r['Y'], r['coord'])
            if r['max_abs'] > summary['max_abs']:
                summary['max_abs'], summary['max_abs_set'] = r['max_abs'], (S, r['X'], r['Y'], r['coord'])
            if r['max_abs_final_third'] < r['max_abs'] and False:
                pass
        detail[key] = rows
    summary['n_fail_sets'] = len(summary['fail_sets'])
    with open(f'q3189_scan_H{H}.json', 'w') as fh:
        json.dump({'summary': summary, 'detail': detail}, fh)
    print(json.dumps({k: v for k, v in summary.items() if k != 'fail_sets'}, indent=1))
    print('fail sets (first 10):', [f['S'] for f in summary['fail_sets'][:10]])


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 6000)
