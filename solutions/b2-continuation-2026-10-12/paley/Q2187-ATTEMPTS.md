# Q2187: full prime-Paley clique bound

Exact target: absolute (C,K>0) with ω(G_p)≤C(log p)^K for every prime p≡1 mod4. No full solution is claimed. Existing B2 results, including global theta=√p and exact-support uncertainty, are preserved and are not new attempts.

Primary setup: Kunisky–Yu, [Conjecture 1.1](https://arxiv.org/abs/2211.02713), local text `texts/papers/collections-1a69b18128a88092.txt.gz`; quadratic character χ(0)=0, adjacency χ(a−b)=1. Kunisky, [Theorem 3.7 and Proposition 4.3](https://arxiv.org/abs/2303.16475), local text `texts/papers/collections-3dba30dbe1f379e4.txt.gz`, supplies the individual polynomial-character Weil estimate. The calculation below is a new local worked reduction, with no novelty claim.

<a id="a1"></a>
## A1. A collective fourth-moment bootstrap from clique constraints

**Outcome: full-target failure of this sufficient proof route, pending independent review.** The exact collective identity is useful, but the individual Weil estimates leave a square-root error after dividing by the clique moment. This does not disprove Q2187.

Let C be a k-clique and F(x)=∑_{a∈C}χ(x−a). For x∈C, F(x)=k−1. For distinct a,b, ∑_xχ(x−a)χ(x−b)=−1. Expanding F^4 by multiplicity patterns gives the exact identity

    ∑_x F(x)^4 = p(3k²−2k)−12k³+26k²−15k
                       +24 ∑_{D⊆C, |D|=4} W(D),
    W(D)=∑_x χ(∏_{a∈D}(x−a)).

Here the five multiplicity patterns contribute respectively

    k(p−1), −4k(k−1), 6 binom(k,2)(p−2),
    −24k binom(k−1,2), and 24∑_D W(D).

For the fourth term, ∑_xχ(x−a)²χ(x−b)χ(x−c)
=−1−χ(a−b)χ(a−c)=−2, using the clique constraint. Thus this calculation actually uses the full pairwise clique condition, rather than bounding an arbitrary character sum by its spectral norm.

Nonnegativity of the fourth powers outside C gives

    k(k−1)^4 ≤ p(3k²−2k)−12k³+26k²−15k
                   +24∑_D W(D).                         (1)

Each W(D)≤3√p by the squarefree degree-four Weil bound, so the collective last term is at most 72 binom(k,4)√p. When k grows, division of (1) by k⁴ leaves a term asymptotic to 3√p. At k of order √p this is compatible with (1); at k any fixed power of log p it is much larger than the left-hand effective k. Consequently (1) with individual estimates cannot force a polylogarithmic k, and in fact is weaker at the exponent level than the existing exact second-moment identity

    ∑_x F(x)²=k(p−k),
    k(k−1)²≤k(p−k).

The attempted bootstrap was to exploit the known clique values of F in a higher moment, retaining the pairwise cancellations before applying Weil to the genuinely new quartic terms. The exact missing step is a **collective upper cancellation bound** for ∑_{D⊆C,|D|=4}W(D) strong enough to suppress the k⁴√p term. The pairwise character identities do not supply it. Higher even moments treated one squarefree polynomial at a time have the same obstruction: the all-distinct terms contribute at most (2s−1)k^(2s)√p, which again leaves a square-root term after normalization. This higher-moment observation belongs to this same attempt, not an additional count.

`check_paley_moments.py` verifies the multiplicity identity and second moment with exact integer arithmetic on bounded prime-Paley cliques and checks the scale compatibility of (1). It does not test or refute the asymptotic conjecture and does not recover the missing earlier verification archive.

<a id="a2"></a>
## A2. Grow the localization degree to obtain a polylogarithmic bound

**Outcome: full-target failure, pending review.** This is a uniformity problem in a concrete moving-degree reduction, separate from A1's collective fourth moment.

Work in the independent-set convention of Kunisky's source; multiplication by a nonsquare identifies independence and clique numbers. For fixed localization degree a, that paper's conditional Theorem 1.19 reads

    α(G_p) ≤ a + [√(2^a−1)/2^(a−1)]√p + o_a(√p),

assuming its minimum-eigenvalue Conjecture 1.9 at degree a. If this estimate instead held uniformly with an absolute constant factor and negligible remainder at

    a(p)=ceil(log₂p−2K log₂log p),

then the principal term would be O((log p)^K) and a=O(log p). If a exceeds the actual independence number, the desired O(log p) bound already holds; otherwise localization is legitimate. Thus this is a sufficient full-Q2187 route for any fixed K≥1.

But the proof needs vertex-count and degree estimates. Even the refined character expansion gives

    | |V(G_{p,I})| − p/2^a + a/2 |
       ≤ (a/2−1+2^(−a))√p.

For a(p) above, the proposed main count is of order (log p)^(2K), while the justified error is of order √p log p. In particular the published size estimate does not even establish the predicted main order. Relative control from this inequality requires approximately a < (log₂p)/2−O(log log p); substituting that regime in the proposed spectral bound leaves a p^(1/4) factor. Fixed-a asymptotics cannot be diagonalized to a(p) of order log p without rates.

The missing lemmas are uniform moving-a intersection counts **and** spectral-edge control for these same deterministic localizations. Weak empirical spectral convergence, even convergence of every fixed moment, does not supply the latter: adjoining one eigenvalue −3 to a sequence whose bulk lies in [−2,2] changes each fixed normalized moment by O(1/N), while the minimum stays −3. This is a matrix-level counterexample to that inference, not a counterexample involving a Paley localization. A uniform high-moment or strong-convergence statement with rates is still needed. The source itself separates weak convergence (Conjecture 1.8) from edge convergence (1.9); neither is a proved moving-a theorem.

<a id="a3"></a>
## A3. Obtain the polylogarithmic clique bound by an optimized degree-four SOS certificate

**Outcome: this whole certificate class is obstructed by a proved feasible pseudoexpectation.** Q2187 itself is not refuted; higher degrees or other methods remain possible.

The proposed route was to exploit affine symmetry in the complete degree-four clique moment matrix and optimize all, rather than only FK, pseudomoments until its dual yielded a polylogarithmic upper bound. With indices the empty set, vertices and edges, the primal entry M_{S,T} depends on S∪T, is zero for noncliques, has M_{∅,∅}=1 and M≽0. Any dual certificate at this degree must upper-bound every such feasible M.

Kunisky–Yu [Theorem 3.1](https://arxiv.org/abs/2211.02713) gives an explicit obstruction: for all sufficiently large eligible primes and a fixed sufficiently small c>0, put

    t=cp^(−2/3), (α₀,α₁,α₂,α₃,α₄)
       =(1,t,4t²,8t³,512t⁴),
    M_{S,T}=α_{|S∪T|} if S∪T is a clique, and 0 otherwise.

I read the definition, the two Schur-complement reductions and the theorem's exact parameter statement in local source sections 2.2–3. The remaining positive-semidefiniteness estimate is a published input here, not a new independent reproof of that long estimate. The structural constraints hold directly and its objective is pα₁=cp^(1/3). By weak duality, **every** feasible degree-four dual has objective at least cp^(1/3), even if its coefficients break affine symmetry. Since p^(1/3)/(log p)^K→∞ for each fixed K, no such upper certificate can solve Q2187. This uses the full feasible family as an obstruction, not a conclusion that FK lower bounds characterize the full SOS optimum. In particular it does **not** settle Q2188: any proposed exponent there may lie between 1/3 and 1/2.

This attempt is distinct from the already-filed exact degree-two theta obstruction: it tests the next full moment class and gives its different unavoidable exponent. No numerical SDP search is necessary.

<a id="a4"></a>
## A4. Force small additive doubling, then apply sum-product growth

**Outcome: the prerequisite structural lemma is false on arbitrarily large prime-Paley cliques.** This refutes a size-only small-doubling reduction, not Q2187.

After translating an anchor to zero, clique differences lie in Q∪{0} and nonzero clique elements lie in Q, so products also lie in Q. The proposed sum-product route would first deduce |C−C|≤L|C| or additive energy E_+(C)≥|C|³/L for an absolute L from the pairwise square condition, then use the fact that products and differences avoid half the field. That first lemma is false, even for prime fields and for arbitrarily large clique size.

For every k choose the integer Sidon set C_k={1,4,...,4^(k−1)}. Its nonzero ordered differences are all distinct: the 2-adic valuation of 4^i−4^j, i>j, is 2j and then its odd part determines i. Thus |C_k−C_k|=k(k−1)+1 and E_+(C_k)=2k²−k. Let M be 8 times the product of odd primes dividing its positive differences. For every prime p≡1 mod M with p>2·4^(k−1), all those differences are quadratic residues: χ_p(2)=1, and quadratic reciprocity gives χ_p(q)=χ_q(p)=1 for each odd q|M. The sign is also a square. No differences collide modulo p under this size condition. Dirichlet's theorem supplies infinitely many such primes for each fixed k.

Consequently C_k is a prime-Paley k-clique of maximal possible difference-set size and minimal possible additive energy. Neither an absolute doubling constant nor a superquadratic energy lower bound can follow from clique size alone. Translation preserves these facts, so the anchor normalization does not repair the lemma. The elementary inclusion itself only gives E_+(C)≥k⁴/((p+1)/2), generally weaker than the diagonal bound near k≤√p.

The construction gives no useful relation between its primes and k and does not contradict a polylogarithmic bound in p. A sum-product route could still use a new **p-dependent** energy/correlation estimate that applies specifically near a hypothetical super-polylogarithmic clique; the rejected size-only structure lemma cannot be that estimate. Dirichlet and quadratic reciprocity are standard external inputs, not newly proved here. A primary exposition of the stronger prime-number theorem in progressions is [Tao's proof](https://terrytao.wordpress.com/2014/10/25/a-banach-algebra-proof-of-the-prime-number-theorem/).

<a id="a5"></a>
## A5. Turn multiplicative residue membership into approximate two-basis concentration

**Outcome: the concentration bridge fails quantitatively.** This works with approximate mass rather than the earlier exact-support degeneracy, but its best directly justified multi-anchor bound returns the second moment. No closure of Q2187 follows.

Translate a k-clique so it contains 0 and put D=C\{0}, d=k−1. Consider the centered indicator f=1_D−d/p, with ‖f‖²=d(p−d)/p. In the completed multiplicative orthonormal basis on the mean-zero subspace, the quadratic-character vector m_χ=χ/√(p−1) has

    |⟨m_χ,f⟩|² / ‖f‖² = pd / [(p−1)(p−d)].       (2)

The completion vector v=(pδ₀−1)/√(p(p−1)) contributes d/[(p−1)(p−d)]. Thus the pair of coefficients determined by the anchor captures only

    (p+1)d / [(p−1)(p−d)]

of the energy. For d=o(p) this tends to zero, rather than one. Multiplicative residue membership is a spatial support constraint on half the multiplicative group; it is not approximate sparsity of the character transform. For D⊆Q, character coefficients at ψ and ψχ are equal (before the trivial-character completion), which permits many nonzero paired coefficients rather than forcing them to vanish.

Trying all clique anchors does not fix the problem. Put q_a(x)=χ(x−a). Their Gram matrix is pI−J. For the centered full-clique indicator h=1_C−k/p one has ⟨q_a,h⟩=k−1 for every a∈C. The largest Gram eigenvalue is at most p, so

    k(k−1)² ≤ p‖h‖²=k(p−k).

This is precisely the square-root second-moment restriction, disclosed here as overlap in the obstruction, not a new impossibility theorem. The attempted new step was to feed a small **approximate** multiplicative spectrum into the robust flat-basis inequality. Formula (2) shows that the only coefficients forced by clique residue membership give vanishing mass, and the simultaneous anchor constraints yield no stronger input. A quantitative higher-order correlation statement is needed to establish actual transform concentration or another uncertainty gain.

The separate indicator-concentration note below will record the size-sensitive transform bounds that really do follow from positivity; they are partial transfer results and do not make this full-target attempt successful.
