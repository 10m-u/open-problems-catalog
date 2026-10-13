# B1 continuation — 12 October 2026

The all-target run is complete under the user's stopping rule: each problem
is solved or stops at five consecutive substantive failed solve attempts.
All 30 current catalog questions and four broader programme targets were
covered, using the retained /root/b14_local_optima agent.

There are four positive terminal targets: retained Q2168, newly proved
Q2777, the exact all-ones Fourier maximum, and the executable fixed-circuit
proof lane. The other 28 catalog questions and two broader targets each
stop at five failures. **Stopped questions remain unresolved.** Partial
results do not reset counters, and failed commands, lookups and service
interruptions do not count.

[STATUS.json](STATUS.json) records every target, its exact statement and
its numbered routes. [CONTROL.md](CONTROL.md) fixes the scope;
QUESTION-SNAPSHOT.json preserves all 30 current
IDs and source contexts. Original accepted classifications, reports and
ledger decisions remain intact. The original missing verification archive
has not been reconstructed or claimed recovered.

## Results and exact limits

| Target | Outcome | Evidence |
|---|---|---|
| Q2168 | Prior exact SC=Σ4 Presburger group construction retained and audited | [Audit](model-theory/ATTEMPTS.md) |
| Q2777 | Every finite total-size GP² spectrum is semilinear; no effective representation promised | [Proof](gp2/Q2777-RESULT.md), [review](gp2/Q2777-ROOT-REVIEW.md) |
| All-ones column | Exact product maximum, realizing frequency and asymptotic rate at every positive width | [Proof](fourier/ALL-ONES.md), [independent review](gp2/ALL-ONES-REVIEW.md) |
| Automatic-proof lane | All-width identity certificates and a compiler for arbitrary fixed acyclic modular-addition/Boolean circuits | [Result](automatic-proofs/RESULT.md), [compiler](automatic-proofs/circuits.py) |
| Q2778 | Decidable homogeneous globals and one-sided positive-surplus bounds; arbitrary affine globals unresolved | [Reduction and five routes](gp2/Q2778-ATTEMPTS.md), [review](gp2/Q2778-ROOT-REVIEW.md) |
| Q2978 / Q2980 | Full-signature two-block truth is c.e.; {n2^n} is not binary automatic; full theories unresolved | [Arithmetic packet](arithmetic/ATTEMPTS.md) |
| Overlap tail | Exact finite block-mixture law, fourth moment and rigorous tail bounds; sharp large-width tail unresolved | [Result and five routes](fourier/DISTRIBUTION.md), [independent review](foundations/DISTRIBUTION-REVIEW.md) |
| Sharp entropy | Exact direct-sum reduction; coherence bounds and saved candidate upper bounds; full constants unresolved | [Reduction and five routes](fourier/ENTROPY.md) |
| Q3824 trees | Original-variable, addition-only CP refutations for tree Tseitin instances; all graphs unresolved | [Routes](proof-complexity/ATTEMPTS.md), [checked certificate](proof-complexity/TREE-CP-CERTIFICATE.json) |
| Foundations restrictions | New finite-core models, uniform-section and finite-expansion obstructions, and homogeneous shatter-growth transfer | [Q1377](foundations/Q1377-ATTEMPTS.md), [Q1378](foundations/Q1378-ATTEMPTS.md), [Q1979](foundations/Q1979-ATTEMPTS.md) |

The entropy note now treats its B2 expression as a verified attainable
upper bound. Matching a local numerical search does not certify a global
minimum or width independence. Inverse inquiries
04 and
25
carry the resulting updates and corrected scope.

## Failed-route packets

| Catalog targets | Packet |
|---|---|
| Q1375, Q1376, Q1481 | [Fixed alternation and definability](foundations/ROOT-DEFINABILITY-ATTEMPTS.md) |
| Q1377, Q1378, Q1979 | [Finite axiomatization](foundations/Q1377-ATTEMPTS.md), [QE](foundations/Q1378-ATTEMPTS.md), [shatter growth](foundations/Q1979-ATTEMPTS.md) |
| Q2978–Q2982, Q2990–Q2993 | [Arithmetic](arithmetic/ATTEMPTS.md) |
| Q246, Q2169, Q2170, Q3268, Q3482 | [Model theory](model-theory/ATTEMPTS.md) |
| Q3075, Q3076, Q3077, Q3079 | [Automatic graphs and BVASS](graphs/ATTEMPTS.md) |
| Q3206 | [Anti-recurrence](anti-recurrence/ATTEMPTS.md) |
| Q3668, Q3824 | [Proof complexity](proof-complexity/ATTEMPTS.md) |
| Q2778 | [Global cardinalities](gp2/Q2778-ATTEMPTS.md) |

Each numbered route gives a construction, reduction, algorithm or attempted
proof and its counterexample or precise missing lemma. Several share
obstructions; the count is not a claim of independent impossibility results.

## Review, verification and filing

[ROOT-REVIEW.md](ROOT-REVIEW.md) records the main-thread proof, scope and
stopping audit. The retained agent independently reviewed the main-thread
all-ones and overlap-law theorems, [definability](foundations/ROOT-DEFINABILITY-REVIEW.md),
[entropy](foundations/ENTROPY-REVIEW.md) and [circuit lane](foundations/CIRCUIT-REVIEW.md).
Exact finite semantic controls, complete
finite transition certificates and bounded experiments retain their actual
strength; no numerical optimizer is a global certificate.

The generated local code and receipts are available in the corresponding
packet directories. The new word-circuit work does not claim a Walnut run,
replay of the missing archive, or compiled Lean formalization.

[RESULTS.json](RESULTS.json) and the programme routes file one exact new
catalog closure, Q2777, plus three partial scopes, Q2778/Q2978/Q2980.
Other failed targets acquire no disproof mark. BASELINE.json
and [preservation validation](FILE-VALIDATION.json) check all earlier
ledger decisions, result routes, membership and original corpus fields.
file_results.py and validate_filing.py
make this filing reviewable and reproducible. All new work is private;
the public GitHub catalog was not changed.
