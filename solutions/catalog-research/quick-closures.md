# Quick closures from a catalog-wide screen

On September 30, all 1,592 unmarked conjecture and open-problem extracts were screened for statements recognizable as settled in the literature, or answerable quickly with a short proof or an exact computation. The screen found three short local resolutions, three resolutions already in the literature, and two promising problems that remain open.

| Thesis statement | Outcome | Basis |
|---|---|---|
| Ahmadi (2008), Conjecture 5.2.1 | **proved** | Hand proof §1; symbolic, exact and numerical controls |
| Ahmadi's suggested n×n extension (not a numbered conjecture) | **false for n = 3** | Exact rational certificates §1 |
| Mottram (2015), Question 2 | **answered: yes, with an explicit C_x** | Classical excursion marginal §2 |
| Martínez (2013), Conjectures 6.100, 6.103 | **proved** | Cyclotomic Möbius argument §3 |
| Martínez (2013), Conjecture 6.104 | **proved**, with one clause corrected | §3: “reflexive” holds as P(−x) = P(x). As palindromic it fails for n = 15, 21, 33, … |
| Martínez (2013), Conjecture 6.105 | **proved** (round 2) | §3: the Galois stabilizer is {±1}, by maximality of \|cot\| at k ≡ ±1 |
| Kadets (2020), Conjecture 4.1.4 (ρ = 2) | **disproved** in the literature | Smith 2021 |
| Lichtman (2023), Conjecture 12.1.1 | **proved** in the literature | Lichtman 2023 |
| Wolfgang (1997), Conjecture 1.2.9 (Stanley–Stembridge) | **proved** in the literature | Hikita 2024 |

The controls are [ahmadi_lyapunov_checks.py](ahmadi_lyapunov_checks.py) → [results](ahmadi-lyapunov-checks.json) and [martinez_cot_checks.py](martinez_cot_checks.py) → [results](martinez-cot-checks.json).

## 1. Ahmadi's 2×2 non-monotonic Lyapunov conjecture

**Statement.** Amir Ali Ahmadi, *Non-monotonic Lyapunov functions for stability of nonlinear and switched systems* (MIT SM 2008), Conjecture 5.2.1. For every 2×2 Hurwitz A there are τ₁, τ₂ ≥ 0 with

\[
M=\tau_2(A^3+3A^\top A^2+3A^{\top2}A+A^{\top3})+\tau_1(A^2+2A^\top A+A^{\top2})+(A+A^\top)\prec0 .
\]

Extraction ID `a10ca07cc94f7e2db9e2`; local text, p. 75. If it holds, one can fix P = I in Butz's third-order condition and search only over (τ₁, τ₂).

**Theorem.** The conjecture is true, with explicit coefficients. Write T = tr A < 0 and Δ = det A > 0.

- Complex eigenvalues (T² < 4Δ): τ₂ = 1/(4Δ), τ₁ = −T/(2Δ).
- Real distinct eigenvalues: τ₂ = 1/T², τ₁ = −2/T.
- Non-scalar repeated eigenvalue: τ₁ = −2/T and τ₂ = 1/T² + ε for all sufficiently small ε > 0.
- A = λI: τ₁ = τ₂ = 0.

**Proof.** Let f(t) = |e^{At}x|². Then x^⊤Mx = (Lf)(0), where L = τ₂D³ + τ₁D² + D has symbol p(s) = s·q(s) with q(s) = τ₂s² + τ₁s + 1. Since f is an exponential polynomial, the construction chooses q so that it annihilates the terms of indefinite sign.

- **Complex eigenvalues μ ± iω.** Here f(t) = e^{2μt}(a + Re(b·e^{2iωt})). The mean a(x) = (|x|² + |Bx|²/ω²)/2, where B = A − μI, is positive definite. The choice above makes the roots of q exactly 2μ ± 2iω, which removes the oscillating term. So M = p(2μ)·Q, where Q = (I + BᵀB/ω²)/2 is positive definite and p(2μ) = 2μω²/(μ²+ω²) < 0. The controls verify this identity symbolically for a general matrix [[a,b],[c,d]].
- **Real eigenvalues λ₁ < λ₂ < 0.** Here f = c₁₁e^{2λ₁t} + 2c₁₂e^{(λ₁+λ₂)t} + c₂₂e^{2λ₂t}, where c₁₁ and c₂₂ are nonnegative and not both zero, and c₁₂ has either sign. With q(s) = (s − T)²/T², the cross exponent T = λ₁+λ₂ is a root of q. What remains is p(2λᵢ) = 2λᵢ(λᵢ − λⱼ)²/T² < 0. More generally, any second root ρ ∈ (2λ₁, 2λ₂) works.
- **Jordan block.** The same q gives M ⪯ 0 with kernel spanned by the eigenvector e. On that kernel, e^⊤V₃e = f‴(0) = 8λ³|e|² < 0 for x = e. Increasing τ₂ slightly therefore makes M strictly negative definite, since M has only two eigenvalues. ∎

