# Independent Q4665 proof and count review

Reviewed 2026-10-13 by the same retained agent. I accept the two scoped
all-size consequences and five distinct failed full-target routes. The
full four-function Schur midpoint conjecture remains unresolved; the
finite calculations are neither a proof nor a counterexample.

The exact target agrees with [Chan--Chen--Pak--Soskin, Conjecture 11.5](https://arxiv.org/html/2606.06688v1#S11.SS2):
finite nonnegative real weights on partitions of any fixed padded length,
coordinatewise ceiling/floor midpoint hypotheses, and positivity in the
full Schur basis. I also checked the original [Lam--Postnikov--Pylyavskyy
Theorem 11](https://math.mit.edu/~apost/papers/schurpositivity.pdf), including
the zero inner shapes and padded parts. It supplies the pairwise midpoint
inequality used here, rather than a four-function conclusion.

The summed-fiber criterion is correct: termwise Schur domination followed
by a genuinely sufficient summed budget proves the result. Nonnegative
Schur multiplication justifies both stages. A singleton input support
makes the midpoint-pair map injective because the sum of the output
partitions recovers the other input. This proof covers all lengths, sizes
and nonnegative real weights in its restricted support scope.

The nonnegative-alphabet consequence is also correct. Multiplying each
weight by its Schur evaluation preserves the local scalar midpoint
inequality by the pairwise theorem. Extension by zero to Z^l satisfies
scalar KL: outside partition inputs the left side is zero, and midpoint
images of partitions are partitions. Finite support avoids convergence
issues. This proves evaluations, not Schur signs. The displayed formal
`s_2-s_11=sum x_i^2` example is appropriately distinguished from an actual
legal four-function difference.

I checked each obstruction and its count contract:

- A1: the actual legal supports on 0 and 2 overspend the output (1,1)
  fiber; the intermediate residual has coefficient -1 at `s_11`.
  The actual final difference stays Schur-positive, so only the asserted
  two-stage budget inference is refuted.
- A2: the actual singleton example violates the meet/join hypothesis;
  no common injective relabeling can turn distinct input outputs of
  min/max into the equal midpoint outputs. Auxiliary lifts remain open.
- A3: a complete all-size scalar reduction is worked, but its final
  numerical-to-Schur implication fails in the ambient ring. The exact
  missing obligation is a stronger statement for the special family of
  actual differences, not another numerical evaluation.
- A4: joint uniform rounding on two actual fixed-row-output LR pairs
  leaves total degree, for every N>=2. No tableau interior coordinates
  can restore that degree. This concerns rounding two coefficient
  summands, not the midpoint pair within one original summand.
- A5: the new rational-weight construction explicitly enforces every
  local inequality and computes complete Schur differences outside the
  source's reported range. It fails to produce a counterexample. This
  is one worked construction, not a count per example or a rerun of an
  already-counted local search.

A1 and A4 are distinct failed coefficient proof mechanisms: the former
assumes an output weight budget after valid pairwise domination, whereas
the latter needs closure of a fixed-coefficient joint LR domain. A2
attempts operation transport; A3 attempts a change of positivity
certificate; A5 attempts an actual counter-construction. No merging of
these five obligations is warranted.

[Independent checker](check_schur_review.py) recomputes **all 233** saved
LR products by a Jacobi--Trudi determinant expansion and horizontal-strip
Pieri interlacing. The submitted ballot-tableau code is used only for
the final comparison. All products agree. All 32 saved weighted
differences were rebuilt with exact rational arithmetic, all local
hypotheses rechecked, and all resulting coefficients agreed and were
nonnegative. The actual fiber obstruction and 19 fixed-output degree
controls were also checked. The [independent receipt](SCHUR-REVIEW-CHECK.json)
records coverage and hashes. No global status or submitted receipt was
modified.
