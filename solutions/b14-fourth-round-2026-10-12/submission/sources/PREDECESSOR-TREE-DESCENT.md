# B14 Q3817/P3 — Exact path guarantees and bounded 2-opt descent on trees

**Scope:** internally reviewed programme-local proofs on named families, 2026-10-12. The main thread independently checked the path/star guarantees, tree-cut quartet argument, move-count bound and exact $97/96$ integral. Q3817 asks about all sparse generating graphs and remains unresolved by this note. No originality or external peer-review claim is made.

There are three useful baseline results. On every positively weighted path, nearest neighbor from any start has approximation ratio at most $3/2$, and the constant is tight even with strict nearest choices. Every tour in a star metric is optimal. On every positively weighted tree metric, every strict 2-opt pivot rule reaches an exact optimum in $O(n^2)$ moves, from any initialization. Independent exponential weights inherit these deterministic statements; no exchange of expectations is needed for the guarantees.

## Model and source boundary

The cities are **all vertices** of a connected generating tree $T$, with positive weights $w_e$. Complete-graph distances are lengths of unique tree paths. Write $W=\sum_{e\in T}w_e$. A tour visits every city exactly once and closes at its start. Nearest neighbor always chooses a closest unvisited city. The path bound permits any tie rule. For the expectation identity below, use a fixed scale-invariant tie rule; ties have probability zero for independent exponential weights.

