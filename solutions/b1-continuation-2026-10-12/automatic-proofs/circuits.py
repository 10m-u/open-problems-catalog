#!/usr/bin/env python3
"""Compile fixed acyclic word circuits and decide all-positive-width equality.

Gates: add (modular), xor, and, or, not, zero, input. Internal carry
bits are the only persistent gate state; NOT complements within the width.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def compile_spec(spec):
    inputs = spec["inputs"]
    gates = spec["gates"]
    seen = set(inputs)
    assert len(seen) == len(inputs), "Input names must be distinct"
    carry_gates = []
    arities = {"add": 2, "xor": 2, "and": 2, "or": 2, "not": 1, "zero": 0}
    for name, op, *args in gates:
        assert name not in seen and op in arities
        assert len(args) == arities[op] and all(a in seen for a in args)
        seen.add(name)
        if op == "add":
            carry_gates.append(name)
    assert all(name in seen for name in spec["outputs"])
    assert len(spec["outputs"]) == 2
    alphabet = list(product((0, 1), repeat=len(inputs)))
    initial = tuple([0] * len(carry_gates) + [False, False])

    def step(state, symbol):
        env = dict(zip(inputs, symbol))
        old = dict(zip(carry_gates, state[:-2]))
        new = []
        for name, op, *args in gates:
            v = [env[a] for a in args]
            if op == "add":
                total = sum(v) + old[name]
                env[name] = total % 2
                new.append(total // 2)
            elif op == "xor":
                env[name] = v[0] ^ v[1]
            elif op == "and":
                env[name] = v[0] & v[1]
            elif op == "or":
                env[name] = v[0] | v[1]
            elif op == "not":
                env[name] = 1 - v[0]
            else:
                env[name] = 0
        left, right = spec["outputs"]
        return tuple(new + [bool(state[-2] or env[left] != env[right]), True])

    return alphabet, initial, step


def certificate(spec):
    alphabet, initial, step = compile_spec(spec)
    states = [initial]
    numbers = {initial: 0}
    todo = deque([initial])
    edges = []
    words = {initial: []}
    while todo:
        s = todo.popleft()
        for symbol in alphabet:
            t = step(s, symbol)
            if t not in numbers:
                numbers[t] = len(states)
                states.append(t)
                words[t] = words[s] + [symbol]
                todo.append(t)
            edges.append((numbers[s], symbol, numbers[t]))
    bad = [i for i, s in enumerate(states) if s[-1] and s[-2]]
    witness = words[states[bad[0]]] if bad else None
    return {"spec": spec, "states": states, "initial": 0, "edges": edges,
            "bad_terminal_states": bad, "counterexample_lsd_bits": witness,
            "all_positive_widths_equal": not bad}


def verify(packet):
    alphabet, initial, step = compile_spec(packet["spec"])
    states = list(map(tuple, packet["states"]))
    assert states[packet["initial"]] == initial
    assert len(states) == len(set(states))
    edges = {(i, tuple(a)): j for i, a, j in packet["edges"]}
    assert len(edges) == len(states) * len(alphabet)
    for i, s in enumerate(states):
        for a in alphabet:
            assert states[edges[i, a]] == step(s, a)
    reached = {packet["initial"]}
    while True:
        nxt = reached | {edges[i, a] for i in reached for a in alphabet}
        if nxt == reached:
            break
        reached = nxt
    assert reached == set(range(len(states)))
    bad = [i for i, s in enumerate(states) if s[-1] and s[-2]]
    assert bad == packet["bad_terminal_states"]
    assert packet["all_positive_widths_equal"] == (not bad)
    word = packet["counterexample_lsd_bits"]
    if bad:
        s = initial
        for symbol in word:
            s = step(s, symbol)
        assert s[-1] and s[-2]
        p = 1 << len(word)
        env = {name: sum(a[j] << i for i, a in enumerate(word))
               for j, name in enumerate(packet["spec"]["inputs"])}
        for name, op, *args in packet["spec"]["gates"]:
            v = [env[a] for a in args]
            if op == "add": env[name] = sum(v) % p
            elif op == "xor": env[name] = v[0] ^ v[1]
            elif op == "and": env[name] = v[0] & v[1]
            elif op == "or": env[name] = v[0] | v[1]
            elif op == "not": env[name] = (p - 1) ^ v[0]
            else: env[name] = 0
        a, b = packet["spec"]["outputs"]
        assert env[a] != env[b]


def examples():
    return [
        {"name": "modular_addition_associative", "inputs": ["x", "y", "z"],
         "gates": [["a", "add", "x", "y"], ["b", "add", "a", "z"],
                   ["c", "add", "y", "z"], ["d", "add", "x", "c"]],
         "outputs": ["b", "d"]},
        {"name": "modular_addition_commutative", "inputs": ["x", "y"],
         "gates": [["a", "add", "x", "y"], ["b", "add", "y", "x"]],
         "outputs": ["a", "b"]},
        {"name": "and_distributes_over_xor", "inputs": ["x", "y", "z"],
         "gates": [["a", "xor", "y", "z"], ["b", "and", "x", "a"],
                   ["c", "and", "x", "y"], ["d", "and", "x", "z"],
                   ["e", "xor", "c", "d"]], "outputs": ["b", "e"]},
        {"name": "de_morgan", "inputs": ["x", "y"],
         "gates": [["a", "and", "x", "y"], ["b", "not", "a"],
                   ["c", "not", "x"], ["d", "not", "y"],
                   ["e", "or", "c", "d"]], "outputs": ["b", "e"]},
        {"name": "false_addition_is_xor", "inputs": ["x", "y"],
         "gates": [["a", "add", "x", "y"], ["b", "xor", "x", "y"]],
         "outputs": ["a", "b"]},
    ]


if __name__ == "__main__":
    packets = json.loads(json.dumps([certificate(s) for s in examples()]))
    for packet in packets:
        verify(packet)
    assert all(p["all_positive_widths_equal"] for p in packets[:-1])
    assert not packets[-1]["all_positive_widths_equal"]
    (HERE / "CIRCUIT-CERTIFICATES.json").write_text(json.dumps(packets, indent=2) + "\n")
    print(json.dumps([{"name": p["spec"]["name"], "states": len(p["states"]),
                       "equal": p["all_positive_widths_equal"],
                       "counterexample": p["counterexample_lsd_bits"]} for p in packets]))
