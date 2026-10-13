# Q1366 independent proof, scope and attempt-count review

Reviewed 2026-10-13 by the same retained second agent. **Accept all five
distinct failed full-target routes A1–A5 and the named all-size partial
proofs.** The full unimodality conjecture is unresolved. No sixth route,
global status edit, publication or novelty claim is supplied by this audit.

## Primary target and source qualification

I read the frozen Q1366 entry and the relevant primary passages:
[McNamara–Steingrímsson, Conjecture9.4](https://arxiv.org/html/1305.5569#S9.SS4)
and [Vatter, Conjecture2.2 and layered setup](https://arxiv.org/html/2602.16355v2#S2).
The order is classical subsequence containment, and ranks count distinct
standardized permutations. Occurrences are not separate rank objects.
The consecutive-pattern result does not answer this question. Layered
containment uses generalized subword embeddings, rather than componentwise
comparison of arbitrary unequal-length compositions.

The original paper already reported checking all intervals with top
length<=8. Thus A1's length8 portion is an old-range/literature control,
even though the earlier B3 packet stopped at7. Its66 actual tops of
length9–12 remain genuinely fresh computations for the prescribed
structured and seeded construction. This supports **one** failed valley
construction, not an extra attempt for each family, top, interval, or
verification implementation.

## All-size partials: accepted

### Equal numbers of decreasing layers

Every subpattern of a layered top is layered. A decreasing layer of the
lower pattern must use one upper layer: entries in different upper layers
are increasing, whereas two entries in one lower layer are decreasing.
Conversely separate lower layers cannot occupy one upper layer. This
proves the strictly increasing layer-index embedding criterion.

If both endpoints have L layers, any intermediate has at most L from
the top and at least L from the bottom. Its composition therefore has
exactly L parts; the layer-index embeddings between L-element ordered
sets are identities. The exact interval is consequently

    product_j {b_j,b_j+1,...,a_j},

with relative rank sum_j(c_j−b_j) and the stated product of chain
polynomials. The argument allows arbitrary L and arbitrary positive
endpoint parts, provided the endpoints are comparable. It does not extend
componentwise order to unequal layer counts.

Each chain row is positive and log-concave with interval support.
The Toeplitz TN2/convolution argument is valid: local decreasing ratios
give all cross inequalities, and Cauchy–Binet preserves every order-two
minor of the convolution matrix. For any specified minor, finite support
leaves only finitely many contributing intermediate indices. Zero gap
factors present no difficulty. Thus the all-size log-concavity conclusion
is proved without relying on the bounded controls.

### At most two decreasing layers and a nonempty bottom

Two-layer bottoms are already covered. For a one-layer bottom delta_s,
reverse the **composition**, equivalently reverse-complement the layered
permutation, to assume a<=b. Then s<=b. Every intermediate is either a
single delta_r, s<=r<=b, or exactly one distinct two-part composition
(i,j), 1<=i<=a,1<=j<=b,max(i,j)>=s.

For transparency, define the bounded-positive-pair count

    N_(A,B)(r)=(r−1)_+−(r−A−1)_+−(r−B−1)_++(r−A−B−1)_+.

If s<=a, subtract N_(s−1,s−1)(r) from N_(a,b)(r), and add
1_{r<=b}. On s<=r<=a+b, the first unrestricted final hinge vanishes,
(r−s)_+=r−s, and

    1_{r<=b}−(r−b−1)_+=1−(r−b)_+.

This gives the first displayed formula in LAYERED-INTERVALS.md. If s>a,
only j can reach s. Replacing j by j−s+1 gives
N_(a,b−s+1)(r−s+1), and adding the same indicator yields the second
formula. These derivations also cover s=1, a=b, s=b and single-term
intervals; hinges with a zero bound cancel correctly.

Both formulas are affine minus positive-part hinges. Each hinge is
discretely convex, so the coefficient sequence is discretely concave at
every interior index. It is strictly positive: fix a bottom occurrence
and add upper positions one at a time, obtaining an intermediate at each
length. Arithmetic concavity then implies log-concavity by the stated
arithmetic/geometric-mean inequality. One-layer tops give chains.
This proves the entire advertised nonempty-bottom family. Empty-bottom
intervals are explicitly excluded from this stronger log-concavity
partial, while remaining within the full unresolved unimodality question.

### Unique inversion and exact occurrence fibers

For iota_p direct-sum21 direct-sum iota_q, every pattern above21 must
contain the top's unique inverted pair. Entries before and after that
pair determine unique parameters(u,v); the position of the sole inversion
and the total length distinguish those patterns. Containment is exactly
coordinatewise, giving a product of two chains for all p,q>=0.
The pair is mandatory in every occurrence, and the other positions may
be chosen independently, giving binom(p,u)binom(q,v) occurrences exactly.
At p=q=2, middle-rank weights1,4,1 and the distinct versus occurrence
rows are correct. This is perfect occurrence coverage with unequal
weights; it is not a missing-coverage example.

## Actual Hall deficit and the other witnesses

Literal position-subset enumeration independently reproduces
[213,2574613] with ranks(1,3,7,7,1). Each listed length5 pattern is in
the interval, and its complete length6 cover neighborhood was checked.
The union neighborhood of the five-pattern witness is exactly the four
listed patterns. A separate subset-DP matching implementation finds
maximum matching size6 between the two seven-element ranks.

The proposed adjacent-rank cover-injection certificate requires a
perfect matching whenever two adjacent ranks tie: whichever side of the
chosen peak they occupy, its corresponding injection must be a bijection.
The Hall deficit defeats that certificate. Counts alone still satisfy
unimodality, so it does not defeat Q1366.

For [21,2143], fixing the first inversion misses132. I also checked the
only other inversion occurrence: fixing it misses213. Thus no choice of
one bottom occurrence covers that example's whole interval, independently
of occurrence weights. The stated all-size first-occurrence failure in
a direct sum of k>=2 copies of21 also follows directly: a next-rank
superset of the first inversion is213, while132 can use a later inversion.

For top2413, all four one-entry deletions give distinct nonmonotone
length3 patterns. Every pair of their nonempty principal downsets
intersects in{1,12,21}; its two incomparable maxima preclude a single
interval top. The actual row(1,2,4,1) is unimodal. The formal rows
A=B=(1,3,3,3,1), H=(1,1,3,1,1) and union(1,5,3,5,1) separately
refute the proposed scalar unimodal-gluing lemma. They are not claimed
to be actual permutation intervals or their actual intersections.

## Five-route count disposition

| Route | Accepted full-target attempt and exact blocker |
|---|---|
| A1 | Actual longer interacting-block/random-top valley construction: complete new rank rows produce no valley. The full obstruction or theorem remains missing; old-range reruns and the subsequently proved structured family do not create extra counts. |
| A2 | Uniform adjacent-rank injections along covers: an actual tied-rank Hall deficit blocks the necessary perfect matching. This is stronger than rank unimodality. |
| A3 | Uniform-fiber descent of Boolean counts/chains: under unique occurrence and perfect coverage, same-rank fibers have sizes1,4,1. This defeats the specified common-weight quotient inference, not every possible weighted or unweighted quotient-chain construction. |
| A4 | One fixed occurrence represents every pattern in the interval: coverage fails already in2143, for either occurrence, regardless of fiber weights. This is logically distinct from A3 despite their shared Boolean-subset model. |
| A5 | Induction by deletion-union gluing: actual intersections leave the interval class, and the proposed scalar closure hypothesis is insufficient even in a formal profile relaxation. This concerns overlapping downsets, rather than fixed-occurrence coverage or common weights. |

All five show different attempted mechanisms and substantive worked
outcomes. A3/A4 share an occurrence starting point, and A4/A5 both need
overlap information in potential repairs; these are disclosed connections,
not duplicate sufficient lemmas. None of the witnesses proves that every
repair of the corresponding architecture fails. Under the user's rule,
I accept five consecutive substantive failed full-target attempts and
the stop of Q1366 with the positive family theorems retained.

## Independent checker and receipt

[check_pattern_review.py](check_pattern_review.py) imports neither root
implementation. It uses literal position subsets for the downsets,
pairwise order comparisons for containment, and subset DP for maximum
matching, rather than root's recursive deletion and augmenting paths.
It recomputes every recorded rank coefficient, not merely their shape.

[PATTERN-REVIEW-CHECK.json](PATTERN-REVIEW-CHECK.json) passes1,573 recorded
intervals on80 tops,136,192 top-position subsets,933 literal equal-layer
cases,9,455 hinge/pair-count cases,90 literal two-layer cases,225 individual
unique-inversion fibers, both2143 occurrence failures, and all six pairwise
2413 deletion intersections. The reviewed files are hashed. These bounded
controls support the written all-size proofs and exact method obstructions;
they do not prove the full catalog conjecture.
