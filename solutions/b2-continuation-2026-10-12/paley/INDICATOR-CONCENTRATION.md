# Uniform indicator concentration across the two arithmetic bases

Locally proved 12 October 2026; main-thread proof and scope review accepted in [ROOT-REVIEW.md](../ROOT-REVIEW.md#transfer). No novelty claim. This is a uniform quantitative transfer theorem, separate from the five open Paley catalog targets and from the earlier flat-basis uncertainty theorem. It handles the constant mode and the missing multiplicative direction explicitly.

For an odd prime p, work in the mean-zero subspace of ℓ²(F_p). Use the orthonormal additive basis e_a(x)=p^(−1/2)exp(2πiax/p), a≠0. Complete the nontrivial multiplicative character vectors m_ψ(x)=ψ(x)/√(p−1), with ψ(0)=0, by

    v=(pδ₀−1)/√(p(p−1)).

These are exactly the bases in the original B2 character result. Let ∅⊊S⊊F_p have k elements, put e=1_{0∈S}, and normalize its centered indicator

    f=(1_S−k/p)/√(k(p−k)/p).

Define

    a=min(k,p−k)²/[k(p−k)],
    b=(pe−k)²/[(p−1)k(p−k)],
    h=min(k−e,p−1−(k−e)),
    q=ph²/[(p−1)k(p−k)].

For arbitrary sets of additive modes R and completed multiplicative modes T, let r=|R|, s=|T| and t=1_{v∈T}. Then

    ‖P_R f‖² ≤ r a,
    ‖P_T f‖² ≤ t b+(s−t)q.                  (1)

Thus if the projection errors are at most ε and η, respectively,

    r a ≥ 1−ε²,
    (s−t)q ≥ (1−η²−t b)_+.              (2)

Equation (2) is interpreted without division when q=0. It is valid for **every** nonconstant indicator, every prime p and every choice of projections and errors; the set need not be a clique and need not have nonvanishing Fourier coefficients.

Proof: the nonzero additive coefficient is ∑_{x∈S}exp(−2πiax/p)/√(k(p−k)). Summing over the complement negates it, so its magnitude is at most min(k,p−k)/√(k(p−k)). The analogous nontrivial character coefficient is √p ∑_{x∈S\{0}}̄ψ(x)/√((p−1)k(p−k)). The full sum over F_p* is zero, so its magnitude is at most √p h/√((p−1)k(p−k)). Finally ⟨v,f⟩=(pe−k)/√((p−1)k(p−k)), exactly. Sum the squared coefficient bounds over each selected orthonormal set. No Gauss-sum cancellation estimate is required for this proof.

For the useful anchored case **S⊆F_p***, one may use the looser caps k/(p−k) in the additive basis and pk/[(p−1)(p−k)] in the entire completed multiplicative basis, since b is 1/p times the latter. Therefore approximate concentration implies

    rs ≥ (1−ε²)(1−η²)
           (p−1)(p−k)²/(p k²).              (3)

For each fixed γ>0, k≤p^(1/2−γ), p≥5 and ε,η<1, this is at least

    [(1−ε²)(1−η²)/8] p^(1+2γ).

This improves the p-scale flat-basis product restriction by a power for small indicators. It concerns **approximate energy**, so the earlier rationality fact that every nonzero additive Fourier coefficient is nonzero does not make it vacuous.

The exception at zero is necessary: for S={0}, f=v exactly, b=1 and q=0; all p−1 additive coefficients have the same energy, while a single completed multiplicative mode captures everything. The unrestricted version of (3) would be false here. Likewise S=F_p* gives f=−v. The full version (1)–(2) includes both cases.

Paley consequence: translate any clique C by any of its vertices and remove the anchor. Its remaining k=|C|−1 vertices form a subset of F_p*, so (3) excludes simultaneous approximate representations on mode sets whose product is smaller than its explicit bound. In particular, a small hypothetical clique indicator cannot be compressed in both arithmetic bases merely because it lies in the quadratic residues. The theorem gives a uniform structural exclusion, **not** a new clique-number upper bound or a resolution of Q2187–Q2191. Its contribution to the broader B2 transfer ambition is precisely this quantitative nondegenerate replacement for the useless exact-support product on rational indicators.

Source/setup links: original [B2 return Part A §3](../../b2-2026-10-07/B2_Research_Report_2026-10-07.md) and primary [Bandeira–Fickus–Mixon–Wong §5.3](https://arxiv.org/abs/1202.1234) for the Paley frame motivation. The argument here follows directly from orthogonality and indicator positivity; it does not assert that existing robust flat-basis bounds were missing.
