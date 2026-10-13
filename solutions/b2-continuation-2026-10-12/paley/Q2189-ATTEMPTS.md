# Q2189: infinitely many strict one-local nonnegative-theta improvements

Exact target: for infinitely many primes p≡1 mod4,

    1+τ_+(L_p) < floor((1+√(2p−1))/2),

where L_p is the Paley graph induced by nonzero squares. This is the one-local graph, not Q2190's two-local H_p. Primary [Magsino–Mixon–Parshall](https://arxiv.org/abs/1907.05971), local `texts/papers/collections-95a192677a9c9142.txt.gz`, definitions (2)–(3), Propositions 4–5 and Conjecture 6 were reread. The circulant clique-theta primal uses a real even f with f(0)=1, f=0 at nonedges, ˆf≥0, and f≥0. Its objective is ∑f. A convenient dual has a real even d with ˆd≥0 and d(j)≤−1 at each adjacency index; its objective is 1+d(0). All five routes below fail to establish the full infinite-prime target. No numerical pattern is counted as a proof or as an independent attempt.

<a id="a1"></a>
## A1. Use the single spectral/Hoffman dual and uniform Jacobi bounds

For a d-regular graph on n vertices and L the largest nonconstant adjacency eigenvalue, the adjacency-only clique-theta dual yields

    τ_+(G)≤τ(G)≤ n(1+L)/(n−d+L).

This follows by using the minimum eigenvalue −1−L of the complement in its usual regular Hoffman theta bound. For L_p, n=(p−1)/2 and d=(p−5)/4. A nonconstant character of the cyclic square group extends to ρ on F_p*, and its adjacency eigenvalue is

    λ_ρ=−1/2+[J(ρ,χ)+J(ρχ,χ)]/4.

Both Jacobi sums have modulus √p. Their triangle inequality gives L≤(√p−1)/2 and the resulting upper bound 1+τ_+(L_p)≤√p. This does not reach the Hanson–Petridis constant 1/√2.

Nor can sharper estimation of L rescue this particular spectral family asymptotically. Kunisky's proved degree-one Kesten–McKay bulk law [Theorem 1.18](https://arxiv.org/abs/2303.16475) implies that L≥(1/2−o(1))√p: every fixed interval just inside the right edge has positive limiting spectral mass. The nonsquare scaling identification with the complementary one-local graph only reverses nonconstant eigenvalues and adds −1. Thus the optimized adjacency-only expression is (1−o(1))√p, above the requested floor ~√p/√2. A magic dual needs more than one affine combination of I,A,J. Any univariate pointwise polynomial of χ(α^j−1) collapses to this same three-value family; it is not an additional attempt.

**Outcome: failed full-target certificate family.**

<a id="a2"></a>
## A2. Find a bounded-rank positive Fourier magic function

Try a dual d whose Fourier support contains at most r frequency pairs, for an absolute r, choosing those frequencies separately for each prime. This is more general than a fixed low-frequency trigonometric polynomial. It is impossible for all sufficiently large p: such a positive-definite d cannot be negative on every one-local edge.

Here is an all-size proof. Let a(j) be the cyclic adjacency indicator, n=(p−1)/2, d_0=(p−5)/4. The preceding Jacobi formula gives |ˆa(ℓ)|≤L_0=(√p+1)/2 for ℓ≠0. For any r selected frequencies k_s set D=4r² and

    W(j)=∏_{s=1}^r(1+cos(2πk_sj/n))^D.

All Fourier coefficients of W are nonnegative. Its normalized constant coefficient is at least c_D^r, where c_D=binom(2D,D)/2^D≥2^D/(2D+1), and the sum of its normalized coefficients is W(0)=2^(Dr). Since 2^D>(2D+1)^r, the gap γ=c_D^r−2^(D(r−1)) is positive. Fourier mixing gives

    ∑_j a(j)W(j)≥d_0 c_D^r−L_0 2^(Dr).

If every adjacent j had cos(2πk_sj/n)≤0 for some s, then W(j)≤2^(D(r−1)) there, and the same sum would be at most d_0 2^(D(r−1)). These contradict for large p, since d_0 is order p and L_0 order √p. Therefore some adjacent j has **all selected cosines positive**. Any real even d with nonnegative Fourier coefficients supported on these frequency pairs (and possibly zero) is nonnegative there, violating d(j)≤−1. Self-opposite frequencies are included by the same argument; r can overcount harmlessly.

