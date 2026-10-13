# Q3817 attempt 3: pointwise domination by a spanning-tree cost fails

**Proposed full-scope route.** Expand NN's metric edges into shortest paths in the sparse generating graph, then bound its complete walk by a constant times a spanning-tree cost, uniformly in the positive edge weights. A pointwise estimate $NN_v\le C_c\,MST$ for $|E|\le cn$ would immediately give the desired expected approximation bound because $MST\le OPT$.

**Outcome.** This domination fails already on trees, and it fails on open positive-probability events in the actual independent-$\operatorname{Exp}(1)$ model. The failure concerns this sufficient pointwise step, not the expected-ratio conjecture. An expectation-only global amortization is still possible.

## The valid exploration observation

An NN move cannot have an unvisited vertex strictly inside its shortest path: that intermediate city would be a strictly closer unvisited choice. Thus, after expansion, each move traverses visited cities and discovers only its final city. The visited set in the generating graph remains connected. On a tree this is exactly the nearest-unvisited exploration rule with its boundary edges revealed. This valid observation does not imply that exploration behaves like DFS or pays only a constant number of traversals per generating edge in total.

The deterministic warning is already published: [Fritsch, *Online graph exploration on trees, unicyclic graphs and cactus graphs*, §2, Lemma 2.1 and Theorem 2.2](https://arxiv.org/abs/2004.06690) constructs recursively spiked trees with logarithmic NN/OPT. Its tree has $2^{k+1}-1$ vertices, connecting-edge lengths equal to the recursion level and unit leaf spikes. The source lower-bound order can use ties. The following independently checked modification removes those ties while retaining the logarithmic ratio; it makes the obstruction relevant to a pointwise/almost-sure envelope under continuous random weights.

## A strict recursive family

Fix an integer $K\ge1$ and $\epsilon=1/(4K)$. Define $T_0$ to be a single vertex with coincident designated left, right and middle vertices. For $1\le j\le K$, take two disjoint copies of $T_{j-1}$, join the left copy's right vertex to the right copy's left vertex by an edge of weight $j$, and attach a fresh leaf $m_j$ to the latter vertex by an edge of weight $1+\epsilon j$. The new left and right vertices are the outermost designated vertices of those copies.

Let $P_j$ concatenate the left copy's order $P_{j-1}$, the right copy's order, and finally $m_j$. There is no duplicated vertex in this order. Define the backbone length $p_j$ and total edge weight $W_j$. Direct induction gives

\[
n_j=2^{j+1}-1,\qquad
p_j=2^{j+1}-j-2,\qquad
W_j=3\cdot2^j-j-3+\epsilon(2^{j+1}-j-2).
\tag{1}
\]

The last term follows because there are $2^{j-i}$ spikes of level $i$, and $\sum_{i=1}^j i2^{j-i}=2^{j+1}-j-2$.

**Strict-order claim.** Starting at the left vertex of $T_K$, NN has exactly the order $P_K$, with strict preference at every nonfinal departure.

Here is an inductive proof that also controls embedded subtrees. For $T_j$, assume any exit edge at its left vertex has weight at least $1+\epsilon(j+1)$, and any exit edge at its right vertex has weight at least $j+1$. Missing exit edges are allowed. The order $P_j$ explores the subtree before any outside city. These exit lower bounds hold for both children in the recursive construction; multiple exit edges cause no change.

For $j=1$, the initial backbone edge of weight 1 beats every left exit, and its spike of weight $1+\epsilon$ beats every right exit of weight at least 2. For $j\ge2$, first apply induction to the left child. Its final middle leaf has distance $R=1+\epsilon(j-1)+p_{j-2}$ to the child's right vertex and distance $R+(j-1)$ to its left vertex. The next right-copy city is at distance $R+j$. Any outside city reached through the left boundary is at distance at least $R+j+\epsilon(j+1)$, which is larger. Every other possible route to an unvisited city on the right passes through that next right-copy city. Hence NN goes there strictly.

Apply induction to explore the right copy. Its last middle leaf has distance $R+(j-1)$ to that copy's left vertex. The new parent spike is at distance $R+j+\epsilon j$. A right-boundary exit has distance at least $R+j+1$, and is farther because $\epsilon j\le1/4$. A left-boundary exit requires the additional connector, the left backbone, and a positive exit edge and is also farther. Thus NN visits the parent spike strictly. This completes the induction. All weights are positive, so paths containing another unvisited intermediate city cannot create an omitted nearer competitor.

Each spike is a leaf and contributes twice its weight to any closed metric tour. Therefore, increasing the level-$i$ spikes from 1 to $1+\epsilon i$ adds $2\epsilon\sum_i i2^{K-i}$ to the cost of this fixed order. Alternatively, summing the two inter-copy moves in the induction gives the same expression. Its closed NN cost is

\[
N_K=(K+2)2^K-2+2\epsilon(2^{K+1}-K-2).
\tag{2}
\]

For every positive weighted tree, $OPT=2W$ by the generating-edge cut lower bound and a doubled-tree walk. Its metric MST also has cost $W$: expanding any metric spanning tree must cross every generating-edge cut, whereas the generating tree itself attains $W$. Consequently,

\[
\frac{N_K}{OPT}
=\frac{N_K}{2W_K}
\ge\frac{(K+1)2^K}{7\cdot2^K}
=\frac{K+1}{7}.
\tag{3}
\]

Here $N_K\ge(K+1)2^K$ for $K\ge1$ and $W_K\le(3+1/(2K))2^K\le(7/2)2^K$. Since $K+1=\log_2(n_K+1)$, no size-independent pointwise constant is possible, even at sparsity $c=1$.

## Why continuous exponential weights do not repair this step

For each fixed $K$, finitely many strict NN comparisons have a positive smallest gap $g_K$. Changing each generating edge by at most $\delta<g_K/[4(n_K-1)]$ changes any tree-path length by at most $(n_K-1)\delta$ and any comparison by at most $2(n_K-1)\delta<g_K/2$. The entire NN order thus survives on an open product box around these weights. The ratio is continuous on that box; shrinking it further preserves any strict lower threshold below (3).

Every such positive-weight product box has positive probability under independent $\operatorname{Exp}(1)$ weights:

\[
\Pr\{w_e\in(a_e,b_e)\ \forall e\}
=\prod_e(e^{-a_e}-e^{-b_e})>0
\qquad(0<a_e<b_e).
\]

Given any proposed universal pointwise or almost-sure constant, choose sufficiently large $K$ and such a box. The constant fails on an event of positive probability for that fixed sparse tree. This does **not** establish a divergent expected ratio: the event probability may decrease extremely fast with $K$. No probability lower bound uniform in $K$ is claimed.

## Exact finite receipt and limits

[check_mst_envelope.py](check_mst_envelope.py) verifies the complete distance matrix against the prescribed NN order using exact rational arithmetic for $K=1,\ldots,8$, through 511 vertices. All **172,234** competing-choice comparisons are strict. The graph sizes, backbone lengths, sums of weights and closed NN cost agree with (1)–(2); every recorded open-box radius satisfies the path-comparison perturbation bound. Receipt: [MST-ENVELOPE-CHECK-RESULTS.json](MST-ENVELOPE-CHECK-RESULTS.json). The all-size assertion is supplied by the induction, not inferred from these finite tests.

This is the third distinct failed full-Q3817 proof route after the packing integral and the uniform expected charge per edge. It rejects eliminating the stochastic analysis through a universal deterministic generating-tree/MST ceiling. The named path, star and tree-local-search theorems in [RESULT.md](RESULT.md) remain separate partial results. No full Q3817 resolution, novelty claim about the source construction, or expected-ratio counterexample is asserted.