Klootwijk and Manthey's Algorithmica 2023 paper proves a constant expected nearest-neighbor ratio under fast-growing-cut assumptions (§4.2), and asks in §6 whether the greedy-like results extend to arbitrary sparse graphs. The same section asks about initialization followed by local search. Its general sparse-graph 2-opt quality theorem does not give the descent bound below. [Original paper](https://doi.org/10.1007/s00453-023-01167-3), [authors' publication record](https://research.utwente.nl/en/publications/probabilistic-analysis-of-optimization-problems-on-sparse-random--2/)

The retained local source is PDF, with text. Q3817 has stable ID `5be5b12412c27b8f10e5`.

Long path families fail the fast-growing-cut hypothesis: a prefix with unbounded size and size at most a fixed fraction of $n$ has just one boundary edge. The path theorem therefore supplies a restricted case outside that hypothesis. Stars are included as exact controls; no assertion that stars fail the hypothesis is needed.

## 1. Cut accounting on a tree

Removing tree edge $e$ partitions the cities into nonempty sets $A_e,B_e$. For a tour $H$, let $C_e(H)$ be its number of crossings of that partition. Expanding each metric edge into its tree path gives

$$
\operatorname{cost}(H)=\sum_{e\in T}w_e C_e(H).
\tag{1}
$$

Every $C_e$ is even and at least two. Doubling the tree and shortcutting an Euler tour gives an upper bound $2W$, so

$$
OPT=2W.
\tag{2}
$$

This uses a tree on the entire city set. Unused Steiner branches require a different statement.

## 2. Nearest neighbor on a path has tight ratio $3/2$

Order the cities along the path at coordinates $z_0<\cdots<z_{n-1}$. The visited set of nearest neighbor is an interval of city indices, and its current vertex is an endpoint of that interval. Indeed, among unvisited vertices on either side the nearest one is the next endpoint extension; the algorithm chooses one of those two.

Let a **switch** mean extending from the current endpoint to the opposite endpoint's next unvisited city. Before switch $k$, write $R_k$ for the visited interval's length, $g_k$ for the new edge crossed at the opposite frontier, and $R'_k=R_k+g_k$ for the enlarged interval's length. Such a move costs $R_k+g_k$, rather than just the extension length $g_k$.

For every switch except the last, the current-side frontier edge $f_k$ exists. If it did not exist, the algorithm would have reached a global path endpoint, and after switching would have unvisited cities only on the other side and could never switch again. Nearest neighbor's choice gives

$$
f_k\geq R_k+g_k=R'_k.
$$

Until the next switch, the algorithm extends only the other side; thus $f_k$ remains exactly the edge crossed at that next switch, so $g_{k+1}=f_k\geq R'_k$. For $K\geq1$ switches, their total excess crossing distance satisfies

$$
\sum_{k=1}^K R_k
=\sum_{k=1}^K(R'_k-g_k)
\leq R'_K-g_1\leq W.
\tag{3}
$$

Without switches the sum is zero. All interval extensions together have total length $W$. Therefore the open nearest-neighbor route has length $W+\sum R_k\leq2W$. Its return from the last endpoint to its start costs at most $W$. Using (2),

$$
NN_v\leq3W=\tfrac32 OPT.
\tag{4}
$$

Ties only replace strict comparisons by non-strict ones in (3). In particular, for independent $\operatorname{Exp}(1)$ path-edge weights,

$$
\mathbb E[NN_v/OPT]\leq3/2
$$

uniformly over $n$ and the start. An endpoint start is monotone and has ratio exactly one.

**Tight family with no tie dependence.** For integer $k\geq2$ and fixed $\epsilon>0$, take a path with $k+2$ cities and successive edge weights

$$
k+2\epsilon,\quad
\underbrace{1,\ldots,1}_{k-1\text{ edges}},\quad
1+\epsilon.
$$

Start at the penultimate city, index $k$. Its strict nearest choices visit $k,k-1,\ldots,1,k+1,0$ in that order. Here $W=2k+3\epsilon$, and direct addition gives

$$
NN=2W+2(k-1),\qquad
\frac{NN}{OPT}=1+\frac{k-1}{2k+3\epsilon}\longrightarrow\frac32.
\tag{5}
$$

This is a deterministic worst-case construction. It is not an exponential-weight counterexample to a smaller expected constant.

## 3. Stars are exact controls

In a star metric, each leaf's spoke belongs to both metric tour edges incident to that leaf and to no other tour edge. Thus every spoke is used exactly twice in every tour, which costs $2W$. Nearest neighbor is optimal from every start, and no strictly improving 2-opt move exists. The expected ratio under exponential weights is exactly one.

## 4. Every strict 2-opt move on a tree lowers an integer potential

Consider a valid exchange removing directed tour edges $a\to b$ and $c\to d$, and adding undirected edges $ac,bd$. These four endpoints are distinct; segment reversal gives a single tour.

For a generating-tree cut, the difference in its crossing multiplicity is determined solely by these endpoints. A $0$–$4$ split contributes zero to both pairings, and a $1$–$3$ split contributes one to both. Only a $2$–$2$ split can change the count. Among four fixed terminals, tree cuts cannot realize two different $2$–$2$ partitions: different pair partitions would cross, whereas partitions induced by edges of a tree are compatible. This also follows by restricting the tree to the minimal subtree connecting the four terminals.

If such cuts exist, they all specify the same pair partition. The pairing inside its two sides has crossing count zero on those cuts; the other two pairings both have count two. Hence the two other pairings have equal cost, and any **strictly improving** exchange replaces one of them by the inside-side pairing. Therefore

$$
C_e(H')\leq C_e(H)\quad\text{for every }e\in T,
\qquad
\Phi(H')\leq\Phi(H)-2,
\tag{6}
$$

where $\Phi(H)=\sum_e C_e(H)$ is an unweighted integer potential. At least one cut changes, since the move strictly decreases the positive-weight cost (1). This is stronger than an objective decrease bounded below by a possibly tiny edge weight.

Conversely, if some $C_e(H)\geq4$, the oriented tour has at least two $A_e\to B_e$ crossings. Select two of them, $a\to b$ and $c\to d$. They have distinct endpoints and are nonadjacent tour edges; replacing them by $ac,bd$ is a valid 2-opt move. The tree cut has the split $\{a,c\}\mid\{b,d\}$, so the quartet argument above proves a saving at least $2w_e>0$. Every nonoptimal tour therefore has a strictly improving move.

**Theorem.** From any initial tour, every rule that repeatedly chooses a strictly improving 2-opt exchange until none remains ends at an exact optimum of cost $2W$. Its move count is at most

$$
\frac{\Phi(H_0)-2(n-1)}2
\leq\sum_{e\in T}\bigl[\min(|A_e|,|B_e|)-1\bigr]
\leq(n-1)(\lfloor n/2\rfloor-1).
\tag{7}
$$

The second inequality uses $C_e(H)\leq2\min(|A_e|,|B_e|)$. No randomness, lower bound on the smallest positive weight, or restriction on initialization is required. Best improvement, first improvement with any fixed scan order, and other strict-improvement rules are covered.

Given the complete distance matrix, checking $O(n^2)$ moves per pivot gives an $O(n^4)$ arithmetic/comparison bound for ordinary full-scan implementations. This is a bound on real-number operations and distance evaluations, not a claim about finite-bit encoding of exponentially distributed real inputs.

Thus P3 has an exact named-family baseline: nearest neighbor followed by any exhaustive strict 2-opt rule on independent-exponential tree metrics reaches optimum in a deterministic quadratic number of moves. A slow-descent obstruction for Q3817/P3 must use a graph with cycles, a different neighborhood, or an additional implementation restriction.

## 5. An exact exponential normalization identity on trees

Let the $m=n-1$ tree-edge weights be independent $\operatorname{Exp}(1)$. Put $S=\sum_e w_e$ and $P_e=w_e/S$. The change of variables $w=sP$ has Jacobian $s^{m-1}$. Its density factors into a Gamma$(m,1)$ density in $s$ and the uniform Dirichlet$(1,\ldots,1)$ density $(m-1)!$ on the simplex in $P$. Thus $S$ and $P$ are independent.

Nearest-neighbor choices depend only on $P$, and its tour cost scales by $s$. Since $OPT=2S$, the ratio $R=NN/OPT$ depends only on $P$, so is independent of $S$. Consequently, **for this tree model**,

$$
\mathbb E[NN/OPT]
=\frac{\mathbb E[NN]}{\mathbb E[OPT]}
=\frac{\mathbb E[NN]}{2(n-1)}.
\tag{8}
$$

This equality is a proved special identity; it is not a general replacement rule for expected ratios. In particular, the normalized optimum need not be constant for a generating graph with cycles. The cut identity is

$$
R(P)=\frac12\sum_e P_e C_e(H(P));
$$

the chosen tour and its multiplicities depend on $P$, so one must not independently average those factors.

**Exact four-city example.** For path weights $a,b,c$ and start at its first interior city, nearest neighbor has excess cost $2b$ precisely when $b<a$ and $c>a+b$. Otherwise it is optimal. Normalize $a+b+c=1$. The uniform simplex density is two, and the bad region is $0<b<1/4$, $b<a<1/2-b$. Therefore

$$
\mathbb E[NN/OPT]
=1+2\int_0^{1/4}b(1/2-2b)\,db
=\frac{97}{96}.
\tag{9}
$$

The second interior start has the same expectation by reversal, and endpoint starts have expectation one. As a separate check, integrating the unnormalized excess against the three independent exponential densities gives

$$
\mathbb E[NN-OPT]
=2\int_0^\infty\int_b^\infty b e^{-2a-2b}\,da\,db
=\frac1{16},
$$

so $\mathbb E[NN]=6+1/16=97/16$, consistent with (8)–(9).

## Verification and remaining scope

check.py independently builds tree distances and cut vectors. It checks the path switch accounting and bound for every start on an exhaustive bounded positive-integer path set, the strict-choice family, arbitrary star tours, all 2-opt moves on a bounded collection of labeled trees and tours, and actual best/first-improvement descents. It also checks the exact rational integration in (9). Its receipt is CHECK-RESULTS.json.

Run `python3 solutions/b14-second-round-2026-10-12/initialization/check.py`. No Monte Carlo or rare-event estimation is used.

Q3817 remains open beyond the named path/star cases. In particular, this note does not bound the expected nearest-neighbor ratio on arbitrary trees. The tree descent theorem controls the hybrid's final cost and move count, while the initializer's ratio is a separate question. The useful next transfer target is a generating graph with a small number of cycles: determine whether its quartet failures admit a substitute integer potential, or produce an explicit move that increases some generating-edge multiplicity.
