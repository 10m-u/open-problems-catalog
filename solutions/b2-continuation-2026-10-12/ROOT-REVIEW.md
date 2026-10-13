# Main-thread B2 proof, route and scope review

This review covers the current 81 catalog targets and A-TRANSFER as defined in
[CONTROL.md](CONTROL.md). It is an internal review, with no external peer-review
or novelty claim. Completion of this research run requires every target to be
locally solved or to have five substantive failed full-target attempts, followed
by filing and preservation checks. A restricted theorem does not close its
catalog question or reset its counter. [STATUS.json](STATUS.json) records the
current dispositions; this review is not itself a declaration of overall completion.

<a id="root-routes"></a>
## Root's 71 catalog targets

The main thread has read all twenty-two root attempt packets, including the
explicit constructions, reductions, algorithms and remaining obligations.
Each target has five numbered routes. These are failed attempts to solve the
full target, not five impossibility theorems. Finite searches stop at their
declared domains; fixed-curve finiteness, conditional inputs, density-one
statements and source subfamilies are never promoted to universal closure.
Source retrieval, command errors and service interruptions are excluded.

| Packet | Targets | Review and evidence |
|---|---|---|
| [SEQUENCE-ATTEMPTS](arithmetic/SEQUENCE-ATTEMPTS.md) | Q2613, Q3715, Q3314, Q4196, Q4585, Q4580, Q4190 | Exact Catalan digit criterion, signed two-factor exclusion, prime cycles and failed seed augmentation have their stated scopes. [Independent retained-agent review](paley/ROOT-DIGIT-SEQUENCE-REVIEW.md). |
| [POLYNOMIAL-DIGIT-ATTEMPTS](arithmetic/POLYNOMIAL-DIGIT-ATTEMPTS.md) | Q1612, Q1613 | Fixed-prime coefficient-carry automata and weighted-cycle decision are valid; no all-prime cycle exclusion is supplied. Independent review above and direct multiplication controls. |
| [POWER-EQUATION-ATTEMPTS](arithmetic/POWER-EQUATION-ATTEMPTS.md) | Q1511, Q1608–Q1611 | Kernel collisions and Pell/twist reductions are exact. Quartic sign and common-base restrictions stay explicit. Source cases and finite checks do not close unrestricted exponents or bases. |
| [TORSION-UNIT-ATTEMPTS](arithmetic/TORSION-UNIT-ATTEMPTS.md) | Q2307–Q2309, Q2010, Q2011, Q3603 | Visible torsion does not certify rank; the section-forcing cover has genus three. Unit clique and varying-field quantifiers remain open. |
| [ANALYTIC-ATTEMPTS](arithmetic/ANALYTIC-ATTEMPTS.md) | Q1312, Q1509, Q1510, Q2904–Q2907 | Sieve tails, sparse digit populations, Wieferich/order conditions and inverse cyclotomic height expose precise missing estimates. No heuristic or conditional statement is filed as a proof. |
| [FACTOR-ATTEMPTS](arithmetic/FACTOR-ATTEMPTS.md) | Q2414, Q2415 | Reciprocal factors are cyclotomic in product-plus-one and unequal-degree sums; remaining-factor irreducibility is not implied. Constant-prime countercontrols and finite factorization boxes are correctly scoped. |
| [SMOOTHNESS-ATTEMPTS](arithmetic/SMOOTHNESS-ATTEMPTS.md) | Q3113 | Complete constructive linear-polynomial theorem, including negative leading coefficient and zero constant. Higher degree is unresolved. |
| [SHIFT-ATTEMPTS](arithmetic/SHIFT-ATTEMPTS.md) | Q3107, Q3109, Q3110 | Pairwise independence is tested separately from triple rank. Source a=2 exclusion and fixed-exponent template obstruction have distinct scopes. |
| [SMALL-EQUATIONS-ATTEMPTS](diophantine/SMALL-EQUATIONS-ATTEMPTS.md) | Q2314–Q2316 | Polynomial orbit/density and local points do not imply global coverage or existence. Q2316's divisor certificate excludes a small coordinate with other coordinates unrestricted. |
| [TUPLE-ATTEMPTS](diophantine/TUPLE-ATTEMPTS.md) | Q1903–Q1908, Q2306 | Multiquadratic genera and the exact two-sided integral-rescaling criterion check out; rational/strong/integral requirements are distinguished. Corrected source witness denominator is preserved. |
| [SQUARE-SUM-ATTEMPTS](diophantine/SQUARE-SUM-ATTEMPTS.md) | Q3208 | Complete integer nonextension of the specified four-by-four seed. It does not exclude rational neighbors or extensions after squared scaling. |
| [RESONANCE-ATTEMPTS](diophantine/RESONANCE-ATTEMPTS.md) | Q49 | Common-kernel reduction and positive polynomial index inequality are valid; no uniform twist or height bound follows. |
| [PARTITION-ATTEMPTS](arithmetic/PARTITION-ATTEMPTS.md) | Q4642, Q4643 | Conjugation-fixed partitions yield the locally finite parity Euler product. Unit orbits repeat one count and do not provide distinct values. |
| [UNCOLOURED-ATTEMPTS](arithmetic/UNCOLOURED-ATTEMPTS.md) | Q4295, Q4296 | Conflict-graph equivalence and the exact one-colour dimension n−1 theorem are valid. Neither gives the requested all-parameter sharp functions. |
| [SUMSET-ROOT-ATTEMPTS](arithmetic/SUMSET-ROOT-ATTEMPTS.md) | Q4302 | Exponent gap, forbidden mixed sums and Boolean Fourier-root obstruction are explicit. Small cyclic anomalies do not refute asymptotic bounds. |
| [ENTROPY-ATTEMPTS](arithmetic/ENTROPY-ATTEMPTS.md) | Q4659, Q4660 | Weighted laws, support cardinalities and the real-valued domain are distinguished. The Bernoulli lower bound is certified by integer inequalities; a small numerical optimization is not a global bound. |
| [RELATIVE-DAVENPORT-ATTEMPTS](arithmetic/RELATIVE-DAVENPORT-ATTEMPTS.md) | Q3116, Q3117, Q3466 | Subset-sum states form an exact finite DAG. Nonunit maps and quotient projections lose admissibility; conductor and weighted invariant distinctions remain. |
| [APPROXIMATE-SQUARE-ATTEMPTS](diophantine/APPROXIMATE-SQUARE-ATTEMPTS.md) | Q2215 | Two fixed shifts prove finite-summand exclusion and the necessary Ω(X^(1/4)) error scale. Sparse infinite/infinite decompositions are not excluded. |
| [BIPARTITE-SQUARE-ATTEMPTS](diophantine/BIPARTITE-SQUARE-ATTEMPTS.md) | Q2216 | Four-row cover genus five and two-row Pell countercontrols are correct. Uniformity remains conditional and clique bounds do not apply to a bipartite graph. |
| [RAMSEY-ATTEMPTS](arithmetic/RAMSEY-ATTEMPTS.md) | Q2203, Q2462, Q2468, Q2469 | Valuation colouring proves the two-variable boundary, single intervals fail the mixed-coefficient small-independence requirement, and RCA₀ proves three-colour single-difference avoidance. Exact finite countercontrols distinguish all four universal targets. |
| [NUMBER-THEORY-ATTEMPTS](arithmetic/NUMBER-THEORY-ATTEMPTS.md) | Q2616, Q2814–Q2817 | Source elasticity∞ subcase, exact moment identity, powerful progression/scaling intruders and unit-index size distinctions are scoped. Independent finite enumerations do not certify logarithmic growth or asymptotic constants. |
| [MONOID-ATTEMPTS](arithmetic/MONOID-ATTEMPTS.md) | Q2008, Q2210, Q2213, Q2217, Q2617 | Coherent prime-class selection is not implied by countable realizations. Exact two-point length sets are sourced; mixed factor/union controls pass. The all-prime reciprocal monoid has finite residual divisor sets and MCDs, hence atomic power monoid. Complete S3 multiset checks prove d=3 and E=9. Graded domains are BF; the well-founded non-BF monoid is not finitely generated and is not a claimed ring counterexample. |

