# B14 P3: blockwise noncancellation and deterministic quadratic 2-opt descent

Date: 2026-10-12. New derivation in this continuation. Review status: written proof and independently implemented finite checks; not externally peer-reviewed or formally verified. Literature priority has not been established.

## 1. Statement

Let G be a connected graph on n >= 3 vertices with arbitrary positive real edge lengths. All its vertices are cities, and the TSP costs are their shortest-path distances d. Include each bridge as a block of size two. Let B range over the biconnected blocks, s_B = |V(B)|, and put

\[
D_B=\binom{s_B}{2},\qquad M_B=D_B 2^{D_B-1}.
\]

**Theorem.** Every sequence of strictly improving, cycle-preserving 2-opt moves, from every initial Hamiltonian tour and under every pivot rule, has length at most

\[
N\le n\sum_B M_B.
\]

In particular, if s_B <= b for every block, then

\[
\boxed{N\le n(n-1)b\,2^{\binom b2-2}.}
\]

For b = 4 this is 64n(n-1). The bound is deterministic and independent of the magnitudes of the generating edge lengths and the smallest positive improvement. For fixed b, scanning the complete 2-opt neighborhood after each move takes O_b(n^4) arithmetic/comparison operations, in addition to constructing the distance matrix. This is not a unit-cost bit-complexity assertion for arbitrary real inputs.

The theorem concerns reaching a local optimum, not proving that it is globally optimal. It holds for every positive realization in the exponential-weight model on this restricted graph class, but does not cover arbitrary sparse graphs, bounded-treewidth graphs with unbounded blocks, or neutral moves.

## 2. Block metric decomposition

Use the block-cut tree, with block nodes adjacent to the articulation vertices they contain. A nonarticulation city can be represented by a leaf attached to its block. For a fixed block B, define p_B(v) as follows: it is v when v belongs to B; otherwise it is the unique articulation of B reached from v along the block-cut tree. Equivalently, delete the internal edges of B. Each resulting connected component contains exactly one vertex of B, and p_B maps that component to this vertex.

Let d_B be the shortest-path metric restricted to edges of B. A shortest path cannot profit by leaving B and returning to it: any such excursion returns through the same articulation, and positive length makes the excursion unnecessary. The unique block-cut route therefore gives

\[
d(u,v)=\sum_B d_B(p_B(u),p_B(v)).\tag{1}
\]

For a Hamiltonian tour T, define its contribution in B by

\[
C_B(T)=\sum_{uv\in T}d_B(p_B(u),p_B(v)).\tag{2}
\]

Repeated projected cities and zero projected edges are allowed. Equation (1) gives c(T) = sum_B C_B(T).

## 3. The noncancellation lemma

For four distinct cities a,b,c,d, consider their three unordered pairings:

\[
P_1=ab\mid cd,\quad P_2=ac\mid bd,\quad P_3=ad\mid bc.
\]

Let F_B(P) be the sum of the two projected distances in pairing P. We claim that, for any two pairings P,Q, the nonzero numbers

\[
F_B(P)-F_B(Q)\tag{3}
\]

all have the same sign. In particular, a 2-opt improvement cannot decrease one block's contribution at the cost of increasing another's.

### 3.1 A block with four distinct projections

Suppose a block B sees the four cities at four distinct vertices of B. They are then in four distinct fibers of p_B. Any different block B' lies in one of those fibers or a fiber containing none of the cities. At most one of the four cities can project in B' differently from the other three. For a 3+1 partition, every pairing has exactly one distance between the two projected points; for a 4 partition, every pairing has value zero. Hence F_B'(P) is constant in P for every B' != B.

There can therefore be at most one contributing block in this case, and cancellation is impossible.

### 3.2 No block has four distinct projections

Consider the possible multiplicities of projected labels in a block.

If all four coincide, or if the multiplicities are 3+1, the three pairing sums are equal.

For multiplicities 2+2, the pairing that joins the two equal-label pairs has value zero; the other pairings both have value 2d_B(x,y).

For multiplicities 2+1+1, write z for the duplicated label and x,y for the other labels. The pairing joining the duplicated pair has value d_B(x,y). The other two have equal value d_B(x,z)+d_B(z,y), which is at least d_B(x,y) by the triangle inequality.

