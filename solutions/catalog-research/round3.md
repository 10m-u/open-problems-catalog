# Round 3: extragradient on 2×2 ratio games

**Result.** For every 2×2 von Neumann ratio game with a non-degenerate interior equilibrium z*, consider extragradient with a small enough constant step. It has **last-iterate convergence to z*** from every start inside the region of closed gradient-descent–ascent orbits. More precisely, it converges uniformly on each compact sub-level set strictly inside that region.

The proof combines three facts:
- an exact Hamiltonian structure of the continuous dynamics, found in [round 2](round2-harder.md);
- a new convexity lemma for its orbits (§2);
- a one-step Lyapunov estimate for the discrete extragradient map (§3).

This is a **partial answer** to Golowich (2025), Problem 13.4.2. Larger games, boundary equilibria, and starts outside the closed-orbit region remain open. A bounded literature search found no prior treatment.

Source: Noah Golowich, *Theoretical Foundations for Learning in Games and Dynamic Environments* (MIT 2025), §13.4, Problem 13.4.2 (`c9757a96a30026468248`; local text). The problem asks whether extragradient with a constant learning rate has last-iterate convergence for V(x,y) = ⟨x,Ry⟩/⟨x,Sy⟩ with ⟨x,Sy⟩ ≥ ζ > 0. The thesis shows that the Minty variational inequality (MVI) fails, so the standard proof route is unavailable.

## 1. Setting and Hamiltonian structure

Write x = (p, 1−p), y = (q, 1−q), u = (1,p), v = (1,q), and V = N/D with N = u^⊤𝒩v and D = u^⊤𝒟v > 0, where 𝒩 = [[n₀,n₂],[n₁,n₃]] and 𝒟 = [[d₀,d₂],[d₁,d₃]]. The minimizer controls p and the maximizer controls q. Extragradient uses the field G = (−∂_pV, ∂_qV).

Two quadratics carry everything. The p-terms in N_pD − ND_p cancel, and so do the q-terms in N_qD − ND_q, giving

\[
D^2\partial_pV = W(q)=\det(\mathcal D v,\mathcal N v),\qquad D^2\partial_qV=\hat V(p)=\det(\mathcal D^\top u,\mathcal N^\top u).
\]

So G = D^{−2}(−W(q), V̂(p)) = D^{−2}J∇H, where H(p,q) = A(p) + B(q), A′ = V̂ and B′ = W, and **∇H·G ≡ 0**. Continuous gradient descent–ascent is a time-changed Hamiltonian flow, and its orbits are level curves of H. The roots of V̂ and W are the affine coordinates of the eigenvectors of the pencil (𝒩, 𝒟).

At an interior equilibrium z* = (p*,q*), V̂′(p*) = W′(q*) = D²·∂²_{pq}V(z*), because ∂_pV = ∂_qV = 0 there. Hence **every interior equilibrium is a center** of H: a strict local minimum of sH with s = sign(∂²_{pq}V) ≠ 0 (the non-degeneracy assumption). The controls confirm V̂′(p*) = W′(q*) in all 300 sampled games. Without loss of generality, take H(z*) = 0 as a minimum.

Let h̄ be the supremum of levels h such that the component of {H ≤ h} containing z* is compact, lies in the open square, and contains no other critical point. Every orbit through a point with H < h̄ is closed.

## 2. Lemma: closed orbits are convex

**Lemma.** For h < h̄, the set K_h = {H ≤ h} (the component of z*) is convex, and its boundary has strictly positive curvature.

**Proof.**

*Normalization.* If V̂ and W are both quadratic, write V̂(p) = c_p(p−p*)(p−p₂) and W(q) = c_q(q−q*)(q−q₂). Substitute p = p* + (p₂−p*)ξ and q = q* + (q₂−q*)ζ. This is a diagonal affine map, so it preserves convexity. Then

  H = P·g(ξ) + R·g(ζ), with g(t) = t²/2 − t³/3 and P, R > 0

(positivity is exactly the center condition). The other critical lines are ξ = 1 and ζ = 1. Since g is decreasing on (−∞, 0] and increasing on [0, 1] with g(1) = 1/6, the closed-orbit region is contained in Ω = {ξ<1, ζ<1, Pg(ξ) + Rg(ζ) < m/6} with m = min(P,R).

*Curvature.* The level-curve curvature numerator (J∇H)^⊤∇²H(J∇H) equals PR·Φ, where

\[
\Phi=R\,g''(\xi)\,g'(\zeta)^2+P\,g''(\zeta)\,g'(\xi)^2,\qquad g'(t)=t(1-t),\ g''(t)=1-2t .
\]

We show Φ > 0 on Ω ∖ {0}.

- **Both ξ, ζ ≤ ½.** Both terms are non-negative. They vanish together only at the origin within Ω.
- **Both > ½.** Impossible, since that would give Pg(ξ) + Rg(ζ) > (P+R)/12 ≥ m/6.
- **ξ ∈ (½, 1) and ζ ≤ ½** (the other case is symmetric).
  - Since g(ξ) > 0 and P ≥ m, Rg(ζ) < m(1/6 − g(ξ)) = m·u(ξ), where u(ξ) = (1−ξ)²(1+2ξ)/6. Hence g(ζ) < u(ξ) and Rg(ζ) < P·u(ξ). In particular ζ < ½.
  - If ζ = 0, Φ = Pg′(ξ)² > 0. Otherwise g(ζ) > 0, and with k(ζ) = g′(ζ)²/(g(ζ)(1−2ζ)) = 6(1−ζ)²/((3−2ζ)(1−2ζ)) and j(ξ) = g′(ξ)²/((2ξ−1)u(ξ)) = 6ξ²/(4ξ²−1):

