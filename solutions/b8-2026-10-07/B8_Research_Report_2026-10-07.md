# B8 unseen-vocabulary research: results and verification

**Research date: 2026-10-07.** Input snapshot: 7 October 2026.

**Outcome: two exact questions have complete independently reviewed written proofs; four have rigorous partial results; two remain unresolved.** “Proved” in this report identifies a written mathematical argument whose dependencies and quantifiers are supplied and whose critical steps received independent internal review. No theorem was compiled in a proof assistant, externally peer reviewed, or published through this work. The primary sources still describe the relevant questions as open; these new derivations are a separate evidence layer.

The complete arguments appear in Appendices A–D. Appendix E supplies the corpus contract, all measured results, and implementation details. The JSON ledger preserves every original statement, stable identifier, changed assumption, evidence class, and residual question.

## 1. Exact-statement disposition

| Question | Stable statement ID | Disposition | Result at the assigned scope |
|---|---|---|---|
| Q851 | `c72db31c0497eb836a83` | **unresolved** | The non-tolerant accuracy-dependent logarithmic gap remains. |
| Q852 | `f9edd65b797563064576` | **proved** | Requested tolerant rate obtained for arbitrary countable support. |
| Q853 | `07232484a765905b847d` | **unresolved** | General removal of the Markov logarithmic factor remains. |
| Q854 | `ad6c67395090a5839dec` | **partial** | Linear variance proved for every refresh chain; arbitrary kernels remain. |
| Q855 | `eeea824c340739a51a8d` | **partial** | Stronger iid rare-mass bound and complementary plug-in envelope; full frontier remains. |
| Q856 | `eee2f3c01977fe365b97` | **partial** | Fixed finite deterministic linear class characterized; global constant remains. |
| Q858 | `0c3cb5efa6b7fd0651a8` | **proved** | Variance divergence implies the fixed-sample CLT without connectedness. |
| Q859 | `11f05c2567c0a33574c8` | **partial** | Growing-threshold iid minimax rate proved; general Markov rarity cost remains. |

## 2. Principal mathematical results

### 2.1 Q852: tolerant support diagnosis on an unrestricted alphabet

