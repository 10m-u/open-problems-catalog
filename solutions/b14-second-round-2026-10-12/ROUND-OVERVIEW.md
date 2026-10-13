# B14 continuation — all targets, separate stopping counts

**Complete under the user's stopping rule.** Every B14 target has been addressed at the broader research scope: four targets are solved locally and ten are stopped at five consecutive failed routes each. The four are Q3818, P5, P2 and P3; Q3818/P5 concern the same counting theorem. The same continuing subagent was retained throughout. [Control](CONTROL.md) · [Machine register](STATUS.json).

Q3818 and P5 were proved in [round 1](../b14-first-round-2026-10-12/ROUND-OVERVIEW.md). P2 now has a proved exponential state quotient on a certified residual family. P3 has a full sparse-model expected 2-opt move bound. Q3817, Q549, Q550, Q1852, Q1853, Q1953, Q3819 and P1/P4/P6 stop at their own five-route limits while remaining unresolved. No stopped conjecture is marked disproved, and first deliverables are not substituted for the broader completion scope.

## Results retained

- [Path/star NN guarantees and quadratic tree-metric 2-opt descent](initialization/RESULT.md), with [main-thread review](INITIALIZATION-REVIEW.md).
- [Unique-optimum strict metric where every rooted forced-1-tree bound fails to delete every edge](generating-graph/RESULT.md), with [independent review](initialization/UNIQUENESS-REVIEW.md).
- [Exact graphical-TSP frontier DP on the generating graph](generating-graph/DP-RESULT.md), with [independent suffix-equivalence review](initialization/DP-REVIEW.md).
- [Saturated-vertex label compression on certified Hamiltonian residuals](residual-search/RESULT.md), with exact controls and stated performance limits.
- [Exponential realizable state reduction after actual elimination](residual-search/EXPONENTIAL-RESULT.md), with [independent review](initialization/P2-EXPONENTIAL-REVIEW.md).
- [Full sparse exponential expected 2-opt descent](P3-REVIEW.md): at most 10m(m−1)n^5(1+log(n!)) expected moves, hence O_c(n^8 log n) for m≤cn. Polynomial convergence is established prior art; the local normalization proof has no novelty claim.
- [Held-family and held-size policy comparison](guidance/RESULT.md) and [five actual learned attempts](guidance/P6-ATTEMPTS.md), with 320 checked packets and no supported learned advantage.
- [Petersen subdivision fractional vertices and exact gap (n+1)/n](lp-supports/RESULT.md), with [independent review](initialization/P4-FAMILY-REVIEW.md).

These are local internally checked results, without a novelty or external peer-review claim. They do not solve general TSP or close broader catalog questions.

## Per-problem attempts

- Q3817: five routes and their limits are reviewed in [INITIALIZATION-REVIEW.md](INITIALIZATION-REVIEW.md).
- Q1852/Q1853: [attempts](other-targets/POWER-ATTEMPTS.md), [independent review](initialization/POWER-REVIEW.md), [exact receipt](other-targets/POWER-ROUTE-CHECK-RESULTS.json).
- Q1953: [five construction routes](other-targets/Q1953-ATTEMPTS.md), with [independent review](initialization/HAAR-REVIEW.md).
- Q3819: [inversion-potential attempt](other-targets/Q3819-ATTEMPTS.md), [four further routes](initialization/Q3819-ATTEMPTS.md), and [main-thread review](Q3819-REVIEW.md).
- Q549/Q550: [general split-direction attempts](certificates/Q549-ATTEMPTS.md), [matching-proof attempts](certificates/Q550-ATTEMPTS.md), and [independent review](initialization/CERTIFICATE-REVIEW.md).
- P1/P4/P6: [final broader-route review](BROADER-ROUTE-REVIEW.md), with the distinct hypotheses, shared ingredients and review provenance disclosed.

The exact catalog questions remain unresolved except Q3818. Q3817 receives a partial mark for paths/stars; the tree and full sparse descent theorems do not resolve its initializer-quality question. Proofs and experiments are internally reviewed, without an originality or external peer-review claim. The subagent's final review turns disconnected; the final P1/P4/P6 count reviews were completed in the main thread, with independent audits of their underlying results and separate exact controls.

## Filing and verification

[RESULTS.json](RESULTS.json) supplies eight continuation result routes. [FILE-VALIDATION.json](FILE-VALIDATION.json) checks that all 28601 original corpus records, all prior ledger decisions and all 380 prior compiled result routes remain intact. Only Q3817 gains a partial catalog mark; it remains eligible for open-question review. There is no new exact catalog closure in this round, and no public GitHub publication.

The finite certificates and checks support the proofs at their stated scopes. Timed comparisons are bounded single-machine measurements; their small differences do not justify a speed claim. The unresolved broad questions remain available for a separately authorized future research run.
