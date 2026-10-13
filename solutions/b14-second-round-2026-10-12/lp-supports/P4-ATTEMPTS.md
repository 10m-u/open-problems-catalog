# P4: five broader rounding routes and their limits

12 October 2026. The user selected the broader research ambitions, including
the general subtour-LP 4/3 target. The subdivision theorem completes a
restricted investigation, but does not reset the full-target failure count.
These are five specified sufficient routes tested in this round, awaiting
independent review. None is a counterexample to the 4/3 conjecture.

## A1: decompose the fractional support into cheap Hamiltonian cycles

Try to convert a feasible degree-two, cut-feasible support point directly
to a convex combination of support Hamiltonian cycles, then choose the
cheapest. Petersen's unit spokes and half pentagons are feasible and
extreme, as the exact certificates show, while its support contains no
Hamiltonian cycle. A convex combination is impossible. Costs beyond the
support, and additional traversal or shortcutting, cannot be avoided by
this route. The exhibited metric has gap 11/10, consistent with 4/3.

## A2: round each half cycle independently while keeping unit edges

Try to select a subset of each half cycle so that each vertex has one
chosen cycle edge, retaining its one unit spoke. The result would be a
degree-two cheap graph; further connectivity choices could seek a tour.
On each odd Petersen pentagon this first step is impossible: a spanning
one-regular subgraph of an odd cycle would be a perfect matching on an
odd number of vertices. The sum of requested degrees is odd, contradicting
the handshake identity. This failure is local parity, distinct from A1's
global Hamiltonicity obstruction. It does not reject coupled cycle
operations, doubled edges, random trees, or a 4/3 rounding theorem.

## A3: bound every minimum tree plus parity correction by 4LP/3

Try to strengthen the Christofides ceiling independently of minimum-tree
selection and Euler shortcutting. In the complete ten-city unit metric,
the Petersen fractional vertex still has cost LP=10. A star is a minimum
tree of cost 9; all ten vertices are odd, so every perfect matching costs
5. Its tree-plus-parity cost is 14>40/3. Thus the proposed strengthened
ceiling is false even on a half-integral LP vertex. Shortcutting yields
an optimal cost-10 tour here; the example refutes this proof ceiling,
not Christofides' returned-tour quality or a tie-aware tree choice.

## A4: extend the supplied-cheap-Hamiltonian-path closure lemma to all supports

The restricted lemma achieves (n+1)/n when a cheap Hamiltonian path is
available. Try to establish that prerequisite on every connected support
formed by unit matching edges and half odd cycles.

The Petersen necklace from the uniqueness obstruction defeats it for
every k>=3. A Hamiltonian path has endpoints in at most two gadgets.
Choose a gadget containing neither endpoint. The path crosses its cut a
positive even number of times, hence uses its only two external support
edges. Its restriction is a spanning path between the two ports; restoring
the removed spoke would make a Petersen Hamiltonian cycle. This is
impossible. The cut-feasible necklace support therefore has no cheap
Hamiltonian path. Expensive edges may still provide a low-cost rounded
tour. No lower bound exceeding 4/3 is obtained.

## A5: reduce the unrestricted target to half-integral vertices without a reduction

Try to close the general gap using only unit-plus-half-cycle extreme
supports and subdivision closure. Linear optimization permits restriction
to extreme points, but does not make them half-integral. The primary
[enumeration paper, Table 4](https://arxiv.org/html/2603.12995v5) reports
13 extreme-point classes at n=8, of which 12 are half-integral. Thus
the claim that every relevant extreme point already has half-integral
coordinates is false. The paper independently checks the general and
half-integral enumerations; this is cited source evidence, not a new local
enumeration certificate.

Two bounded local searches for an explicit non-half-integral witness
(600 metric-objective LPs at n=8,9 and 4000 random face/objective LPs at n=8)
found none. They do not challenge the source or imply absence. Their
purpose was a local illustration, and they are not extra solve failures.
No reduction mapping arbitrary extreme points to half-integral ones
while preserving gap has been proved here. Such a reduction could still
be possible; the failed route is simply omitting that indispensable step.

## Failure-count scope

These test different necessary steps: exact tour decomposition, independent
parity rounding, a tree-cost ceiling, existence of a support-spanning path,
and coverage of the fractional input class. A1/A2/A4 reuse Petersen
ingredients but assert different algebraic or connectivity premises.
The all-size subdivision lemma and finite gap/parity certificates remain
valid partial results. Stop P4 at five failures only after review; retain
the unrestricted 4/3 ambition as mathematically unresolved.

Evidence: [restricted theorem](RESULT.md), [exact gap receipt](CHECK-RESULTS.json),
[necklace proof](../generating-graph/RESULT.md), and
[broader-route checker](check_routes.py).

Final disposition: the [main-thread route review](../BROADER-ROUTE-REVIEW.md) accepts the five-failure count. This target is stopped for this run and remains mathematically unresolved.
