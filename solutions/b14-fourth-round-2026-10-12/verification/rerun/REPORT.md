# B14 research continuation: completion certificates, exact contraction, and blockwise descent

**Date:** 2026-10-12. **Scope:** new work on P1-P2 and P3, not another replication of the Q3818/P5 count result.

**Review state:** full proofs and exact computational certificates are provided. They have been checked within this continuation but have not been externally peer-reviewed or formally verified. Newness relative to the supplied handoff is documented; priority across the wider literature is not established.

## Executive findings

The practical thread now has a positive result on the handoff's negative example. A module-completion certificate overcomes a family on which every forced rooted 1-tree bound, at every root and every real vertex potential vector, fails to delete any edge. An exact characterization of minimum-cost repairs reduces the global search to two connector patterns and a subset search over paired path units. With endpoint-separable repair costs, even that subset search disappears.

The probabilistic/local-search thread now has a deterministic result. In a shortest-path metric, a 2-opt move cannot improve one biconnected block by making another worse. Combining this noncancellation property with small-integer metrics preserving all local gain signs gives a quadratic move bound when block size is fixed, without any assumption about random weights or a minimum improvement size.

Full arguments: [completion, exact contraction and separation](proofs/COMPLETION-CERTIFICATES.md); [blockwise descent](proofs/BLOCKWISE-DESCENT.md).

## 1. P1-P2: from a complete residual to an exact tour

### 1.1 The all-size separating family

For every even k >= 18, use k ten-vertex Petersen-minus-spoke modules in a necklace, with n = 10k cities. A cheap connector joins the right port of each module to the left port of the next. Each module has a Hamiltonian path from either port but none between its two ports.

For a tour, every module must be incident to a noncheap repair edge. Counting incidences gives at least k/2 repairs. The new structural result is that this lower bound is attained, and equality forces exactly one repair incidence and exactly one cheap connector at each module. The connector set must be one of the two alternating perfect matchings. The module paths pair into k/2 disjoint path units, which must then form one cycle.

This minimum-repair characterization is stronger than the handoff's obstruction, which only required a lower bound to show failure of the relaxation. It supplies a complete description of the face on which exact solving is required.

Choose any such minimum-repair tour T. Let B = n+1, and give each edge the cost

\[
c_e=B\bigl(2+\mathbf1_{e\text{ is a repair}}\bigr)+\mathbf1_{e\notin T}.
\]

The resulting metric is strict and has only four O(n)-sized values: 2n+2, 2n+3, 3n+3, and 3n+4. Tour T is unique, of cost B(2n+k/2).

The handoff's fractional subtour point can be relabeled to force every edge. Its cost is at most B(2n+8)+n, strictly below the tour optimum for k >= 18. Fractional spanning-tree domination proves that every forced rooted 1-tree lower bound, for every root and all real vertex potentials, is below the optimum. This is a quantified proof, not a finite potential-tuning test.

The new completion bounds instead force a non-T edge to pay at least one secondary unit, or to leave the minimum-repair face. They delete every edge outside T.

### 1.2 Exact 180-city separation

| Quantity | Checked value |
|---|---:|
| Cities | 180 |
| Cost values | 362, 363, 543, 544 |
| Unique optimum | 66,789 |
| Complete-graph edges | 16,110 |
| Edges deletable by any forced rooted 1-tree bound | 0 |
| Edges deleted by completion bounds | 15,930 |
| Remaining edges | 180, exactly the optimal cycle |

Thus the residual treewidth drops from 179 to 2 on this family. This example is deliberately constructed for a separation theorem; it is not a blinded general-purpose solver benchmark.

Retained evidence includes the original instance and tour, all 16,110 forced fractional witness objective checks, and 179 integer flow certificates with 29,358 nonzero signed flow entries. The flows establish every subtour inequality of the fractional point. The largest doubled witness cost is 133,017, below the doubled optimum 133,578.

### 1.3 Weighted solving without planting the answer

More generally, give cheap edges primary cost 2B and repair edges primary cost 3B, with secondary costs s_e in [0,W] and B > nW. This makes the minimum-repair face contain every optimum.

If intermodule repair costs satisfy s_uv = t_u+t_v, local Hamiltonian-path tables determine a number S_j for each connector pattern j. The exact optimum is

\[
OPT=B(2n+k/2)+\min(S_0,S_1).
\]

