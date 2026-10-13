# Q2190: a fixed constant improvement for two-local ordinary theta

Exact target: there is ε>0 with θ(H_p)≤(1/√2−ε)√p for all sufficiently large primes p≡1 mod4. Here H_p is induced on the common nonneighbors of the independent pair {0,g}, g a primitive root, and θ is ordinary independence theta. This is not Q2189's one-local nonnegative clique theta.

Primary [Kunisky, Appendix A, Conjecture A.1](https://arxiv.org/abs/2303.16475), local `texts/papers/collections-3dba30dbe1f379e4.txt.gz`; Definitions 1.3, Conjectures 1.8–1.9, Theorem 1.19 and Appendix A reread. Put T_p={x:χ(x)=χ(x−1)=1}, with its induced Paley graph. The map x↦gx identifies H_p with the **complement** of this graph. Thus θ(H_p) is ordinary clique theta of T_p; |T_p|=(p−5)/4. Five worked sufficient routes below fail; the conjecture is not refuted.

<a id="a1"></a>
## A1. Prove the predicted degree-two spectral edge, then use Hoffman

The source's edge prediction at localization degree a=2 is

    −λ_min(A_{H_p}) ∼ (√3/4)√p.

Even granting this difficult conjecture, the intended spectral ratio does not give the target constant. In the ideal regular limit n∼p/4, degree d∼p/8, the regular Hoffman theta certificate gives

    nγ/(d+γ) ∼ 2γ
                      =(√3/2)√p.

The constant √3/2≈0.866 exceeds 1/√2≈0.707. The source's Theorem 1.19 likewise gives the independence bound 2+(√3/2)√p+o(√p), not Appendix A's proposed theta constant. It is invalid to identify these separate conjectures. Proving spectral-edge control might be valuable for other targets, but this edge-only scalar ratio still cannot prove Q2190. This does not lower-bound the actual theta value; more structured duals can do better than that certificate.

**Outcome: failed edge-only sufficient route, exact coefficient obstruction.**

<a id="a2"></a>
## A2. Retain the one-local multiplicative circulant diagonalization

The one-local graph's vertices form the full cyclic square group. Try to use the same character Fourier LP after imposing the second anchor. The new vertex set T_p is not a multiplicative subgroup or a coset, and the resulting graph need not even be regular.

At p=37,

    T={4,10,11,12,26,27,28,34}.

The T-induced degrees are 2 at {4,10,12,26,28,34} and 4 at {11,27}; hence H degrees are 5 and 3. No relabeling can make this graph circulant, since every circulant graph is regular. Also 4·10=3 mod37 is outside T, directly refuting the proposed multiplicative closure. The principal compression of a circulant matrix is not diagonalized by the unrestricted group characters; multiplication by the indicator T couples frequencies.

This finite obstruction refutes a universal inherited-circulant reduction. It does not exclude an eventually special structure or a useful large matrix Fourier compression; either would need a new theorem. The source explicitly says that two-local theta requires an SDP rather than the one-local LP.

**Outcome: failed multiplicative-group reduction.**

<a id="a3"></a>
## A3. Iteratively condition ordinary degree-two theta without increasing moment degree

The proposed shortcut is to start with one-local ordinary theta and condition once more, hoping its low-degree moment constraints localize to the second anchor. This is not a valid general pseudoexpectation operation at degree two.

On {0,1}² assign weight 1 to (0,0),(1,0),(0,1), weight −1/3 to (1,1), and normalize by 8/3. Every affine polynomial q has zero second Walsh coefficient. Thus its value at (1,1) is a signed sum of the other three values, and Cauchy gives ∑_other q²≥q(1,1)²/3. This is a degree-two positive pseudoexpectation for the clique K₂, with

    y_1=y_2=1/4, y_{12}=−1/8.

Conditioning on x_1 gives expected x_2=−1/2, incompatible even with Boolean positivity. Ordinary theta permits such negative off-diagonal moments. Consequently repeated conditioning is not an available degree-two localization theorem. A true graph clique can be localized, but its theta relaxation cannot be conditioned the same way without further constraints/higher degree.

The witness is a general conditioning obstruction, not a proposed Paley optimum. A Paley-specific theorem could still help, but would have to establish the extra positivity/extension conditions. This is related to Q2188's degree-four/two-anchor obstruction, disclosed as shared mechanism, while the present attempted reduction uses a lower-degree starting program.

**Outcome: failed degree-preserving theta-conditioning route.**

<a id="a4"></a>
## A4. Use elliptic Weil bounds to regularize degrees and construct an explicit diagonal-corrected dual

For x∈T_p the exact triple-intersection expansion yields

    deg_T(x)=[p−15+W_x]/8,
    deg_H(x)=[p−3−W_x]/8,
    W_x=∑_tχ(t(t−1)(t−x)), |W_x|≤2√p.

So H degrees differ from b=(p−3)/8 by at most a=√p/4. This suggests making B=A_H+diag(b−deg_H), which has constant row sum b, then using the regular spectral dual. Principal interlacing of the global adjacency gives λ_min(A_H)≥−(√p+1)/2, hence λ_min(B)≥−γ with γ=3√p/4+1/2.

The construction is valid, but quantitatively too weak. Since B1=b1,

    B+γI−(b+γ)J/n ≽ 0,
    s=n/(b+γ), t=s(γ+a),
    tI+sA_H−J ≽ 0.

The last line follows by adding the nonnegative diagonal s[a−(b−deg_H)]. It is a genuine ordinary-theta dual and gives

    θ(H_p)≤t
      =2(p−5)(√p+1/2)/(p+6√p+1) ∼2√p.

This is worse even than the inherited global √p bound. Changing the center b within the degree interval does not repair its leading numerator: the upper bound on the eigenvalue shift and the necessary diagonal slack trade off, with their sum unchanged. The attempted degree-regularization route needs a **joint spectral/degree correlation** estimate; separate pointwise Weil and interlacing estimates are insufficient. Unlike A1, this constructs a dual for the genuinely irregular graph rather than pretending it is regular.

**Outcome: failed explicit elliptic-degree dual family, preserving the exact degree identities.**

<a id="a5"></a>
## A5. Use all projective two-anchor symmetries to recover a scalar LP

There is more symmetry than multiplicative closure: T is preserved by the six transformations generated by x↦1−x and x↦1/x, and their differences change by squares on T. Average the theta program under this S₃ action, then try simultaneous scalar diagonalization of its invariant coefficients.

At p=37 the two vertex orbits are O={4,10,12,26,28,34} and P={11,27}. Let D be the diagonal indicator of O and let B be the adjacency between O and P in the T-induced graph. Both are symmetric invariant matrices. Their off-diagonal entries are at **nonedges of H**, hence allowed in the independence-theta primal. But

    (DB−BD)_{4,11}=1.

The trace-zero variation D−(6/8)I has the same commutator. Starting from I/8, sufficiently small perturbations in either this diagonal direction or B preserve positivity, trace 1 and the H-edge zero constraints. Thus these are actual feasible invariant directions. Symmetry averaging does not simultaneously scalar-diagonalize their family; a representation-theoretic reduction retains PSD blocks.

This is a different attempted repair from A2: it uses the genuine projective S₃ action after multiplicative closure has failed. The witness refutes a universal scalarization claim, not a theorem that every large-prime dual has no exploitable form. The missing step is a tractable analysis of the remaining matrix blocks or a specific noncommuting dual construction with the desired constant.

**Outcome: failed projective-symmetry scalar-LP route.**
