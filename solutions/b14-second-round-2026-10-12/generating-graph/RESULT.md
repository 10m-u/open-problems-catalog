# B14 P1/P2 — Uniqueness does not make 1-tree elimination sparse

**Review state:** independently reviewed by the same continuing subagent; [review](../initialization/UNIQUENESS-REVIEW.md). This follows the [first-round tree-metric obstruction](../../b14-first-round-2026-10-12/elimination/RESULT.md): breaking optimal-tour ties cannot, by itself, solve the residual-density problem.

**Theorem.** For every integer $k\geq17$, there is a strictly metric, positive integer-cost TSP instance on $n=10k$ cities with a unique optimal undirected tour, yet no edge can be deleted using any forced-edge rooted minimum-1-tree bound, at any root and any vertex potentials, against any feasible incumbent.

The claim concerns this bound family, not stronger cuts, branching, combinatorial elimination, or exact solving. No originality claim is made for the construction or its ingredients.

## 1. A necklace of Petersen gadgets

Use $k$ copies of the Petersen graph, each with vertices $u_{i,j},v_{i,j}$, $j$ modulo five, and edges

$$
u_{i,j}u_{i,j+1},\quad
v_{i,j}v_{i,j+2},\quad
u_{i,j}v_{i,j}.
$$

Delete spoke $u_{i,0}v_{i,0}$ in each copy. Connect $v_{i,0}$ to $u_{i+1,0}$, with copy indices modulo $k$. Call this connected cubic graph $H_k$. Its complete-graph metric costs are $a_e=1$ on $H_k$ and $a_e=2$ elsewhere.

Assign a fractional vector $x$ as follows: every remaining spoke and every connector has value one; the outer and inner cycle edges have value $1/2$; all other pairs have value zero. Every vertex has fractional degree two. Its objective value is $n$.

We check every subtour cut. First restore the removed spoke in one Petersen gadget with value one. Any proper subset has cut value at least two: if at least two spokes cross, they suffice; if none cross, the outer and inner selected index sets coincide and their cycle cuts each contribute at least one; if exactly one spoke crosses, at least one of the two cycle cuts contributes one. The exceptional empty/full cycle-side cases also obey this last assertion.

Deleting the spoke reduces a gadget cut by one exactly when its two ports are separated. Thus a partial gadget contributes at least one internally, or at least two when its ports lie on the same side.

For a nonempty proper global subset, two partial gadgets already contribute at least two. One partial gadget with unseparated ports also does. If there is exactly one partial gadget and its ports are separated, the connector ring has at least one crossing: along the alternating cycle of virtual port links and connectors, the number of changes of side is even. The separated virtual link supplies one, so a connector supplies another. Finally, with no partial gadgets, the subset is a proper union of whole gadgets and at least two ring connectors cross. This proves $x(\delta(S))\geq2$ for every nontrivial $S$.

Therefore $x$ is feasible for the subtour LP, of value $n$. Summing degree constraints and using $a_e\geq1$ proves that the unrestricted LP value is exactly $n$.

## 2. Every tour needs many expensive edges

A Hamiltonian tour with no expensive edge incident to a particular gadget must enter and leave it on its only two external cheap edges. Its restriction inside that gadget would be a spanning path from $u_{i,0}$ to $v_{i,0}$ in Petersen minus the removed spoke. Restoring that spoke would give a Hamiltonian cycle in the Petersen graph, which is impossible.

Hence every gadget is incident to an expensive tour edge. Each such edge can cover at most two gadgets, so every tour uses at least $\lceil k/2\rceil$ cost-two edges. In particular,

$$
OPT(a)\geq n+\lceil k/2\rceil.
$$

The Petersen non-Hamiltonicity needed here is checked exhaustively in the first-round receipt and separately by the checker below. The construction supplies a lower bound on all tours; an exact optimum formula is unnecessary.

## 3. Every forced edge has a cheap fractional witness

Choose one edge $f$ with $x_f=1$. For any prescribed edge $e=ab$, there is a permutation $\sigma$ of the cities mapping the endpoints of $f$ to $a,b$, made from at most two transpositions. At most four vertices move.

