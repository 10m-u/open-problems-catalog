# B3 reviewed resolutions

13 October 2026. These reviews separate full targets from useful partial results.

## Retained

The initial intake review and its cited original
proofs were read before retaining Q165, Q166 and Q325. Q165 retains its stated
degenerate-endpoint convention; Q166 proves ordinary log-concavity; Q325 retains
its stated hypotheses. No canonical conclusion was transferred to larger questions.

For Q3499, the [counterexample proof](../seven-more-2026-10-09/discrete/Q3499-proof.md)
and [independent review](../seven-more-2026-10-09/algebra/review-Q3499.md)
were read. The full face lattice of a 13-gon gives an Ehrhart polynomial with
linear coefficient -298495711/35302608. The distinction between the order
polynomial and its shifted Ehrhart polynomial is preserved. Earlier exact
checks retain their original provenance; this review does not claim a fresh replay.

## Hankel TN2

The retained subagent's [all-size proof](stirling/HANKEL-TN2.md) was read in full.
The normalization gives the asserted weighted log-concavity, hence numerical
triangle minors of order two. The symmetric pairing uses that triangle inequality
and the monotonicity of birth and stay weights at each coefficient degree.
Telescoping reduces every arbitrary-gap Hankel minor of order two to these
adjacent-row differences without dividing coefficient polynomials. The row-zero,
column-zero and support boundaries are included.

The proof resolves B3C-Q02 for both cycle and subset families at every integer
r>=1. Its exact [check receipt](stirling/HANKEL-TN2-CHECK-RESULTS.json) passed:
900 independent assemblies, 5,460 normalization defects, 40,500 triangle minors,
46,200 paired terms, 900 recurrence differences, and 40,500 arbitrary-gap minors.
These finite checks support the proof; they do not replace its all-size argument.
The result gives a new partial scope for Q1160, whose all-orders target stays open.

## Eulerian

The root's [strictness and representation proof](eulerian/SIMPLE-ROOTS.md) was
reviewed independently by the same retained subagent in
[EULERIAN-REVIEW.md](stirling/EULERIAN-REVIEW.md). The published weak interlacing
input is identified precisely. The new argument proves strictly signed proper
prefix sums at each old root and a nonzero weighted sum after appending any
denominator at least two. It covers arbitrary denominator order and equal degrees.
No conclusion of strictness is inferred from weak interlacing alone.

This resolves B3C-Q07. Unit entries split the polynomial into nonunit blocks;
each block dividing (1+u*x)^d has degree one. Counting the d blocks and their
d-1 separators, with the explicit matching construction, resolves B3C-Q06.
The [exact receipt](eulerian/STRICTNESS-CHECK.json) passed 3,905 vectors,
155 literal enumerations, 3,900 summation identities and 49 sharp constructions,
and retains the repeated-root unit-separator control. The full coloured
classification in Q1262 remains open. Historical missing archive bytes have
not been recovered by these new proofs.

## Stirling attempts and restricted theorems

The root read the retained agent's full triangle, cycle-Hankel, stability,
and row-pattern packets, including the subsequently added symbolic
derivation of the all-r triangle order-three formulas. Their attempts have
different concrete obligations; overlapping methods across separately
stated targets are disclosed. Source or service failures contribute no
mathematical count. Accept five failed full-target attempts each for
Q1158, Q1159, Q1160, Q1161, Q4429 and B3C-Q03. These dispositions leave
the catalog conjectures open. The root reran the cycle-Hankel, row-stability
and row-pattern checkers; all passed their exact controls.

The triangle packet proves positivity of the specified first solid
order-three minor for all r, by reducing the atom-size sums to rational
identities and then to positive factors. Parameter substitutions alone
are not used as its all-r proof. It leaves arbitrary initial minors missing.
The cycle-Hankel packet's factorial-weighted moment theorem is numerical
in x; the factorial weight cannot be discarded. Its three lowest nonzero
coefficients in the displayed shifted order-three block have all-r proofs,
but that block's remaining coefficients and arbitrary blocks stay open.

For Q1161, the exact fixed-excess assembly formula gives rational identities
for the normalized third Hurwitz determinant. After n=u+6, their numerators
have positive coefficients and every denominator factor is positive.
The finitely many lower-degree endpoints and the strict log-concavity
argument complete positivity of every applicable first, second and third
Hurwitz determinant for both r=3 families at all n. Higher determinants
remain unproved. Its compound-Poisson instability example tests a numerical
moment-to-stability implication; it does not claim coefficientwise moment
total positivity. This qualification is essential to the accepted count.

