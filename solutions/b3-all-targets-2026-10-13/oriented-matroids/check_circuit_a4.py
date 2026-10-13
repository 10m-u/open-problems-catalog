#!/usr/bin/env python3
"""Exact fractional-gauge shells and free-sum Ehrhart numerator control."""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def main():
    receipt = json.loads((HERE/'CIRCUIT-A2-CHECK.json').read_text())
    case = receipt['cases'][1]
    assert case['missing'] == [[0, 1]]
    facets = case['complete_primitive_facet_inequalities']
    assert set(f[-1] for f in facets) == {1, 2}
    shells = Counter()
    for z in product(range(-8, 9), repeat=4):
        twice_gauge = max(2*sum(a*x for a, x in zip(f[:-1], z))//f[-1]
                          for f in facets)
        if twice_gauge <= 16:
            shells[twice_gauge] += 1
    assert shells[0] == 1 and shells[1] == 0 and shells[3] == 2
    base_counts = [sum(v for g, v in shells.items() if g <= 2*m)
                   for m in range(9)]
    assert base_counts[:5] == case['ehrhart_counts_0_to_4']
    counts = [sum(va*vb for a, va in shells.items() for b, vb in shells.items()
                  if a+b <= 2*m) for m in range(9)]
    integer_prediction = [sum(va*vb for a, va in shells.items()
                              for b, vb in shells.items()
                              if (a+1)//2+(b+1)//2 <= m) for m in range(9)]
    h = [sum((-1)**j*comb(9, j)*counts[i-j] for j in range(i+1))
         for i in range(9)]
    expected_h = [sum(case['h_star'][j]*case['h_star'][i-j]
                     for j in range(5) if 0 <= i-j < 5) for i in range(9)]
    predicted_h = [sum((-1)**j*comb(9, j)*integer_prediction[i-j]
                       for j in range(i+1)) for i in range(9)]
    assert predicted_h == expected_h
    assert counts[:3] == integer_prediction[:3]
    assert counts[3] == integer_prediction[3]+4
    assert h[3] == expected_h[3]+4 == 3128
    assert h != expected_h
    defects = [h[i]**2-h[i-1]*h[i+1] for i in range(1, 8)]
    assert all(v >= 0 for v in h)
    result = {
        'status': 'PASS', 'base': 'dual graphical K5 minus edge01',
        'actual_direct_sum_ground_set_size': 18, 'dimension': 8,
        'twice_gauge_shells': dict(sorted(shells.items())),
        'actual_free_sum_lattice_counts': counts,
        'integer_split_prediction': integer_prediction,
        'actual_h_star': h, 'incorrect_product_h_star': expected_h,
        'log_concavity_defects': defects,
        'scope': 'Actual free-sum row and fractional-carry obstruction, not a universal non-LC claim.',
        'facet_input_sha256': sha256((HERE/'CIRCUIT-A2-CHECK.json').read_bytes()).hexdigest(),
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'CIRCUIT-A4-CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['status','actual_h_star',
        'incorrect_product_h_star','log_concavity_defects']}, indent=2))


if __name__ == '__main__':
    main()
