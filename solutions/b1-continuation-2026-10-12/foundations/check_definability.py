#!/usr/bin/env python3
"""Exact finite controls for new definability and prefix obstructions."""
from collections import deque
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def in_k(x):
    if x == 0: return True
    digits = bin(x)[2:]
    if len(digits) % 2: digits = "0" + digits
    return all(digits[i:i+2] in ("01", "10") for i in range(0,len(digits),2))


def existential_complement_witness(x):
    h = 1
    while h <= x:
        assert h & (h-1) == 0 and h % 3 == 1
        r = x % h
        d = (x // h) % 4
        u = x - d*h - r
        if d in (0,3) and (u == 0 or (u & -u) >= 4*h):
            assert x == u+d*h+r and 0 <= r < h
            return {"h":h, "digit":d, "u":u, "r":r}
        h *= 4
    return None


def k_dfa():
    nfa = {(0,0):{1}, (0,1):{2,3}, (2,0):{3}, (3,0):{4},
           (3,1):{5}, (4,1):{3}, (5,0):{3}}
    states = [frozenset({0})]
    ids = {states[0]:0}
    edges = []
    for state in states:
        row = []
        for letter in (0,1):
            nxt = frozenset(q for p in state for q in nfa.get((p,letter),set()))
            if nxt not in ids:
                ids[nxt] = len(states)
                states.append(nxt)
            row.append(ids[nxt])
        edges.append(row)
    accepting = {i for i,s in enumerate(states) if s & {1,3}}
    return edges, accepting


def monoid_control():
    edges, accepting = k_dfa()
    identity = tuple(range(len(edges)))
    representatives = {identity:""}
    todo = deque([identity])
    while todo:
        mapping = todo.popleft()
        for letter in (0,1):
            new = tuple(edges[s][letter] for s in mapping)
            if new not in representatives:
                representatives[new] = representatives[mapping] + str(letter)
                todo.append(new)
    finite = {word for mapping,word in representatives.items() if mapping[0] in accepting}
    assert all(word and in_k(int(word,2)) for word in finite)
    omitted = "10" * (1 + max(map(len,finite)))
    state = 0
    for digit in omitted: state = edges[state][int(digit)]
    assert state in accepting and omitted not in finite
    for x in range(1 << 16):
        s = 0
        for digit in bin(x)[2:]: s = edges[s][int(digit)]
        assert (s in accepting) == in_k(x)
    return {"DFA_states":len(edges), "monoid_elements":len(representatives),
            "finite_representatives":sorted(finite),
            "accepted_word_missing_from_finite_representatives":omitted,
            "same_accepting_monoid_image":True}


def main():
    for x in range(1 << 16):
        assert (existential_complement_witness(x) is not None) == (not in_k(x))
    q = 17
    def masked(x): return x % q != 1 or in_k((x-1)//q)
    affines = 0
    for a in range(1,17):
        for b in range(17):
            exceptional = [n for n in range(q) if (a*n+b) % q == 1]
            assert len(exceptional) == 1
            assert all(masked(a*n+b) for n in range(1024)
                       if n % q != exceptional[0])
            affines += 1
    assert all(masked(q*n+1) == in_k(n) for n in range(1 << 16))
    matrix = lambda y,z: y//2 == z%2
    assert not any(all(matrix(y,z) for z in range(4)) for y in range(4))
    assert all(matrix(2*(z%2),z) for z in range(4))
    result = {"complement_formula_controls":1 << 16, "masked_slice_controls":1 << 16,
              "affine_coefficient_cutoff":16, "mask_prime":q,
              "affine_periodic_density_controls":affines,
              "whole_integer_quantifiers_false_online_bit_game_true":True,
              "monoid_image_control":monoid_control(),
              "scope":"Finite exact obstructions; no unbounded definability decision."}
    (HERE/"ROOT-DEFINABILITY-CHECK.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="monoid_image_control"}))


if __name__ == "__main__": main()
