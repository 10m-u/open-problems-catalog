# Independent review of P4's five broader routes

**Verdict:** the five specified sufficient routes in [P4-ATTEMPTS.md](../lp-supports/P4-ATTEMPTS.md) have distinct failed intermediate claims. I accept this count for the user's stopping rule, preserving the qualifications below. None disproves the unrestricted 4/3 conjecture.

| Route | Verified obstruction | Exact limit |
|---|---|---|
| A1 | The feasible extreme Petersen support has no Hamiltonian cycle, so no convex combination of support Hamiltonian cycles exists | Extra-support metric edges or repeated traversal remain available |
| A2 | Keeping each unit spoke requires degree one from its odd pentagon; the requested degree sum is odd | This blocks independent local cycle rounding, not coupled operations |
| A3 | In the ten-city uniform metric, a minimum star has cost 9 and an all-odd matching costs 5, exceeding 4LP/3=40/3 | The pre-shortcut ceiling for every minimum tree fails; the returned shortcut tour may be optimal |
| A4 | A k≥3 Petersen necklace has no support Hamiltonian path | Cheap-path closure cannot supply its own prerequisite on every such support |
| A5 | General extreme subtour vertices are not all half-integral | A gap-preserving reduction to half-integral vertices remains unproved, rather than refuted |

For A4, a Hamiltonian path has endpoints in at most two gadgets. A third gadget must have positive even path-cut degree. Its only two external support edges must therefore both be selected. All interior vertices have local degree two and its two ports local degree one. Restriction to the gadget is acyclic, since it lies in a global path, so it is exactly one spanning port-to-port path. Restoring the missing spoke would yield a Petersen Hamiltonian cycle, contradicting the previously verified fixed-gadget obstruction. The necklace cut-feasibility proof was independently reviewed in [UNIQUENESS-REVIEW.md](UNIQUENESS-REVIEW.md).

For A5, I directly checked the primary [Cook–Hougardy–Petrich paper, Table 4](https://arxiv.org/html/2603.12995v5): at n=8 it lists 13 general extreme-point classes and 12 half-integral classes. This is published enumeration evidence; no local non-half-integral witness is claimed. Absence from the two bounded illustration searches is not evidence of absence and contributes no extra failure. Mere existence of other vertices does not prove they attain the worst gap; that is why the packet correctly leaves a possible gap-preserving reduction open.

**Overlap:** A1, A2 and A4 use Petersen ingredients, but their claims are different: global convex tour decomposition, local degree/parity feasibility, and spanning-path existence. A3 is a different universal ceiling on tree-plus-parity cost. A5 addresses coverage of the LP input class. They are five failed sufficient methods, not five independent lower-bound constructions. In particular, restricting to half-integral vertices without a proved reduction is an unsuccessful coverage argument, not a hardness result.

The parent [checker](../lp-supports/check_routes.py) and [receipt](../lp-supports/ROUTE-CHECK-RESULTS.json) check the 32 odd-pentagon subsets, uniform-metric tree/parity costs, and three-gadget cut feasibility. The mathematical all-size A4 argument and source-only A5 assertion are correctly separated from those finite controls. The earlier [family review](P4-FAMILY-REVIEW.md) preserves the valid restricted subdivision theorem. Internal review only; no new proof search or external-review claim.
