# Q2191: near-linear fixed-constant RIP for the prime Paley frame

Exact target: absolute C,α>0 and 0<δ<√2−1 such that the Paley frame has two-sided RIP for every support of size at most Cp/(log p)^α at every sufficiently large prime p≡1 mod4. This is a fixed-δ question, not the stronger polynomially decaying-δ profile sometimes discussed in later sources. Full target remains unresolved.

Primary [Bandeira–Fickus–Mixon–Wong](https://arxiv.org/abs/1202.1234), local `texts/papers/collections-cfe7f3dbfd385686.txt.gz`, Definition 1, Theorem 13, §5.3, Lemma 22 and Conjecture 25 were reread. Write N=p+1 and S for the extended real sign matrix: finite entries χ(x−y), diagonal zero, and entries between ∞ and each finite point +1. Then S²=pI_N and Φ*Φ=I+S/√p. For a support I of size k, let A=S_{I,I}; its RIP constant is ‖A‖/√p.

Existing B2 coherence/Gershgorin, clique saturation and its first spectral gap are retained and not counted here. Below are five attempted extensions, with exact limitations.

<a id="a1"></a>
## A1. Import the exact global conference powers into every compressed support

The strong global identity S²=pI suggests controlling all higher moments of A without estimating new correlations. Compression gives ‖A‖≤√p and, for every integer s≥1,

    Tr A^(2s) ≤ p^(s−1)Tr A²
                =p^(s−1)k(k−1).

The ensuing power-method bound is

    δ_I ≤ min{1,[k(k−1)/p]^(1/(2s))}.

For k of the requested near-linear size, k(k−1)/p>1 eventually. Increasing s therefore never improves the constant 1. Global powers do not equal powers after compression: if B=S_{I,I^c},

    A²=pI_k−BB^T,
    δ_I²=1−λ_min(BB^T)/p.

Thus the exact missing assertion is a **uniform cross-block singular-value bound** λ_min(BB^T)≥(1−δ²)p on every near-linear support. The conference identity supplies only nonnegativity, and cannot remove the possibility that this eigenvalue is close to zero. This is the higher-power/compression route, not a new recount of entrywise coherence.

**Outcome: failed full-target proof route; no Paley support with bad RIP is asserted.**

<a id="a2"></a>
## A2. Randomize using symmetries, then invoke random partial Fourier RIP

The source's random-row Fourier theorem requires genuinely sampled row indices. The proposed derandomization is to randomize the fixed Paley frame by phases, permutations or row unitaries and treat the resulting distribution as the random model.

For every row unitary U and every column monomial unitary DΠ, the frame UΦDΠ has **exactly the same** worst-support RIP constants as Φ: restricted Grams are only relabeled and unitarily conjugated. A probability of success under that randomization is consequently either zero or one, determined by the unknown original RIP property. It cannot be inferred from a theorem about independent random Fourier rows. Even affine randomization of a quadratic-residue row mask has at most p(p−1) possible masks, versus binom(p,(p+1)/2) masks in the uniform model; it is a different distribution. The entropy observation alone is not a bad-RIP theorem, but it rules out an identification of those sampling laws.

The missing mathematical input is a concentration theorem for the actual algebraic row-mask law, rather than for independent row draws. No software randomization or numerical restart counts as a new attempt.

**Outcome: failed symmetry-to-random-sampling transfer.**

<a id="a3"></a>
## A3. Quantify full spark using an algebraic norm gap

Lemma 22 proves δ_I<1 whenever k≤(p+1)/2. The requested near-linear k eventually lies in this regime. To upgrade strictness to a uniform fixed gap, use that A is an integer matrix and both G_±=I±A/√p are positive definite in this regime. The latter follows from full spark and the tight-frame complement argument in the source.

The matrix pI−A² is a positive-definite integer matrix, so its determinant is an integer at least 1. Hence

    det G_+ det G_- = det(pI−A²)/p^k ≥ p^(−k).

Both Grams have eigenvalues at most 2. Thus det G_±≥(2p)^(−k) and

    λ_min(G_±) ≥ 2^(1−2k)p^(−k),
    δ_I ≤ 1−2^(1−2k)p^(−k).                  (1)

This is a real explicit quantitative consequence beyond mere nonzero minors. But at k=Cp/(log p)^α its gap is exponentially tiny, so it cannot establish δ<√2−1. The missing step is a far stronger collective minor/singular-value estimate, rather than algebraic integrality alone. Bound (1) does not show that any actual RIP constant approaches 1.

**Outcome: failed full-target route, with a valid restricted all-support gap.**

<a id="a4"></a>
## A4. Feed indicator uncertainty directly into flat restricted orthogonality

Theorem 13 turns flat restricted orthogonality of size k and constant θ-hat into an operator bound with a logarithmic loss. For disjoint finite supports I,J, the relevant sum is

    p^(−1/2)∑_{i∈I,j∈J}χ(i−j)
      =∑_{a≠0}χ(a)̄ˆ{1_I}(a)ˆ{1_J}(a),

using the unitary additive Fourier transform and the quadratic Gauss sum. The new indicator-concentration theorem bounds individual transform mass, but says nothing about its alignment with the signs χ(a). Cauchy on this expression only gives θ-hat≤1; multiplication by the logarithmic transfer loss is unusable.

This limitation is precise. Flat unit vectors u_a=1/√(p−1), v_a=χ(a)/√(p−1) satisfy the strongest singleton-scale coefficient caps, yet the displayed signed inner product is 1. They are not both indicator transforms, so this is a counterexample to a deduction **from coefficient caps alone**, not to the desired indicator correlation estimate. Positivity and joint arithmetic structure would need an additional argument.

There is also a genuine small-set obstruction to an overstrong replacement lemma: take I={0} and any J⊆Q of size k. The flat normalized correlation is √(k/p). At k=p/(log p)^α this decays only logarithmically, so a proposed uniform p^(−ε) flat-correlation gain on all such supports is false. A logarithmic gain, with sufficiently large α, remains compatible with this example and could solve the target. The missing step is exactly such a uniform **joint phase/correlation** bound, which does not follow from uncertainty's individual mass restrictions.

**Outcome: failed uncertainty-to-flat-orthogonality deduction; no RIP counterexample.**

<a id="a5"></a>
## A5. Replace worst-support control by a uniform random-support fourth moment

There is an exact positive calculation for a uniformly chosen k-subset I of the N=p+1 columns:

    E Tr(S_{I,I}^4)
      =k(k−1)(2k−3)−[k(k−1)(k−2)(k−3)]/(p−2).    (2)

Proof: closed four-step walks with two or three distinct vertices contribute k(k−1)(2k−3). Since Tr S⁴=Np², the sum of signed walks with four distinct vertices in the full matrix is −Np(p−1). Each survives restriction with probability (k)_4/(N)_4, producing the second term in (2).

Consequently P(δ_I>δ)≤2k³/(δ⁴p²). For k=o(p^(2/3)), a fixed-δ bound holds with probability tending to one for a random support. This breaks the coherence-scale restriction for **most** supports, but neither proves the near-linear size nor the worst-support requirement. At k=Cp/(log p)^α, this bound diverges. Even in its useful regime, a polynomial tail cannot be union-bounded over binom(N,k) supports.

The exact missing step is a uniform/high-tail bound strong enough to cover every support at the near-linear size. Random-support success does not remove exceptional algebraic supports. This random-column calculation is separate from A2's random-row sampling law, and belongs to one attempt together with the Markov/union-bound analysis.

**Outcome: failed full target, preserving the exact random-support theorem (2).**
