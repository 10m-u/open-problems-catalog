# Analytic arithmetic: Q1312,Q1509,Q1510,Q2904–Q2907

12 October 2026. Primary texts reread: Letendre 2607.07641 (H definition, Conjecture 1, Proposition 3, rarity estimates); Mukhopadhyay thesis introductory squarefree/abc statements; Pasten's squarefree-at-primes paper §§1–2; Carrillo Santana 2504.08502v2 Theorem 1.1 and §1.3; Benli–Dartyge–Dombrowsky–Pollack–Thompson 2607.18981 Conjecture 1.3 and exact density setup; Thompson's cyclotomic survey order-five open problem. Paths are in QUESTION-REGISTER.md. No unverified imported quartic theorem is upgraded.

## Q1312 — strengthened abc with H

<a id="q1312-a1"></a>
### A1. Absorb the logarithmic denominator into classical abc
Write R=rad(abc), k=ω(abc); H=R/(log R)^k. Classical abc controls c by R^{1+δ}, but the required replacement would need k log log R=o(log R) uniformly over abc triples. General squarefree R can have k≈log R/log log R, so this loss is order log R, not negligible. The source's minimum H at fixed k is e^{−k(1+o(1))}. No abc-specific exclusion of that regime has been proved. **Failed deduction from the ordinary conjecture, itself unproved here.**

<a id="q1312-a2"></a>
### A2. Refute the target using arbitrarily small H on primorial-like integers
The source minimizes H(n) over all integers with ω(n)=k. An arbitrary such n need not be abc for a coprime positive sum a+b=c. Setting a=1,b=n gives abc=n(n+1), introducing every prime factor of n+1 and changing both R and k. Thus the minimizers alone do not provide a sequence c/H(abc)^{1+ε}→∞. **Failed counterexample construction.**

<a id="q1312-a3"></a>
### A3. Convert a rarity count into a uniform abc bound
The primary rarity estimate #{n≤X:H(n)≤z}≪zX^{o(1)} is a population count. It does not exclude an infinite sparse exceptional sequence of products abc with large c/H. A zero-density exceptional set is compatible with violating a statement about every triple. Counting products also discards their additive factorization. **Failed rarity-to-universality route.**

<a id="q1312-a4"></a>
### A4. Mimic Mason–Stothers by differentiating the integer relation
For polynomials a+b=c, logarithmic derivatives control repeated roots and yield a radical-degree bound. Differentiating fixed integers yields zero; embedding constants into polynomials gives degree zero and no information about prime multiplicities. A polynomial specialization does not preserve a degree-vs-prime-radical lower bound. **Failed function-field transfer.**

<a id="q1312-a5"></a>
### A5. Force a+b to have only prescribed small primes by CRT
Prescribing a+b≡0 mod selected primes imposes divisibility, not smoothness: the least CRT solution can have arbitrarily large unprescribed prime factors and their radical contributes to H. Prescribing powers further grows the modulus and the least positive c. The source itself formulates a new conjectural lower bound for CRT representatives; it cannot be used as an established construction proving or refuting the main claim. **Failed smooth-abc construction.**

## Q1509 — integer-argument squarefree asymptotic in every higher degree

<a id="q1509-a1"></a>
### A1. Complete the elementary square-divisor sieve
For good primes q, ρ_f(q²)≤deg f=d. A union bound gives
#{n≤X:some q>Y,q²|f(n)}≤O_f(X/Y)+O_f(X^{d/2}/log X),
because q can reach O_f(X^{d/2}) and each residue class contributes X/q²+1. The second term is not o(X) for d≥4. Small-prime Euler-product convergence is rigorous; the large-prime-square tail is not controlled by this bound. **Failed full sieve.**

<a id="q1509-a2"></a>
### A2. Reduce every f to the proved low-degree factor class
The earlier product-transfer result applies when all irreducible factors have established asymptotics. An irreducible degree-five polynomial cannot be factored into low-degree constituents over Q by this method. More generally the exact target quantifies over irreducible high degrees. A substitution or number-field factorization changes the argument set and sieve conditions. **Failed general factor transfer; no new quartic assumption.**

