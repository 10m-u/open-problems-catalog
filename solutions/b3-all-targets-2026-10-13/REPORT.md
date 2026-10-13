# B3 all-target completion report

13 October 2026. B3 is complete under the user's stopping rule for this run:
every one of the 49 frozen catalog questions and seven broader mathematical
targets is resolved or has reached five consecutive substantive failed
full-target attempts. The same `/root/b14_local_optima` subagent was retained
throughout. Private catalog filing and preservation validation passed.

| Scope | Previously resolved and retained | Newly resolved in this run | Stopped unresolved after five failures | Total |
|---|---:|---:|---:|---:|
| Catalog questions | 4 | 4 | 41 | 49 |
| Broader targets | 0 | 3 | 4 | 7 |
| All targets | 4 | 7 | 45 | 56 |

“Resolved” includes proofs and counterexamples. One new catalog closure is
an attributed literature result. The stopping dispositions leave their
questions mathematically unresolved; partial results do not reset counters.

## Catalog resolutions

| Target | Accepted outcome and evidence |
|---|---|
| Q165 | Retained proof of real-rooted domination parity polynomials for every path length, with the original degenerate-endpoint convention. [Retained review](ROOT-REVIEW.md#retained). |
| Q166 | Retained ordinary log-concavity proof for compositions avoiding a prescribed run of unit parts. Its numerical weighted scope remains distinct from coefficientwise positivity. [Retained review](ROOT-REVIEW.md#retained). |
| Q325 | Retained sharp imaginary-part bound for every polynomial in the stated Stanley-nonnegative cone. [Retained review](ROOT-REVIEW.md#retained). |
| Q3499 | Retained 13-gon face-lattice Ehrhart counterexample: linear coefficient `-298495711/35302608`. [Retained review](ROOT-REVIEW.md#retained). |
| Q1443 | New degree-36 counterexample in the exact class U_36: `(2z+1)^32(5z+2)^2(5z-12)^2` has consecutive distinct roots with gap `14/5`, refuting every proposed bound below two. [Proof and certificate](interpolation/Q1443-RESULT.md). |
| Q3902 | Attributed literature counterexample to universal reflexive boundary-polytope gamma positivity through the homology branch. The exact lattice and complete gamma certificate were audited. [Closure and scope](boundary-polytopes/Q3902-LITERATURE-CLOSURE.md). |
| Q4082 | New full proof of `M(X)^2[1+k(alpha)Var(X)]<=1` for every stated discrete alpha-concave law, `-1/3<alpha<0`, with `k(alpha)=(1+2alpha)^2(1+3alpha)/(1+alpha)^3`. [Full proof](concave-laws/FULL-PROOF.md). |
| Q4666 | New counterexample to log-concavity necessity: offspring law `(1,2,3,5)/11` admits a simultaneous nested conditioned-tree coupling at every size although `3^2<2*5`. [All-size proof](stirling/Q4666-RESULT.md). |

Q3902 credits [Ferroni's July 2026 preprint](https://arxiv.org/html/2607.02424v1),
Corollary 2.2. Five internally disjoint length-eight paths produce a
36-dimensional reflexive homology polytope with `gamma_16=-9799680`.
The standalone cohomology assertion and the source's separate subcomplex
reflexivity Question 9.3 are outside this closure. The local work reconstructs
the published numerator and verifies the target transfer; it does not claim
discovery of that counterexample.

## Broader targets

| Target | Disposition |
|---|---|
| B3C-Q01: central crossing-interval APP | Five accepted full-target failures; unresolved. [Attempts](intervals/ATTEMPTS.md). |
| B3C-Q02: coefficientwise Hankel TN2 for both Stirling families | Proved for every integer parameter r>=1, arbitrary row and column gaps, and support boundaries. [Proof](stirling/HANKEL-TN2.md). |
| B3C-Q03: cycle coefficientwise Hankel TN3 | Five accepted full-target failures; unresolved. [Status and evidence](STATUS.json). |
| B3C-Q04: all-degree positive Hurwitz coefficients | Five accepted full-target failures; unresolved. [Status and evidence](STATUS.json). |
| B3C-Q05: independent-parameter centered disk | Five accepted full-target failures; unresolved. [Status and evidence](STATUS.json). |
| B3C-Q06: sharp s-Eulerian representation length | Proved: the shortest positive integer vector representing `(1+u*x)^d` has length exactly `2d-1` for every d,u>=1. [Proof](eulerian/SIMPLE-ROOTS.md). |
| B3C-Q07: simple roots in nonunit s-Eulerian blocks | Proved for every nonempty vector whose entries are at least two; arbitrary denominator order and degree-preserving steps are covered. [Proof](eulerian/SIMPLE-ROOTS.md). |

## Retained partials and methods

The [30 scoped result records](RESULTS.json) distinguish exact catalog
closures, broader theorems, restricted results, auxiliary corrections and
the failed-route register. Sixteen new partial topics mark eighteen catalog
questions without excluding them from open review. Additional partials for
Q167, Q1160 and Q2400 retain their older ledger topics unchanged.

Among the useful all-size results are the complete degree-five integer
coefficient orders; layered permutation interval inequalities; the colored
endpoint partition and small gamma orbits; atom log-concavity through twice
a monoid's multiplicity; a fixed-density random-graph log-concavity prefix;
the Perazzo derivative-rank identity and quartic rank classification;
parameter-four q-Fibonomial unimodality; width-two weak-order coefficient
positivity; arbitrary cycle connected-sum Boninger inequalities; path and
subsum endpoint bounds; two-column Eulerian total positivity; horizontal-strip
endpoint eigenvalue unimodality; descending Koszul half-rows in every socle
degree; and Schur midpoint positivity with injective output fibers.

The boundary packet also proves the even binary-code gamma formula for every
reflexive crosspolytope, covering homology polytopes with vanishing top homology.
The circuit packet gives the precise fractional-gauge correction to free-sum
Ehrhart multiplication. Auxiliary Perazzo source corrections are filed as
such; they do not solve the catalog classification question. Source-known
families and earlier bounded controls retain their attribution. Exact scope
and review provenance are recorded in [ROOT-REVIEW.md](ROOT-REVIEW.md).

## Failed attempts and stopping

There are 225 accepted failed routes across the 45 stopped targets, plus
three failed routes before later resolution: two for Q4666 and one for Q3902.
All 228 are preserved. Q1262's rejected proposed E01 remains explicitly
rejected; its five accepted failures are the substantive replacement sequence.
Service errors, source lookups, audits and known-range replays count zero.
Shared mechanisms between related targets are disclosed in the review.

The 41 unresolved catalog stops are Q164, Q167, Q183, Q1158, Q1159, Q1160,
Q1161, Q1249, Q1262, Q1263, Q1366, Q1441, Q1442, Q1454, Q2212, Q2400,
Q2508, Q2731, Q2751, Q2924, Q3436, Q3437, Q3498, Q3500, Q3568, Q3579,
Q3626, Q3627, Q3678, Q3702, Q3703, Q3846, Q3892, Q4331, Q4332, Q4396,
Q4429, Q4443, Q4591, Q4592 and Q4665. The other four stops are B3C-Q01,
B3C-Q03, B3C-Q04 and B3C-Q05. [STATUS.json](STATUS.json) links every
accepted route to its written analysis and evidence. The frozen
[question register](QUESTION-REGISTER.md) retains the exact target wording
and initial states.

## Filing and verification

[FINAL-FILING.json](FINAL-FILING.json) records private canonical filing;
[FINAL-VALIDATION.json](FINAL-VALIDATION.json) records the preservation audit.
The catalog has 439 statement decisions and 254 topics. Programme compilation
has 462 records, including the thirty records from this run. All original
432 compiled records and the separately filed Q4082 increment remain exact.
All 28,601 statement records retain their original source fields and order.
Every previous stable decision remains unchanged.

Q1443 is the sole older topic refined from partial to disproved. Its complete
previous note, source prefix and topic version are preserved, and its earlier
compiled result remains unchanged. All other 235 previously filed topics are
unchanged. The validator checks target membership, stopping counters, proof
references and anchors, resolution scopes, result routing, checker receipt
status and recorded source hashes, and local document links. The proof reviews
and independent checker replays are described at their individual scopes;
finite controls support the written proofs rather than replace them.

The missing original B3 verification archive remains absent. New proofs and
receipts have separate provenance. This report records internal mathematical
review, not external peer review or a novelty certification. Filing was private.
The dated B2 and B14 handoffs and original B3 packets remain preserved.