The theorem includes arbitrary internal secondary costs. An optimal tour is constructed from the minimizing paths; no optimal tour is part of the input. Random weighted instances at 20, 40, 180, 400 and 1,000 cities were exactly solved in this family. At 1,000 cities, the optimum is 41,010,220.

The lower-bound method also permits s_uv >= t_u+t_v. It charges endpoint tolls and ignores nonnegative excesses except where a forced edge requires paying its excess. These bounds remain safe but need not be exact. Of 26 nonseparable small controls, 25 were not closed by the inexpensive bound and directly constructed tour. Those failures are recorded.

### 1.4 Exact contraction closes the nonseparable gap

The continuation then removes the separability requirement from exact solving. Each selected connector and its two module paths contract into a path unit. A state retains the set of visited units and the actual free endpoint of the last unit; it does not merge states merely by boundary degrees. Local path endpoint tables supply the cost of every unit traversal, and the original repair matrix supplies all links.

There are m = k/2 units. A subset DP over these units, with root entrance retained, exactly optimizes arbitrary secondary repair costs. With local weighted subset tables, its arithmetic complexity is

\[
O\!\left(n^2+kb^2 2^b+m^2b^3 2^m\right).
\]

For ten-vertex modules, the global subset exponent is n/20 rather than n. The prototype enumerates local paths instead of using the optimized local weighted subset implementation, so its worst-case dependence on variable b is factorial locally; it has 16 paths per port in the tested Petersen module. The separate certificate checker recomputes local weighted path tables by subsets.

On a nonseparable, nonplanted 180-city instance:

| Certificate/search stage | Cost |
|---|---:|
| Endpoint-toll lower bound | 1,330,163 |
| Directly constructed feasible tour | 1,330,192 |
| Exact contracted DP optimum | 1,330,166 |

The exact solver uses nine path units. Its retained certificate contains 147,528 DP entries, covering both connector patterns and every root entrance. A separate standard-library checker recomputes local path costs from the original secondary matrix, checks all required states are present, verifies all Bellman equalities using 6,200,064 predecessor comparisons, and independently verifies the original tour cost.

The all-root 1-tree obstruction also holds on this nonplanted weighted family: each forced fractional point has cost at most B(2n+8)+nW < C_0. In the nonseparable 180-city instance, this uniform analytic upper bound is 1,328,768, below the primary tour lower bound 1,328,769 and the exact optimum 1,330,166. The successful exact contraction is therefore not an artifact of planting the answer.

This is an exact solution with a checkable lower certificate, not a tour improvement reported without optimality evidence.

## 2. P3: deterministic convergence beyond trees

Let G be a connected graph whose biconnected blocks, including bridges as two-vertex blocks, have at most b vertices. Assign arbitrary positive real lengths to its edges and use its shortest-path metric on all vertices.

Every sequence of strict cycle-preserving 2-opt improvements satisfies

\[
N_{\mathrm{moves}}\le n\sum_B\binom{|B|}{2}2^{\binom{|B|}{2}-1}
\le n(n-1)b2^{\binom b2-2}.
\]

For blocks of size at most four, this is 64n(n-1). The statement covers first improvement, best improvement and any other rule choosing strictly improving moves, from any initialization. Full neighborhood rescanning gives O_b(n^4) arithmetic/comparison work. Distances must still be computed, and arbitrary real-number arithmetic is not being treated as an automatic bit-complexity result.

### 2.1 The new structural lemma

Distances decompose over the block-cut tree. Project each city onto each block's attachment vertex; a tour's cost is the sum of its projected block costs.

For any two pairings of four cities, the nonzero changes in those block costs all have the same sign. A block seeing four distinct projections is the only block that can contribute. Otherwise, every contributing block has one preferred pairing and two equal alternatives. Its preferred pairing corresponds to a 2-versus-2 edge split of the same terminal tree; incompatible preferred pairings would require crossing tree splits. Hence they cannot coexist.

An improving 2-opt move therefore never worsens any block contribution. This extends the tree-cut observation from the handoff to blocks with nontrivial internal metrics.

### 2.2 Removing dependence on arbitrarily small gains

For a block with D = binom(|B|,2) distances, there is a positive integer metric with all distances at most D2^(D-1), preserving the signs and equalities of every four-label 2-opt comparison, including repeated projected labels.

The proof encodes those signs as a feasible integral linear system, selects a vertex, and applies Cramer's rule and Hadamard's determinant inequality. Repeated-label comparisons also preserve the triangle inequalities. This is a direct specialized weight-compression argument; weight compression in general is established background, not itself a claimed invention here.

