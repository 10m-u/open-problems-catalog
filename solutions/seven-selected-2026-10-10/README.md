# Seven selected problems: proofs, a counterexample, and partial classifications

**Research date: 2026-10-10.** This round contains four proposed affirmative
resolutions, one proposed counterexample, and two proved partial classifications.
Each result has a separate internal AI proof review, dated primary-source and
later-literature checks, and reproducible computational controls. None has
external peer review or formal proof certification. The catalog's `proved` and
`disproved` labels record proposed resolutions at the scope specified below.

The seven entries were open at base commit
`322939ded7f14279544590a46e7917abbcc96942`. Their original statements and sources
are preserved. [RESULTS.json](RESULTS.json) is the scope and artifact manifest.

## Results and remaining scope

| Problem | Result | Catalog status | Scope boundary |
| --- | --- | --- | --- |
| [Q212](../../problems/mathematics/algebra-representation-theory-part-1.md#q212) | [Explicit primitive-idempotent counterexample](algebra/212.md) in $M_2(k[t^2,t^3])$. | Disproved | Resolves the stated locally finite nonnegative-grading question. The stricter standard-grading variant remains outside the result. |
| [Q726](../../problems/mathematics/optimization-operations-research.md#q726) | [Unrestricted MaxMinLCB regret proof](learning/Q726.md), with the original confidence coefficients. | Proved | Retains the source's bounded estimator and prescribed projection convention; uses exact optimization and includes all ties. |
| [Q3840](../../problems/mathematics/combinatorics-graph-theory-part-3.md#q3840) | [Complete circumference-five cylinder classification](discrete/Q3840.md): existence exactly for $m=3,5,7$ or $m\ge9$. | Partial | Positive covering families are included; the general odd-circumference classification remains unresolved. |
| [Q3841](../../problems/mathematics/combinatorics-graph-theory-part-3.md#q3841) | [Complete circumference-five torus classification](discrete/Q3841.md): for odd $m\ge5$, existence exactly when $m\ge7$. | Partial | Positive covering families are included; the case of two arbitrary odd circumferences at least seven remains unresolved. |
| [Q3893](../../problems/mathematics/algebra-representation-theory-part-2.md#q3893) | [Whiskered-graph WLP failure](algebra/3893.md) over every field. | Proved | Uses complete whiskering and the source's square relations; every linear form fails in one specified degree. |
| [Q3982](../../problems/mathematics/probability-stochastic-processes-part-2.md#q3982) | [Conditioned Brownian limit](probability/brownian_l2_drift.md) for every $\mu(T)^2=o(T)$. | Proved | The source's deterministic norm threshold and time-constant drift within each path are retained. |
| [Q3983](../../problems/mathematics/probability-stochastic-processes-part-2.md#q3983) | [Explicit critical-drift limit](probability/brownian_l2_drift.md) for $\mu(T)\sim c\sqrt T$. | Proved | Convergence holds on fixed initial intervals and in the requested path topology; no terminal-window or diverging-ratio assertion. |

## Main mathematical arguments

### Q212: an obstruction preserved by every automorphism

For $R=k[t^2,t^3]$ and $A=M_2(R)$, the proof constructs complementary
primitive idempotents $e,f$ by conjugating constant matrix idempotents over
$k[t]$. The resulting matrices lie in $A$, but their cross-corner is the
central module

$$
eAf\cong\{u\in k[t]:u'(0)=-2u(0)\}.
$$

This module is not free of rank one over $R$. Every homogeneous primitive
idempotent in this grading has a free complementary cross-corner. An arbitrary
algebra automorphism may act nontrivially on the center, but its induced
semilinear bijection still preserves freeness. This supplies the obstruction
for all automorphisms, beyond conjugation by units. Characteristic zero
provides a counterexample within the source's hypotheses.

### Q726: control of both queried actions without the plausible-maximizer set

The posterior uncertainty on a duel is a pseudometric because its feature
vector is a difference of action features. The triangle inequality and the
positive lower bound on the logistic derivative over the source's bounded
score range control the follower's fitted advantage over the leader. The
uniform confidence event then bounds the true regret of each queried action
by a constant times the selected duel's uncertainty. Summing through the
information-gain determinant identity yields

$$
R_T^D=O_{B,\lambda,\kappa}
\left(\beta_T^D(\delta)\sqrt{T\gamma_T^D}\right)
$$

simultaneously for all horizons, with probability at least $1-\delta$.
Both optimization domains are the full action space. The source's estimator
and confidence construction remain in force, including Appendix A's
prescribed gradient-space projection when needed to meet the norm bound.
The result makes no computational-efficiency claim for solving the max-min
problem on a continuous action space.

### Q3840 and Q3841: exact finite obstructions and constructive infinite tails

A five-bit row records membership in a proposed proper total dominating set.
Three consecutive rows determine the middle row's neighbor counts. The exact
transfer graph has 4,310 legal states and 10,800 arcs. Endpoint conditions give
cylinders; closed walks give tori. Exhaustive traversal proves the finite
nonexistence cases. Separately checked membership patterns and an explicit
two-row insertion lemma prove every claimed positive length, without
extrapolating from finite samples. Graph coverings extend these constructions
to odd circumferences divisible by five. The nonexistence claims are confined
to circumference five.

### Q3893: a kernel and a cokernel in the same degree

The shear $y_i\mapsto y_i-x_i$ is an automorphism of the square-truncated
whiskered-graph algebra and sends $\sum_i(x_i+y_i)$ to $\sum_i y_i$.
The monomial basis splits into invariant summands indexed by independent
sets of original vertices. In degree $d=\lceil n/2\rceil$, the empty-set
summand forces a kernel while an independent-triple summand forces a
cokernel. Both occur in the map $A_d\to A_{d+1}$, so its rank is below
both dimensions. Diagonal rescaling and an open-minor argument over the
algebraic closure cover every linear form and every ground field.

The proof also supplies explicit coordinate certificates. Its cokernel
construction is attributed to the source's Theorem 3.10; the simultaneous
kernel obstruction and invariant-summand argument complete the resolution.

### Q3982 and Q3983: one moving-saddle theorem

The unified result treats every finite limit $\mu(T)^2/T\to r\ge0$.
The limiting process is

$$
dX_t=dB_t-\lambda_rX_t\,dt,\qquad X_0=x,
\qquad 2\theta\lambda_r^3-\lambda_r^2-r=0,
$$

where $\lambda_r$ is the unique positive root. Thus Q3982 has
$\lambda_0=1/(2\theta)$, and Q3983 has $r=c^2$, independently of the sign
of $c$. The proof derives an exact endpoint-tilted Mehler transform, controls
its moving saddle over the full inversion contour, and identifies the limit
of conditional densities. Martingale normalization and Scheffe's lemma yield
total variation convergence on each fixed initial interval, which implies
the requested weak convergence on $C([0,\infty))$ with uniform convergence
on compact intervals.

## Independent review and source records

| Problems | Independent internal review | Dated source check |
| --- | --- | --- |
| Q212 | [Algebra proof review](discrete/review-Q212.md) | [Algebra sources](algebra/SOURCES.md) |
| Q726 | [Learning proof review](algebra/review-Q726.md) | [Learning sources](learning/SOURCES.md) |
| Q3840, Q3841 | [Transfer, construction, and independent-enumeration review](probability/review-Q3840-Q3841.md) | [Graph sources](discrete/sources.md) |
| Q3893 | [Algebra proof and independent-matrix review](discrete/review-Q3893.md) | [Algebra sources](algebra/SOURCES.md) |
| Q3982, Q3983 | [Transform, full-contour, and change-of-measure review](reviews/Q3982-Q3983.md) | [Probability sources](probability/sources.json) |

Each reviewer was separate from the author of the corresponding argument.
No blocking mathematical issue remained after review. Source checks verify
the exact statements, assumptions, and inspected versions; later searches
are bounded evidence and do not certify novelty. Original source texts are
linked and are not copied into this repository.

## Reproduce the checks

Run from the repository root, with Python 3 and assertions enabled:

```sh
python solutions/seven-selected-2026-10-10/run_checks.py
python solutions/seven-selected-2026-10-10/validate_catalog.py
```

These commands require only the Python standard library. The recorded
[verification report](verification.json) and [catalog validation report](catalog-validation.json)
cover the following controls:

| Area | Controls |
| --- | --- |
| Q212 | Exact integer polynomial identities, primitive-corner reductions, cross-corner coefficient conditions, and a Bezout certificate. |
| Q726 | 4,617 exact finite scenarios, all 6,726 optimizing pairs, 200 feature/kernel posterior comparisons, 1,000 squared triangle tests, and eight determinant identities. A deliberately nonmetric negative control fails the claimed bound, confirming that the hypothesis matters. |
| Q3840, Q3841 | Complete transfer graph, exact boundary and closed-walk certificates, direct graph-neighborhood checks of all seeds and insertion controls; a separately written row-word enumerator confirms the small obstructions. |
| Q3893 | Exact kernel/cokernel certificates for 48 graphs, shear identities on 1,745 basis monomials, and independent multiplication-matrix ranks over three finite fields. |
| Q3982, Q3983 | 25 exact saddle-series cases, 150 exact contour cases, and 125 exact generator cases. |
| Catalog | Only the selected seven entries change; JSON, CSV, full pages, overview tables, number indices, aggregate counts, and artifact links agree. Original statements and source metadata remain intact. |

Optional Brownian diagnostics use NumPy and SciPy:

```sh
python solutions/seven-selected-2026-10-10/run_checks.py --numeric
```

They compare the transform with independent Karhunen-Loeve products and
perform twelve contour inversions across zero, subcritical, and positive
and negative critical drifts. These floating-point diagnostics are
supplementary checks, with no interval-arithmetic or formal-certification
claim. The mathematical proof does not rely on them.

The catalog validator compares against the stated base commit. A shallow
clone must include that commit to run the unchanged-entry comparison.