\[
R(2\xi-1)g'(\zeta)^2=R\,g(\zeta)(1-2\zeta)k(\zeta)(2\xi-1)< P\,u(\xi)(1-2\zeta)(2\xi-1)\,k(\zeta),
\]
\[
P(1-2\zeta)g'(\xi)^2=P(1-2\zeta)(2\xi-1)u(\xi)\,j(\xi).
\]

  - So it suffices that k(ζ) ≤ j(ξ). After clearing positive denominators, this is

\[
\xi^2(3-2\zeta)(1-2\zeta)-(1-\zeta)^2(4\xi^2-1)=(1-\zeta)^2-\xi^2=(1-\zeta-\xi)(1-\zeta+\xi)\ \ge 0 ,
\]

    that is, ζ ≤ 1 − ξ.
  - Let G(t) = 6g(t) = 3t² − 2t³ (smoothstep). Then G(1−t) = 1 − G(t), so g(ζ) < u(ξ) = 1/6 − g(ξ) = g(1−ξ). Because g is increasing on [0, 1] and 1−ξ ∈ (0, ½), this gives ζ < 1 − ξ when ζ > 0. When ζ < 0 the conclusion is immediate.

*Degenerate cases.*
- If V̂ is linear (an eigenvector at infinity), then H = P·ξ²/2 + R·g(ζ). Only ζ > ½ can make Φ negative. Using Pξ²/2 < R·u(ζ), the requirement reduces to g′(ζ)² ≥ 2(2ζ−1)u(ζ), which is 3ζ² ≥ 4ζ² − 1, true for ζ ≤ 1.
- If both V̂ and W are linear, H is quadratic and the orbits are ellipses.

Φ > 0 away from the center and ∇H ≠ 0 there, so the closed level curves are smooth, strictly convex simple curves. ∎

Numerical controls agree:
- the reduced one-variable inequality has minimum ratio exactly 1, attained in the corner ξ → 1, ζ → 0, as the factorization predicts;
- a normalized two-variable grid over 41 values of P/R has no violations;
- 19,940 random games had no negative curvature on their closed-orbit regions ([round 2](round2-harder.md)).

## 3. Theorem: last-iterate convergence of extragradient

**Theorem.** Let z* be a non-degenerate interior equilibrium of a 2×2 ratio game with ⟨x,Sy⟩ ≥ ζ > 0, and let h < h̄. There is η₀ > 0 such that for every constant η ∈ (0, η₀), extragradient

  z_{t+1} = T_η(z_t) = z_t + ηG(z_t + ηG(z_t))

started at any z₀ ∈ K_h stays in K_h, and z_t → z* linearly. In K_h the projections are inactive.

**Proof.** Fix z and set φ(η) = H(T_η z). Then φ′(0) = ∇H·G = 0. Differentiating the identity ∇H·G ≡ 0 gives ∇H·(DG·G) = −G^⊤∇²H·G, and therefore φ″(0) = G^⊤∇²H·G + 2∇H·DG·G = −G^⊤∇²H·G.

Write w(t) = T_t z − z = tG(z + tG(z)). Then w′ = O(|G|), w″ = O(|G|²) and w‴ = O(|G|²). Also |∇H| = D²|G| exactly, so every term of φ‴ is O(|G|²) on the compact set K_h. Taylor's theorem then gives

\[
H(T_\eta z)-H(z)\le-\tfrac{\eta^2}{2}\,G^\top\nabla^2H\,G+C\eta^3|G|^2 .
\]

Now G^⊤∇²H·G = D^{−4}(J∇H)^⊤∇²H(J∇H) = D^{−4}·κ·|∇H|³.
- Near z*, H is a positive-definite quadratic up to higher order, so this quantity is ≥ c|G|².
- On K_h minus a small ball around z*, the Lemma gives κ > 0 and |∇H| is bounded below, so again it is ≥ c|G|².

For η ≤ c/(4C), H(z_{t+1}) ≤ H(z_t) − (cη²/4)|G(z_t)|². The iterates stay in K_h, since H decreases and steps are O(η). Hence Σ_t|G(z_t)|² < ∞, G(z_t) → 0, and z_t → z*, the only zero of G in K_h. Near z*, |G|² ≥ c′H, which gives the linear rate. ∎

**Controls** ([ratio_game_eg_lyapunov.py](ratio_game_eg_lyapunov.py) → [results](ratio-game-eg-lyapunov.json)). Over 300 random games with an interior equilibrium:
- V̂′(p*) = W′(q*) held in every case;
- one exact extragradient step (η = 2·10⁻³) strictly decreased H at **all 6,390,753** grid points of {H ≤ 0.9 h̄};
- 4,000,000-step runs from the outermost such point converge geometrically. The worst-case distance to z* halves every quarter of the run (0.052 → 0.026 → 0.0127 → 0.0063), and 298/300 runs end within 10⁻⁴. Contraction is only O(η²) per step, so convergence is slow in absolute terms.

**Scope and limits.**
- The theorem is local–semiglobal: η₀ depends on h, and starts with H ≥ h̄ are not covered. Those are orbits that reach the boundary or pass the saddle level, where the projection acts.
- Equilibria on the boundary of the square and degenerate equilibria (∂²_{pq}V(z*) = 0) are not covered.
- Larger games have no separable Hamiltonian. The cancellation that makes ∂_pV depend only on q is a 2×2 phenomenon.
- The thesis's MVI-failure example (its eq. 13.13) is not covered, because its equilibrium is a pure profile on the boundary. The theorem therefore does not contradict the thesis's observation that MVI fails.
- Ledger status for Problem 13.4.2: **partial**.
