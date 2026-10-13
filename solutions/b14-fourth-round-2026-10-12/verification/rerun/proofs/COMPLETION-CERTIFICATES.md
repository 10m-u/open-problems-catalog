# B14 P1-P2: exact completion certificates for obstructed two-port necklaces

Date: 2026-10-12. New results in this continuation, extending rather than reattributing the supplied necklace obstruction. Review status: full derivations and independent finite checks; not externally peer-reviewed or formally verified. Literature priority has not been established.

## 1. Results and model

There are three linked results.

**Theorem A: minimum-repair structure.** For an even necklace of two-port modules admitting no spanning port-to-port path, every optimal tour under the dominant primary cost described below uses exactly k/2 repair edges. Its cheap connectors are one of two alternating perfect matchings. Every module contributes one spanning path.

**Theorem B: exact solving and forced-edge certificates.** Endpoint-separable repair costs make the two connector patterns independently optimizable using local Hamiltonian-path tables. For arbitrary bounded secondary repair costs, an exact subset dynamic program operates on k/2 paired path units rather than all n cities. Endpoint-toll lower bounds remain valid without separability and give safe forced-edge deletion certificates.

**Theorem C: separation from every rooted 1-tree bound.** For every even k >= 18 there is a strictly metric instance on n = 10k cities, with four O(n)-sized integer cost values and a unique optimal tour, on which no forced rooted 1-tree bound at any root and any real vertex potentials deletes any edge. The completion bounds delete every nonoptimal edge and retain only the optimal cycle.

### 1.1 Modules and cheap edges

Take an even number k >= 2 of disjoint modules F_i, indexed modulo k. Each module has b vertices and distinct ports L_i,R_i. The proof also permits unequal bounded module sizes, but the implementation uses a common module graph and common b.

Assume:

1. F_i has no Hamiltonian path from L_i to R_i.
2. F_i has a Hamiltonian path starting at each of its ports.

A Hamiltonian path starting at a port therefore ends at a nonport. Let H consist of all module edges and the k ring connectors

\[
e_i=R_iL_{i+1}.
\]

All complete-graph edges outside H are called repair edges. An internal missing edge is a repair edge too; repairs are not assumed to run between modules.

Let n = kb and assign off-diagonal costs

\[
c_e=B\bigl(2+\mathbf1_{e\notin H}\bigr)+s_e,
\qquad 0\le s_e\le W,\qquad B>nW,\tag{1}
\]

with B,W,s_e integers and B positive. These costs are strictly metric: every edge is at least 2B and at most 3B+W < 4B. All claims concern the original complete graph and costs (1), not an unproved restriction to H.

## 2. Exact primary optimum and the two connector patterns

For a tour T, let r(T) be its number of repair edges. In module i, let q_i(T) be the number of incidences of repair edges with vertices of that module. An internal repair contributes two to q_i; an intermodule repair contributes one to each incident module. Thus

\[
\sum_iq_i=2r(T).\tag{2}
\]

If q_i = 0, the tour can cross the module boundary only on its two cheap connectors. It must use both: a nonempty proper subset of a Hamiltonian cycle has an even positive boundary. The part of T inside the module is then a Hamiltonian L_i-to-R_i path. It cannot contain a separate internal cycle because T is a single Hamiltonian cycle. This contradicts the module assumption. Therefore q_i >= 1 for every i, giving

\[
r(T)\ge k/2.\tag{3}
\]

The bound is attained. Select either alternating perfect matching of the ring connectors. In each module choose a Hamiltonian path starting at its selected connector port. Each selected connector joins two of these module paths into a spanning path through a pair of modules. There are m = k/2 such disjoint paired path units. Their free endpoints are nonports. Join the units in an arbitrary cyclic order by repair edges. All these new edges are repairs because they run between distinct modules and neither endpoint is a port. For m = 1, use one edge joining the two free endpoints of the single paired unit. This gives a Hamiltonian tour with exactly k/2 repairs.

Define

\[
C_0=B(2n+k/2).\tag{4}
\]

The constructed tour has cost at most C_0+nW < C_0+B. Every tour with more than k/2 repairs costs at least C_0+B. Therefore every optimum has exactly k/2 repairs.

Equality in (2)-(3) forces q_i = 1 in every module. There can be no internal repair. Each module has exactly one external repair incidence. If h_i is the number of cheap connectors used at that module, its total boundary size is h_i+1, which must be positive and even. Since 0 <= h_i <= 2, necessarily h_i = 1. Thus the selected connectors form a perfect matching of the ring: one of exactly two alternating choices. The restriction to each module is one spanning path from its selected connector port to the incident repair endpoint. A disconnected internal cycle would again contradict global Hamiltonicity.

