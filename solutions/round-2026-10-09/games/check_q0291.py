#!/usr/bin/env python3
"""Exact outcome enumeration for Q291 payoff identities and boundary cases."""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json


def share(actions, player):
    present = set(actions)
    if len(present) == 1:
        winner = actions[0]
    elif "R" in present and "S" in present:
        winner = "R"
    elif "P" in present and "R" in present:
        winner = "P"
    else:
        assert present == {"P", "S"}
        winner = "S"
    return F(1, actions.count(winner)) if actions[player] == winner else F(0)


def payoff(distributions, player, action):
    options = [((action, F(1)),) if j == player
               else tuple((a, p) for a, p in dist.items() if p)
               for j, dist in enumerate(distributions)]
    return sum((prod(p for _, p in outcome) *
                share(tuple(a for a, _ in outcome), player)
                for outcome in product(*options)), F(0))


def expected_reciprocal(qs, offset):
    return sum((prod((q if b else 1-q for q, b in zip(qs, bits)), start=F(1)) /
                (offset + sum(bits))
                for bits in product((0, 1), repeat=len(qs))), F(0))


def main():
    counts = {"opponent_profiles": 0, "unique_scissors_profiles": 0,
              "special_best_response_profiles": 0,
              "ordinary_deviation_comparisons": 0}
    grid = (F(0), F(1, 3), F(2, 3), F(1))
    for m in range(2, 6):
        for qs in product(grid, repeat=m-1):
            counts["opponent_profiles"] += 1
            ordinary = [{"R": 1-q, "P": q, "S": F(0)} for q in qs]
            base = [{"R": F(0), "P": F(1), "S": F(0)}] + ordinary
            a = expected_reciprocal(qs, 1)
            q_all = prod(qs)
            assert payoff(base, 0, "P") == a
            assert payoff(base, 0, "S") == q_all
            assert payoff(base, 0, "P") > payoff(base, 0, "R")
            assert a >= F(1, m)
            for s in (F(1, 3), F(2, 3), F(1)):
                counts["unique_scissors_profiles"] += 1
                distributions = [{"R": F(0), "P": 1-s, "S": s}] + ordinary
                eligible = q_all >= a
                counts["special_best_response_profiles"] += eligible
                if eligible:
                    assert all(q > 0 for q in qs)
                for i, qi in enumerate(qs):
                    other = qs[:i] + qs[i+1:]
                    b = expected_reciprocal(other, 2)
                    d = expected_reciprocal(other, 1)
                    q_without = prod(other)
                    assert a == (1-qi) * d + qi * b
                    assert b <= a
                    p_share = payoff(distributions, i+1, "P")
                    s_share = payoff(distributions, i+1, "S")
                    assert p_share == (1-s) * b
                    assert s_share == (1-s/F(2)) * q_without
                    counts["ordinary_deviation_comparisons"] += 1
                    if eligible:
                        assert s_share > p_share
                        assert s_share-p_share >= s*q_without/F(2)
                        assert m*(s_share-p_share) >= s/F(2)
    result = {"problem": "Q291", "arithmetic": "exact rational",
              "players": "2..5", "ordinary_paper_probabilities":
              [str(x) for x in grid], "special_scissors_probabilities":
              ["1/3", "2/3", "1"], "checks": counts,
              "result": "all assertions passed",
              "scope": "finite independent payoff controls; all-m proof in Q0291.md"}
    Path(__file__).with_name("q0291-checks.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
