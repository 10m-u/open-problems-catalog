# Control, Estimation & Filtering

1 problems: 1 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q2786](control-estimation-filtering.md#q2786) | Continuity in POMDP stage duration | Open |

<a id="q2786"></a>

## Q2786. Continuity in POMDP stage duration

**Status:** Open · **Kind:** open problem · **Collection** 28

Must h↦V(h) be continuous throughout (0,1)?

**Context.** Origin for question 2786: Post-thesis question; Novikov’s Paris Dauphine PhD (2025) advisor was Guillaume Vigeral. Setup for question 2786: Fix finite state, action and signal sets Ω,A,S, deterministic observation f:Ω→S, payoff g:Ω×A→R unobserved by the decision maker, transition kernel P, and initial law p. Replace P by P_h=hP+(1−h)I. With behavioural strategies based on observed signals/actions, set V(h)=lim_{λ↓0}sup_σ E_σ[∑\_{i≥1}λh(1−λh)^{i−1}g(ω\_i,a_i)].

**Source.** Ivan Novikov. *Strategies in POMDPs with Stage Duration*. 2026. [primary source](https://arxiv.org/abs/2603.16055) Location: §5.2, Remark 7, p. 14.

**Literature check.** Status for question 2786, checked 7 October 2026: June 2026 v2 proves left-continuity and retains full interior continuity as open.

**Further links.** [1](https://arxiv.org/abs/2603.16055v2) · [2](https://ivan-novikov98.github.io/)

