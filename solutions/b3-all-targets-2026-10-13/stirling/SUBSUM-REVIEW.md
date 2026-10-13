# Subsum independent proof and attempt-count review

13 October 2026. I read the exact frozen Q3702/Q3703 statements,
[the full attempt packet](../subsums/ATTEMPTS.md),
[the boundary proof](../subsums/BOUNDARIES.md), its complete checker and
receipt, and the original
[Reciprocals of subsum polynomials](https://link.springer.com/article/10.1007/s11139-026-01419-0),
locally texts/papers/collections-2b52229a115666e0.txt.gz.
The relevant source statements are Proposition 3.8(a), Conjecture 4,
Proposition 4.1 and Conjecture 7. The targets are ordinary
coefficient log-concavity, with Q3702 excluding n=3,5,6,7 and Q3703
quantifying over n>=6. Neither nonreal roots nor failed binomial
normalization contradicts those targets.

## Boundary proofs

The product coefficients c1,c2,c3 are correct. The estimate m3<=L-1
gives exactly the stated positive second-defect lower bound for L>=4.
The first defect and reflected inequalities also pass. This covers
all admissible sizes at those boundary indices; it does not extend
to arbitrary coefficient indices.

The binary-partition split n=m1+2t gives c0=sum b(t) and c1=2 sum t b(t)
without multiplicity factors. For e1<=2N,
binom(e1,2)<=(N-1/2)e1. The step decomposition of the nondecreasing
weights b(t) has base mass 2N and mean of 2t equal to N+1-1/N.
Each additional tail has mean N+j and nonnegative weight. Consequently
u>=N+1/2 and the increasing quadratic at that endpoint is exactly 1/2.
The common-degree palindromicity supplies the final inequality.
The claimed first/last strict inequalities at every n>=4 are proved.

The probability mixture and its variance identity pass: weighting a
partition by 2^(-length(lambda)) gives the summand's correct evaluation
at one after removing a common factor. Every conditional mean is d/2,
so there is no between-component variance term. At n=2^s,
S_n=2n^2-n, sum of squared parts<=n^2 and d=sn.
Since 2^s-1>s for s>=2, the variance exceeds d/4.

The variance ceiling for symmetric ULC distributions needs positive
consecutive support. The revised proof states this requirement.
For a symmetric positive log-concave ratio to the binomial mass,
the ratio is nonincreasing with distance from the center;
its covariance with squared distance is therefore nonpositive.
The partition (n) explicitly contributes full support through degree sn:
the size-one block covers 0..n, and each next denomination is at most
one plus the previous degree. Thus the ceiling applies to the actual
H_(2^s) if it were ULC. The infinite ULC obstruction is valid, while
ordinary LC remains unresolved.

The product CLT also passes. The power-sum double sum has respective
errors O(n), O(n^2); its geometric main sums give degree~2n^2/3 and
variance~2n^3/21. The largest standardized cosine argument tends to
zero, and the fourth-power remainder is O_t(1/n), proving the
stated central normal limit. This weak limit does not provide local
second-difference signs or tail estimates.

## Counts and logical scope

I accept five distinct substantive failed full-target routes for Q3702:
direct actual boundary coefficient ratios; a real-rooted sufficient
class; preservation by the exact n-recursion; a fixed geometric
factorization with TN2 Toeplitz certificates; and transfer from the
proved central normal limit.

A3 and A4 share a gapped-convolution obstruction, which is disclosed.
They are still distinct attempted completions: A3 proposes an invariant
of generated whole rows under the actual size increment, while A4
proposes a certificate for individual factors in a different exact
regrouping. The two encodings and their missing obligations differ.
Neither generic control is presented as an actual product row.
The auxiliary binomial perturbation in A5 is positive and fails LC at
its center; its total variation tends to zero, so it correctly shows
that the limiting-law statement alone cannot force LC.

I also accept five distinct routes for Q3703:
actual low-coefficient ratio control; real-rootedness; termwise LC
and synchronized summation; an exact mean/variance certificate;
and Lorentzian/ULC homogenization. A4 asks whether preserved global
moments plus boundary data imply local LC; its positive symmetric
same-moment perturbation disproves that sufficient inference.
A5 instead imposes a stronger structural normalization and refutes
it on infinitely many actual sizes. These are separate obligations,
not two counts for the same numerical failure. A3's actual all-ones
partition summand has positive coefficients at 0 and 2 and zero at 1,
so its termwise premise fails directly.

The source already states the cyclotomic facts used in A2; rereading
those facts is not counted as a new attempt. The counted attempts are
the explicit stronger-class proof routes and their precise obstructions.
Both complete targets therefore stop unresolved at five failed routes.
The boundary theorems, exact mixture identity and CLT remain useful
partial results, and no failure is an LC counterexample.

[check_subsum_review.py](check_subsum_review.py) uses descending-denomination
partition recursion and independent exact expansions.
[SUBSUM-REVIEW-CHECK.json](SUBSUM-REVIEW-CHECK.json) records 16 product
expansions, 15 literal binary-partition sums, 32 recurrence/regrouping
controls, powers-of-two full-support/moment controls and the generic
counterexamples. The all-size conclusions rest on the proofs above.
This is internal mathematical review, with no novelty or external
peer-review claim.

