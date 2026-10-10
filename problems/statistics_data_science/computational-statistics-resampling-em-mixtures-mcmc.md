# Computational Statistics: Resampling, EM, Mixtures & MCMC

3 problems: 3 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q510](computational-statistics-resampling-em-mixtures-mcmc.md#q510) | Sample-polynomial optimality under unknown-covariance mean shifts | Open |
| [Q511](computational-statistics-resampling-em-mixtures-mcmc.md#q511) | Nearly half-contaminated unknown-covariance mean-shift recovery | Open |
| [Q3995](computational-statistics-resampling-em-mixtures-mcmc.md#q3995) | For T>0 and integer m≥1, determine the sharp dependence of R_B^{x,y}(T,m)=inf_A… | Open |

<a id="q510"></a>

## Q510. Sample-polynomial optimality under unknown-covariance mean shifts

**Status:** Open · **Kind:** open problem · **Collection** 6

For fixed sufficiently small α>0, is the information-theoretic sample scale poly(d,2^(1/ε²)) attainable in time polynomial in sample size and d? Otherwise establish an information–computation separation under an explicit computational model or assumption.

**Context.** Attribution: Two explicit algorithmic frontiers in §1.2. Shared setup for questions 510, 511: Observe i.i.d. samples from (1−α)N(μ,Σ)+(α/m)Σ\_{j=1}^m N(μ\_j,Σ), with unknown Σ≻0, arbitrary component means and arbitrary finite m. The target is μ within ε√||Σ||op in Euclidean norm, with probability at least 2/3.

**Source.** Ilias Diakonikolas; Jingyi Gao; Giannis Iakovidis; Daniel M. Kane; Sihan Liu; Thanasis Pittas. *A Quasi-Polynomial Time Mean Estimator Under Mean-Shift Contamination with Unknown Covariance*. 2026. [primary source](https://proceedings.mlr.press/v336/diakonikolas26c.html) Location: Definition 1; Theorem 2; §1.2 first open problem.

**Literature check.** Status for questions 510, 511, checked 5 October 2026: Explicitly open in COLT 2026. No later resolution located; known-covariance results do not supply these unknown-covariance guarantees.

**Further links.** [1](https://raw.githubusercontent.com/mlresearch/v336/main/assets/diakonikolas26c/diakonikolas26c.pdf)


<a id="q511"></a>

## Q511. Nearly half-contaminated unknown-covariance mean-shift recovery

**Status:** Open · **Kind:** open problem · **Collection** 6

Can Theorem 2 extend to every fixed 0<α<1/2 with quasipolynomial dimension dependence and sample-polynomial runtime, retaining arbitrarily small target error? Constants and accuracy dependence may depend on 1/2−α.

**Context.** Attribution: Two explicit algorithmic frontiers in §1.2. Shared setup for questions 510, 511: Observe i.i.d. samples from (1−α)N(μ,Σ)+(α/m)Σ\_{j=1}^m N(μ\_j,Σ), with unknown Σ≻0, arbitrary component means and arbitrary finite m. The target is μ within ε√||Σ||op in Euclidean norm, with probability at least 2/3.

**Source.** Ilias Diakonikolas; Jingyi Gao; Giannis Iakovidis; Daniel M. Kane; Sihan Liu; Thanasis Pittas. *A Quasi-Polynomial Time Mean Estimator Under Mean-Shift Contamination with Unknown Covariance*. 2026. [primary source](https://proceedings.mlr.press/v336/diakonikolas26c.html) Location: §1.2 second open problem; Theorem 2; Proposition 12.

**Literature check.** Status for questions 510, 511, checked 5 October 2026: Explicitly open in COLT 2026. No later resolution located; known-covariance results do not supply these unknown-covariance guarantees.

**Further links.** [1](https://raw.githubusercontent.com/mlresearch/v336/main/assets/diakonikolas26c/diakonikolas26c.pdf)


<a id="q3995"></a>

## Q3995. For T>0 and integer m≥1, determine the sharp dependence of R_B^{x,y}(T,m)=inf_A…

**Status:** Open · **Kind:** open problem · **Collection** 40

For T>0 and integer m≥1, determine the sharp dependence of R_B^{x,y}(T,m)=inf_A sup_{(b,σ)∈F_T,0&lt;t_1<⋯&lt;t_m&lt;T}E[work_A] jointly on T,m,x,y, where A samples (X_{t_1},…,X_{t_m}) from that bridge.

**Context.** Fix integers d,k≥1, Γ>0 and 0<λ≤Λ. Let F_T be the nonempty class of coefficients b,σ whose components on [0,T]×R^d have bounded continuous time–space derivatives through total order k, including order zero, bounded by Γ; endpoint derivatives extend one-sided continuously; λI≤σσ^T≤ΛI. Let dX=b(t,X)dt+σ(t,X)dW, W standard d-dimensional Brownian motion. For x,y∈R^d, the bridge from x to y uses its positive continuous transition density. Algorithms receive T,x,y and the requested grid, know these bounds and query only scalar coefficient values. Exact-real arithmetic, comparisons, square roots, exponentials, logarithms, queries, independent scalar Gaussian/uniform draws, memory and output have fixed positive finite costs; π is available. Work includes all preprocessing, rejections and auxiliary computation. Admissible algorithms terminate almost surely and sample exactly for every allowed input. Doctoral context: Jikai Jin is a Stanford ICME PhD student, admitted in 2023, advised by Vasilis Syrgkanis. No completed dissertation is asserted. https://jkjin.com/ https://icme.stanford.edu/people/jikai-jin

**Source.** Jose Blanchet, Jikai Jin and Hao Liu. *Exact Simulation of Multivariate Diffusions and Bridges*. 2026. [primary source](https://arxiv.org/abs/2610.11330) Location: §§2,5–6.

**Literature check.** Status: Paper-origin. Fixed-horizon, fixed-endpoint dependence is Θ(m); the joint problem remains unresolved in the source. No matching resolution found on 10 October 2026.

**Further links.** [1](https://jkjin.com/) · [2](https://icme.stanford.edu/people/jikai-jin)

