#!/usr/bin/env python3
"""Exact exhaustive certificate for the symmetric-interval APP lemma, 2q<=8.

No external dependencies; regenerate checks.json beside this script.
The exhaustive part enumerates *all distinct intersections* of interval-band
predicates, rather than sampled bound lists. An empty intersection from an
impossible negative bandwidth is handled separately and satisfies 0>=0.
"""
from hashlib import sha256
from itertools import product
from math import comb, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def generators(n):
    out = set()
    for a in range(n):
        for b in range(a + 1, n + 1):
            length = b - a
            interval = ((1 << length) - 1) << a
            # Bounds >=length are vacuous; odd/even lower bounds round down
            # to the largest value of the same parity as length.
            for bandwidth in range(length % 2, length, 2):
                allowed = sum(1 << x for x in range(1 << n)
                              if abs(2 * (x & interval).bit_count() - length)
                              <= bandwidth)
                out.add(allowed)
    return sorted(out)


def exhaustive_app(n):
    full = (1 << (1 << n)) - 1
    families = {full}
    gs = generators(n)
    for allowed in gs:
        # After j generators, these are precisely the intersections of all
        # subsets of the first j generators: induction gives completeness.
        families.update(f & allowed for f in tuple(families))
    q = n // 2
    middle = sum(1 << x for x in range(1 << n) if x.bit_count() == q)
    below = sum(1 << x for x in range(1 << n) if x.bit_count() == q - 1)
    failures = []
    equality = 0
    for family in families:
        c = (family & middle).bit_count()
        b = (family & below).bit_count()
        slack = q * c - (q + 1) * b
        if slack < 0:
            failures.append({"family_hex": hex(family), "c_q": c,
                             "c_q_minus_1": b, "slack": slack})
        equality += slack == 0
    canonical = "\n".join(format(f, "x") for f in sorted(families)) + "\n"
    return {"dimension": n, "generators": len(gs),
            "distinct_nonempty_families": len(families),
            "empty_family_passes": True, "exhaustive": True,
            "equality_cases": equality, "failures": failures,
            "sorted_family_hex_sha256": sha256(canonical.encode()).hexdigest()}


def rank_counts(n, intervals, weights=None):
    weights = [1] * n if weights is None else weights
    row = [0] * (n + 1)
    members = []
    for x in range(1 << n):
        if all(lo <= ((x >> a) & ((1 << (b-a))-1)).bit_count() <= hi
               for a, b, lo, hi in intervals):
            members.append(x)
            row[x.bit_count()] += prod(weights[i] for i in range(n) if x >> i & 1)
    return row, members


def ulc(row):
    n = len(row) - 1
    return all(k * (n-k) * row[k] ** 2 >=
               (k+1) * (n-k+1) * row[k-1] * row[k+1]
               for k in range(1, n))


def matching_obstruction():
    bounds = [(0, 2, 1, 1), (1, 3, 1, 1),
              (3, 5, 1, 1), (4, 6, 1, 1)]
    row, members = rank_counts(6, bounds)
    lower = [x for x in members if x.bit_count() == 2]
    middle = [x for x in members if x.bit_count() == 3]
    edges = [(a, b) for a in lower for b in middle if a & b == a]
    assert row == [0, 0, 1, 2, 1, 0, 0]
    assert len(lower) == 1 and len(middle) == 2 and not edges
    assert 3 * row[3] >= 4 * row[2]
    return {"dimension": 6, "zero_based_half_open_bounds": bounds,
            "rank_counts": row, "lower_rank_masks": lower,
            "middle_rank_masks": middle, "inclusion_edges": edges,
            "refuted_statement": "Every rank q-1 feasible word can be extended by adding one 1 to a rank q feasible word",
            "central_APP_still_passes": True}


def elementary_controls():
    weighted_cases = 0
    # Boundary-rich interval examples; exhaustive APP, not these instances,
    # supplies the all-weight theorem for m<=9.
    for n in range(1, 10):
        for ell in range(1, min(4, n + 1)):
            bounds = [(max(0, v-ell), min(n, v+ell+1), 1, n)
                      for v in range(n)]
            for weights in ([1] * n, [1 + i % 3 for i in range(n)],
                            [0 if i % 4 == 0 else i + 1 for i in range(n)]):
                row, _ = rank_counts(n, bounds, weights)
                assert ulc(row), (n, ell, weights, row)
                weighted_cases += 1
    # Coefficientwise ULC already fails for two independent variables.
    # (w1+w2)^2 -4*w1*w2=(w1-w2)^2, numerically >=0 but has -2 w1 w2.
    assert (1 + 3) ** 2 - 4 * 1 * 3 == (1-3) ** 2
    return {"weighted_path_power_controls": weighted_cases,
            "coefficientwise_ULC_obstruction":
            {"dimension": 2, "central_defect": "w1^2 - 2*w1*w2 + w2^2",
             "negative_mixed_coefficient": -2,
             "numerical_nonnegativity": "(w1-w2)^2 >= 0"}}


def main():
    app = [exhaustive_app(n) for n in (2, 4, 6, 8)]
    assert [x["distinct_nonempty_families"] for x in app] == [2, 16, 377, 32554]
    assert all(not x["failures"] for x in app)
    results = {"scope": "Complete symmetric interval-band families in even dimensions 2,4,6,8; exact integers",
               "central_inequality": "q*c_q >= (q+1)*c_(q-1)",
               "exhaustive_certificates": app,
               "matching_obstruction": matching_obstruction(),
               "controls": elementary_controls(),
               "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
               "passed": True}
    (HERE / "checks.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({"passed": True, "families_by_dimension":
                      [x["distinct_nonempty_families"] for x in app]}))


if __name__ == "__main__":
    main()
