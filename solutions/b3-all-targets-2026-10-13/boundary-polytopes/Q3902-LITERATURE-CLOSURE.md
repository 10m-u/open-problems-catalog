# Q3902 is false: an audited literature counterexample

2026-10-13. Attributed literature closure accepted by root source and exact-certificate review.
No local novelty claim. The universal assertion is refuted by an actual
**homology** polytope of a graph. This does not settle the standalone
cohomology assertion or the separate subcomplex-reflexivity Question 9.3.

The frozen target `ede55ed8ecc1ee3fb171` agrees with [Donzelmann--Holleben--Juhnke,
Question 9.4](https://arxiv.org/html/2602.17253v1): every reflexive symmetric
(co)homology polytope should have a nonnegative gamma vector. The combined
frozen location metadata also mentions Question 9.3; that is a different
question and is not being closed here.

[Luis Ferroni, *Symmetric edge polytopes are not gamma-positive*,
arXiv:2607.02424v1](https://arxiv.org/html/2607.02424v1), submitted 2 July
2026, supplies the graph construction and its polynomial formula in
Proposition 2.1, with the explicit counterexample in Corollary 2.2.
This is a later primary preprint, not an external peer-review claim.
The proof was read in full in both HTML and PDF. Its use of planar dual
arborescences and the away-edge statistic agrees with [Kálmán--Tóthmérész,
Example 1.1 and Theorem 1.2](https://arxiv.org/html/2203.17127v4).
Ferroni's theorem-number reference is 1.1; the available v4 labels the
away-edge theorem 1.2. The mathematical statement, not that numbering,
was checked.

## Direct transfer to the exact lattice and target

Take two endpoints s,t and five internally disjoint paths between them,
each containing eight edges. This is a finite simple connected graph G,
with 37 vertices and 40 edges. Regard its edges as the facets of a
one-dimensional simplicial complex Delta. Its top boundary has columns
`e_v-e_u`, up to independently chosen orientation. Therefore

    P_Delta=conv{±(e_v-e_u):uv in E(G)}.

Its real span is the sum-zero hyperplane and has dimension 36. Its exact
target lattice is

    L={x in Z^37: sum x_i=0}.

A spanning tree's incidence columns form an integral basis of L:
delete one vertex coordinate and use successive leaf elimination to
obtain determinant ±1. Thus there is no finite-index vertex-lattice
versus ambient-lattice change in this example.

Here is also a direct reflexivity argument. A functional on L can be
represented uniquely by vertex potentials with one specified potential
zero. The polar is defined by `|y_u-y_v|<=1` along every graph edge.
At a polar vertex, the tight edges contain a spanning tree. Otherwise,
a component's potentials can be varied together, leaving tight edges
fixed and preserving all strict constraints for a sufficiently small
variation, contradicting that it is a vertex. Along a tight spanning
tree all potential differences are ±1. Starting at the zero potential
proves every potential integral. Every polar vertex consequently lies
in L*, so P_Delta is reflexive in precisely the frozen target's lattice.

## Independent exact numerator audit

For a length-k sign word w and a marked deleted edge q, define

    alpha(w,q)=number of plus signs before q
                 + number of minus signs after q.

Let B_(k,i,+) and B_(k,i,-) enumerate these marked words by `t^alpha`,
with i plus signs and prescribed sign at the deleted edge. The checker
computes these directly over all `2^k` words. It separately checks the
binomial coefficient enumeration of the same objects: if r plus signs
and j minus signs precede a deleted plus edge, the number of choices is
`binom(r+j,r)binom(k-1-r-j,i-1-r)` and alpha=`k-i+r-j`.

In a facet of this graph every edge is tight. Indeed the graph is
bipartite; a connected tight-edge spanning subgraph fixes parity on its
two classes, and every other edge has an odd potential difference of
absolute value at most one. The path signs have a common plus count i,
since every path has the same endpoint potential difference.

For a planar dual rooted at the outer face, deleting the dual bundle of
the unique whole primal path leaves a dual path. Its arborescence edges
have one prescribed sign on one side of the whole path and the opposite
sign on the other side. The whole path contributes `binom(k,i)t^i`;
the two blocks of broken paths contribute the independent marked-word
polynomials. The audited published dissection theorem identifies the
sum with the Ehrhart numerator. This is an exact identification using
a primary theorem, not an extrapolation from the smaller controls.

For k=8 and five paths, [the executable certificate](FERRONI-CHECK.json)
records the complete degree-36 numerator. Literal marked-word counting
agrees with the primary coefficient formula and every displayed
coefficient. Two different exact triangular gamma inversions agree;
the resulting coefficients are

    1,8,48,256,1280,6144,28672,131072,461136,1373568,
    3438592,8290304,16487040,37120000,63755264,77045760,
    -9799680,0,0.

In particular gamma_16 is negative. Re-expansion in
`t^i(1+t)^(36-2i)` reproduces the entire numerator with zero residual.
This refutes the universal full Q3902 assertion through its homology
branch.

The [independent checker](check_ferroni.py) verifies 18,432 literal
marked-word objects, builds the actual graph and a lattice-basis tree,
and checks eight smaller graphs by exact lattice-point sumsets and
Ehrhart inversion, independently of the sign-word formula. The latter
are exact Ehrhart counts: integral minimum-cost flow realizes every
integer sum-zero vector of minimum edge l1 cost at most k as a sum of
at most k signed edge columns, so integer points in kP are exactly the
computed sumsets. The large result relies on the audited dissection
identity; it does not claim a direct 36-dimensional point enumeration.

## Stopping and retained evidence

Root review accepted this literature closure; no further solving attempts
are needed. The earlier [A1 forest-assembly failure](Q3902-ATTEMPTS.md#q3902-a1)
and [all-size even-code crosspolytope formula](CROSSPOLYTOPES.md) remain
valid and preserved. The lookup itself counts zero as a failed
mathematical attempt. The closure credits Ferroni's published preprint
construction and formula, with local exact source and arithmetic audit.
