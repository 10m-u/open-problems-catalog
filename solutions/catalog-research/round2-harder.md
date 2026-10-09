# Round 2: harder targets from the catalog

Round 2 targeted problems one level harder than the [quick closures](quick-closures.md). The literature was checked before committing proof effort; for Gu's inequality the check came late, after a proof was already in hand (§2).

| Thesis statement | Outcome |
|---|---|
| Martínez (2013), Conjecture 6.105 | **proved** (local, short; in [quick closures §3](quick-closures.md)) |
| Gu (2023), Conjecture 7.6 | **proved in the literature** (Marwaha 2023). An independent short proof is given below |
| Hopkins (2018), Conjectures 2.3.4 and 2.3.5 | **proved in the literature** (Klivans–Liscio 2020/2022) |
| Noel (2016) 5.22–5.24 and Morrison (2017) 7.1–7.3 on m(Q_d, r) | **partial**: exact for r = 4 at infinitely many d (Noel 2026). The 5.22/7.1 limit for r = 4 is **1/8**, derived here |
| Hopkins (2018), Conjecture 2.3.1 (odd-chip inversion bound) | open. **Exhaustively verified for N = 11** (6,520,201 states), beyond the published n ≤ 9. New OEIS A282901 term a(5) = 819 |
| Golowich (2025), Problem 13.4.2 (extragradient on ratio games) | open. For 2×2 games: Hamiltonian reduction, and convergence follows if closed orbits are convex. Convexity holds in all 19,940 tested games (§4) |
| Schwarze (2019), Conjecture 1 (diagonal matrices maximize log-minor variance) | open. Adversarial search found no counterexample for (n,k) = (4,2), (5,2), (6,3) |

## 1. Martínez 6.105

The proof is in [quick closures §3](quick-closures.md). For odd k, |cot(πk/2n)| attains its maximum exactly at k ≡ ±1 (mod 2n). This pins the Galois stabilizer of −cot(π/2n)cot(π/2m) to {±1}, which gives both the stated degree and the stated product.

## 2. Gu's arctanh inequality: an independent proof

