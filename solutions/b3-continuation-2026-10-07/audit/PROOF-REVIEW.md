# Review of the reconstructed B3 continuation

7 October 2026. Three research agents worked independently on interval
constraints, Stirling minors, and interpolation; the coordinating agent
reconstructed the s-Eulerian arguments. The interval agent then independently
reviewed those Eulerian arguments. This is mathematical reading and exact
computer-assisted checking, with no publication-priority or proof-assistant
claim.

The nine scopes in [RESULTS.json](../RESULTS.json) pass this review. They are
auxiliary theorems within the original questions, rather than new resolutions
of entire catalog targets.

## Interval constraints

The prefix-height floor argument preserves all integer difference bounds,
including adjacent increments zero or one. It proves consecutive support.
After coordinate conditioning, the remaining intersection of each original
interval is still an interval in the retained order. For a word and its
complement, each bound reduces exactly to
`|2 sum_I x_i-|I|| <= min(2U'-|I|, |I|-2L')`.

Antipodal products of positive position weights are constant. Dividing the
two rank counts by their binomial factors gives precisely
`q*c_q >= (q+1)*c_(q-1)`, without a squared normalization. Nonnegative weights
follow by continuity; support for zero weights follows by fixing those
coordinates to zero. The empty case is harmless.

The exhaustive finite calculation is complete: every symmetric interval band
has one of the enumerated parity-compatible bandwidths, is vacuous, or makes
the family empty. Every family is an intersection of these predicates.
The parent checker uses breadth-first intersection closure, independently of
the research lane's generator-by-generator dynamic program. Both produce the
same complete sets, hashes, and equality counts in dimensions 2,4,6,8. An
alternating word satisfies every nonempty minimal band, so the ordinary
intersections here are nonempty; explicitly impossible bounds are handled
separately.

The parent read [Kahn–Neiman](https://arxiv.org/pdf/0907.0243), Theorems 1,4,9,
including their conditioning and support assumptions. Theorem 9 proves the
inequalities at indices 1 through 4 and m−4 through m−1, which correspond to
six-term normalized rank segments at the ends. This establishes the claimed
all-weight, at-most-nine-variable consequence. Projection and circular
intervals have not been substituted for conditioning and linear intervals.
The laminar argument correctly sums child-block orders under convolution and
truncates only consecutive rank intervals.

## Stirling minors

The recurrence and independent labelled-assembly formula agree on the saved
finite controls. The parent independently expanded the first principal
determinant with symbolic r,B,T,U and recovered all seven coefficients,
including its two initial zeros. It checked the displayed factorial-ratio
identities and every positivity step.

For the highest coefficient, the gamma-product variable is positive with
nondegenerate continuous support and has moments
`d_n=(rn)!/(n!(r!)^n)`. The consecutive ratios agree by canceling the factor
`r(n+1)` in the factorial ratio. Consequently the leading determinant is a
strictly positive Gram determinant. Its generalized 2x2 moment minors are
also strictly positive: strict moment log-convexity makes the consecutive
ratios increase, yielding `U>B^2`, `U>BT`, and `BU>T^2`. These justify the
highest coefficients in the entire leading-block corollary.

The assertion about *all* order-two Hankel minors in both families remains
unproved here. Its proposed adjacent fixed-sum reduction is valid: after
ordering the two middle indices b<=c, a determinant
`f_a f_d-f_b f_c`, with a+d=b+c, telescopes into
`f_m f_(a+d-m)-f_(m+1) f_(a+d-m-1)` for m=a,...,b−1.
Each is the stated adjacent inequality with m<n. Conversely adjacent
inequalities are minors with rows (0,1) and columns (m,n). This reduction
does not divide polynomials or transfer triangle TN2 to Hankel TN2.

## Interpolation

The parent audited the formal generating-function derivation and the
tridiagonal characteristic recurrence. For a normalized complex eigenvector,
the expectations of the real symmetric matrices D and K are real; the
eigenvalue lies in their stated numerical-range rectangle. The absolute row
bound on K is n−3/2 for n>=2, and the n=1 case is checked separately. This
proves the all-degree equal-parameter theorem and its strict interior case.

For independent parameters, the Cayley map sends the disk interior to the
left half-plane. The multi-affine Bernoulli interpolation produces exactly
the displayed F_n. The parent compared its transform with the original
elementary-symmetric formula for P using 80 exact rational controls, and
compared independently evaluated integer determinants with the compressed
coefficient certificates in 40 cases. The lane's exact polynomial verifier
regenerated **all 4,816 coefficients** through degree five.

Every coefficient box is full and strictly positive. Separate homogenization
in each pair (a_i,1−a_i) therefore gives positive Hurwitz determinants even
at parameter faces. The leading and constant coefficients vanish only at
their respective all-one and all-zero endpoints, whose factorial
polynomials are explicitly checked. The classical Routh–Hurwitz criterion,
as proved in [Holtz](https://arxiv.org/abs/math/0512591), then supplies strict
interior stability elsewhere. This is a uniform finite-degree proof, rather
than root sampling. It does not certify degrees six through eight.

## s-Eulerian reconstruction and correction

The independent [Eulerian review](eulerian-independent-review.md) verifies
the extra-ascent construction, contraction at incoming ratios zero and one
half, unit separators, reversal, complete degree-two block classification,
and the strict b<5 exclusion. It caught a coefficient error:
`E_(2,6,3)=1+19x+16x^2`, replacing the incorrect `(1,18,17)` row.
The report was corrected and the exact checker now asserts all five
exceptional rows. E1–E3 survive this correction. No argument here assumes
simple roots in arbitrary nonunit blocks or sharpness in every degree.

## Disposition

The nine theorem scopes and three precisely limited obstructions are saved.
The initial complete-proof submissions Q165/Q166/Q325 retain their previous
review status; this round does not re-audit their entire proofs. The original
20-question membership, stable IDs, historical report, canonical questions,
and resolution ledger remain unchanged. The unknown Schur claims,
degree-six-to-eight certificates, universal Hankel TN2 proof, and strict-root
claims remain explicitly pending in [NEW-QUESTIONS.md](../NEW-QUESTIONS.md).