Glue the integer block metrics along the same block-cut tree. Noncancellation makes every global 2-opt gain sign unchanged. The resulting integer tour cost decreases by at least one on every original improving move and starts below n times the sum of the block distance bounds. That proves the theorem without a lower bound on the original positive gains.

### 2.3 Checks and boundaries

The generated tests verify 183,858 quartet comparisons on 160 trees of small blocks. They include 34,424 comparisons with multiple nonzero block contributions. All pass the sign-consistency test. The test lengths include very large powers of ten to exercise weight disparity.

There are 112 retained exact integer metric certificates. The construction checks 5,076 distinct nonzero local gain rows, 28,188 global gain signs, 96 identical fixed-scan first-improvement trajectory pairs, and 780 actual strict moves. The independent saved-certificate reader checks all 29,414 ordered four-label comparisons, including repetitions and zero rows, directly from the saved matrices.

The theorem does not say that a local optimum is globally optimal when blocks contain cycles. It does not bound nearest-neighbor approximation quality on all sparse random metrics, and it does not extend to arbitrary bounded-treewidth generating graphs.

There is an explicit limit to the proof technique: on the path with lengths (1,1,10,1,1), the 3-opt exchange from tour (0,1,3,2,4,5) to (0,1,2,4,3,5) decreases cost from 48 to 30 while increasing one generating-cut crossing count from two to four. Thus the blockwise argument must not be extended to arbitrary 3-opt or Lin-Kernighan moves without additional reasoning.

## 3. Verification record

| Check | Scope | Result |
|---|---|---|
| Completion bounds vs unstructured Held-Karp | 52 complete instances, 2,484 forced-edge optima | All valid |
| Contracted exact solver vs unstructured Held-Karp | The same 52 instances, including all 26 nonseparable cases | All optima agree |
| Four-cost separation | Every one of 16,110 forced fractional witnesses | Strictly below optimum |
| Subtour certificate | 179 integer flows | Capacity and conservation valid |
| Saved contracted DP | 147,528 entries; 6,200,064 comparisons | Recurrences and optimum valid |
| Blockwise gains | 183,858 quartet comparisons | No cancellation |
| Saved integer metrics | 112 metrics; 29,414 ordered comparisons | Every sign and triangle valid |

The two 52-case checks use the same controlled instances, not 104 distinct test instances. Small-instance checks and the general proofs have different roles. No finite check is represented as a proof of an unrestricted conjecture.

## 4. What changed and what remains

The handoff's necklace obstruction showed that uniqueness and rooted 1-tree bounds do not guarantee a sparse residual. This continuation characterizes its exact minimum-repair face, builds stronger forced-edge certificates, proves a four-small-cost separation, and supplies an exact solver for arbitrary bounded secondary costs on the promised necklace family. The separable case is polynomial for fixed module size; the arbitrary secondary case uses the contracted subset DP.

The handoff's tree analysis showed cut monotonicity on trees. This continuation proves blockwise noncancellation for general block trees and obtains a deterministic quadratic move bound when the block size is fixed.

These are programme-local advances. They do not establish a new generic polynomial-time TSP solver, a better universal metric approximation ratio, a general residual-width theorem, a general sparse-metric nearest-neighbor ratio, or improved real-world benchmark performance. Q3818/P5 received no additional result in this continuation, and the earlier claimed count theorem is not used by these proofs. The other catalog questions are not marked resolved.

The main integration bottleneck is discovering useful two-port modules and proving their repair budget in an arbitrary residual graph, rather than receiving the necklace structure as input. For descent, the corresponding mathematical boundary is an unbounded biconnected component or an exchange involving more than two tour edges. The exact nonseparable DP and the explicit 3-opt counterexample identify these boundaries rather than concealing them.

## Sources and reproducibility

The original programme and three relevant predecessor notes are retained byte-for-byte under sources/, with archive members and SHA-256 hashes in sources/PROVENANCE.json. They are background and provenance, not new deliverables. External primary-source context and the limited literature search are recorded in sources/LITERATURE.md. No public repository or catalog status was changed.

Use README.md for commands. The complete saved-certificate audit requires only Python's standard library. Regenerating all experiments additionally uses a C++17 compiler, NetworkX, NumPy, SciPy and SymPy. Exact checks are rerunnable; timing figures in receipts are single-environment measurements, not matched-budget comparisons against other solvers.
