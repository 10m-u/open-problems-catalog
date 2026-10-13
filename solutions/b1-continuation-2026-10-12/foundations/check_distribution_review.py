"""Direct finite-matrix audit, independent of the block derivation."""
import cmath
import json
import math
from pathlib import Path


def main():
    rows = []
    for w in range(1, 8):
        p = 1 << w
        direct = []
        for a in range(p):
            phase = [cmath.exp(-2j * math.pi * a * x / p) / p for x in range(p)]
            direct += [abs(sum(phase[x] * (-1 if (b & x).bit_count() % 2 else 1)
                               for x in range(p))) for b in range(p)]
        predicted = [1.0]
        for m in range(w):
            for d in range(1, 1 << (m + 1), 2):
                for mask in range(1 << m):
                    value = 1.0
                    for j in range(2, m + 2):
                        angle = math.pi * d / (1 << j)
                        value *= abs(math.sin(angle) if mask & (1 << (j - 2))
                                     else math.cos(angle))
                    predicted.append(value)
        nonzero_count = (p * p + 2) // 3
        assert len(predicted) == nonzero_count
        predicted += [0.0] * (p * p - nonzero_count)
        error = max(abs(x - y) for x, y in zip(sorted(direct), sorted(predicted)))
        assert error < 3e-13, (w, error)
        second = sum(x * x for x in direct) / (p * p)
        fourth = sum(x ** 4 for x in direct) / (p * p)
        assert abs(second - 1 / p) < 3e-13
        assert abs(fourth - (4 / 3) * (3 / 8) ** w) < 3e-13
        rows.append(dict(width=w, entries=p*p, nonzero=nonzero_count,
                         multiset_error=error, second=second, fourth=fourth))
    receipt = dict(status="passed", scope="finite widths 1 through 7; no tail claim",
                   entries=sum(r["entries"] for r in rows), checks=rows)
    Path(__file__).with_name("DISTRIBUTION-REVIEW-CHECK-RESULTS.json").write_text(
        json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k:v for k,v in receipt.items() if k != "checks"}))


if __name__ == "__main__":
    main()
