#!/usr/bin/env python3
"""Finite transition certificates for all positive word widths.

Words are read least significant bit first. Word length w encodes P=2**w;
there is no exponentiation inside the recognized relation. Internal carries
are discarded at the end, exactly as modular addition requires.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
BITS = list(product((0, 1), repeat=2))


def step_carry(s, xy):
    carry, differs, lower_and, previous_and, started, bad_low = s
    x, y = xy
    z = (x + y + carry) % 2
    return (
        (x + y + carry) // 2,
        differs or (z != (x ^ y)),
        lower_and or previous_and,
        x & y,
        True,
        bad_low or (not started and z != (x ^ y)),
    )


def step_toggle(s, xt):
    carry, differs, earlier_t, previous_t, started = s
    x, t = xt
    z = (x + t + carry) % 2
    return (
        (x + t + carry) // 2,
        differs or z != (x ^ t),
        earlier_t or previous_t,
        t,
        True,
    )


def graph(initial, step, violation):
    # Every finite word over the input alphabet has a reachable state.
    todo = deque([initial])
    seen = {initial}
    edges = []
    while todo:
        s = todo.popleft()
        for symbol in BITS:
            t = step(s, symbol)
            edges.append((s, symbol, t))
            if t not in seen:
                seen.add(t)
                todo.append(t)
    states = sorted(seen)
    numbers = {s: i for i, s in enumerate(states)}
    return {
        "states": states,
        "initial": numbers[initial],
        "edges": [(numbers[s], a, numbers[t]) for s, a, t in edges],
        "violations": [numbers[s] for s in states if violation(s)],
    }


def make():
    carry = graph((0, False, False, 0, False, False), step_carry,
                  lambda s: s[4] and (s[5] or bool(s[1]) != bool(s[2])))
    toggle = graph((0, False, False, 0, False), step_toggle,
                   lambda s: s[4] and s[3] == 1 and not s[2] and s[1])
    return {"carry_and_low_bit": carry, "top_toggle": toggle}


def verify(packet):
    specs = {
        "carry_and_low_bit": ((0, False, False, 0, False, False), step_carry,
                             lambda s: s[4] and (s[5] or bool(s[1]) != bool(s[2]))),
        "top_toggle": ((0, False, False, 0, False), step_toggle,
                       lambda s: s[4] and s[3] == 1 and not s[2] and s[1]),
    }
    for name, (initial, step, bad) in specs.items():
        g = packet[name]
        states = [tuple(s) for s in g["states"]]
        assert states[g["initial"]] == initial
        assert len(set(states)) == len(states)
        edges = {(i, tuple(a)): j for i, a, j in g["edges"]}
        assert len(edges) == len(states) * len(BITS)
        for i, s in enumerate(states):
            for a in BITS:
                assert states[edges[i, a]] == step(s, a)
        assert [i for i, s in enumerate(states) if bad(s)] == g["violations"] == []
        # Reject certificates with unreachable extra states.
        reached = {g["initial"]}
        while True:
            enlarged = reached | {edges[i, a] for i in reached for a in BITS}
            if enlarged == reached:
                break
            reached = enlarged
        assert reached == set(range(len(states)))


def semantic_controls():
    count = 0
    for w in range(1, 9):
        p = 1 << w
        top = p // 2
        for x in range(p):
            assert (x + top) % p == (x ^ top)
            for y in range(p):
                z = (x + y) % p
                assert (z & 1) == ((x ^ y) & 1)
                assert (z == (x ^ y)) == ((x & y) in (0, top))
                count += 1
    # Deliberately false variants must fail, including the width-one exception.
    assert ((1 + 1) % 2 == (1 ^ 1)) and (1 & 1) != 0
    assert ((1 + 1) % 4) != (1 ^ 1)
    return count


if __name__ == "__main__":
    packet = make()
    # JSON round trip verifies the actual emitted artifact.
    serialized = json.dumps(packet, indent=2)
    verify(json.loads(serialized))
    (HERE / "CERTIFICATES.json").write_text(serialized + "\n")
    result = {"all_width_certificates_verified": True,
              "states": {k: len(v["states"]) for k, v in packet.items()},
              "arithmetic_controls": semantic_controls(),
              "walnut_run": False,
              "scope": "three uniform arithmetic identities, every positive width"}
    (HERE / "VALIDATION.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
