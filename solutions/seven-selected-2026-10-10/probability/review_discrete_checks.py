#!/usr/bin/env python3
"""Independent row-word enumeration for the Q3840/Q3841 review.

Does not import the discrete author's verifier or its transition graph.
In particular the 5-by-5 torus is checked by extending explicit membership
words and directly testing the two boundary rows and three boundary edges.
"""
from itertools import product
import json


rows = [tuple(map(int, f'{a:05b}')) for a in range(32)]
within = [tuple(row[(i - 1) % 5] + row[(i + 1) % 5] for i in range(5))
          for row in rows]


def colors(a, b, c):
    return tuple(rows[a][i] + within[b][i] + rows[c][i] for i in range(5))


def proper(vector):
    return all(vector[i] > 0 and vector[i] != vector[(i + 1) % 5]
               for i in range(5))


def separated(first, second):
    return all(a != b for a, b in zip(first, second))


def main():
    all_colors = {word: colors(*word) for word in product(range(32), repeat=3)}
    valid = {word: vector for word, vector in all_colors.items() if proper(vector)}
    extensions = {}
    for (a, b, c), vector in valid.items():
        extensions.setdefault((a, b), []).append((c, vector))

    # Finalized row colors for a word (a,b,c) contain only the color of b.
    words = [(word, [vector]) for word, vector in valid.items()]
    word_counts = [len(words)]
    for _ in [4, 5]:
        longer = []
        for word, finalized in words:
            for next_row, vector in extensions.get(word[-2:], []):
                if separated(finalized[-1], vector):
                    longer.append((word + (next_row,), finalized + [vector]))
        words = longer
        word_counts.append(len(words))

    torus_witnesses = 0
    for word, finalized in words:
        first = all_colors[word[-1], word[0], word[1]]
        last = all_colors[word[-2], word[-1], word[0]]
        if (proper(first) and proper(last)
                and separated(first, finalized[0])
                and separated(last, finalized[-1])
                and separated(last, first)):
            torus_witnesses += 1
    assert word_counts == [4310, 10800, 25170]
    assert torus_witnesses == 0

    active = {word: vector for word, vector in valid.items() if word[0] == 0}
    cylinder_counts = []
    for length in range(1, 9):
        cylinder_counts.append({
            "length": length,
            "frontier_size": len(active),
            "accepting_frontiers": sum(word[-1] == 0 for word in active),
        })
        active = {(b, c, d): vector for (a, b, c), previous in active.items()
                  for d, vector in extensions.get((b, c), [])
                  if separated(previous, vector)}
    assert [row['accepting_frontiers'] for row in cylinder_counts] == [0, 0, 10, 0, 20, 0, 50, 0]
    print(json.dumps({
        "arithmetic": "exact integers, standard library only",
        "independence": "No imports from discrete/verify.py; explicit row words for the torus",
        "torus_word_counts_at_lengths_3_4_5": word_counts,
        "closed_torus_5_by_5_membership_words": torus_witnesses,
        "cylinder_counts": cylinder_counts,
        "all_passed": True,
    }, indent=2))


if __name__ == '__main__':
    main()