Let \(d_n(p)\) be the TV distance from laws supported on at most \(n\) symbols, and let \(\delta=\varepsilon-\varepsilon'\). The new written theorem constructs an estimator of \(d_n(p)\) with additive error at most \(\delta/4\), success probability at least \(3/4\), and deterministic maximum sample budget

\[
\boxed{C\frac{n\log^2(e/\delta)}{\delta^2\log(en)}}.
\]

The constant is universal. The result holds for every integer \(n\ge1\), every \(0<\delta<1\), and every countable distribution, without a promise on its actual support size. Comparing the estimate to \((\varepsilon+\varepsilon')/2\) therefore answers the exact question. Here \(n\) is the *target support size*, not the number of observations.

The key reduction is

\[
1-d_n(p)=\inf_{t\ge0}\left(nt+\sum_i(p_i-t)_+\right).
\]

A polynomial can approximate the hinge between horizontally shifted cutoffs \(t\) and \(t-h\), with only \(\eta p_i\) vertical error for atom \(i\). The vertical errors sum to \(\eta\), even on an infinite alphabet; optimization turns the horizontal shift into at most \(2nh\). Taking \(h\) of order \(\delta/n\) gives the needed accuracy without paying an additional support-truncation factor. Independent Poisson counts gate either a low-probability polynomial or a localized polynomial near a positive cutoff. Their factorial-moment estimators have controlled total variance. An empirical estimator covers the very small-gap regime, and a Poisson sample cap converts the proof to a deterministic sample budget.

Appendix A supplies the positive-kernel construction, both localized moment calculations, countable expectation/variance summability, and the order of universal constant choices. The two audits are `support_audit.md` and `root_review.md`. No numerically usable constants or executed implementation of this tester are claimed. Source comparison: [S1], §1.4 and Appendix C.2.

### 2.2 Q858: a vertex-count CLT without connectedness

For every fixed arbitrary probability law on unordered pairs of distinct natural numbers,

\[
\boxed{\operatorname{Var}(|V_n|)\longrightarrow\infty
\quad\Longrightarrow\quad
\frac{|V_n|-\mathbb E|V_n|}{\sqrt{\operatorname{Var}(|V_n|)}}
\Rightarrow N(0,1).}
\]

This is the exact fixed-sample, loopless, countable, no-dust statement. There is no connectedness, maximum-degree, regular-variation, or minimum variance-growth condition. Sources [S4], [S7], and [S8] were compared at their stated versions; the argument here is not presented as a published result from those sources.

The proof has three substantive parts. Under Poissonization, edge-presence variables are independent and each edge affects only its two endpoint indicators. A read-two Cauchy–Schwarz inequality bounds the centered real moment generating function in terms of

\[
B(t)=\sum_v e^{-tp_v}(1-e^{-tp_v}),\qquad p_v=\Pr(v\in E_1),\quad\sum_vp_v=2.
\]

An elementary unit-disc contraction proves that the finite covered-count generating polynomial has no zeros in \(\operatorname{Re}z>1/2\). The absent-vertex expansion is a ferromagnetic graph polynomial, so this is a special Lee–Yang argument proved directly in the appendix. The nonvanishing region converts the real bound into cumulant bounds

\[
B(t)\le\operatorname{Var}(|V_{N(t)}|)\le2B(t),\qquad
|\kappa_j(|V_{N(t)}|)|\le j!e2^{j-1}B(t),\quad j\ge2.
\]

Higher standardized cumulants vanish when the variance diverges. Countable truncation is justified by \(|V_{N(t)}|\le2N(t)\), which supplies all exponential moments. Finally, the proof compares fixed and Poissonized variances and controls random sample-count fluctuations using

\[
\frac{n(\sum_vp_ve^{-np_v})^2}{B(n)}
\le\sum_vp_v\frac{np_v}{e^{np_v}-1}\longrightarrow0.
\]

The last limit follows from dominated convergence against the summable masses \(p_v\); it handles arbitrarily slow variance divergence. Appendix B gives every step. No variance estimator or finite-sample confidence interval is supplied by this CLT.

### 2.3 Q855: linear rarity is not the sharp iid upper order

For iid observations and \(0\le\zeta\le n/2\), cumulative Good–Turing

\[
G_\zeta=\frac1n\sum_{r=1}^{\zeta+1}r\Phi_r
\]

estimates the realized rare mass \(M_{\le\zeta}=\sum_xp_x\mathbf1\{N_x\le\zeta\}\) with

\[
\boxed{\sup_p\mathbb E(G_\zeta-M_{\le\zeta})^2
\le\min\{1,22\sqrt{\zeta+1}/n\}.}
\]

The proof works directly with fixed-size multinomial samples. Exact second-moment identities preserve cancellations between consecutive frequency classes; a binomial point-mass bound then produces the square-root dependence. It was independently checked algebraically and against 235 exact rational cases.

For any observation sequence, the complementary plug-in estimator obeys a pointwise Cauchy–Schwarz bound over the at most \(n/(\zeta+1)\) frequently observed symbols. It yields

\[
R^{\rm iid}_{n,\zeta}\le
\min\left\{1,\frac{22\sqrt{\zeta+1}}n,\frac1{\zeta+1}\right\},
\]

and, combining with the existing WingIt theorem [S2],

\[
R^{\rm Markov}_{n,\zeta,T}\le
C\min\left\{1,\frac{(\zeta+1)T\log(1+n/T)}n,\frac T{\zeta+1}\right\}.
\]

These are upper envelopes, not asserted minimax equalities. The first proves that a lower bound proportional to \((\zeta+1)/n\) cannot hold uniformly when \(\zeta\to\infty\), \(\zeta=o(n)\): the risk ratio is at most \(22/\sqrt{\zeta+1}\to0\). Thus one sharpness possibility is disproved, while the full joint frontier remains open. Appendix C, Theorems M1–M2, gives the details.

### 2.4 Q859: unconditional exposure and realized rare mass have different rates

For the iid subproblem, when \(\zeta_n\to\infty\) and \(\zeta_n=o(n)\), the minimax MSE for the *unconditional* next-token probability is

\[
\boxed{\inf_{\widehat S}\sup_p\mathbb E(\widehat S-S_{\zeta_n}(p))^2
\asymp\zeta_n/n.}
\]

The upper bound combines the cumulative-Good–Turing result with the variance of the realized rare mass. The lower bound uses a heavy atom plus a uniform group of small atoms, varying only the group's total mass. Statistically hard perturbations of order \(n^{-1/2}\) move the target by order \(\sqrt{\zeta/n}\). A uniform Stirling expansion and a two-point testing bound establish the claimed order without assuming \(\zeta^2/n\to0\).

For general Markov chains the quadratic rarity factor remains unresolved. Appendix C reproduces the finite-sample bias terms of [S5], Corollary 2. With \(r=n/T\ge4\), \(L=\lceil\log_2r\rceil\), it gives

\[
\operatorname{MSE}\le\min\left\{1,
\frac{64(1+L)^2}{r^2}+\frac{4(\zeta+1)^2L^2}{r^2}
+\frac{18(2\zeta+5)^2}{r}\right\}.
\]

This full display prevents a leading-order shorthand from silently discarding relevant growing-parameter bias. A separate exact replacement example shows why a proof based only on worst-case coordinate changes retains a quadratic rarity factor; that is a method limitation, not a minimax lower bound.

### 2.5 Q854: the variance conjecture holds for every refresh chain

For \(P=(1-a)I+a\mathbf1\pi^\top\), initialized at stationarity,

\[
\boxed{\operatorname{Var}(M_0)\le\min\{1/4,1/(an)\}
\le\min\{1/4,2T/n\}.}
\]

Explicit avoidance probabilities show pairwise nonpositive covariance of missing indicators in this family. Uniform-state examples with \(a\to0\), \(na\to\infty\), and \(K\sim na\) have variance of order \(T/n\), so the linear dependence is needed even here. Arbitrary Markov kernels need not share the covariance property; Q854 remains partial.

The same construction gives an exact estimand warning: its conditional next-token discovery probability is \(aM_0\), and its unconditional value is \(a\mathbb EM_0\). A stationary missing-mass estimate alone does not estimate the immediate next-token probability.

### 2.6 Q856: a restricted-class barrier and the JASA reconciliation

The unrestricted exact constant remains unresolved. The new restricted theorem says that for every fixed positive integer \(R\), the best asymptotic worst-case constant among unclipped estimators with deterministic coefficients \(\sum_{r=1}^R\beta_{r,n}\Phi_r\) is

\[
c_{GT}=\max_{a>0}\{(1+a)e^{-a}-e^{-2a}\}
=0.608036786522882\ldots.
\]

Uniform occupancy profiles force any such estimator with \(O(1/n)\) risk to approach Good–Turing's coefficient vector; the residual random fluctuation cannot remove its leading least-favorable risk. This leaves nonlinear procedures, clipping, and a growing number of coefficients outside the result. Appendix D supplies the full argument and identifies its one imported dependency, the sharp global GT upper bound in [S3], Theorem 4.

The official supplement to Painsky's JASA paper [S9], Eq. (G73), was obtained and inspected. That particular unrestricted-alphabet estimator differs uniformly from GT by at most \(2.08n^{-0.7}=o(n^{-1/2})\), so it has the same leading constant. Its improvement does not settle whether the general minimax constant equals the uniform-family candidate \(c_u=0.5700772328176\ldots\). The main paywalled article was not represented as fully retrieved.

## 3. Controlled-generator experiment

Four known generators were run at 500, 2,000, and 8,000 tokens, with 400 stationary trajectories per configuration: iid uniform, iid finite Zipf with exponent 1.1, and uniform refresh chains with probabilities 0.1 and 0.02. Every alphabet had 2,000 states. The seed was 20261007; the budget was 16.8 million tokens over 4,800 trajectories. All complete trajectories are preserved as compressed arrays. The loss is squared error against the realized stationary missing mass computed from the known stationary law.

The following table shows the 8,000-token configurations. “WingIt” uses the exact known mixing-time parameter and the theoretical window, with a one-token window in the iid controls. Parentheses give the Monte Carlo standard error of the MSE estimate.

| Generator | Mixing time T | Mean true M0 | GT MSE | WingIt MSE |
|---|---:|---:|---:|---:|
| iid uniform | 1 | 0.01840 | 0.00001154 (0.00000085) | 0.00001154 (0.00000085) |
| iid Zipf, exponent 1.1 | 1 | 0.06695 | 0.00001546 (0.00000103) | 0.00001546 (0.00000103) |
| Refresh probability 0.1 | 14 | 0.66979 | 0.43992 (0.00069) | 0.0008356 (0.0000614) |
| Refresh probability 0.02 | 69 | 0.92261 | 0.85056 (0.00054) | 0.0012601 (0.0000766) |

These results verify behavior on the declared finite controls. They do not prove a minimax rate or resolve Q853. Mixing time was calculated from the known generator, not inferred from lag correlations. Exact uniform-family means and variances were also calculated and retained alongside the Monte Carlo summaries.

## 4. Chronological prose pilot

Two original-English public-domain book texts were obtained from Project Gutenberg [S15–S16]. The exact files, license wrappers, cleaning rules, tokens, and hashes are bundled. The retained narratives contain 26,613 tokens in *Alice's Adventures in Wonderland* and 122,169 in *Pride and Prejudice*. The latter edition's editorial preface and illustration captions were explicitly removed. Tokenization uses NFC normalization, Unicode casefolding, letters with internal apostrophes, and no lemmatization or stopword removal.

The design used 1,000, 3,000, and 5,000 training tokens, future-to-training ratios 0.5, 1, and 2, and three chronological positions per book: 18 training windows and 54 evaluations. The windows overlap; they are descriptive comparisons, not independent replicates. No stationary or iid law was asserted for the novels.

The Good–Turing diagnostic was below the realized proportion of future tokens whose types were absent from training in all 54 evaluations, by 0.8–8.5 percentage points. Poisson-smoothed Good–Toulmin, with fixed smoothing mean 3 and sensitivity means 2 and 4, underestimated distinct new types in 52 of 54 evaluations. The formula was checked against [S14]; no statistical guarantee for this fixed smoothing choice on chronological prose is claimed.

At 5,000 training tokens followed by 10,000 future tokens, the three-position means were:

| Corpus | GT mass diagnostic | Held-out novel-token proportion | Predicted new types | Observed new types |
|---|---:|---:|---:|---:|
| Alice | 10.45% | 17.50% | 654.50 | 885.67 |
| Pride and Prejudice | 12.90% | 17.19% | 805.47 | 1,142.00 |

One Alice window produced 459.15, 409.77, and 235.52 predicted new types under smoothing means 2, 3, and 4, versus 684 observed. The 223.63-type sensitivity is a recorded failure of stable extrapolation in that window. It is not an impossibility theorem about prose or the iid model.

Independent implementations of the handoff's observed-diversity definitions were also run on the same 18 training windows, retaining their reliability floors. For the 5,000-token windows:

| Corpus | MTLD .720 | MATTR 50 | HD-D 42 | Maas, natural log |
|---|---:|---:|---:|---:|
| Alice | 83.42 | 0.80254 | 0.85510 | 0.021942 |
| Pride and Prejudice | 100.67 | 0.82496 | 0.87001 | 0.020365 |

These measurements describe observed tokens. They are separate from coverage and extrapolation. Both logarithm bases are retained for Maas because the handoff did not specify the base. Exact parity with the unavailable original `prosescan` implementation is not asserted.

### Consequence for a prose tool

The evidence supports an experimental coverage panel with explicitly declared tokenization, sample budget, corpus boundaries, sampling model, and held-out checks. It should show observed diversity, missing-mass diagnostics, and future new-type predictions as different quantities. When only chronological text is available, the present experiments support reporting calibration error and smoothing sensitivity. They do not support a universal author-vocabulary total, an author-quality ranking, or an iid confidence interval represented as calibrated for arbitrary prose.

## 5. Verification and reproducibility

The archive contains every authored proof, review, executed script, computational input, configuration, and raw output cited here. All original generator trajectories and exact prose token sequences are included. `MANIFEST.json` records hashes and byte sizes; `verify_archive.py` checks them. The main experiments run from the extracted archive with Python 3.12, NumPy 2.3.5, and SciPy 1.17.0. The optional plot additionally uses Matplotlib. `README.md` lists the commands.

| Evidence | Executed scope | Meaning |
|---|---|---|
| Q855 exact enumeration | 235 configurations, 2,893 count vectors | Rational checks of moment identities and finite inequalities |
| Q856 exact checks | 70 configurations, 9,940 count-vector visits | Rational validation of occupancy risk formulas |
| Q856 numerical exploration | bounded optimizer and five large uniform evaluations | Numerical evidence only; no certified minimax optimization |
| Q858 finite checks | 829 graph models; 625 fixed-sample checks | Exact polynomial/variance identities plus floating-point roots |
| Markov controls | 4,800 trajectories, 16.8 million tokens | Bias/MSE and exact-truth controls for declared generators |
| Prose pilot | 148,782 tokens, 54 evaluations | Chronological calibration and extrapolation sensitivity |
| Observed diversity | same 18 training windows | Separate implementations of the supplied definitions |
| Formal proof compilation | not run | No compiled theorem or kernel certificate |
| Q852 polynomial tester | not implemented | Sample-complexity proof only |

The official Painsky supplement/code has documented CC BY 4.0 metadata and is bundled. Other external papers are cited by exact URL and version; copies with uncertain redistribution status are represented by retrieval hashes. They are not inputs required by the numerical scripts. The full originating user handoff is included unchanged.

## 6. Residual research programme

The exact unresolved rate questions are Q851 and Q853. Q854 needs a general-kernel variance argument; pairwise-negative missing-indicator covariance cannot be assumed outside the proved family. Q855 now needs matching lower bounds for the improved upper envelope. Q856 needs methods beyond the fixed finite deterministic linear class. Q859 needs an argument that controls joint rarity and Markov dependence more sharply than worst-case coordinate sensitivity.

For the two completed statements, the next mathematical task is external checking of the written proofs and, if desired, formalization. For prose measurement, the next empirical task is broader corpus validation under explicit units and stable preprocessing, with uncertainty assessed against actual held-out observations. The pilot's failure cases are part of the result and should remain visible.

## 7. Original statement register

### Q851 — The remaining accuracy cost of support-size diagnosis

**B8; stable ID:** `c72db31c0497eb836a83`. **Disposition:** unresolved.

Close the minimax gap Ω(n/(ε log n)) versus O((n/(ε log n))min{log(1/ε), log n}) for distinguishing d_n(p)=0 from d_n(p)>ε.

**Remaining:** Close the epsilon-dependent logarithmic gap in the non-tolerant sample complexity.

### Q852 — Tolerant support diagnosis without a support-size promise

**B8; stable ID:** `f9edd65b797563064576`. **Disposition:** proved.

For 0≤ε′<ε<1, can d_n(p)≤ε′ versus d_n(p)>ε be tested with (n/log n)·Õ((ε−ε′)⁻²) samples, without a bound on the true support?

**Remaining:** Exact assigned sample-rate existence question answered by written proof. Practical constants, stable implementation and further lower bounds are separate unfinished work.

### Q853 — Removing the log cost of dependent missing-mass estimation

**B8; stable ID:** `07232484a765905b847d`. **Disposition:** unresolved.

Is minimax MSE for M₀ O(T/n) when n≳T log n, removing the known log(n/T) factor?

**Remaining:** A general O(T/n) estimator or a lower bound ruling it out remains absent.

### Q854 — Linear mixing-time variance of unseen stationary mass

**B8; stable ID:** `ad6c67395090a5839dec`. **Disposition:** partial.

Does Var(M₀)≤C min{T log(1+n/T)/n, 1} hold universally, replacing T² in Theorem 2?

**Remaining:** Remove the refresh-kernel restriction; the universal conjecture is not established.

### Q855 — The rare-count mass estimation frontier

**B8; stable ID:** `eeea824c340739a51a8d`. **Disposition:** partial.

For 1≤ζ=o(n), determine minimax MSE for M_ζ jointly in n,ζ, T. Are O(min{(ζ+1)T log(1+n/T)/n, 1}) and iid O(min{(ζ+1)/n, 1}) sharp?

**Remaining:** Find matching lower bounds for the improved iid envelope and determine the full joint Markov frontier.

### Q856 — The exact minimax constant for unseen probability mass

**B8; stable ID:** `eee2f3c01977fe365b97`. **Disposition:** partial.

For iid X₁: n∼p on an unrestricted countable alphabet, let M₀=Σ_xp_x1{N_x=0} and R_n*=inf_Mhat sup_p E_p[(Mhat−M₀)²]. Does lim_n nR_n* exist, and is it c_u=max_{x∈(0, 1]} x e^(−x)(1−e^(−x))²/[1−e^(−x)−x e^(−x)]≈0.570077, the uniform-family constant?

**Remaining:** Prove existence/value of the unrestricted minimax limit; the fixed finite linear class cannot settle it.

### Q858 — Gaussian uncertainty for distinct entities observed in pairs

**B8; stable ID:** `0c3cb5efa6b7fd0651a8`. **Disposition:** proved.

For iid unordered pairs E_i of distinct natural numbers with arbitrary fixed law μ, set V_n=∪_{i≤n}E_i. Does Var(|V_n|)→∞ imply (|V_n|−E|V_n|)/sqrt(Var(|V_n|))⇒N(0, 1), without eventual connectedness? This is the loopless countable-support model, without dust.

**Remaining:** Exact assigned CLT answered by written proof. Variance estimation, finite-sample inference and broader hyperedge models remain separate.

### Q859 — Linear rarity cost for next-event exposure estimation

**B8; stable ID:** `11f05c2567c0a33574c8`. **Disposition:** partial.

For a stationary finite-state ergodic Markov trajectory X₁: n+1, let S_ζ=Pr{N_{X_{n+1}}(X₁: n)≤ζ}, an unconditional probability. Determine minimax MSE’s optimal ζ-dependence from X₁: n. Can the leading O((ζ+1)²T/n) bound become O((ζ+1)T/n), where T is a worst-start TV mixing-time bound? Retain Corollary 2’s finite-n bias terms, or state a valid growing-parameter regime. The ζ=0 case is settled.

**Remaining:** Establish optimal joint rarity/mixing dependence for general Markov chains; iid rate and finite-bias specialization alone do not close it.

## 8. Primary-source catalog

- **[S1]** Renato Ferreira Pinto Jr.; Nathaniel Harms. *Testing Support Size More Efficiently Than Learning Histograms*. TheoretiCS 5, Article 10, published 21 May 2026; arXiv v4 dated 20 May 2026. Theorem 1.3, p.3; Section 1.4, p.7; Appendix C.2, pp.41–42. [Primary source](https://theoretics.episciences.org/18250/pdf). Retrieval scope: primary full text.
- **[S2]** Ashwin Pananjady; Vidya Muthukumar; Andrew Thangaraj. *Just Wing It: Near-Optimal Estimation of Missing Mass in a Markovian Sequence*. JMLR 25, 2024, 43 pages. Theorem 1 and Eq.18, pp.10–11; Theorem 2 and Eq.20, pp.11–12; Theorem 3 and Eqs.25–27, pp.12–14. [Primary source](https://jmlr.org/papers/volume25/24-0511/24-0511.pdf). Retrieval scope: primary full text.
- **[S3]** Jayadev Acharya; Yelun Bao; Yuheng Kang; Ziteng Sun. *Mean Squared Error of Missing Mass Estimation*. author working manuscript, 15 December 2017; associated ISIT 2018 proceedings. Section 3, pp.4–6; Theorems 4–6. [Primary source](https://people.ece.cornell.edu/acharya/papers/missing-mass-mse.pdf). Retrieval scope: primary full text.
- **[S4]** Svante Janson. *On Edge Exchangeable Random Graphs*. Journal of Statistical Physics 173 (2018), 448–484; online 2017. Problem 6.9, journal p.464 / PDF p.17. [Primary source](https://uu.diva-portal.org/smash/get/diva2:1273609/FULLTEXT01.pdf). Retrieval scope: primary full text.
- **[S5]** Milind Nakul; Vidya Muthukumar; Ashwin Pananjady. *Next-token functional estimation*. arXiv:2609.19529v1, 17 September 2026. Section 4.2 and Corollary 2; Appendix A.3, Lemma 5. [Primary source](https://arxiv.org/html/2609.19529v1). Retrieval scope: primary full text.
- **[S6]** Milind Nakul; Vidya Muthukumar; Ashwin Pananjady. *Estimating stationary mass, frequency by frequency*. arXiv:2503.12808 / COLT 2025. problem formulation and main vector-risk theorem. [Primary source](https://arxiv.org/abs/2503.12808). Retrieval scope: primary setup and principal statements; scope comparison.
- **[S7]** Edward Eriksson. *Edge Exchangeable Graphs: Connectedness, Gaussianity and Completeness*. arXiv:2501.09511v2, revised 6 May 2026. Section 4; Theorem 14; Proposition 16; Corollary 18. [Primary source](https://arxiv.org/html/2501.09511v2). Retrieval scope: primary full text.
- **[S8]** Edward Eriksson. *The Unseen Species Problem Revisited*. arXiv:2602.08769v4, revised 9 September 2026. footnote 3 and generalized-sampling setup. [Primary source](https://arxiv.org/html/2602.08769v4). Retrieval scope: primary exact scope/status passages.
- **[S9]** Amichai Painsky. *Generalized Good-Turing Improves Missing Mass Estimation: official supplement and implementation*. JASA 118(543), 2023; online 31 January 2022; official Figshare materials. Supplement Appendix G, Eq.G73, p.32; Eq.G94, pp.38–41. [Primary source](https://tandf.figshare.com/articles/dataset/Generalized_Good-Turing_Improves_Missing_Mass_Estimation/17308517). Retrieval scope: official supplement and implementation; main article paywalled.
- **[S10]** Gregory Valiant; Paul Valiant. *Instance Optimal Learning*. author manuscript, 10 December 2015. Definition 3, pp.6–7; Theorem 2, p.8. [Primary source](https://theory.stanford.edu/~valiant/papers/optlearning_arxiv.pdf). Retrieval scope: primary definitions and theorem.
- **[S11]** T. D. Lee; C. N. Yang. *Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model*. Physical Review 87 (1952), 410–419. . [Primary source](https://doi.org/10.1103/PhysRev.87.410). Retrieval scope: bibliographic attribution; required special case reproved in Appendix B.
- **[S12]** David Ruelle. *Extension of the Lee–Yang Circle Theorem*. Physical Review Letters 26 (1971), 303–304. . [Primary source](https://doi.org/10.1103/PhysRevLett.26.303). Retrieval scope: bibliographic attribution; unit-disc contraction reproved in Appendix B.
- **[S13]** D. Gavinsky; S. Lovett; M. Saks; S. Srinivasan. *A Tail Bound for Read-k Families of Functions*. Random Structures & Algorithms 47 (2015). . [Primary source](https://www.cs.toronto.edu/tss/files/papers/1205.1478.pdf). Retrieval scope: read-k/Finner attribution; read-two lemma reproved in Appendix B.
- **[S14]** Alon Orlitsky; Ananda Theertha Suresh; Yihong Wu. *Optimal prediction of the number of unseen species*. PNAS 113(47), 13283–13288 (2016). Smoothed Good–Toulmin Estimator section. [Primary source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127330/). Retrieval scope: primary estimator definition.
- **[S15]** Lewis Carroll. *Alice's Adventures in Wonderland*. Project Gutenberg ebook 11, downloaded 7 October 2026. . [Primary source](https://www.gutenberg.org/ebooks/11). Retrieval scope: exact raw text and metadata.
- **[S16]** Jane Austen. *Pride and Prejudice*. Project Gutenberg ebook 1342, edition updated 29 September 2026, downloaded 7 October 2026. . [Primary source](https://www.gutenberg.org/ebooks/1342). Retrieval scope: exact raw text and metadata.

---

## Appendix A. Complete support-diagnosis proof

## B8 support diagnosis: Q852 proved by independently reviewed written argument; Q851 unresolved

Date: 2026-10-07. Evidence: primary-source comparison and a written mathematical argument that passed two independent in-session proof audits. No proof assistant was run. The support estimator was not numerically implemented or executed; no simulation is used as evidence for its theorem. No claim of publication, external peer review, or literature priority is made.

### Statements and dispositions

- **Q851**, stable ID `c72db31c0497eb836a83`: Close the minimax gap `Omega(n/(epsilon log n))` versus `O((n/(epsilon log n)) min{log(1/epsilon),log n})` for distinguishing `d_n(p)=0` from `d_n(p)>epsilon`, with iid samples on an unrestricted countable alphabet. **Unresolved here.** No improved non-tolerant minimax rate is established.
- **Q852**, stable ID `f9edd65b797563064576`: For `0 <= epsilon' < epsilon < 1`, test `d_n(p)<=epsilon'` against `d_n(p)>epsilon` with `(n/log n) tilde-O((epsilon-epsilon')^-2)` iid samples, without bounding the actual support. **Proved by independently reviewed written argument below.** The theorem gives an explicit upper bound `C n log^2(e/delta)/(delta^2 log(en))`, where `delta=epsilon-epsilon'`. It estimates `d_n` itself and applies to every countable distribution. The construction is mathematical; no numerical implementation or formal kernel checking is claimed.

### Primary sources checked

1. Ferreira Pinto Jr. and Harms, *Testing Support Size More Efficiently Than Learning Histograms*, TheoretiCS 5, Article 10, 2026, DOI https://doi.org/10.46298/theoretics.26.10 ; journal PDF https://theoretics.episciences.org/18250/pdf . ArXiv record https://arxiv.org/abs/2410.18915 identifies v4, 20 May 2026; journal publication 21 May 2026. Theorem 1.3 (printed p.3) gives the non-tolerant upper bound. Section 1.4 (p.7) still asks both assigned questions. Appendix C.2 (pp.41–42) sketches, without completing it, a weaker histogram-metric route.
2. Gregory and Paul Valiant, *Instance Optimal Learning*, author manuscript dated 10 December 2015, https://theory.stanford.edu/~valiant/papers/optlearning_arxiv.pdf ; arXiv https://arxiv.org/abs/1504.05321 . Definition 3 (pp.6–7) gives truncated relative earthmover distance; Theorem 2, Section 2 (printed p.8), gives histogram recovery with threshold `w/(m log m)` and error `C/sqrt(w)` for `1<=w<=log m`. This source is needed only for the secondary metric corollary, not for the polynomial theorem.

The journal PDF and its arXiv version are same-origin copies, not independent confirmations. Searches did not identify a later source-published exact resolution; absence from these searches is not proof that none exists. The affirmative disposition below rests on the reviewed argument in this report.

### 1. Definitions and elementary facts

Let `p=(p_i)_{i in N}` be a countable probability distribution. Write its coordinates in decreasing order `p_(1)>=p_(2)>=...`, adding zeros if necessary. Such an ordering exists for summable nonnegative coordinates. Define

\[
C_n(p)=\sum_{i=1}^n p_{(i)},\qquad d_n(p)=1-C_n(p).
\]

The latter equals the TV distance from the distributions supported on at most `n` points: every such support `A` misses `p(A^c)`, and renormalizing `p` on a maximizing `n`-point set attains this distance (the zero-mass case is trivial).

For `t>=0`, put

\[
F_p(t)=\sum_i(p_i-t)_+,\quad \Phi_p(t)=nt+F_p(t).
\]

Then

\[
C_n(p)=\inf_{t\ge0}\Phi_p(t)=\Phi_p(p_{(n)}). \tag{1}
\]

Indeed, each summand `p_(i)` for `i<=n` is at most `t+(p_(i)-t)_+`; summing gives the lower inequality. At `t=p_(n)`, equality holds, including ties and zero cutoff. Notice `p_(n)<=1/n`.

#### Elementary empirical fallback

For empirical frequencies `p_hat` from `M` observations,

\[
|C_n(\widehat p)-C_n(p)|\le\sup_{|A|\le n}|\widehat p(A)-p(A)|
\le\sqrt n\|\widehat p-p\|_2.
\]

Moreover `E||p_hat-p||_2^2=(1-sum_i p_i^2)/M<=1/M`. Thus

\[
\Pr\{|d_n(\widehat p)-d_n(p)|>a\}\le {n\over Ma^2}. \tag{2}
\]

This proof is directly valid for countable support by Tonelli. In particular `O(n/delta^2)` samples estimate `d_n` to accuracy `delta/4` with fixed success probability. No support promise is present.

### 2. A useful deterministic polynomial sandwich

The essential feature is a **horizontal** error of size `h`, not a uniform additive error per symbol. Suppose, simultaneously over a grid of `t`, the expected estimates of `F_p(t)` lie between

\[
F_p(t)-\eta-b \quad\hbox{and}\quad F_p(t-h)+\eta+b, \tag{3}
\]

and realized estimates differ from those expectations by at most `a`. Here `t>=h`. Let

\[
t_j=jh,\quad 1\le j\le J=\lceil1/(nh)\rceil+1,
\quad \widehat C=\min_j\{nt_j+\widehat F(t_j)\}.
\]

Equation (1) gives `C_hat >= C_n-eta-b-a`. Choose `j=ceil(p_(n)/h)+1`; then `p_(n)+h<=t_j<=p_(n)+2h`, so

\[
nt_j+F_p(t_j-h)\le n(p_{(n)}+2h)+F_p(p_{(n)})=C_n(p)+2nh.
\]

Therefore clipping `C_hat` to `[0,1]` yields

\[
|\widehat C-C_n(p)|\le 2nh+\eta+b+a. \tag{4}
\]

This argument explains why the alphabet cardinality never enters the approximation error.

### 3. Explicit bounded polynomial steps

#### Lemma 1: a trigonometric kernel

There is an absolute constant `C` such that, for `0<a<=pi` and `0<eta<1/2`, an even nonnegative trigonometric polynomial `K` of degree at most `C a^-1 log(1/eta)` has integral one on `[-pi,pi]` and puts at most `eta` of its integral outside `[-a,a]`.

**Construction and proof.** Take integers `k>=4pi/a` and `q>=C_0 log(1/eta)`. Normalize to integral one the even nonnegative polynomial

\[
B_k(\theta)^q,
\qquad B_k(\theta)=\left({\sin(k\theta/2)\over k\sin(\theta/2)}\right)^2.
\]

It has degree `q(k-1)`. On `|theta|<=1/(k sqrt(q))`, the sine bounds give `B_k(theta)^q>=c`, so its integral is at least `c/(k sqrt(q))`. For `a<=|theta|<=pi`, `B_k(theta)<= (pi/(k|theta|))^2`. Integrating this bound and dividing by the lower normalization bound gives tail mass at most

\[
C{\sqrt q\over2q-1}\pi\left({\pi\over ka}\right)^{2q-1}\le C' q^{-1/2}4^{-(2q-1)},
\]

which is at most `eta` after fixing `C_0`. Taking `k=ceil(4pi/a)` proves the degree claim. The removable singularities are filled by continuity.

#### Lemma 2: polynomial sandwiches on a low-probability interval

For `0<h<=t<=r/4` and `0<eta<1/2`, there is a polynomial `P_t`, of degree at most

\[
1+C{\sqrt{rt}\over h}\log(1/\eta), \tag{5}
\]

such that `P_t(0)=0`, `0<=P_t(x)<=x` on `[0,r]`, and

\[
(x-t)_+-\eta x\le P_t(x)\le(x-t+h)_++\eta x \quad(0\le x\le r). \tag{6}
\]

**Proof.** Set `theta(x)=arccos(1-2x/r)`. The angular separation of `t-h` and `t` is at least `h/sqrt(rt)`, because `theta'(x)=1/sqrt(x(r-x))`. Let `theta_0` be their angular midpoint and use Lemma 1 with half that separation. Convolve the even circular indicator of the arc `[theta_0,2pi-theta_0]` with `K`. The result is an even trigonometric polynomial, hence a polynomial `S(x)` in `cos(theta)=1-2x/r`. It obeys `0<=S<=1`; it is at most `eta` for `x<=t-h`, and at least `1-eta` for `x>=t`. Put `P_t(x)=integral_0^x S(u)du`. Integrating these inequalities proves (6), and degree increases by one. The construction uses only `t,h,r,eta`.

#### Lemma 3: polynomial sandwiches near a positive cutoff

Let `0<w<=t/8`, `h>0`, and `0<eta<1/2`. There is a polynomial `P_t`, bounded between `0` and `4w` on `I=[t-2w,t+2w]`, of degree at most

\[
1+C\max\{1,w/h\}\log(1/\eta), \tag{7}
\]

which satisfies (6) for `x in I`.

**Proof.** If `h>=2w`, use `P_t(x)=x-(t-2w)`; the asserted sandwich is immediate. Otherwise repeat the preceding arc construction on `[t-2w,t+2w]` with transition `[t-h,t]`, and integrate from `t-2w`. The angular gap is at least `h/(2w)`. Its error is initially `eta(x-(t-2w))`; throughout the interval `x-(t-2w)<=4w<=t/2<=x`, which implies (6). Positivity and the bound `4w` follow from `0<=S<=1`.

### 4. Unbiased polynomial estimation and coefficient bounds

For a polynomial bounded in magnitude by `b` on an interval with midpoint `a` and half-width `s`, the coefficients of its expansion in powers of `(x-a)/s` have total absolute value at most `b A^L`, where `L` is the degree and `A` is a universal constant. To see this, expand in Chebyshev polynomials on `[-1,1]`: every Chebyshev coefficient is at most `2b`; the monomial coefficient norm of `T_j` grows at most geometrically by its recurrence. The sum of the first `L+1` geometric bounds can be absorbed into `A^L` for `L>=1`. The same conclusion, with another fixed `A`, holds for powers `x/r` on `[0,r]`.

Let `N~Poi(mp)`. For a center `a`, define

\[
u_j(N;a)=\sum_{k=0}^j {j\choose k}(-a)^{j-k}{(N)_k\over m^k},
\]

where `(N)_k` is the falling factorial and `(N)_0=1`. Then `E u_j=(p-a)^j`. More precisely,

\[
E[u_j(N;a)u_k(N;a)]
=\sum_{s=0}^{\min(j,k)}{j\choose s}{k\choose s}s!\left({p\over m}\right)^s(p-a)^{j+k-2s}. \tag{8}
\]

A complete verification is supplied by the exponential generating function

\[
\sum_{j\ge0}u_j(N;a){z^j\over j!}=e^{-az}(1+z/m)^N;
\]

the expectation of its product for `z,y` equals `exp((p-a)(z+y)+pzy/m)`. Coefficient comparison gives (8).

Replacing every `(p-a)^j` in `P(p)` by `u_j` gives an unbiased estimator `U_P(N)`.

We use independent count arrays `N_i,N'_i~Poi(mp_i)`, independent across `i`. These are obtained from two independent Poisson-sized iid samples, each of expected size `m`.

### 5. Low-probability estimator: full bias and variance bounds

There are universal constants `K_0,B,C,c>0` with the following property. Fix `L>=1`, `r=K_0 L/m`, `t<=r/4`, and a polynomial from Lemma 2 of degree at most `L`. Define

\[
Y_i=U_{P_t}(N_i)\mathbf1\{N'_i\le mr/2\}
+(N_i/m-t)\mathbf1\{N'_i>mr/2\},
\quad \widehat F(t)=\sum_iY_i. \tag{9}
\]

Then

\[
F_p(t)-\eta-Ce^{-cL}\le E\widehat F(t)
\le F_p(t-h)+\eta+Ce^{-cL}, \tag{10}
\]

and

\[
\operatorname{Var}(\widehat F(t))\le C{L\over m}B^L. \tag{11}
\]

The constants can be chosen so that the exponent `c` in the bias exceeds `1`, by increasing `K_0`; changing `K_0` affects only universal constants below.

**Variance proof.** Write `ell=mr=K_0 L`, `lambda=mp`, and `x=p/r=lambda/ell`. From (8) at center zero, for `1<=j,k<=L`, normalized factorial products are bounded in absolute expectation by

- `x exp(L^2/ell)` when `x<=1`, since every power `x^(j+k-s)` has exponent at least one;
- `x^(2L) exp(L^2/ell)` when `x>=1`.

The coefficient bound therefore gives `E U_P^2 <= C r^2 A^(2L) exp(L/K_0)` times the appropriate expression in `x`. For `x>=1`, the low-count gate has probability at most `exp(-lambda/8)`. Since `log x<=x-1`, choosing `K_0>=32` gives

\[
x^{2L}e^{-K_0Lx/8}\le x.
\]

Consequently, for every `p`,

\[
E[U_P(N)^2\mathbf1_{\mathrm{low}}]\le C rp B^L. \tag{12}
\]

For `W=(N/m-t)1_high`, independence of the two samples gives

\[
\operatorname{Var}(W)={p\over m}\beta+(p-t)^2\beta(1-\beta),
\]

where `beta=Pr(high)`. The second term is at most `Cpr`: for `p>=r` use the low-count exponential bound; for `t/2<=p<=r`, use `(p-t)^2<=4pr`; for `p<t/2`, Markov's inequality gives `beta<=2p/r` and `t^2<=r^2`. Thus `Var(Y_i)<=2E[U_P^2 1_low]+2Var(W)<=C rp B^L+2p/m`. Sum over `i` to get (11).

**Bias proof.** For `p<=r`, the polynomial sandwich survives mixing with the exact branch `(p-t)_+`, except that the linear high branch is negative when `p<t`. Its extra loss is at most `t Pr(high)`. For `p<t<=r/4`, the Poisson upper tail has the mass-weighted bound

\[
\Pr\{\operatorname{Poi}(mp)>mr/2\}\le C(p/r)e^{-c_0mr}. \tag{13}
\]

For completeness, apply Markov to `2^N-1`: the numerator is `exp(mp)-1<=mp exp(mp)`, while the denominator is at least a constant times `2^(mr/2)`. Since `mp<=mr/4`, the result is `C(mp)exp(-c mr)`, and the factor `mr` is absorbed into a slightly weaker exponential. Hence the summed wrong-branch loss is exponentially small. For `p>r`, the coefficient bound gives `|P(p)|<=Cr A^L(p/r)^L`; multiplication by the low-gate probability `exp(-mp/8)` bounds the bias by `Cp(A^L+1)exp(-mr/8)`. Summing uses `sum p=1`; increasing `K_0` dominates `A^L`. This proves (10).

**Countable alphabet check.** Since `P(0)=0`, terms with `N_i=N'_i=0` vanish, so the sum is almost surely finite. To justify expectation interchange explicitly, expand the polynomial in powers of `p/r`. For `p<=r`, its lack of a constant term and the factorial moments give `E|U_P(N)|<=C A^L p`. For `p>r`, the same expansion gives `E|U_P(N)|<=Cr A^L(p/r)^L`; multiplication by the independent low-gate probability makes this at most `C A^L p`. Also `E|N/m-t| beta <=p+t beta<=Cp`, using `beta<=2p/r` and `t<=r/4`. Therefore `sum_i E|Y_i|<infinity`. The finite variance sum in (11) and independence give L2 convergence of the centered sums, so the countable expectation and variance formulas are justified.

### 6. Local estimator: full bias and variance bounds

Choose a universal constant `K` sufficiently large, and suppose

\[
t>64KL/m,\quad w=\sqrt{KtL/m}<t/8.
\]

Use the polynomial of Lemma 3, of degree at most `L`, and let

\[
Y_i=
\begin{cases}
0,&N'_i/m<t-w,\\
U_{P_t}(N_i),&|N'_i/m-t|\le w,\\
N_i/m-t,&N'_i/m>t+w.
\end{cases} \tag{14}
\]

The same bounds (10)–(11) hold, with universal constants and bias `Ce^{-cL}`. Here the polynomial is expanded about center `t`; it need not vanish at zero, because the middle gate excludes `N'_i=0`.

The details that prevent an implicit finite-support assumption are recorded next.

#### 6.1 Polynomial second moment

Write `v=|p-t|/(2w)`. The coefficient bound and (8) give

\[
E U_P(N)^2\le Cw^2 A^{2L}e^{CL/K}\max\{1,v\}^{2L}. \tag{15}
\]

Indeed, if `v<=1`, then `p<=t+2w<=5t/4`, and the factorial-product sum is bounded by `exp(L^2p/(4mw^2))<=exp(CL/K)`. If `v>=1`, factor out `v^(j+k)`, bounding the residual exponential by `exp(L^2p/[m(p-t)^2])`. Using `p<=t+|p-t|`, `|p-t|>=2w`, `mw>=8KL`, and `w^2=KtL/m` bounds this exponent by `CL/K` as well.

#### 6.2 The middle gate away from the interval

For `|p-t|>2w`, standard exponential-Markov bounds, obtained by optimizing the Poisson moment generating function, imply

\[
\gamma(p):=\Pr\{|N'/m-t|\le w\}
\le\exp\left[-{m(p-t)^2\over8\max(p,t)}\right]. \tag{16}
\]

For the lower tail use `Pr(Poi(lambda)<=lambda-s)<=exp(-s^2/(2lambda))`; for the upper tail use `Pr(Poi(lambda)>=lambda+s)<=exp(-s^2/(2(lambda+s)))`. In (16), the gap to the gate is at least `|p-t|/2`.

For `v>=1`, `2w/t<=1/4` gives

\[
{m(p-t)^2\over8\max(p,t)}
\ge{KL\over2}{v^2\over1+(2w/t)v}\ge {2\over5}KLv.
\]

Consequently `gamma(p) v^(2L)<=exp(-cKL)` for sufficiently large `K`, by `log v<=v-1`. Equations (15)–(16) control all symbols with `p>=t/2`. There are at most `2/t` such symbols, so their total middle-branch second moment is at most `C(w^2/t)B^L`.

For the infinitely many possible symbols with `p<t/2`, the additional essential factor is

\[
\gamma(p)\le\Pr\{N'/m\ge t-w\}\le C(p/t)e^{-cmt}. \tag{17}
\]

To verify (17), use the `2^N-1` argument from (13); the threshold is at least `7mt/8`, while `mp<=mt/2`, giving a strictly negative constant times `mt` in the exponential. The factor `mp=(p/t)mt` is absorbed as before. Put `y=mt/(KL)>=64`. Then `v<=t/(2w)=sqrt(y/4)`, and `v^(2L)<= (y/4)^L`. For large fixed `K`, this power is dominated by `exp(-cKLy)` in (17), uniformly in `y>=64`. Summing (15) times (17) therefore gives another `C(w^2/t)B^L`, using only `sum p=1`.

#### 6.3 Variance of the linear branch

For `W=(N/m-t)1_high`, its variance is `beta p/m+beta(1-beta)(p-t)^2`. For `p>=t/2`, this second term is `O(w^2)` per symbol: this is immediate if `|p-t|<=2w`; otherwise the appropriate one-sided version of (16) makes `(p-t)^2` times the relevant rare-gate probability at most `Cw^2`. The number of these symbols is at most `2/t`.

For `p<t/2`, (17), applied to the still higher high gate, bounds the second term by `Cpt exp(-cmt)`. Its sum is at most `Ct exp(-cmt)<=C/m<=Cw^2/t`. Thus `sum Var(W_i)<=C/m+Cw^2/t`.

Using `Var(Y_i)<=2E[U_P^2 1_middle]+2Var(W_i)`, then `w^2/t=KL/m`, proves (11).

#### 6.4 Bias

On the interval `[t-2w,t+2w]`, (6) bounds the middle branch. Replacing each non-middle branch by the correct hinge produces only a **downward** error: when `p>t`, an erroneous low classification loses `p-t`; when `p<t`, an erroneous high classification contributes `p-t<0`.

For `p>=t/2`, those wrong-branch losses are bounded by `Cw exp(-cKL)` per symbol. For example, when `p=t+d>=t`, the wrong low gate has tail at most

\[
\exp[-m(d+w)^2/(2(t+d))],
\]

and `m(d+w)^2/(t+d)>=cKL(1+d/w)`. The analogous upper-tail inequality applies for `p<t`. Summation costs at most `2/t`, and `w/t<=1/8`. For `p<t/2`, the loss is at most `t` times the probability in (17), so its sum is at most `C exp(-cmt)`.

Outside the polynomial interval, its coefficient bound gives `|P(p)|<=Cw A^L max(1,v)^L`; the exact hinge is bounded by `2wv` when nonzero. Equations (16)–(17), with the same two classes `p>=t/2` and `p<t/2`, make the summed contribution of `gamma(p)|P(p)-(p-t)_+|` at most `C exp(-cL)`; increasing fixed `K` absorbs `A^L`.

Inside the interval the summed sandwich error is at most `eta sum p<=eta`; outside it the just-established exponential bound applies. These observations prove (10).

**Countable alphabet check.** Here `t-w>0`; a symbol absent from the second sample enters neither the middle nor the high branch, so the statistic is almost surely finite. For absolute expectation summability, there are only finitely many `p>=t/2`. For `p<t/2`, independence gives `E[|U_P(N)| 1_middle]=gamma(p) E|U_P(N)|<=gamma(p) sqrt(E U_P(N)^2)`. Substitution of (15) and (17) retains the full factor `p/t`; the same exponential domination used above bounds this by `Cw B^L(p/t)`. This is summable. The linear branch satisfies `E|N/m-t| beta<=p+t beta<=Cp`: use `t<=2p` for `p>=t/2` and (17) for the other atoms. Hence `sum_i E|Y_i|<infinity`. Independence and the summable variances give L2 convergence of centered sums, completing the justification for the countable expectation and variance formulas.

### 7. Theorem: unrestricted tolerant support diagnosis at the requested rate

**Theorem (independently reviewed written argument).** There is an absolute constant `C` such that for every integer `n>=1`, every `0<delta<1`, and every countable distribution `p`, an estimator based on at most

\[
C\,{n\log^2(e/\delta)\over\delta^2\log(en)} \tag{18}
\]

iid observations satisfies

\[
\Pr_p\{|\widehat d_n-d_n(p)|>\delta/4\}\le1/4.
\]

Consequently, with `delta=epsilon-epsilon'`, comparing `d_hat` to `(epsilon+epsilon')/2` answers Q852 with success at least `3/4`, for all `0<=epsilon'<epsilon<1`. No upper bound on `|supp(p)|` is used.

#### Proof and order of constant choices

It suffices initially to prove the theorem for large `n` and `delta<=1/2`.

1. Fix the universal kernel constants and coefficient constant `A`. Choose `K` sufficiently large for the local bias and moment bounds. Set the low-interval constant `K_0=256K`, increasing it if needed for the low estimator. Both estimators then have variance `C(L/m)B^L` and exponentially decreasing bias `C exp(-c_1L)` for fixed universal `B,c_1>0`.
2. Choose `c>0` so small that `B^(c log n)<=n^(1/4)`. Set `L=floor(c log n)`.
3. If `delta<exp(-sqrt(log n))`, use the empirical estimator (2) with `O(n/delta^2)` observations. This obeys (18), since `log^2(e/delta)>=log n`.
4. In the remaining regime, choose

\[
m=\left\lceil C_0{n\log^2(e/\delta)\over\delta^2\log n}\right\rceil,
\quad h={\delta\over128n},\quad\eta={\delta\over128}.
\]

For the grid in Section 2, use (9) when `t_j<=K_0L/(4m)`, with `r=K_0L/m`. Otherwise use (14), with `w=sqrt(Kt_jL/m)`. The latter range ensures `w<t_j/8`. The maximal grid value is less than `2/n`.
5. Lemmas 2–3 require a degree bounded by

\[
C_2\left[\log(e/\delta)
+{\sqrt{Ln/m}\over\delta}\log(e/\delta)\right]. \tag{19}
\]

In the low branch this follows from `r=K_0L/m`, `t<=2/n`, and (5); in the local branch use `w<=sqrt(2KL/(mn))` and (7). Choose fixed `C_0` sufficiently large to make the second term in (19) at most `L/2`. Since `delta>=exp(-sqrt(log n))`, the first term is `O(sqrt(log n))`, hence at most `L/2` for all sufficiently large `n`. Thus every prescribed polynomial has degree at most `L`.
6. The bias `b=C exp(-c_1 L)` is at most `delta/128` for sufficiently large `n`, uniformly in this regime. For each grid value the variance is at most `C(L/m)n^(1/4)`. By Chebyshev and a union bound over `J<=C/delta` grid values, the probability that any estimate differs from its expectation by more than `delta/16` is at most

\[
C\,{\log^2 n\over n^{3/4}\delta\log^2(e/\delta)}
\le C\,{\log^2 n\,e^{\sqrt{\log n}}\over n^{3/4}}, \tag{20}
\]

which tends to zero uniformly. Take `n` large enough that it is at most `1/16`.
7. On the resulting event, (4) gives error at most

\[
2nh+\eta+b+\delta/16
\le (2+1+1+8)\delta/128=3\delta/32<\delta/4.
\]

Set `d_hat=1-clip_0,1`.
8. To obtain a deterministic sample budget, draw two independent Poisson sample sizes of mean `m` before seeing the data, and abort with an arbitrary output if their sum exceeds `8m`. Its tail probability is at most `exp(-c'm)`, which is below `1/16` for the present range. Otherwise use that many observations from a fixed budget of `ceil(8m)`. This coupling preserves the analysis except on the abort event. Total error probability is at most `1/8`, hence certainly at most `1/4`.
9. The finitely many `n` below this universal threshold are handled by (2), absorbing the bounded factor `log(en)` into the universal constant. For `delta>1/2`, use the established estimator at `delta=1/2`; its error bound is stronger than required, and its sample count is bounded by a universal constant times (18). The use of `log(en)` handles `n=1`.

This completes the written argument.

#### Proof provenance, audit metadata, and limitations

The proof was developed during this task using the horizontal-sandwich/minimization construction, positive polynomial kernels, Poisson sample splitting, and factorial-moment estimation. It spells out the required arguments and does not invoke a finite-support theorem as a black box. Literature priority is not established.

Two independent in-session mathematical reviews checked the construction and found no substantive gap:

- `support_audit.md`: review by the pair-CLT research branch, covering the variational reduction, kernel approximation, low and local estimators, countable-support summability, and parameter selection. Its requested explicit absolute-expectation arguments are included in Sections 5–6.
- `root_review.md`: independent line-by-line review by the coordinating branch, including the kernel localization, horizontal sandwiches, factorial moments, both probability gates, the countable-support factors, constant hierarchy, union bound, small-gap fallback, and fixed sample budget.

These reviews are written mathematical evidence. No formal proof assistant, journal review, or external publication is claimed. No numerical implementation of this support estimator was executed. The universal constants and the threshold for using the polynomial branch are not optimized for practice; the theorem establishes sample-complexity existence. A stable practical implementation remains separate work.

The support-testing branch also independently audited Theorems M3 and M4 in the companion Markov appendix; its findings are in `support_work/audit_markov.md`. That review found no correction necessary, including the local Stirling argument when `k^2/n` does not vanish.

### 8. Secondary completed result: a sharp metric modulus

This argument is independent of the polynomial theorem and completes a specific source-paper sketch.

For a distribution `p`, let its mass-weighted histogram be the probability measure `nu_p=sum_i p_i delta_(p_i)` on `(0,1]`. For generalized histograms the same definition uses fractional multiplicities. Define `R_tau` as optimal transport between these probability measures with cost `|log(max(x,tau))-log(max(y,tau))|`, exactly the metric in Valiant's Definition 3.

For every `n>=1`, `tau>0`, and normalized generalized histograms `p,q`,

\[
|d_n(p)-d_n(q)|\le R_\tau(p,q)+n\tau. \tag{21}
\]

For generalized histograms define `C_n` by (1), equivalently by taking the highest-probability mass subject to fractional symbol-count budget `n`.

**Proof.** Let

\[
C_n^\tau(p)=\inf_{t\ge\tau}\left\{nt+\int(1-t/x)_+\,d\nu_p(x)\right\}.
\]

Restricting the infimum gives `0<=C_n^tau-C_n<=n tau`: choose `t=tau` if a minimizing cutoff is below `tau`, or more generally compare with an approximate minimizer and use that `F_p` decreases. For `t>=tau`, the function `(1-t/x)_+` is 1-Lipschitz in `log(max(x,tau))`: it vanishes below `t`, and its derivative in log-coordinate above `t` is `t/x<=1`. Coupling and integrating therefore gives `|C_n^tau(p)-C_n^tau(q)|<=R_tau`. The two truncation errors are both in `[0,n tau]`, so their **difference** is at most `n tau`, proving (21), without an unnecessary factor two.

#### Exact ambiguity example

For `n>=2`, `0<a<1/2`, and integer `M>n-1`, put

\[
p=(1-a,\underbrace{a/(n-1),\ldots,a/(n-1)}_{n-1}),
\quad q=(1-a,\underbrace{a/M,\ldots,a/M}_{M}).
\]

If `tau>=a/(n-1)`, both tails collapse to the same truncated mass atom; hence `R_tau(p,q)=0`. Nevertheless

\[
d_n(p)=0,\qquad d_n(q)=a\left(1-{n-1\over M}\right).
\]

Thus a metric-only black-box guarantee cannot resolve additive errors substantially smaller than `n tau`. This is a limitation of this metric reduction, not a statistical lower bound for Q852. The coefficient of the truncation term is also sharp in the full modulus: take `tau=1/M` with `M>=n`, let `p` be uniform on `M` points and `q` uniform on `L>M` points. Then `R_tau=0` and `|d_n(p)-d_n(q)|=n/M-n/L`, which approaches `n tau` as `L` increases.

#### Source-based corollary, with its regime retained

Using Valiant's Theorem 2 with `w=C/delta^2`, choosing `tau=w/(m log m)<=c delta/n`, and applying (21) gives `O(n/(delta^3 log n))` tolerant testing when the theorem's condition `w<=log m` holds, in particular for sufficiently large `n` and `delta>=C'/sqrt(log n)` with suitable constants. The empirical bound (2) remains available outside that regime. This corollary has weaker accuracy dependence than theorem (18); it is useful because every part of the earlier Appendix C sketch is now explicit.

### 9. Q851 and remaining research after Q852's proof

The proof above costs `delta^-2` and does not improve the non-tolerant `epsilon^-1` upper bound. It therefore does not close Q851's logarithmic factor. For fixed `epsilon` in `(0,1/2)`, the supplied upper and lower bounds already agree at order `n/log n`; the unresolved target is their joint accuracy dependence as `epsilon` shrinks. The Q851 ledger should remain unresolved.

With Q852 proved at the requested sample-complexity scope, remaining work includes making the universal constants numerically usable, stable polynomial implementation, computational complexity, confidence amplification, and sharp lower bounds for tolerant diagnosis. None of those additional questions is silently included in the rate theorem. This result is an iid countable-alphabet theorem; it does not justify Markov or natural-prose vocabulary claims.


---

## Appendix B. Complete pair-sampling CLT proof

## B8 / Q858: a complete independently reviewed written proof of the vertex-count CLT

**Date:** 7 October 2026. **Stable statement ID:** `0c3cb5efa6b7fd0651a8`.

**Exact retained question.** Let `(E_i)_{i>=1}` be iid unordered pairs of distinct natural numbers, with an arbitrary fixed probability law `mu` on the countable set of such pairs. Put `V_n = union_{i<=n} E_i`. Does `Var(|V_n|) -> infinity` imply `( |V_n| - E|V_n| ) / sqrt(Var(|V_n|)) => N(0,1)`, without eventual connectedness, loops, or dust?

**Answer: proved by a complete independently reviewed written argument.** The argument below proves the exact retained statement. No connectedness, maximum degree, regular variation, or rate-of-variance-divergence hypothesis is used. The central ingredient is a uniform zero-free region for the probability generating function of the number of covered vertices of an independent-edge random graph. A short Asano-contraction proof is included, so the result does not rest on an unchecked invocation of the Lee–Yang theorem.

**Evidence and review status:** a complete written argument, independently checked by the coordinating agent and a second research agent in this research pass; source comparison completed for the three target papers. The reviews are recorded in `pair_independent_audit.md` and `root_review.md`. No proof assistant has been used, and no compiled formal theorem, human peer review, publication, or established novelty is claimed. Finite computations, when recorded below, are supplementary checks only.

### 1. Source comparison

Janson, *On Edge Exchangeable Random Graphs*, Journal of Statistical Physics 173 (2018), 448–484, DOI `10.1007/s10955-017-1832-9`, Problem 6.9, journal p. 464 / PDF p. 17, asks the vertex-count CLT under divergent variance. The paper appeared online 30 June 2017.

Edward Eriksson, *Edge Exchangeable Graphs: Connectedness, Gaussianity and Completeness*, arXiv:2501.09511v2, revised 6 May 2026, Theorem 14 and Corollary 18, establishes a CLT under eventual forever connectedness. Proposition 16 treats isolated-edge support. Section 4 still identifies the general problem as open.

Edward Eriksson, *The Unseen Species Problem Revisited*, arXiv:2602.08769v4, revised 9 September 2026, footnote 3, expressly retains the general Gaussianity problem even for sets of size two.

Primary URLs:

- https://uu.diva-portal.org/smash/get/diva2:1273609/FULLTEXT01.pdf
- https://arxiv.org/html/2501.09511v2
- https://arxiv.org/html/2602.08769v4

The coordinating reviewer independently reopened these primary sources and checked their exact statements and versions. Source retrieval is distinct from a mathematical certificate.

The contraction argument below is the elementary unit-disc case of the Lee–Yang/Asano method. Relevant original/general sources include T. D. Lee and C. N. Yang, *Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model*, Physical Review 87 (1952), 410–419, DOI `10.1103/PhysRev.87.410`; David Ruelle, *Extension of the Lee–Yang Circle Theorem*, Physical Review Letters 26 (1971), 303–304, DOI `10.1103/PhysRevLett.26.303`. The read-two product inequality is the case k=2 of Finner’s generalized Hölder inequality; an accessible paper discussing it is Gavinsky, Lovett, Saks, Srinivasan, *A Tail Bound for Read-k Families of Functions*, Random Structures & Algorithms 47 (2015), DOI `10.1002/rsa.20532`, https://www.cs.toronto.edu/tss/files/papers/1205.1478.pdf . Both needed lemmas are proved here.

### 2. Notation

Write `mu_uv = P(E_1={u,v})` for u<v, extend symmetrically, and put

\[
p_v=\sum_{u\ne v}\mu_{uv},\qquad \sum_vp_v=2,\qquad 0\le p_v\le1.
\]

Let `N(t)` be a rate-one Poisson process, independent of the iid edges, and define

\[
F_n=|V_n|,\qquad \widetilde F(t)=F_{N(t)}.
\]

For each edge e, its arrivals by time t are independent Poisson variables of means `t mu_e`. Therefore its presence indicator is independent of all other edge-presence indicators.

Set

\[
q_v(t)=e^{-tp_v},\quad
B(t)=\sum_vq_v(t)(1-q_v(t)),\quad
D(t)=\sum_vp_ve^{-tp_v}.
\]

All sums are finite at fixed t: `B(t) <= sum_v(1-q_v(t)) <= 2t`. Moreover `0 <= F_n <= 2n` and `0 <= Ftilde(t) <= 2N(t)`.

### 3. Two elementary lemmas

#### Lemma 1: read-two product inequality

Let `(X_e)` be independent random variables. For a finite collection of nonnegative functions `(f_v)`, suppose each `X_e` appears in at most two functions. Then

\[
\mathbb E\prod_v f_v\le\prod_v(\mathbb E f_v^2)^{1/2}.
\]

**Proof.** Integrate one coordinate `X_e` at a time, conditionally on all remaining coordinates. If it appears in two current factors, apply Cauchy–Schwarz to those two factors; replace each factor f by `(E_e f^2)^{1/2}`. If it appears in one factor, apply the same inequality against the constant one. Each transformed factor remains the square root of the conditional expectation of the square of its original factor over the coordinates already integrated. Repeating yields the asserted right side. Countably many coordinates follow by conditional-expectation approximation and the usual L2 convergence, or by merging the external edge variables as in the finite-vertex construction below. QED.

#### Lemma 2: unit-disc contraction

Suppose a polynomial `P(x,y)=A+Bx+Cy+Dxy` does not vanish whenever `|x|<1` and `|y|<1`. Then `A+Dz` does not vanish for `|z|<1`.

**Proof.** First A is nonzero. For fixed `|x|<1`, absence of roots in the y-disc implies

\[
|A+Bx|\ge |C+Dx|.
\]

Integrating the squared inequality on `x=r exp(i theta)` gives

\[
|A|^2+r^2|B|^2\ge |C|^2+r^2|D|^2.
\]

Interchanging x and y similarly gives

\[
|A|^2+r^2|C|^2\ge |B|^2+r^2|D|^2.
\]

Add these and let r increase to 1: `|A|>=|D|`. Thus `|Dz|<|A|` for `|z|<1`, unless D=0, when the conclusion is immediate. The statement continues to hold with further variables: fix those variables within their unit discs and apply this argument. QED.

#### Lemma 3: a ferromagnetic graph polynomial is zero-free in the polydisc

For a finite graph H=(W,E) and edge numbers `0<=a_e<=1`, define

\[
Z_H((u_v)_{v\in W})
=\sum_{S\subseteq W}\prod_{v\in S}u_v
             \prod_{e\in\partial_H S}a_e.
\]

Here `partial_H S` denotes edges with exactly one endpoint in S. Then Z is nonzero if every `|u_v|<1`.

**Proof.** For each edge e={v,w}, introduce distinct endpoint variables `x_{v,e},x_{w,e}` and the factor

\[
1+a_ex_{v,e}+a_ex_{w,e}+x_{v,e}x_{w,e}.
\]

It has no zero in the bidisc: for `|x|<1`,

\[
|1+a_ex|^2-|a_e+x|^2=(1-a_e^2)(1-|x|^2)\ge0,
\]

and `1+a_ex` is nonzero. The possible root in the second variable therefore has modulus at least one. Take the product of all edge factors, and include `(1+u_v)` for vertices of degree zero. Repeatedly use Lemma 2 to contract all variables incident to a given vertex to one variable `u_v`. A contraction retains only the terms in which both contracted variables are present or both absent. At the end, a monomial corresponds to a vertex subset S, and its coefficient is exactly the product of `a_e` over crossing edges. Zero-freeness is preserved at each step. QED.

### 4. Uniform zero-free region for the coverage generating function

Fix t>0 and a finite vertex set W. Put `lambda_uv=t mu_uv` for edges inside W,

\[
b_v=t\sum_{u\notin W}\mu_{uv},\quad
d_v=\sum_{u\in W\setminus\{v\}}\lambda_{uv},\quad
a_v=b_v+d_v=tp_v.
\]

All edges from v to outside W can be aggregated into one independent Bernoulli variable indicating at least one such edge. These aggregate variables are independent for distinct vertices, because their underlying unordered edges are disjoint, and independent of internal edges. Thus the finite-vertex indicators are functions of a finite independent family, each input read by at most two vertices.

Let `A_v=1{v is absent at time t}`. Independence of edge arrivals gives, for every S subset W,

\[
\mathbb E\prod_{v\in S}A_v
=\exp\left(-\sum_{v\in S}a_v+
               \sum_{\{u,v\}\subseteq S}\lambda_{uv}\right).
\]

Consequently, with `z=e^s-1`,

\[
\mathbb E e^{s\sum_{v\in W}A_v}
=\sum_{S\subseteq W}z^{|S|}
 \exp\left(-\sum_{v\in S}a_v+
               \sum_{\{u,v\}\subseteq S}\lambda_{uv}\right).
\]

Use Lemma 3 with

\[
a_{uv}^{\mathrm{LY}}=e^{-\lambda_{uv}/2},\qquad
u_v=z\,e^{-b_v-d_v/2}.
\]

The coefficient for S in that graph polynomial equals the displayed coefficient: the exponent from selected vertices is `-sum_S b_v -sum_{internal S}lambda - (1/2)sum_{crossing}lambda`; the crossing-edge factors contribute the other half of the crossing exponent. It is therefore `-sum_S a_v+sum_{internal S}lambda`.

Every `|u_v|<=|z|`, so Lemma 3 proves nonvanishing whenever `|e^s-1|<1`.

For the covered count

\[
F_W=\sum_{v\in W}(1-A_v)
\]

its moment generating function is nonzero whenever `|e^{-s}-1|<1`; in particular, it is nonzero throughout

\[
|s|<\log2.
\]

Equivalently, the probability generating polynomial of F_W has no roots in the half-plane `Re z>1/2`.

### 5. Variance bounds and cumulants

For finite W put

\[
B_W=\sum_{v\in W}q_v(t)(1-q_v(t)).
\]

Let `X_v=1-A_v-E(1-A_v)`. Each X_v is centered, has absolute value at most one, and has second moment equal to its Bernoulli variance. The read-two inequality gives, for real u,

\[
\mathbb E e^{u(F_W-\mathbb EF_W)}
\le\prod_{v\in W}\big(\mathbb E e^{2uX_v}\big)^{1/2}.
\]

For any centered random variable X with `|X|<=1`, Taylor expansion gives

\[
\log\mathbb Ee^{rX}
\le\frac{r^2e^{|r|}}2\mathbb EX^2.
\]

Hence

\[
\log\mathbb E e^{u(F_W-\mathbb EF_W)}
\le u^2e^{2|u|}B_W.\tag{5.1}
\]

Differentiating the inequality at zero, where both sides vanish with zero first derivative, yields `Var(F_W)<=2B_W`. Also, for u!=v,

\[
\operatorname{Cov}(1-A_u,1-A_v)
=e^{-t(p_u+p_v)}(e^{t\mu_{uv}}-1)\ge0.
\]

Therefore

\[
B_W\le\operatorname{Var}(F_W)\le2B_W.\tag{5.2}
\]

Let `H_W(s)=log E exp(s(F_W-EF_W))` be the analytic logarithm on `|s|<log2`, chosen with H_W(0)=0. For complex s,

\[
\operatorname{Re}H_W(s)
=\log\left|\mathbb E e^{s(F_W-\mathbb EF_W)}\right|
\le(\operatorname{Re}s)^2e^{2|\operatorname{Re}s|}B_W.
\]

Thus `Re H_W(s)<= (e/4)B_W` for `|s|<1/2`.

For completeness, if an analytic H with H(0)=0 satisfies `Re H<=M` in `|s|<R`, then its Taylor coefficients `H(s)=sum_{k>=1}h_k s^k` satisfy

\[
|h_k|\le 2M R^{-k}.\tag{5.3}
\]

To see this, integrate `Re H(r e^{i theta}) e^{-ik theta}` around the circle. This integral is `pi h_k r^k`; replacing `Re H` by `Re H-M` does not change it when k>=1. The nonnegative function `M-Re H` has average M by the mean-value property, so the absolute value is at most `2pi M`. Let r increase to R.

Applying (5.3) with R=1/2 and M=e B_W/4 gives the explicit uniform bound

\[
\boxed{\quad |\kappa_k(F_W)|\le k!\,e\,2^{k-1}B_W\quad(k\ge2).\quad}\tag{5.4}
\]

The first cumulant of the centered variable is zero; for k>=2 centering does not change cumulants.

#### Countable extension

Take W increasing to all natural numbers. Then F_W increases to Ftilde(t), and `F_W<=2N(t)`. The latter has all exponential moments. Consequently the moment generating functions and all their derivatives converge locally uniformly on every bounded complex disc, by domination by `exp(2rN(t))` (and the same domination with powers of N for derivatives). Their centered versions converge locally uniformly as well.

Every finite centered moment generating function is nonzero on `|s|<log2`. Hurwitz’s theorem, and value one at s=0, imply that the limit is also nonzero there. Alternatively, the coefficient estimates can be passed to the limit directly using derivative convergence. The variance bounds and cumulant estimates pass to the limit:

\[
B(t)\le\sigma_P^2(t):=\operatorname{Var}(\widetilde F(t))\le2B(t),\tag{5.5}
\]

\[
|\kappa_k(\widetilde F(t))|\le k!\,e\,2^{k-1}B(t),\qquad k\ge2.\tag{5.6}
\]

The corresponding analytic logarithm has the same Taylor-coefficient bound.

#### Poissonized CLT

Assume B(t)->infinity. For every fixed real x and t sufficiently large, `|x|/sigma_P(t)<1/2`. The log characteristic function of the standardized variable is

\[
H_t(ix/\sigma_P(t))=-x^2/2+R_t(x).
\]

By (5.6),

\[
|R_t(x)|\le\frac{4eB(t)|x|^3}{\sigma_P^3(t)}
              \frac1{1-2|x|/\sigma_P(t)}\longrightarrow0.
\]

Here B(t)<=sigma_P^2(t). Lévy’s continuity theorem proves

\[
\frac{\widetilde F(t)-\mathbb E\widetilde F(t)}{\sigma_P(t)}
\Rightarrow N(0,1).\tag{5.7}
\]

The proof also works for arbitrary triangular arrays of independent-edge models whenever their vertex-count variances diverge. The fixed law is needed later for de-Poissonization.

### 6. General fixed-law variance comparison

This section is independent of the analytic argument and handles every fixed pair law mu.

Put `f_n(x)=(1-x)_+^n`, and suppress t=n in B(n). Define

\[
d_n=\sum_vp_v(1-p_v)^{n-1}.
\]

#### Lemma 4: diagonal and mean errors vanish

For the fixed law,

\[
\sum_v|f_n(p_v)-e^{-np_v}|\to0.\tag{6.1}
\]

Indeed for p<=1/2,

\[
0\le e^{-np}-(1-p)^n
\le np^2e^{-np}\le p/e.
\]

For p>1/2 the difference is at most 1<=2p. Each fixed-p summand tends to zero, and `sum p_v=2`, so dominated convergence applies. The function x(1-x) is 1-Lipschitz on [0,1], so (6.1) also bounds the total discrepancy of diagonal variance terms. In particular,

\[
\mathbb E\widetilde F(n)-\mathbb EF_n\to0.\tag{6.2}
\]

#### Lemma 5: positive edge-interaction errors vanish

For p=p_u, q=p_v, w=mu_uv, define

\[
P_n(u,v)=f_n(p+q-w)-f_n(p+q),
\]

\[
P_P(u,v)=e^{-n(p+q-w)}-e^{-n(p+q)}.
\]

Then

\[
\sum_{u\ne v}|P_n(u,v)-P_P(u,v)|\to0.\tag{6.3}
\]

For n>=2, the difference is the integral over `[p+q-w,p+q]` of

\[
n\big((1-x)_+^{n-1}-e^{-nx}\big).
\]

This integrand is bounded by a universal absolute constant for all n>=2 and x>=0. To check the only delicate range, 0<=x<=1/2, write `-log(1-x)=x+r` with `0<=r<=x^2`. Then

\[
n|(1-x)^{n-1}-e^{-nx}|
\le e^{1/2}\big(nx+(nx)^2\big)e^{-nx},
\]

which is uniformly bounded. For x>=1/2 both terms are directly bounded after multiplication by n. For each fixed x>0 the integrand tends to zero.

If w>0, the lower integration endpoint is at least max(p,q)>0. Therefore each edge’s integral tends to zero and has absolute value at most Cw. Summing uses `sum_{u!=v}mu_uv=2` and dominated convergence. Edges of weight zero contribute zero.

#### Lemma 6: the multinomial correction is negligible on the variance scale

Define

\[
Q_n=\sum_{u\ne v}\big(f_n(p_u)f_n(p_v)-f_n(p_u+p_v)\big).
\]

Then

\[
0\le Q_n\le n d_n^2=o(B(n)).\tag{6.4}
\]

For a=(1-p)(1-q) and b=(1-p-q)_+, we have `0<=b<=a<=1` and `a-b<=pq`. Thus

\[
a^n-b^n\le npq(1-p)^{n-1}(1-q)^{n-1},
\]

giving the first two inequalities after summing. Cauchy–Schwarz gives

\[
\frac{nd_n^2}{B(n)}
\le\sum_v\frac{np_v^2(1-p_v)^{2n-2}}
 {e^{-np_v}(1-e^{-np_v})}.
\]

For 0<p<=1 and n>=2 each summand is bounded by

\[
p e^{2p}\frac{np}{e^{np}-1}\le e^2p,
\]

where the case p=1 has zero numerator and is immediate. Each fixed positive-p summand tends to zero. Dominated convergence with `sum p_v=2` proves (6.4).

#### Variance conclusion

The fixed-n covariance for u!=v is

\[
f_n(p_u+p_v-\mu_{uv})-f_n(p_u)f_n(p_v)
=P_n(u,v)-\big(f_n(p_u)f_n(p_v)-f_n(p_u+p_v)\big).
\]

The Poissonized covariance is P_P(u,v). All sums are absolutely convergent: the positive interaction sums are at most `2n`, and the negative correction is at most `nd_n^2<=4n`. Finite truncation therefore justifies summing covariances. Lemmas 4–6 imply

\[
\boxed{\quad \operatorname{Var}(F_n)
=\operatorname{Var}(\widetilde F(n))-Q_n+o(1),
\quad Q_n=o(B(n)),\quad Q_n\ge0.\quad}\tag{6.5}
\]

Together with (5.5), this gives

\[
\operatorname{Var}(F_n)\to\infty
\quad\Longleftrightarrow\quad B(n)\to\infty,
\]

and in this regime

\[
\frac{\operatorname{Var}(F_n)}{\operatorname{Var}(\widetilde F(n))}\to1.\tag{6.6}
\]

### 7. General fixed-law de-Poissonization

Cauchy–Schwarz, now directly for D(n), gives

\[
\frac{nD(n)^2}{B(n)}
\le\sum_vp_v\frac{np_v}{e^{np_v}-1}\longrightarrow0.\tag{7.1}
\]

Again the summands are bounded by p_v and converge individually to zero.

Assume `Var(F_n)->infinity`; hence B(n)->infinity by (6.5). Choose positive c_n increasing to infinity sufficiently slowly that

\[
c_n\frac{\sqrt nD(n)}{\sqrt{B(n)}}\to0,
\qquad \frac{c_n\log n}{\sqrt n}\to0.
\]

Such a choice exists by (7.1). Put `h_n=ceil(c_n sqrt n)`, so h_n=o(n). A split at `p_v=4 log(n)/n` gives

\[
D(n-h_n)\le(1+o(1))D(n)+O(n^{-3}).\tag{7.2}
\]

For the small p_v terms use `exp(h_n p_v)<=exp(4h_n log n/n)=1+o(1)`. For the remaining terms, eventually `h_n<=n/4`, so `exp(-(n-h_n)p_v)<=n^{-3}`, and their p_v weights sum to at most two.

On the coupling using the same iid edges and independent `N(n)`,

\[
\Pr(|N(n)-n|>h_n)\le n/h_n^2\to0.
\]

On the complementary event, monotonicity gives

\[
|F_{N(n)}-F_n|\le F_{n+h_n}-F_{n-h_n}.
\]

Its expected upper bound is

\[
\sum_v(1-p_v)^{n-h_n}\big(1-(1-p_v)^{2h_n}\big)
\le 2h_nD(n-h_n)=o(\sqrt{B(n)}).
\]

Markov’s inequality therefore proves

\[
\frac{F_{N(n)}-F_n}{\sqrt{B(n)}}\longrightarrow0
\quad\text{in probability}.\tag{7.3}
\]

Equations (6.2), (6.6), (7.3), and the Poissonized CLT (5.7) now give the exact fixed-n conclusion by Slutsky’s theorem:

\[
\boxed{\qquad
\frac{|V_n|-\mathbb E|V_n|}{\sqrt{\operatorname{Var}(|V_n|)}}
\Rightarrow N(0,1)
\quad\text{whenever}\quad\operatorname{Var}(|V_n|)\to\infty.
\qquad}
\]

### 8. Scope and residual work

The mathematical target Q858 is covered by this complete written proof, whose lemmas and analytic passage passed both independent reviews recorded in `pair_independent_audit.md` and `root_review.md`. It proves the precise fixed-law, countable, loopless, no-dust statement. It does not assert a universally estimable variance from one observed graph, a finite-sample confidence interval with estimated variance, a fixed-n universal Berry–Esseen rate, or a theorem for arbitrary unbounded hyperedge sizes.

The zero-free/cumulant argument itself is uniform over independent-edge models; its interaction structure uses size two. For sets of size three or more, the absent-indicator polynomial has higher-order interactions, and this Lee–Yang proof does not automatically apply. Thus the broader bounded-incidence question remains a separate target.

Novelty is not established by the present literature comparison. The three source papers still retain the exact question as open, but that does not prove that this route is absent from all literature. The report presents an independently reconstructible argument, not an external publication claim.

### 9. Executed finite checks and verification archive

`pair_work/verify_pair_clt.py` ran successfully with Python 3.12.14 and NumPy 2.3.5. Its random seed was **85820261007**. The bounded input budget was 829 independent-input models plus 625 fixed-sample checks:

- All 729 assignments of edge-presence probabilities from `{1/10,1/2,9/10}` to the six edges of the complete graph on four vertices.
- One hundred seeded models on six vertices, including independent private singleton inputs to test the finite-truncation boundary construction. Probabilities were multiples of 1/10 from zero through 9/10.
- Twenty-five seeded fixed laws on the six pairs of four vertices, obtained from positive integer weights in `{1,...,20}`, each checked at n=1,...,25.

Exact rational enumeration verified the absent-moment/covered-count polynomial identity and `B<=Var<=2B` in every independent-input model. Exact rational dynamic programming verified the full fixed-n covariance decomposition and `0<=Q_n<=n d_n^2` in all 625 fixed-sample cases. Floating-point polynomial-root computations found no zero in `Re z>1/2`; the largest computed root real part was **0.21356063092942126**. The tested variance/B ratios ranged from **1.0088860715578432** to **1.896678966789668**.

These finite checks support the formulas and implementation of the proof’s intermediate objects. They establish neither the asymptotic theorem nor a formal verification. The written proof supplies the unrestricted quantifiers.

Complete archive:

- `pair_work/verify_pair_clt.py`: executable script and input-generation specification.
- `pair_work/finite_check_inputs_outputs.json`: every generated model, every exact rational PGF coefficient, exact means/variances/B, computed roots, and every exact fixed-n decomposition output.
- `pair_work/finite_check_summary.json`: machine-readable execution summary.
- `pair_work/finite_check_stdout.txt`: actual captured standard output.

### 10. Statement-ledger entry for reconciliation

- Programme: **B8**.
- Q number: **Q858**.
- Stable statement ID: **`0c3cb5efa6b7fd0651a8`**.
- Retained statement: the exact fixed-law iid-pair divergent-variance CLT quoted at the top of this report.
- Changed assumptions: **none**.
- Result classification: **proved** by the written argument in Sections 2–7, as checked independently within this research pass.
- Primary-source comparison: **completed**, showing the exact problem still stated as open in the May/September 2026 sources reviewed.
- Finite-computation evidence: **passed**, with the bounded domains and archive in Section 9.
- Compiled-formal-theorem evidence: **not attempted**.
- Residual uncertainty: no human peer review or proof-assistant certification; novelty beyond the checked source set is unestablished. Applications requiring variance estimation or fixed-sample error rates need additional results.


---

## Appendix C. Rare mass, Markov variance, and next-token arguments

## B8: stationary rare mass and next-token exposure

Date: 7 October 2026. This appendix develops written arguments for Q853–855 and Q859. No formal proof assistant was run. Finite checks and simulations are separately identified.

### 1. Exact retained statements and source comparison

**Q853 — `07232484a765905b847d`.** Is minimax MSE for the realized stationary missing mass \(M_0\) \(O(T/n)\) when \(n\gtrsim T\log n\), removing the known \(\log(n/T)\) factor? **Status: unresolved.** The arguments below do not construct an estimator attaining this rate for arbitrary finite ergodic chains.

**Q854 — `ad6c67395090a5839dec`.** Does \(\operatorname{Var}(M_0)\le C\min\{T\log(1+n/T)/n,1\}\) hold universally? **Status: partial.** Section 4 proves the stronger \(O(T/n)\) bound for every refresh chain \(P=(1-a)I+a\mathbf1\pi^\top\), with an exact variance formula and a matching order example. This is an added restriction on the kernel, not a proof for all chains.

**Q855 — `eeea824c340739a51a8d`.** For \(1\le\zeta=o(n)\), determine the minimax MSE of \(M_\zeta=\sum_x\pi_x\mathbf1\{N_x\le\zeta\}\) jointly in \(n,\zeta,T\), including whether the stated linear-in-\(\zeta+1\) upper bounds are sharp. **Status: partial, with a disproved sharpness subclaim.** Sections 2–3 give stronger upper bounds. In particular, the iid bound \(O((\zeta+1)/n)\) cannot be minimax-sharp uniformly for growing \(\zeta=o(n)\). A matching lower bound for the new envelope is not proved.

**Q859 — `11f05c2567c0a33574c8`.** For an unconditional next-token rare-exposure probability \(S_\zeta=\Pr\{N_{X_{n+1}}(X_{1:n})\le\zeta\}\), determine optimal rarity dependence for stationary finite ergodic Markov chains, including whether the quadratic rarity factor can be replaced by a linear one. **Status: partial.** Section 5 gives the exact iid order for \(\zeta\to\infty\), \(\zeta=o(n)\), and preserves the finite-sample terms in the Markov bound. The general Markov improvement remains unresolved.

The primary comparison is Pananjady, Muthukumar, Thangaraj, *Just Wing It*, JMLR 25 (2024), Theorem 1 / Eqs. (18a–b), Theorem 2 / Eq. (20), and Theorem 3 / Eqs. (25–27), printed pp. 10–14. The later *Estimating stationary mass, frequency by frequency*, arXiv:2503.12808, studies a different vector-estimation loss. Nakul, Muthukumar, Pananjady, *Next-token functional estimation*, arXiv:2609.19529v1, 17 September 2026, Corollary 2 and §4.2, retains the rarity question. The next-token paper uses a one-sided deleted window; the stationary WingIt estimator uses a two-sided window. These objects are kept separate here.

Primary URLs:

- https://jmlr.org/papers/volume25/24-0511/24-0511.pdf
- https://arxiv.org/abs/2503.12808
- https://arxiv.org/html/2609.19529v1

### 2. A stronger iid cumulative Good–Turing bound

#### Theorem M1

Let \(n\ge1\), let \(p\) be any probability law on a finite or countably infinite alphabet, and let \(X_1,\ldots,X_n\) be iid with law \(p\). For an integer \(0\le k\le n/2\), define

\[
 M_{\le k}=\sum_x p_x\mathbf1\{N_x\le k\},\qquad
 G_k=\frac1n\sum_xN_x\mathbf1\{N_x\le k+1\}
     =\frac1n\sum_{r=1}^{k+1}r\Phi_r.
\]

Then

\[
\boxed{\quad
 \sup_p\mathbb E_p(G_k-M_{\le k})^2
 \le\min\left\{1,\frac{22\sqrt{k+1}}{n}\right\}.
\quad}\tag{M1}
\]

The estimator uses only the observed multiplicities and is already in \([0,1]\). No bound on the true support, minimum atom mass, Poissonization, or changing observation contract is assumed.

#### Proof

For \(n\ge8\), put \(m=n-2\). Write \(b_{m,p}(r)=\Pr\{\operatorname{Bin}(m,p)=r\}\) and \(F_{m,p}(r)=\Pr\{\operatorname{Bin}(m,p)\le r\}\), taking negative-threshold probabilities to be zero. Define

\[
 B_r=\sup_{0\le p\le1}p\,b_{m,p}(r),\qquad
 C_r=\sup_{0\le p\le1}p^2b_{m,p}(r),
\]

with \(B_{-1}=C_{-1}=0\).

We first calculate the risk exactly for a finite alphabet. The diagonal term for an atom of mass \(p\) is

\[
\begin{aligned}
&\mathbb E\left[\frac{N}{n}\mathbf1\{N\le k+1\}-p\mathbf1\{N\le k\}\right]^2\\
&=\frac pnF_{n-1,p}(k)-\frac{p^2}{n}F_{m,p}(k-1)
 +p^2(1-p)^2b_{m,p}(k)
 +p^3(2-p)b_{m,p}(k-1).
\end{aligned}\tag{M2}
\]

This follows from the binomial shift identities
\(\mathbb E[Nf(N)]=np\,\mathbb E f(1+\operatorname{Bin}(n-1,p))\) and
\(\mathbb E[N(N-1)f(N)]=n(n-1)p^2\,\mathbb E f(2+\operatorname{Bin}(n-2,p))\), followed by two applications of the binomial recursion.

For distinct atoms with masses \(p,q\), let \(F_j(k,k)\) be the joint lower-tail probability for their two counts in \(j\) multinomial trials. The off-diagonal term in the squared error is

\[
 pq\left[(1-1/n)F_m(k,k)-2F_{m+1}(k,k)+F_{m+2}(k,k)\right].\tag{M3}
\]

In the \(m\)-trial experiment set
\(a_r=\Pr(N_p=r,N_q\le k)\),
\(c_r=\Pr(N_q=r,N_p\le k)\), and
\(j_{kk}=\Pr(N_p=k,N_q=k)\). The bracket in (M3) is exactly

\[
 -\frac1nF_m(k,k)+p^2(a_k-a_{k-1})
 +q^2(c_k-c_{k-1})+2pqj_{kk}.\tag{M4}
\]

Indeed, adding one trial applies the operator
\(I+p(S_1-I)+q(S_2-I)\) to the joint CDF, where \(S_i\) lowers threshold \(i\) by one. Squaring this operator gives the displayed second difference. This calculation retains the cancellations between adjacent frequency classes.

Drop only the negative terms in (M2) and (M4). Summing the diagonal terms is at most \(1/n+B_k+2C_{k-1}\). The two asymmetric terms in (M4), summed over ordered distinct atoms, are at most \(2C_k\). Finally,

\[
2\sum_{x\ne y}p_x^2p_y^2\Pr_m(N_x=k,N_y=k)
\le2\sum_xp_x^2b_{m,p_x}(k)\sum_{y\ne x}p_y^2
\le2B_k.
\]

Consequently,

\[
\mathbb E(G_k-M_{\le k})^2
\le\frac1n+3B_k+2C_{k-1}+2C_k
\le\frac1n+5B_k+2B_{k-1}.\tag{M5}
\]

For \(0\le r\le n/2\), the binomial identity

\[
p\,b_{n-2,p}(r)=\frac{r+1}{n-1}b_{n-1,p}(r+1)
\]

shows that the supremum is attained at \(p=(r+1)/(n-1)\). Put \(a=r+1\), \(b=n-2-r\), and \(N=n-1=a+b\). The elementary Stirling factorial bounds give

\[
\binom{N}{a}(a/N)^a(b/N)^b
\le\sqrt{\frac{N}{ab}}.
\]

Here \(b/N\ge2/7\) for \(n\ge8\), \(r\le n/2\). Thus

\[
B_r\le\frac{\sqrt{7/2}\sqrt{r+1}}{n-1}
\le\frac{3\sqrt{r+1}}n.
\]

Substituting in (M5) yields \((1+15+6)\sqrt{k+1}/n\), proving the asserted constant 22. For \(n\le7\), both target and estimator lie in \([0,1]\) and \(22\sqrt{k+1}/n\ge1\), so the assertion is immediate.

For a countable alphabet, merge the tail beyond a finite initial set into one atom. Its mass tends to zero; the probability that one of the \(n\) observations comes from that tail also tends to zero. The finite-alphabet risks therefore converge to the original risk by bounded convergence. This proves the countable case. ∎

#### A Poissonized consistency check, not the fixed-sample proof

If the independent counts have laws \(N_x\sim\operatorname{Pois}(\lambda_x)\), \(\lambda_x=np_x\), the per-atom scaled error
\(N_x\mathbf1\{N_x\le k+1\}-\lambda_x\mathbf1\{N_x\le k\}\) has expectation zero and second moment

\[
\lambda_x\Pr\{\operatorname{Pois}(\lambda_x)\le k\}
 +\lambda_x^2\Pr\{\operatorname{Pois}(\lambda_x)=k\}.
\]

This directly suggests the square-root threshold dependence. Theorem M1 was proved in the fixed-\(n\) experiment; it does not rely on transferring this Poissonized risk without justification.

#### Consequence for the Q855 sharpness question

For every integer sequence \(k_n\to\infty\), \(k_n=o(n)\), Theorem M1 gives

\[
\frac{R^{\mathrm{iid}}_{n,k_n}}{(k_n+1)/n}
\le\frac{22}{\sqrt{k_n+1}}\longrightarrow0.
\]

Therefore a universal lower bound of order \((k+1)/n\) in this growing-threshold regime is false. This conclusion is an analytic implication of a proved upper bound, not an empirical assessment of sharpness. It does not determine the true minimax rate.

### 3. Complementary plug-in bounds and a new upper envelope

#### Theorem M2

For any sequence of observations on a countable alphabet, let \(\widehat p_x=N_x/n\), and for an integer \(0\le k<n\) define

\[
P_k=\sum_x\widehat p_x\mathbf1\{N_x\le k\}
    =1-\sum_{x:N_x>k}\widehat p_x.
\]

For every probability vector \(p\), pointwise in the observations,

\[
\boxed{\quad
 (P_k-\sum_xp_x\mathbf1\{N_x\le k\})^2
 \le\frac{n}{k+1}\sum_x(\widehat p_x-p_x)^2.
\quad}\tag{M6}
\]

**Proof.** At most \(n/(k+1)\) symbols have count greater than \(k\). Express the difference as the sum of \(p_x-\widehat p_x\) over those symbols, and apply Cauchy–Schwarz. ∎

For iid data, \(\mathbb E\|\widehat p-p\|_2^2=(1-\|p\|_2^2)/n\), so

\[
\sup_p\mathbb E(P_k-M_{\le k})^2\le\min\{1,1/(k+1)\}.\tag{M7}
\]

For a stationary finite ergodic Markov chain write
\(d(t)=\sup_x\|P^t(x,\cdot)-\pi\|_{\rm TV}\), and assume \(T=t_{\rm mix}(1/4)\ge1\). Stationarity gives

\[
\mathbb E\|\widehat p-\pi\|_2^2
=\frac{1-\|\pi\|_2^2}{n}
+\frac2{n^2}\sum_{t=1}^{n-1}(n-t)
 \left(\sum_x\pi_xP^t(x,x)-\|\pi\|_2^2\right).
\]

The quantity in parentheses is at most \(d(t)\). The total-variation contraction coefficient
\(\bar d(t)=\sup_{x,y}\|P^t(x,\cdot)-P^t(y,\cdot)\|_{\rm TV}\)
satisfies \(\bar d(s+t)\le\bar d(s)\bar d(t)\), \(\bar d(T)\le1/2\), and
\(d(jT)\le d(T)\bar d(T)^{j-1}\le2^{-j-1}\) for \(j\ge1\). Hence
\(\sum_{t\ge1}d(t)\le(T-1)+T/2\), and in particular

\[
\mathbb E\|\widehat p-\pi\|_2^2\le4T/n.
\]

Equation (M6) proves

\[
\boxed{\quad
\sup_{P:t_{\rm mix}\le T}\mathbb E(P_k-M_{\le k})^2
\le\min\{1,4T/(k+1)\}.
\quad}\tag{M8}
\]

For \(k\ge n\), the target equals one and can be estimated exactly. Combining (M1), (M7), and the source WingIt theorem yields the following upper envelopes (constants universal):

\[
R^{\mathrm{iid}}_{n,k}
\le\min\left\{1,\frac{22\sqrt{k+1}}n,\frac1{k+1}\right\},
\qquad 0\le k\le n/2,\tag{M9}
\]

\[
R^{\mathrm{Markov}}_{n,k,T}
\le C\min\left\{1,
\frac{(k+1)T\log(1+n/T)}n,
\frac{T}{k+1}\right\}.
\tag{M10}
\]

The choice between these estimators depends only on the declared parameters and bounds, not on unavailable stationary probabilities. For example, \(k=\lfloor n^{3/4}\rfloor\), \(T=1\), already refutes a uniform linear-\(k\) sharpness interpretation. None of these inequalities identifies a matching lower bound for the entire envelope.

### 4. Linear mixing-time variance for all refresh chains

#### Theorem M3

Let \(\pi\) be any probability vector on a finite alphabet of at least two states with positive masses, let \(0<a\le1\), and let a stationary Markov chain have transition matrix

\[
P=(1-a)I+a\mathbf1\pi^\top.
\]

For every \(n\ge1\),

\[
\boxed{\quad
\operatorname{Var}(M_0)
\le\min\left\{\frac14,\frac1{an}\right\}
\le\min\left\{\frac14,\frac{2T}{n}\right\},
\quad T=t_{\rm mix}(1/4).
\quad}\tag{M11}
\]

**Proof.** Construct the chain by drawing \(X_1\sim\pi\), and at each subsequent step independently refreshing with probability \(a\); a refresh draws a fresh label from \(\pi\), including the possibility of the same label. For any atom of mass \(p\), and any two distinct atoms of masses \(p,q\),

\[
\Pr(N_p=0)=(1-p)(1-ap)^{n-1},
\]
\[
\Pr(N_p=N_q=0)=(1-p-q)(1-a(p+q))^{n-1}.
\]

Both factors in the pair expression are no larger than the corresponding products of the singleton factors. The missing indicators are therefore pairwise negatively correlated. It follows that

\[
\operatorname{Var}(M_0)
\le\sum_x\pi_x^2(1-\pi_x)(1-a\pi_x)^{n-1}
\le\sup_{0\le p\le1}p(1-ap)^{n-1}\le\frac1{an}.
\]

The last inequality follows by putting \(u=ap\) and maximizing \(u(1-u)^{n-1}\) on \([0,1]\). The bound \(1/4\) holds because \(M_0\in[0,1]\).

Moreover,
\(P^t=(1-a)^tI+(1-(1-a)^t)\mathbf1\pi^\top\), so
\(d(t)=(1-a)^t(1-\pi_{\min})\). Since \(\pi_{\min}\le1/2\), the definition of \(T\) implies \((1-a)^T\le1/2\). Bernoulli's inequality gives \(1-aT\le(1-a)^T\), whence \(aT\ge1/2\), proving the second bound. ∎

#### Exact uniform-family variance and order sharpness within this subclass

For \(K\) equiprobable states, let

\[
q=(1-1/K)(1-a/K)^{n-1},\qquad
q_2=(1-2/K)(1-2a/K)^{n-1}.
\]

Then

\[
\mathbb EM_0=q,\qquad
\operatorname{Var}(M_0)=\frac{q(1-q)}K+
\left(1-\frac1K\right)(q_2-q^2).\tag{M12}
\]

Take any sequence \(a_n\downarrow0\) with \(na_n\to\infty\), and \(K_n=\lfloor na_n\rfloor\). Taylor expansion in \(1/K_n\) gives

\[
na_n\operatorname{Var}(M_0)\longrightarrow e^{-1}(1-e^{-1})>0,
\qquad a_nT_n\longrightarrow\log4.
\]

To check the negligible pair contribution directly, subtract logarithms:
\(\log q_2-2\log q=O(K_n^{-2}+na_n^2/K_n^2)\).
Multiplying this error by \(na_n\asymp K_n\) gives \(O(1/K_n+a_n)\to0\).
Thus the variance is of order \(T_n/n\), which makes linear mixing-time dependence necessary for variance even within this restricted family. The missing indicators need not be negatively correlated for a general Markov kernel, so that feature cannot be transferred without proof.

#### Consequence for next-token versus stationary missing mass

In this same refresh model, the next observation can be new only following a refresh. Conditionally on the trajectory,

\[
\Pr(X_{n+1}\text{ unseen}\mid X_{1:n})=aM_0,
\qquad S_0=a\mathbb EM_0.\tag{M13}
\]

Therefore an accurate estimator of stationary missing mass and an accurate estimator of next-token surprise need not estimate numerically similar quantities.

### 5. The iid next-token problem has a different rarity cost

For iid observations, \(S_k(p)=\mathbb E_p M_{\le k}\) is deterministic. The random target in Q855 is not interchangeable with this deterministic target.

#### Theorem M4: iid next-token rate in the growing-threshold regime

For any integer sequence \(k_n\to\infty\), \(k_n=o(n)\), there are universal constants \(0<c<C<\infty\) such that, eventually along that sequence,

\[
\boxed{\quad
c\frac{k_n}{n}\le
\inf_{\widehat S}\sup_p
\mathbb E_p(\widehat S-S_{k_n}(p))^2
\le C\frac{k_n+1}{n}.
\quad}\tag{M14}
\]

Here observations are exactly \(n\) iid draws; the alphabet is unrestricted and countable. This proves a subcase of Q859 with \(T=1\), and not its joint Markov dependence.

##### Upper bound

For distinct multinomial counts, the events \(\{N_x\le k\}\) and \(\{N_y\le k\}\) have nonpositive covariance. One elementary proof conditions on \(N_x=i\): the probability \(\Pr(N_y\le k\mid N_x=i)\) increases with \(i\), whereas \(\mathbf1\{i\le k\}\) decreases with \(i\). The covariance identity for two oppositely monotone functions gives the assertion.

Consequently,

\[
\operatorname{Var}(M_{\le k})\le\sum_xp_x^2\Pr\{\operatorname{Bin}(n,p_x)\le k\}
\le\frac{k+1}{n+1}.
\]

The last step uses the exact identity

\[
p\Pr\{\operatorname{Bin}(n,p)\le k\}
=\sum_{j=0}^k\frac{j+1}{n+1}\Pr\{\operatorname{Bin}(n+1,p)=j+1\}
\le\frac{k+1}{n+1}.
\]

Theorem M1 and \((u+v)^2\le2u^2+2v^2\) give

\[
\mathbb E(G_k-S_k)^2
\le\frac{44\sqrt{k+1}}n+\frac{2(k+1)}{n+1}
\le\frac{46(k+1)}n.
\tag{M15}
\]

##### Lower bound

Fix a sequence as in the theorem, write \(k=k_n\), set
\(m=\lfloor n/(2k)\rfloor\), and let \(r_0=km/n\). Then \(r_0\to1/2\). Consider the finite-alphabet family

\[
p_r(0)=1-r,\qquad p_r(j)=r/m\quad(1\le j\le m).
\]

For this family,

\[
S_k(r)=rF_{n,r/m}(k)+(1-r)F_{n,1-r}(k).
\]

Differentiating the binomial CDF yields

\[
S_k'(r)=F_{n,r/m}(k)-\frac{nr}{m}b_{n-1,r/m}(k)
 -F_{n,1-r}(k)+n(1-r)b_{n-1,1-r}(k).\tag{M16}
\]

For \(|r-r_0|\le h/\sqrt n\), with a fixed positive \(h\), the binomial mean \(nr/m\) differs from \(k\) by \(O(k/\sqrt n)=o(\sqrt k)\). Stirling's formula applied to the binomial point probability, uniformly on this interval, gives

\[
b_{n-1,r/m}(k)\sim\frac1{\sqrt{2\pi k}}.
\]

The two heavy-atom terms in (M16) tend to zero exponentially fast because \(1-r\) stays bounded away from zero and \(k=o(n)\). The CDF term is at most one. Hence, uniformly on the interval,

\[
S_k'(r)=-\frac{\sqrt k}{\sqrt{2\pi}}(1+o(1)).\tag{M17}
\]

For completeness, the stated local Stirling approximation follows by writing the log binomial mass as
\(-\tfrac12\log(2\pi k(1-k/(n-1)))-(n-1)D(k/(n-1)\Vert r/m)+o(1)\).
Here \((n-1)D=O(k/n)=o(1)\); the factorial remainder is \(O(1/k+1/(n-k))\), uniformly. This checks the approximation even when \(k^2/n\) does not vanish.

Choose \(h=1/16\) and \(r_\pm=r_0\pm h/\sqrt n\). The corresponding target separation is at least a universal positive constant times \(\sqrt{k/n}\). Meanwhile the one-observation Kullback–Leibler divergence is exactly the Bernoulli divergence \(D(\operatorname{Ber}(r_+)\Vert\operatorname{Ber}(r_-))\), since conditional on being in the rare group the labels are uniform and independent of \(r\). For all sufficiently large \(n\), \(r_\pm\in[1/4,3/4]\), and

\[
nD(p_{r_+}\Vert p_{r_-})
\le n\frac{(r_+-r_-)^2}{r_-(1-r_-)}\le64h^2=1/4.
\]

Pinsker's inequality bounds the total variation of the two \(n\)-sample laws by \(1/\sqrt8<1\). Classifying by which target value is closer to an estimator shows that its larger squared risk is at least the squared target separation times \((1-\mathrm{TV})/8\). This proves the lower bound. ∎

This explains why an improved bound for the sample-specific rare mass does not automatically improve the unconditional next-token bound to the same order. In the hard family above, the population probability changes by order \(\sqrt{k/n}\) under statistically hard parameter perturbations. The sample-specific target can track part of the observed fluctuation.

#### Markov finite-sample bound with all bias terms retained

Corollary 2 of *Next-token functional estimation* states

\[
\operatorname{MSE}(\widehat S_k(\tau),S_k)
\le64\left(\beta(\tau)+\frac\tau n\right)^2
+4\left(\frac{(k+1)\tau}{n}\right)^2
+\frac{2(2k+5)^2\gamma^2s}{n}.
\tag{M18}
\]

For a stationary finite ergodic Markov chain take \(\gamma=3\), \(s=T\). If \(r=n/T\ge4\), choose
\(L=\lceil\log_2r\rceil\), \(\tau=TL<n\). The standard mixing contraction bound gives \(\beta(\tau)\le1/r\). Thus a valid finite-sample consequence is

\[
\operatorname{MSE}\le
\min\left\{1,
\frac{64(1+L)^2}{r^2}
+\frac{4(k+1)^2L^2}{r^2}
+\frac{18(2k+5)^2}{r}\right\}.\tag{M19}
\]

For \(r\to\infty\), the displayed bias terms are lower order than the quadratic leading term, since \(L^2/r\to0\). This gives consistency if \(k+1=o(\sqrt r)\). If a future variance argument produces a linear term \((k+1)/r\) while retaining this bias bound, absorbing its second bias term also requires \((k+1)L^2=O(r)\), or the bias term must be stated separately.

#### A precise obstruction to using only worst-case coordinate changes

At window length one, \(\widehat S_k\) is \(G_k\). For an integer \(0\le k\le n-2\), take a sample with exactly \(k+2\) occurrences of one label \(a\), and make every other observation a different label. Replacing one \(a\) by a fresh label increases \(nG_k\) by exactly \(k+2\). Therefore its best worst-case one-coordinate Lipschitz constant is at least \((k+2)/n\) in this range. A proof using only that constant in a standard bounded-differences variance inequality retains a quadratic rarity factor. This is a limitation of that proof route, not an impossibility theorem for a linear minimax rate. For \(k\ge n-1\), \(G_k\) is identically one and this lower bound does not apply.

### 6. Executed finite verification

`markov_work/check_cumulative_gt.py` was executed with Python 3.12. It exhaustively enumerated 2,893 count vectors across sample sizes 2–12 and five explicitly listed rational laws on two, three, and four symbols. It checked 235 `(n,p,k)` configurations. All probabilities and risks were rational `Fraction` values; all second-moment identities, plug-in inequalities, and rate-bound checks passed exactly. The full configurations and exact output are in `markov_work/cumulative_gt_exact_checks.json`.

These checks detect algebraic and implementation errors on the stated finite set. The proofs of M1–M4 cover the quantified parameter ranges; the finite enumeration alone does not.

The controlled-generator simulation and its full inputs are documented in `markov_work/controls_config.json`, `controls_run.json`, `controls_raw.jsonl`, `controls_summary.json`, and the twelve `inputs_*.npz` files. The script is `markov_work/run_controls.py`. The declared budget is 16.8 million generated tokens over 4,800 stationary trajectories. The stationary probabilities are generator inputs, so realized missing mass is available exactly. Mixing time is calculated from the known transition matrix, not inferred from token correlations. Aggregate uncertainty is Monte Carlo standard error, not a confidence guarantee for an unknown prose source.

### 7. Remaining questions

Q853 still requires either a general \(O(T/n)\) estimator or an impossibility result for that rate. Q854 still requires a variance argument that handles positive dependence among missing indicators for arbitrary kernels. Q855 now has a strictly improved iid upper envelope, but its matching minimax lower bounds and full Markov frontier are open in this work. Q859 has an iid growing-threshold solution, while replacing its Markov quadratic rarity factor with a linear one remains open. None of the generator results certify a mixing-time parameter for real text.


---

## Appendix D. Missing-mass minimax-constant analysis

## B8 Q856: exact minimax constant — research findings

Date: 2026-10-07. Stable statement ID: `eee2f3c01977fe365b97`.

### Retained question and disposition

For iid observations from an arbitrary distribution on a countable alphabet, let
\(M_0=\sum_xp_x1\{N_x=0\}\) and
\(R_n^*=\inf_{\widehat M}\sup_p E_p(\widehat M-M_0)^2\).
Does \(\lim_n nR_n^*\) exist, and is it

\[
c_u=\max_{0<x\le1}\frac{xe^{-x}(1-e^{-x})^2}{1-e^{-x}-xe^{-x}}
\simeq0.5700772328176?
\]

**Full question: unresolved.** This work does not prove existence of the limit,
nor its equality or inequality to \(c_u\). It establishes a complete restricted
class theorem, resolves the specific ambiguity about the cited JASA estimator's
leading constant, and provides finite reproducible checks. No formal theorem was
compiled in a proof assistant.

#### Main partial theorem

For each fixed positive integer \(R\), the asymptotic minimax constant among
unclipped estimators of the form
\(\sum_{r=1}^R\beta_{r,n}\Phi_r\), with deterministic coefficients, is exactly

\[
c_{GT}=\max_{a>0}\{(1+a)e^{-a}-e^{-2a}\}
      =0.608036786522882\ldots.
\]

Consequently, a finite, fixed collection of frequency counts with deterministic
linear coefficients cannot attain the conjectured smaller constant. This is a
restriction on an estimator class, not a lower bound of \(c_{GT}\) for arbitrary
estimators. Nonlinear estimators and a number of coefficients increasing with
\(n\) remain outside the theorem. No claim of literature novelty is made.

### Primary-source reconciliation

1. **Acharya, Bao, Kang, and Sun, December 15, 2017 working paper, _Mean Squared
   Error of Missing Mass Estimation_.** Author-hosted complete manuscript:
   https://people.ece.cornell.edu/acharya/papers/missing-mass-mse.pdf.
   Section 3, printed pp. 4–6, gives the uniform-family expression above and the
   interval \([c_u,c_{GT}]\) for the leading general minimax risk. The uniform
   upper and lower statements are Theorems 5 and 6; the sharp GT analysis is
   Theorem 4. The related 2018 proceedings paper is _Improved Bounds for Minimax
   Risk of Estimating Missing Mass_, ISIT pp. 326–330,
   DOI 10.1109/ISIT.2018.8437620; public copy:
   https://par.nsf.gov/servlets/purl/10101013.

2. **Amichai Painsky, _Generalized Good-Turing Improves Missing Mass
   Estimation_.** JASA 118(543), 1890–1899 (2023); online January 31, 2022;
   DOI https://doi.org/10.1080/01621459.2021.2020658. The publisher abstract
   advertises improved performance guarantees, including unrestricted alphabet
   size. The main article remained paywalled in this retrieval. However, the
   official, publicly accessible supplement and implementation were obtained:
   https://tandf.figshare.com/articles/dataset/Generalized_Good-Turing_Improves_Missing_Mass_Estimation/17308517.
   Metadata endpoint https://api.figshare.com/v2/articles/17308517 identifies
   official files `supp_mat.pdf` (31966763) and `code.zip` (31966760).
   Direct URLs: https://ndownloader.figshare.com/files/31966763 and
   https://ndownloader.figshare.com/files/31966760.
   Supplement Appendix G, printed p. 32, Eq. (G73), specifies the unrestricted
   estimator coefficients used below. Appendix G, pp. 38–41, Eq. (G94) onward,
   compares risk expressions with an \(o(1/n)\) remainder. Official code
   `main_unbounded_k.m` and `minimax_for_unbounded_k_parametric.m` uses exactly
   the same coefficients. The official PDF itself was downloaded and read locally.

3. A targeted recent search and the source author's publications page did not
   locate a sharp-constant closure. This is a bounded literature search, not a
   proof that none exists. Source author page:
   https://amichai.sites.tau.ac.il/publications.

The phrase “uniform family” here means arbitrary unknown finite support,
with labels conveying no known support-order information. It must not be read
as the narrower experiment where the support is promised to be exactly
\(\{1,\ldots,k\}\), whose maximum observed label supplies additional information.
The full unrestricted-countable-alphabet Q856 setup is unchanged.

### Proof of the fixed finite linear-class theorem

Write \(\Phi_r=\#\{x:N_x=r\}\). For a fixed integer \(R\ge1\), define

\[
L_{n,R}=\inf_{\beta\in\mathbb R^R}\sup_p
 E_p\left(\sum_{r=1}^R\beta_r\Phi_r-M_0\right)^2.
\]

**Theorem.** \(\lim_{n\to\infty}nL_{n,R}=c_{GT}\).

#### Lemma 1: expected profiles at uniform distributions

Fix \(a>0\), and let \(k_n=\lfloor n/a\rfloor\) (ignoring the finitely many
\(n\) for which this is zero). If \(p\) is uniform on \(k_n\) symbols, then

\[
\frac{E\Phi_r}{n}=\frac{k_n}{n}{n\choose r}k_n^{-r}
 (1-1/k_n)^{n-r}\longrightarrow
 e^{-a}\frac{a^{r-1}}{r!}.
\]

This follows by counting a specified symbol's binomial occupancy and applying
\(k_n/n\to1/a\). Also

\[
E(\Phi_1/n-M_0)=k_n^{-1}(1-k_n^{-1})^{n-1}=O(n^{-1}).
\]

#### Lemma 2: small risk forces coefficients toward GT

Consider any sequence of deterministic coefficients \(\beta_n\) satisfying
\(\sup_pE_p(\sum_{r\le R}\beta_{r,n}\Phi_r-M_0)^2\le C/n\), for a constant
\(C\) independent of \(n\). Put \(b_n=n\beta_n\),
\(\delta_n=b_n-(1,0,\ldots,0)\).

Choose \(R\) distinct fixed positive numbers \(a_1,\ldots,a_R\). Let
\(A_{i,r,n}=E_{u(k_{i,n})}\Phi_r/n\), where
\(k_{i,n}=\lfloor n/a_i\rfloor\). Lemma 1 says that \(A_n\) converges to the
matrix \(A_{i,r}=e^{-a_i}a_i^{r-1}/r!\), a Vandermonde matrix multiplied by
invertible diagonal matrices. It is invertible. Therefore \(A_n^{-1}\) is
uniformly bounded for all sufficiently large \(n\).

Jensen's inequality bounds each estimator bias by \(\sqrt{C/n}\). Subtract
the GT bias from Lemma 1 to obtain
\(\|A_n\delta_n\|_\infty=O(n^{-1/2})\). Consequently

\[
\|\delta_n\|=O(n^{-1/2}),\qquad
\beta_{1,n}=n^{-1}+O(n^{-3/2}),\quad
\beta_{r,n}=O(n^{-3/2})\ (r\ge2).
\]

#### Lemma 3: their random fluctuations differ negligibly

Replacing one observation changes any \(\Phi_r\) by at most two. The
Efron–Stein inequality therefore gives \(\operatorname{Var}(\Phi_r)\le2n\)
under every iid distribution. Define
\(H_n=\sum\beta_{r,n}\Phi_r-\Phi_1/n=n^{-1}\sum\delta_{r,n}\Phi_r\).
The covariance Cauchy–Schwarz inequality and Lemma 2 imply

\[
\operatorname{Var}(H_n)
 \le\frac{2}{n}\Big(\sum_{r\le R}|\delta_{r,n}|\Big)^2=O(n^{-2}).
\]

At any fixed uniform occupancy rate, \(EH_n=O(n^{-1/2})\).

#### Lemma 4: exact uniform GT risk and its limiting maximum

For uniform \(p\) on \(k\ge2\) symbols and \(n\ge2\), direct occupancy
moments give

\[
R_{GT}(n,k)=\frac{(1-1/k)^{n-1}}n+\frac{(1-1/k)^n}{k}
 +\frac{k-1}{k}(1-2/k)^{n-2}\left(\frac4{k^2}-\frac1n\right).
\]

Indeed \(E\Phi_1^2/n^2=(1-1/k)^{n-1}/n+
((n-1)/n)((k-1)/k)(1-2/k)^{n-2}\),
\(EM_0^2=k^{-1}(1-1/k)^n+((k-1)/k)(1-2/k)^n\), and
\(E[(\Phi_1/n)M_0]=((k-1)/k)(1-2/k)^{n-1}\); subtraction yields the formula.
Thus, when \(n/k_n\to a\),

\[
nR_{GT}(n,k_n)\to g(a)=(1+a)e^{-a}-e^{-2a}.
\]

Since \(g'(a)=e^{-2a}(2-ae^a)\), its unique positive maximum is at
\(a_*=W(2)\), the positive root of \(ae^a=2\). It follows that
\(c_{GT}=a_*/2+a_*^2/4\).

#### Completion of the theorem

Use the uniform sequence with \(n/k_n\to a_*\). Set
\(E_n=\Phi_1/n-M_0\). Its variance is \(O(n^{-1})\), and its mean is
\(O(n^{-1})\). Lemma 3 gives

\[
2|\operatorname{Cov}(E_n,H_n)|=O(n^{-3/2}),\qquad
2|(EE_n)(EH_n)|=O(n^{-3/2}).
\]

Therefore

\[
E(E_n+H_n)^2
 =EE_n^2+2\operatorname{Cov}(E_n,H_n)+2(EE_n)(EH_n)+EH_n^2
 \ge R_{GT}(n,k_n)-O(n^{-3/2}).
\]

Every sequence in the class with uniformly \(O(1/n)\) risk has limiting
worst-case constant at least \(c_{GT}\). To apply this to the infimum, choose
coefficients within \(n^{-2}\) of \(L_{n,R}\). They have \(O(1/n)\) risk
because GT belongs to the class and the source's GT upper bound is
\(c_{GT}/n+o(1/n)\). The lower inequality follows from the preceding display;
the upper inequality follows by using GT. This proves the stated limit.

The proof's lower-bound part is self-contained; its upper-bound part uses the
sharp global GT risk theorem from Acharya et al. Any known uniform \(O(1/n)\)
GT bound suffices for coefficient control, but its precise constant is needed
to conclude equality.

### Why the JASA proposal does not close Q856

For sufficiently large \(n\), Eq. (G73) defines

\[
\widehat M_P=\frac{1-2.08n^{-0.7}}n\Phi_1+4.1n^{-1.7}\Phi_2.
\]

On every sample, \(\Phi_1+2\Phi_2\le n\). Therefore

\[
|\widehat M_P-\widehat M_{GT}|
 =n^{-1.7}|-2.08\Phi_1+4.1\Phi_2|
 \le2.08n^{-0.7}=o(n^{-1/2}).
\]

For any two estimators differing by at most \(d_n\), their risks obey

\[
|R_P(p)-R_{GT}(p)|
 \le2d_n\sqrt{R_{GT}(p)}+d_n^2.
\]

The uniform GT risk bound makes the right-hand side
\(O(n^{-1.2})+O(n^{-1.4})=o(1/n)\), uniformly in \(p\). Hence

\[
\sup_pR_P(p)=c_{GT}/n+o(1/n).
\]

This conclusion follows directly from the published coefficients, regardless
of the supplement's finite-sample upper-bound derivation. It does not claim
that the whole main article was retrieved, nor that every procedure considered
there has been analyzed.

### Executed finite checks

`minimax_work/minimax_analysis.py` ran successfully under SciPy 1.17.0.
It computed both displayed constants; verified the general two-frequency-count
uniform risk formula against exact enumeration in **70 rational-arithmetic
cases**, covering all \(n=2,\ldots,8\), \(k=2,\ldots,6\), and two coefficient
choices (9,940 count-vector visits in total); and evaluated five large uniform
examples with Decimal precision 70.

| n | uniform support k | n × GT MSE | n × Eq. (G73) MSE |
|---:|---:|---:|---:|
| 1,000 | 1,173 | 0.6084413683 | 0.5901608089 |
| 10,000 | 11,729 | 0.6080772122 | 0.6046392258 |
| 100,000 | 117,288 | 0.6080408288 | 0.6074531543 |
| 1,000,000 | 1,172,875 | 0.6080371907 | 0.6079596800 |
| 10,000,000 | 11,728,754 | 0.6080368269 | 0.6080372101 |

These are evaluations at one prescribed distribution for each sample size,
not general-class minimax computations. The last row shows that pointwise
dominance for every sample size must not be inferred from early examples or
from a comparison with unspecified \(o(1/n)\) remainders. Decimal calculations
are not interval certificates. The analytic leading-constant proof above does
not depend on them.

A bounded exploratory optimization also examined the candidate
\(w c_u(x)+(1-w)c_u(y)+w(1-w)(e^{-x}-e^{-y})^2\), suggested by a two-stratum
occupancy approximation with unknown stratum masses. Domain: \(x,y\in
[0.001,20]\), \(w\in[0,1]\), seed 856, at most 200 differential-evolution
generations, population 60. It used 2,644 objective evaluations and returned
0.5700772328175747 with both rates close to 0.801351. This supplies neither a
certified global maximum nor a proved minimax reduction. No improvement over
the uniform candidate was found in this finite search.

#### Artifact and execution record

All paths below are under `/workspace/scratch/03489ce91d9b/`.

* `minimax_findings.md`: this report.
* `minimax_work/minimax_analysis.py`: executed analysis and exact checks.
* `minimax_work/minimax_analysis_output.json`: all numerical output, generator
  contract, finite search budget, seed, scope, and result flags.
* `minimax_work/artifact_manifest.json`: byte sizes and SHA-256 hashes of all
  retrieved/created local inputs present when the manifest was generated.
* `minimax_work/figshare_metadata.json`: exact official source metadata.
* `minimax_work/painsky_supplement.pdf`, `.txt`: retrieved official supplement
  and `pdftotext -layout` extraction; extraction actually ran.
* `minimax_work/painsky_code.zip` and extracted `painsky_code/`: official MATLAB
  implementation. These were inspected, **not executed**; no MATLAB optimizer
  run is claimed.
* `minimax_work/acharya2017_full.pdf`, `.txt`: retrieved manuscript and executed
  text extraction. These source copies are research inputs, not newly authored
  deliverables; exact public URLs are supplied above.
* `minimax_work/painsky_publications.html`: author-page retrieval used to inspect
  public source links.

A preliminary in-memory SciPy constant/two-stratum calculation ran before the
preserved script; the saved script reruns those numerical calculations. An
optional symbolic derivative attempt using `sympy` failed because that package
was absent in the default Python environment; no result depends on it. No
simulation, corpus data, proof assistant, or formal certificate was used.

### Independent audit of the root agent's Q855 calculation

The following was independently verified algebraically and sent to the root.
For \(k\ge0\), cumulative GT
\(A=n^{-1}\sum_xN_x1\{N_x\le k+1\}\) estimates
\(M_{\le k}=\sum_xp_x1\{N_x\le k\}\). With \(m=n-2\), the exact diagonal
term is

\[
\frac p n F_{n-1,p}(k)-\frac{p^2}nF_{m,p}(k-1)
+p^2(1-p)^2b_{m,p}(k)+p^3(2-p)b_{m,p}(k-1).
\]

For distinct symbols of probabilities \(p,q\), write \(F_m\) for their joint
CDF at \((k,k)\), and \(a_j=\Pr_m(N_x=j,N_y\le k)\),
\(b_j=\Pr_m(N_y=j,N_x\le k)\). Their off-diagonal bracket is exactly

\[
(1-1/n)F_m-2F_{m+1}+F_{m+2}
=-F_m/n+p^2(a_k-a_{k-1})+q^2(b_k-b_{k-1})
+2pq\Pr_m(N_x=k,N_y=k).
\]

Dropping negative terms and summing yields
\(\operatorname{MSE}(A)\le1/n+3B_k+2C_{k-1}+2C_k\), where
\(B_r=\sup_pp\Pr(\mathrm{Bin}(n-2,p)=r)\),
\(C_r=\sup_pp^2\Pr(\mathrm{Bin}(n-2,p)=r)\).
Since \(C_r\le B_r\le3\sqrt{r+1}/n\) for \(n\ge4\), \(r\le n/2\), the
root's bound \(22\sqrt{k+1}/n\) is valid. The last bound follows from the
maximizer \(p=(r+1)/(n-1)\), Stirling's binomial point-mass bound, and the
finite endpoint cases \(n=4,5\). This is an independent written check, not a
proof-assistant check; the complete Q855 statement belongs in the root report.


---

## Appendix E. Complete prose protocol and results

## B8 supplementary prose pilot: chronological coverage and new-type prediction

Date: 2026-10-07. Evidence class: **finite computation on two declared public
corpora**. This is the empirical continuation proposed in the B8 handoff. It
does not close any Q851–Q859 mathematical statement.

### Findings

The frozen Good–Turing missing-mass diagnostic underestimated the realized
future proportion of training-unseen tokens in all **54** chronological
evaluations, by **0.8–8.5 percentage points**. The Poisson-smoothed
Good–Toulmin predictor with fixed smoothing mean 3 underestimated distinct new
types in **52 of 54** evaluations. Its signed relative errors ranged from
**−55.64% to +2.53%**. These are finite, overlapping comparisons; the counts
are not independent replicates and no significance test is attached to them.

The following rows average the three chronological positions within each
book. Training budgets and future ratios are identical across books.

| Book | Training tokens | Future tokens | GT diagnostic | Observed novel-token proportion | Predicted distinct new types, r=3 | Observed distinct new types |
|---|---:|---:|---:|---:|---:|---:|
| Alice | 1,000 | 1,000 | 23.00% | 28.80% | 176.86 | 203.67 |
| Alice | 3,000 | 3,000 | 13.57% | 19.31% | 299.17 | 393.67 |
| Alice | 5,000 | 5,000 | 10.45% | 16.45% | 389.43 | 486.33 |
| Alice | 5,000 | 10,000 | 10.45% | 17.50% | 654.50 | 885.67 |
| Pride and Prejudice | 1,000 | 1,000 | 23.90% | 29.23% | 189.23 | 234.67 |
| Pride and Prejudice | 3,000 | 3,000 | 16.02% | 20.20% | 371.85 | 467.00 |
| Pride and Prejudice | 5,000 | 5,000 | 12.90% | 17.05% | 494.43 | 651.33 |
| Pride and Prejudice | 5,000 | 10,000 | 12.90% | 17.19% | 805.47 | 1,142.00 |

The full table also includes future ratios 0.5 and 2 at every training budget,
each individual position, singleton and doubleton counts, and smoothing means
2 and 4. There was no negative or above-future-token-budget prediction for the
primary smoothing mean 3 in these 54 rows. Feasibility alone did not imply
accuracy.

The static diagnostic plot is
`prose_work/chronological_diagnostics.png`, with an exportable SVG companion.
Its dashed lines indicate equality. Both estimands predominantly fall below
their corresponding held-out observations.

### Data and permissions contract

These are two original-English novels; no translation, lemmatization, or
dictionary-based language filtering was used. The retained alphabet includes
proper names, contractions, and occasional non-English words appearing in the
novels, subject to the same tokenization rule.

| Corpus | Primary metadata | Exact downloaded text | Retained tokens | Retained types |
|---|---|---|---:|---:|
| Lewis Carroll, Alice's Adventures in Wonderland | https://www.gutenberg.org/ebooks/11 | https://www.gutenberg.org/cache/epub/11/pg11.txt | 26,613 | 2,616 |
| Jane Austen, Pride and Prejudice | https://www.gutenberg.org/ebooks/1342 | https://www.gutenberg.org/cache/epub/1342/pg1342.txt | 122,169 | 6,314 |

Both Project Gutenberg metadata pages designate their texts public domain in
the USA. The exact downloaded raw files retain their complete Gutenberg
license, wrapper, credits, and publication metadata. The pilot used
**148,782** retained narrative tokens in total, below the declared one-million
token budget. It did not access private files or any other corpus.

The download SHA-256 hashes are:

* Alice raw UTF-8: `01b38ea4c710a84bc18d0bd41271a5a1a92b94e97b2812f4dece97d4a694725e`.
* Pride raw UTF-8: `3f6bb9d6f78e0293b56acd4714dd68cb7d6d1d293402031ce9d5a216bcaf9d75`.

The coordinating reviewer independently reopened the primary Project
Gutenberg metadata and checked the exact text links. No automatically
generated book synopsis was used as research evidence.

### Preprocessing, fixed before the numerical evaluation

The parser first removes everything outside the explicit `*** START OF THE
PROJECT GUTENBERG EBOOK ... ***` and `*** END OF THE PROJECT GUTENBERG EBOOK
... ***` lines. Their exact observed strings are recorded in
`corpus_records.json`.

Alice is cropped from the unique opening narrative literal “Alice was
beginning to get very tired” through the narrative ending before the standalone
`THE END`. This excludes the title page and table of contents. Eleven later
chapter headings and their following title lines are removed.

The Gutenberg Pride edition includes George Saintsbury's preface, a list of
illustrations, and Hugh Thomson illustration captions. The corpus is cropped
from “It is a truth universally acknowledged,” through “had been the means
of uniting them.” This excludes 34,294 characters of front matter after the
Gutenberg start marker and the final printer colophon. Within the retained
body, 154 `[Illustration ...]` groups are removed with a balanced-bracket
parser, including nested brackets, and 60 chapter-heading lines are removed.
The text being measured is consequently Austen's narrative rather than the
edition's preface and captions.

Tokenization performs Unicode NFC normalization, `str.casefold()`, and maps
curly apostrophes U+2018/U+2019 to ASCII apostrophe. A token is a maximal
Unicode-letter string, permitting an apostrophe internally only when directly
flanked by letters. `str.isalpha()` defines a letter. Hyphens split tokens;
numbers and other punctuation are excluded. Leading/trailing quotation marks
are not part of tokens. There is no lemmatization or stopword removal.

The script verifies the example `Don't DON’T Mother-in-law 123 café 'cat'
Alice’s` becomes `don't, don't, mother, in, law, café, cat, alice's`.
The exact cleaned narratives and one-token-per-line token sequences are saved,
so the alphabet and all offsets can be reconstructed without re-downloading.

### Observation and hold-out design

Each book is the corpus unit. For each of three chronological starts, the
training window has \(n\in\{1000,3000,5000\}\) tokens. The immediately following
future block has \(m=tn\) tokens for \(t\in\{0.5,1,2\}\). Every future block
follows its own training window in the original order; no future token enters
that window's estimator.

The longest planned training-plus-future horizon is 15,000 tokens. Starts are
the beginning, midpoint, and end of the allowable start range for that horizon:

* Alice: zero-based offsets **0, 5,806, 11,613**.
* Pride and Prejudice: zero-based offsets **0, 53,584, 107,169**.

Equivalently, starts are
\(\operatorname{round}(f(N-15000))\) with \(f\in\{0,0.5,1\}\) and \(N\)
the retained book token count. This yields 18 training windows and 54
training/future evaluations. Positions were not chosen to maximize or minimize
an error. Budgets and smoothing parameters are all explicit in
`prose_config.json`.

The windows overlap, and a token can enter more than one separate evaluation.
Means and ranges across them are descriptive summaries only. They do not
supply standard errors or confidence intervals for an author or a population
of books.

### Estimators and distinct targets

For the training window, \(N_x\) is the count of token type \(x\), and
\(\Phi_i=\#\{x:N_x=i\}\).

The Good–Turing diagnostic is
\[
\widehat M_{GT}=\Phi_1/n.
\]
Under an iid law it estimates probability mass on types absent from the
training window. Its observed comparison here is the **held-out novel-token
proportion**:
\[
\frac1m\sum_{j=1}^m1\{Y_j\notin\{X_1,\ldots,X_n\}\}.
\]
The training vocabulary remains fixed across that future block. Every
appearance of a type absent from training counts, including repetitions after
the type's first future appearance. This proportion is therefore distinct
from the rate at which previously unencountered types are first discovered
while reading the block.

The **distinct new-type count** is
\[
U=|\{Y_1,\ldots,Y_m\}\setminus\{X_1,\ldots,X_n\}|.
\]
It is predicted by the Poisson-smoothed Good–Toulmin estimator
\[
\widehat U_{r}(t)=-\sum_{i\ge1}(-t)^i
       \Pr\{L\ge i\}\Phi_i,\qquad L\sim\operatorname{Poisson}(r).
\]
The primary smoothing mean is **r=3**, with **r=2 and r=4** retained as
sensitivity checks. No value was fitted to the held-out results. Predictions
are left unclipped, so any out-of-range result would be visible. The
computation uses Poisson log-survival probabilities to avoid subtracting
nearly equal CDF values and to avoid directly raising \(t\) to a high count.

The formula was checked against the primary article by Orlitsky, Suresh and
Wu, _Optimal prediction of the number of unseen species_, PNAS 113(47),
13283–13288 (2016), DOI https://doi.org/10.1073/pnas.1607774113,
“Smoothed Good–Toulmin Estimator” section:
https://pmc.ncbi.nlm.nih.gov/articles/PMC5127330/.
This framework averages randomly truncated Good–Toulmin sums; the
Efron–Thisted variant uses a binomial smoothing distribution instead. The
article's statistical guarantees require its declared sampling models. A
fixed smoothing mean in chronological prose is used here as an explicitly
regularized diagnostic, with no minimax or confidence-coverage claim.
The coordinating reviewer independently reopened the full primary article
and checked the estimator definition.

### Sensitivity and practical implication

Smoothing sensitivity is material. In Alice's third window, with 3,000 training
tokens and 6,000 future tokens, the actual distinct new-type count is **684**.
Predictions are **459.15, 409.77, and 235.52** for smoothing means 2, 3, and 4,
respectively: a range of **223.63 types**. A larger smoothing mean is not
automatically better in a given sample.

The largest primary relative error occurs in Pride's third 1,000-token
training window and its following 2,000-token block. There are **442** distinct
new types; the primary prediction is **196.06**, a **55.64% shortfall**. The
corresponding GT diagnostic is **23.50%**, while **30.05%** of the future
tokens have types absent from training.

These examples demonstrate that a plausible numerical output and a
distribution-free iid theorem do not by themselves calibrate a chronological
prose prediction. Repetition within scenes, changes in subject matter,
differences in vocabulary across a novel, estimator smoothing bias, and finite
sample variation are possible contributors. This experiment does not isolate
their causal contributions or certify a stationary Markov model. It estimates
neither an author's complete vocabulary nor literary quality.

A prose tool can expose these quantities as separate diagnostics with their
observation contract and held-out validation. The present evidence does not
justify reporting an iid confidence interval as calibrated for arbitrary
chronological prose, or using either count as an author-quality ranking.

### Preserved observed-diversity measurements

An independent implementation also computed the handoff's observed-diversity
measures on the **same 18 training windows**, using the already saved tokens.
The original `prosescan` implementation was unavailable and was not executed;
these outputs are explicitly labeled an independent implementation. All
windows exceed the supplied reliability floors of 100 tokens for MTLD, MATTR
and Maas and 50 for HD-D.

MTLD completes and resets a factor when the segment type/token ratio reaches
or falls below 0.720. A final unfinished segment contributes the fractional
factor `(1 − residual TTR)/(1 − 0.720)`. Each directional score is window
length divided by its factor count; the reported score averages the forward
and reverse directions. MATTR averages type/token ratios over every
overlapping 50-token window. HD-D is the expected type/token ratio of a
42-token sample drawn without replacement:
\[
\mathrm{HD\!D}_{42}=\frac1{42}\sum_x\left[1-
  \frac{\binom{n-N_x}{42}}{\binom n{42}}\right].
\]
Maas is `(log n − log V)/(log n)^2`. The handoff does not specify the log base,
so both **natural-log** and **base-10** versions are retained; the latter is
exactly `ln(10)` times the former. This also avoids implying numerical parity
with an unseen implementation. The software-author documentation at
https://quanteda.io/reference/textstat_lexdiv.html explicitly exposes log base
as a parameter and confirms the supplied Maas/MATTR formulas.

| Book | Training tokens | MTLD .720 | MATTR 50 | HD-D 42 | Maas, natural log |
|---|---:|---:|---:|---:|---:|
| Alice | 1,000 | 92.50 | 0.81894 | 0.84857 | 0.020512 |
| Alice | 3,000 | 83.06 | 0.80107 | 0.85209 | 0.021653 |
| Alice | 5,000 | 83.42 | 0.80254 | 0.85510 | 0.021942 |
| Pride and Prejudice | 1,000 | 102.19 | 0.82458 | 0.86669 | 0.020201 |
| Pride and Prejudice | 3,000 | 102.50 | 0.82779 | 0.87048 | 0.020228 |
| Pride and Prejudice | 5,000 | 100.67 | 0.82496 | 0.87001 | 0.020365 |

Rows average the three existing book positions. The measures describe the
tokens observed in those windows. They are kept separate from missing mass
and future new-type predictions; no composite author score or quality ranking
is constructed. Exact per-window outputs, directional MTLD factor details,
both Maas scales, and ordinary TTR are saved in the separate diversity files.

The addition ran in **0.1215 seconds**. It verified that every reused window's
word counts match the original saved counts, checked the repeated/all-unique
limits of MTLD/MATTR/HD-D, checked an explicit fractional MTLD remainder, and
verified the Maas log-base conversion. No new corpus or hold-out run was
introduced. The supplied definitions remain the measurement contract;
primary study references are McCarthy and Jarvis (2010),
https://doi.org/10.3758/BRM.42.2.381, and Covington and McFall (2010),
https://doi.org/10.1080/09296171003643098.

### Reproducibility and executed artifact record

All paths below are relative to `/workspace/scratch/03489ce91d9b/`.

* `prose_work/prose_config.json`: frozen corpus, cleaning, tokenization,
  windows, smoothing, loss and resource contract.
* `prose_work/alice_raw.txt`, `pride_raw.txt`: exact downloaded primary texts,
  retaining the license wrappers.
* `prose_work/download_metadata.json`: requested URLs, resolved URLs, file
  sizes and original SHA-256 hashes.
* `prose_work/reproduce_downloads.py`: source retrieval/re-verification script;
  executed in cached-verification mode and passed both hashes. Its output is
  `source_verification_output.json`. A changed upstream file triggers failure.
* `prose_work/prose_pilot.py`: the executed analysis. It completed in
  **0.4195 seconds excluding downloads**, with Python 3.12.14, Unicode 15.0.0,
  NumPy 2.3.5 and SciPy 1.17.0. No random seed is needed because every analysis
  step is deterministic.
* `prose_work/alice_narrative.txt`, `pride_narrative.txt`: cleaned exact prose.
* `prose_work/alice_tokens.txt`, `pride_tokens.txt`: exact token sequences.
* `prose_work/corpus_records.json`: cleaning audit, counts, starts and hashes.
* `prose_work/training_profiles_and_counts.json`: complete observed word
  counts and frequency-of-frequency profiles for all 18 training windows.
* `prose_work/chronological_results.csv`, `.json`: all 54 raw evaluation rows.
* `prose_work/grouped_summary.csv`: all 18 three-position grouped summaries.
* `prose_work/run_summary.json`: complete execution metadata, scope, checks,
  summary values and resource accounting.
* `prose_work/plot_prose.py`: executed static-plot script;
  `chronological_diagnostics.png` and `.svg` are its outputs. The rendered PNG
  was visually inspected for legibility and correct axes.
* `prose_work/diversity_config.json`, `diversity_measures.py`: the independent
  observed-diversity contract and executed script on the same 18 windows.
* `prose_work/observed_diversity.csv`, `.json`: all per-window diversity
  outputs, including both Maas log bases and reliability-floor flags.
* `prose_work/mtld_direction_details.json`: directional factor counts and
  residual-factor details; `diversity_run_summary.json` records execution,
  checks, input hashes, and grouped means.
* `prose_work/artifact_manifest.json`: SHA-256 and byte size for every saved
  pilot artifact at final manifest generation.

Wrapper boundaries, unique narrative crop literals, the tokenization example,
all future-block lengths, the number of evaluation rows, and the computation
budget were checked during execution. There was no proof-assistant use,
language-model scoring, resampling confidence interval, unrecorded corpus, or
mixing-time estimate in this pilot.


---

## Appendix F. Coordinating independent review

## B8 coordinating mathematical review

Date: 7 October 2026. Evidence class: independently written mathematical review. This is not a proof-assistant certificate or human peer review.

### Q852 — f9edd65b797563064576

The coordinating reviewer read the complete support proof and independently checked the following steps: the top-n-mass variational identity and its countable-alphabet interpretation; the direction of both horizontal hinge inequalities; the positive trigonometric kernel and its degree/tail estimates; conversion to bounded algebraic polynomials; the centered falling-factorial covariance formula; the low-probability estimator's mass-weighted moments and erroneous-branch bias; the local estimator's normalized-distance tail bounds, cardinality 2/t estimate, and essential p/t weighting for infinitely many small atoms; the order of universal constant choices; uniformity over gaps at least exp(-sqrt(log n)); the empirical fallback below that gap; and the deterministic budget coupling of two Poisson samples.

No substantive gap was found. A second reviewer independently requested expansion of countable absolute-integrability details. The final proof supplies that expansion: for local tiny atoms the full middle-gate probability multiplies E|U|, retaining its p/t factor; for the low estimator P(0)=0 supplies a direct mass-weighted factorial-moment bound. These arguments justify the expectation and variance sums. The final statement covers all countable probability laws, all n>=1, and all 0<delta<1 with a universal constant. The conclusion is **proved by the written argument**, with unchanged Q852 assumptions. Practical numerical constants and an implemented polynomial tester are not claimed.

### Q858 — 0c3cb5efa6b7fd0651a8

The coordinating reviewer independently derived the Ising field mapping, then checked the complete self-contained proof: coordinatewise read-two Cauchy–Schwarz; unit-disc contraction; the graph-polynomial coefficient identity; the uniform nonvanishing region; centered real-MGF bound; the harmonic Taylor-coefficient bound; countable truncation and exponential-moment domination; exact fixed-n covariance decomposition; uniformly bounded interaction-error kernel; dominated convergence of the positive interaction correction; the negative correction Q_n=o(B(n)); and the monotone fixed-law de-Poissonization.

No substantive gap was found. The uncentered cumulant display initially included order one; a separate reviewer identified and the author corrected this notation to orders k>=2. The CLT only uses these orders. The conclusion is **proved by the written argument**, for fixed arbitrary loopless countable pair laws without dust or connectedness assumptions. No finite-sample confidence interval or variance-estimation theorem is inferred.

### Q855 — eeea824c340739a51a8d

The coordinating author derived the exact diagonal and off-diagonal fixed-n cumulative-Good–Turing error identities. The minimax reviewer independently recomputed the identities and positive-term upper bound. A separate exact rational enumeration checked 235 (n,p,k) configurations over 2,893 count vectors. The argument proves the explicit upper bound min(1,22 sqrt(k+1)/n) for k<=n/2 on any countable iid law. The complementary plug-in bound follows pointwise by Cauchy–Schwarz and is valid for arbitrary observations. Its iid and stationary Markov consequences follow from the stated empirical L2 variance calculations. These are upper bounds; no matching minimax lower bound is claimed. The full Q855 status remains **partial**, while uniform growing-threshold sharpness of the previous linear iid upper bound is **disproved**.

### Q854 — ad6c67395090a5839dec

The support reviewer independently audited the stationary refresh-chain construction, pairwise-negative missing-indicator covariance, exact uniform variance formula, and the asymptotic order example. The argument proves a stronger linear bound only for the specified kernel family. No general-chain result follows; full status **partial**.

### Q856 — eee2f3c01977fe365b97

The coordinating reviewer checked coefficient identifiability via the finite Vandermonde system, the Efron–Stein variance control, the exact uniform Good–Turing second moment, and the leading-risk perturbation argument. The restricted-class lower bound is self-contained; equality of its leading constant also uses the primary paper's sharp global Good–Turing upper bound, directly rechecked in Theorem 4. The Painsky coefficient formula was inspected in the official supplement. The result covers fixed R, deterministic coefficients, and unclipped linear estimators only. The global limit and uniform-family conjecture remain **unresolved**, so the member's overall research disposition is **partial**.

### Q859 — 11f05c2567c0a33574c8

The support reviewer independently audited the iid two-group Le Cam construction and the local Stirling approximation. The KL remainder is O(k/n), so no unstated condition k^2/n->0 is needed. The proof establishes the iid rate Theta(k/n) for k->infinity and k=o(n); it does not establish linear rarity dependence for general Markov chains. The published Corollary 2 was directly checked, and all its bias terms are retained in the finite-sample specialization. Overall status **partial**.

### Q851 and Q853

No new rate theorem closes either exact target. Source comparison, auxiliary results, and finite experiments are not substituted for their requested minimax conclusions. Both are **unresolved**.

### Evidence boundary

All reviews above are internal independent mathematical checks in this research run. None is an external publication, formal kernel acceptance, or a guarantee that the proof has no error. All computational checks apply only to their recorded finite inputs. The exact statement ledger separately records these evidence levels.


---

## Appendix G. Independent support-proof audit

## Independent audit of the Q852 polynomial estimator

**Date:** 7 October 2026. **Programme:** B8. **Question:** Q852. **Stable ID:** `f9edd65b797563064576`.

**Audited artifact:** `/workspace/scratch/03489ce91d9b/support_findings.md`, the candidate affirmative theorem and its proof in Sections 1–7. This audit concentrates on Sections 3, 5, 6, and 7 as requested, and checks the deterministic reduction and moment identity on which they depend.

### Verdict

**The written argument supports the full stated Q852 upper bound. No additional support restriction, gap restriction, or growth regime is required.** In particular, the argument establishes a universal constant C such that for all integers n>=1, all gaps 0<delta<1, and all probability laws on arbitrary countable alphabets, an estimator using at most

\[
C\frac{n\log^2(e/\delta)}{\delta^2\log(en)}
\]

iid observations estimates d_n to error delta/4 with probability at least 3/4. Thresholding therefore provides the assigned tolerant test.

One initially terse justification needed expansion: the countable-alphabet estimator requires absolute integrability of its coordinate sum, not merely a finite sum of coordinate second moments. Direct bounds establish the required absolute integrability. The originating agent added those bounds to Sections 5–6 during the audit. This was an exposition gap with a valid repair, not a restriction on the theorem.

The conclusion is a mathematical proof audit, not a proof-assistant check, empirical validation, human peer review, or a claim that the result is absent from all prior literature. No extra experiment was needed or run for this audit.

### 1. Horizontal approximation and minimization

For every countable probability law, the formula

\[
C_n(p)=\inf_{t\ge0}\left(nt+\sum_i(p_i-t)_+\right)
\]

is correct, with minimizer p_(n), including ties and finite support of size below n. The countable sum is bounded by sum p_i=1, so no cardinality hypothesis enters.

The proposed sandwich is correctly directed:

\[
F_p(t)-\eta-b\le E\widehat F(t)
\le F_p(t-h)+\eta+b.
\]

Taking the minimum on the grid does not turn the upper horizontal shift into an error depending on the total number of symbols. For the grid point j=ceil(p_(n)/h)+1,

\[
t_j-h\ge p_{(n)},\qquad t_j\le p_{(n)}+2h,
\]

so monotonicity of F_p gives the claimed upper error 2nh. Every grid value separately gives the lower inequality because nt+F_p(t)>=C_n. The clipping operation cannot increase the estimation error relative to C_n in [0,1]. This part of the construction is valid on unrestricted countable support.

### 2. Polynomial construction

#### 2.1 The concentrated positive trigonometric kernel

The normalized power of the squared Dirichlet ratio has degree q(k-1) and is nonnegative. On |theta|<=1/(k sqrt(q)), its unnormalized integral is at least c/(k sqrt(q)). Outside |theta|>=a, integrating `(pi/(k|theta|))^(2q)` and dividing by that normalization gives a bound proportional to

\[
\frac{\sqrt q}{2q-1}\pi
       \left(\frac{\pi}{ka}\right)^{2q-1}.
\]

With k>=4pi/a this decays geometrically in q. Consequently q=O(log(1/eta)) and k=O(1/a) give the stated degree. The integer ceilings and the range eta<1/2 change only universal constants.

#### 2.2 Low interval

For theta(x)=arccos(1-2x/r),

\[
\theta'(x)=\frac1{\sqrt{x(r-x)}}.
\]

On [t-h,t], this is at least 1/sqrt(rt), including the integrable singularity if t=h. The angular gap is therefore at least h/sqrt(rt). The two boundaries of the symmetric circular arc are both at sufficient distance from the required low and high regions; the restriction t<=r/4 ensures there is no opposing-boundary problem near theta=pi.

Convolution with the positive normalized kernel gives 0<=S<=1, S<=eta below t-h, and S>=1-eta above t. Integrating from zero produces P(0)=0 and 0<=P(x)<=x. Its lower error is at most eta(x-t)<=eta x, and its upper error is at most eta times the integrated low interval, again at most eta x. Thus the pointwise sandwich and degree bound are correct.

#### 2.3 Positive cutoff interval

The local interval has half-width 2w. Its angular derivative is at least 1/(2w), giving the required degree O((1+w/h)log(1/eta)). When h>=2w, the stated linear polynomial satisfies the sandwich directly. Otherwise the transition lies inside the local interval.

Integration from t-2w initially gives an error eta(x-(t-2w)); the assumption w<=t/8 implies x-(t-2w)<=4w<=x throughout the interval. The conversion to eta x is therefore valid. No error proportional to the actual support size appears.

### 3. Factorial moment calculation

The exponential generating function

\[
e^{-az}(1+z/m)^N
\]

indeed has coefficient u_j/j!. Under N~Poi(mp), the expectation of its product at z and y is

\[
\exp\big((p-a)(z+y)+pzy/m\big).
\]

This gives exactly

\[
E[u_j u_k]
=\sum_{s=0}^{\min(j,k)}\binom js\binom ks s!
 (p/m)^s(p-a)^{j+k-2s}.
\]

The powers, scale m, and factor s! are correct. Centered polynomial estimation is unbiased. The geometric monomial coefficient bound follows from Chebyshev coefficients and the three-term recurrence, with an absolute constant A independent of the interval, center, m, or distribution.

### 4. Low-probability estimator

Let ell=mr=K_0L and x=p/r. Since P(0)=0, only degrees j,k>=1 appear in its second moment. In the normalized factorial expansion every power x^(j+k-s) has exponent at least one. For x<=1, this supplies the mass factor x; the remaining combinatorial sum is bounded by exp(L^2/ell). For x>=1, the power can be bounded by x^(2L). Both cases are as claimed.

The low-count gate has probability at most exp(-mp/8) when p>=r. For sufficiently large fixed K_0,

\[
x^{2L}e^{-K_0Lx/8}\le x\qquad(x\ge1).
\]

This yields the globally mass-weighted second moment C r p B^L. The linear-branch variance formula is also exact because the gate and estimation count are independent. Its classification term is bounded by Cpr in each of the three stated p ranges; all sums then use sum p=1.

For the low-probability wrong high gate, Markov’s inequality applied to 2^N-1 gives the necessary p/r factor. Specifically the threshold exponent `(log 2)ell/2` exceeds the largest numerator exponent ell/4 by a fixed positive multiple of ell. Absorbing a polynomial ell factor into a weaker exponential is valid because ell>=K_0. This proves the small-p bias bound uniformly.

For p>r, the polynomial extension grows at most geometrically in its degree times (p/r)^L. The exponentially unlikely low gate dominates that growth. Increasing fixed K_0 absorbs A^L and makes the summed bias exponentially small in L. There is no mismatch between the parameter used for the variance gate and the one needed for the bias gate.

### 5. Local estimator

#### 5.1 Polynomial second moment

After normalizing by the interval half-width 2w, the second-moment identity contains the factor p/(4mw^2). For v=|p-t|/(2w)<=1, the factorial overlap sum is bounded by

\[
\exp\left(\frac{L^2p}{4mw^2}\right)
\le\exp(CL/K),
\]

since p<=5t/4 and w^2=KtL/m. For v>=1, factoring out v^(j+k) gives exponent L^2p/(m(p-t)^2). The inequalities p<=t+|p-t|, |p-t|>=2w, and mw>=8KL again bound this by CL/K. Thus equation (15), including its dependence on the center and width, is correct.

#### 5.2 Far-middle gate and infinitely many small coordinates

The one-sided Poisson bounds give

\[
\gamma(p)\le
 \exp\left(-\frac{m(p-t)^2}{8\max(p,t)}\right)
\]

outside the doubled interval. With v>=1 and 2w/t<=1/4, its exponent is at least `(2/5)KLv`. This dominates the factor v^(2L) once K is a sufficiently large absolute constant. For p>=t/2, the number of coordinates is bounded by 2/t, giving the asserted second-moment sum.

For p<t/2, the threshold of the middle gate is at least 7mt/8. Applying the same 2^N-1 argument gives

\[
\gamma(p)\le C(p/t)e^{-cmt}.
\]

Here `(7/8)log2-1/2>0`, so the exponent is genuinely negative with an absolute constant. With y=mt/(KL)>=64, the polynomial growth is at most (y/4)^L. The exponential exp(-cKLy) dominates this uniformly in y>=64 for fixed sufficiently large K. The factor p/t survives and permits summation over an arbitrary countable collection of tiny probabilities.

#### 5.3 Linear branch and bias

The variance term `beta(1-beta)(p-t)^2` is O(w^2) per coordinate for p>=t/2. Within the doubled interval this is immediate; outside it the relevant rare classification tail is bounded by the same exponential envelope used above. Tiny coordinates again have the factor p/t, which makes their total contribution bounded by Ct exp(-cmt)<=C/m.

Wrong non-middle classifications create downward errors relative to the hinge, as claimed. For p=t+d>=t, the exponent for erroneous low classification is

\[
\frac{m(d+w)^2}{2(t+d)}
=\frac{KL}{2}\frac{(1+d/w)^2}{1+(w/t)(d/w)}
\ge\frac{KL}{2}(1+d/w).
\]

Thus the loss d times this tail is bounded by Cw exp(-cKL). The analogous upper-tail inequality works for p<t. Counting coordinates only in p>=t/2 costs at most 2/t, and w/t<=1/8. The small-p class uses its mass-weighted bound. Polynomial contributions outside the approximation interval are controlled by the same gates; inside it the eta p errors sum to at most eta. This proves the stated bias sandwich.

### 6. Absolute integrability and countable sums

This was the one point whose original exposition was too compressed. A sum of coordinate variances alone is insufficient to justify exchanging an infinite sum and expectation. The needed repair is elementary and now appears in the source artifact.

For the low estimator, expand P(p)=sum_{j=1}^L a_j(p/r)^j with sum|a_j|<=Cr A^L. Since factorials of a nonnegative integer are nonnegative,

\[
E|U_P(N)|\le\sum_{j=1}^L|a_j|(p/r)^j.
\]

For p<=r this is at most C A^L p. For p>r, multiply the polynomial growth bound by the independent low-gate probability to obtain another finite multiple of p. Also,

\[
E|N/m-t|\,\Pr(\mathrm{high})
\le(p+t)\Pr(\mathrm{high})
\le p+2tp/r\le(3/2)p.
\]

Thus sum_i E|Y_i|<infinity.

For the local estimator, there are only finitely many p>=t/2. In the small-p class, independence must be used in the order

\[
E[|U_P(N)|1_{\mathrm{middle}}]
=\gamma(p)E|U_P(N)|
\le\gamma(p)\sqrt{EU_P(N)^2}.
\]

The factor p/t in gamma is retained. Applying Cauchy–Schwarz to the already gated variable instead would lose that factor and would not suffice. The displayed bound, the moment estimate, and the small-p gate estimate give a finite constant times p for every coordinate. The linear branch is handled identically. Again the absolute expectation sum is finite.

Both statistics are almost surely finite sums over observed symbols: in the low estimator, an entirely unobserved symbol vanishes because P(0)=0; in the local estimator the middle and high gates exclude a zero second count. Absolute expectation convergence and the proven summable variance bounds then justify all countable calculations and identify the limit with the observable statistic.

### 7. Quantifiers, constants, and the advertised rate

The order of choices is noncircular:

1. Fix the kernel and coefficient constants.
2. Choose the local gate constant K large enough to dominate the polynomial extension. Choose K_0>=256K large enough for the low gate as well.
3. Fix the resulting variance base B and bias exponent c_1. Choose c>0 so that B^(c log n)<=n^(1/4), and set L=floor(c log n).
4. Choose C_0 large enough for polynomial degree, after c, K, K_0, and all approximation constants are fixed.
5. Choose the universal lower threshold for n large enough for the remaining first-degree term, bias bound, and grid concentration estimate.

With H=log(e/delta) and m=C_0 n H^2/(delta^2 log n), the second term of the degree bound reduces to

\[
C_2\sqrt{\frac{L\log n}{C_0}}.
\]

Since L is comparable to c log n, a sufficiently large fixed C_0 makes this at most L/2. The remaining degree term C_2 H is at most L/2 eventually, uniformly under delta>=exp(-sqrt(log n)). The required sample constant may be extremely large; the theorem claims existence, not practical calibration.

The local estimator begins only when t>K_0L/(4m)>=64KL/m, so its width assumption holds. The grid maximum is at most 1/n+2h<2/n. Every point has t>=h, as required by the deterministic minimization lemma.

At most C/delta grid values are used. The variance bound and union bound give

\[
C\frac{\log^2n}{n^{3/4}\delta H^2}
\le C\frac{\log^2n\,e^{\sqrt{\log n}}}{n^{3/4}},
\]

which tends uniformly to zero. The polynomial bias exp(-c_1L) is likewise uniformly smaller than delta/128 in that regime. No omitted requirement such as delta>=constant/sqrt(log n) enters this argument.

For smaller delta, the empirical fallback costs O(n/delta^2). Since H^2>=log n there, it obeys the proposed bound. The finitely many small n are absorbed into a universal constant using log(en); this absorption is uniform in delta because H>=1. For delta>1/2, the fixed delta=1/2 procedure has stronger accuracy, and its cost differs from the advertised expression by a bounded universal factor.

Finally, generating two Poisson sample sizes before collecting observations and aborting if their sum exceeds 8m gives a valid fixed maximum sample budget. Coupling to the ideal untruncated experiment changes the failure probability by at most the Poisson tail. It does not condition or otherwise invalidate the analyzed count arrays on successful runs. The accumulated error probability remains below 1/4 with the displayed slack.

### 8. Reconciliation recommendation

**Q852 / `f9edd65b797563064576`: proved by the complete written argument, with no changed assumptions.** The explicit countable-integrability repair above is part of the audited proof. Mark primary-source comparison separately from mathematical proof, and keep compiled-formal-theorem status as not attempted.

**Q851 / `c72db31c0497eb836a83`: unresolved.** The Q852 estimator has delta^-2 dependence and does not remove the non-tolerant epsilon^-1 logarithmic gap. No cross-promotion is justified.


---

## Appendix H. Independent pair-proof audit

## Independent audit of the Q858 proof

Date: 2026-10-07. Reviewer: the independently delegated Q856 research agent.
Target: B8/Q858, stable ID `0c3cb5efa6b7fd0651a8`.
Reviewed file: `/workspace/scratch/03489ce91d9b/pair_findings.md`.

### Finding

No substantive mathematical gap was found in the written proof. The exact
fixed-law, countable, loopless pair model is essential to its final
de-Poissonization argument and is preserved throughout. This audit is a written
mathematical review, not a compiled formal verification or an external peer
review. It does not independently establish priority or literature novelty.

### Checks performed

1. **Contraction lemma.** For fixed \(|x|<1\), bidisc stability of
   \(A+Bx+Cy+Dxy\) indeed implies \(|A+Bx|\ge|C+Dx|\). Integrating the squared
   inequality and its symmetric version, then letting the circle radius tend
   to one, proves \(|A|\ge|D|\); \(A\ne0\) makes the contracted polynomial
   \(A+Dz\) nonzero in the open disc. Degenerate denominator cases do not
   invalidate the inequality. Fixing all additional variables in their unit
   discs makes the same argument applicable at every multivariate contraction.

2. **Edge-factor assembly.** The identity
   \(|1+ax|^2-|a+x|^2=(1-a^2)(1-|x|^2)\) applies for every \(0\le a\le1\),
   including endpoints. Iterative contractions retain exactly the monomials
   selecting either all or none of a vertex's incident half-edge variables.
   Degree-one and isolated vertices are covered. This gives the claimed graph
   polynomial with products of crossing-edge weights.

3. **Probability-to-polynomial mapping.** For a finite retained vertex set,
   external edges incident to distinct retained vertices are disjoint
   independent inputs even when they have a common external endpoint. Their
   aggregation into private Bernoulli variables is valid. The vertex fugacity
   \((e^s-1)e^{-b_v-d_v/2}\) and crossing-edge factors
   \(e^{-\lambda_{uv}/2}\) give exponent
   \(-\sum_{v\in S}a_v+\sum_{\{u,v\}\subseteq S}\lambda_{uv}\), exactly the
   probability that all vertices of \(S\) are absent. The resulting covered
   count is zero-free for \(|s|<\log2\).

4. **Read-two and analytic bounds.** Sequential conditional
   Cauchy–Schwarz preserves each transformed factor as the square root of a
   conditional second moment of its original factor. Thus the displayed
   read-two inequality is justified. The real centered log-MGF bound implies
   the required complex real-part bound because \(|M(s)|\le M(\Re s)\).
   The Fourier-coefficient estimate on an analytic logarithm and the geometric
   series bound for the normalized characteristic-function remainder have the
   stated constants. Positive covariances give the lower variance bound, and
   the real-MGF inequality gives the upper bound \(2B\).

5. **Countable extension.** All truncated covered counts are dominated by
   \(2N(t)\); the latter has all exponential moments. Truncated counts converge
   almost surely and their MGFs converge locally uniformly on complex discs,
   with derivatives. Hurwitz applies because the limiting MGF is one at zero.
   Unsupported vertices with \(p_v=0\) make no contribution.

6. **Fixed-law variance comparison.** The bound
   \(e^{-np}-(1-p)^n\le np^2e^{-np}\le p/e\) for \(p\le1/2\), with a summable
   large-\(p\) bound, proves the total diagonal and mean error is \(o(1)\).
   The positive edge-interaction discrepancy is an integral of
   \(n[(1-x)_+^{n-1}-e^{-nx}]\), whose absolute value is uniformly bounded.
   It is consequently dominated by \(C\mu_{uv}\), and
   \(\sum_{u\ne v}\mu_{uv}=2\) justifies dominated convergence. The negative
   multinomial correction is bounded by \(nd_n^2\), and its ratio to \(B(n)\)
   tends to zero by the displayed Cauchy–Schwarz bound and domination by
   \(e^2p_v\). Thus the fixed and Poisson variances are asymptotically equal
   under the required divergence condition.

7. **De-Poissonization.** An initial concern was that Poisson sample-count
   fluctuations might dominate when the fixed-sample variance is \(o(n)\).
   The proof resolves this: for a fixed countable law,
   \[
   nD(n)^2/B(n)\le\sum_vp_v\frac{np_v}{e^{np_v}-1}\to0.
   \]
   A slowly increasing \(c_n\) can therefore satisfy both stated constraints.
   Splitting at \(p_v=4\log n/n\) proves the claimed comparison between
   \(D(n-h_n)\) and \(D(n)\). Chebyshev controls the Poisson count outside the
   window, while the expected coverage increment inside it is
   \(o(\sqrt{B(n)})\). Monotonicity and Markov's inequality prove the coupling
   error is negligible on the correct variance scale. The mean and variance
   comparisons then justify Slutsky's theorem.

### Minor correction communicated to the author

The initial version of Eq. (5.4) wrote the cumulant bound for
\(\kappa_k(F_W)\) with \(k\ge1\), although its analytic logarithm was centered.
For \(k=1\), the uncentered mean need not be bounded by a constant times
\(B_W\). The equation should refer to
\(\kappa_k(F_W-EF_W)\) for \(k\ge1\), or retain \(F_W\) and restrict it to
\(k\ge2\). This is a notation/scope correction only; every subsequent
variance and CLT step uses orders at least two.

No numerical computation or new external-source claim was needed for this
audit. The full mathematical argument remains in the reviewed proof file.

