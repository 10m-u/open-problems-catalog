"""Complete 200-box using exact valuation Gram determinants."""
import json
from itertools import combinations
from pathlib import Path
from sympy import factorint


def main():
    bound = 200
    factors = {n: factorint(n) for n in range(2, bound + 3)}
    dot = {(a, b): sum(e * factors[b].get(p, 0) for p, e in factors[a].items())
           for a in factors for b in factors}
    def minimal(a, b, c):
        aa, bb, cc = dot[a,a], dot[b,b], dot[c,c]
        ab, ac, bc = dot[a,b], dot[a,c], dot[b,c]
        if aa*bb <= ab*ab or aa*cc <= ac*ac or bb*cc <= bc*bc:
            return False
        return aa*bb*cc + 2*ab*ac*bc - aa*bc*bc - bb*ac*ac - cc*ab*ab == 0
    two, three, count = [], [], 0
    for a,b,c in combinations(range(2,bound+1), 3):
        count += 1
        if minimal(a,b,c) and minimal(a+1,b+1,c+1):
            two.append([a,b,c])
            if minimal(a+2,b+2,c+2):
                three.append([a,b,c])
    expected = [[7,23,161],[9,49,63],[10,32,80],[12,24,64],[16,50,80]]
    assert two == expected and three == []
    assert count == 1293699
    out = {"status":"passed","max_original_coordinate":bound,"triples_checked":count,
           "two_minimal_shift_count":len(two),"two_minimal_shift_examples":two,
           "three_minimal_shift_witnesses":three,
           "scope":"Complete box, not infinite families or unbounded nonexistence"}
    Path(__file__).with_name("SHIFT-BOX-CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
