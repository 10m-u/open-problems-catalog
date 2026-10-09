# Uniqueness of Lippmann spectrum recovery

**Result.** Baechler's §4.7 conjecture holds for **uniform development**, the analytic model of §4.3.1. Assume a calibrated plate and any nonzero reflection coefficient r = ρe^{iθ}, covering air, mercury and both ideal mirrors. Then the reflected intensity spectrum determines the valid (nonnegative, band-limited) exposing spectrum exactly. Under **exponential development decay** (τ > 0), I prove a partial result. The reversal-type ambiguity is impossible for every r, because the exposure intensity is nonnegative. Every other ambiguity must be a Blaschke flip of a common zero. Such a flip is impossible when the support is preserved and contains a line at an odd comb index. The remaining τ > 0 cases are open here. Numerical and algebraic searches found no example.

The nonnegativity in “valid” is necessary. For real r and uniform development, there are signed spectra with identical data (§4).

This is a **partial answer**. It settles the conjecture in the uniform-development model with calibrated Z and r. It does not cover the decay model in full, or the uncalibrated recovery in which Algorithm 4.1 also estimates Z, τ and ε.

## Source and exact model

Gilles Baechler, *Sampling the Multiple Facets of Light* (EPFL 2018), §4.7 “Can we invert the Lippmann operations?”, printed pp. 91–92. After Algorithm 4.1 he writes: “We conjecture that this recovery is unique, under the condition that P(ω) is a valid and bandlimited power spectrum. Even though we do not provide a formal proof here, extensive simulations have shown that our algorithm always converges to the correct spectrum.” Extraction ID `0d1e1cc523bd2a4c63e8`; local text; [EPFL record](https://infoscience.epfl.ch/handle/20.500.14299/148835). “Valid” is defined just above as real, nonnegative and zero at negative frequencies.

Measure depth in units of the plate thickness Z. The band-limited spectrum is represented by comb samples p_n ≥ 0 at ω = nΩ_Z (n ∈ V, eq. 4.15), and line n exposes cos(nπz + θ). The thesis's matrix Φ_{m,n} = H_Z(nΩ_Z, mΩ_s) (eq. 4.17, with the decay filter of §4.5.2) is then exactly

\[
u(k)=\int_0^1 e^{-\tau z}\,h(z)\,e^{-ikz}\,dz,\qquad
h(z)=a_0+\sum_n p_n\,2\rho\cos(n\pi z+\theta),\qquad a_0=(1+\rho^2)\sum_n p_n ,
\]

where k = 4πZ/λ′ and the observation is v(k) = |u(k)|². Here h is the exposing intensity (eq. 4.1), so h ≥ (1−ρ)²Σp ≥ 0. The checker confirms the closed form against quadrature and against the partial-fraction form below (both to about 1e‑14).

v is the squared modulus of an entire function of k. Knowing it on any wavelength interval therefore determines it everywhere by analytic continuation. The theorems below assume that full observation. §6 covers finitely many samples.

## 1. The data as three rational functions

Put s = −τ − ik. Integrating each exponential gives u = e^{s}G(s) − K(s), with

\[
K(s)=\sum_i \frac{c_i}{s-s_i},\qquad G(s)=\sum_i \frac{\varepsilon_i c_i}{s-s_i},
\]

where the poles are s_i ∈ {0, ±inπ}. The residues are c = a₀ at 0, r p_n at −inπ and r̄ p_n at +inπ, with ε_i = (−1)^n and ε = 1 at the origin. G is K with each line's sign alternated because e^{s_i} = (−1)^n. It is the transform of h(·+1), and K is the transform of h.

Both functions are real-structured. On the data line, s̄ = −2τ − s. Hence

\[
v=e^{-2\tau}|G|^2+|K|^2-2\,\mathrm{Re}\!\left(e^{s}G\bar K\right).
\]

Here 1, e^{s} and e^{s̄} are linearly independent over rational functions. The data therefore determine exactly two rational functions: **M₀ = e^{−2τ}|G|² + |K|²** and **M₁ = G·K̄** (as G(s)K(−2τ−s)). Set X = e^{−2τ}|G|² and Y = |K|². Then X + Y = M₀ and XY = e^{−2τ}|M₁|². So {X, Y} is fixed as an unordered pair, and the rational identity forces one consistent choice on the whole line. Any spectrum p′ with the same data is therefore in one of two cases:

- **(i)** |K′| = |K| and |G′| = |G|;
- **(ii)** |K′|² = e^{−2τ}|G|² and e^{−2τ}|G′|² = |K|² (the *swap*, which is time reversal when τ = 0).

In both cases G′K̄′ = GK̄.

One-dimensional phase retrieval for rational functions with real structure then applies. |K′| = |K| on the data line forces K′ = c·B·K, where c = ±1 and B is a real-structured Blaschke product. B reflects a conjugate-closed set of numerator zeros across the data line and has |B| = 1 on it. With G′K̄′ = GK̄, case (i) gives G′ = cBG. So each flipped zero must be a **common** zero of K and G. Otherwise G′ acquires a pole that no spectrum can have.

## 2. Theorem 1: uniform development (τ = 0), any r ≠ 0

**Theorem 1.** Let τ = 0, r ≠ 0, and let Z be known. If two nonnegative, nonzero comb spectra p and p′ produce the same reflected intensity on any wavelength interval, then p′ = p.

**Proof.** The poles s_i lie on the data line itself. Every flip B is therefore unimodular at every pole. (Zeros on the line flip to themselves; B is regular and nonzero at poles, since a numerator zero is never a pole.)

*Case (i).* K′ = cBK. Its residue at ∓inπ is c·B(∓inπ)·(r or r̄)p_n. The residue must also equal (r or r̄)p′_n, and r ≠ 0. So cB(inπ) = p′_n/p_n is real and nonnegative with modulus 1, hence equal to 1, and p′_n = p_n. If p_n = 0, K has no pole at ±inπ. Since B is regular there, K′ has none either, so p′_n = 0.

*Case (ii).* Write K′ = c₁B₁G and G′ = c₂B₂K. At line n, K′ has residue c₁B₁(inπ)(−1)^n r̄ p_n. As in case (i), c₁B₁(−1)^n is a unimodular nonnegative real, so it equals 1 and p′_n = p_n. ∎

No nonnegativity argument beyond “a unimodular nonnegative real is 1” is needed. That is why the theorem covers complex r, including mercury's θ = −148°.

**Real r: the whole real fibre.** When θ ∈ {0, π}, the proof also describes the signed solutions. Split the lines by parity. Let E be the constant plus the even lines and O the odd lines, each a real rational function of k. Then

\[
v(k)=4\sin^2\!\tfrac{k}{2}\,E(k)^2+4\cos^2\!\tfrac{k}{2}\,O(k)^2
\]

(checked to 7e‑13). After clearing denominators, the cos k component separates E² from O². The data therefore fix E and O up to independent signs. For **real** p, the fibre is {±p} unless Σ_{n odd} p_n = 0. In that case it also contains ±(p_even − p_odd). The constant term a₀ = (1+ρ²)Σp is shared by both parity classes, and that makes the condition exact.

## 3. Theorem 2: exponential development decay (τ > 0)

Now the poles lie on Re t = τ in t = s + τ, strictly to the right of the data line Re t = 0. B need no longer be unimodular at the poles.

**Theorem 2a (no reversal ambiguity).** For τ > 0 and any r ≠ 0, case (ii) is impossible for nonnegative spectra.

**Proof.** Take the quotient H = c₁B₁/(c₂B₂). The identity G′K̄′ = GK̄ gives H(t) = K(t)G(−t)/(G(t)K(−t)). At the pole t = τ (the constant term, residue a₀ in both K and G), the residue patterns of K′ and G′ must agree. This forces H(τ) = e^{2τ}. Substituting K/G → 1 at that pole gives G(−2τ) = e^{2τ}K(−2τ) in the s-variable. But K and G are Laplace transforms of h and h(·+1), so

\[
G(-2\tau)-e^{2\tau}K(-2\tau)=e^{2\tau}\int_0^1 h(z)\,e^{-2\tau z}\,dz>0,
\]

because h ≥ 0 and h ≢ 0 (its mean a₀ is positive). The identity is checked to 2e‑15 on 200 random cases. B₁ and B₂ are regular and nonzero at τ, because K(−2τ) and G(−2τ) are strictly negative. ∎

**Theorem 2b (common-zero flips).** Suppose τ > 0 and p′ ≠ p has the same data. By 2a we are in case (i): K′ = cBK and G′ = cBG, where B flips common zeros of K and G. Also, B is real at every line position τ ± inπ, because p′_n/p_n is real. **If supp p′ = supp p and the support contains an odd n, no nontrivial B exists.**

**Proof.** Common zeros of K = E + O and G = E − O are common zeros of E and O. Their numerators have degree at most 2|S_even| and 2|S_odd| − 1. So B has degree d ≤ min(2|S_e|, 2|S_o| − 1) ≤ |S| − 1. The polynomial numerator of F(y) = B(τ+iy) − B(τ−iy) has degree at most 2d ≤ 2|S| − 2. It vanishes at the 2|S| + 1 points y ∈ {0, ±nπ}, so F ≡ 0, and B(t) = B(2τ − t). Unimodularity on the data line gives B(t)B(−t) = 1. Together these make B periodic with period 4τ. A periodic rational function is constant, so K′ = ±K. Nonnegativity then gives p′ = p. ∎

**What remains open under decay.**

- All lines at even comb indices. Then O ≡ 0, G = K, and every zero of K is flippable.
- Flips that add or remove lines, where support identifiability fails.

These cases reduce to a finite algebraic system: B real and positive at the line positions, B(τ) = 1 when r ≠ −1, and Σλ_n p_n = Σp_n. For two lines, the count of equations matches the count of free parameters (ratio, ρ, θ, τ), so isolated special-parameter counterexamples are not excluded by counting. A direct search of that system found only degenerate near-solutions. In all of them p′ = p and a far-away zero pair is flipped, giving B ≈ 1 at the poles. (Scratch search, not part of the checker.) A minimum-phase shortcut fails: zeros of the transform of h reach deep into the right half-plane, up to Re ≈ 2800 near r = −1.

## 4. Nonnegativity is necessary

Take r real, τ = 0, and lines 29, 30, 31 with p = (1, 2, −1). The odd lines sum to zero, so p′ = (−1, 2, 1) gives identical data for air and for the ideal mirror (maximum relative difference ≤ 4e‑15 over k ∈ [0.2, 60π]). The same pair is *not* equivalent for mercury's complex r (7e‑3) or with decay (2e‑2). The ambiguity is therefore specific to that model, and it is exactly the one §2 predicts. Without the “valid power spectrum” condition, the conjecture is false. The thesis's own Figure 4.24 already made this point informally with a negative interference pattern.

## 5. Numerical controls

The [checker](lippmann_uniqueness_checks.py) → [results](lippmann-uniqueness-checks.json) uses the thesis's visible-band operator: Z = 5 µm, 23 lines, 300 samples between 390 and 700 nm. It covers six regimes: air, ideal mirror and mercury, each uniform or with decay, plus a generic complex r.

- **Random and sparse spectra.** Eight spectra per regime, four dense and four with 1–3 lines, each with 25 random nonnegative restarts. Of 639 exact fits, **none** lies away from the truth.
- **Adversarial pairs.** A joint optimisation over (p, p′) ≥ 0, forced apart and allowed any support, was run on five small supports, including the unproved all-even ones. The best objective was 7e‑6, well above numerical zero. These are near-misses caused by conditioning, not ambiguities.
- **Conditioning, a new caveat.** For dense spectra the local Jacobian of p ↦ |Φp|² is well conditioned (condition number 15–500). For **real r without decay**, a spectrum with no odd-index line has a singular Jacobian (condition ~1e17). By the formula in §2, O enters v only through O², and the odd lines reach E only through the total a₀. So a signed, zero-sum perturbation of the odd lines is invisible to first order. Every such direction leaves the nonnegative cone, and every feasible direction inside the cone changes v at first order. Stability at these spectra therefore depends on enforcing nonnegativity, as the thesis's NNLS step (4.19–4.20) does. An unconstrained solver has error freedom of order √δ there. The simulations behind the conjecture used generic spectra, which avoid the boundary. This is why §5 reports it: “unique” and “stable” are separate claims.

## 6. Finite samples and what is not covered

**Finite samples.** Theorems 1–2 use the continuous visible band. After clearing denominators, the data lie in a real space of dimension at most 12N + 3 (three polynomial components of degree ≤ 4N). Evaluation at M ≥ 12N + 3 wavelengths in general position is therefore injective on that space, and the theorems transfer. The thesis's example has N = 23 and a few hundred bands, so this is satisfied (279 ≤ 300). For a 10 µm plate (N ≈ 45) the count needs about 550 bands. This is a genericity statement, not a certificate for a particular grid. Numerically, analytic continuation from the visible band is exponentially ill-conditioned in the lifted space, with a numerical rank of about 35.

**Not covered.**

- Unknown Z, τ, ε. ε·p is identifiable only up to scale in any case, and Algorithm 4.1 re-estimates Z and τ each round.
- The refractive-index model of §4.6.
- The wave-transfer (multiple-reflection) model.
- Convergence of Algorithm 4.1 itself. Uniqueness of the solution does not imply that the alternating projections reach it.

## Literature

No proof of this uniqueness appears in the group's 2022 signal-processing account ([Baechler, Pacholska, Latty, Scholefield, Vetterli, arXiv:2207.06004](https://arxiv.org/abs/2207.06004)). It cites the thesis for the recovery algorithm. The PNAS paper ([Baechler et al. 2021](https://www.pnas.org/doi/10.1073/pnas.2008819118)) could not be read here (HTTP 403), so it is unchecked. The proof ingredients are standard: zero flipping in 1‑D phase retrieval (e.g. [Beinert–Plonka, arXiv 2016](https://arxiv.org/abs/1604.04493)) and Blaschke factors. **No novelty claim**; this is a local deduction checked against the thesis model.

