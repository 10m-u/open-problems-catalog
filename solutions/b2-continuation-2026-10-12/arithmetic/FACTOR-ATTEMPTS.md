# Q2414–Q2415: cyclotomic sums and products

Exact setup and source statements are in the question register. The primary paper is the cached October 2026 source `texts/papers/collections-efd9d2285dc0c9ac.txt.gz`, particularly Theorems 1.1, 1.3–1.7 and Lemma 3.1. Its nonreciprocal-part theorem and its noncyclotomic-part conjectures have different hypotheses. Earlier powers-of-two partials are preserved. The exact local box in [FACTOR-CHECK.json](FACTOR-CHECK.json) contains 870 sum/product polynomials, 2≤n≤m≤30; this is smaller than the paper's reported box and is a control, not new extensive evidence.

## A reciprocity reduction with exact scope

Write h*(X)=X^deg(h)h(1/X). For n,m>1 the two cyclotomic polynomials are reciprocal.

For the product question, put F=Φ_nΦ_m and D=deg F. Then h=F+1 and h*=F+X^D. Every reciprocal irreducible factor of h divides h* as well, hence divides X^D−1 and is cyclotomic. Thus **all reciprocal irreducible factors of this particular product-plus-one family are cyclotomic**, and its nonreciprocal and noncyclotomic parts agree. It would be incorrect to obstruct this family by proposing a reciprocal noncyclotomic factor.

For a sum with d=deg Φ_n>e=deg Φ_m, h*=Φ_n+X^(d−e)Φ_m. A common reciprocal factor divides (X^(d−e)−1)Φ_m, so again it is cyclotomic. When d=e, the whole sum is reciprocal and this argument has no degree-difference term. Neither reduction proves that the remaining nonreciprocal part has only one irreducible factor.

<a id="q2414-a1"></a>
## Q2414 A1 — Apply the sparse prime-constant theorem directly

The source's theorem applies to a polynomial with constant prime p and remaining coefficients 1 at distinct exponents. Test this prerequisite on the family before applying it: Φ_3+Φ_4=X²+X+1+X²+1=2X²+X+2 already has a nonconstant coefficient 2. Cyclotomic polynomials can also have negative coefficients. Thus arbitrary sums do not have the required shape. Multiplication by a carefully chosen cyclotomic factor repairs special index patterns, but no such repair is constructed for every pair. **Failed unrestricted sparse-theorem route.**

<a id="q2414-a2"></a>
## Q2414 A2 — Complete the argument using reciprocity

The displayed common-factor calculation successfully removes reciprocal factors for unequal degrees. The unresolved step is uniqueness of the remaining nonreciprocal factor. Reciprocity alone does not imply this: (X+2)(X+3) has two nonreciprocal factors. Equal-degree sums are themselves reciprocal, so a theorem only about the nonreciprocal part says nothing about their entire remaining reciprocal part. This is an actual algebraic reduction with a residual factorization obligation, not a claim that the conjecture has a reciprocal counterexample. **Failed reciprocity-only completion.**

<a id="q2414-a3"></a>
## Q2414 A3 — Extend the powers-of-two Eisenstein proof to all sums

The earlier powers-of-two sum has two isolated nonconstant monomials and constant 2; the appropriate substitution/Eisenstein argument exploits that shape. In contrast Φ_3+Φ_4=2X²+X+2 has an odd middle coefficient and leading coefficient divisible by 2, so Eisenstein at 2 cannot apply directly. A prime constant alone does not suffice: (X²+X+1)(X²+2) is monic, has constant 2, and is reducible. No uniform translation or cyclotomic stripping is proved to restore an Eisenstein polygon for all pairs. **Failed uniform Eisenstein extension.**

<a id="q2414-a4"></a>
## Q2414 A4 — Turn the source's density-one theorem into an all-pairs proof

Theorem 1.3 covers n=ℓ^t p,m=ℓ^t q with primes p>q>ℓ; Theorems 1.6–1.7 extend to almost all suitably squarefree coprime odd-prime patterns with matched parity. For fixed numbers of primes the exceptional-count estimate is one power of π(X) smaller than the total, but may still grow without bound. Pairs with shared odd factors, repeated odd-prime powers and different parity are not all covered either. The estimate gives neither a finite list nor an induction closing its exceptions. **Failed density-to-universality route.**

<a id="q2414-a5"></a>
## Q2414 A5 — Use finite factorization to infer a bound on exceptional indices

Exact factorization and removal of every cyclotomic factor were executed for 2≤n≤m≤30, with no counterexample. The procedure can be repeated at any finite bound, but cyclotomic coefficients and φ(n) are not bounded in terms of this box, and the degree comparison has no monotone exceptional-index descent. The paper's larger reported 500-box also lacks that descent. This is a failed counterexample search at a declared domain, not evidence of a theorem bounding all indices. **Failed bounded-search completion.**

<a id="q2415-a1"></a>
## Q2415 A1 — Apply the sparse theorem to a general product plus one

For Φ_3²+1=X⁴+2X³+3X²+2X+2, overlapping convolution coefficients violate the distinct-exponent coefficient-1 condition of Theorem 1.1. Negative cyclotomic coefficients create further violations. The source constructs cyclotomic multipliers for special prime patterns, but multiplication is not a general coefficient-decollision operation. **Failed direct sparse-theorem route.**

<a id="q2415-a2"></a>
## Q2415 A2 — Use constant 2 and the complete reciprocal-factor reduction

The displayed reduction proves all reciprocal factors cyclotomic, so it removes a real logical ambiguity. What is still needed is an irreducibility theorem for the entire remaining nonreciprocal part. Monicity, constant 2 and absence of reciprocal factors are insufficient: (X²+X−1)(X²−2) is monic, has constant 2, and has two nonreciprocal irreducible factors. This is not a cyclotomic-product-plus-one counterexample. No structural exclusion of such a split in the target family is obtained. **Failed constant/reciprocity criterion.**

<a id="q2415-a3"></a>
## Q2415 A3 — Extend equal-index powers-of-two Eisenstein

The old equal powers-of-two result is genuine. Its coefficient divisibility does not survive a general cyclotomic product. For n=m=3, the coefficient of X² in Φ_3²+1 is 3, so Eisenstein at 2 fails. Even equal indices require more than that proof. Prime-constant reducibility examples above rule out replacing the missing divisibility by constant 2 alone. **Failed Eisenstein extension.**

<a id="q2415-a4"></a>
## Q2415 A4 — Extend the three-prime theorem by induction on prime divisors

Theorem 1.4 covers n=2^e p_1p_2,m=2^e q_1 with distinct odd primes. Theorem 1.6 covers almost all opposite-parity disjoint patterns. Adding another prime changes Φ_n(X) by quotient/substitution identities, but does not preserve irreducibility of Φ_nΦ_m+1: division and the final addition of 1 do not commute. There is no induction step reducing an arbitrary repeated/shared-prime pair to the theorem. The density-one exceptional set is not an induction base. **Failed prime-pattern induction.**

<a id="q2415-a5"></a>
## Q2415 A5 — Exhaust a box and strip cyclotomic factors

The second half of the exact 870-polynomial control validates the factor-stripping implementation and finds no product counterexample in the box. A finite search supplies no upper bound on the prime divisors, degrees or overlap pattern of a potential exceptional pair. Its limitation is the same missing global index descent as the sum search; this shared ingredient is disclosed rather than described as a separate impossibility theorem. **Failed finite counterexample search.**

Five substantive routes per target failed to close the exact universal claims. The reciprocity lemma and known source subfamilies survive at their stated scopes; neither conjecture is marked solved.
