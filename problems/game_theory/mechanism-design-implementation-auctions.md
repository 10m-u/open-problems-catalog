# Mechanism Design, Implementation & Auctions

7 problems: 7 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q111](mechanism-design-implementation-auctions.md#q111) | Let X=[0,1]², c=(1/3,1/3), and let U be the set of all convex nonnegative u on X… | Open |
| [Q112](mechanism-design-implementation-auctions.md#q112) | With trader values uniform on [0,1]³, market-maker belief c=(1/2,1/2,1/2), no ad… | Open |
| [Q225](mechanism-design-implementation-auctions.md#q225) | For independent v, θ ∼ Uniform[0,1], is a single posted-price, fully revealing e… | Open |
| [Q226](mechanism-design-implementation-auctions.md#q226) | For v ∼ Uniform[c,1], 0 ≤ c < 1, and θ drawn from an equal mixture of Beta(8,30)… | Open |
| [Q591](mechanism-design-implementation-auctions.md#q591) | Exact truthfulness versus regret with noisy strategic features | Open |
| [Q1694](mechanism-design-implementation-auctions.md#q1694) | Straight-jacket optimality beyond six goods | Open |
| [Q1695](mechanism-design-implementation-auctions.md#q1695) | Optimal two-buyer two-good auction | Open |

<a id="q111"></a>

## Q111. Let X=[0,1]², c=(1/3,1/3), and let U be the set of all convex nonnegative u on X…

**Status:** Open · **Kind:** open problem · **Collection** 2

Let X=[0,1]², c=(1/3,1/3), and let U be the set of all convex nonnegative u on X with u(c)=0 and ||∇u||∞≤1 almost everywhere. Is sup_(u∈U) ∫\_X[∇u(x)·(x−c)−u(x)]dx equal to 2(−1350−2903√2+32√(58234+40462√2))/35721? The proposed seven-option menu attains this value, about 0.30333726.

**Context.** Origin: Original conjectured mechanism with Michael J. Curry and David Parkes, derived using differentiable economics; thesis does not claim a full optimality proof for this asymmetric case. Structural form of the author’s conjecturally optimal three-good mechanism with Michael Curry and David Parkes. Restates only the proposed trade-vector support, not guessed numerical prices.

**Source.** Zhou Fan. *Designing for Decentralized Finance through Differentiable Optimization, and a Study of Bayesian Optimization*. Harvard University, 2025. Advisor(s): David C. Parkes. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/4d7a995d-3ac8-4da5-b6c4-440414326c2d/content) · [record](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2026-01/ParkesJan26.pdf) Location: §4.5.3 pp.128–129, Table 4.3; §C.5; exact profit §C.7.1 p.221; model §4.2 pp.106–109. Status evidence, checked 5 October 2026: The WINE 2025 proceedings version, published 1 May 2026, Appendix M.2 and Appendix N, still calls the mechanism conjecturally optimal and proves only a 96.28% guarantee. Later targeted searches found no exact certificate.

**Further links.** [1](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2025-12/marketmakers.pdf) · [2](https://link.springer.com/chapter/10.1007/978-3-032-18660-7_8)


<a id="q112"></a>

## Q112. With trader values uniform on [0,1]³, market-maker belief c=(1/2,1/2,1/2), no ad…

**Status:** Open · **Kind:** open problem · **Collection** 2

With trader values uniform on [0,1]³, market-maker belief c=(1/2,1/2,1/2), no adverse selection, and trade quantities in [−1,1]³, does an optimal truthful, individually rational mechanism admit a menu using only 0, the six signed unit vectors, and the eight vectors (±1,±1,±1)? Impose the thesis’s no-trade normalization u(c)=0. This excludes trades of exactly two goods.

**Context.** Origin: Original conjectured mechanism with Michael J. Curry and David Parkes, derived using differentiable economics; thesis does not claim a full optimality proof for this asymmetric case. Structural form of the author’s conjecturally optimal three-good mechanism with Michael Curry and David Parkes. Restates only the proposed trade-vector support, not guessed numerical prices.

**Source.** Zhou Fan. *Designing for Decentralized Finance through Differentiable Optimization, and a Study of Bayesian Optimization*. Harvard University, 2025. Advisor(s): David C. Parkes. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/4d7a995d-3ac8-4da5-b6c4-440414326c2d/content) · [record](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2026-01/ParkesJan26.pdf) Location: §4.5.3 pp.129–130, Figure 4.8; model §4.2 pp.106–109. Status evidence, checked 5 October 2026: The May 2026 WINE proceedings version repeats this structure under Further Conjectures (Appendix N) without an exact optimality certificate. No later proof located.

**Further links.** [1](https://link.springer.com/chapter/10.1007/978-3-032-18660-7_8) · [2](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2025-12/marketmakers.pdf)


<a id="q225"></a>

## Q225. For independent v, θ ∼ Uniform[0,1], is a single posted-price, fully revealing e…

**Status:** Open · **Kind:** open problem · **Collection** 3

For independent v, θ ∼ Uniform[0,1], is a single posted-price, fully revealing experiment revenue-optimal among all information menus?

**Context.** Origin: New optimal-menu conjectures from joint work with Yanchen Jiang and David Parkes, published at NeurIPS 2023. Shared setup for questions 225, 226: A seller observes a binary state. A buyer privately knows a payoff v and belief θ = Pr(state 1), earns v for choosing the matching binary action, and may buy a priced stochastic experiment before acting. Menus must be incentive-compatible and individually rational relative to buying no information. Payoffs and beliefs are independent.

**Source.** Sai Srivatsa Ravindranath. *Differentiable Economics: Auctions, Data Markets, and Matching Markets*. Harvard University, 2025. Advisor(s): David C. Parkes. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/ca199353-dfc8-489e-bfbe-ba60edcf0bd8/content) · [record](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2026-01/ParkesJan26.pdf) Location: §4.5.2, Setting E, pp. 113–114 (PDF pp. 132–133); model §4.2, pp. 93–95.

**Further links.** [1](https://proceedings.neurips.cc/paper_files/paper/2023/file/1577ea3eaf8dacb99f64e4496c3ecddf-Paper-Conference.pdf) · [2](https://dash.harvard.edu/server/api/core/bitstreams/f0f0ab67-aa12-4c61-946a-08eead219189/content)


<a id="q226"></a>

## Q226. For v ∼ Uniform[c,1], 0 ≤ c < 1, and θ drawn from an equal mixture of Beta(8,30)…

**Status:** Open · **Kind:** open problem · **Collection** 3

For v ∼ Uniform[c,1], 0 ≤ c < 1, and θ drawn from an equal mixture of Beta(8,30) and Beta(60,30), can an optimal menu always use at most two paid experiments, one fully revealing? Determine when a partially informative option is needed.

**Context.** Origin: New optimal-menu conjectures from joint work with Yanchen Jiang and David Parkes, published at NeurIPS 2023. Shared setup for questions 225, 226: A seller observes a binary state. A buyer privately knows a payoff v and belief θ = Pr(state 1), earns v for choosing the matching binary action, and may buy a priced stochastic experiment before acting. Menus must be incentive-compatible and individually rational relative to buying no information. Payoffs and beliefs are independent.

**Source.** Sai Srivatsa Ravindranath. *Differentiable Economics: Auctions, Data Markets, and Matching Markets*. Harvard University, 2025. Advisor(s): David C. Parkes. [primary source](https://dash.harvard.edu/server/api/core/bitstreams/ca199353-dfc8-489e-bfbe-ba60edcf0bd8/content) · [record](https://parkes.seas.harvard.edu/sites/g/files/omnuum8711/files/2026-01/ParkesJan26.pdf) Location: §4.5.2, Setting F and Figure 4.4, pp. 113–114 (PDF pp. 132–133).

**Further links.** [1](https://proceedings.neurips.cc/paper_files/paper/2023/file/1577ea3eaf8dacb99f64e4496c3ecddf-Paper-Conference.pdf) · [2](https://dash.harvard.edu/server/api/core/bitstreams/f0f0ab67-aa12-4c61-946a-08eead219189/content)


<a id="q591"></a>

## Q591. Exact truthfulness versus regret with noisy strategic features

**Status:** Open · **Kind:** open problem · **Collection** 6

Can a no-payment algorithm achieve o(T) worst-case regret while truthful reporting is an exact Nash equilibrium in the strategic linear contextual-bandit model with unknown θ\* and noisy rewards? K persistent arms privately see true unit-bounded contexts x\*\_{t,i}, report contexts strategically, and maximize expected total selections. The learner observes only reports and the selected reward ⟨θ\*,x\*\_{t,i_t}⟩+η\_t, with zero-mean sub-Gaussian noise. Nature may choose contexts adversarially; reward differences are bounded and the nonzero optimality gap is constant. The conjecture rules out exact truthfulness plus no regret, not approximate Nash truthfulness.

**Context.** Attribution: Explicit impossibility conjecture; the source gives exact truthfulness only when θ\* is known and rewards are noiseless.

**Source.** Thomas Kleine Buening; Aadirupa Saha; Christos Dimitrakakis; Haifeng Xu. *Strategic Linear Contextual Bandits*. 2024. [primary source](https://arxiv.org/abs/2406.00551) Location: §3.3 final paragraph; Appendix A final conjecture; §3 protocol and regularity assumptions.

**Literature check.** Status for question 591, checked 5 October 2026: Current v2 retains the conjecture. COBRA (2025/ICLR 2026 workshop), Theorem 2, provides approximate O-tilde(d√T)-Nash truthfulness rather than exact Nash truthfulness; its all-equilibrium regret additionally assumes confidence-bound relations under joint manipulation. MESHA (July 2026) concerns best-arm identification with a different arm objective. Neither resolves the conjecture; bounded further searches found no proof or counterexample.

**Further links.** [1](https://arxiv.org/html/2505.23720) · [2](https://openreview.net/pdf?id=YZ3CoUoZ2S) · [3](https://arxiv.org/abs/2607.14706)


<a id="q1694"></a>

## Q1694. Straight-jacket optimality beyond six goods

**Status:** Open · **Kind:** open problem · **Collection** 17

For one buyer and m≥7 items, is SJA well-defined and optimal? It offers every r-item bundle at price p_r, recursively chosen so that Vol{x∈[0,1]^r: Σ\_{j∈J}x_j&lt;p_|J| for every nonempty J⊆[r]}=1−r/(m+1), for r=1,…,m. The buyer chooses a utility-maximizing bundle or nothing.

**Context.** Origin for questions 1694, 1695: SJA: Giannakopoulos–Koutsoupias (2014; journal 2018). Two-buyer target: thesis §7(1). Setup for questions 1694, 1695: Values are independent Uniform[0,1], additive across items; bidders are risk-neutral with quasilinear utility. Optimize expected seller revenue over feasible randomized mechanisms. Truthfulness must maximize expected utility over the mechanism’s randomness for every report of the other bidders; truthful expected utility must be nonnegative at every valuation profile.

**Source.** Yiannis Giannakopoulos. *Duality Theory for Optimal Mechanism Design*. 2015. Advisor(s): Elias Koutsoupias. [primary source](https://yiannisgiannakopoulos.com/files/papers/DPhil_thesis.pdf) Location: Definition 4.1 and following conjecture, pp. 52–53.

**Literature check.** Status for questions 1694, 1695, checked 6 October 2026: no exact solution found; general SJA global optimality remains conjectural despite local-optimality and numerical results.

**Further links.** [1](https://ora.ox.ac.uk/objects/uuid:90e1fdec-8803-4306-8985-5106c457f34d) · [2](https://arxiv.org/abs/1404.2329) · [3](https://www3.math.tu-berlin.de/disco/research/projects/tropical-mechanism-design/)


<a id="q1695"></a>

## Q1695. Optimal two-buyer two-good auction

**Status:** Open · **Kind:** open problem · **Collection** 17

For two buyers and two items, determine the maximum expected revenue and a mechanism attaining it.

**Context.** Origin for questions 1694, 1695: SJA: Giannakopoulos–Koutsoupias (2014; journal 2018). Two-buyer target: thesis §7(1). Setup for questions 1694, 1695: Values are independent Uniform[0,1], additive across items; bidders are risk-neutral with quasilinear utility. Optimize expected seller revenue over feasible randomized mechanisms. Truthfulness must maximize expected utility over the mechanism’s randomness for every report of the other bidders; truthful expected utility must be nonnegative at every valuation profile.

**Source.** Yiannis Giannakopoulos. *Duality Theory for Optimal Mechanism Design*. 2015. Advisor(s): Elias Koutsoupias. [primary source](https://yiannisgiannakopoulos.com/files/papers/DPhil_thesis.pdf) Location: §7(1), p. 125.

**Literature check.** Status for questions 1694, 1695, checked 6 October 2026: no exact solution found; general SJA global optimality remains conjectural despite local-optimality and numerical results.

**Further links.** [1](https://ora.ox.ac.uk/objects/uuid:90e1fdec-8803-4306-8985-5106c457f34d) · [2](https://arxiv.org/abs/1404.2329) · [3](https://www3.math.tu-berlin.de/disco/research/projects/tropical-mechanism-design/)

