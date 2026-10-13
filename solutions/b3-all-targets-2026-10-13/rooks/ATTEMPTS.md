# Q183 non-nesting rook attempts

The frozen target is the unweighted non-nesting rook polynomial on every
skew shape avoiding (3,3,2)/(1) by row and column deletion. These are
attempts on that target, not counterexamples to it.

## Q183-K01: an actual forbidden-pattern counterexample search

Attempt: enumerate exact rook numbers for actual skew shapes, test the
seven-cell forbidden pattern directly, and construct a nonreal-rooted
avoiding instance. The pinned screen generated 1,600 shapes with 3–10 rows
and at most 12 columns. Exactly 1,359 avoided the pattern. Exact integer
coefficients and Arb root enclosures found no candidate; see EXPLORATION.json.
This bounded construction failed to settle the all-size question.

The dynamic program retains the last selected column and rook count.
At each row it either skips the row or selects a strictly smaller column
in its allowed interval. It counts precisely the non-nesting placements.
Direct placement enumeration supplies an independent control at 666333.

## Q183-K02: stability of the uniform rook-basis polynomial

Attempt: prove the multiaffine basis-generating polynomial of every avoiding
rook matroid stable, then specialize row variables to t and column variables
to 1. A direct exact obstruction exists on the allowed straight shape
lambda=(6,6,6,3,3,3), mu=0. The checker enumerates its 662 **dual** bases,
occupied rows union unoccupied
columns. Give variable t to elements {1,2,3,10,11,12} and 1 to the others:

    f(t)=400t^3+225t^4+36t^5+t^6.

Its reduced cubic has discriminant -602100 and exactly one real root.
The source convention is unoccupied rows union occupied columns. For the
same six selected variables, its specialization is
1+36t+225t^2+400t^3, also with discriminant -602100 and only one real root.
Indeed it is t^6 f(1/t). Stability of multiaffine matroid basis polynomials
is invariant under complementation, by variable inversion and a monomial
factor. Thus the dual certificate refutes the proposed HPP proof equally
for the source convention. It does not change the ordinary rook count.
Thus that stronger uniform multivariate stability assertion is false.
The ordinary non-nesting polynomial here is instead

    1+27t+162t^2+282t^3+162t^4+27t^5+t^6.

No nonreal-root assertion is made for this ordinary polynomial. Every
straight shape avoids the forbidden pattern: its absent upper-left cell
and present middle-left cell cannot occur when upper row lengths dominate
lower ones and every row starts in column one.

The source's lattice-path-matroid non-HPP example (Alexandersson–Jal,
[arXiv:2410.00127v3, Theorem 4.3](https://arxiv.org/html/2410.00127v3))
motivated this route check. We independently enumerate the rook bases
and identify the actual substitution on this different labeling. This
does not treat an isomorphism as preserving an arbitrary row/column
specialization. The conflicting older all-HPP claim is not used as a proof.

## Q183-K03: use a claw-free conflict graph

Attempt: represent non-nesting rook placements as independent sets and
apply real rootedness for claw-free graphs. A conflict joins two cells
when they share a row or column, or lie strictly Northwest/Southeast.
The allowed 3-by-3 rectangle already contains an induced claw: center
(1,1) and leaves (1,3),(2,2),(3,1). The center conflicts with each leaf,
and the three leaves form a valid non-nesting placement. Hence the
needed claw-free hypothesis fails on an actual avoiding board. Its
ordinary rook polynomial is 1+9t+9t^2+t^3 and is real rooted; a different
graph transformation might still apply. This particular proof fails.

## Q183-K04: cell deletion with universal positive compatibility

Attempt: prove the exact recurrence M_B=M_(B minus v)+t M_(B excluding
v and its conflicts) by a common-interlacing certificate valid for every
positive weight on v. For the upper-left cell v=(1,1) of the 3-by-3
rectangle, the second polynomial is 1 and the first is

    g(t)=1+8t+9t^2+t^3.

g has discriminant 1489 and three real roots. The original g+t has
discriminant 2160 and three real roots. But giving that cell weight 101
produces g+101t=1+109t+9t^2+t^3, of discriminant -4203040 and only one
real root. Thus the hoped-for universal positive compatibility fails
even when both pieces and the original unweighted polynomial are real
rooted. The polynomial g belongs to the allowed skew shape (3,3,3)/(1).
This is a cell-weight obstruction, different from K02's matroid element
weights. Neither is a counterexample to the unweighted target. A special
argument fixing the cell weight at one is still needed.

## Q183-K05: extremal compatible-clique bounds and degree induction

Attempt: use the compatible-cell graph and extremal clique inequalities to
certify all roots, starting with the first two rook numbers. RANK-TWO.md
gives an all-size proof for every finite board of rook degree at most two.
The exact triangle-free edge inequality supplies the entire quadratic
discriminant. Extending this to higher rook degree fails to close the
target: bounds on edges and clique counts do not determine every higher
critical value or higher Toeplitz minor. No sufficient all-rank inequality
using the forbidden-pattern hypothesis was obtained. This retains a
partial theorem and records one failed full-target degree-induction route.
K03 and K05 both use graphs; K03 needs the conflict graph to be claw free,
whereas K05 uses extremal clique counts in its complementary compatibility
graph, and does not require that claw-free condition.

Five consecutive failed full-target attempts are proposed for independent
review. Source availability errors count zero, and the target remains open.