This proves Theorem A and characterizes every optimal tour. It does not forget connectivity: the paired path units must still be linked into one cycle.

For the underlying unweighted (1,2) necklace, the same proof also gives the exact formula OPT = n+k/2 for even k. The handoff had only needed the lower bound n+ceil(k/2); exact attainment and the characterization of its minimum-repair face are additions here.

## 3. Endpoint-toll completion bounds

Choose nonnegative vertex tolls t_v satisfying

\[
s_{uv}\ge t_u+t_v\tag{5}
\]

for every intermodule repair uv. Equality is not required. Internal repairs cannot occur in a primary-minimal tour, so no toll condition on them is needed.

For module i, selected port p, and endpoint v, let g_i(p;v) be the minimum sum of internal secondary costs over a Hamiltonian p-to-v path using only F_i. Set g_i(p;v) = infinity when there is no such path. Put

\[
h_i(p;v)=g_i(p;v)+t_v,
\qquad h_i(p)=\min_vh_i(p;v).\tag{6}
\]

For connector pattern j in {0,1}, let C_j be its connectors and p_i(j) the selected port in module i. Define

\[
S_j=\sum_{e\in C_j}s_e+\sum_i h_i(p_i(j)).\tag{7}
\]

Every primary-minimal tour with this pattern has secondary cost at least S_j: each internal path contributes at least its g value, and each free endpoint is incident to exactly one repair, allowing its toll to be charged once. Consequently

\[
L=C_0+\min(S_0,S_1)\tag{8}
\]

is a global lower bound. To check the other primary levels, each S_j is at most the cost of a constructed primary-minimal completion, hence at most nW < B. Tours outside that face cost at least C_0+B > L.

If every intermodule repair is exactly endpoint-separable,

\[
s_{uv}=t_u+t_v,\tag{9}
\]

choose a minimizing local path in each module and join the paired units cyclically. The cost is exactly C_0+S_j. Thus

\[
\boxed{OPT=C_0+\min(S_0,S_1)}\tag{10}
\]

and an optimal tour is constructible. This is not an oracle that needs to know the optimum tour beforehand.

If the repair excess delta_uv = s_uv-t_u-t_v is merely nonnegative, (8) remains a valid bound, but arbitrary linking may not attain it. The exact solver in Section 5 handles these excesses; the lower bound alone must not be called an exact solution.

## 4. Forced-edge lower bounds and safe deletion

Let an actual feasible incumbent of cost U < C_0+B be supplied or constructed. For every edge e, obtain a pattern-specific secondary lower bound A_e,j as follows.

**Cheap connector.** If e belongs to C_j, take A_e,j = S_j; otherwise it is incompatible with this pattern.

**Cheap internal edge in module i.** Let h_i^e(p) minimize internal path secondary cost plus the free-endpoint toll over Hamiltonian paths starting at p and using e. Then

\[
A_{e,j}=S_j-h_i(p_i(j))+h_i^e(p_i(j)).\tag{11}
\]

No feasible forced local path means the edge is incompatible with the pattern.

**Internal repair.** It is incompatible with every primary-minimal pattern.

**Intermodule repair e = uv between modules i and l.** Both u and v must be feasible free endpoints. If k > 2, modules i and l must not be joined by the same selected cheap connector: joining that paired unit's two free endpoints would prematurely close a cycle while other units remain. For compatible endpoints and units,

\[
\begin{aligned}
A_{e,j}={}&S_j-h_i(p_i(j))-h_l(p_l(j))\\
&+h_i(p_i(j);u)+h_l(p_l(j);v)+\delta_{uv}.\tag{12}
\end{aligned}
\]

Other repairs still contribute at least their endpoint tolls. For k = 2, closing the sole paired unit is permitted.

The safe full-instance forced-edge lower bound is

\[
\boxed{L_e=\min\left\{C_0+B,\ C_0+\min_{j\text{ compatible}}A_{e,j}\right\}.}\tag{13}
\]

The first term is essential. Incompatibility on the primary-minimal face does not imply that no more expensive tour uses e. Formula (13) covers all primary levels. Delete e only if L_e > U. The proof does not compare a locally modified or rounded cost matrix with U.

