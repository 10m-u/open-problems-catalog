# Seven further open problems: proofs, counterexamples and partial results

Date: 2026-10-09. Base commit: `b75acbb7671a16ac38e8f41656b92f211dce5f4a`.

This round investigates seven entries that were open and had no repository
results at the base commit. It adds two proposed affirmative resolutions,
two counterexamples and three partial results. The selected problems are
distinct from those already added in `solutions/seven-problems-2026-10-09/`.

**Evidence:** each result has a written mathematical argument, exact executable
controls or certificates, a dated source check, and a review by a separate
internal AI research agent. These are proposed research results, not externally
peer-reviewed or formally certified theorems. Finite controls establish only
the scopes proved in the reports. Dated literature searches do not certify
novelty.

## Catalog update package

The complete catalog edits are supplied in [catalog-update.patch](catalog-update.patch),
with before/after file hashes in [CATALOG_PATCH.json](CATALOG_PATCH.json).
The publication upload of the 7.7 MB catalog replacement stalled; this compact
patch preserves all validated changes to the seven entries, their detailed
pages, indexes and totals. The published catalog retains its base values until
the patch is applied. The statuses in the table below are the proposed values.

Apply the update from the repository root with:

```sh
python solutions/seven-more-2026-10-09/apply_catalog_update.py
python solutions/seven-more-2026-10-09/validate_catalog.py
```

The application command verifies the patch and all 16 target file hashes,
preserves exact bytes and line endings, accepts an already-applied update,
and refuses edited or partly updated target files. It does not stage or commit
changes. Add `--check` for a dry run. The patch was applied and validated in
a disposable worktree before publication.

## Results

