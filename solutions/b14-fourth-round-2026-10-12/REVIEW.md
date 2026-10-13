# Review of the B14 fourth return

13 October 2026. Main-thread review against the actual preceding obstruction, state-compression and tree-descent proofs, the two submitted proofs, implementations and complete replay. The three main results are accepted with their explicit assumptions. The original submission is unchanged. This review records mathematical scope separately from computational evidence.

## Minimum repairs and completion

The earlier necklace construction proved a lower bound sufficient to defeat rooted 1-tree elimination. The return additionally proves exact attainment for even $k$, characterizes every primary-minimal tour, and gives exact solving and safe forced-edge bounds on that face.

For every module, zero repair incidence would force a spanning port-to-port path, contradicting the module promise. Thus $2r=\sum q_i\ge k$. Alternating connectors, local port-starting Hamiltonian paths and repairs joining their nonport endpoints construct a tour with $r=k/2$, including the single-unit case $k=2$. Equality forces $q_i=1$: no internal repair, one cheap connector per module and one spanning local path. The selected connectors are exactly one of the two ring matchings. Global connectivity remains necessary after this characterization.

Costs $B(2+\mathbf1_{e\notin H})+s_e$, with $0\le s_e\le W$ and $B>nW$, are strictly metric and force every optimum onto that face. A primary-minimal completion costs less than the next primary level. Endpoint tolls are charged once per local free endpoint. The displayed $S_j$ are lower bounds; equality with endpoint-separable repairs makes the local minimizers simultaneously attainable by linking paired units. Nonnegative repair excesses give bounds without implying attainment.

Forced-local-path and fixed-endpoint restrictions are necessary conditions on tours containing the forced edge. An intermodule repair joining the ends of the same paired unit is excluded when other units remain; for $k=2$ it is the closing edge. Taking the minimum with the next-level bound $C_0+B$ covers tours outside the primary-minimal face. Strict deletion against the actual original-cost incumbent is therefore safe. The cap is essential and is present in the implementation.

## Exact contraction

Every primary-minimal tour contracts to a cycle of paired spanning paths. The local optimum for fixed endpoints can be substituted without changing any external interface. The transition minimizes the incoming repair and entry-side path while retaining the actual exit city. The subset mask enforces one visit per unit; retaining each possible root entrance allows the final closing repair to be priced exactly. Global orientation can be chosen so the root traverses its designated direction, since tours and costs are undirected. Closure occurs only after every unit is visited.

This proves exactness for arbitrary secondary repair costs under the primary gap. The claimed $O(n^2+kb^2 2^b+m^2b^3 2^m)$ arithmetic bound uses local weighted subset tables and $m=k/2$. The provided producer instead enumerates local paths and has factorial worst-case dependence on variable $b$; the review retains that distinction. The global exponent $n/20$ applies only to the ten-city promised modules, not arbitrary metric instances.

## All-root separation

The restored fractional Petersen module has every proper cut at least two, by considering the number of crossing spokes. Deleting its port spoke leaves internal capacity at least one when the ports separate and at least two otherwise. The necklace cut argument then restores the global cut lower bound. Integer flows independently verify it for the retained 180-city point.

Relabeling a unit edge onto any prescribed edge moves at most four vertices, increasing repair mass by at most eight because fractional degrees are two. Total fractional mass is $n$, so the secondary contribution is at most $nW$. The resulting forced subtour point costs at most $B(2n+8)+nW<C_0$ for even $k\ge18$.

For any root, restricting a subtour point to nonroot edges gives the spanning-tree rank inequalities and correct total mass. A forced unit edge can be contracted. Greedy prefix-rank domination and summation by parts bound a minimum tree even for signed transformed costs; the root-spoke selection has the same bound. Degree-two potentials cancel exactly. Thus the domination holds for every real potential and root, not just those tried in a computation.

Planting secondary cost zero on one primary-minimal tour and one elsewhere makes it unique. The completion formulas charge at least one secondary unit for a non-tour edge or exclude it from the face. This deletes precisely the complement of that tour. The four-cost family and its 180-city certificate are accepted. The blindness argument also holds for nonplanted secondary costs; it does not compare against every LP or combinatorial elimination method.

## Blockwise noncancellation

The block-cut tree gives the distance decomposition into local projected metrics. With four distinct projections in one block, every other block sees at most a 3+1 split and contributes the same to all pairings. Otherwise a contributing block sees 2+2 or 2+1+1 and has one preferred pairing, with the other two equal. The duplicated-label fiber has a corresponding branch cut in the block-cut tree, even when that fiber contains several branches at one articulation. Different preferred pairings would give crossing 2-versus-2 terminal splits, which two tree-edge cuts cannot induce. All nonzero block gains therefore share a sign.

Every four-label comparison row has Euclidean norm at most two, including repeated labels. Orient strict rows with right-hand side one, retain zero rows as equalities and impose positive coordinates. Scaling the original metric makes this system feasible. A minimizing extreme point of the positive-coordinate polyhedron has a full-rank active integral basis. Cramer's rule and Hadamard's inequality bound each determinant-scaled coordinate by $D2^{D-1}$. All gain signs and equalities are preserved.

There is one minor wording error in the submitted proof's triangle-inequality parenthesis: for its displayed comparison $w_{ab}+w_{cd}-w_{ac}-w_{bd}$, use $(a,b,c,d)=(u,v,w,v)$, so the second and fourth labels coincide. This gives $w_{uv}+w_{wv}-w_{uw}$; coinciding the second and third labels would give zero. The lemma includes every repeated quadruple, so the proof and checked theorem hold with this corrected witness. The submitted text is preserved as received.

Gluing the positive integer block metrics preserves the global gain sign by noncancellation. It need not preserve gain magnitudes, best-improvement choices or global tour rankings. Every original strict descent decreases the resulting nonnegative integer tour potential by at least one. Its initial value is at most $n\sum_B D_B2^{D_B-1}$. Using $\sum_B(|B|-1)=n-1$ proves the fixed-block-size bound, including $64n(n-1)$ for size four. The existing tree theorem is a predecessor, while noncancellation and the deterministic bounded-block extension are additions. The provided 3-opt counterexample correctly limits this method.

## Replay and disposition

All 34 manifested payloads plus the manifest passed hash checks; all three predecessor excerpts match the live catalog and the original-programme copy matches its provenance hash. A separate runtime copy preserved the received state. All six stages of the complete suite passed; the mathematical structured outputs agree with the submitted receipts after omitting elapsed times. The saved-certificate reader also passed before regeneration, checking the delivered artifacts themselves.

The replay checks 52 complete instances and 2,484 forced bounds, both contracted solver patterns and all root entrances, 147,528 retained DP entries and 6,200,064 Bellman comparisons, 179 flow certificates, 183,858 block comparisons and 112 saved integer metrics. All eight damaged-certificate controls were rejected. The same 52 oracle instances are shared between two comparisons. Twenty-five of 26 nonseparable inexpensive bounds did not close; those controls are preserved and the exact contraction resolves their finite optima.

These are restricted programme advances, filed as three separate result routes. They do not close Q3817 or restart the broader P1 stopping count. All earlier catalog marks, programmes, proofs and failed routes retain their original scopes. The third-round sharp count is separate and is not used here. Published elimination and weight compression remain attributed background; no literature-priority claim is accepted.