For a fixed module size b, local Held-Karp tables from the two ports compute all g_i(p;v) in O(kb^2 2^b) arithmetic operations. Running an augmented table with a required-edge flag for each of O(b^2) internal edges gives all forced-local sensitivities in O(kb^4 2^b). Constructing and verifying a fully explicit complete cost matrix adds O(n^2) work. The prototype enumerates local Hamiltonian paths instead of using these optimized local weighted tables; its parameter overhead is factorial in b in the worst case. It enumerates only 16 paths per port for the ten-vertex module used in the larger checks. The separate saved-certificate checker computes the local weighted subset tables independently.

## 5. Exact contraction for arbitrary secondary repair costs

The following algorithm does not assume (5) or (9); it only uses the cost range and dominant primary gap in (1). The implemented combined interface retains a toll envelope because it also computes the bounds above. Zero tolls make the envelope valid for every nonnegative secondary matrix.

Fix one alternating connector pattern. It has m = k/2 paired units. Unit j consists of modules a_j,b_j, joined at their selected ports. Let E_i be the feasible free endpoints for module i, and abbreviate g_i(v) = g_i(p_i;v). An oriented traversal of unit j enters at u in E_a and exits at v in E_b, or the reverse. Its secondary cost is

\[
g_a(u)+s_{\mathrm{connector}(j)}+g_b(v).\tag{14}
\]

This equality minimizes over local path choices without losing any information needed by future completion: the two ends are retained, and the interior has no remaining external attachments. Each local path can be independently replaced by a cheapest path with the same endpoints.

For a previous unit's exit x and a desired exit v of a new unit j, let i be the module of v and let i' be the other module of j. Precompute

\[
T(x,j,v)=g_i(v)+s_{\mathrm{connector}(j)}
+\min_{u\in E_{i'}}\bigl(s_{xu}+g_{i'}(u)\bigr).\tag{15}
\]

The edge xu is a repair between distinct units. Remember a minimizing entrance u for reconstruction. Equation (15) incorporates the incoming repair and traversal of the new unit.

Fix root unit 0 and orient its traversal from a_0 to b_0. Every undirected global tour has a direction with this root orientation, so this removes no candidate. For each possible root entrance z in E_a0, define

\[
D_z(S,j,v)
\]

as the minimum secondary cost of a path starting at z, traversing the root unit first, traversing exactly the units in S once each, and ending at exit v of last unit j. The set S includes 0. Initialize

\[
D_z(\{0\},0,v)=g_{a_0}(z)+s_{\mathrm{connector}(0)}+g_{b_0}(v),
\quad v\in E_{b_0}.\tag{16}
\]

For q not in S and each feasible exit v of q,

\[
D_z(S\cup\{q\},q,v)
=\min_{j,x}\{D_z(S,j,x)+T(x,q,v)\}.\tag{17}
\]

Finally add the closing repair s_vz, minimize over last exit, root entrance, and the two connector patterns, then add C_0. For m = 1, initialization followed by that single closing edge is already the complete solution.

Every feasible tour on the primary-minimal face contracts to such a unit cycle by Section 2, and every state transition expands into compatible internal paths and a repair. No premature cycle is permitted because closure occurs only after all units have been visited. Equations (14)-(17) therefore give an exact dynamic program, not a degree-only relaxation.

There are O(mb2^m) states for each fixed root entrance. Precomputed transitions take O(m^2b^3) time. At most b root entrances and two patterns give total arithmetic complexity

\[
\boxed{O\!\left(n^2+kb^2 2^b+m^2b^3 2^m\right),\quad m=k/2.}\tag{18}
\]

Working storage, processing one root entrance at a time, is O(n^2+mb2^m+kb2^b). Retaining a complete certificate for every root entrance increases stored output size accordingly. The prototype's local path enumeration has the caveat already stated after (13).

For ten-vertex modules, the global subset exponent becomes n/20 rather than n. The theorem is restricted to the certified necklace family and dominant primary gap; it is not a generic exponential-time improvement for arbitrary metric TSP. Arbitrary secondary repair costs still encode a genuine global ordering problem, so the special separable case is where subset search disappears altogether.

## 6. A four-cost strict-metric separation from all rooted 1-trees

### 6.1 The ten-vertex module

Use vertices u_0,...,u_4,v_0,...,v_4 and edges

\[
u_ju_{j+1},\qquad v_jv_{j+2},\qquad u_jv_j\ (j=1,2,3,4),
\]

where pentagon indices are modulo five. Ports are u_0,v_0; the missing spoke is u_0v_0. This is the Petersen graph with that spoke removed.

