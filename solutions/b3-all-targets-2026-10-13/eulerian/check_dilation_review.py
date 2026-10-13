#!/usr/bin/env python3
"""Independent E06 controls using the retained agent's literal enumerators."""
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json

from check_colored_review import (canonical_vectors, colored_words, descents,
                                  ehrhart_numerator, inversion_row, trim)

HERE = Path(__file__).resolve().parent


def two_coordinate_formula(a, b):
    return trim([1, (a*b+a+b+gcd(a,b)-4)//2,
                 ((a-1)*(b-1)-gcd(a,b)+1)//2])


def literal_colored_row(a, b):
    h = [0, 0, 0]
    for w in colored_words((1, 1), (a, b)):
        h[descents(w, 2)] += 1
    return trim(h)


def main():
    recorded = json.loads((HERE/'DILATION-CHECK.json').read_text())
    candidates = list(canonical_vectors(40, 3))
    rows = {s: inversion_row(s) for s in candidates}
    assert len(rows) == 22
    assert all(h != [1, 27, 12] for h in rows.values())
    assert rows == {tuple(r['s']): r['row']
                    for r in recorded['all_candidate_rows']}
    assert literal_colored_row(4, 5) == [1, 27, 12]
    assert ehrhart_numerator((1, 1), (4, 5)) == [1, 27, 12]

    formula_controls = 0
    for a, b in product(range(1, 37), repeat=2):
        assert inversion_row((a, b)) == two_coordinate_formula(a, b)
        formula_controls += 1

    # Direct word counts independently match inversion products and Ehrhart
    # transformation; the written formula, rather than these t values, is
    # the all-size proof.
    family = []
    for t in range(1, 9):
        h = [1, 180*t*t+27*t-2, 180*t*t-27*t+1]
        assert literal_colored_row(12*t, 15*t) == h
        assert ehrhart_numerator((1, 1), (12*t, 15*t)) == h
        assert inversion_row((8*t, 45*t)) == h
        assert two_coordinate_formula(8*t, 45*t) == h
        family.append({'t': t, 'row': h})

    # Boundaries and padding: before dilation each leading unit contributes
    # zero; after dilation it becomes a genuine coordinate, as required by
    # matched-dimensional Ehrhart dilation.
    assert inversion_row((1, 1, 2, 3)) == inversion_row((2, 3))
    assert inversion_row((2, 2, 4, 6)) != inversion_row((4, 6))
    reviewed = ['DILATION-FAMILIES.md', 'Q1262-ATTEMPTS.md',
                'check_dilation.py', 'DILATION-CHECK.json',
                'check_colored_review.py']
    receipt = {
        'status': 'PASS',
        'canonical_volume40_candidate_count': len(rows),
        'primitive_input_unrepresentable_dependency':
            'Previously reviewed all-length degree-two compression theorem.',
        'primitive_row_by_literal_words': [1, 27, 12],
        'two_coordinate_formula_literal_controls': formula_controls,
        'family_literal_controls': family,
        'leading_units_dilate_into_genuine_coordinates_checked': True,
        'all_size_forward_dilation_and_family_proved_in_review': True,
        'accepted_new_failed_route': 'E06 primitive-ray equivalence',
        'rejected_route_stays_rejected': 'E01 finite recognizer rerun',
        'reviewed_sha256': {f: sha256((HERE/f).read_bytes()).hexdigest()
                            for f in reviewed},
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    (HERE/'DILATION-REVIEW-CHECK.json').write_text(
        json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: v for k, v in receipt.items()
                      if k != 'reviewed_sha256'}, indent=2))


if __name__ == '__main__':
    main()