The quadratic factor of p is Hurwitz in every case, which is consistent with Butz's co-system condition.

**Controls.**
- The complex case is an exact symbolic identity.
- Exact rational negativity holds on 365 sampled matrices of all four types.
- On 200,000 random Hurwitz matrices, the numerical maximum of λ_max/‖M‖ is −1.8·10⁻⁹.

**The suggested extension fails.** Ahmadi adds that “the natural extension of this conjecture would be” to fix P = I in dimension n and use n coefficients on derivatives up to order n+1. For n = 3 this is false whenever the coefficients are nonnegative. That includes every choice whose co-system polynomial is Hurwitz, since q(0) = 1 then forces all coefficients to be positive. The controls give three exactly verified rational counterexamples. Each consists of A, Hurwitz by the Routh–Hurwitz test, and a rational x for which f′(0), f″(0), f‴(0) and f⁗(0) are all strictly positive. Then x^⊤M x > 0 for every admissible choice. For example,

A = [[−13/8, −25/8, 1/8], [−5/4, −9/4, −1], [−8, 0, −3/2]], x = (433/1000, −22/25, −193/1000).

The 2×2 argument cannot extend: an exponential polynomial with n(n−1) cross exponents cannot be annihilated by a polynomial with n free coefficients.

**Literature check (bounded).** The later Ahmadi–Parrilo note (ACC 2011) and Meigoli–Nikravesh (Systems & Control Letters 2012) treat general higher-derivative criteria. They do not state this 2×2 result. No prior resolution was found; novelty is not claimed.

## 2. Mottram's excursion question

Edward Mottram, *The geometry of non-Markovian interacting systems* (Cambridge 2015), Question 2 (`3cd16ad221bb93b595f7`). For a standard Brownian excursion (B_t)_{t∈[0,1]} and fixed 0 < x < 1, is B(B_x < ε) ~ C_x ε³, and how does C_x depend on x?

**Answer: yes.** The one-time marginal of the normalized excursion has density 2y²(2π)^{−1/2}(x(1−x))^{−3/2} exp(−y²/(2x(1−x))) on y > 0. This is the Bessel(3)-bridge marginal: Durrett, Iglehart and Miller 1977, and Revuz–Yor Ch. XII. Integrating near 0 gives

\[
\mathbb B(B_x<\varepsilon)=\frac{\sqrt{2/\pi}}{3\,(x(1-x))^{3/2}}\;\varepsilon^3\,(1+O(\varepsilon^2)).
\]

So C_x = √(2/π) / (3(x(1−x))^{3/2}), symmetric about 1/2 and blowing up at the endpoints. The ε³ exponent matches Mottram's entropic-repulsion theorem (his 4.1.7). This is a classical computation, not new work.

## 3. Martínez's cotangent conjectures

Roberto E. Martínez II (2013), Conjectures 6.100, 6.103, 6.104 and 6.105 (`554e70d25a867d4b5fde`, `adab297f8aede12e8145`, `6183bbce3ba05e94be41`, `7dcc3dfc5e1d6d81270f`); local text.

**Key identity.** Let ζ = e^{iπ/n}. Then θ_n = i·cot(π/2n) = (1+ζ)/(1−ζ), so ζ = (θ_n − 1)/(θ_n + 1) and Q(θ_n) = Q(ζ_{2n}). Apply the Möbius substitution to the cyclotomic polynomial:

\[
P_n(x)=\Phi_{2n}(1)^{-1}(x+1)^{\varphi(2n)}\,\Phi_{2n}\!\Big(\frac{x-1}{x+1}\Big).
\]

This is irreducible, monic, integral and of degree φ(2n). Its roots are σ_k(θ_n) = i·cot(πk/2n) for gcd(k,2n) = 1. That proves **6.103**.

**6.100.** For n ≥ 2 the product of the conjugates is the norm, Φ_{2n}(−1)/Φ_{2n}(1). For even n it equals 1. For odd n it equals Φ_n(1) = p if n = pᵃ and 1 otherwise. That is exactly lcm(1,3,…,n)/lcm(1,3,…,n−1). The case n = 1 is the δ-term.

**6.104.** For n = 2^m, Φ_{2n}(z) = z^n + 1 gives P_n = ((x+1)^n + (x−1)^n)/2 = Σ C(n,2k)x^{n−2k}. For an odd prime n, Φ_{2n}(z) = (z^n+1)/(z+1) gives ((x+1)^n + (x−1)^n)/(2x), which is the stated formula with φ(2n) = n−1.

The second clause covers n > 1 that is not an odd prime power. Palindromy of Φ_{2n} gives P(−x) = P(x). The leading coefficient is Φ_{2n}(1) = 1, and P(±1) = 2^{φ(2n)}. Read as “P(−x) = P(x)”, the clause holds.