There is no spanning port-to-port path: adding the missing spoke would make a Hamiltonian cycle in the Petersen graph. The retained checker also verifies the required nonexistence directly by ten-vertex subset DP, so this use of the standard graph fact is independently checkable from the listed edges. Hamiltonian paths from both ports do exist; the enumerator finds 16 from each port, with the independently checked endpoint sets given in the receipt.

Take even k >= 18 copies. Construct any primary-minimal Hamiltonian tour T by Section 2, and define

\[
B=n+1,\quad W=1,\quad
s_e=\begin{cases}0&e\in T,\\1&e\notin T.\end{cases}\tag{19}
\]

The only possible edge costs are

\[
2n+2,\quad2n+3,\quad3n+3,\quad3n+4.\tag{20}
\]

Tour T has cost C_0 and is unique as an undirected edge set. Every tour has primary cost at least C_0; any different tour has a non-T edge and hence positive secondary sum. Larger primary levels cannot tie. Thus

\[
OPT=(n+1)(2n+k/2).\tag{21}
\]

The planted tour defines a separation family. This is not a blinded practical benchmark. The independently generated random secondary instances in Section 7 exercise exact solving without planting the answer.

### 6.2 Fractional subtour witness

The fractional point from the handoff assigns value one to the remaining spokes and necklace connectors, one half to each pentagon edge, and zero elsewhere. Its degree at every city is two and its total mass is n.

For completeness, its subtour feasibility can be proved directly. Restore the missing spoke inside one module with value one. In a proper cut, two or more crossing spokes give weight at least two. With zero crossing spokes, the selected outer and inner index sets agree, and both nontrivial pentagon cuts contribute at least one. With one crossing spoke, at least one pentagon cut is nontrivial and contributes one in addition to the spoke. If neither pentagon cut were nontrivial, the two selected index sets would be empty/full, differing in zero or five positions rather than one. Thus every proper cut of the restored weighted module has capacity at least two.

Removing its missing spoke reduces a cut by one exactly when its ports are separated. Every partial module therefore contributes at least one internally, or at least two if its ports are on the same side. For a global proper cut, two partial modules suffice. One partial module with unseparated ports also suffices. With exactly one partial module and separated ports, the alternating cycle of virtual port links and necklace connectors has an even number of side changes: the separated virtual link forces at least one crossing connector. With no partial modules, a proper union of whole modules has at least two crossing connectors. Every subtour cut therefore has weight at least two.

The 180-city check retains an alternative explicit certificate: in integer capacities 2x, it stores a flow of value four from vertex zero to every other vertex. Flow conservation and capacity checks certify all nontrivial cut lower bounds without enumerating exponentially many cuts.

### 6.3 Every edge can be forced in a cheap fractional point

Fix an edge f with x_f = 1. For any prescribed complete-graph edge e, relabel x by a permutation sending f to e using at most two transpositions. At most four vertices move. The relabeled point x^e remains subtour-feasible and x^e_e = 1.

Changing labels changes the primary class only on edges incident to moved vertices. Their total fractional mass is at most eight, using fractional degree two and counting a moved-moved edge at most twice. The original support is entirely cheap. Hence

\[
B\sum_f(2+\mathbf1_{f\notin H})x^e_f\le B(2n+8).
\]

The secondary fractional sum is at most n because s_f <= 1 and total mass is n. Therefore

\[
c^Tx^e\le B(2n+8)+n<B(2n+9)\le C_0,\tag{22}
\]

since B=n+1 and k/2 >= 9.

The same blindness argument is not restricted to the planted secondary costs. For every Petersen necklace of even k >= 18 with arbitrary s_e in [0,W] and B > nW, the relabeled point obeys

\[
c^Tx^e\le B(2n+8)+nW<B(2n+9)\le C_0\le OPT.\tag{22a}
\]

Thus the general exact solver in Section 5 also operates on an entire nonplanted weighted family where every forced rooted 1-tree bound fails to eliminate an edge. Planting in (19) is used only to obtain uniqueness, four small cost values, and deletion down to a single cycle.

### 6.4 Why all roots and all real potentials are covered

Let z be any subtour-feasible point with z_e = 1. Fix any root r. On the nonroot vertices it has total edge mass n-2. For every nonempty nonroot subset S,

\[
z(E(S))=|S|-\tfrac12z(\delta(S))\le |S|-1.
\]

It is therefore a fractional spanning tree. The root spokes lie in [0,1] and sum to two.

For any signed transformed edge weights, a minimum nonroot spanning tree is no dearer than this fractional tree. A direct greedy argument avoids an integrality assertion left unchecked: order edges by increasing weight, let F_j be a prefix and r_j its graphic rank, and sum the displayed inequalities over its connected components to obtain z(F_j) <= r_j. A Kruskal tree has prefix cardinalities r_j. Summation by parts, using equal total edge mass, gives its no-greater weight even when weights are negative.

