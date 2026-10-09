# Ten open-problem investigations — 9 October 2026

This round contains **five proposed affirmative proofs, two counterexamples, two hardness theorems, and one partial theorem**. Every result has a complete written argument, a separate internal mathematical review, primary-source references, and reproducible computational controls where applicable.

**Evidence:** the arguments and reviews were produced with AI research assistance. A second AI agent checked each result independently within this session; this is not external peer review or formal verification. The finite computations check identities, constructions, examples and conventions. They do not prove the infinite statements. No historical-priority claim is made.

The starting commit was `8967f4f70776856b3dfc0b2494ed73167b15ee0c`. The selected questions had open status and no exact prior solution recorded at that commit. The selection emphasized accessible primary statements and problems admitting a complete argument or a small, independently checkable obstruction. The reports document later-literature searches and distinguish existing background results from the contributions here.

## Results

| Problem | Conclusion | Main result | Written argument |
|---|---|---|---|
| [Q56](../../problems/mathematics/optimization-operations-research.md#q56) | Hardness theorem | The requested high-precision tensor oracle is NP-hard already at rank at most two, with positive bounded rational factors. A uniform-marginal MOT corollary follows. | [Proof](optimization/Q0056.md) |
| [Q192](../../problems/mathematics/probability-stochastic-processes-part-1.md#q192) | Proposed affirmative solution | The canonical Brownian law conditioned on one high-order power integral being zero concentrates on the zero path in the uniform topology. | [Proof](probability/Q192-brownian-power-conditioning.md) |
| [Q270](../../problems/mathematics/probability-stochastic-processes-part-1.md#q270) | Proposed affirmative solution | The bunkbed inequality holds for every transitive tournament in the exact independent-edge model, with a strict quantitative bound. | [Proof](probability/Q270-transitive-tournament-bunkbed.md) |
| [Q291](../../problems/game_theory/noncooperative-games-equilibrium-theory.md#q291) | Proposed affirmative solution | Every mixed Nash equilibrium has at least two players using scissors, for every number of players $m\ge2$. | [Proof](games/Q0291.md) |
| [Q1060](../../problems/mathematics/optimization-operations-research.md#q1060) | Counterexample | The unrestricted optimum is $16$, while the optimum with all pairwise covariances nonpositive is $920/57$. | [Proof and exact certificates](probability/Q1060-negative-covariance-counterexample.md) |
| [Q1653](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1653) | Counterexample | The factorial language $0^*1^*\cup\{10\}$ has complexity $2,4,4,5,6,\ldots$, impossible for recurrent-factor complexity. | [Proof](discrete/Q1653-recurrent-complexity-counterexample.md) |
| [Q3236](../../problems/mathematics/functional-analysis-operator-theory.md#q3236) | Proposed affirmative solution | The actual sum quasinorm has both exact rearrangement invariance and the exact Fatou property in the full source scope. | [Proof](algebra/Q3236-proof.md) |
| [Q3454](../../problems/mathematics/functional-analysis-operator-theory.md#q3454) | Partial theorem | Commuting initial and final support pairs, together with the proximity condition in the proof, give equal supports and a quantitative local Lipschitz bound for Moore–Penrose inverses. | [Partial proof](algebra/Q3454-proof.md) |
| [Q3489](../../problems/computer_science_ai/theory-of-computation-algorithms-part-2.md#q3489) | Hardness theorem | Exact $C_G(-2)$ evaluation is #P-hard and in GapP; every nonzero fixed algebraic evaluation point is #P-hard. | [Proof](discrete/Q3489-connected-set-evaluation.md) |
| [Q3569](../../problems/mathematics/combinatorics-graph-theory-part-2.md#q3569) | Proposed affirmative solution | Periodic zero-extension is equivalent to compatible maximal greedy words, with all cross-residue shift inequalities. | [Proof](discrete/Q3569-periodic-zero-extension.md) |

The [machine-readable ledger](RESULTS.json) records each exact conclusion, its scope, the catalog entry, primary source, review, checker and certificate.

## Three concise mechanisms

For **Q1060**, the marginals are centered two-point variables. Two explicit rational couplings attain the two claimed optima. The decisive universal inequality is

$$
57T+16\operatorname{Cov}(X_2,X_3)\ge920,
$$

where $T$ is the largest subset variance. The unrestricted minimum is $16$, so every minimizing coupling has $\operatorname{Cov}(X_2,X_3)\ge1/2$. Imposing nonpositive covariances raises the optimum by exactly $8/57$. An integer identity valid at every one of the sixteen possible outcomes proves the bound; no numerical optimizer is needed to verify it.

For **Q1653**, every recurrent factor has a recurrent right extension. If the number of recurrent factors is equal at two consecutive lengths, each shorter factor has exactly one recurrent right extension. A longer recurrent word is then determined by its initial block, so the complexity stays constant forever. The factor-closed example has a plateau at lengths 2 and 3 followed by growth at length 4, which gives the contradiction. Exact equality at every length, as required by the source, matters here.

For **Q270**, expose a transitive tournament in vertex order and track the reachable counts in its two layers. The count process is Markovian and symmetric under layer exchange. Before the first equality of the counts, their difference stays positive because it changes by at most one. After equality, symmetry cancels the expected target-probability difference. The remaining contribution is nonnegative. In the source model,

$$
\mathbb P(u^{(0)}\to v^{(0)})-\mathbb P(u^{(0)}\to v^{(1)})
\ge2^{-(v-u+2)}>0\quad(u<v).
$$

## Scope and catalog status

The catalog assigns its existing **“solved here”** labels to the five affirmative proof proposals and two counterexamples. This has the repository's stated meaning: a result recorded here at a precise scope, without a claim of external verification. The original source statements and source metadata are preserved.

The two complexity questions, **Q56 and Q3489**, conservatively retain **partial** status. Their hardness theorems are complete arguments, but a categorical negative answer to the literal algorithm-existence question would require an unresolved complexity-class separation. Q56 excludes the specified deterministic algorithm unless $\mathrm P=\mathrm{NP}$ in the binary rational-input model. Q3489 is polynomial-time computable if and only if $\mathrm{FP}=\#\mathrm P$. Its signed value is in GapP and is not described as a #P-complete function.

**Q3454 remains partial.** The proof treats commuting corresponding support idempotents. The unrestricted noncommuting conjecture is not settled. Q192 does not settle Q191 or Q193; Q270 does not settle arbitrary acyclic graphs; Q291 does not settle larger action-space versions; Q3569 does not settle the source's separate alternate-base conjectures.

The catalog totals after this round are **3,456 open, 90 partial, and 42 solved here** (30 proved and 12 disproved), out of 3,588 entries. This round changes ten formerly open records: seven to repository-local solved statuses and three to partial.

## Reproduce the computational controls

Python 3 and the standard library are sufficient:

```bash
python solutions/round-2026-10-09/run_all.py
```

The runner executes the eight existing checkers and writes [verification-summary.json](verification-summary.json). It records hashes of the programs and their certificate files. Individual programs can also be run directly from the repository root.

| Target | Exact controls |
|---|---|
| Q56 | 3,002 product-partition instances and 141,568 tensor entries; all gap and threshold checks pass. |
| Q192 | 1,035 deterministic rational peak-inequality checks; the Brownian theorem itself is proved analytically. |
| Q270 | Every one of the 66,066 retained-edge graphs for tournaments through four vertices; all ordered vertex-pair probabilities agree with an independent count calculation. |
| Q291 | 1,020 unique-scissors strategy profiles and 3,756 direct payoff comparisons, including pure-strategy boundary values. |
| Q1060 | All sixteen outcomes of the universal identity; both couplings, exact marginals, covariance matrices, and every subset cost. |
| Q1653 | 32,767 binary words, 7,826 factor-closure checks, and all sixteen relevant recurrent right-extension rules. |
| Q3236 / Q3454 | 128 exact breakpoint cases for the auxiliary nonattainment example; six rational matrix cases and a sharp scalar threshold. |
| Q3489 | 1,100 leaf attachments, 12 two-leaf attachments, 12 rooted-cycle attachments, 152 clique substitutions, three complete single-call reductions, and 440 exact norm checks. |
| Q3569 | 995,085 numerical/suffix comparisons on 729 place-value prefixes; 2,916 finite equivalence profiles; 9,841 period-two extension and 62 shift checks. |

The optional [Q1060 search script](probability/search_q1060.py) uses SciPy to explore candidates. It is not run by the standard-library verifier and is not required to certify the result.

## Separate internal mathematical reviews

| Targets | Review |
|---|---|
| Q56 | [Reduction, encoding, precision gap and MOT corollary](algebra/review-Q0056.md) |
| Q192 | [Canonical conditioning, normalization and concentration](discrete/review-Q192.md) |
| Q270 | [Exact graph model, stopping-time symmetry and boundary cases](discrete/review-Q270.md) |
| Q291 | [Payoffs, asymmetric strategies and strict best responses](discrete/review-Q291.md) |
| Q1060 | [Source scope, universal dual inequality and both exact optima](algebra/review-Q1060.md) |
| Q1653, Q3236, Q3454, Q3489 | [Source alignment and complete logical audits](reviews/root-review.md) |
| Q3569 | [Suffix criterion, zeroing step, residue indices and boundaries](algebra/review-Q3569.md) |

Each proof contains its own primary-source links and dated literature boundary. Downloaded source texts are not included. Independent external mathematical review remains the next evidentiary step for these research proposals.
