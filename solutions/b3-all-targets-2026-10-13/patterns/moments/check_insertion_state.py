#!/usr/bin/env python3
"""Literal maximum-insertion tests of the failed active-site state quotient."""
from collections import Counter
from itertools import permutations
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def insert_maximum(word):
    return [word[:i] + (len(word) + 1,) + word[i:] for i in range(len(word) + 1)]


def main():
    betas = parents = 0
    explicit = None
    for k in range(4, 7):
        for beta in permutations(range(1, k + 1)):
            sigma = tuple(x for x in beta if x != k)
            exceptional = tuple(x for x in beta if x < k - 1)
            seen = []
            for parent in permutations(range(1, k - 1)):
                children = insert_maximum(parent)
                assert len(children) == k - 1  # all have length below the forbidden pattern
                child_labels = Counter()
                for child in children:
                    allowed = [grandchild for grandchild in insert_maximum(child) if grandchild != beta]
                    active = len(allowed)
                    assert active == k - int(child == sigma)
                    child_labels[active] += 1
                expected = Counter({k - 1: 1, k: k - 2}) if parent == exceptional else Counter({k: k - 1})
                assert child_labels == expected
                seen.append(child_labels)
                parents += 1
                if beta == (1, 3, 2, 4) and parent == (1, 2):
                    explicit = {'beta': beta, 'first_parent': parent,
                        'first_children': children, 'first_labels': dict(child_labels),
                        'second_parent': (2, 1), 'second_children': insert_maximum((2, 1)),
                        'second_labels': {4: 3}}
            assert len(seen) >= 2 and any(s != seen[0] for s in seen)
            betas += 1
    receipt = {'status': 'PASS', 'k_range': [4, 6], 'forbidden_patterns': betas,
        'literal_parent_transition_controls': parents, 'actual_1324_witness': explicit,
        'scope': 'Non-lumpability of a prescribed active-site label; not a moment-property counterexample.',
        'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / 'INSERTION-STATE-CHECK.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