Thus each nonconstant block has exactly one preferred pairing with a smaller value, while the other two values agree. This preferred pairing defines a 2-versus-2 split of the four original cities.

That split is witnessed by an edge cut of the block-cut tree. In the 2+1+1 case, cut the branch containing the two cities with the duplicated projection. In the 2+2 case, either of the two terminal-containing fiber branches gives the split. The relevant projection has a fiber containing two distinct cities, so it is an articulation branch rather than an isolated nonarticulation leaf.

Two distinct 2-versus-2 splits on the same four terminals cross: all four intersections of their sides are nonempty. Edge cuts of a tree cannot cross in this way. To see this directly, delete one of the two tree edges. The other edge lies in one resulting component, so one side of its split is wholly contained in that component. Consequently all the nonconstant blocks have the same preferred pairing.

It follows that (3) cannot have opposite signs in different blocks. This proves the lemma.

### 3.3 Consequences for 2-opt

A cycle-preserving 2-opt move replaces one of the three pairings by another. Its gain is the sum of (3). If the gain is strictly positive, every summand is nonnegative and at least one is positive. If the gain is zero, all summands are zero. This conclusion depends only on the block tree and the metric triangle inequalities; no distributional assumption appears.

## 4. An explicit small-integer metric preserving every local gain sign

The following finite-dimensional lemma supplies a bounded integer potential. Integer objective compression is an established general technique; Frank and Tardos (1987) is relevant background. The elementary lemma here preserves a particular family of four-label comparisons, with an explicit determinant bound, and is proved directly.

**Lemma.** Let w be any positive metric on s >= 2 labels, with D = binom(s,2). There is a positive integer metric q on the same labels such that

\[
1\le q_{uv}\le D2^{D-1}\quad(u\ne v),\tag{4}
\]

and for every ordered quadruple a,b,c,d, including repeated labels,

\[
\operatorname{sgn}(w_{ab}+w_{cd}-w_{ac}-w_{bd})
=
\operatorname{sgn}(q_{ab}+q_{cd}-q_{ac}-q_{bd}).\tag{5}
\]

Diagonals are zero. In particular, both strict comparisons and equalities are preserved.

**Proof.** Regard the upper-triangular distances as a vector w in R^D. Every four-label comparison is r dot w, where r is an integral vector and ||r||_2 <= 2. For four distinct labels, the vector has four coordinates equal to +1 or -1. For three distinct labels, a nonzero row is a triangle row, with three coordinates of magnitude one, or a shorter row. With two labels, it is a signed twice-unit row or zero. These exhaust the repetition patterns.

For every nonzero comparison, orient its row so r dot w > 0 and impose r dot z >= 1. For a comparison equal to zero impose r dot z = 0. Also impose z_e >= 1 for every coordinate. This finite system is feasible: a sufficiently large positive scalar multiple of w meets all strict rows with right-hand side one and preserves every zero row.

Minimize sum_e z_e. A sublevel set containing a feasible point is compact because every coordinate is at least one. An optimum therefore exists, and an optimum extreme point can be selected. At that point, D linearly independent active integral rows give Az = h, with each h_i in {0,1} and each row of A having Euclidean norm at most two. Include the active equality rows as needed; the argument also covers a lower-dimensional feasible polyhedron.

Let delta = |det A|, a positive integer, and set q = delta z. Cramer's rule makes q integral. Each coordinate is positive. Expanding the determinant with its column replaced by h gives at most D cofactors, each of absolute value at most 2^(D-1) by Hadamard's inequality. Therefore q_e <= D2^(D-1). Scaling preserves all the signs and zero values, proving (4)-(5).

Finally, the repeated-label comparisons include

\[
w_{ab}+w_{bc}-w_{ac}\ge0
\]

(take the second and third projected positions equal). Their signs are preserved, so q satisfies every triangle inequality. Thus q is a metric. QED.

The proof establishes existence for positive real metrics. For rational input, one can compute a rational vertex of the displayed finite LP exactly, then apply the determinant scaling. The implemented checker uses a numerical LP only to propose a basis; it reconstructs the basis solution exactly and checks every comparison and triangle inequality with integer arithmetic. No numerical optimization status is accepted as a certificate.