<a id="q1509-a3"></a>
### A3. Sum fixed-twist integral-point finiteness
A repeated prime-square divisor leads to f(n)=q²m. For fixed m, y²=f(x)/m is a curve with finitely many integral points under appropriate genus assumptions. The cofactor m varies up to O(X^d/q²), and its curve and height bounds vary. Finiteness of each twist does not give an o(X) uniform count over all twists. **Failed fixed-curve summation.**

<a id="q1509-a4"></a>
### A4. Replace the missing tail by the conditional abc theorem
The thesis cites Granville's abc implication for squarefree values. This is a sufficient conditional route and explains the strength needed to control repeated prime factors. It does not establish abc, so it supplies no unconditional all-f theorem in this run. **Failed unconditional closure via conjectural input.**

<a id="q1509-a5"></a>
### A5. Promote averaged squarefree results to every fixed polynomial
A positive proportion or density-one result as coefficients of f vary allows exceptional polynomials, and does not fix the required local constant for each exceptional f. The thesis's coefficient-box monogeneity/squarefree applications explicitly vary parameters. Fixing one coefficient tuple is a measure-zero slice with no transferred error estimate. **Failed average-to-individual asymptotic.**

## Q1510 — prime-argument squarefree asymptotic

<a id="q1510-a1"></a>
### A1. Transfer an integer asymptotic to its prime subsequence
An o(X) exceptional set may contain all primes, whose count is O(X/log X). Thus integer squarefree density does not imply the relative prime density or its prime-specific local factors r_f(q²)/φ(q²). The retained explicit polynomial with c_f=0 illustrates the hypothesis distinction and is not a counterexample to the positive-c_f target. **Failed subsequence transfer.**

<a id="q1510-a2"></a>
### A2. Finish the sieve with prime progression distribution
Bombieri–Vinogradov reaches moduli q² roughly up to X^{1/2}, hence q roughly X^{1/4}; fixed-modulus prime distribution supplies the small-prime main term. The tail beyond that, in particular the source's Σ_X={p≤X:some q>X^{1−ε},q²|f(p)}, is not eliminated by progression distribution. An o(X/log X) polynomial-value large-square tail is still required. **Failed distribution-only sieve.**

<a id="q1510-a3"></a>
### A3. Invoke the primary's abc conditional theorem as unconditional
Pasten Theorem 1.1 assumes a specified abc theorem in each irrational-root number field, not merely local admissibility or an integer-value conjecture. Its dual varying-polynomial/prime-progression argument closes the tail under that hypothesis. The hypothesis is not proved here. **Failed unconditional theorem import; conditional scope retained.**

<a id="q1510-a4"></a>
### A4. Use the Green–Tao progression theorem directly on bad primes
If the bad-prime set had positive relative density, it would have long progressions. To contradict this one must prove that bad primes contain no such sufficiently long progression. Having p mapped to different q² and different cofactors at different progression terms does not prohibit a progression. The primary's progression exclusion uses abc; combinatorial progression existence alone supplies no exclusion. **Failed progression contradiction.**

<a id="q1510-a5"></a>
### A5. Factor over the root field and apply unit valuations
f(p)=a∏(p−α_i) allows control of prime ideals with repeated valuation outside discriminant primes. But a large squareful ideal can occur in a linear factor at a large prime argument, and individual local valuations impose no global density bound. Effective height/radical control in those root fields is the missing arithmetic step, precisely what the source assumes. **Failed ideal-factorization proof.**

## Q2904 — digits 0/1 in every base b≥6

<a id="q2904-a1"></a>
### A1. Apply the primary Fourier squarefree theorem
At x=b^L there are approximately 2^L=x^θ allowed integers, θ=log_b2<1/2. For the normalized transform F, |F|≤1 and Parseval give ∫|F|≥∫|F|²=1/|A(x)|≈x^{−θ}. The theorem demands ∫|F|≪x^{−1/2−δ}, impossible in this range. This exact size obstruction survives perfect phase estimates within that theorem. **Failed invocation of the squarefree criterion.**