Relabeling $x$ by $\sigma$ preserves the complete-graph degree, box and subtour constraints, and yields $x^e_e=1$. Edges whose costs can change are incident to the moved vertices. Their original total fractional mass is at most twice the number of moved vertices, hence at most eight. Each individual cost changes by at most one. Consequently

$$
a^Tx^e\leq n+8
$$

for every complete-graph edge $e$. A witness with an edge fixed to one is stronger than merely having positive fractional mass on that edge.

## 4. Any forced 1-tree bound is below its fractional witness

Let $z$ satisfy all subtour-LP constraints and $z_e=1$, and choose any root $r$. On nonroot vertices, the vector has total mass $n-2$, and for every nonempty nonroot subset $S$,

$$
z(E(S))=|S|-\tfrac12z(\delta(S))\leq |S|-1.
$$

Thus it is a fractional spanning tree; the root spokes lie in the box $[0,1]$ and have total mass two.

Here is a direct justification that a minimum spanning tree is no dearer than this fractional tree, including signed transformed weights. Sort nonroot edges by weights $\omega_1\leq\cdots\leq\omega_m$, and let $F_i$ be the first $i$ edges. Summing the displayed inequalities over the connected components of $F_i$ bounds $z(F_i)$ by its graphic rank $r_i$. Kruskal's greedy tree has exactly $r_i$ edges in each prefix. The identity

$$
\sum_j\omega_jz_j
=\omega_m(n-2)-\sum_{i<m}(\omega_{i+1}-\omega_i)z(F_i)
$$

therefore lower-bounds the Kruskal tree weight. This uses no sign assumption on the weights. The two cheapest distinct root spokes similarly minimize weight over their box with total mass two.

If the forced edge is a nonroot edge, contract it. Removing its unit coordinate leaves the same fractional-tree inequalities in the contracted multigraph: a subset containing the merged endpoint corresponds to a subset with one additional vertex before contraction. The forced edge plus a minimum tree after contraction is no dearer than the fractional tree. If the forced edge is a root spoke, its unit coordinate is fixed and the cheapest other spoke is no dearer than the remaining fractional root mass.

For transformed costs $w_{uv}=d_{uv}+\pi_u+\pi_v$, fractional degrees are two, so subtracting $2\sum_v\pi_v$ cancels the potentials exactly. It follows that the forced minimum-1-tree bound obeys

$$
L_e(r,\pi)\leq d^Tz.
$$

This holds for every root and every real potential vector, independently of any tuning schedule.

## 5. A strict metric with a unique optimum

Rank all $m=\binom n2$ complete-graph edges from zero to $m-1$, set $B=2^m$, and define

$$
d_e=B(a_e+1)+2^{\operatorname{rank}(e)}.
$$

These positive integers form a strict metric: each edge costs less than $7B/2$, while each two-edge path costs more than $4B$.

Every tour's secondary sum is less than $B$, and different undirected edge subsets have different binary sums. Thus the primary integer cost order is preserved and the optimum is unique. Every tour costs at least

$$
B(2n+\lceil k/2\rceil).
$$

For each forced-edge LP witness, the degree sum gives $\sum_f x^e_f=n$. Also $0\leq x^e_f\leq1$ gives a secondary sum less than $B$. Hence

$$
d^Tx^e < B(2n+9)\leq B(2n+\lceil k/2\rceil)\leq OPT(d)
$$

when $k\geq17$. Section 4 now proves $L_e(r,\pi)<OPT(d)$ for every $e,r,\pi$. Every feasible incumbent has $U\geq OPT(d)$, so no strict comparison $L_e>U$ can delete any edge. The residual is $K_n$, of treewidth $n-1$.

The construction has a polynomial binary encoding: $m$ extra bits per cost. Large numerical magnitudes are not required to be printed or materialized in the checker.

## Consequence for B14

The first-round obstruction arose from a complete union of tied optimal tours. This one removes ties and keeps a uniform gap below every forced 1-tree bound. A universal residual-width theorem based only on uniqueness and this relaxation is false.

The next exact-solver direction must use stronger structural information, additional cuts or branching, or operate on a supplied sparse graph that generates the metric. This result closes the proposed universal uniqueness route; it does not close P1/P2 or Q549.
