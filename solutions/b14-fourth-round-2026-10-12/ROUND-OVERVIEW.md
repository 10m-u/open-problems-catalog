# B14 fourth round completion and block descent

**Accepted after main-thread mathematical review and complete check replay.** This return advances P1/P2 on a specified family of two-port necklaces and P3 on shortest-path metrics whose biconnected blocks have bounded size. It strengthens restricted programme results while leaving the broader stopped ambitions and all catalog marks at their existing scopes.

- [Completion certificates and exact contraction](submission/proofs/COMPLETION-CERTIFICATES.md) characterize the minimum-repair face and solve arbitrary bounded secondary costs by a subset DP on $k/2$ paired units. Endpoint-separable repair costs give an exact formula. On the retained nonseparable 180-city instance, the exact optimum is 1,330,166, with all 147,528 DP entries checked independently.
- [Separation from every rooted forced 1-tree bound](submission/proofs/COMPLETION-CERTIFICATES.md#6-a-four-cost-strict-metric-separation-from-all-rooted-1-trees) gives an all-size, four-cost family with a unique optimum. Completion bounds delete every nonoptimal edge, while all roots and real vertex potentials leave every edge undeleted. At 180 cities this retains the optimal 180-edge cycle from 16,110 complete-graph edges.
- [Deterministic block descent](submission/proofs/BLOCKWISE-DESCENT.md) proves that 2-opt gains cannot cancel across blocks. An integer metric preserving all gain signs bounds every strict descent by $n\sum_B D_B2^{D_B-1}$, where $D_B=\binom{|B|}{2}$. For maximum block size four the bound is $64n(n-1)$, for arbitrary positive generating lengths and any strict pivot rule.

[Submitted report](submission/REPORT.md) · [Intake review and scope correction](REVIEW.md) · [Filed results](RESULTS.json) · [Replay validation](verification/REPLAY-VALIDATION.json).

The original 35-file submission is preserved byte for byte. The replay used a separate copy and passed the complete six-stage suite, including 52 full-city exact oracle cases, 2,484 forced-edge comparisons, 179 flow certificates, 112 integer metric certificates and eight damaged-certificate rejection controls. The same 52 instances support both solver comparisons; they are not 104 distinct cases. The inexpensive bound failed to close 25 of 26 nonseparable controls before exact contraction; those failures are retained.

The necklace representation, port obstruction and dominant primary cost gap are assumptions of the accepted exact solver. The larger instances are structured correctness controls, not general-purpose performance comparisons. The block theorem gives descent length; Q3817's arbitrary sparse-graph nearest-neighbor quality remains unresolved. A retained 3-opt counterexample limits the noncancellation method. Literature priority and external or formal verification are not established.

B14 programme · [Third return and sharp count rate](../b14-third-round-2026-10-12/ROUND-OVERVIEW.md) · [Earlier terminal register](../b14-second-round-2026-10-12/CONTROL.md).
