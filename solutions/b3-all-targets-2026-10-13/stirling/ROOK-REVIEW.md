# Independent Q183 review

13 October 2026. Accept the all-board rank-at-most-two theorem and five
distinct full-target route failures. The unweighted forbidden-pattern
conjecture remains unresolved. I read the frozen target, root packet/code,
and actual primary [Alexandersson–Jal v3](https://arxiv.org/html/2410.00127v3),
including its non-nesting convention, rook bases and Theorem 4.3.

A source-convention correction is required for K02: in v3, a basis is the
unoccupied rows union occupied columns. The root enumerator uses occupied
rows union unoccupied columns, which are the complementary, dual bases.
This does not invalidate the HPP obstruction. My separate enumeration by
row and column subsets gives 662 source bases, and under the same selected
elements {1,2,3,10,11,12} their polynomial is
1+36t+225t^2+400t^3. Its discriminant is -602100.
The dual polynomial is t^6 f(1/t)=400t^3+225t^4+36t^5+t^6.
Both are nonreal rooted. This direct calculation avoids relying on an
arbitrary specialization being preserved by a matroid isomorphism.
The ordinary rook polynomial remains
1+27t+162t^2+282t^3+162t^4+27t^5+t^6 and is not refuted.

The rank-two theorem is correct for any finite board. Compatible-cell
cliques are exactly non-nesting placements. With no compatible triple,
the graph is triangle free. For every edge its two neighbor sets are
disjoint, so summing d(u)+d(v)<=N gives sum d(v)^2<=Nr_2.
Cauchy then gives r_2<=N^2/4, with the zero-edge case separate.
Hence the quadratic discriminant is nonnegative and every root is
negative; the zero-degree and linear cases are harmless.

The five contracts are distinct:

- K01 constructs an actual avoiding counterexample; the bounded screen
  checked 1,359 such shapes and found none, with no all-size extrapolation.
- K02 asks for uniform multivariate rook-basis stability; the actual
  allowed straight shape defeats it by the exact specialization above.
- K03 asks for a claw-free conflict representation; the three leaves of
  the actual 3x3 claw are mutually compatible, so that hypothesis is false.
- K04 asks for a cell-deletion pencil compatible for every positive cell
  weight; its exact cubic discriminant becomes negative at weight 101.
  Cell weights and matroid element weights are different contracts.
- K05 attempts extremal clique-count degree induction. It proves rank at
  most two, but higher critical-value/Toeplitz obligations remain absent.
  This is distinct from the claw-free hypothesis in K03.

The generic weighted failures do not refute the unweighted catalog target.
The forbidden-pattern test checks exact 3x3 occupancy after row/column
deletion, and every straight shape avoids the pattern for the stated
upper-left/middle-left reason. No source error or rerun is counted.

[check_rook_order_review.py](check_rook_order_review.py) and
[ROOK-ORDER-REVIEW-CHECK.json](ROOK-ORDER-REVIEW-CHECK.json) record my
independent 662-base enumeration, both weighted cubic discriminants,
all three cell-pencil discriminants, and 448 rank-two 3x3 board controls.
The all-size theorem follows from the graph proof, not those finite checks.