<a id="q2904-a2"></a>
### A2. Upgrade known cubefree/kth-powerfree digit results
An integer with a prime exponent exactly two is cubefree but not squarefree. The source condition k>log b/log2 never permits k=2 at b≥6. Neither a kth-powerfree asymptotic nor its error term controls those exponent-two factors. **Failed exponent upgrade.**

<a id="q2904-a3"></a>
### A3. Use a one-digit or two-digit infinite family
The one-digit family b^j is squarefree for at most j=0,1. If b contains a square factor, every j≥1 already fails. The least-digit-one two-digit family b^h+1 avoids divisors of b, but its squarefreeness is a separate exponential sequence problem; no uniform tail theorem for every b has been proved. **Failed sparse explicit family.**

<a id="q2904-a4"></a>
### A4. Avoid finitely many prime squares by digital CRT
Fix a finite set of q∤b and choose a common period L with b^L≡1 mod q². Digits at positions multiples of L then determine residues through their Hamming weight, so choosing that weight prime to the selected q² gives explicit small-prime avoidance. New prime squares can still divide the resulting unbounded integer. There is no bound making the finite prime list exhaustive. **Failed finite local construction.**

<a id="q2904-a5"></a>
### A5. Regard random allowed digits as uniform residues for every square modulus
The exact transform for all L-digit words is ∏_{j=0}^{L−1}(1+e(b^jt)). For moduli sharing factors with b, residues are constrained by the lowest digits, and for square moduli exceeding b^L the set cannot be equidistributed at all. A valid sieve needs a uniform medium/large-square estimate for this sparse product measure, not independence of prime-square events. No such bound was obtained. **Failed random-digit independence proof.**

## Q2905 — infinitely many squarefree Mersenne numbers

<a id="q2905-a1"></a>
### A1. Use primitive divisors of 2^n−1
A primitive q has order n, but that alone says nothing about v_q(2^n−1)=1 or about other repeated prime factors. Squarefreeness requires every valuation≤1, much stronger than existence of one new divisor. **Failed primitive-divisor construction.**

<a id="q2905-a2"></a>
### A2. Restrict n to primes and use the order formula
q²|2^n−1 iff ord_(q²)(2)|n. For odd prime n, this order can be n. Normally ord_(q²)(2)=q·ord_q(2), which rules out many q; when q is a base-two Wieferich prime the order does not grow. Excluding every such prime with prime order n is not known here. The prime-exponent restriction is useful but not an unconditional infinite family. **Failed order-only proof.**

<a id="q2905-a3"></a>
### A3. Inductively avoid all previously found bad orders
Given a finite list of orders d_q, infinitely many prime exponents avoid their multiples. A later exponent can have a new square divisor q² with an order not in that list. There is no finite completeness certificate for all q. **Failed finite-avoidance induction.**

<a id="q2905-a4"></a>
### A4. Multiply good exponents to create larger good Mersennes
If q|2^n−1 then LTE gives v_q(2^{nq}−1)=v_q(2^n−1)+1 for odd q. Thus multiplying an exponent by a prime already dividing its Mersenne number immediately creates a square factor. The proposed closure under exponent multiplication is false; squarefree 2²−1=3 gives nonsquarefree 2⁶−1=63. **Failed multiplicative closure.**

<a id="q2905-a5"></a>
### A5. Prove positive density by a union bound over bad orders
The density of multiples of ord_(q²)(2) is its reciprocal. An elementary size bound only gives ord_(q²)(2)≥log₂(q²+1), whose reciprocal sum over primes diverges. Nor are the multiple sets independent. A useful summable order estimate or overlap theorem is missing, so the Euler-product heuristic is not a proof of positive density or infinitude. **Failed density sieve.**

## Q2906 — every zero-density set has zero-density aliquot preimage

<a id="q2906-a1"></a>
### A1. Apply a uniform bounded-fiber transfer
A bounded fiber count would transfer |A∩[1,Y]|=o(Y) at a comparable range. But s(p)=1 for every prime p, so the fiber over 1 is infinite and has count π(X)≈X/log X. This does not refute the target (primes have density zero); it refutes the uniformly bounded-fiber route. **Failed fiber bound.**