For Q4429, the left and right endpoint limits are for fixed r and fixed
column or fixed right excess. The entirely convex limit is for fixed n
and r tending to infinity. Both follow from the finite atom formula or
the stated coefficient asymptotics. Their differing quantifiers leave
an intervening two-parameter region unproved. Actual finite curvature
drops refute the proposed monotonicity in n, not the catalog shape claim.

## Intervals and path heights

The same retained subagent independently read the full root packets,
primary definitions and earlier scope reductions, then filed
[INTERVAL-PATH-REVIEW.md](stirling/INTERVAL-PATH-REVIEW.md). Its exact
independent ceiling/component, midpoint, factorial-ratio and Sturm controls
passed on root replay. Accept the five-attempt stops for Q164, B3C-Q01,
Q4331 and Q4332. The APP intersection counterexample has a stronger
single-legitimate-band refinement at the same count, with the old family
still explicitly a generic APP control.

Accept both all-size partial theorems in paths/UPPER-TAIL.md: the displayed
degree-normalized upper ranges for A/B, and the final nontrivial ordinary
inequality for M/R at every length. Their formula thresholds, parity
normalizations, component uniqueness and finite small endpoints were
checked separately. Their interior gaps remain genuine open obligations.

## Q4666 tree-growth converse

The root read the retained agent's entire [counterexample proof](stirling/Q4666-RESULT.md),
the literal catalog setup, and the primary source's complete Propositions
2.8 and 3.2 and Problem 1. Both source propositions have the required
nondegeneracy hypotheses and impose no log-concavity assumption at these
reduction steps. The all-size proof is accepted: the square production
matrix Q has contiguous band support, its exceptional first-column
adjacent minors are positive, and its adjacent ratios therefore control
arbitrary rectangles. Cauchy–Binet transfers row-pair TN2 through Q.
The two parity bases give the needed f2-to-all-rows base; induction on
the smaller row index then proves the entire forest array TN2.

Pairing that array with e1, (3,5), and Qe1 gives precisely the three
normalizer inequalities stated in the proof. The upper comparison has
lag two. The root-composition criterion needs only q=n-m<=n-1, so
R_(q+2)<=R_(n+1) is valid even at m=1. The zero-size shifted constants
are handled separately. This verifies both successive admissible
composition pairs. Proposition 3.2 then builds a simultaneous Markov
coupling that preserves literal Ulam–Harris parents and left siblings.

Thus mu=(1,2,3,5)/11, zero beyond three, is a full counterexample to
the log-concavity necessity clause: mu2^2=9/121<10/121=mu1*mu3.
It has positive size normalizers and no internal zeros. The previous
support-necessity partial theorem remains valid; it is not refuted.
The root reran [check_q4666.py](stirling/check_q4666.py): 23,409 square
matrix minors, 36,100 forest minors, 325 independent Lagrange entries,
120 ratio controls and 3,280 proposition inequalities passed. These
bounded checks support an all-size structural proof, rather than
standing in for one. No external peer review or priority is claimed.
The two preceding failed routes remain in the research record; the
accepted third route ends further mathematical attempts on Q4666.

## Matrix and subsum audit acceptance

Root read the full independent [matrix review](stirling/MATRIX-REVIEW.md)
and [subsum review](stirling/SUBSUM-REVIEW.md), their receipts and the complete
independent subsum checker, and reran the latter successfully. The matrix
review independently expands 21 leading-column minors and recomputes the
forced negative production entry. The all-size two-column determinant
identity is accepted at its written scope. Output-row rescalings remain
outside the negative production-matrix obstruction.

Q3846, Q3702 and Q3703 each stop unresolved at five distinct worked routes.
The Q3702 size-recursion and fixed-factor routes share a gapped-convolution
obstruction; their distinct sufficient contracts are explicitly disclosed
in both packets. The subsum endpoint proofs, exact mixture variance, infinite
powers-of-two ultra-log-concavity obstruction, full-support argument and
central limit theorem pass internal review. None proves or refutes the full
ordinary log-concavity conjectures. Root replay passed 16 product and 15
binary-partition expansions, 32 regrouping/increment controls and exact
mixture, support and moment controls. No external review or novelty claim
is implied. These three attempt counts are accepted for the user's stopping
rule, with the stronger-property failures kept separate from the targets.

