# Information Theory & Coding

31 problems: 29 open, 2 open, partial results.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q115](information-theory-coding.md#q115) | Does truncating an 8×8 full-rate real orthogonal design, choosing the submatrix … | Open |
| [Q116](information-theory-coding.md#q116) | Can one such code family satisfy log M≥ℓC/(1−ε)+O(log ℓ) and log(M/L)≥E[τL]C/(1−… | Open |
| [Q373](information-theory-coding.md#q373) | Use Tse’s fixed-block variable-length quantization model (§§2.1, 3.1): the obser… | Open |
| [Q378](information-theory-coding.md#q378) | What is the noisy-permutation capacity of the following \$q\$-symbol “zigzag” chan… | Open |
| [Q429](information-theory-coding.md#q429) | Exact entropy profiles with two pairwise independences | Open |
| [Q433](information-theory-coding.md#q433) | Lifting a self-adhesive CI pattern to a self-adhesive polymatroid | Open |
| [Q449](information-theory-coding.md#q449) | A common garbling decoder for opposite-correlation binary models | Open, partial results |
| [Q556](information-theory-coding.md#q556) | Channel coding with a fixed-state receiver | Open |
| [Q614](information-theory-coding.md#q614) | Are coordinate summaries optimal through seven bits? | Open |
| [Q615](information-theory-coding.md#q615) | Sharp Hellinger information from a noisy Boolean sensor | Open, partial results |
| [Q628](information-theory-coding.md#q628) | Universality with arbitrary stationary-ergodic side information | Open |
| [Q694](information-theory-coding.md#q694) | An additive approximation scheme for arbitrary-marginal entropy coupling | Open |
| [Q699](information-theory-coding.md#q699) | Least redundant finite-alphabet reports of one hidden bit | Open |
| [Q700](information-theory-coding.md#q700) | A finite weak-dependence regime for symmetric report compression | Open |
| [Q744](information-theory-coding.md#q744) | Uniqueness of canonical information-optimal representations | Open |
| [Q807](information-theory-coding.md#q807) | Subexponential tree aggregation without irreducibility assumptions | Open |
| [Q830](information-theory-coding.md#q830) | Are near-constant noisy query designs globally optimal? | Open |
| [Q831](information-theory-coding.md#q831) | Exact information rate of noisy adaptive diagnosis | Open |
| [Q832](information-theory-coding.md#q832) | Order-optimal noisy observations and decoding together | Open |
| [Q833](information-theory-coding.md#q833) | Best acquisition constant with near-linear sparse decoding | Open |
| [Q834](information-theory-coding.md#q834) | Efficient certainty-preserving partial diagnosis at rate one | Open |
| [Q835](information-theory-coding.md#q835) | A universal lower bound for selectable-threshold sensors | Open |
| [Q836](information-theory-coding.md#q836) | Sharp query cost with bounded pool sizes | Open |
| [Q837](information-theory-coding.md#q837) | One-sided approximate recovery in the dense regime | Open |
| [Q838](information-theory-coding.md#q838) | Fast decoding with tightly limited evidence reuse | Open |
| [Q839](information-theory-coding.md#q839) | Optimal information threshold with limited item participation | Open |
| [Q840](information-theory-coding.md#q840) | Order-optimal inference for every monotone pooled sensor | Open |
| [Q841](information-theory-coding.md#q841) | When do pooled tests stop saving worst-case queries? | Open |
| [Q842](information-theory-coding.md#q842) | Do pairwise queries achieve the best nested Bayesian policy? | Open |
| [Q843](information-theory-coding.md#q843) | Exact eleven-query capacity for two hidden failures | Open |
| [Q844](information-theory-coding.md#q844) | Does imbalance reduce two-failure query complexity? | Open |

<a id="q115"></a>

## Q115. Does truncating an 8×8 full-rate real orthogonal design, choosing the submatrix …

**Status:** Open · **Kind:** open problem · **Collection** 2

Does truncating an 8×8 full-rate real orthogonal design, choosing the submatrix maximizing Σᵢfᵢ² (symbol multiplicities fᵢ), minimize dispersion for (nₜ,T) in {(2,3),(3,3),(3,5),(3,6),(3,7),(4,5),(4,6),(4,7),(5,5),(5,6),(5,7),(6,6),(6,7),(7,7)} and their transposes?

**Context.** Origin: Joint Collins–Polyanskiy conjecture, predating thesis filing. Thesis Conjecture 31 replaces the random-codebook assumption. Setup for question 115: Channel: Y=HX+Z, with X an nₜ×T real matrix, standard Gaussian noise, independent isotropic block fading with rank(H)≤1 almost surely and Pr(H≠0)>0, known only to the receiver; E[‖X‖²\_F]≤TP. Dispersion minimization over capacity-achieving inputs is equivalent to maximizing Var(‖X‖²\_F).

**Source.** Austin Daniel Collins. *Non-Asymptotic Results for Point to Point Channels*. Massachusetts Institute of Technology, 2019. Advisor(s): Yury Polyanskiy. [primary source](https://people.lids.mit.edu/yp/homepage/data/theses/2019_PHD_Collins.pdf) · [record](https://people.lids.mit.edu/yp/homepage/groups.shtml) Location: §6.5, printed pp.85–86 (PDF pp.86–87); conjecture immediately below Table 6.1; truncation construction and objective in (6.53). Status evidence, checked 5 October 2026: Joint paper retains the conjecture and distinguishes Gaussian-restricted optimality from the unresolved general cases. Targeted searches and the advisor's current publication list yielded no resolution.

**Further links.** [1](https://arxiv.org/pdf/1704.06962#page=34) · [2](https://people.lids.mit.edu/yp/homepage/papers.shtml) · [3](https://arxiv.org/pdf/1704.06962)

*Duplicate of Q528659910d2e23897833.*


<a id="q116"></a>

## Q116. Can one such code family satisfy log M≥ℓC/(1−ε)+O(log ℓ) and log(M/L)≥E[τL]C/(1−…

**Status:** Open · **Kind:** conjecture (Conjecture 31) · **Collection** 2

Can one such code family satisfy log M≥ℓC/(1−ε)+O(log ℓ) and log(M/L)≥E[τL]C/(1−ε)+O(log ℓ) with L=M^(1−α), fixed 0<α<1, and E[τL]=ℓ−(log L)/C? Collins conjectures impossibility.

**Context.** Origin: Joint Collins–Polyanskiy conjecture, predating thesis filing. Thesis Conjecture 31 replaces the random-codebook assumption.

**Source.** Austin Daniel Collins. *Non-Asymptotic Results for Point to Point Channels*. Massachusetts Institute of Technology, 2019. Advisor(s): Yury Polyanskiy. [primary source](https://people.lids.mit.edu/yp/homepage/data/theses/2019_PHD_Collins.pdf) · [record](https://people.lids.mit.edu/yp/homepage/groups.shtml) Location: Conjecture 31, §7.1.1, printed p.92 (PDF p.93); unique-decoding target (7.7) on printed p.91; variable-length stop-feedback model defined pp.90–91. Status evidence, checked 5 October 2026: No subsequent proof or counterexample located in exact topic searches or the advisor's current publication list.

**Further links.** [1](https://people.lids.mit.edu/yp/homepage/data/theses/2019_PHD_Collins.pdf#page=93) · [2](https://people.lids.mit.edu/yp/homepage/papers.shtml)

*Duplicate of Q033b4bba22af8313006d.*


<a id="q373"></a>

## Q373. Use Tse’s fixed-block variable-length quantization model (§§2.1, 3.1): the obser…

**Status:** Open · **Kind:** conjecture (Conjecture 3.5.3) · **Collection** 4

Use Tse’s fixed-block variable-length quantization model (§§2.1, 3.1): the observed source state \$H_n\in\\{0,1\\}\$ flips with probability \$\alpha\$, and samples are conditionally independent with state-dependent distributions. Quantizers depend on source and buffer states; the buffer has capacity \$L\$ and drains \$R_c\$ bits/slot. Let \$D_i(R)\$ be the convexified operational distortion-rate functions, with \$D_0'(R_c)&lt;D_1'(R_c)\$. Define \$V^\*(c)\$ by the fluid problem in §3.5: the source flips at rate one, the buffer \$y\in[0,c]\$ follows controlled drifts \$\mu_i(y)\$ preserving this interval, and running cost is \$D_i(R_c+\mu_i(y))\$. Is it true that, for every \$\varepsilon>0\$ and \$L\to\infty\$, \$\alpha L\to c>0\$, ergodic buffer-control schemes attain \$\limsup D_q(L,\alpha)\le V^\*(c)+\varepsilon\$ while \$p_f(L,\alpha)\$ decays exponentially in \$L\$? Here \$V^\*\$ is the minimum long-run average fluid cost, \$D_q\$ the stationary distortion contribution from nonfull-buffer slots, and \$p_f\$ the stationary full-buffer probability.

**Context.** Metadata note: Title page February 1995, signed September 1994. The title page verifies both supervisors; repository metadata lists Gallager alone. Discovery path (advisor ascent; student → supervisor):
Brice Huang → Guy Bresler: https://dspace.mit.edu/server/api/core/bitstreams/6aabbc9a-661d-4f61-8389-c91f797c7d20/content#page=1
Guy Bresler → David Ngar Ching Tse: https://digicoll.lib.berkeley.edu/record/134354/files/EECS-2013-43.pdf
David Ngar Ching Tse → Robert G. Gallager; John N. Tsitsiklis: https://dspace.mit.edu/server/api/core/bitstreams/ac990fdb-8c4b-41a1-a21d-8b3b88658b59/content Origin: Tse explicitly presents the achievability statement as his conjecture after proving the corresponding lower bound. No earlier conjecture is cited.

**Source.** David Ngar Ching Tse. *Variable-rate lossy compression and its effects on communication networks*. Massachusetts Institute of Technology, 1995. Advisor(s): Robert Gray Gallager; John Nikolaos Tsitsiklis. [primary source](https://dspace.mit.edu/server/api/core/bitstreams/ac990fdb-8c4b-41a1-a21d-8b3b88658b59/content) · [record](https://dspace.mit.edu/entities/publication/efa6b55e-835d-410c-8a34-6d2113fa95f5) Location: Conjecture 3.5.3, printed p. 82; coding model §§2.1 and 3.1, printed pp. 20–22 and 48–50; fluid optimization §3.5, printed pp. 78–81.

**Further links.** [1](https://dspace.mit.edu/server/api/core/bitstreams/6aabbc9a-661d-4f61-8389-c91f797c7d20/content#page=1) · [2](https://digicoll.lib.berkeley.edu/record/134354/files/EECS-2013-43.pdf) · [3](https://tselab.stanford.edu/publications/) · [4](https://www.mit.edu/~jnt/publ.html) · [5](https://www.mit.edu/~jnt/Papers/J056-95-tse-muxing.pdf)


<a id="q378"></a>

## Q378. What is the noisy-permutation capacity of the following \$q\$-symbol “zigzag” chan…

**Status:** Open · **Kind:** open problem · **Collection** 4

What is the noisy-permutation capacity of the following \$q\$-symbol “zigzag” channel, for \$q\ge3\$? Its transition matrix satisfies \$W_{i,i}=a_i\$, \$W_{i,i+1}=1-a_i\$ for \$i&lt;q\$, \$0&lt;a_i<1\$, and \$W_{q,q}=1\$, with all other entries zero. A length-\$n\$ input passes independently through \$W\$ and its outputs are then uniformly permuted. Capacity is the supremum of achievable rates \$\liminf_{n\to\infty}\log M_n/\log n\$ over codes whose average decoding error tends to zero.

**Context.** Discovery path (lateral/sibling branch; student → supervisor):
Austin Daniel Collins → Yury Polyanskiy: https://people.lids.mit.edu/yp/homepage/groups.shtml
Jennifer Tang → Yury Polyanskiy: https://people.lids.mit.edu/yp/homepage/data/theses/2022_PHD_Tang.pdf Origin: Tang introduces and names this channel family to expose a limitation of her converse method. It is also in her joint paper with Polyanskiy; this specific family is not merely the previously known general permutation-channel problem.

**Source.** Jennifer Tang. *Divergence Covering*. Massachusetts Institute of Technology, 2022. Advisor(s): Yury Polyanskiy. [primary source](https://people.lids.mit.edu/yp/homepage/data/theses/2022_PHD_Tang.pdf) · [record](https://people.lids.mit.edu/yp/homepage/data/theses/2022_PHD_Tang.pdf) Location: §5.5.4, printed p. 98, especially matrix (5.167) and the unresolved gap following (5.172); capacity definition in §5.1.

**Further links.** [1](https://people.lids.mit.edu/yp/homepage/groups.shtml) · [2](https://people.lids.mit.edu/yp/homepage/data/2021_permut_capacity.pdf) · [3](https://arxiv.org/abs/2111.00559) · [4](https://arxiv.org/html/2406.15031) · [5](https://arxiv.org/abs/2605.25699) · [6](https://ieeexplore.ieee.org/abstract/document/11654043)


<a id="q429"></a>

## Q429. Exact entropy profiles with two pairwise independences

**Status:** Open · **Kind:** open problem · **Collection** 5

Characterize the seven-dimensional entropy vectors of discrete triples (A,X,Y) with finite entropies satisfying I(A;X)=I(A;Y)=0, without requiring any of A,X,Y to be a function of the other two.

**Context.** Attribution: The current revision explicitly leaves this exact profile characterization open. Shared setup for question 429: The coordinates are H(A),H(X),H(Y),H(A,X),H(A,Y),H(X,Y),H(A,X,Y). Pairwise independence is expressed by zero mutual information. Alphabet cardinalities are not fixed; all entropies must be finite.

**Source.** Tobias Boege. *On the Intersection and Composition properties of conditional independence*. 2026. [primary source](https://arxiv.org/abs/2504.11978) Location: §5, “Conditional information inequalities for Composition,” printed p. 17 of arXiv:2504.11978v3 (7 May 2026).

**Literature check.** Status, checked 5 October 2026: Explicit in the May 2026 revision; no later exact-region characterization located. Closure alone is insufficient.

**Further links.** [1](https://arxiv.org/html/2504.11978) · [2](https://taboege.de/research/)


<a id="q433"></a>

## Q433. Lifting a self-adhesive CI pattern to a self-adhesive polymatroid

**Status:** Open · **Kind:** open problem (Question 4.14) · **Collection** 5

Using the CI gluing definitions for questions 423–426, is every M∈st^◇ induced by one self-adhesive polymatroid? Its numerically identical copies must, for every overlap L, admit a polymatroid extension ĥ with ĥ(N)+ĥ(N′)=ĥ(N∪N′)+ĥ(L).

**Context.** Attribution: Explicit 2023 question; the 2025 joint paper establishes the converse only.

**Source.** Tobias Boege. *Selfadhesivity in Gaussian conditional independence structures*. 2023. [primary source](https://arxiv.org/abs/2205.07667) Location: Question 4.14.

**Literature check.** Status, checked 5 October 2026: The 2025 paper proves only the converse. No later resolution of the 2023 question located.

**Further links.** [1](https://doi.org/10.1016/j.ijar.2023.109027) · [2](https://arxiv.org/abs/2402.14053) · [3](https://taboege.de/research/)


<a id="q449"></a>

## Q449. A common garbling decoder for opposite-correlation binary models

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 1) · **Collection** 5

Let (X^n,Y^n) consist of n i.i.d. DSBS(p_h) pairs under hypothesis h∈{0,1}, with p_0≠p_1 and (p_0−1/2)(p_1−1/2)≤0. For every full-row-rank binary k×n matrix G, does observing the first k pairs (X^k,Y^k) Blackwell-dominate observing (GX^n,GY^n), all arithmetic modulo two? Equivalently, is there one stochastic channel from the truncated experiment to the linearly compressed experiment that reproduces its distribution under both hypotheses? The independence endpoints and p_1=1−p_0 are already proved; the unequal-magnitude opposite-sign case remains.

**Context.** Attribution: Conjecture 1 asserts truncation optimality in Blackwell order for opposite correlations. Shared setup for question 449: DSBS(p) means X is a fair bit and Y=X⊕Z with independent Z∼Bernoulli(p).

**Source.** Adway Girish; Robinson D. H. Cung; Emre Telatar. *On the suboptimality of linear codes for binary distributed hypothesis testing*. 2026. [primary source](https://arxiv.org/abs/2601.10526) Location: Conjecture 1; §2.1 Blackwell order, Theorems 1–2; §5 numerical evidence.

**Literature check.** Status, checked 5 October 2026: The 2026 paper retains Conjecture 1. Independence endpoints and equal-magnitude opposite correlations are solved; the stated remaining regime is not.

**Results.**

- **Partial result**: Explicit common decoder for every one-row parity summary (S); explicit common stochastic decoder for an overlapping rank-two code and an infinite block family, with 27,297 exact rank-two grid comparisons (R1). Scope: General full-rank multirow case and the parameter continuum outside the proved family remain open. Recorded from the external research packet ; not independently re-derived here. [Details](../../solutions/packet-2026-10-05/01_solutions.md).


<a id="q556"></a>

## Q556. Channel coding with a fixed-state receiver

**Status:** Open · **Kind:** open problem · **Collection** 6

For a given finite-alphabet DMC W(y|x), S states and 0<ε<1, characterize C_ε(W,S)=sup_{n≥1} R\*(n,W,S,ε). Here R\* maximizes (log₂ M)/n over deterministic encoders [M]→X^n, a time-invariant update g:Y×[S]→[S], initial state U0=1 and final decoder d:[S]→[M], with a uniform message and average error≤ε. Can processing more symbols than can be stored verbatim improve the optimum, and by how much?

**Context.** Attribution: This is a newly posed open model in the primary authors’ survey, with explicit encoder, transition and readout definitions. The question is not an unsourced general claim about finite-memory communications.

**Source.** Tomer Berg; Or Ordentlich; Ofer Shayevitz. *Statistical Inference with Limited Memory: A Survey*. 2024. [primary source](https://arxiv.org/html/2312.15225v3) Location: §10 final paragraph, equations(50)–(51), pp. 43–44.

**Literature check.** Status for question 556, checked 5 October 2026: November 2024 version 3 poses the characterization. Searches for finite-state decoding capacity and this paper’s bounded-state DMC model through 2026-10-05 found no solution. Existing finite-state channel capacity and finite-state encoder results generally constrain different objects.

**Further links.** [1](https://arxiv.org/abs/2312.15225)


<a id="q614"></a>

## Q614. Are coordinate summaries optimal through seven bits?

**Status:** Open · **Kind:** conjecture (Conjecture 13) · **Collection** 7

Let X be uniform on F₂^n and Y=X⊕Z with independent Bernoulli(p) noise bits, 0≤p≤1/2. For every 2≤k≤7, n≥k and deterministic f:F₂^n→F₂^k, must I(f(X);Y)≤k(1−h₂(p))? No balance or surjectivity assumption is imposed on f; h₂ is binary entropy in bits.

**Context.** Attribution: The revision’s single grouped conjecture covers k=2,…,7; it reports counterexamples for k≥8 and a scalar proof.

**Source.** Hessam Mahdavifar; Ahmad Beirami. *The Most Informative Bit and Beyond: A Proof of the Courtade–Kumar Conjecture and Multibit Extensions*. 2026. [primary source](https://arxiv.org/abs/2609.26444) Location: 28 September 2026 v2, §VI.E, Conjecture 13, equation (31).

**Literature check.** Status for question 614, checked 5 October 2026: Explicitly conjectured in the revision; the concurrent scalar-proof paper does not resolve it. No later result located by the check date.

**Further links.** [1](https://arxiv.org/abs/2609.24931)


<a id="q615"></a>

## Q615. Sharp Hellinger information from a noisy Boolean sensor

**Status:** Open, partial results · **Kind:** conjecture (Conjecture 2) · **Collection** 7

For uniform X∈{−1,1}^n, let Y_i=X_i Z_i with independent signs of mean ρ∈[−1,1]. For every f:{−1,1}^n→{−1,1}, is sqrt(1−(E f(X))²)−E[sqrt(1−(E[f(X)|Y])²)]≤1−sqrt(1−ρ²)? The question conditions on the full noisy vector Y and allows unbalanced f.

**Context.** Attribution: Spring 2015 conjecture, published at ITA 2017; the original conditions on the full noisy vector.

**Source.** Venkat Anantharam; Andrej Bogdanov; Amit Chakrabarti; T. S. Jayram; Chandra Nair. *A conjecture regarding optimality of the dictator function under Hellinger distance*. 2017. [primary source](https://staff.ie.cuhk.edu.hk/~cnair/pub/papers/HC/hel-conj.pdf) Location: Conjecture 2; 2026 follow-up equations (1.2), (1.4).

**Literature check.** Status for question 615, checked 5 October 2026: Reaffirmed in the 29 September 2026 revision. Its one-bit-observation theorem and February’s balanced low-noise limit are weaker; Shannon-information proofs do not settle Hellinger.

**Results.**

- **Partial result**: Exact reduction to an affinity problem; exact obstruction to a tempting stronger multiplicative inequality; rigorous finite-grid audit through four Boolean inputs. Scope: The full conjecture remains unresolved. Recorded from the external research packet ; not independently re-derived here. [Details](../../solutions/packet-2026-10-05/bks_round4_research_report.md).

**Further links.** [1](https://arxiv.org/abs/2609.28534) · [2](https://arxiv.org/abs/2602.20462) · [3](https://arxiv.org/abs/2609.24931)


<a id="q628"></a>

## Q628. Universality with arbitrary stationary-ergodic side information

**Status:** Open · **Kind:** open problem · **Collection** 7

Fix m,S≥2 and a class G of state maps g:Z→[S] with finite Natarajan dimension. At time t observe Z_t before choosing b_t∈Δ\_m and then see arbitrary nonzero nonnegative return vector x_t. With W_n(b)=∏\_t〈b_t,x_t〉, can a causal strategy achieve E[sup_{g∈G,θ1:S∈Δ\_m}log(W_n((θ\_{g(Z_t)})\_t)/W_n(b))]=o(n) for every stationary ergodic Z process, without the extra Eρ\_{G×G}(Z^n)=o(n/log²n) condition? Here ρ\_H= sup_{h∈H}|Σ\_t(h(Z_t)−Eh(Z_t))| and H={1{g≠g′}:g,g′∈G}. Returns may depend on Z; they need not be stationary.

**Context.** Doctoral researcher: Alankrita Bhatt. Dissertation: Universal Probability and Its Applications. University of California San Diego, 2022. Supervision: Young-Han Kim (doctoral advisor). Attribution: Explicit removal of the empirical-process-rate condition; arbitrary deterministic contexts are known insufficient.

**Source.** Alankrita Bhatt; J. Jon Ryu; Young-Han Kim. *On Universal Portfolios with Continuous Side Information*. 2023. [primary source](https://proceedings.mlr.press/v206/bhatt23a.html) · [dissertation](https://escholarship.org/content/qt3ks510sn/qt3ks510sn_noSplash_68b7dcfb652a73a6c43656faab2c2cc8.pdf) · [record](https://escholarship.org/content/qt3ks510sn/qt3ks510sn_noSplash_68b7dcfb652a73a6c43656faab2c2cc8.pdf) Location: §§3.1–3.2, Theorem 5 and equation 13; §5; thesis §4.5.

**Literature check.** Status for question 628, checked 5 October 2026: No extension or recent explicit reaffirmation located; historical-source, bounded-search status. Classical results with stationary ergodic returns have different quantifiers and do not settle adversarial-return comparison.


<a id="q694"></a>

## Q694. An additive approximation scheme for arbitrary-marginal entropy coupling

**Status:** Open · **Kind:** open problem · **Collection** 7

Given m rational discrete marginals p_1,…,p_m, each on n states, with m part of the input, does there exist, for every fixed ε>0, an algorithm polynomial in the full input bit length returning a coupling Q with exactly those marginals and H(Q)≤min_{Q′}H(Q′)+ε bits? The number of marginals is unrestricted; the constant-m additive PTAS is already known.

**Context.** Attribution: The primary source explicitly leaves this target unresolved.

**Source.** Spencer Compton. *Efficient ε-approximate minimum-entropy couplings*. 2026. [primary source](https://arxiv.org/abs/2509.19598) Location: v3, 18 June 2026; §IV Discussion, p. 16; Theorem I.1 and Appendix A finite-precision model.

**Literature check.** Status for question 694, checked 5 October 2026: Checked 2026-10-05; bounded later-literature search found no resolution.

**Further links.** [1](https://doi.org/10.1109/TIT.2026.3710290)


<a id="q699"></a>

## Q699. Least redundant finite-alphabet reports of one hidden bit

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 7

Let X∼Bernoulli(1/2), U⊥V|X, with arbitrary finite output alphabets and I(X;U)=c, I(X;V)=d for c,d∈(0,1). Must I(U;V)≥I(Z_a;Z_b)? The comparison outputs are independent conditional on X, with P(Z_a=1|X=x)=ax and P(Z_b=1|X=x)=bx; a,b∈(0,1) satisfy h₂(a/2)−h₂(a)/2=c and h₂(b/2)−h₂(b)/2=d. Information is in bits. The binary-output case is proved.

**Context.** Attribution: Conjectures 2–3; the 2026 result proves Conjecture 2 only for binary outputs. Shared setup for questions 699, 700: Write h₂ for binary entropy in bits.

**Source.** Michael Dikshtein; Or Ordentlich; Shlomo Shamai (Shitz). *The Double-Sided Information Bottleneck Function*. 2022. [primary source](https://doi.org/10.3390/e24091321) Location: §3.1, Remark 5 and Conjecture 2; Pichler (2026), §4.1.

**Literature check.** Status for questions 699, 700, checked 5 October 2026: Explicitly open in Pichler (2026), §6; no later resolution located by the check date.

**Further links.** [1](https://arxiv.org/abs/2609.27991) · [2](https://arxiv.org/html/2609.27991v1#S4.SS1) · [3](https://arxiv.org/html/2609.27991v1#S6) · [4](https://www.mdpi.com/1099-4300/24/9/1321)


<a id="q700"></a>

## Q700. A finite weak-dependence regime for symmetric report compression

**Status:** Open · **Kind:** conjecture (Conjecture 3) · **Collection** 7

Let X∼Bernoulli(1/2), Y=X⊕N with independent N∼Bernoulli(p). Define R(c,d,p)=sup I(U;V) over finite U−X−Y−V with I(X;U)≤c and I(Y;V)≤d. For every c,d∈(0,1), is there θ(c,d)<1/2 such that R(c,d,p)=1−h₂(α\*p\*β) whenever θ&lt;p≤1/2? Here α=h₂^{-1}(1−c), β=h₂^{-1}(1−d), h₂^{-1} takes values in[0,1/2], and a\*b=a(1−b)+(1−a)b. The formula represents independent binary-symmetric compression channels.

**Context.** Attribution: Conjectures 2–3; the 2026 result proves Conjecture 2 only for binary outputs. Shared setup for questions 699, 700: Write h₂ for binary entropy in bits.

**Source.** Michael Dikshtein; Or Ordentlich; Shlomo Shamai (Shitz). *The Double-Sided Information Bottleneck Function*. 2022. [primary source](https://doi.org/10.3390/e24091321) Location: §3.1, Conjecture 3; Pichler (2026), §6.

**Literature check.** Status for questions 699, 700, checked 5 October 2026: Explicitly open in Pichler (2026), §6; no later resolution located by the check date.

**Further links.** [1](https://arxiv.org/abs/2609.27991) · [2](https://arxiv.org/html/2609.27991v1#S4.SS1) · [3](https://arxiv.org/html/2609.27991v1#S6) · [4](https://www.mdpi.com/1099-4300/24/9/1321)


<a id="q744"></a>

## Q744. Uniqueness of canonical information-optimal representations

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 8

For a finite joint law p(X,Y), put F(λ)=max_{T−X−Y:I(X;T)≤λ}I(Y;T), restricting |T|≤|X|+1, and assume F is strictly concave on [0,H(X)]. At each fixed λ, must every optimal canonical T have the same pair (q(T),q(X|T)), up to output permutation, and must q(X|T) be injective as a map from output probability distributions to distributions on X? Canonical means positive-mass output symbols have distinct posterior vectors q(X|t).

**Context.** Attribution: Audited earlier reserve, not previously delivered; primary paper conjecture.

**Source.** Hippolyte Charvin; Nicola Catenacci Volpi; Daniel Polani. *Exact and Soft Successive Refinement of the Information Bottleneck*. 2023. [primary source](https://doi.org/10.3390/e25091355) Location: AppendixD Conjecture 1,p. 45; §1.3.2 cardinality restriction.

**Literature check.** Status for question 744, checked 5 October 2026: No resolution found in checked follow-ups; strict concavity is essential.

**Further links.** [1](https://www.mdpi.com/1099-4300/25/9/1355) · [2](https://uhra.herts.ac.uk/id/eprint/10690/1/entropy-25-01355.pdf) · [3](https://proceedings.mlr.press/v282/charvin26a.html)


<a id="q807"></a>

## Q807. Subexponential tree aggregation without irreducibility assumptions

**Status:** Open · **Kind:** open problem · **Collection** 9

Must P_e(t)=exp[-o(k^t)] without any of §IV.B’s irreducibility assumptions? No internal node receives an extra private signal.

**Context.** Attribution: Explicit conjecture in the original 2011 paper. Shared setup for question 807: Fix k≥2, finite M, positive binary prior and δ∈(0, 1/2). In a depth-t k-ary tree only leaves receive conditionally iid binary signals with error δ. Fixed deterministic maps g:{0, 1}→M, f: M^k→M and h: M^k→{0, 1} encode leaves, relay internally and decide at the root.

**Source.** Yashodhan Kanoria; Andrea Montanari. *Subexponential convergence for information aggregation on regular trees*. 2011. [primary source](https://arxiv.org/abs/1104.2939) Location: Full version §IV.C.3.

**Literature check.** Status for question 807, checked 5 October 2026: Checked 2026-10-05; bounded searches found no resolution; no recent independent reaffirmation.

**Further links.** [1](https://ykanoria.github.io/subexp_cr_yk2.pdf) · [2](https://profiles.stanford.edu/andrea-montanari?tab=publications)


<a id="q830"></a>

## Q830. Are near-constant noisy query designs globally optimal?

**Status:** Open · **Kind:** open problem · **Collection** 9

Fix 0<θ<1 and 0<ρ<1/2, let k=⌊n^θ⌋, and draw S uniformly among k-subsets. Each nonadaptive OR test is independently flipped with probability ρ. Is the supremum achievable exact-recovery rate liminf log₂(binomial(n, k))/T over all designs equal to that over near-constant-column designs, optimized over ν>0? In the latter, each item independently chooses L=⌊νT/k⌋ tests uniformly with replacement. Achievable means Pr(Ŝ≠S)→0; decoding time is unrestricted.

**Context.** Attribution: Explicit question in Chen–Scarlett §4; later restated in Krieg’s thesis.

**Source.** Junren Chen; Jonathan Scarlett. *Exact Thresholds for Noisy Non-Adaptive Group Testing*. 2025. [primary source](https://arxiv.org/abs/2401.04884) Location: §4 Conclusion, p. 13; §§1.1, 1.3.2.

**Literature check.** Status for question 830, checked 5 October 2026: Checked 2026-10-05: reaffirmed in the 2026 synthesis.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://arxiv.org/abs/2402.02895) · [3](https://eldorado.tu-dortmund.de/bitstreams/f4fb281d-565a-41f3-9d84-d241936a4e10/download)


<a id="q831"></a>

## Q831. Exact information rate of noisy adaptive diagnosis

**Status:** Open · **Kind:** open problem (Problem 12) · **Collection** 9

For S uniform among k=⌊n^θ⌋ subsets of [n], 0<θ<1, an adaptive OR query is independently flipped with known probability 0<ρ<1/2. Determine the supremum liminf log₂(binomial(n, k))/T_n over strategies using at most T_n tests on every history and satisfying Pr(Ŝ≠S)→0. Queries may depend on all earlier results; the number of adaptive stages and decoding computation are unrestricted.

**Context.** Attribution: Explicitly posed as a new question in the 2026 second edition, building on noisy adaptive testing bounds.

**Source.** Matthew Aldridge; Oliver Johnson; Jonathan Scarlett. *Group Testing: An Information Theory Perspective, Second Edition*. 2026. [primary source](https://arxiv.org/abs/1902.06002v4) Location: Open Problem 12; §5.2.2; Scarlett 2019 model and bounds.

**Literature check.** Status for question 831, checked 5 October 2026: Checked 2026-10-05: Explicitly open in May 2026; later author publications yielded no resolution.

**Further links.** [1](https://arxiv.org/abs/1803.05099) · [2](https://arxiv.org/abs/2106.12193) · [3](https://www.comp.nus.edu.sg/~scarlett/publications.html)


<a id="q832"></a>

## Q832. Order-optimal noisy observations and decoding together

**Status:** Open · **Kind:** open problem · **Collection** 9

For every fixed θ∈(0, 1), ρ∈(0, 1/2), and k=Θ(n^θ), does a nonadaptive noisy OR-testing scheme achieve exact recovery with error o(1), using both T=O(k log n) tests and O(k log n) word-RAM decoding operations? Outcomes are independently flipped with probability ρ. Use the small-error uniform-support model, randomized design, and random access to tests/results; matrix construction time is separate.

**Context.** Attribution: Li–Mazumdar explicitly leave simultaneous optimal test and decoding scaling open; earlier splitting work initiated the target.

**Source.** Xiaxin Li; Arya Mazumdar. *Noisy Nonadaptive Group Testing with Binary Splitting: New Test Design and Improvement on Price-Scarlett-Tan’s Scheme*. 2025. [primary source](https://arxiv.org/abs/2410.14566v2) Location: Abstract; §2.1 model; final general-BSC limitation.

**Literature check.** Status for question 832, checked 5 October 2026: Checked 2026-10-05: reaffirmed in the 2026 synthesis.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://arxiv.org/abs/2311.08283)


<a id="q833"></a>

## Q833. Best acquisition constant with near-linear sparse decoding

**Status:** Open · **Kind:** open problem · **Collection** 9

For each fixed θ∈(0, 1), k=⌊n^θ⌋, noiseless nonadaptive OR tests and a uniform k-subset, what is the infimum achievable leading constant a(θ) in T=(a(θ)+o(1))k ln n when exact-recovery error tends to zero and decoding uses O(k log n) word operations? In particular, can a(θ)<(ln 2)^(−2) be achieved? Random-access design/outcome lookup is allowed; construction time is not decoder time.

**Context.** Attribution: The original paper explicitly asks how far its leading constant can be reduced.

**Source.** Hsin-Po Wang; Ryan Gabrys; Venkatesan Guruswami. *Quickly-Decodable Group Testing with Fewer Tests: Price-Scarlett and Cheraghchi-Nakos’s Nonadaptive Splitting with Explicit Scalars*. 2024. [primary source](https://arxiv.org/abs/2405.16370) Location: Abstract; §II Theorem 1.

**Literature check.** Status for question 833, checked 5 October 2026: Checked 2026-10-05: reaffirmed in the 2026 synthesis.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4)


<a id="q834"></a>

## Q834. Efficient certainty-preserving partial diagnosis at rate one

**Status:** Open · **Kind:** open problem · **Collection** 9

Let S be a uniform k=⌊n^θ⌋ subset, ln(2)/(1+ln(2))<θ<1. Under noiseless nonadaptive OR queries, can a polynomial-time design/decoder attain rate 1 and, with probability 1−o(1), output Ŝ⊂S with |Ŝ|≥(1−η)k whenever η=o(1) and η=Ω(k^(−λ(1/θ−1))) for fixed 0<λ<1/2? Rate is liminf log₂(binomial(n, k))/T. Preserve zero false positives on the successful event.

**Context.** Attribution: Explicit efficient-decoding question in the 2025 preprint, retained in the 2026 journal version.

**Source.** Daniel McMorrow; Jonathan Scarlett. *Optimal Non-Adaptive Group Testing with One-Sided Error Guarantees*. 2026. [primary source](https://arxiv.org/abs/2506.10374v4) Location: Theorem 2; Remark 2; §IV discussion.

**Literature check.** Status for question 834, checked 5 October 2026: Checked 2026-10-05: April 2026 v4 still uses exponential decoding and retains this question.


<a id="q835"></a>

## Q835. A universal lower bound for selectable-threshold sensors

**Status:** Open · **Kind:** open problem · **Collection** 9

Fix r≥2, θ∈(0, 1), k=⌊n^θ⌋, and uniform S. Nonadaptive test t selects Q_t⊂[n] and γ\_t∈{1,…, r}, returning 1{|Q_t∩S|≥γ\_t}. Does every design with exact-recovery success bounded away from zero require T≥(1−o(1))k ln k/B_r, where B_r=max_{u>0} −u ln(1−u^(r−1)e^(−u)/(r−1)!)? Remove the paper’s degree-regularity and small-pairwise-overlap assumptions; tests have no repeated item.

**Context.** Attribution: The authors explicitly conjecture extension of their converse to arbitrary designs.

**Source.** Trung-Khang Tran; Daniel McMorrow; Jonathan Scarlett. *Group Testing with Selectable Thresholds*. 2026. [primary source](https://arxiv.org/abs/2607.14448) Location: Theorems 5–6, Lemma 1 and §IV “Converse for arbitrary designs”.

**Literature check.** Status for question 835, checked 5 October 2026: Checked 2026-10-05: July 2026 paper retains this restriction; no subsequent unrestricted converse located.


<a id="q836"></a>

## Q836. Sharp query cost with bounded pool sizes

**Status:** Open · **Kind:** open problem · **Collection** 9

For fixed θ,β∈(0, 1), k=⌊n^θ⌋ and ρ=⌊(n/k)^β⌋, determine the sharp asymptotic number of tests needed for Pr(Ŝ≠S)→0 when every pool has at most ρ items. Close the remaining leading-constant gap at scale n/ρ; the constant-pool case β=0 is excluded.

**Context.** Attribution: Source-stated residual. Shared setup for questions 836, 837: Tests are noiseless OR queries on a uniformly random k-subset S⊂[n]. All pools are fixed before any result; arbitrary randomized designs and decoders are allowed.

**Source.** Nelvin Tan; Way Tan; Jonathan Scarlett. *Performance Bounds for Group Testing With Doubly-Regular Designs*. 2023. [primary source](https://arxiv.org/abs/2201.03745) Location: §VII; Theorem 3.

**Literature check.** Status for questions 836, 837, checked 5 October 2026: Checked 2026-10-05: no resolution located.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://nelvintan.github.io/publications.html) · [3](https://www.comp.nus.edu.sg/~scarlett/publications.html)


<a id="q837"></a>

## Q837. One-sided approximate recovery in the dense regime

**Status:** Open · **Kind:** open problem · **Collection** 9

For fixed p∈(0, 1), δ∈(0, 1) and k=⌊pn⌋, determine the optimal leading test density T/n for Pr(Ŝ⊂S and |S∖Ŝ|≤δk)→1. In particular, obtain matching achievable and converse bounds for this false-negatives-only criterion; sparse k=o(n) results do not settle it.

**Context.** Attribution: Source-stated residual. Shared setup for questions 836, 837: Tests are noiseless OR queries on a uniformly random k-subset S⊂[n]. All pools are fixed before any result; arbitrary randomized designs and decoders are allowed.

**Source.** Nelvin Tan; Way Tan; Jonathan Scarlett. *Performance Bounds for Group Testing With Doubly-Regular Designs*. 2023. [primary source](https://arxiv.org/abs/2201.03745) Location: §VII; Theorem 2.

**Literature check.** Status for questions 836, 837, checked 5 October 2026: Checked 2026-10-05: no resolution located.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://nelvintan.github.io/publications.html) · [3](https://www.comp.nus.edu.sg/~scarlett/publications.html)


<a id="q838"></a>

## Q838. Fast decoding with tightly limited evidence reuse

**Status:** Open · **Kind:** open problem · **Collection** 9

Fix θ,δ∈(0, 1), k=⌊n^θ⌋ and γ=⌊(ln n)^(1−δ)⌋. With noiseless nonadaptive OR tests and each item in at most γ pools, can exact recovery with error o(1) attain T=O(γk max{k, n/k}^(1/γ)) with o(n) word-RAM decoding operations? Require randomized for-each recovery and random-access outcomes/design lookup; design construction time is separate.

**Context.** Attribution: Explicit challenge to match the DD curve with sublinear decoding.

**Source.** Eric Price; Jonathan Scarlett; Nelvin Tan. *Fast Splitting Algorithms for Sparsity-Constrained and Noisy Group Testing*. 2023. [primary source](https://arxiv.org/abs/2106.00308) Location: §2.2 after equation (2.4), Figure 3 and Table 1.

**Literature check.** Status for question 838, checked 5 October 2026: Checked 2026-10-05: No later resolution located; current synthesis distinguishes test bounds from decoder cost.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://nelvintan.github.io/publications.html) · [3](https://www.comp.nus.edu.sg/~scarlett/publications.html)


<a id="q839"></a>

## Q839. Optimal information threshold with limited item participation

**Status:** Open · **Kind:** open problem · **Collection** 9

Fix 0<θ<1/2 and 0<δ<1; let k=⌊n^θ⌋ and Δ=⌊(ln n)^(1−δ)⌋. For a uniform k-subset and noiseless nonadaptive OR tests with each item in at most Δ pools, determine the exact recovery threshold at scale M=Δk(n/k)^(1/Δ). Is the best possible test count asymptotic to M/e, M, or an intermediate constant times M? Decoding is unrestricted; error must tend to zero.

**Context.** Attribution: The source leaves the θ<1/2 threshold open and expects DD to be suboptimal.

**Source.** Oliver Gebhard; Max Hahn-Klimroth; Olaf Parczyk; Manuel Penschuck; Maurice Rolvien; Jonathan Scarlett; Nelvin Tan. *Near-Optimal Sparsity-Constrained Group Testing: Improved Bounds and Algorithms*. 2022. [primary source](https://arxiv.org/abs/2004.11860v4) Location: §III equations (6), Theorems 3.1–3.4 and following open-problem paragraph.

**Literature check.** Status for question 839, checked 5 October 2026: Checked 2026-10-05: No later closure located; constant-degree error subtleties are avoided by diverging Δ.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://nelvintan.github.io/publications.html) · [3](https://www.comp.nus.edu.sg/~scarlett/publications.html)


<a id="q840"></a>

## Q840. Order-optimal inference for every monotone pooled sensor

**Status:** Open · **Kind:** conjecture (Conjecture 1) · **Collection** 9

Let d=⌊n^θ⌋, 0<θ<1, and known nonconstant nondecreasing f:{0,…, d}→[0, 1]. A pool containing j defectives returns Bernoulli(f(j)), conditionally independently. Put B~Bin(d−1, q), a(q)=E f(B+1), b(q)=E f(B), Δ(q)=(1−q)(a(q)−b(q)), and G(q)=min{a(q), 1−b(q)}(1−q)/(qΔ(q)²). For Z_χ~Hypergeom(n, d,χ), set h(f)=min_{1≤χ&lt;n, Var(f(Z_χ))>0} E[f(Z_χ)\](1−E[f(Z_χ)])/Var(f(Z_χ)). Is inf_{0&lt;q<1}G(q)=Θ(d h(f)) uniformly over such sensor families? This is Conjecture 1 with the fixed-error logarithm and numerical constant in Γ removed.

**Context.** Attribution: Explicit conjecture of Cheng–Jaggi–Zhou.

**Source.** Xiwei Cheng; Sidharth Jaggi; Qiaoqiao Zhou. *Generalized Group Testing*. 2023. [primary source](https://arxiv.org/abs/2102.10256v4) Location: Conjecture 1; equations (4)–(14), Definition 9 and equation (23), September 2022 v4.

**Literature check.** Status for question 840, checked 5 October 2026: Checked 2026-10-05: Retained in v4; bounded searches found no general proof or refutation.

**Further links.** [1](https://research-information.bris.ac.uk/en/publications/generalized-group-testing/)


<a id="q841"></a>

## Q841. When do pooled tests stop saving worst-case queries?

**Status:** Open · **Kind:** open problem · **Collection** 9

For integers 0&lt;d&lt;n with d≥n/3, must every adaptive noiseless OR-testing strategy that identifies every d-subset of [n] require at least n−1 tests in the worst case? Equivalently, is M(d, n)=n−1 throughout that range, where M is the minimum worst-case test count and d is known?

**Context.** Attribution: Hu–Hwang–Wang’s 1981 cutoff conjecture; equivalent reformulations are not separate entries.

**Source.** M. C. Hu; F. K. Hwang; Ju Kwei Wang. *A Boundary Problem for Group Testing*. 1981. [primary source](https://epubs.siam.org/doi/10.1137/0602011) Location: Original abstract; Leu 2008 §1.

**Literature check.** Status for question 841, checked 5 October 2026: Checked 2026-10-05: reaffirmed in the 2026 synthesis.

**Further links.** [1](https://arxiv.org/abs/1902.06002v4) · [2](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1A57EDF93A3B819AA210B0AD7D1C8CB5/S1446181108000175a.pdf/note_on_the_huhwangwang_conjecture_for_group_testing.pdf)


<a id="q842"></a>

## Q842. Do pairwise queries achieve the best nested Bayesian policy?

**Status:** Open · **Kind:** conjecture (Conjecture 2) · **Collection** 9

Let independent X_i~Bern(p_i), with p_i∈[1−1/√2,(3−√5)/2]. Does some ordering make GPTA minimize expected noiseless OR-test count among all nested strategies identifying every X_i? GPTA tests the first remaining pair; after a positive result it tests the member with smaller p_i, infers the partner if negative, otherwise returns that partner to its original position among unclassified items; a lone item is tested. A nested strategy, while a group is known to contain an unresolved defective, next tests a proper subset of that group.

**Context.** Attribution: Malinovsky 2020 Conjecture 2; the 2025 joint paper solves only the ordered Conjecture 1.

**Source.** Yaakov Malinovsky. *Conjectures on Optimal Nested Generalized Group Testing Algorithm*. 2020. [primary source](https://arxiv.org/abs/1805.01345v3) Location: Conjecture 2; 2025 follow-up Definition 2, Conjecture 2 and Comment 1(a).

**Literature check.** Status for question 842, checked 5 October 2026: Checked 2026-10-05: The 2025 follow-up, published in 2026, expressly leaves Conjecture 2 open.

**Further links.** [1](https://arxiv.org/abs/2506.15797) · [2](https://doi.org/10.1109/TIT.2025.3647637)


<a id="q843"></a>

## Q843. Exact eleven-query capacity for two hidden failures

**Status:** Open · **Kind:** open problem · **Collection** 9

What is the largest n for which M(K_n)≤11? An eleven-test strategy is known for n=328; maximality remains unproved, including whether n=329 or 330 can be resolved.

**Context.** Attribution: Author-posed 2026 question. Shared setup for questions 843, 844: Exactly two items are defective. Query Q returns |Q∩S|∈{0, 1, 2}; later queries can depend on earlier answers. Let M(G) be the optimal worst-case query count when S is an unknown edge of known graph G.

**Source.** Fedor Karpelevitch. *Certified exact bounds for adaptive quantitative group testing with two defectives*. 2026. [primary source](https://arxiv.org/abs/2609.38489v1) Location: §3.4; §5.

**Literature check.** Status for questions 843, 844, checked 5 October 2026: Checked 2026-10-05: still open in v1.


<a id="q844"></a>

## Q844. Does imbalance reduce two-failure query complexity?

**Status:** Open · **Kind:** conjecture (Conjecture 5.1) · **Collection** 9

For all n≥m>1 and integers k≥0, does M(K_{n, m})≤k imply M(K_{n+1, m−1})≤k? The prior information is exactly one defective in each of two disjoint sets; this is the source’s antidiagonal-transfer conjecture.

**Context.** Attribution: Author-posed 2026 question. Shared setup for questions 843, 844: Exactly two items are defective. Query Q returns |Q∩S|∈{0, 1, 2}; later queries can depend on earlier answers. Let M(G) be the optimal worst-case query count when S is an unknown edge of known graph G.

**Source.** Fedor Karpelevitch. *Certified exact bounds for adaptive quantitative group testing with two defectives*. 2026. [primary source](https://arxiv.org/abs/2609.38489v1) Location: Conjecture 5.1.

**Literature check.** Status for questions 843, 844, checked 5 October 2026: Checked 2026-10-05: still open in v1.