## 5. Gluing the integer metrics

For each block choose q_B from the lemma and define

\[
d'(u,v)=\sum_B q_B(p_B(u),p_B(v)).\tag{6}
\]

The sum is an integer metric. Each term is a pseudometric on the original city set, and at least one term distinguishes any two distinct cities. Equivalently, complete each block with its q_B distances and glue these completed blocks along the original articulation tree. It is not necessary that d' be generated using only the original edges of G.

Every local gain in block B has the same sign under d_B and q_B, including zero. The blockwise noncancellation lemma applies to both decompositions. Consequently the global sign of every 2-opt gain is identical under d and d'. A zero global gain also stays zero.

This is preservation of the local improvement digraph, not preservation of numerical gain magnitudes, the ranking of all tours, or global optima. A fixed-scan first-improvement rule takes the same trajectory under both metrics, but best-improvement need not choose the same move because gain sizes may change. Regardless, every move chosen by any strictly improving rule under d decreases the d' tour cost.

Define

\[
\Phi(T)=\sum_{uv\in T}d'(u,v).
\]

It is a nonnegative integer. Each improving move decreases it by at least one. Every tour has n edges and every block contributes at most M_B to each edge, so Phi(T) <= n sum_B M_B. This proves the first bound.

For the second bound, the block-cut decomposition of a connected graph gives

\[
\sum_B(s_B-1)=n-1.
\]

For s >= 2,

\[
\frac{\binom s2 2^{\binom s2-1}}{s-1}
=s2^{\binom s2-2}
\]

is increasing in s. Therefore sum_B M_B <= (n-1)b2^(binom(b,2)-2), completing the proof.

## 6. Checked scope boundary: failure for 3-opt

Even on a tree, an improving 3-opt move can worsen one block while improving another. Take the six-vertex path 0-1-2-3-4-5 with generating lengths (1,1,10,1,1). The old tour

\[
(0,1,3,2,4,5)
\]

has cost 48. Replace edges {1,3},{2,3},{4,5} by {1,2},{3,4},{3,5}. This gives the tour

\[
(0,1,2,4,3,5)
\]

of cost 30. The crossing counts of the five generating cuts change from

\[
(2,2,4,2,2)\quad\text{to}\quad(2,2,2,4,2).
\]

The heavy third cut improves while the fourth cut worsens. The theorem must therefore not be transferred to arbitrary 3-opt or Lin-Kernighan moves using the noncancellation argument.

## 7. Evidence and relation to the handoff

The new checker generates 160 trees of blocks of sizes 2 through 5, with integer lengths ranging from small values to values multiplied by powers of ten up to 10^30. It checks 16,491 distance entries against an independent shortest-path implementation, and 183,858 quartet comparisons; 34,424 comparisons involve multiple nonzero block gains. All pass noncancellation.

On 32 of these graphs, and two additional individual blocks, 112 exact integer surrogates are constructed. All 5,076 distinct nonzero local gain rows in these certificates are checked exactly. The checker verifies 28,188 global gain signs, 96 pairs of identical first-improvement trajectories, and 780 actual strictly improving moves. The certificates and integer metrics are retained. A separate standard-library checker rechecks the saved metrics without importing the construction code or using an LP solver.

These finite checks exercise the identities and implementation. They are not a proof by finite extrapolation; Sections 2-5 are the all-size argument.

The supplied handoff already contains tree-cut monotonicity and tree-metric descent bounds, as well as probabilistic results for other generating graphs. This continuation adds the blockwise noncancellation lemma, the glued gain-sign-equivalent integer metric, and a weight-independent deterministic quadratic move bound for fixed maximum block size. It does not reattribute the tree result as new.

Related external background: Frank and Tardos, “An application of simultaneous diophantine approximation in combinatorial optimization,” Combinatorica 7 (1987), 49-65, DOI 10.1007/BF02579200; Klootwijk, Manthey and Visser, “Probabilistic Analysis of Optimization Problems on Generalized Random Shortest Path Metrics,” arXiv:1810.11232, revised 2020. The latter studies expected 2-opt iterations in random shortest-path settings; it is not being cited as the present deterministic bounded-block theorem. Targeted searches did not establish priority for the specific theorem proved here.
