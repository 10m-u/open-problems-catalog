# B14 P1 — Certified elimination and its structural limits

The first round implements exact forced-edge minimum-1-tree bounds, checks every deletion independently, and measures residual exact-search work on a bounded set of small metric instances. It also identifies an all-size obstruction: a tree metric can require retaining the complete graph when every optimal tour must be preserved.

The sensitivity formulas are established minimum-1-tree mathematics, closely related to alpha-nearness. This packet makes no novelty claim for them. Certified elimination is already a developed TSP method; compare [Cook, Helsgaun, Hougardy and Schroeder](https://arxiv.org/abs/2307.07054). The contributions here are a reproducible baseline, independent certificates, and scope restrictions for the proposed B14 pipeline.

## 1. Exact forced-edge bound

Let costs $c_{uv}$ be symmetric and choose arbitrary vertex potentials $\pi_v$. Define

$$
w_{uv}=c_{uv}+\pi_u+\pi_v.
$$

Fix a root $r$. A rooted 1-tree consists of a spanning tree on $V\setminus\{r\}$ and two distinct edges incident to $r$. Every tour is such a 1-tree. If $T$ is a minimum spanning tree on the nonroot vertices, and $s_1,s_2$ are the two least root-edge weights, then

$$
L=w(T)+s_1+s_2-2\sum_v\pi_v
$$

is a valid lower bound on every tour. Transformed weights may be negative; the argument still holds.

For a nonroot edge $e=uv$, let $P_T(u,v)$ denote its path in $T$. The exact minimum 1-tree cost under the requirement $e\in H$ is

$$
L_e=L+w_e-\max_{f\in P_T(u,v)}w_f.
$$

To prove the spanning-tree part, add $e$ to $T$ and remove a maximum-weight edge $f$ on its resulting cycle. This constructs a tree of the stated cost. Conversely, remove $e$ from any tree $R$ containing it. The $T$-path from $u$ to $v$ has an edge $g$ crossing the resulting cut, with $w_g\leq w_f$. Minimality of $T$ gives $w(T)\leq w(R)-w_e+w_g$, hence $w(R)\geq w(T)+w_e-w_f$. This covers ties, negative weights, and $e$ already in $T$.

For a root edge $rv$, forcing that spoke gives

$$
L_{rv}=L+w_{rv}+
\min_{z\notin\{r,v\}}w_{rz}-s_1-s_2.
$$

The second spoke must have a different endpoint. The same minimum spanning tree remains available.

If a feasible tour has cost $U$, delete an edge only when $L_e>U$. Every tour using it is then worse than the incumbent; in particular every optimum survives. Equality is retained. Bounds from different roots and potential vectors can be combined by taking their maximum for each edge.

For one fixed root and potential vector, dense Prim and all tree-path maxima give all forced-edge bounds in $O(n^2)$ arithmetic operations. Integer bit complexity and repeated potential updates require their own accounting.

## 2. Arithmetic and independent verification

[one_tree.py](one_tree.py) uses integer costs and potentials represented in units of $1/16$. All transformed weights and comparisons are integral numerators, avoiding tolerance-dependent deletions.

[check_certificate.py](check_certificate.py) reconstructs both unrestricted and forced minimum spanning trees with Kruskal's algorithm, checks the two root spokes, the incumbent tour, every forced-edge bound, and the residual edge partition. It does not trust the producer's Prim tree or path-max calculation.

The [validation receipt](validation.json) covers 147 certificate packets and 6,807 forced-edge bounds. Five deliberately corrupted certificates are rejected. Another 24 four-vertex cases cover zero costs, ties, and signed transformed weights.

The other research agent then performed an [independent exhaustive audit](../local-optima/ELIMINATION-REVIEW.md): 100 snapshots and 1,280 forced bounds for $n=3,\ldots,7$, using Prüfer-tree enumeration and every root-spoke pair. Direct enumeration of tours verified both the lower bounds and preservation of every optimum. These include 69 snapshots with negative transformed weights and 69 with ties.

## 3. Bounded experiment

[run.py](run.py) generates four families, at $n=8,10,12$ with four seeds each:

- rounded-up Euclidean distances between integer points;
- the same construction with three separated clusters;
- shortest-path metrics from independent integer complete-graph edge weights;
- weighted tree metrics.

Each instance receives a nearest-neighbor incumbent followed by deterministic best-improvement 2-opt. The subset-DP optimum is used only for verification and reporting. The random shortest-path family is not the sparse exponential model of Q3817.

Three methods are compared: zero potentials; 48 subgradient evaluations at root zero; and 48 evaluations split equally over four roots. The latter two have equal evaluation counts, not a measured equal-time budget. All reported deletion counts sum over 12 instances per family, with 556 possible edges in each family. Width is the mean upper bound from a greedy fill ordering, not exact treewidth.

| Family | Method | Deleted edges | Mean width upper bound | Residual subset-DP transitions |
|---|---|---:|---:|---:|
| Euclidean | zero | 92 | 6.83 | 208,231 |
| Euclidean | single root | 416 | 2.33 | 1,290 |
| Euclidean | four roots | 416 | 2.33 | 1,390 |
| Clustered Euclidean | zero | 22 | 8.08 | 264,092 |
| Clustered Euclidean | single root | 403 | 2.42 | 1,207 |
| Clustered Euclidean | four roots | 148 | 5.58 | 158,517 |
| Random shortest-path | zero | 22 | 8.17 | 256,788 |
| Random shortest-path | single root | 359 | 3.58 | 4,287 |
| Random shortest-path | four roots | 356 | 3.58 | 6,971 |
| Tree metric | all three | 0 | 9.00 | 267,520 |

The complete-graph DP uses 267,520 transitions per family. Every residual optimum equals the original optimum. The incumbent happened to be optimal on this small set; that does not establish broad heuristic quality. No Concorde comparison, held-out benchmark, or decomposition-based TSP implementation was run.

The clustered family shows that dividing the same number of evaluations across roots can weaken elimination substantially. The useful immediate follow-up is adaptive selection of roots and potential budgets, with actual wall-time and held-out instances, after accounting for the obstruction below.

Full per-instance results, bound gaps, certificate paths, and generation details are in [experiment.json](experiment.json).

## 4. An all-size tree-metric obstruction

**Proposition.** Let a weighted tree on all $n\geq3$ tour vertices have nonnegative edge weights totaling $W$, and let $c$ be its shortest-path metric. Every pair of vertices belongs to some optimal tour, and the optimum is $2W$.

For the lower bound, expand each tour edge into its tree path. Every tree-edge cut is crossed at least twice by a tour, so its total expanded cost is at least $2W$.

To construct an optimum containing a prescribed pair $ab$ with $a\ne b$, double every tree edge. Begin at $a$ and traverse the simple tree path to $b$, using one copy of each path edge. The remaining multigraph is connected, because at least one copy of every tree edge remains. Exactly $a,b$ have odd degree, so it has an Euler trail from $b$ back to $a$. Concatenation gives a closed walk of cost $2W$.

Shortcut the initial path directly to the metric edge $ab$. Defer its internal vertices to the remaining trail, which still contains them. Retain one occurrence of every vertex other than $a,b$ along that trail, and close at $a$. Metric shortcutting gives a Hamiltonian tour containing $ab$ of cost at most $2W$. The lower bound forces equality.

Therefore any edge-elimination rule preserving every optimal tour must retain $K_n$ on this family. Its treewidth is $n-1$, although the tree defining the metric has treewidth one and the optimum is easy to construct. A stronger lower bound cannot remove this obstruction. The generating tree and the residual complete metric are different graphs.

This explains the zero-deletion tree rows and rules out a universal low-width guarantee for the all-optima-preserving version of B14 P1. It does not rule out preserving one selected optimum or exploiting the metric's generating structure directly.

## 5. A positive-gap obstruction

Give Petersen-graph edges cost one and all other pairs cost two. Exhaustive enumeration of 181,440 undirected tours gives optimum 11 and 120 optimal tours. Every one of the 45 edges belongs to an optimal tour, with explicit witnesses in [petersen-obstruction.json](petersen-obstruction.json).

Its subtour LP has optimum 10: assign $x_e=2/3$ to the 15 Petersen edges and zero elsewhere. Cubic degrees give degree two; every nontrivial cut has at least three cheap edges, so every subtour cut has value at least two. The objective is 10. Conversely, summing degree constraints gives $\sum_e x_e=10$ and all costs are at least one, so no smaller LP value is possible.

[The independent audit](../COUNT-CHECK-RESULTS.json) verifies all 1,022 proper cuts and all 45 tour witnesses. Thus complete residual density under all-optima preservation can coexist with a strictly positive subtour-LP gap. It is not just a zero-gap tree phenomenon.

## 6. Next direction: choose one optimum explicitly

One route around degeneracy is to preserve a selected optimum. For integer primary costs, rank the $m=\binom n2$ edges from zero to $m-1$, put $B=2^m$, and replace each cost by

$$
c'_e=Bc_e+2^{\operatorname{rank}(e)}.
$$

Every secondary tour sum is below $B$, and distinct edge subsets have distinct sums. Hence the perturbed instance has a unique undirected optimum, which is also primary-optimal. The transformation adds $O(m)$ bits per cost, though numerical magnitudes become large. It generally destroys the triangle inequality; it is an exact-search encoding, not a metric-approximation device.

Uniqueness alone does not guarantee that a 1-tree bound can eliminate every other edge, or that the remaining graph has low width. The next theoretical target is an instance-dependent bound on residual structure after selecting an optimum, or a method operating on the sparse generating graph instead of the complete metric.

## Reproduce

From the repository root:

    python3 solutions/b14-first-round-2026-10-12/elimination/run.py
    python3 solutions/b14-first-round-2026-10-12/local-optima/check_elimination.py

The first command regenerates deterministic certificates and experiment receipts. The second performs the independent small-size exhaustive audit. No package installation or network access is needed.