| Problem | Result | Catalog status |
|---|---|---|
| [Q276](../../problems/mathematics/probability-stochastic-processes-part-1.md#q276) | Stochastic monotonicity of constant-freezing percolation on every finite simple graph whose connected components have at most five edges, for all positive rates. | Partial |
| [Q277](../../problems/mathematics/probability-stochastic-processes-part-1.md#q277) | Positive association on every finite simple graph whose connected components have at most four edges, for every positive rate. | Partial |
| [Q964](../../problems/mathematics/optimization-operations-research.md#q964) | Worst-case expected regret `O_{K,c}(T^(4/5)(log T)^(1/5))` for known `lambda=c/T`, fixed `K,c`, against the full informed action-sequence benchmark. | Proved, proposed complete affirmative answer |
| [Q1715](../../problems/mathematics/algebra-representation-theory-part-1.md#q1715) | A 13-dimensional, class-five, two-generated nilpotent Lie algebra has property F for every generating pair but is not free nilpotent. | Disproved by an explicit counterexample |
| [Q2305](../../problems/mathematics/algebra-representation-theory-part-1.md#q2305) | An explicit isomorphism model for partial inner automorphisms of `End_F(V)` for every field and finite dimension, including equality, composition and inversion. | Proved, proposed complete affirmative answer |
| [Q3480](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3480) | A finite automaton for each fixed alphabet, exact matrix counting, and a rational generating function with asymptotics for the four-symbol Cayley-word slice. | Partial |
| [Q3499](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3499) | The full face lattice of a 13-gon has Ehrhart linear coefficient `-298495711/35302608`. | Disproved by an exact counterexample |

The general questions Q276 and Q277 and the unrestricted enumeration target
in Q3480 remain unresolved. The `proved` and `disproved` statuses use the
repository's convention for results obtained here, at the stated scope.

## Mathematical contributions

### Freezing-process questions: Q276 and Q277

The [joint proof](probability/Q276-Q277-proof.md) gives a terminating recursion
for the final edge law. It represents each atom by an integer polynomial over
a positive common denominator. Every increasing-event derivative in the first
scope and every event-pair covariance in the second scope has the needed
coefficient sign, proving the inequalities for all positive real parameters.
Independence between components extends each finite list of connected graphs
to graphs of arbitrary total size satisfying the component bound.

The proof certifies 91,881 derivative polynomials and 71,637 covariance
polynomials. An independent full-clock Markov computation checks the laws
at three exact rational parameters. The four-vertex path fails the stronger
FKG lattice condition by `-1/525` at rate one; that negative control guards
against confusing the lattice condition with positive association.

### Learning with horizon-scale memory: Q964

The [learning proof](learning/Q964-proof.md) uses short transient experiments
before the latent state has moved far from one. A reference arm probes the
change caused by each other arm, while a separate calibration removes the
reference arm's own state effect. The argument bounds reward-weighted
end-state error, so it does not assume a positive lower bound on arm rewards.

The policy charges both the exploration rounds and their continuing effect on
the state. Its comparison uses the original full-horizon informed sequence
optimum, with no multiplicative discount. An explicit state-grid planner has
an additive error at most one half. The rate is an existence guarantee; no
optimal exponent, growing-arm bound or unknown-rate result is asserted.
The exact [reference implementation](learning/q964.py) is intended for
reproducibility. Its conservative exploration budget and cubic planner are
not optimized for practical horizons.

### Algebra: Q1715 and Q2305

The [Q1715 counterexample](algebra/Q1715.md) is given by an integer bracket
table. Three injective maps between homogeneous layers establish property F
for the displayed generators. A symmetric-matrix change-of-basis argument
and lowest-degree induction extend the result to every generating pair over
every characteristic-zero field. Its dimension distinguishes it from the
free two-generated class-five Lie algebra.

The [Q2305 proof](algebra/Q2305.md) shows that every original partial-inner
generator extends to invertible conjugation. Its possible domains are the
full matrix space, the zero-matrix singleton, and rectangular spaces
`D(U,W)={a: im(a) ⊆ U, W ⊆ ker(a)}` with `U,W` both proper and nonzero.
Explicit formulas identify representatives and compose or invert them.
The inverse-monoid zero is the identity on `{0}`. The proof covers arbitrary
fields and dimensions, including nonsemisimple products.

### Discrete enumeration: Q3480 and Q3499

The [Q3480 report](discrete/Q3480-proof.md) compresses equal runs in two hare
stacks while preserving the detection of an output inversion. This yields a
finite automaton for each fixed alphabet. For sortable Cayley words using
exactly four symbols, the generating function is

\[
\frac{z^4(22-119z+162z^2)}{(1-z)(1-2z)(1-3z)^4},
\]

and the number of length-n words is asymptotic to `n^3*3^n/324`. The general
matrix formula has exponential dependence on alphabet size and is retained
as partial progress on the unrestricted enumeration problem.

The [Q3499 counterexample](discrete/Q3499-proof.md) derives an exact transfer
matrix count of lattice points and uses two separate methods to extract
the linear Ehrhart coefficient for the 13-gon. Both include the empty face
and the whole polygon and distinguish the Ehrhart polynomial from the
source's shifted order polynomial. All coefficients are positive for polygon
sizes three through twelve, so thirteen is the first failure in this family.

## Reproduce

Only Python 3.10 or later and its standard library are needed. From the
repository root:

```sh
python solutions/seven-more-2026-10-09/run_all.py
python solutions/seven-more-2026-10-09/check_catalog_patch.py
git -c core.whitespace=cr-at-eol diff --check
```

The runner regenerates the certificates, runs the separately written discrete
verifiers and the independent graph/event enumeration control, and records
hashes in [verification-summary.json](verification-summary.json).
The patch checker creates a disposable worktree at the pinned base, applies
the exact catalog update, and runs the integration validator there. It also
checks dry-run behavior, idempotence and rejection of edited targets. The
validator permits changes to exactly the seven selected entries and checks
source preservation, linked evidence, statuses and counts.

| Mathematical controls | Coverage |
|---|---|
| Freezing process | 22 connected graph classes; 91,881 derivative and 71,637 covariance certificates; 66 full-law cross-checks |
| Q964 learning | 12,096 state inequalities; 252 matched offsets; 144 estimator cases; 512 clipping cases; 108 planner/exhaustive comparisons; 324 tail-state comparisons |
| Q1715 Lie algebra | All 2,197 ordered basis Jacobi triples; exact central-series/center calculations; ranks 3, 6 and 9; a noncentral-solution negative control |
| Q2305 matrix monoids | All generator pairs and generated maps in `M_2(F_2)` and `M_2(F_3)`; 198 generated domains in `M_3(F_2)`; singular/nonsemisimple controls |
| Q3480 and Q3499 | Independent literal-stack/automaton and integer-matrix/interpolation verification; source-sequence and order-polynomial shift controls |

## Reviews and sources

Separate reviews are linked in [RESULTS.json](RESULTS.json):
[Q276/Q277](reviews/review-Q276-Q277.md), [Q964](learning/review-Q964.md),
[Q1715](discrete/review-Q1715.md), [Q2305](discrete/review-Q2305.md),
[Q3480](algebra/review-Q3480.md), and [Q3499](algebra/review-Q3499.md).

Source checks are logged by group:
[probability](probability/source-log.md), [learning](learning/SOURCES.md),
[algebra](algebra/sources.md), and [discrete](discrete/SOURCES.md).
The Cambridge thesis route for Q276/Q277 was inaccessible; the author's
available primary paper was read and supplies both exact questions and the
model. No copyrighted source texts, PDFs, or dependency directories are included.
