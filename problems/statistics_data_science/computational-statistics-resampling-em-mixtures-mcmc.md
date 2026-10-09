# Computational Statistics: Resampling, EM, Mixtures & MCMC

2 problems: 2 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q510](computational-statistics-resampling-em-mixtures-mcmc.md#q510) | Sample-polynomial optimality under unknown-covariance mean shifts | Open |
| [Q511](computational-statistics-resampling-em-mixtures-mcmc.md#q511) | Nearly half-contaminated unknown-covariance mean-shift recovery | Open |

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

