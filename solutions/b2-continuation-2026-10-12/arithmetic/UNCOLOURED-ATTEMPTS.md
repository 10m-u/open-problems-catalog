# Q4295/Q4296: structure in an uncoloured remainder

Read primary source `texts/papers/collections-5b89ab34d74dca89.txt.gz`, Problems 3–4 and the preceding distinction from Roth's fully coloured problem. The target is a sharp function over all admissible N,k or n,k, not simply an algorithm enumerating all finite partitions. R has density at least one tenth and is uncoloured.

## Exact conflict-graph reduction

For a proposed R, form a graph on X\R joining distinct x,y when (x+y)/2∈R. The partition is admissible exactly when this graph has a proper colouring with at most k colours (subject to any explicit nonempty-colour convention). Equal endpoints make no new constraint because x∉R. This produces a correct exact finite algorithm: enumerate R with the required density, solve k-colourability, and minimize its largest progression or affine dimension. It gives no closed sharp asymptotic law; colours are part of the feasibility constraint, not an independent choice.

## Q4296 with one colour is completely determined

If k=1 and A=X\R is nonempty, its midpoint closure implies A is an affine subspace in F₃^n. Translate some a∈A to 0. Closure gives −x∈A from the midpoint of 0,x; applying closure to −x,−y then gives x+y∈A, since division by 2 is multiplication by −1. Hence the translated set is linear.

For any nonempty proper affine A, choose a nonconstant affine linear form constant on A. A different level set is a disjoint affine hyperplane, contained in R. Thus R contains dimension n−1, and it cannot contain dimension n because A≠∅. If A is empty the largest dimension is n. Taking A to be a hyperplane is admissible and attains n−1. Therefore the minimum is **n−1 for every positive n and k=1**. This proves the whole one-colour subcase, not the requested general function.

<a id="q4295-a1"></a>
## Q4295 A1 — Apply density Szemerédi without using the colours

Density |R|≥N/10 implies progressions of every fixed length once N is sufficiently large. It does not determine the minimum longest length as a function of N,k, and uses none of the extra conflict-graph information. The desired sharp value is still absent; a qualitative lower bound is not an exact function. **Failed density-only determination.**

<a id="q4295-a2"></a>
## Q4295 A2 — Make each colour class a full interval

Intervals are midpoint-closed, so removing k intervals of total length≤9N/10 gives admissible examples. The complement has at most k+1 interval components, with a contiguous block of length at least ceil(|R|/(k+1)). This is an upper-construction family with a calculable internal lower bound, not a proof that arbitrary admissible partitions have those components. A minimizer may have highly interlaced colours, and its progressions need not be contiguous. **Failed interval-only extremizer classification.**

<a id="q4295-a3"></a>
## Q4295 A3 — Force individual colour classes to be convex

Even with one colour, the condition requires only *integer* midpoints. The class {1,4} is midpoint-closed inside [4], since the cross-midpoint is 5/2; its remainder {2,3} has density≥1/10 and the class is not an integer interval. For several colours, even an integer midpoint can lie in another colour rather than R. Therefore neither ordinary convexity nor colourwise midpoint closure follows. **Failed convexification proof.**

<a id="q4295-a4"></a>
## Q4295 A4 — Replace the uncoloured question by a cap/progression-free colouring bound

The source's fully coloured version uses a large colour intersection with R to create a progression-free set. Here R∩A_i is empty by definition. The same pigeonhole step has no nonempty intersection, and R itself is unrestricted internally. For example R can be a long interval. Thus the fully coloured Roth bound does not supply the requested longest-progression function under this different setup. **Failed coloured-remainder transfer.**

<a id="q4295-a5"></a>
## Q4295 A5 — Enumerate R independently of its colouring cost

With at least |X\R| available singleton colours any R works, but at small fixed k its conflict graph may need more colours. As a concrete obstruction, R={1,3,5} in [5] leaves vertices {2,4}; their midpoint3 lies in R, so a one-colour assignment is impossible. The density/minimum-progression optimization over arbitrary R therefore does not solve the constrained k problem. The exact graph reduction can enumerate it, but no formula across all parameters is obtained. **Failed colour-free enumeration reduction.**

<a id="q4296-a1"></a>
## Q4296 A1 — Extend the one-colour affine theorem

For k≥2 the midpoint of a same-colour pair may be in a different colour. In F₃, A_1={0,1}, A_2={2}, R=∅ illustrates the local logical failure, though not the density premise. To include that premise, use F₃² with A_1={0,e_1}, place 2e_1 in A_2, and take R to be one point outside this line, assigning the remaining points singleton colours. This is admissible with sufficiently many colours, but A_1 is not affine. The one-colour proof cannot classify all classes for arbitrary k. **Failed colourwise affine extension.**

<a id="q4296-a2"></a>
## Q4296 A2 — Use a cap-set theorem on R

The prohibition concerns pairs outside R, not lines entirely inside R. R may be an affine hyperplane or the full space when empty colours are permitted, containing many affine lines. A cap-set upper bound does not apply to R and gives no forced-subspace minimum. **Failed cap-set substitution.**

<a id="q4296-a3"></a>
## Q4296 A3 — Infer a large affine subspace from density alone

At n=2 a singleton R has density1/9≥1/10 and affine dimension0. Its conflict graph pairs x with 2r−x and is a matching, so two colours suffice. In contrast the one-colour minimum is1. This exact difference already shows the colours affect the answer, and a density-only affine-hyperplane conclusion is false. Quantitative density theorems at large n are weaker than a sharp two-parameter minimum. **Failed density-only sharpness route.**

<a id="q4296-a4"></a>
## Q4296 A4 — Build all minimizers from affine cosets

Partitioning by a linear projection gives convenient admissible examples because a full same-colour coset has midpoints in itself. But admissibility does not require colours to be cosets, as A1 demonstrates, and an arbitrary remainder need not be a union of quotient fibers. The conflict graph retains partial fibers and cross-fiber edges. No transformation is proved to replace them by full fibers while preserving k and decreasing the largest affine subspace. **Failed quotient-fiber extremizer reduction.**

<a id="q4296-a5"></a>
## Q4296 A5 — Tensor a finite optimum at fixed colour count

A product remainder R_0^t has density (|R_0|/|X_0|)^t, below1/10 for all sufficiently large t unless R_0 is full. Product colouring generally multiplies the number of colours as well. Thus repeating a small construction does not preserve either fixed k or the density premise. A tensor claim respecting both would require a different remainder or correlated colouring; none is produced. **Failed naive tensor extension.**

Each all-parameter target stops after five routes. The conflict-graph algorithm and the exact one-colour finite-field theorem are useful restricted results, without asserting a general sharp formula.
