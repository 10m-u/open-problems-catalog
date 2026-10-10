# Foundations, Zero-Sum & Matrix Games

5 problems: 5 open.

[All subjects](../README.md) · [Index by number](../INDEX.md)

| Q | Title | Status |
|---|---|---|
| [Q2597](foundations-zero-sum-matrix-games.md#q2597) | Random-first-player asymptotics | Open |
| [Q2598](foundations-zero-sum-matrix-games.md#q2598) | Four flipped-game responses | Open |
| [Q2700](foundations-zero-sum-matrix-games.md#q2700) | Normality of optimal-strategy density | Open |
| [Q3688](foundations-zero-sum-matrix-games.md#q3688) | State-blind continuous-time asymptotic value | Open |
| [Q3689](foundations-zero-sum-matrix-games.md#q3689) | Passing asymptotic existence to vanishing stages | Open |

<a id="q2597"></a>

## Q2597. Random-first-player asymptotics

**Status:** Open · **Kind:** conjecture (Conjecture 7.1) · **Collection** 26

Is p_n−2/3∼cn/2^n for some c>0 as n→∞?

**Context.** Origin for questions 2597, 2598: Authors’ §7 conjectures. Setup for questions 2597, 2598: Fix n≥3. Player I chooses A∈{H,T}^n; after seeing A, II chooses B≠A of length n. Independent fair coin tosses continue until A or B first appears. Normally that string’s owner wins; in the flipped game that owner loses. Let p_n be II’s winning probability when A is uniform and II responds optimally.

**Source.** Reed Phillips; A. J. Hildebrand. *The Number of Optimal Strategies in the Penney-Ante Game*. 2021. [primary source](https://math.colgate.edu/~integers/v27/v27.pdf) Location: §7, proposed strengthening (7.4) of Conjecture 7.1, p. 23.

**Literature check.** Status for questions 2597, 2598, checked 7 October 2026: No resolution located in the bounded 7 October 2026 search.

**Further links.** [1](https://arxiv.org/abs/2107.06952)


<a id="q2598"></a>

## Q2598. Four flipped-game responses

**Status:** Open · **Kind:** conjecture (Conjecture 7.3) · **Collection** 26

In the flipped game, for every A=a₁⋯a_n, must every optimal response B lie in {H^n,T^n,a₂⋯a_nH,a₂⋯a_nT}\\{A}?

**Context.** Origin for questions 2597, 2598: Authors’ §7 conjectures. Setup for questions 2597, 2598: Fix n≥3. Player I chooses A∈{H,T}^n; after seeing A, II chooses B≠A of length n. Independent fair coin tosses continue until A or B first appears. Normally that string’s owner wins; in the flipped game that owner loses. Let p_n be II’s winning probability when A is uniform and II responds optimally.

**Source.** Reed Phillips; A. J. Hildebrand. *The Number of Optimal Strategies in the Penney-Ante Game*. 2021. [primary source](https://math.colgate.edu/~integers/v27/v27.pdf) Location: §7, Conjecture 7.3, p. 25.

**Literature check.** Status for questions 2597, 2598, checked 7 October 2026: No resolution located in the bounded 7 October 2026 search.

**Results.**

- **Computational evidence** (B9: evidence): Holds for every string of length n ≤ 17 (exact computation); no proof. [Report](../../solutions/b9-2026-10-08/REPORT.md#problem-2-q2598-flipped-penney-ante-phillipshildebrand-conjecture-73).

**Further links.** [1](https://arxiv.org/abs/2107.06952)


<a id="q2700"></a>

## Q2700. Normality of optimal-strategy density

**Status:** Open · **Kind:** open problem · **Collection** 27

Let c_n count first-player strings maximizing the worst-case winning probability in the normal game, and α=lim_n c_n/2^n. Is α normal in base 2?

**Context.** Origin for question 2700: Authors’ §7 conjectures and arithmetic question. Setup for question 2700: Fix n≥3. Player I chooses A∈{H,T}^n; after seeing A, II chooses B≠A of length n. Independent fair coin tosses continue until A or B first appears; that string’s owner wins.

**Source.** Reed Phillips; A. J. Hildebrand. *The Number of Optimal Strategies in the Penney-Ante Game*. 2021. [primary source](https://math.colgate.edu/~integers/v27/v27.pdf) Location: §7, “Arithmetic nature of α”, p. 21; Theorem 2, p. 6.

**Literature check.** Status for question 2700, checked 7 October 2026: No resolution located in the bounded 7 October 2026 search.

**Further links.** [1](https://arxiv.org/abs/2107.06952)


<a id="q3688"></a>

## Q3688. State-blind continuous-time asymptotic value

**Status:** Open · **Kind:** open problem (Question 1) · **Collection** 37

If c is constant, must lim_{λ→0}v_{0,λ} exist?

**Context.** Origin: Novikov, Asymptotic Value in Zero-Sum Stochastic Games with Vanishing Stage Duration and Public Signals. Setup: A finite two-player zero-sum stochastic game has simultaneous actions, payoff g, transition kernel P and deterministic public state signal c(s). Only actions and signals are observed. For h,λ∈(0,1], replace P by (1−h)I+hP and use expected payoff Σₘ≥₁λh(1−λh)ᵐ⁻¹gₘ. Write v_{h,λ}(p) for its value at initial state law p and v_{0,λ}=lim_{h→0}v_{h,λ}, when defined.

**Source.** Ivan Novikov. *Asymptotic Value in Zero-Sum Stochastic Games with Vanishing Stage Duration and Public Signals*. 2024. [primary source](https://arxiv.org/abs/2403.07467v3) Location: Question 1, p.20.

**Literature check.** Status: Full current arXiv v3 (19 February 2026) inspected. The author still lists it as submitted; no subsequent resolution found.

**Further links.** [1](https://ivan-novikov98.github.io/)


<a id="q3689"></a>

## Q3689. Passing asymptotic existence to vanishing stages

**Status:** Open · **Kind:** open problem (Question 2) · **Collection** 37

For deterministic public signals, does existence of lim_{λ→0}v_{1,λ} imply existence of lim_{λ→0}v_{0,λ}?

**Context.** Origin: Novikov, Asymptotic Value in Zero-Sum Stochastic Games with Vanishing Stage Duration and Public Signals. Setup: A finite two-player zero-sum stochastic game has simultaneous actions, payoff g, transition kernel P and deterministic public state signal c(s). Only actions and signals are observed. For h,λ∈(0,1], replace P by (1−h)I+hP and use expected payoff Σₘ≥₁λh(1−λh)ᵐ⁻¹gₘ. Write v_{h,λ}(p) for its value at initial state law p and v_{0,λ}=lim_{h→0}v_{h,λ}, when defined.

**Source.** Ivan Novikov. *Asymptotic Value in Zero-Sum Stochastic Games with Vanishing Stage Duration and Public Signals*. 2024. [primary source](https://arxiv.org/abs/2403.07467v3) Location: Question 2, p.20.

**Literature check.** Status: Full current arXiv v3 (19 February 2026) inspected. The author still lists it as submitted; no subsequent resolution found.

**Further links.** [1](https://ivan-novikov98.github.io/)