Shared ingredients are disclosed: Q4196 routes 2/4/5 reuse a least-factor cycle
for three different mechanisms; Q3715's finite-digit and cross-base arguments
have different obligations; paired plus/minus power routes share valuation
and twist issues but count separately per exact target. Factorization boxes
are shared across Q2414/Q2415. Q3107/Q3110 product templates overlap at a
different target. Q2215's fixed-gap proof and failed two-translate construction
use one identity for opposite tasks. These are not claims of independence.

Corrections retained in the files include the seven-divisor progression's
Ω(S^7) lower bound; the actual p=3 coefficient-cancellation example; the
elliptic twist powers of d; 2223/30464 in the strong-tuple source witness;
25922=2·13·997; and Q3208's rational-versus-integer scaling limit. Corrections
repair an existing route and do not add or reset a failure.

The Q4660 finite-law route has also been converted from a floating-point
candidate to an exact rational law. Positive atanh-series logarithm intervals
certify an entropy-increment ratio above139/100. This verifies one already
counted construction and neither reopens the stopped question nor adds a
sixth route. The script and exact scaled intervals are retained in
[CERTIFIED-LAW-CHECK.json](arithmetic/CERTIFIED-LAW-CHECK.json).

<a id="transfer"></a>
## A-TRANSFER