## Q1443 root-gap counterexample

Root read the complete [result](interpolation/Q1443-RESULT.md), certificate,
checker and [independent review](stirling/Q1443-REVIEW.md), then reran the
independent checker successfully. The degree-36 polynomial
(2z+1)^32(5z+2)^2(5z-12)^2 has consecutive roots x34=-2/5 and x35=12/5,
with gap14/5. Every one of its37 sampled-value numerator coefficients is
positive; all36 disjoint negative sign-change brackets pass exact integer
arithmetic in two differently implemented evaluators. Newton interpolation
proves the generating-function identity at all coefficients. The AESW
finite-product theorem then certifies the entire sampled Toeplitz matrix.
This closes the exact frozen catalog Q1443 by counterexample on its first
new full-target route. Stop the problem; no additional attempts are needed.

The original source also asks whether *some finite* dimension-free bound
exists. A gap14/5 does not settle that broader question. The accepted
resolution is specifically the catalog's proposed bound 1<=d<2. Earlier
lower-bound proofs and exploratory failed candidates stay preserved. No
novelty or external peer-review claim is made.

## Q3579

Root read the complete Q3579-ATTEMPTS.md and check_chern.py, and the primary
Libman–Orelowitz Problem 26 and its finite-variable qualification. The exact
checker passed: 44 n=2 identity controls, the decorated-tableau dimension,
the separating functional, the negative stable coefficient outside the
finite-variable range, all 77 forward Pieri controls, and all six fixed-tableau
signed fibres. The five full-target routes are accepted as failures. A1 and A5
share a decorated tableau model; A1 rejects a prescribed lifted vector-crystal
action, whereas A5 rejects cancellation restricted to each fixed tableau.
Neither rules out a different global crystal or cancellation rule. General
Q3579 remains open; the target stops at five failures, with the all-shape n=2
identity and all-n Pieri relation retained at their explicit partial scopes.

<a id="q4082-full-sharp-variance-bound"></a>

## Q4082 full sharp variance bound

Accepted as locally proved at the frozen Conjecture 4.7 scope. Root read
the source, all analytical components and the retained agent's independent
review, then replayed both checkers. The source coefficient k, every
alpha in (-1/3,0), and all finite/one-sided/two-sided alpha-concave laws
are covered. No novelty or external peer-review claim is made.

The proof matches maximum mass and mean with a convex-order dominating
affine law, proves every one-sided slope using Gamma kernels and a positive
Bernstein rectangle certificate, bounds the first moments through a directly
proved Gamma variance inequality, and glues the tails with a positive
cross-term factor. Boundary and moment convergence are justified.
The separate stdlib Fraction auditor reconstructed all 221 polynomial slots,
verified all four exponential controls and replayed the gluing independently.
The certificate hash is 156a070bf0f80bd52e7fe685338b5e65c65d9686c7368d1d6557e2284984bdc1.
Evidence: concave-laws/FULL-PROOF.md and stirling/Q4082-REVIEW.md.
Canonical private filing for Q4082 is complete; FILING.json preserves all
432 previous compiled result records, all prior decisions and statement fields.
Filing of the remaining B3 results is still pending.

<a id="interpolation-final"></a>

## Interpolation final proofs and counts

Root read INTERPOLATION-REVIEW.md and its complete independent checker, then replayed all 638 exact corner controls and the 257 large-base brackets. Accepted Q1441/Q1442/B3C-Q04/Q05 at five unsuccessful full-target routes. The corner theorem and large lower family retain their exact partial scopes; N05 rules out only the concrete cutoff-six construction, leaving larger cutoffs open.

<a id="finite-convolution-final"></a>

## Finite convolution final proofs and counts

Root read FINITE-CONVOLUTION-REVIEW.md, the result proofs and the exact checker, then replayed 420 moment and 528 derivative identities. Accepted Q3436 and Q3437 at five unsuccessful full-target routes each. All commutators through degree five, all-degree rank-one spectra, degree-two rectangular convolution and the derivative identity retain their limited scopes. F03/F04 are separately reviewed contracts with source anticipation disclosed, without a target counterexample claim.

<a id="rook-and-order-final"></a>

## Rook and coefficient-order final review

