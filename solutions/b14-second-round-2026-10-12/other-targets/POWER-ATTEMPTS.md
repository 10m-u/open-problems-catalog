# Q1852 and Q1853 — Separate Hamiltonicity attempts

These are five distinct sufficient proof routes for each **separate** problem. None resolves the catalog conjecture. The counterexamples below are themselves Hamiltonian, with explicit tour witnesses, and refute only the proposed intermediate lemmas or algorithms. Attempts are counted per target, without combining the two streaks. No theorem of non-Hamiltonicity or novelty claim is made.

## Q1852: spanning subgraphs of path powers

The exact hypothesis is H⊆P_n^k and deg_H(v)≥deg_host(v)/2+2.

**A1 — Transfer the source's asymmetric degree theorem in either order.** Theorem 5 for cycles requires degree at least min(i+1,k+2,k+n-i) in one-based order. On P_20^6 delete edges {0,6} and {13,19}, with zero-based vertices. Both endpoints retain degree five, meeting the target's threshold five. All other vertices meet their thresholds too. Theorem 5 requires degree six at the last endpoint, so fails in both natural orientations. The effective-degree Theorem 2 also fails at those endpoints. A symmetric boundary improvement, explicitly proposed by the authors, is still needed. Outcome: unsuccessful, streak 1.

**A2 — Use a global degree-sequence closure certificate.** On the full P_25^4 the hypothesis holds, but every degree is at most eight. Every nonadjacent pair has degree sum at most sixteen, below twenty-five. Bondy–Chvátal closure adds no edge; Dirac's criterion fails as well. More generally take n>4k and k≥4. The global closure route cannot derive completeness from the local hypothesis. This rejects that sufficient closure certificate, not Hamiltonicity. Outcome: unsuccessful, streak 2.

**A3 — Force high connectivity across the ordered boundary.** Try to derive k-connectivity (or 2-toughness) from the degree condition, then use that robust boundary supply in a construction. Let H be the union of P_7^4 on vertices 0,...,6 and P_7^4 on 5,...,11. The graph satisfies the hypothesis in P_12^4. Removing {5,6} leaves two components of size five. It is not four-connected and its toughness is at most one. Thus a proof requiring those stronger separator properties cannot follow from the target degrees. The example is the source's overlapping-path construction at ℓ=3, in a target-valid parameter range. Outcome: unsuccessful, streak 3.

**A4 — Solve a degree-and-cut LP and rely on promised integrality.** The promise does not make the full subtour polytope integral. Already H=P_10^9=K_10 satisfies it. On a Petersen-labeled support, set each spoke to one and every edge of the outer and inner five-cycles to one half, all other edges zero. All degrees are two and every proper cut has weight at least two. This is a fractional vertex: five tight spoke upper bounds leave two odd-cycle degree systems, which uniquely force their ten half-values. Zero bounds fix the remaining variables. Consequently this LP cannot promise to return a Hamilton cycle for every objective merely from the degree hypothesis. Integrality, rather than LP feasibility, was the attempted shortcut. Outcome: unsuccessful, streak 4.

**A5 — Delete an endpoint and induct with the same degree hypothesis.** On P_12^4 remove edges {4,7},{4,8},{3,7}. The resulting H satisfies every target threshold. Vertex 4 has degree six; after deleting endpoint 0 it has degree five while its new host degree is seven, requiring six. Vertex 7 gives the mirrored failure after deleting endpoint 11. Thus neither natural endpoint deletion preserves the induction class. Repairs need a boundary buffer or a different invariant. Outcome: unsuccessful, streak 5.

These five routes have not solved Q1852. Subject to independent review, this problem reaches the user's per-problem stop condition; its catalog status remains unresolved.

## Q1853: spanning subgraphs of cycle powers

The exact hypothesis is H⊆C_n^k and δ(H)≥k+1.

**A1 — Cut the cyclic order and apply the known path theorem, allowing a better bandwidth parameter.** Let H be C_20^2 plus edges {0,3},{10,13}, inside C_20^3. Every degree is four or five, meeting k+1. After any cyclic cut, retain only edges of the resulting P_20^3. A degree-five vertex survives, forcing bandwidth at least three under any relabeling. At least sixteen vertices have degree at most four. At any bandwidth parameter k'≥3, Theorem 5 permits degree≤4 in at most five positions: the first three and, only when k'=3, the last two. For k'≥6 it also requires an endpoint degree at least six, exceeding the graph's maximum. The effective-degree Theorem 2 is no weaker for this purpose. Thus optimizing the bandwidth or reversing/relabeling the path does not make this direct transfer work. Adding only C_20^2 would be inadequate as an obstruction: cutting it yields P_20^2, where k'=2 is applicable. The source's proposed stronger symmetric path statement would give the cycle threshold k+2, still one above this target. Outcome: unsuccessful, streak 1.

**A2 — Global Dirac/closure.** The full C_25^4 satisfies the target but has degree eight. Nonadjacent degree sums are sixteen, below twenty-five, so the usual closure makes no progress. Taking n>4k gives an all-size obstruction to this sufficient certificate. Outcome: unsuccessful, streak 2.

**A3 — Derive k-connectivity from the extra one neighbor.** On C_9^3 take P_5^3 on 0,...,4, P_5^3 on 4,...,8, and add edge {0,8}. Every degree is at least four, but deleting {0,4} leaves components {1,2,3} and {5,6,7,8}. It is not three-connected. The natural cycle 0,1,...,8,0 is present, so the stronger connectivity lemma is unnecessary for Hamiltonicity and false under the hypothesis. Outcome: unsuccessful, streak 3.

**A4 — Promised subtour-LP integrality.** H=C_10^5=K_10 satisfies δ≥6. The same unit-spoke/half-cycle Petersen point is a fractional feasible vertex. Thus this promise too cannot justify an LP-only Hamilton-cycle construction through integrality of the relaxation. Outcome: unsuccessful, streak 4.

**A5 — Orient every short edge forward and construct a directed Hamilton cycle.** For odd n≥7, let H=C_n^2 minus disjoint edges {0,1},{2,4}. It has minimum degree three, the target for k=2. In the natural forward orientation every arc advances one or two positions. A directed Hamilton cycle would have n advances and total n+t for 0≤t≤n, divisible by n; hence all steps are one or all are two. The deleted edges block both possibilities. Yet the undirected tour 0,2,1,3,4,...,n-1,0 exists. Restricting construction to forward cycles loses valid solutions. Outcome: unsuccessful, streak 5.

These five routes have not solved Q1853. Subject to independent review, its per-problem stop condition is reached; this does not stop the other B14 targets.

## Exact controls and scope

[check_power_routes.py](check_power_routes.py) verifies host containment, every degree inequality, theorem-transfer failures, separators, the lack of closure additions, endpoint induction failures and all claimed tour witnesses. It checks all 1,022 proper Petersen cuts and the fractional vertex's defining equations. The forward-cycle obstruction is checked on n=7,9,11,13; the advance-sum proof covers every odd n≥7. [Receipt](POWER-ROUTE-CHECK-RESULTS.json).

The source is Espuny Díaz et al., *Dirac's Theorem for Graphs of Bounded Bandwidth*, Theorems 2 and 5, Example 4 and §1.2. [Primary paper](https://doi.org/10.37236/13474), retained local text ../../../texts/papers/collections-295e0a79f41bcbaa.txt.gz. Original targets are unchanged. The route failures are local research outcomes, not literature resolutions of the conjectures.
