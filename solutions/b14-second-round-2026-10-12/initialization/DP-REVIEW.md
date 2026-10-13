# Independent review of graphical covered/parity/partition DP

I read [DP-RESULT.md](../generating-graph/DP-RESULT.md), [euler_dp.py](../generating-graph/euler_dp.py), and [check_dp.py](../generating-graph/check_dp.py). The state equivalence, multiplicity restriction, forgetting rule and component-closing rule are sound for a connected generating graph on the entire city set, with nonnegative weights. No novelty or external peer-review claim follows from this review.

Expanding a metric tour yields a connected spanning Eulerian multigraph; shortcutting an Euler walk gives the reverse cost inequality. Reducing a multiplicity at least three by two leaves the edge in the support, preserves parity and connectivity, and does not increase nonnegative cost. Positive degrees then follow from connectivity and even parity. Thus considering multiplicities zero, one and two is complete.

Covered degree zero, positive odd degree and positive even degree are sufficient boundary degree states because this formulation has no upper-degree constraint. The component partition captures exactly which selected paths or subgraphs are already connected, without forcing a path-only Hamiltonian state. For every suffix, degrees depend only on the coverage/parity flags, and connectivity depends only on these flags and the partition. Costs of that suffix depend only on its assigned multiplicities. Retaining the least-cost prefix for each state is therefore a valid dominance rule.

A forgotten vertex has no future incident edge, so an uncovered or odd-degree vertex cannot be repaired. Likewise a selected component with no remaining boundary vertex cannot reconnect. Rejecting its early disappearance is correct. A completed component spanning *all* cities cannot disappear while an unprocessed edge remains, because that edge's endpoints would still be boundary vertices of the component. This addresses the apparent concern that rejecting early component closure might reject an optimum whose remaining edge multiplicities are all zero. On the last processed edge, exactly one closing component is required; the existing forgetting tests ensure every vertex is covered and even.

I checked the compressed parity update in the implementation: adding one exchanges odd/even states, adding two preserves positive parity, and either addition changes uncovered to covered. The component labels are merged and then canonically renamed. An endpoint outside the current frontier is genuinely new: a previously forgotten endpoint cannot occur again, since forgetting is tied to its last occurrence in the fixed processing order. The winning full multiplicity prefix is enough for reconstruction, with the copying overhead already acknowledged in the main note.

[check_dp_equivalence.py](check_dp_equivalence.py) gives a separate literal suffix-feasibility audit, using graph-component searches rather than the DP transition code. It passed:

- Seven small graph families in 21 forward, reverse and shuffled processing orders.
- 1,454 accepted prefixes, including 903 collisions of distinct prefixes with the same state. Every such pair has exactly the same feasible suffix assignments.
- 30,672 literal complete-multigraph suffix-feasibility tests.
- 63 four-way optimum comparisons: exhaustive multiplicity enumeration, exhaustive metric-tour enumeration, the main compressed DP, and the main full-degree DP. These include all-zero, all-unit-tied and unequal positive weights.

The receipt is [DP-EQUIVALENCE-CHECK-RESULTS.json](DP-EQUIVALENCE-CHECK-RESULTS.json). Run `python3 solutions/b14-second-round-2026-10-12/initialization/check_dp_equivalence.py`.

The Bell-number state bound is a frontier-width baseline, rather than a treewidth bound for the complete metric. The input assumption that all generating vertices are cities is essential to the coverage tests; Steiner vertices need a modified formulation. General sparse graphs can have large frontiers, so these checks and the state theorem establish no polynomial algorithm for arbitrary TSP.
