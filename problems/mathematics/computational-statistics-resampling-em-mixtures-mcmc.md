# Computational Statistics: Resampling, EM, Mixtures & MCMC

1 problems: 1 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q2795](computational-statistics-resampling-em-mixtures-mcmc.md#q2795) | Polylogarithmic exact Two-Choice sampling | Open |

<a id="q2795"></a>

## Q2795. Polylogarithmic exact Two-Choice sampling

**Status:** Open · **Kind:** open problem · **Collection** 28

Can the exact joint law of (K,X_0,…,X_K) be sampled in expected time polylog(n)?

**Context.** Origin for question 2795: Authors’ Two-Choice simulation question. Setup for question 2795: Place n balls sequentially into n initially empty bins. Each ball independently samples two uniform bins with replacement and joins a least-loaded sampled bin, with random tie-breaking. Let X_j count bins of final load j and K=max{j:X_j>0}. Use an ideal real-RAM with unit-cost arithmetic, comparisons, truncation, exponentials, logarithms, trigonometric operations and independent Uniform(0,1) draws.

**Source.** Luc Devroye; Dimitrios Los. *An asymptotically optimal algorithm for generating bin cardinalities*. 2025. [primary source](https://arxiv.org/abs/2404.07011) Location: §5, p. 154; RAM model p. 147.

**Literature check.** Status for question 2795, checked 7 October 2026: No resolution located in bounded searches through 7 October 2026.

**Further links.** [1](https://doi.org/10.1016/j.matcom.2024.08.034) · [2](https://luc.devroye.org/Devroye%2Blos-BinCardinalities-MCS-2024.pdf)

