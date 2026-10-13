# Independent Q1249 review — 2026-10-13

I accept the shifted repeated-pole theorem in [RESULTS](../hadamard/RESULTS.md) and five distinct full-target failures in [ATTEMPTS](../hadamard/ATTEMPTS.md). This leaves Conjecture 1.12 unresolved, with its necessity and degree-two-through-four literature cases preserved. I read the [primary setup, Conjecture 1.12, Theorems 1.11 and 1.18](https://arxiv.org/html/2512.06468v1), both checkers and receipts.

For each l>=0, t>0, m>=1, removing the zero factor from the l-th tail gives an LP-I function C_l. The coefficient of z^j after the stated product of theta+h operators is precisely binomial(j+m-1,m-1) a_(j+l); hence the output for z^l/(1-tz)^m is the asserted LP-I function. At a simple negative zero r of p, (theta+h)p(r)=r p'(r). Alternation gives the internal roots, and the largest root and zero give the final negative root. Zero factors replace h by h+s; repeated roots and entire functions follow by LP-I polynomial approximation and convergence of derivatives. Zero tails, constant functions and m=1 cause no exception.

The ordinary Hadamard preservation statement for two nonnegative LP-I entire functions is valid. The text's phrase “source's classical Malo/Hadamard theorem” needs a more precise reference: the 2025 target paper does not explicitly state it. [Csordas–Dimitrov, Theorem 2.4(4)](https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/czdssurvey.pdf) states the polynomial Hadamard theorem. Extend it using nonnegative LP-I polynomial approximations to both functions: for any fixed R their absolute coefficient sums on radius sqrt(R) are uniformly bounded, and a larger radius supplies a geometric bound on the Hadamard tails. Thus the products converge locally uniformly to the entire coefficient product. This is an attribution clarification, not a mathematical gap.

The five failures have different obligations:

- H01 constructs degree-five-through-seven candidate multipliers and actual Edrei pole/numerator inputs. The 30,960 inputs are actual TP inputs; the 387 multipliers are only numerically tail-tested. The screen is one bounded counterexample attempt, not 30,960 attempts or an exact theorem that those candidates satisfy the hypothesis.
- H02's exact all-tail cubic disproves the proposed universal q>=4 bridge. Positive cubic discriminant and positive coefficients give three negative real roots; its next-tail discriminant is also positive.
- H03 proves the repeated-pole subclass, but the entire-input approximation step fails already at b0=b1=b2=1: for an entire normalized Edrei product, b2=(b1²-sum alpha_i²)/2<=b1²/2.
- H04's positive tail cone is not LP-I. The weights (1,1,101) are outside TP-infinity and do not refute the conjecture.
- H05 changes the multiplier A, rather than the input B as in H03. At q=18/5 the primary partial-theta result certifies preservation, while its quadratic Taylor section has negative discriminant. Its tails are rescaled copies of the entire function, so the all-tail condition is genuinely present.

The source theorem is normalized to positive initial coefficients; that is enough to establish the partial-theta LP-I premise here (take a geometric input), after which the exact rescaling handles all tails. No general mixed-pole result follows from the two preserved subclasses.

[Independent checker](check_hadamard_forest_review.py) and [receipt](HADAMARD-FOREST-REVIEW-CHECK.json) verify four discriminants and 256 shifted repeated-pole coefficient identities using Fraction arithmetic and repeated geometric-series convolution. No floating screen was rerun or promoted. This is internal review, with no novelty or external peer-review claim.

