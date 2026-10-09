# Seven open-problem investigations — 2026-10-09

This round investigates **Q132, Q256, Q257, Q3101, Q3102, Q3286, and Q3287**. It supplies four proposed complete answers and three proved partial results, together with proofs, separate internal reviews, source notes, runnable checks, and machine-readable result records.

**Evidence level.** The arguments were developed with AI research assistance and independently re-derived by another agent in this research round. These are internal reviews, not external peer review or formal proof certification. The finite computations and numerical integrals are supplementary controls; the universal claims depend on the written proofs. The dated literature checks do not certify historical priority.

Base repository commit: `368ce0d95a90c073be730b27c724133ce31666f0`. All seven entries were open, nonprovisional, and had no linked repository result at that commit. The selection groups related questions so that source verification and structural lemmas can be reused, while covering dynamics, graph theory, semigroups, and probability.

## Results and remaining questions

| Problem | Result obtained | Catalog status |
|---|---|---|
| [Q132: donation dynamics](../../problems/game_theory/social-choice-voting-theory.md#q132) | Convergence for schedules whose complete-interval lengths satisfy $\sum_k 1/L_k=\infty$; convergence with finite total variation for every fair schedule when support weights factor as $v_{ix}=a_iw_x$, including every incidence forest. | **Partial.** Arbitrary fair schedules with unrestricted weights on incidence cycles remain unresolved. |
| [Q256: caterpillars](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q256) | An exact 16-state characterization and algorithm for a minimum proper total dominating set; sharp bounds of three selected leaves and four selected neighbors at each spine vertex. | **Proposed complete affirmative answer.** The characterization is algorithmic, using $O(k)$ arithmetic operations for a $k$-vertex spine. |
| [Q257: tree parameter pairs](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q257) | Every realizable pair satisfies $a+1\le b\le6a-4$ and has a representative on at most $6a-4$ vertices. Exactly $b\in\{3,5\}$ occurs for $a=2$, and $b\in\{6,7\}$ for $a=3$. | **Partial.** The general pair classification for $a\ge4$ remains unresolved. |
| [Q3101: odd girths](../../problems/mathematics/algebra-representation-theory-part-2.md#q3101) | Triangle-free commuting graphs of finite bands are bipartite. In the full completely regular class, a triangle-free graph's noncentral idempotents induce a bipartite graph, and every odd cycle requires at least two nonidempotent involutions with central subgroup identities. | **Partial.** Odd girths at least five in the full completely regular class remain unresolved. |
| [Q3102: knit degree three](../../problems/mathematics/algebra-representation-theory-part-2.md#q3102) | Every length-three left path in a finite completely regular semigroup yields a length-two left path, so knit degree three cannot occur. | **Proposed complete negative existence answer**, recorded as `disproved`. The result is a nonexistence theorem. |
| [Q3286: large-parameter dispersion](../../problems/mathematics/probability-stochastic-processes-part-2.md#q3286) | For each fixed integer $d\ge2$, the limit $C_d=\lim_{a\to\infty}B_d(a)$ is finite and greater than one, with an explicit positive integral formula. | **Proposed complete affirmative answer.** |
| [Q3287: small-parameter dispersion](../../problems/mathematics/probability-stochastic-processes-part-2.md#q3287) | For each fixed integer $d\ge2$, $B_d(a)=1-2a/(d-1)+O_d(a^2)$ as $a\downarrow0$. This gives the requested limit one and underdispersion for sufficiently small positive $a$. | **Proposed complete affirmative answer.** |

In Q257, $a=\gamma_t(T)$ and $b=\gamma_{pt}(T)$ are the minimum total-domination and proper-total-domination sizes. In Q3286–Q3287, $B_d(a)$ is the limiting variance-to-mean ratio for record arrivals $R_n$; the limit in the sample size $n$ is taken before either limit in $a$.

The large-parameter constant is

$$
C_d=1+\sum_{q=1}^{d-1}
\frac{\binom dq}{(d-q-1)!(q-1)!}
\int_0^\infty\!\int_0^\infty
\frac{x^{d-q-1}y^{q-1}}{e^x+e^y-1}\,dx\,dy.
$$

In particular, $C_2=1+\pi^2/3$ and $C_3=1+12\zeta(3)$. The [analysis proof](analysis/REPORT.md) justifies the integral transformations and the limits with explicit bounds.

## Proofs, reviews, and source checks

| Questions | Proof | Separate internal review | Sources and dated search |
|---|---|---|---|
| Q132 | [Convergence theorems](dynamics/Q0132.md) | [Dynamics review](analysis/review-Q0132.md) | [Source and scope discussion](dynamics/Q0132.md#6-literature-boundary-and-reproducibility) |
| Q256 | [Caterpillar characterization](combinatorics/Q0256-caterpillars.md) | [Graph-theory review](reviews/combinatorics-review.md) | [Search log](combinatorics/SEARCH-LOG.md) |
| Q257 | [Tree bounds and finite reduction](combinatorics/Q0257-tree-pairs.md) | [Graph-theory review](reviews/combinatorics-review.md) | [Search log](combinatorics/SEARCH-LOG.md) |
| Q3101 | [Odd-cycle obstructions](algebra/Q3101-odd-girth-obstructions.md) | [Odd-girth review](analysis/review-Q3101.md) | [Source log](algebra/SOURCES.md) |
| Q3102 | [Nonexistence theorem](algebra/Q3102-no-knit-degree-three.md) | [Knit-degree review](combinatorics/review-Q3102.md) | [Source log](algebra/SOURCES.md) |
| Q3286–Q3287 | [Endpoint limits](analysis/REPORT.md) | [Analysis review](reviews/analysis-review.md) | [Search log](analysis/SEARCH_LOG.md) |

The original donation thesis, semigroup paper, and Pareto-record dissertation were read. For the Pareto formulas, a separate visual inspection confirmed that the normalization is the rising factorial $(a)_d$. The tree-problem thesis returned an access error; its statements were compared with the author's publisher-indexed question text and conference abstract, and the related general-graph paper was checked. The graph-theory notes state this access limitation explicitly. No copyrighted source PDFs are included in the repository.

[RESULTS.json](RESULTS.json) records each claim, its exact scope, the remaining gap, source access, and evidence paths. Catalog statements and original source records are preserved; only the seven statuses and their result ledgers change.

## Reproduce the checks

Run from the repository root using Python 3.10 or newer:

```sh
python -m pip install -r solutions/seven-problems-2026-10-09/requirements.txt
python solutions/seven-problems-2026-10-09/run_all.py
python solutions/seven-problems-2026-10-09/validate_catalog.py
```

The numerical analysis checks use `mpmath==1.3.0`. The dynamics, graph, semigroup, and catalog checks use the Python standard library. The catalog validator also needs Git and the base commit's history; it is separate from the mathematical checks so those remain runnable from a source archive. Optional Z3 exploration in the algebra folder is excluded from the default verification and from the premises of the proofs.

| Control | Coverage | Evidence type |
|---|---|---|
| [Donation dynamics](dynamics/q0132-checks.json) | 1,380 best-response comparisons; 13,080 nonexpansiveness comparisons; 9,688 residual comparisons; 960 complete-interval bounds; 8,640 transfer inequalities; 3,945 weighted best-response and 3,945 cumulative-variation bounds. | Exact rational arithmetic on finite examples. |
| [Tree characterization and bounds](combinatorics/verification.json) | All 2,287 unlabeled trees of orders 2–13, including 1,086 caterpillars; 388 leaf reductions; 554 additional short leaf words; a compressed example representing 20,020,100 vertices. | Exact enumeration and independent subset search. |
| [Semigroup identities and paths](algebra/verification.json) | 13 explicit semigroups, 49,725 associativity triples, and 674 constructive left-path collapses covering all three proof cases. Includes published examples outside the hypotheses. | Exact multiplication-table and graph calculations. |
| [Pareto-record integral transformations](analysis/checks.json) | 252 kernel identities at 60-digit precision, four radial integrals, 24 exact small-parameter bounds, and the $d=2,3$ limiting constants. | High-precision numerical diagnostics plus exact rational bound evaluations. |

[verification-summary.json](verification-summary.json) records the mathematical check outcomes and file hashes. [catalog-validation.json](catalog-validation.json) records the status, ledger, source-preservation, and index consistency checks. The finite and numerical controls test the implementations and selected identities; they do not certify the universal proofs.
