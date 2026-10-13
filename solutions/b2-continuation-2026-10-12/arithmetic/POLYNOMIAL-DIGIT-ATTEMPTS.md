# Q1612–Q1613: split polynomials, units and degree digits

12 October 2026. Primary [Hajdu–Tijdeman–Varga](https://doi.org/10.1112/mtk.12209), local `texts/papers/collections-2f9061b447b8ccd0.txt.gz`. Introduction, Lemmas 2.1–2.3, Theorems 1.2–1.3 and Problems 2–3 reread. Source proves the p=2,3 digit cases and the degree bound when 2,3∉S; those are preserved prior scope, not counted as new solutions. Five routes below are per full target, with their unproved obligations explicitly retained.

## A useful exact fixed-prime reduction (Q1613 partial)

For each fixed prime p, the set of degrees n of rationally split integer polynomials with all coefficients nonzero mod p is effectively p-automatic. Consequently there is an algorithm deciding, for **that fixed p**, whether the numbers of nonzero digits of n+1 are bounded, and computing their maximum when bounded. This does not decide the universally quantified question or prove c(p)=p−1. No novelty claim.

Indeed the leading and constant coefficients are p-adic units. In a primitive integral factorization into linear factors, every numerator and denominator of a rational root is prime to p. Modulo p the polynomial is a nonzero scalar times
f(X)=∏_{r=1}^{p−1}(X−r)^{m_r}.
Conversely any such polynomial with no zero coefficient lifts to a rationally split integer polynomial ∏(X+r)^{m_r}: substituting −X and multiplying by a sign preserves coefficient nonvanishing modulo p, and all its integer coefficients are positive. Thus it is enough to recognize the tuples m whose entire coefficient interval is nonzero.

Write m_r=∑_j μ_{r,j}p^j. Frobenius gives f=∏_j F_j(X^{p^j}), where F_j=∏_r(X−r)^{μ_{r,j}} has degree at most (p−1)². To compute the coefficient indexed by i=∑_j d_jp^j, process these digits from low to high with a vector v∈F_p^p, initially (1,0,…,0), representing carry c=0,…,p−1. The transition is
v'_{t}=∑_{c=0}^{p−1}v_c [X^{d_j+pt−c}]F_j.
No carry exceeds p−1: ((p−1)²+p−1)/p=p−1. Once all input digits finish, zero padding (F_j=1,d_j=0) clears positive carries and the coefficient is v_0. This is a finite automaton with p^p coefficient states, not a heuristic about digit sums.

The synchronized relations n=∑m_r, 0≤i≤n, and i's digits are regular using ordinary finite addition/comparison carries. Intersect them with final coefficient zero and existentially project i to recognize bad multiplicity tuples. Complement within canonical finite padded words, then existentially project m_r and the degree-addition relation to recognize good degrees. Regular languages are closed under these operations (subset determinization provides an explicit finite construction). Add one by the usual carry transducer to obtain the language of n+1. Padding and canonical leading digits can be enforced by regular constraints, so infinitely many representations of one integer do not affect the result.

Give each nonzero digit weight 1. In a finite automaton for the canonical language, the weights of accepted words are unbounded exactly when an accessible positive-weight directed cycle can reach an accepting state. Repeating that cycle proves necessity; in its absence contracting zero-weight strongly connected components bounds every accepting path and computes the maximum. This supplies the stated fixed-p decision algorithm. We have not constructed/determinized the enormous universal recognition automata even at p=5, or proved a property of their positive cycles uniformly in p.

`check_digit_carries.py` checks the central coefficient transition against direct multiplication on 8,264 coefficients at p=2,3,5,7. It is a control of the reduction, not an evaluation of every accepted word and not proof of the universal conjecture.

<a id="q1613-a1"></a>
## Q1613 A1 — Solve the universal question through the fixed-prime decision reduction

The exact automaton and weighted-cycle test above are a complete algorithm for any specified p. Applying this for successively many primes still cannot prove all primes succeed: the state space and transitions depend on p, and no uniform exclusion of accessible positive cycles has been obtained. Its sufficient remaining lemma is that every resulting good-degree automaton has no such cycle, with maximal weight ≤p−1 for the stronger conjecture. **Full-target failure; useful partial theorem.**

<a id="q1613-a2"></a>
## Q1613 A2 — Extend the one-root Lucas classification

For (X−r)^n, Lucas makes all coefficients nonzero exactly when n+1=ap^j with 1≤a≤p−1: every digit below the leading digit of n must be p−1. This gives just one nonzero digit of n+1. With several roots the coefficient is a sum of products of binomial coefficients, not one product; neither nonzero summands nor individually good factors imply a nonzero sum. Already p=3, (X−1)(X+1)=X²−1 has a zero middle coefficient while both factors are good. Thus multiplication does not preserve the predicate used by the Lucas induction. The source's p=3 two-root analysis supplies additional cancellations; no p−1-root counterpart has been proved. **Failed universal proof.**

<a id="q1613-a3"></a>
## Q1613 A3 — Bound digits from Frobenius block support alone

If each F_j had degree <p, coefficient blocks would not overlap and support would be a product of digit supports. In reality deg F_j≤(p−1)², so neighboring blocks overlap through nonzero carries. For p=3 and μ_1=2, μ_2=1, F_j=(X−1)²(X+1)=X³−X²−X+1 modulo 3 reaches degree 3. Index 3 in F_j(X)F_j(X³) has contributions 1 from degrees (3,0) and −1 from (0,1), which cancel. Thus Cartesian support even predicts a nonzero coefficient where the actual coefficient vanishes; the complete carry sum is required. The worked reduction accounts for this but does not force the number of active digit positions. The missing statement is a cancellation-sensitive global bound, not merely a maximum block degree. **Failed support-only route.**

<a id="q1613-a4"></a>
## Q1613 A4 — Use the logarithmic derivative to constrain all multiplicities

The identity f'/f=∑_r m_r/(X−r) over F_p sees only m_r mod p. Replacing any m_r by m_r+p^j for j≥1 leaves this logarithmic derivative unchanged, although the degree and higher blocks change. A rational-function identity of bounded degree therefore cannot constrain all digit positions by itself. Recursive application would need the stronger property that a nonvanishing coefficient row forces a good row after Frobenius stripping, precisely the carry-cancellation condition left open above. Derivative/Newton identities also lose indices divisible by p. **Failed differential route; higher multiplicity information remains absent.**

<a id="q1613-a5"></a>
## Q1613 A5 — Lift to characteristic zero and use the real-root height bound

The source height theorem gives n≤(5/log2)log H for split polynomials with nonzero roots and H≥2. The positive lift ∏(X+r)^{m_r} has H growing exponentially with n, so this inequality is compatible with arbitrarily large n. More generally roots r+pL preserve all mod-p coefficients while making H arbitrarily large. Residue nonvanishing imposes no uniform height cap. The theorem bounds degree once height is bounded; it supplies no digit bound from the finite-field hypothesis. **Failed height route.**

<a id="q1612-a1"></a>
## Q1612 A1 — Remove degree from the fixed-degree S-unit classification

The source proof writes ∑q_i²=A_1²−2A_2 with all q_i,A_j S-units and uses a nondegenerate S-unit estimate of size (8m−8)^{4(m−1)^4(m+|S|)} for m=n+2. It classifies root shapes at each fixed n. Both the equation's number of terms and its bound increase with n, so finiteness of the shape list at each n does not bound which n occur. Degenerate subsums lead to its paired-root family, not a contradiction. A degree-independent bound on the lengths of the positive-square subsums would close this route; it is not supplied by the fixed-m theorem. **Failed uniform classification route.**

<a id="q1612-a2"></a>
## Q1612 A2 — Combine two primes outside S and digit sparsity

Choose distinct p,q∉S. All coefficients are units modulo both, so the two digit conjectures, if proved, bound the nonzero digits of n+1 in multiplicatively independent bases. Stewart's theorem quoted in the primary paper then bounds n. This is an exact sufficient conditional reduction, but Q1613 at arbitrary p,q is still unproved; S may contain 2 or 3 or both, so the established pair (2,3) cannot be chosen in general. This is not a full proof of Q1612 and does not count the known S∩{2,3}=∅ case anew. **Failed unconditional route.**

<a id="q1612-a3"></a>
## Q1612 A3 — Convert finite prime support into bounded height

Each nonzero coefficient has form ±∏_{ℓ∈S}ℓ^{e_{j,ℓ}}, with exponents unbounded. Fixed S does not bound H; even multiplying a single split polynomial by ℓ^M yields arbitrary H without changing degree or its admissibility. Removing content does not solve this, since roots can vary through rational S-units and coefficient ratios can have arbitrarily large valuations. The real-root height inequality from the source therefore remains a degree-vs-height relation, not a degree bound in terms of S. **Failed height route.**

<a id="q1612-a4"></a>
## Q1612 A4 — Exploit Newton inequalities using positivity

After flipping all roots' signs when they have one common sign, elementary symmetric coefficients are positive and Newton's inequalities give (A_j/binom(n,j))²≥(A_{j−1}/binom(n,j−1))(A_{j+1}/binom(n,j+1)). Ratios of A's are S-units, but S-units can be arbitrarily large or small, so these inequalities alone do not bound n. Moreover signs are unrestricted in the exact problem: the admissible paired-root family (X+u)∏(X²−v²r_i²) changes coefficient signs and defeats the proposed all-positive reduction. A sign-sensitive unit estimate of length independent of n is still missing. **Failed positivity route.**

<a id="q1612-a5"></a>
## Q1612 A5 — Induct down the source's paired-root family

The exceptional family has degree 2t+1 and coefficients alternating between those of g(X)=∏(X−r_i²), multiplied by powers of v and by u. Hence f is an S-polynomial only if every coefficient of g is an S-unit. Descending from f to g halves the degree, but admissibility at a smaller degree is no contradiction, and reverse lifting requires the roots of g to be rational squares at every step. There is neither a maximal starting degree nor a preserved infinite square-root tower construction here. The reduction produces a concrete smaller-instance obligation instead of bounding all admissible degrees. **Failed descent/constructive route.**

## Status

Five substantive routes failed for each full target. Retain both original partial marks. Add the fixed-prime automaticity and decision result at its stated scope only; no catalog closure follows.