[INDICATOR-CONCENTRATION.md](paley/INDICATOR-CONCENTRATION.md) proves the
defined broader target. Centering removes the constant component. Additive
coefficient caps, the separate origin contrast, and nontrivial multiplicative
caps give uniform approximate-concentration inequalities. The point mass at
zero is treated explicitly and cannot be inserted into the restricted
F_p^* formula. The small-support product bound improves the flat exact-support
baseline in the specified density regime; its assumptions do not resolve the
catalog Paley questions. The proof and exhaustive finite controls were read
and accepted by the main thread in the preceding research round.

<a id="paley"></a>
## Five Paley questions

Q2187–Q2191 each have five accepted full-target failed routes. The main thread
read their proof/reduction packets, exact rational theta certificates,
conference-matrix controls and signed-square dual constructions in the
preceding round. Q2189's finite relaxation gaps refute particular transfers,
not the requested asymptotic theta estimate. Q2190's irregular degree and
noncommuting symmetry models explain why scalar certificates fail. Negative
pseudo-conditioning witnesses concern their stated moment degree. Neither
bounded computations nor random-support averages are worst-support RIP proofs.

<a id="cubes"></a>
## Cube-free families

Q1959–Q1961 each have five reviewed failed routes. The main thread read all
three packets, the exact checker and CUBE-CHECK-RESULTS.json. The 17/24
fractional cube-hyperedge construction obstructs that linear relaxation.
Q1960's diagonal-progression counterexample refutes an auxiliary sufficient
lemma; it contains a genuine mixed cube, so it is not a catalog counterexample.
Q1961's high-odd-density branch proves the five-eighths bound in that branch,
while its intermediate-density interval remains open. The small cyclic
maxima and four-translate countercontrols have their exact scopes.

<a id="colouring"></a>
## Rainbow colourings

Both Q1860 and Q1861 have five accepted failed routes. The main thread read
the two attempt packets, PARITY-OPTIMUM.md, TWO-PREFIX.md, and the passed
COLOUR-CHECK-RESULTS.json receipt. The parity-class proof is valid: weak
compactness and the compact kernel give a relaxed maximizer; first variation
and the zero-level-set derivative fact conserve the reflected-gradient
diamond. Nonflat endpoint motion forces q=1/(12j+11), hence maximum 9/22.
The cell discretization error is uniform even for arbitrary odd colour sets.
No reduction of unrestricted colourings to this class has been proved.

The two-prefix palette family has exact optimum 3/7, and the tested uniform
parity refinements have best density 60/121. Both are below the preserved
50368/90905 return bound. Carry dilation, scalar increment inequalities and
translated-copy assembly fail at different explicit obligations; their
relationship is disclosed. An abstract nonconvergent count sequence is not
asserted to be realized by colourings. The source paper was rechecked at
its primary arXiv page on resumption; its stated bounds agree with the packet.

## Final factorization review and provenance

The main thread completed the final five catalog targets and read the exact
cached statements and primary setup before selecting routes. Their 25 routes
include explicit failed constructions and missing proof obligations, with
shared C3 and divisor mechanisms disclosed. The reciprocal-prime normal form
has nonnegative carries; subtracting the smallest integer part leaves an
element with a finite divisor set, yielding an MCD for every finite subset.
The sourced atomic-MCD ascent theorem then rules out this entire candidate.
Pointwise atomic finite support is not confused with power atomicity.

The complete bounded power-set algorithm grades by additive maximum and covers
all 4,096 normalized sets through maximum twelve, with 10,272 unordered
decompositions. The S3 checker retains every ordering product for each candidate
submultiset; it checks all 126 length-four and 2,002 length-nine multisets, with
the necessary length-three and length-eight witnesses. This is exact finite
proof, within known group families, without a universal Gao-Zhuang result.
The non-BF monoid's normal form proves ACCP by a nonincreasing integer budget
and coordinatewise descent between budget decreases. Its infinite rank blocks
finite algebra generation; monoid ACCP is not silently transferred to its ring.

The retained agent remains the same identity. Its earlier ten catalog packets
and A-TRANSFER are accepted as reviewed above. Its initialization delay prevented
a fresh audit of these last root proofs; the new route and mathematical checks
were completed in the main thread. No fresh retained-agent review is claimed.
Neither this delay nor source retrieval counts as a failed mathematical attempt.

All 81 catalog targets now have five substantive failed full-target routes;
A-TRANSFER is solved locally. Canonical filing and final preservation checks
passed on 13 October 2026, completing this run under the per-target rule.
[RESULTS.json](RESULTS.json) contains 29 scoped records;
[FILE-VALIDATION.json](FILE-VALIDATION.json) checks all 405 written attempts,
five new partial marks, every prior ledger decision and original corpus field.
The original verification archive is still absent;
new checker receipts do not recover it. The separately authorized B14 return
intake adds six routes and preserves the original ledger/corpus; B2's final
validation explicitly reconciles that addition rather than changing its baseline.
