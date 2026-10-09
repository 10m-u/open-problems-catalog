# B4: optimal stopping and search under partial information

Research report from an AI research agent working on this catalog, filed as received. The proofs are written arguments by that agent; they have not been independently re-derived or peer reviewed. Statuses below are the report's own, at its stated scope.

| Problem | Title | Status | Result |
|---|---|---|---|
| [Q535](../../problems/mathematics/optimization-operations-research.md#q535) | Does time-dependent Pandora search admit a PTAS? | disproved | Ruled out under a standard complexity assumption, as the question allows: a deterministic PTAS implies P=NP, and a randomized one is excluded under NP⊄BPP. Already holds with zero costs, no deterioration, equal delays, {0,1} rewards and… |
| [Q536](../../problems/mathematics/optimization-operations-research.md#q536) | Efficient optimal stopping under a finite mixture of product distributions | partial | Exact optimal-policy synthesis is #P-hard under Turing reductions already for two scenarios and at most four values (a stopping gadget worth 1+TV(P,Q)/2); every fixed number of scenarios admits an FPTAS for nonnegative rewards. Scope: A… |
| [Q540](../../problems/mathematics/optimization-operations-research.md#q540) | Half-prophet utility under an unobserved additive common cause | partial | For X_i in {0}∪[ℓ,u] with c=u/ℓ, an observable rule earns 3/(c+1+2√(c²−c+1)) of the prophet: 3/4 for a common binary residue alphabet and at least 1/2 when c≤2√2−1. Exact O(nm)-arithmetic algorithm for finite-support common binary… |
| [Q541](../../problems/computer_science_ai/theory-of-computation-algorithms-part-1.md#q541) | Exact complexity of finite coupon-collection query scheduling | proved | Finding an optimal permutation is #P-hard under polynomial-time Turing reductions, already for n=d+1 with all probabilities positive; that restricted search problem is Turing-equivalent to the permanent. No polynomial-time algorithm… |
| [Q767](../../problems/computer_science_ai/theory-of-computation-algorithms-part-1.md#q767) | Constant approximation for search under a latent mixture | partial | Exact posterior dynamic programme; an FPTAS when both the scenario count and the number of box types are fixed; an unbounded gap between optimal fixed-order and fully adaptive search (5/4 against (m+1)/2). Scope: A polynomial… |
| [Q1496](../../problems/mathematics/probability-stochastic-processes-part-1.md#q1496) | The limiting full-information expected rank | investigated | No new exact limiting-rank result; prior finite numerical estimates remain explicitly prior and uncertified. Remaining/limits: Q1496: exact Robbins limiting expected rank and any new interval certification of the prior finite computations. |
| [Q2390](../../problems/mathematics/probability-stochastic-processes-part-2.md#q2390) | Optimal ordinal matroid secretary ratio | investigated | No new proof or disproof of the full ordinal random-arrival 1/e matroid-secretary statement. Remaining/limits: Q2390: ordinal random-arrival 1/e guarantee for every finite matroid. |

## Files

- [B4_Research_Report_2026-10-07.md](B4_Research_Report_2026-10-07.md)
- [B4_Statement_Ledger_2026-10-07.json](B4_Statement_Ledger_2026-10-07.json)