Yuzhou Gu (MIT 2023), Conjecture 7.6 (`cfbae250ab2ad0836965`), is the inequality behind the r = 4 case of weak-recovery impossibility for the hypergraph SBM. Marwaha had already proved it ([arXiv:2305.18348](https://arxiv.org/abs/2305.18348)), as the published [Gu–Polyanskiy COLT 2023](https://arxiv.org/abs/2303.14689) Lemma 17 records. The thesis text predates that proof. Below is a different, short proof of the same per-sign-pattern inequality.

**Reduction.** Put θᵢ = tanh aᵢ, C = ∏cosh aᵢ, μ = λ/((1−λ)C), and c_x = a₁ + x₂a₂ + x₃a₃. By the tanh addition law, s_x = sinh(c_x)/C and 1 + q_x = cosh(c_x)/C. With g_μ(c) = log((1+μe^{c})/(1+μe^{−c})), the conjecture is

\[
\sum_{x_2,x_3}\sinh(c_x)\,\big[g_\mu(c_x)-2\lambda c_x\big]\le0 ,
\]

and at λ = 1 it is an identity. It suffices to show g_μ(c) ≤ 2λc for every c > 0; this per-pattern form is also Marwaha's Theorem 1. Write μ = e^{s}. Then g_μ(c)/(2c) = A_c(s), the average of the logistic function σ over [s−c, s+c], and λ = σ(s + log C).

- **Monotonicity.** T(s) = logit(A_c(s)) − s is non-increasing. Indeed T′(s) + 1 = E[σ(1−σ)]/(Eσ) ≤ 1, which is equivalent to E[σ]² ≤ E[σ²] (Jensen, uniform window).
- **Limit.** As s → −∞, T(s) → log(sinh c / c). Hence A_c(s) ≤ σ(s + log(sinh c / c)).
- **Cosh bound.** sinh(u)/u is increasing and |c_x| ≤ A := Σaᵢ. Convexity of log cosh gives C ≥ cosh³(A/3). Finally, sinh(3x)/(3x) ≤ cosh³x: with t = tanh x this reads t(3+t²) ≤ 3·artanh t = 3t + t³ + (3/5)t⁵ + …, which holds term by term. So log(sinh|c_x|/|c_x|) ≤ log C, and therefore A ≤ λ. ∎

With k = r−1 children, the last step needs sinh(kx)/(kx) ≤ coshᵏx. That is t ≤ artanh t for k = 2 (Gu's r = 3 lemma), holds for k = 3, and fails for k = 4 (t(1+t²) > artanh t for small t). This matches Gu's report that the SKL contraction fails for r ≥ 5.

## 3. Literature closures and one derived limit

- **Hopkins 2.3.4 and 2.3.5** (`5a4088dafbe203b392f7`, `feffed9528f3215eda70`): the self-loop line sorts N ≡ 3 (mod 4), and the r-parallel-edge line weakly sorts N ≡ 0 (mod 2r). Both are proved by [Klivans–Liscio, *Confluence in labeled chip-firing*](https://arxiv.org/abs/2006.12324) (§3.2 and §3.5).
- **Hypercube bootstrap percolation.** [Noel (April 2026)](https://arxiv.org/abs/2604.15534) proves m(Q_d; 4) = d(d²+3d+14)/24 + 1 for infinitely many d, and within O(d) of that value for all d. The Morrison–Noel r = 4 lower bound 8 + ⌈[C(d−2,3) + 4C(d−3,2) + 12(d−4)]/4⌉ simplifies exactly to d(d²+3d+14)/24 + 1. Lower bound plus O(d) upper bound give

\[
\frac{m(Q_d,4)-d^3/24}{d^2}\longrightarrow\frac18 ,
\]

answering Noel Q5.22 / Morrison Q7.1 for r = 4. Problems 5.23/7.2 (every d) and Questions 5.24/7.3 (all r ≥ 4) remain partial.

## 4. Extragradient on 2×2 ratio games (Golowich Problem 13.4.2)

**Problem.** Does extragradient with a constant step have last-iterate convergence on von Neumann ratio games V(x,y) = ⟨x,Ry⟩/⟨x,Sy⟩ with ⟨x,Sy⟩ ≥ ζ > 0? (`c9757a96a30026468248`; thesis text §13.4.)

**Structural fact (2×2).** Write x = (p, 1−p), y = (q, 1−q), and V = N/D with N, D bilinear. Then D²V_p =: W(q) depends only on q, and D²V_q =: V̂(p) depends only on p, because every p-term cancels in N_pD − ND_p. Hence the gradient descent–ascent field

(ṗ, q̇) = (−V_p, V_q) = D^{−2}·(−W(q), V̂(p))

is a positive time change of the Hamiltonian field of H(p,q) = ∫V̂ dp + ∫W dq. Interior orbits are closed, as in bilinear games, and the continuous dynamics have no limit cycles. V̂ and W are quadratic, so H is a separable cubic rather than a quadratic.

**Extragradient drift.** Extragradient's modified equation is ż = G + (η/2)·DG·G. Because ∇H·G ≡ 0,

\[
\frac{dH}{dt}=-\frac{\eta}{2}\,\frac{\hat V'(p)\,W(q)^2+W'(q)\,\hat V(p)^2}{D^4}.
\]

For small η, convergence is governed by the orbit average of this drift. By Green's theorem the average is ∬_{inside} (2/D³)[V̂′W′D − W′V̂D_p − V̂′WD_q] dA.

At the center (a Nash equilibrium) the drift is stabilizing. This agrees with a general linear-algebra fact: the symmetric part of DF on the tangent space is PSD at any interior Nash equilibrium, so extragradient is never locally repelled. A counterexample to Problem 13.4.2 would need an orbit whose averaged drift turns destabilizing.

**Geometric form.** With G = D^{−2}J∇H, the drift numerator V̂′W² + W′V̂² equals (J∇H)^⊤∇²H(J∇H) = κ|∇H|³, where κ is the curvature of the level curve. In arclength s, the per-orbit change is therefore

\[
\Delta H \approx -\frac{\eta}{2}\oint \frac{|\nabla H|^2}{D^2}\,\kappa\,ds .
\]

So if every closed orbit inside the square is **convex**, the drift is stabilizing at every point of every orbit. Extragradient with small constant η would then converge from every start inside the largest closed orbit (modulo the standard averaging justification).

**Evidence (no proof).** Controls: [drift scan](ratio_game_drift_scan.py), [orbit convexity](ratio_game_orbit_convexity.py), [symbolic factorisation](ratio_game_symbolic.py) → [results](ratio-game-results.txt).
- Across 66,199 random 2×2 ratio games with an interior equilibrium, the orbit-averaged drift I(h) (via Green's theorem, I(h) = ∬_{H≤h} 2K/D³ with K = −(n₃D − d₃N)·Q) never changed sign before orbits reached the boundary. Every interior equilibrium found was a center.
- In 19,940 games, the curvature numerator was non-negative on the entire region of closed orbits, so every closed orbit was convex.
- This is **not** explained by separate convexity of A or B, which fails on the swept range in about 4% of games. Nor is it explained by K having a fixed sign, since K takes the destabilizing sign on up to 45% of the square.
- Direct extragradient runs on 8,000 random and 12,000 near-bilinear game/start pairs converged once η ≤ 0.01. The non-convergence flagged at η = 0.05 disappears at smaller η: it was a step-size artifact.

**Conjecture (2×2 convexity), proved in [round 3](round3.md).** For every 2×2 ratio game with an interior equilibrium, the level sets of H that close inside [0,1]² are convex. With a rigorous averaging argument and a treatment of boundary-touching orbits, this would answer Problem 13.4.2 affirmatively for 2×2 games. Larger games have no such separable Hamiltonian structure, and the problem remains open there. No counterexample to last-iterate convergence was found.

## 5. Evidence on the remaining open items

- **Hopkins 2.3.1.** A memoized exhaustive search over all firing choices ([hopkins_chipfiring_inversions.cpp](hopkins_chipfiring_inversions.cpp) → [results](hopkins-chipfiring-inversions.txt)) gives a maximum of m inversions for N = 3, 5, 7, 9, 11. The state counts are 4, 56, 1,699, 84,793 and 6,520,201. The numbers of distinct final permutations for N ≤ 9 are 3, 12, 54, 232. The full-run count of distinct final permutations at N = 11 is **819**. This extends OEIS [A282901](https://oeis.org/A282901) (1, 3, 12, 54, 232; keyword *more*, and its comment states this inversion conjecture) by the new term a(5) = 819; it has not been submitted. Extremal permutations are not products of adjacent transpositions (for example 1 2 4 3 5 9 6 7 8 at N = 9), so a proof needs a new invariant.
- **Schwarze's log-minor conjecture.** For k = 1 and k = n−1 it follows from Schur–Horn majorization, because diagonals of matrices with a fixed spectrum are majorized by it. Adversarial optimization over rotations and spectra matched the diagonal optimum to six digits at (n,k) = (4,2), (5,2), (6,3), for log κ ∈ {0.5, 2, 5}.