Read as palindromic, it fails for odd n: x^φP(1/x) corresponds to Φ_{2n}(−w) = Φ_n(w) ≠ Φ_{2n}(w). The controls find failures at n = 15, 21, 33, 35, 39, 45, 51, 55, 57 among n ≤ 60. For even n it is palindromic, since 4 | 2n.

**6.105 (proved in round 2).** Let ϑ = −cot(π/2n)cot(π/2m) = (1+α)(1+β)/((1−α)(1−β)), with α = e^{iπ/n} and β = e^{iπ/m}. It lies in Q(ζ_{2L}), where L = lcm(n,m), and σ_k(ϑ) = ϑ_k := −cot(πk/2n)cot(πk/2m) for k ∈ (Z/2L)^×.

Every such k is odd, so πk/2n is an odd multiple of π/2n modulo π. Hence |cot(πk/2n)| ≤ cot(π/2n), with equality exactly when k ≡ ±1 (mod 2n); likewise for m. Therefore |ϑ_k| ≤ |ϑ_1|, with equality only if k ≡ ε₁ (mod 2n) and k ≡ ε₂ (mod 2m). The value ϑ_k = ϑ_1 also needs the same sign, which forces ε₁ = ε₂ and so k ≡ ±1 (mod 2L). The stabilizer is therefore {±1}.

So deg ϑ = φ(2L)/2 = φ(2nm)/(2 gcd(n,m)); the last step uses φ(2nm) = gcd(n,m)·φ(2L), because every prime of gcd(n,m) divides 2L. The conjugates are ϑ_k for 1 ≤ k ≤ L with gcd(k, 2L) = 1, equivalently gcd(k, 2nm) = 1. This is exactly the stated product. The m = 2 and n,m = 1 special cases follow. The earlier computational check (2 ≤ n, m ≤ 16) agrees.

The Möbius/cyclotomic description is classical; these are routine closures, not novel results.

## 4. Settled in the literature (primary sources checked)

- **Kadets (2020), Conjecture 4.1.4** (`b5f3c1665d4b1d9c5aa7`), the Schur–Siegel–Smyth constant ρ = 2. Here ρ is the liminf of the normalized trace over totally positive algebraic integers. Smith proves there are infinitely many totally positive α with tr(α) < 1.8984·deg(α), so ρ < 2. [Smith, arXiv:2111.12660](https://arxiv.org/abs/2111.12660).
- **Lichtman (2023), Conjecture 12.1.1** (`36bcc441fb74db7e8d51`), the Erdős primitive set conjecture. Proved by the thesis author: [Lichtman, Forum Math. Pi 11 (2023)](https://doi.org/10.1017/fmp.2023.16).
- **Wolfgang (1997), Conjecture 1.2.9** (`cee1fe1f4ab921eaf6da`, `0dcb32a0b350e49b87b3`), the Stanley–Stembridge e-positivity of X_inc(P) for (3+1)-free posets. Proved by [Hikita, arXiv:2410.12758](https://arxiv.org/abs/2410.12758). The neighbouring Conjecture 1.2.8 (claw-free ⇒ s-positive) is **not** settled by this.

## 5. Promising but not closed

- **Gu (2023), Conjecture 7.6** (`cfbae250ab2ad0836965`). This is a four-variable arctanh inequality that would give the r = 4 hypergraph SBM weak-recovery threshold. Findings:
  - At λ = 1 it is an identity: with θᵢ = tanh aᵢ, the tanh addition law gives F₁ = Σxᵢaᵢ, and sign-orthogonality reduces the left side to Σθᵢ arctanh θᵢ.
  - Both sides vanish at λ = 0. The left side is not convex in λ (convexity fails near λ = 0 with θᵢ → 1), so interpolation does not prove it.
  - The sign-averaged Lemma-7.4 analogue A₁ ≤ arctanh(λθ₁) holds numerically. The cubic Fourier coefficient can be positive, which blocks the r = 3 argument.
  - Two million random points confirm the inequality, with ratio → 1 only as λ → 1.

  A rigorous proof probably needs a computer-assisted interval argument with analytic treatment of the λ = 1 and θ = 0 faces.
- **Y. Zhang (2021), Conjecture A** (`df8ff6a17d2b44ad3e06`): the only integer solutions of (k²−n²)² + 4k⁴n⁴ = t² are the trivial ones. For fixed n, write N = n² and K = k². Then X = (1+4N²)K − N satisfies X² − (1+4N²)t² = −4N⁴, and the trivial solution K = N generates infinitely many Pell solutions. The conjecture is that no other K in these orbits is a nonzero square. No counterexample exists for k < n ≤ 2500, nor in the trivial Pell class for n ≤ 300. A proof needs square-detection in these recurrences, which is not a quick target.

Recognized-but-hard items were set aside without marks: White's conjecture, Stanley's pure O-sequence, the 1/3–2/3 conjecture, Hadwiger, KLS, Carmichael's totient conjecture, Falconer and the Pitts–Rubinstein index conjecture, among others.