This establishes a genuine restricted obstruction: the Fourier rank of a valid dual must grow with p. It does not rule out growing-rank magic functions, and does not refute Q2189. The same argument includes bounded low-frequency degree as one special case, not a second count.

**Outcome: failed full-target bounded-rank construction.**

<a id="a3"></a>
## A3. Lift the continuous Hanson–Petridis clique bound to this LP

The proposed route starts by treating the combinatorial Hanson–Petridis bound as an upper certificate for the one-local LP, then seeks a strictness argument and prime rounding. Its first universal implication is false. A new rational primal witness at p=29 proves

    1+τ_+(L_29) > (1+√57)/2.

Use square-group generator α=4, n=14, f(0)=1, and nonzero entries

    f(3)=f(11)=738250/1001000,
    f(4)=f(10)=63687/1001000,
    f(6)=f(8)=356895/1001000.

All these indices are edges, entries are nonnegative and all Fourier coefficients are positive. The objective after adding the anchor is 4319664/1001000, about 4.31535, exceeding HP(29)≈4.27492. `check_theta_routes.py` certifies Fourier positivity with rational Taylor enclosures and proves the last strict comparison by exact squaring. A bounded numerical LP suggested this witness; the proof uses the saved rational vector and interval check, not solver success.

Thus the finite-field clique argument does not automatically supply a dual of this real LP. This witness does not exclude an eventually valid strengthened LP theorem, nor does it refute the infinite-prime conjecture (floor HP(29)=4). The missing step is an actual PSD/nonnegative-theta certificate, rather than importing a bound valid only for integer clique indicators.

**Outcome: failed clique-bound-to-LP transfer, exact feasible obstruction.**

<a id="a4"></a>
## A4. Integralize the cyclic LP, so rounding an integer clique bound controls its objective

For p=17 take square-group generator α=9. The eight-vertex local graph has adjacency indices {1,4,7}. A symmetric primal is f(0)=1, f(1)=f(7)=a, f(4)=b, zero elsewhere. Fourier positivity and entrywise nonnegativity reduce to

    a,b≥0, b≤1−√2 a, b≥2a−1.

The objective 1+2a+b is maximized at a=2−√2, b=3−2√2, giving

    τ_+(L_17)=8−4√2,
    1+τ_+(L_17)=9−4√2≈3.34315.

For completeness the upper bound follows by b≤1−√2a and a≤2/(2+√2); the displayed vector attains it. Symmetry averaging is valid here because the graph is circulant. Thus the LP optimum is irrational and strictly above the integer clique bound 3. The full Paley graph has no four-clique because τ_+(L_17)<3, while an explicit three-clique exists. The floor of an integer bound does not turn this LP into an integral one.

This refutes the proposed integrality/total-unimodularity shortcut. It is different from A3's failed continuous HP lift: even an exact integer clique bound cannot be substituted for the LP objective. A Paley clique-number theorem alone would not establish the required theta improvement without an additional relaxation bound.

**Outcome: failed integer-rounding reduction.**

<a id="a5"></a>
## A5. Amplify a finite prime certificate by tensor powers

Suppose a verified seed certificate exists on the cyclic local graph at p_0 (the source reports p_0=61 among its improvements; the missing old certificate archive is not recovered here). Write n_0=(p_0−1)/2. Tensoring a kernel or a graph construction naturally gives the group (Z_{n_0})^t and n_0^t vertices. To identify it with another prime local graph would require p_t=2n_0^t+1 prime and a compatible cyclic Paley adjacency pattern.

Already the group identification fails: for t>1, (Z_{n_0})^t has exponent n_0, whereas Z_{n_0^t} has exponent n_0^t. They are not isomorphic. Reading tensor coordinates as base-n_0 digits changes the convolution through carries; the cyclic Fourier positivity is no longer the tensor diagonalization. The Paley character pattern is not closed under this product operation either. Finally, infinitely many primes of the exponential form p_t are not furnished by Dirichlet's theorem, which only handles arithmetic progressions. Any of these gaps blocks the proposed amplification; no claim about whether such primes actually are infinite is made.

Unlike A2, the tensor rank is allowed to grow, so its failure is not merely the bounded-rank obstruction. The missing construction is an actual graph/kernel transfer preserving the prime local adjacency constraints and cyclic positivity, together with an infinite eligible prime set. Finite seed certificates remain valid finite evidence, not an infinite-prime proof.

**Outcome: failed tensor-amplification route.**
