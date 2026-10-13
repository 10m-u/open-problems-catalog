"""Complete fixed-seed extension check, not a bounded-coordinate search."""
import json
from math import isqrt
from pathlib import Path


def square(n):
    return n >= 0 and isqrt(n)**2 == n


def neighbors(values):
    v0, v1 = sorted(values)[:2]
    delta = v1 - v0
    found = set()
    for d in range(1, isqrt(delta) + 1):
        if delta % d:
            continue
        e = delta // d
        if (e - d) % 2:
            continue
        u = ((e - d) // 2)**2 - v0
        if all(square(u + v) for v in values):
            found.add(u)
    return sorted(found)


def main():
    a = [324, 54756, 119716, 264196]
    b = [0, 79200, 227205, 1258560]
    assert all(square(x + y) for x in a for y in b)
    na, nb = neighbors(b), neighbors(a)
    assert na == a and nb == b
    result = {
        "status": "passed", "seed_A": a, "seed_B": b,
        "all_possible_new_A": na, "all_possible_new_B": nb,
        "scope": "Complete unbounded one-element extensions of this fixed four-by-four seed",
    }
    Path(__file__).with_name("SQUARE-SUM-SEED-CHECK.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
