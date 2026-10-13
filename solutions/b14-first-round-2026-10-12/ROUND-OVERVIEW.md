# B14 — First research round

**Q3818 is locally proved.** For independent uniform $[0,1]$ costs on $K_n$, the expected number of 2-opt local optima is

$$
\mathbb E[M_n]=O((6/7)^n\sqrt{n!}).
$$

This improves the conjectured $O(\sqrt{n!})$ bound. The complete written proof passed a separate internal mathematical review and independent exact finite checks. It is filed at the exact catalog scope, with no external peer-review or originality claim.

The main thread developed P1 certified edge elimination; the same continuing subagent developed P5 counting local optima. Each reviewed the other's mathematical line. The user authorized this first bounded round and one continuing subagent. No large benchmark, training run, or other waiting research programme was started.

## Counting local optima: Q3818 / P5

[Full proof](local-optima/RESULT.md) · [Independent review](COUNT-REVIEW.md) · [Main-thread check receipt](COUNT-CHECK-RESULTS.json) · [Subagent check receipt](local-optima/CHECK-RESULTS.json)

Conditioning on the fixed tour's costs separates the chord constraints into cycles. A Frobenius/read-two inequality retains every exchange while respecting its shared replacement edges. The resulting quadratic integral yields a constant $c=\sqrt\pi\,\operatorname{erfc}(1/2)<6/7$ and, for $n\geq12$,

$$
\frac{\mathbb E[M_n]}{\sqrt{n!}}
\leq\frac{e^{13/2}}{2\sqrt n}\,c^n.
$$

Finite smaller sizes are absorbed into the asymptotic constant. The model is generally nonmetric. The count does not bound tour quality, attraction basins, or descent time.

Reading the published theorem corrected the initial programme's baseline: its $1.2098^n$ bound is stated for $n=2^k+1$. The local proof handles every integer size. [MFCS 2025, Theorem 3 and §5](https://doi.org/10.4230/LIPIcs.MFCS.2025.73)

## Certified elimination: P1

[Derivation, experiment and obstructions](elimination/RESULT.md) · [Independent exhaustive review](local-optima/ELIMINATION-REVIEW.md) · [Experiment](elimination/experiment.json) · [Certificate validation](elimination/validation.json)

Exact forced-edge 1-tree bounds produce independently checked strict deletions. This is established sensitivity mathematics implemented as a transparent baseline. The packet includes:

- 147 integer-arithmetic certificate packets, with 6,807 forced-edge bounds checked independently;
- a separate exhaustive audit of 100 snapshots and 1,280 forced bounds, including ties and negative transformed costs;
- 48 metric instances at sizes 8, 10, 12, with residual subset-DP optima agreeing in every case;
- an all-size tree-metric proposition: every edge belongs to an optimum, so preserving all optima retains the complete graph;
- a Petersen (1,2)-metric witness with tour optimum 11, subtour LP 10, and all 45 edges occurring in optimal tours.

On the small Euclidean family, the tuned single-root method deletes 416 of 556 edges and reduces subset-DP transitions from 267,520 to 1,290. Its gain weakens when the same evaluation budget is split over roots in the clustered family. Tree metrics permit no all-optima-preserving deletions. These observations do not establish scalable performance or a general low-width theorem.

## Current research direction

P5's original count target is closed at its stated model. Further landscape work must ask about costs, basins, or descent time rather than repeat that conjecture.

For P1/P2, the next useful target is preserving one selected optimum, or exploiting a shortest-path metric's sparse generating graph directly. Unique tie-breaking has a polynomial bit encoding, but it alone gives no residual-width guarantee. Adaptive root selection can be tested on held-out families once a benchmark scope is chosen.

Q3817/P3 remains a separate unstarted probabilistic line. The complete-uniform proof and the bounded integer shortest-path experiment do not settle its sparse exponential initializer question. The other seven B14 catalog members retain their previous resolution state.

## Files and reproduction

Programme · [Structured results](RESULTS.json) · Catalog resolution

From the repository root, the independent counting audit is:

    python3 solutions/b14-first-round-2026-10-12/audit_count.py

The proof author's checks and independent elimination audit are:

    python3 solutions/b14-first-round-2026-10-12/local-optima/check.py
    python3 solutions/b14-first-round-2026-10-12/local-optima/check_elimination.py

The elimination experiment is:

    python3 solutions/b14-first-round-2026-10-12/elimination/run.py

file_results.py records the reviewed scopes in the private catalog. Reapply catalog annotations with the existing conjecture-status tool, then compile programme routes. [FILE-VALIDATION.json](FILE-VALIDATION.json) records preservation checks. A pre-filing snapshot is kept under the catalog's data/archive directory. This round has not been published to the public GitHub repository.