If the forced edge e is nonroot, contract its unit coordinate. The residual vector satisfies the corresponding spanning-tree inequalities on the contracted multigraph, so a minimum tree containing e is still no dearer. If e is a root spoke, keep it and take a cheapest different spoke; its weight is no greater than the remaining fractional root-spoke weight. Otherwise choose the two cheapest root spokes.

Set transformed weights to c_uv + pi_u + pi_v and subtract 2 sum_v pi_v from the chosen 1-tree weight. Since z has fractional degree two, the potentials cancel exactly in its objective. Thus for every root r and every real potential vector pi,

\[
L_e^{1\text{-tree}}(r,\pi)\le c^Tz.\tag{23}
\]

Applying (23) to z=x^e and (22) proves

\[
L_e^{1\text{-tree}}(r,\pi)<OPT
\]

for every edge, root and potential vector. No such forced bound can exceed a feasible incumbent and delete any edge. This conclusion is analytic, not inferred from trying finitely many potentials.

### 6.5 Completion deletes every non-T edge

Use zero tolls in (5). The connector pattern used by T has S_j = 0. Every internal path with cost zero uses only T edges, so it is the unique T path in its module. An alternative connector pattern incurs positive secondary connector costs. Forcing any non-T cheap internal edge incurs at least one secondary unit. Forcing any non-T intermodule repair incurs delta_e = s_e = 1 whenever it is otherwise compatible. Other edges are excluded from the minimum-repair face and obtain the next-level bound C_0+B. Formulas (11)-(13) therefore give L_e >= C_0+1 for every e not in T. Edges in T cannot be deleted because T is a valid containing tour of cost C_0.

With U = C_0, the residual graph is exactly T: n edges and treewidth two. The 1-tree residual is K_n: binom(n,2) edges and treewidth n-1. This proves Theorem C.

The separation says nothing about the strength of all LP cuts, all local elimination procedures, or Concorde as a complete solver. It isolates one bound family and supplies a stronger completion-based alternative on an explicitly characterized family. Local combinatorial elimination itself predates this work; Cook, Helsgaun, Hougardy and Schroeder, arXiv:2307.07054, is the programme's relevant established baseline.

## 7. Evidence

The basic completion-bound checker uses a separate C++ Held-Karp oracle on 52 complete-graph instances of 8, 10, 12 and 16 cities, including 26 with nonseparable repair excess. It checks 2,484 forced-edge lower bounds against exact forced-edge tour optima. All are safe. The separable formula is exact in all its promised cases. In 25 of the 26 excess cases, the inexpensive endpoint bound and constructed tour do not meet; those failures were retained rather than suppressed.

The new contracted solver was then tested on all 52 oracle instances, and agrees with every exact full-city optimum, including all 26 nonseparable cases. It closes the gap that the separable bound did not close.

Random separable Petersen necklaces at n=20,40,180,400,1000 were exactly solved from their generated secondary matrices without planting a tour. The n=1000 optimum is 41,010,220. This is a correctness and scaling exercise on the promised family, not a comparison against general-purpose solvers.

For nonseparable Petersen necklaces with seed 29, the exact optima are 65,963 (n=40), 263,250 (n=80), 591,644 (n=120), and 1,330,166 (n=180). In the 180-city case, the endpoint lower bound was 1,330,163 and the directly constructed tour cost 1,330,192. The contracted DP has nine units, retains 147,528 table entries across both patterns and root entrances, and evaluates 6,200,064 transitions. It closes the three-unit lower-bound gap and improves that feasible tour by 26. The entire DP table certificate is retained for independent recurrence checking against the original instance.

For the four-cost separating instance, n=180, k=18, B=181, costs are {362,363,543,544}, and the unique optimum is 66,789. All 16,110 edges have explicit cheap forced fractional witnesses; completion deletes 15,930 and retains the 180 tour edges. The checker retains 179 integer flow certificates with 29,358 nonzero signed flow entries. The largest doubled witness objective is 133,017, strictly below the doubled optimum 133,578.

Finite controls support implementation correctness. The arbitrary-k results rely on Sections 2-6, not on extrapolating the checked sizes. The prior handoff's negative necklace construction and forced-1-tree dominance argument are retained in sources/PREDECESSOR-1TREE-OBSTRUCTION.md with archive provenance; their ingredients are not presented as new here.