Root read both independent reviews and the complete row/column-subset
checker, then replayed the 662 source bases, 448 rank-two board controls
and all fourteen degree-five order witnesses. Q183 stops unresolved after
five distinct failures. The root's old weighted enumeration used dual
bases; the source and dual specializations both have discriminant -602100.
The convention is corrected explicitly without altering the original receipt.
The all-board rank-two theorem retains its stated scope.

Q167's degree-five classification is accepted, including ties. O01 and O03
are merged as one reciprocal/unit-factor induction route. The supplementary
Q167-O06-REVIEW accepts the endpoint sum/product extremal-separation method
as the distinct fifth failure: (1,1,12,14) and (1,2,4,21) have the same sum
28 and product168 but opposite c2/c4 orders. A set-valued classification with
additional arithmetic data remains possible. Q167 stops unresolved with
five accepted failures; degree at most four remains the prior result.

<a id="hadamard-and-forest-final"></a>

## Hadamard and forest-correlation final review

Root read the independent reviews and full Fraction/BFS checker and replayed
256 shifted-pole identities, four exact discriminants, three cycle identities
and141 cycle/cactus pair controls. Q1249 and Q4396 each stop unresolved after
five distinct failures. The all-size shifted repeated-pole preservation and
coefficientwise cactus correlation proofs are accepted at their partial scopes.
The Hadamard attribution is clarified with Csordas–Dimitrov Theorem2.4(4)
and an explicit entire limiting argument. The K6 screen is bounded evidence
for arbitrary graphs, not the all-size proof. No stronger-property obstruction
in these packets is promoted to a counterexample to either catalog target.

<a id="power-monoid-final"></a>

## Power-monoid final review

Root read the independent review and per-set factor checker, and replayed
156 maximum-formula and 31 boundary controls. The arbitrary numerical-monoid
theorem for cutoff l<=2m is accepted, with m the least positive element.
The cutoff18 computation covers that one cutoff, not all smaller cutoffs.
Q2212 stops unresolved after five distinct full-target failures. The original
paper's almost-all-cardinality-index quantifiers are kept distinct from the
survey's stronger attribution about full rows for almost all cutoffs.

<a id="og-and-lg-final"></a>

## Equivariant OG and K-theoretic LG final review

Root read both full attempt packets, their exact checkers and the cited
primary Chevalley, edge-rectification, Pieri and genomic rules, then replayed
all five checkers. Q4591 and Q4592 each stop unresolved after five distinct
full-target failures. Rank-two presentations and the fresh -5 Pieri
reconstruction are accepted as partial results and controls. Known edge
order and genomic overcount examples are attributed to their sources;
fresh replay is validation, rather than a separate attempt.

The rim test in the LG checker is valid for shifted skew partition shapes:
a strictly southeast pair forces every intervening southeast diagonal cell
to stay inside the outer shape and outside the inner shape. Thus it agrees
with the adjacent-diagonal rim test. An additional exact check compared
2,352 nested pairs through rank6. Ballot counting increments unprimed letters
only, matching the primary definition. The leading Q rule is used only in
leading degree, and the full coefficient is reconstructed using proved
Pieri rules and the codimension filtration.

The five routes on each target have distinct specified contracts even where
they reuse a candidate or witness. None of the failed unchanged-object,
parameter reconstruction, raw localization, prescribed rectification,
normalization, rescaling, Euler-duality, positive Pieri assembly or all-Q
object methods rules out a different full combinatorial rule.

<a id="shuffle-review-correction"></a>

## Shuffle review and count correction

The all-size k=1 and k=N proofs pass, hence every rank for N<=2.
Root replayed the independent direct-tuple/deleted-column checker on
434 strips, 1,301 polynomials and 734 endpoint controls. V02--V05 are
four accepted failures. The n<=14 screen merely repeats the source's
n<=28 coverage and does not complete the failure counter. Q4443 is active
at four failures while V01 receives a fresh actual-strip construction.

The V01 continuation now passes its independent review:260 actual three-row
strips,1,760 intermediate polynomials, with ambient sizes beyond28.
Root read the added checker segment and replayed the independent direct
expansion on20 strips/32 intermediate polynomials. The attempted valley
construction failed, and Q4443 now stops unresolved with five accepted
distinct failures. The old finite replay remains validation only.

<a id="fibonomial-final"></a>

## Q-Fibonomial final review

