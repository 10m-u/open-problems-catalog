# B14 third round sharp local optimum count

**Accepted after main-thread mathematical review and replayed checks.** This return contains a substantive improvement to Q3818/P5: a matching exponential upper and lower rate, approximately 0.597586978551345, and the consequence $\mathbb E M_n=O((3/5)^n\sqrt{n!})$. The earlier handoff supplied an upper bound with base at most $6/7$, without a matching lower bound. Q3818 was already locally proved; this strengthens its result without adding a catalog closure.

The new proof uses a small-threshold Janson estimate, clipping of the full tour-cost cube, and a tilted-measure lower bound. It also extends the rate to fixed independent edge-cost laws with finite positive density at a finite lower endpoint. This includes direct independent exponential costs, with the stated endpoint assumption. Dependent shortest-path distances need a different argument.

[Full submitted proof](submission/REPORT.md) · [PDF](submission/REPORT.pdf) · [Intake mathematical review](REVIEW.md) · [Filed results](RESULTS.json).

The return separately reproduces four bounded checks from the handoff. Those replications support the previous evidence and add no new P1/P2/P3 theorem. The sharp-rate proof and distribution extension are the new mathematics.

The original 29-file packet is preserved byte for byte under [submission](submission/README.md). IMPORT.json records the received archive and hashes; [replay validation](verification/REPLAY-VALIDATION.json) records the new exact and numerical reruns. Numerical quadrature is illustrative, while the rational certificate for the base $3/5$ is exact. No asymptotic equivalence, $O(\rho^n\sqrt{n!})$ bound, count concentration, tour quality or search-time result follows.

This is internally reviewed mathematics; literature priority, external peer review and formal verification are not established. All earlier proofs, catalog marks and stopping counts are retained. The [fourth return](../b14-fourth-round-2026-10-12/ROUND-OVERVIEW.md) develops different programme lines. B14 programme.
