# Bayesian Inference

4 problems: 4 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q641](bayesian-inference.md#q641) | Sharp Bayesian prediction overhead | Open |
| [Q642](bayesian-inference.md#q642) | Bayesian regret under misspecification | Open |
| [Q643](bayesian-inference.md#q643) | Asymptotic predictive minimax equality | Open |
| [Q949](bayesian-inference.md#q949) | Can one convex PAC-Bayes bound attain the pointwise ideal in expectation? | Open |

<a id="q641"></a>

## Q641. Sharp Bayesian prediction overhead

**Status:** Open · **Kind:** open problem · **Collection** 7

Is Θ(log n) the sharp universal overhead g(n) such that every C,ρ admit one discrete mixture ν over C with L_n(μ,ν)≤L_n(μ,ρ)+g(n) for all μ∈C,n? Known upper:8log₂n+O(loglog n); lower: merely divergent.

**Context.** Attribution: Explicit residuals in §§3,5–7. Shared setup for questions 641, 642, 643: For finite X, let P be laws on X^N, L_n(μ,ρ)=E_μ log₂[μ(X₁:n)/ρ(X₁:n)], and L̄=limsup_n L_n/n. Bayesian predictors: barycenters ρ\_W=∫μdW with W carried by a measurable subset of C⊆P; with cylinder-evaluation measurability. Let C\* contain these priors. For regret, require μ(w),ρ(w)>0 for every μ∈C and finite w; define R(C,ρ)=sup_{λ∈P,μ∈C}limsup_n[L_n(λ,ρ)−L_n(λ,μ)]/n and U_C=inf_ρ R(C,ρ).

**Source.** Daniil Ryabko. *On Asymptotic and Finite-Time Optimality of Bayesian Predictors*. 2019. [primary source](https://jmlr.org/papers/volume20/18-512/18-512.pdf) Location: §3, Theorems 1 and 3; §7, p. 22.

**Literature check.** Status for questions 641, 642, 643, checked 5 October 2026: Checked 5 October 2026: no resolution located; medium confidence.

**Further links.** [1](https://arxiv.org/abs/1812.08292) · [2](https://jmlr.org/papers/v20/18-512.html)


<a id="q642"></a>

## Q642. Bayesian regret under misspecification

**Status:** Open · **Kind:** open problem · **Collection** 7

Characterize C for which a Bayesian predictor attains U_C, especially when U_C=0 is attainable without the mixture restriction.

**Context.** Attribution: Explicit residuals in §§3,5–7. Shared setup for questions 641, 642, 643: For finite X, let P be laws on X^N, L_n(μ,ρ)=E_μ log₂[μ(X₁:n)/ρ(X₁:n)], and L̄=limsup_n L_n/n. Bayesian predictors: barycenters ρ\_W=∫μdW with W carried by a measurable subset of C⊆P; with cylinder-evaluation measurability. Let C\* contain these priors. For regret, require μ(w),ρ(w)>0 for every μ∈C and finite w; define R(C,ρ)=sup_{λ∈P,μ∈C}limsup_n[L_n(λ,ρ)−L_n(λ,μ)]/n and U_C=inf_ρ R(C,ρ).

**Source.** Daniil Ryabko. *On Asymptotic and Finite-Time Optimality of Bayesian Predictors*. 2019. [primary source](https://jmlr.org/papers/volume20/18-512/18-512.pdf) Location: §2.2; §6, Theorem 6 and p. 21; §7, p. 22.

**Literature check.** Status for questions 641, 642, 643, checked 5 October 2026: Checked 5 October 2026: no resolution located; medium confidence.

**Further links.** [1](https://arxiv.org/abs/1812.08292) · [2](https://jmlr.org/papers/v20/18-512.html)


<a id="q643"></a>

## Q643. Asymptotic predictive minimax equality

**Status:** Open · **Kind:** open problem · **Collection** 7

Must inf_ρ sup_{W∈C\*}E_W L̄(μ,ρ)=sup_{W∈C\*}inf_ρ E_W L̄(μ,ρ) hold for every C? An upper-value minimizer exists.

**Context.** Attribution: Explicit residuals in §§3,5–7. Shared setup for questions 641, 642, 643: For finite X, let P be laws on X^N, L_n(μ,ρ)=E_μ log₂[μ(X₁:n)/ρ(X₁:n)], and L̄=limsup_n L_n/n. Bayesian predictors: barycenters ρ\_W=∫μdW with W carried by a measurable subset of C⊆P; with cylinder-evaluation measurability. Let C\* contain these priors. For regret, require μ(w),ρ(w)>0 for every μ∈C and finite w; define R(C,ρ)=sup_{λ∈P,μ∈C}limsup_n[L_n(λ,ρ)−L_n(λ,μ)]/n and U_C=inf_ρ R(C,ρ).

**Source.** Daniil Ryabko. *On Asymptotic and Finite-Time Optimality of Bayesian Predictors*. 2019. [primary source](https://jmlr.org/papers/volume20/18-512/18-512.pdf) Location: §5.1, equations(32)–(33), pp. 16–17.

**Literature check.** Status for questions 641, 642, 643, checked 5 October 2026: Checked 5 October 2026: no resolution located; medium confidence.

**Further links.** [1](https://arxiv.org/abs/1812.08292) · [2](https://jmlr.org/papers/v20/18-512.html)


<a id="q949"></a>

## Q949. Can one convex PAC-Bayes bound attain the pointwise ideal in expectation?

**Status:** Open · **Kind:** open problem · **Collection** 10

Let S∼D^N, ℓ∈[0, 1], fixed prior P and posterior Q(S); put q=E_Q R_S, K=KL(Q||P). For proper convex l.s.c. Δ:[0, 1]²→R∪{∞}, set I_Δ=sup_{r∈[0, 1]} E_{B∼Bin(N, r)}e^{NΔ(B/N, r)} and b_Δ=sup{p∈[0, 1]: NΔ(q, p)≤K+log(I_Δ/δ)}, sup∅=1. For each setup and N≥1, δ∈(0, 1), does some Δ fixed before S attain E b_Δ=E sup{p∈[0, 1]: Nkl(q, p)≤K+log(1/δ)}? If not, how close can it get?

**Context.** Attribution: Open Problem 1; related motivation: Langford 2002 Problem 6.1.2.

**Source.** Andrew Y. K. Foong; Wessel P. Bruinsma; David R. Burt; Richard E. Turner. *How Tight Can PAC-Bayes be in the Small Data Regime?*. 2021. [primary source](https://papers.nips.cc/paper/2021/hash/214cfbe603b7f9f9bc005d5f53f7a1d3-Abstract.html) Location: Theorem 3; Corollary 3; §5.

**Literature check.** Status for question 949, checked 5 October 2026: No resolution located in bounded current searches.

**Further links.** [1](https://papers.nips.cc/paper_files/paper/2021/file/214cfbe603b7f9f9bc005d5f53f7a1d3-Supplemental.pdf) · [2](https://andrewfoongyk.github.io/) · [3](https://hunch.net/~jl/projects/prediction_bounds/thesis/thesis.pdf)