Root read FIBONOMIAL-REVIEW.md and its full independent convolution/formal
division checker, then replayed136 exact base differences, all six residue
errors, the two-variable numerator cancellation, Hall neighbors, constrained
recursion and literal NNEEN fiber weights. The all-m parameter-four theorem
is accepted, extending the known boundary to min(m,n)<=4. It leaves the
full question unresolved at min(m,n)>=5. All five full-target routes pass
the distinctness and scope audit, and Q2751 stops at the user's failure limit.
The partial result does not reset the counter. A corrected draft degree
and checker implementation errors are zero mathematical failures.

<a id="boninger-final"></a>

## Boninger full-target route review

Root read the primary [Boninger paper](https://arxiv.org/pdf/2608.28484v1),
including the actual 4_1 and 8_10 polynomials, root/basepoint-dependent
tree weights and canonical Tait minor conditions. All attempt packets,
the cycle-product proof and the full exact checker were read and replayed.
The positive-cycle formula follows for every size, and arbitrary connected
sums of those diagrams and their mirrors have M-convex support and all
root-direction coefficient inequalities. Cross-group directions cannot
have both neighbors in the support; within-group rows are convolutions
of hole-free uniform rows. This is a family theorem, not either full
catalog conjecture.

The exact normalized quadratic derivative for actual 8_10 has Hessian
determinant -1 and trace 2, hence two positive eigenvalues. The quadratic
criterion and nonnegative derivative closure in
[Brändén--Huh](https://arxiv.org/pdf/1902.03719) confirm the stronger
Lorentzian certificate fails. Arbitrary larger clearing monomials cannot
repair it: differentiating their factorial-normalized monomial lift
recovers the minimal lift exactly. The source-known obstruction is
attributed, and the original two targets pass on that example.

The other routes have worked symmetric-difference, joint-marginal,
conditional-minor and product/generation obligations. Formal relaxed
examples are consistently separated from actual links. Five distinct
full-target failures are accepted for each of Q3626 and Q3627; both stop
unresolved. The positive cycle-product partial does not reset either count.

<a id="poset-final"></a>

## Crown and width-two family review

Root read POSET-REVIEW.md and its full independent Fraction/Sturm and
coefficient-array checker, then replayed all 19 gamma rows, 16 direct
cyclic-assignment/matrix traces, the full C6 descent row and Rayleigh
witness, and 48 weak-order factors. The crown transfer formula is valid
for arbitrary size; real-rootedness is certified only for n=2,...,20.
C01--C05 are accepted as five distinct failed full-target routes. The
operator ansatz and spectrum-only relaxation have their limited scopes
explicit; neither is a crown conjecture counterexample. Q3498 stops.

The width-two theorem proves nonnegative ordinary order-polynomial
coefficients for all ordinal sums of layers of size one or two. The
fixed-b generating function and imaginary-axis recurrence yield the
claimed vertical root line by elementary interlacing. Chain and empty
boundaries are covered. Q3568 remains active because arbitrary two-chain
posets need not have this layer structure; no failure is counted merely
for this proof audit.

<a id="links-gould-final"></a>

## Links--Gould route review

Root read all five Q2731 packets and the entire exact checker, replayed
its receipt, and read the primary type-B exchange definition, stated
actual exception list, both Alexander identities, cubic R1 and
connected-sum multiplicativity. Each route is valid at its stated
scope. The all-convex-relations catalog condition is retained.

The concave min-affine model fails the specified type-B exchange;
actual source-listed knots show the stronger certificate cannot be
uniform. The Laurent kernel intersection is a product ideal although
its two factors are not comaximal over integers, by prime divisibility
in the Laurent UFD. The symmetric 3×3 grid passes every lattice-line
condition but fails its exact centroid inequality. Substituting negative
variables in primary R1 gives the displayed cubic factorization; the
uniform generator sign twist still leaves the negative middle branch.
Finally the two primitive-segment factors separately satisfy the
three coefficient properties but have a product with a missing hull
lattice point, refuting only unrestricted multiplicative closure.

Formal examples are not asserted knot invariants. The eight actual
non-type-B examples and the source's large bounded verification are
attributed evidence, not a new enumeration. These exchange, information,
convex-reconstruction, skein-induction and product-closure routes are
distinct. Five full-target failures are accepted, and Q2731 stops
unresolved under the user rule. No source lookup or replay was counted.

<a id="boolean-width-two-final"></a>

## Boolean and width-two final route review

Root read POSET-ROUTE-REVIEW.md and its entire independent ideal-multichain
and Newton-difference checker, then replayed all394 twelve-element
orders, Boolean h* n0..4 and all six stored gamma rows through n5.
The alternative weak-map method reproduces every scaled ordinary
coefficient independently of descent DP. Root accepts the five
restricted full-target routes for each of Q3500 and Q3568; both stop
unresolved. The actual/formal examples are properly separated and
neither root-preservation nor the full positivity conjecture is
refuted. The all-size weak-layer proof remains an accepted partial.

<a id="rulings-final"></a>

## Positive-braid ruling final review

Root read all five routes, the full integer walk engine, Fraction/Sturm checker and two-strand proof, and replayed 35 fresh longer braid rows, 4096 independently enumerated masks for the source example, 22 braid-relation controls, 61 two-strand rows and400 composition pairs. Primary Definition2.1 identifies the stay steps with ruling switches; left multiplication swaps values. Component/parity normalization agrees with the actual source.

The degree12 actual positive-braid polynomial has exactly four distinct real roots, so the stronger real-rootedness certificate fails while the target inequalities hold. The actual negative transfer cross term, one-meeting suffix-exchange obstruction and adjacent-generator off-diagonal composition contributions each disprove their precise sufficient contract. The last two algebraic routes share state interactions but require different local curvature and global structural lemmas. The two-strand formula and parity-normalized composition identity have all-size proofs.

Five distinct substantive full-target failures are accepted. Q2924 stops unresolved; finite enumeration, the stronger-root counterexample and useful two-strand partial do not close or reset the full target. Source-range replays and convention corrections count zero. Checker SHA256:e24d247c9d0e822450e5f185684e01ab8f121f4e1db2259f8a90c6bd3291f9a7.

<a id="colored-final"></a>

## Colored Eulerian independent review

Root read the complete independent review and its separate literal-word, inversion-sequence and Fraction checker, then replayed all36 inputs and4,012 candidate strings,86 growth controls,90,416 wordwise endpoint checks and explicit small gamma orbits. The endpoint involution has an all-size proof for distinct symbols/common colors, giving both ordinary symmetric parts. N1/N2 have gamma interpretations for every common color count; repeated letters give the stated actual failure. These partials do not close the full question.

Q1263's five distinct sufficient-construction failures are accepted; the full target stops unresolved. Q1262 E01 is rejected as a count because it evaluates a previously general recognizer on fresh inputs without a new structural inference. E02--E05 are accepted, leaving Q1262 active at four consecutive substantive failures. No source/error/audit operation counts as a solve attempt.

<a id="pattern-final"></a>

## Classical permutation interval final review

Root read the complete independent proof/count audit and checker, then replayed every1573 rank row, the literal Hall deficit and subset-DP matching, all layered/fiber formulas and actual deletion intersections. Equal-layer-count intervals are products of chains; the two-layer one-bottom rows are affine minus hinges and thus positive arithmetically concave. Unique-inversion grids retain exact occurrence fibers. These are all-size partial proofs.

Five distinct full-target failures are accepted for Q1366. Source qualification: the original paper covered top lengths<=8, so the n8 portion is an old-range control; only66 tops and1333 intervals at n9--12 supply the fresh valley construction. Uniform-weight fiber quotients and one-occurrence coverage have different actual obstructions, explicitly limited to those contracts. The formal gluing row is not an actual interval counterexample. The full target stops unresolved. Independent checker SHA256:64f0b8772218c8fe2d95adf4808145c2259458d5420cc6101835d31e6f61d052.

<a id="avoidance-moments-final"></a>

## Principal avoidance moment review

Root read the full source-scope and five proofs plus each exact checker, then replayed all receipts. The first-forbidden-rank RSK obstruction covers every nonmonotone beta; maximum-insertion active-site collapse fails every length>=4 beta. The formal scalar sequence has all-n bounds and a negative higher-order quadratic form, consistently separated from actual avoidance. The exact full-state creation operator violates its normal-extension inequality on actual1324, while its root norm identity holds. The direct/skew renewal reduction is an all-size conditional equivalence, but its shifted indecomposable counts cannot be an ordinary permutation-class enumeration.

Five distinct sufficient constructions are accepted as failed full-target attempts. A2/A4 share insertion histories but obstruct a quotient rule versus positivity of the uncollapsed operator. Known Catalan/1342 and nonprincipal Fibonacci controls count zero additional attempts. Q1454 stops unresolved; none of these gives a negative actual principal-avoidance Hankel form.

<a id="random-graph-final"></a>

## Random graph independent review

Root read the independent proof/count review and full alternate minimum-element recursion and literal small-graph checker. The all-size fixed-d n^(2/5) Bonferroni prefix and O_(T,d)(1/n) fixed isolated-tree omission bounds pass. The five routes concern full-row bounds, real-rootedness, multivariate exchange/all weights, an actual random-model construction and componentwise convolution. Their failures do not refute the unweighted probability-limit question. Q2400 stops unresolved after five reviewed distinct failures. The exact144-row and small-graph receipt is independently replayed below; source-known tree26 is attributed, with its random-model isolated-component obstruction proved here.

<a id="dilation-final"></a>

## Common-color dilation review

Root read the complete new independent dilation review and checker and replayed22 canonical exclusions,1296 two-coordinate formula controls and eight literal-word/Ehrhart/inversion family rows. The dimension-matched forward dilation theorem is valid with leading-unit padding; the reverse primitive-ray implication fails at primitive colors(4,5) versus every(12t,15t). E06 is accepted as the replacement fifth substantive full-target failure. E01 remains explicitly rejected, without counting a finite recognizer rerun. Q1262 stops unresolved.

<a id="perazzo-final"></a>

## Perazzo rank and source-correction review

Root read the complete independent source/proof/count review and factorial-moment catalecticant checker, then replayed six flats,15 rank-Q quartics,four deformations and five nonzero generic minors. The restricted-pairing identity h_i=r_i+r_(d-i)+rankB_i is accepted, with all-degree flat and all-r quartic rank classifications. Both geometric propagation obstructions and the actual negative gamma certificate retain their stated scopes.

The cited final paper's universal minimum formula has an actual legal counterexample d4,m3,n4 with h=(1,8,8,8,1), below its predicted middle minimum10. The general derivative's fixed-q independence assertion also fails in the all-degree family. The latter does not exclude a smaller deconed Perazzo presentation. These are precise local source corrections, with no public communication or novelty claim. Five distinct full-target methods failed; Q2508 stops unresolved because the complete classification is still open.

<a id="circuit-final"></a>

## Circuit-polytope final review

Root read the primary Definition 2.2, direct-sum Remark 2.3, dimension
Remark 2.6 and Conjecture 3.11 in Escobar--McWhirter v2, then the complete
five-route packet and every exact checker. The saturated-span lattice,
sign normalization, known complete-graph family and prior at-most-seven-
element coverage agree with the primary scope.

The rank-one constant-term proof is valid coefficient by coefficient;
positive/negative root matching proves the gauge description, and Pascal
finite differences prove the binomial-square numerator. The simplex facet
obstructs a connected zonotope for every N>=4. For cographic K_N minus
one edge, all bond potentials except the deleted opposite pair remain.
The displayed N-1 facet vertices are affinely independent and its primitive
distance N-3 proves nonreflexivity at every N>=5.

The free-sum discrepancy is counted at exactly one dilate per nonintegral
gauge pair. Integer gauges in either factor remove all discrepancies.
Finite differences of the carry counts need not be coefficientwise positive.
The actual 18-element direct sum has numerator
(1,48,704,3128,5350,3372,800,52,1), different from the component product
and log-concave. Finally, the rank-two minimal dependence signs have sum
one, and the explicit determinant-one block basis proves full sign span
and saturated Z^N for every N>=4, rather than the flow kernel of dimension
N-2. None of these is an actual failure of the requested inequalities.

Root replayed all five checkers: eight root-family rows, 56 dense labelled
cographic graphs in four isomorphism types with complete exact facets,
seven primitive-distance controls, the entire dimension-eight direct-sum
row, and 17 determinant-one sign bases. Check receipts all pass. The
zonotope geometry, fresh actual counter-construction, reciprocal lattice
certificate, component carry reduction and realization conservation
contracts are distinct; A3/A4 share an explicitly disclosed factor.
Five substantive full-target failures are accepted. Q3678 stops unresolved;
no source replay or parameter count supplies additional attempts. The known
root-family proof retains its attribution, without a novelty claim.

<a id="koszul-final"></a>

## Koszul ordering final review

Root read the full independent Q3892-INDEPENDENT-REVIEW.md and its
separate squarefree apolar derivative-matrix checker, then replayed it.
The original pure flag hypotheses of D'Alì--Venturello Corollary 8.2
and Proposition 8.3 are retained. The shellable equal-part joins give
the exact Hilbert formula and every descending half-row for d>=3;
endpoints are one, not the doubled empty-face term. The all-permutation
claim remains open.

The approximate-face CM obstruction, equal-part ordering capacity,
fixed-seed tensor smoothing, nonnegative reciprocal insufficiency and
nonquadratic connected-sum relation have distinct full-target contracts.
The alternative-realization argument is valid: an m-primary quadratic
ideal contains a regular sequence of N quadrics, so its Artinian
quotient has no terms above degree N. The tested numerical rows have
socle degree N+2 and therefore admit no quadratic, hence no Koszul,
realization. A2/A3 share a known algebra family but fail at different
within-degree coverage and between-degree transport steps.

The independent receipt passes nine literal join apolar matrices, six
connected-sum matrices, 5,660 CM label-pair maximizations, 50 padding
rows, 89 order bounds and the exact reciprocal polynomial identity.
The all-size proofs, rather than these finite checks, establish the
retained partials and obstructions. All five substantive full-target
failures are accepted; Q3892 stops unresolved. No sixth route is begun,
and no novelty or external peer-review claim is made.

<a id="schur-midpoint-final"></a>

## Schur midpoint final review

Root read the full independent Q4665-INDEPENDENT-REVIEW.md and its
separate Jacobi--Trudi/Pieri checker, then replayed all 233 products
and all 32 exact rational-weight instances. The independent expansion
uses determinant permutations and horizontal-strip interlacing; the
submitted ballot-tableau code is called only for comparison. All
products, full differences and pairwise midpoint hypotheses agree.

The summed-fiber criterion, injective-support consequence (including
either singleton input), and nonnegative-alphabet evaluation theorem
hold at every size and padded length. The actual unit-budget collision
has a negative intermediate s_(1,1) coefficient, although the final
legal difference is Schur-positive. The formal evaluation obstruction
is not a legal four-function counterexample. Uniform joint rounding
leaves a fixed row-output LR domain at every N>=2 by total degree,
independently of tableau interior coordinates. Midpoint operations
cannot be conjugated to meet/join by a common injective chain relabeling;
a more elaborate auxiliary lift is not excluded.

The budget inference, operation transport, positivity-certificate
recovery, fixed-output closure and fresh weighted counter-construction
are five distinct full-target obligations. No numerical case, source
lookup or known-range replay supplies an extra count. All five failures
are accepted. Q4665 stops unresolved; the full Schur conjecture remains
open and the restricted support results are genuine partial scopes.
No sixth route, novelty or external peer-review claim is made.

<a id="boundary-final"></a>

## Boundary-polytope final review

Root read the complete crosspolytope proof, A1 forest-assembly obstruction,
exact checkers and literature-closure packet. The even binary-code lattice
classification and coset norm series prove the all-size gamma formula;
the actual triangle obstruction prevents the proposed whole-forest assembly.
The independent code-family controls and RP2 boundary/minor calibration pass.
A1 is accepted as one failed full-target route; the restricted theorem remains
valid and is not counted as another attempt.

Root read [Ferroni's primary preprint](https://arxiv.org/html/2607.02424v1),
including its construction, dissection argument and complete certificate,
and [Kálmán--Tóthmérész Example 1.1 and Theorem 1.2](https://arxiv.org/html/2203.17127v4).
The latter supplies the planar-dual dissection and away-edge identity;
Ferroni's theorem-number reference differs without changing the statement.
The five length-eight paths give an actual simple graph with 37 vertices
and 40 edges. Its incidence polytope is exactly a homology polytope in
the saturated sum-zero lattice of dimension 36. The spanning-tree integral
basis and tight-potential polar argument verify reflexivity in this lattice.
The exact marked-word reconstruction matches the complete published numerator;
two gamma inversions agree, with gamma_16=-9799680 and zero re-expansion
residual. Root replayed the 18,432 word controls and eight literal small
Ehrhart rows. The large numerator uses the audited primary dissection theorem,
not a direct 36-dimensional lattice-point enumeration.

The full frozen universal Q3902 assertion is therefore disproved through
its homology branch, with explicit literature attribution and no local
counterexample-discovery claim. The standalone cohomology assertion and
source Question 9.3 about subcomplex reflexivity remain outside this closure.
The source lookup counts zero failures. One earlier failure is preserved;
further solving stops because the target is resolved. Checker SHA256:
043c9aeec7a2b94d555616562e0742321af5cff96a09e7fd27447a3558003fbb.