<a id="q2906-a2"></a>
### A2. Transfer via the rough size comparison s(n)≈n
Size comparison alone does not stop many n mapping into a sparse set. The function g(n)=2^{floor(log₂ n)} is within a factor two of n and maps all n into a zero-density set of powers of two. This is a counterexample to the proposed size-only transfer lemma, not to the aliquot conjecture. **Failed comparison criterion.**

<a id="q2906-a3"></a>
### A3. Extend digital equidistribution to arbitrary sparse sets
The primary proves special digit sets and logarithmic Benford laws. A zero-density A can have arbitrary locations and no cylinder/digit structure, and logarithmic distribution is weaker than the required natural density. Countably combining fixed digit patterns has no uniform error controlling an arbitrary moving set. **Failed digit-to-all-sets transfer.**

<a id="q2906-a4"></a>
### A4. Use the largest-prime linearization
For n=mp with p∤m, s(mp)=p s(m)+σ(m). For fixed m>1 this is an injective progression in p, so sparse A along that **fixed** progression can be controlled if its density restriction is sufficient. As X grows, m ranges over many values and the progressions have slopes s(m) and shifts σ(m); summing crude counts contributes an uncontrolled error for each m. m=1 also gives the constant prime fiber. A uniform averaged progression-preimage estimate is missing. **Failed fixed-m summation.**

<a id="q2906-a5"></a>
### A5. Use the known cardinality-thin-set theorem
The primary cites a result for |A∩[1,X]|≤X^{1/2+o(1)}. Natural density zero permits much larger sets, for example cardinality X/log X; it does not imply the cited square-root scale. Neither changing X nor covering A by finitely many such thin sets preserves a bound strong enough for all sparse A. **Failed quantitative-hypothesis reduction.**

## Q2907 — flat cyclotomic polynomial with five distinct odd primes

<a id="q2907-a1"></a>
### A1. Try the first five odd primes
Exact integer polynomial arithmetic gives Φ₁₅₀₁₅ degree 5760 and height 23. It is a complete rejection of that witness, not an exclusion of other five-prime choices. `CYCLOTOMIC-HEIGHT-CHECK.json` records this and smaller controls. **Failed explicit candidate.**

<a id="q2907-a2"></a>
### A2. Lift any flat lower-order polynomial by one new prime
For q∤n, Φ_(nq)(X)=Φ_n(X^q)/Φ_n(X). Flatness of Φ_n does not imply flatness of this quotient: Φ₁₅ is flat whereas Φ₁₀₅ has coefficient −2. The convolution/inverse coefficients, not only the input height, matter. **Failed generic order-raising theorem.**

<a id="q2907-a3"></a>
### A3. Preserve height by repeated-prime substitution
When q|n, Φ_(nq)(X)=Φ_n(X^q), so height is preserved. But the set of distinct prime divisors is unchanged. Starting with order at most four and repeating factors never gives the required five distinct odd primes. **Failed height-preserving construction.**

<a id="q2907-a4"></a>
### A4. Raise order using a sufficiently large prime and inverse flatness
Put Ψ_n=(X^n−1)/Φ_n. For q>n, coefficients of Φ_(nq) below q are those of 1/Φ_n=−Ψ_n/(1−X^n); in particular its first n coefficients include all coefficients of −Ψ_n. Thus inverse height>1 rules out every q>n for that n. This is a valid necessary restriction on candidate four-prime bases. It does not classify all bases with inverse height≤1 or all q≤n, nor guarantee that the higher coefficient range stays flat. **Failed complete witness/classification; preserve the exact inverse-height restriction.**

<a id="q2907-a5"></a>
### A5. Choose the final prime in a Dirichlet progression
A residue q≡a mod n controls how coefficient blocks permute, but Dirichlet only supplies primes in the class. It does not certify that every quotient coefficient is in {−1,0,1}. Without one congruence class and four-prime base whose entire quotient pattern is proved flat, infinitude in progressions supplies no witness. The generic lift counterexample above shows why coefficient cancellation must be proved separately. **Failed progression-only construction.**

## Status

Seven full catalog targets: five substantive failed routes each. No exact conjecture is closed. Elementary necessary conditions and bounded rejected witnesses have their stated domains; all prior partial marks remain.

