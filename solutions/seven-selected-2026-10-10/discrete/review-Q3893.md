# Independent review of Q3893

**Review date:** 2026-10-10. **Outcome:** no blocking mathematical issue found. The argument establishes failure of WLP for the entire stated class, over every field.

Reviewed [3893.md](../algebra/3893.md) and [verify_3893.py](../algebra/verify_3893.py). The supplied exact checker passed. An independent implementation constructs the actual multiplication matrix for the source's eight-vertex example; see [review_algebra_checks.py](review_algebra_checks.py) and its [output](review_algebra_checks.json).

## Primary-source scope

Independently read [Holleben–Nicklasson, arXiv:2502.00155v2](https://arxiv.org/html/2502.00155v2), Conjectures 1.3 and 3.15, the whiskering definition, and Theorem 3.10. The conjecture uses one whisker at every original vertex and squares of all original and whisker variables. The proposed quotient matches those definitions. The final-journal PDF endpoints timed out during this review; the review does not represent an independent rereading of that final PDF.

## Reconstruction of the proof

The shear `x_i -> x_i`, `y_i -> y_i-x_i` preserves every generator of the defining ideal. In particular the square of the new whisker variable is zero because `y_i^2`, `x_i y_i`, and `x_i^2` all vanish. Reversing the sign of the shear provides its inverse, including in characteristic two. Thus the sum of all variables is conjugate to multiplication by `Y=sum y_i`.

Partitioning the surviving monomial basis according to its set `C` of original variables gives a genuine direct sum, indexed by independent sets `C` of the original graph. In the block for `C`, all `y_i` with `i in C` annihilate the block. The remaining whisker variables form a squarefree polynomial algebra on `n-|C|` variables, with a degree shift of `|C|`. Multiplication by `Y` stays in the same block; there is no off-diagonal term that could fill another block's cokernel.

Let `d=ceil(n/2)`. The empty block has larger degree-`d` dimension than degree-`d+1` dimension and therefore a kernel. An independent triple gives a block with smaller degree-`d` dimension than degree-`d+1` dimension and therefore a cokernel. For `n=3,4` the latter dimensions are `0,1`. For `n>=5` the ratio of the larger binomial coefficient to the smaller is `(n-d)/(d-2)>1`. Thus both defects occur in the same total multiplication map. Its rank is strictly below both total dimensions regardless of the shape of the full Hilbert function.

A diagonal automorphism normalizes any linear form whose coefficients are all nonzero to the sum of the variables. Over an algebraic closure this set of forms is a dense open set. Maximal rank in the specified degree would give a nonvanishing maximal minor and hence a nonempty open set intersecting it, a contradiction. Rank of a matrix over the original field is unchanged by field extension. This justifies every coefficient pattern and every field, including finite fields and forms with zero coefficients.

The alternative kernel polynomial is nonzero because one of its surviving all-whisker terms has unit coefficient. Its product with the sum of variables vanishes by square-zero factor identities. The displayed cokernel polynomial is supported only on surviving monomials because its original variables belong to an independent triple. Its derivative cancellation computes a matrix transpose on coordinate bases; it does not require a derivation on the quotient. This distinction is explicitly handled in the solution note.

## Independent direct-matrix calculation

The review implementation imports none of the solution's algebra helpers. It represents a monomial as a word with each position equal to `none`, `x`, or `y`, filters original-original forbidden pairs, and constructs every allowed one-variable extension. For the graph `K_8` with the three edges of one triple removed, the degree-4 and degree-5 spaces have dimensions 400 and 406. Sparse elimination over exact finite fields gives:

| Characteristic | Multiplication rank |
| ---: | ---: |
| 2 | 229 |
| 3 | 328 |
| 101 | 386 |

The characteristic-zero rank is also 386. Reduction modulo 101 gives the lower bound 386; the proof's empty-block kernel has dimension at least `binom(8,4)-binom(8,5)=14`, giving the matching upper bound `400-14=386`. Thus this source example has kernel dimension 14 and cokernel dimension 20 in characteristic zero.

These computations are an independent check of the same-degree rank defect, including small-characteristic behavior. The general conclusion rests on the shear, direct-sum decomposition, dimension inequalities, and coefficient-space argument, not extrapolation from these cases.

## Scope preserved

The proof uses the exact square relations and the complete whiskering hypothesis. It does not extend without argument to arbitrary higher powers or general very-well-covered graphs. The solution states those limits correctly.
