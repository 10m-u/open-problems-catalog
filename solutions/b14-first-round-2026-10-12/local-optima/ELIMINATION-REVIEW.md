# Independent review of the main B14 elimination thread

**Finding:** the rooted forced-minimum-1-tree bounds and the strict edge-deletion rule in [one_tree.py](../elimination/one_tree.py) are sound under the declared symmetric nonnegative integer-cost model. Signed integer potentials and tied transformed costs do not invalidate them. I also reviewed the independent calculations in [check_certificate.py](../elimination/check_certificate.py).

## Why the bound is valid

With positive scale $s$ and integer potentials $p_v$, transformed weights are $w_{uv}=s c_{uv}+p_u+p_v$. Every tour has transformed cost $s c(T)+2\sum_vp_v$, because each vertex has degree two. A tour is a rooted 1-tree: deleting its chosen root and the two incident edges leaves a spanning path. Hence the minimum rooted 1-tree value minus $2\sum_vp_v$, divided by $s$, is a valid tour lower bound. The same inclusion holds when an edge is forced.

For a fixed root $r$, let $T$ be a minimum spanning tree on $V\setminus\{r\}$. If a nonroot edge $e=uv$ is forced, its minimum spanning-tree value is

$$
w(T)+w_e-\max_{f\in P_T(u,v)}w_f.
$$

The upper bound comes from inserting $e$ in $T$ and deleting a maximum-weight path edge; if $e\in T$, the correction is zero. For the lower bound, let $S$ be any tree containing $e$. Deleting $e$ partitions $S$ into two components. The path $P_T(u,v)$ crosses this partition in an edge $f$. Then $S-e+f$ is an unforced spanning tree, so $w(S)-w_e+w_f\geq w(T)$. Since $w_f$ is at most the maximum path weight, the stated expression lower-bounds $w(S)$. This proof permits negative and tied weights. The implementation's path traversal starts with `None`, rather than zero, and therefore computes negative path maxima correctly.

The root edges are independent of the nonroot tree selection. If a root edge $rv$ is forced, their minimum sum is $w_{rv}+\min_{u\ne r,v}w_{ru}$; otherwise it is the sum of the two cheapest distinct spokes. These are exactly the implemented formulas. The two spokes must be distinct, which both producer and checker enforce.

If $U$ is the cost of a checked feasible incumbent tour, deleting only edges with forced lower-bound numerator greater than $sU$ preserves every optimal tour. Equality is deliberately retained. Taking the largest valid bound for an edge over different roots or potentials preserves validity even when the bounds have different owners. The producer retains the owner certificate for each bound.

## Independent exact checks

[check_elimination.py](check_elimination.py) enumerates spanning trees using Prüfer sequences, without Prim, Kruskal, or the path-max formula. It also enumerates tours directly, up to reversal. It checks all roots for four instances at each $n=3,4,5,6,7$, including a complete tie instance, negative potentials making transformed edges negative, and mixed signed potentials.

The check passed:

- 100 snapshots and 1,280 forced-edge bounds agree with exhaustive spanning-tree and root-pair enumeration.
- Each forced bound is at most the minimum cost of a tour containing its edge.
- Strict deletion preserves every optimum tour in the exhaustive tour set.
- The main standalone checker accepts each independently recomputed certificate.
- 69 snapshots have negative transformed edges, and 69 have tied transformed weights.

The reproducible output is [ELIMINATION-CHECK-RESULTS.json](ELIMINATION-CHECK-RESULTS.json). Run `python3 solutions/b14-first-round-2026-10-12/local-optima/check_elimination.py`.

The standalone checker separately verifies tree connectedness and minimum cost by Kruskal, the minimum distinct root pair, each forced tree or root-pair value, the original-cost incumbent, and the exact deletion/residual lists. It recomputes costs from the original input matrix and supplied potentials. It does not depend on the producer's path maxima, optimal-tour claim, or heuristic width calculation for the mathematical certificate.

## Review of the all-size tree-metric obstruction

The main thread's proposed tree-metric argument is also sound. Let a weighted tree have the city set as its vertices, nonnegative edge weights, and total weight $W$. Its complete-graph costs are tree-path distances. Fix any distinct cities $a,b$.

Double every tree edge and remove one copy of each edge on the simple $a$–$b$ path. Every original tree edge still has a copy, so the remaining multigraph is connected. Its only odd-degree vertices are $a,b$, so it has an Euler trail from $b$ to $a$. This trail visits every city. Prefix it with traversal of the removed path from $a$ to $b$, yielding a closed walk of cost $2W$.

Shortcut that initial path to the prescribed metric edge $ab$. Do not retain its intermediate cities at this stage: retain their first subsequent visits on the remaining Euler trail. Skip subsequent occurrences of $a,b$ and other already retained cities, retaining the final return to $a$. Connectedness of the remaining trail ensures every deferred city appears, so this produces a Hamiltonian tour containing $ab$. Triangle inequalities give tour cost at most $2W$.

Conversely, each tree edge separates the cities into two nonempty sets. A Hamiltonian cycle crosses that cut at least twice. Expanding every metric tour edge as its unique tree path expresses its cost as $\sum_f w_f$ times its cut-crossing multiplicity. Hence every tour costs at least $2W$. The constructed tour is optimal. Since $a,b$ were arbitrary, every complete-graph edge belongs to an optimum.

Consequently no valid forced-cost lower bound can strictly exceed a feasible incumbent $U$ for any edge: its forced optimum is $2W\leq U$. This obstructs deletion based on excluding an edge from **every** optimum. It does not obstruct retaining just one optimum, or returning the edges of an already certified optimal tour. The tree-on-city-set assumption matters; unused Steiner branches would invalidate the assertion that every tree cut partitions the cities into two nonempty parts.

## Limits of this review

This validates the lower bounds and their use in safe elimination; it does not establish that the chosen potential schedule finds strong bounds efficiently. Equal snapshot counts also need not mean equal elapsed time. The residual minimum-fill width is an upper bound on treewidth, and sparsity alone does not guarantee useful decomposition. Benchmark generalization and any practical speed claim must be assessed from the main experiment's actual scope.
