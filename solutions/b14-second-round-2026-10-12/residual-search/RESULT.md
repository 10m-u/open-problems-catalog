# P2 — Forget saturated vertices' component labels

**Result:** a proved exact frontier-state reduction for Hamilton-cycle search, integrated with sixteen certified P1 residual graphs. This is an implementation of established boundary-state reasoning, not an originality claim or a scalable-solver benchmark. The explicit first deliverable is met; broader performance ambitions remain separate.

Process the residual graph's edges in a fixed order. A prefix chooses some processed edges, with degree at most two. Forget a vertex only after its final incident edge has been processed, and only at degree two. Forbid a closed selected cycle unless it already spans every city. Every other selected component is a path with two degree-one endpoints. Both endpoints must remain in the boundary: a degree-one vertex cannot be forgotten.

The baseline key records each boundary vertex's degree 0,1,2 and the component partition of all covered boundary vertices. The reduced key retains the same degrees, but keeps only the pairing of **degree-one endpoints**. A degree-two boundary vertex is saturated; no feasible suffix can select another incident edge. Which existing path contains that vertex therefore cannot affect any future attachment.

**State-equivalence theorem.** If two valid prefixes have the same boundary degrees and endpoint pairing, every suffix is feasible for both or neither. When feasible, adding that suffix adds the same cost to both. Keeping the cheaper prefix preserves the minimum tour cost.

To prove this, suppress each prefix path to an abstract edge between its two endpoints. Every future selected edge touches only degree-zero or degree-one boundary vertices, or newly introduced vertices. Each suppressed path behaves identically under those attachments. Degree-zero boundary vertices are isolated in both prefixes; degree-two vertices permit no attachment. Forgotten vertices already have their final required degree. The pairing and future edges determine whether the result is one spanning cycle or several components. Prefix costs differ by a fixed additive constant independent of the suffix, so selecting the minimum is safe. A fully completed tour has a distinct terminal state permitting only omitted suffix edges.

For b boundary vertices, the reduced state count is at most

$$
\sum_{\substack{0\le s\le b\\s\text{ even}}}
\binom bs\,2^{b-s}(s-1)!!,
$$

where (-1)!!=1. Choose the s degree-one vertices and their pairing; all other degrees are zero or two. Reachability and remaining incidence usually remove additional states. Copying full prefix witnesses in this prototype adds a factor depending on the processed edge count to its runtime/storage; no implementation-level linear runtime is claimed.

The implementation also rejects any state where a vertex's current degree plus its number of remaining incident edges is below two. If equality holds, its remaining incident edges are thereby forced. This uses the certified residual graph, not an unsupported score. An optional feasible incumbent prunes prefixes already more costly than it, using nonnegative edge costs.

## Verification and measured limits

[hamilton_dp.py](hamilton_dp.py) supports full-history controls, degree-and-full-partition compression, and the endpoint-pairing reduction. [check.py](check.py) compares all three with independent subset DP on eight six-city graphs with zero, tied and positive integer costs. Each returns the exact same optimum. Two disjoint triangles are rejected.

Sixteen n=8 residuals from round 1's four-root elimination packets were independently rechecked against original costs before use. All frontier and subset-DP optima agree. The endpoint rule reduces total retained states from **14,808 to 13,932** on these residuals. On the six-city controls, histories compress from 858 to 721 states; dropping saturated labels does not reduce them further.

The frontier method still performs more transitions than subset DP on this bounded residual set. Across the four Euclidean residuals, for example, it takes 101 transitions versus 88 for subset DP; full partition totals on the tree-metric controls are 19,268 versus 5,376. The rule is safe and saves states in the measured cases, but the available data do not establish faster search. [Exact receipt](CHECK-RESULTS.json).

This addresses P2's state-equivalence deliverable in the actual P1 residual setting. The separate [graphical-TSP parity DP](../generating-graph/DP-RESULT.md) addresses walks on the sparse generating graph; its even-degree states cannot simply replace the degree-two constraints in this Hamiltonian residual formulation.
