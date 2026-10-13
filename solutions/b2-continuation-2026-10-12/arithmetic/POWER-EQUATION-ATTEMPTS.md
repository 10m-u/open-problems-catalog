# Five full-target routes for Q1511 and Q1608–Q1611

12 October 2026. Exact setups are in QUESTION-REGISTER.md: 1≤a<b for plus, 1<a<b for minus, n,x positive. Primary [Virbalas 2606.31223](https://arxiv.org/abs/2606.31223), local `collections-5a1d8d094014fc81.txt.gz`, introduction, Lemmas 2.2–2.6, Pell section, Theorems 1.1–1.2 proofs and §6 reread. Primary [Mutlu–Le–Soydan](https://arxiv.org/abs/2301.05431), local `collections-587cafac904a8c07.txt.gz`, exact Theorems 1.1–1.3 and even-z factorization reread. Earlier B2 eight-gap repair and its precise subcase remain intact. The controls below are new bounded runs, not recovery of the missing original 10-million verification archive.

Each numbered route tries to solve the full stated target. A restricted consequence or a sufficient conditional lemma does not reset its counter. All five per target failed at full scope. These are failures of the routes, not proofs that the questions are false or impossible to solve.

## Common exact reduction and bounded controls

Let sf(v) be the product of primes of odd valuation in v. The product (a^n+σ)(b^n+σ) is a square iff sf(a^n+σ)=sf(b^n+σ). For even n=2h this gives a^n+σ=d u², b^n+σ=d v² and two solutions of X²−dY²=−σ with X=a^h,b^h. For n=3, setting X=da, Y=d²u gives Y²=d⁴u²=d³(a³+σ)=X³+σ d³. Alternatively from a³+σ=d u² the standard twist d u²=a³+σ is genus one directly. This explicit power of d matters; no incorrect fixed-d Mordell transformation is used below.

`POWER-EQUATION-CHECK.json` contains an independent sf grouping to b≤5000, reproducing the three plus and four minus listed cubic solutions, each substituted exactly; it supplies no larger exclusion than the retained prior search. It also substitutes the quartic minus exception (13,239) and checks Terai k≤100,y,z≤20. The latter is a box, with no bound on any omitted exponent.

## Q1608 — plus equation, all n≥4

<a id="q1608-a1"></a>
### A1. Quartic uniqueness followed by exponent reduction

If 4|n, write n=4h and a^n+1=d u², b^n+1=d v². The distinct positive a^h,b^h solve X⁴−dY²=−1, contradicting Ljunggren's at-most-one theorem (primary source Lemma 2.5). This is the source's rigorous whole 4|n subcase, reread rather than asserted as a new theorem. Theorem 1.2 also excludes every even n≥4 when gcd(a,b)=1. After these reductions, n≡2 mod4 with gcd(a,b)>1 and odd n≥5 remain. Neither reduction moves these exponents to a multiple of four. **Full-target failure; retain a sourced partial at this exact scope.**

<a id="q1608-a2"></a>
### A2. Use the complete common-base classification

Theorem 1.1 rules out n≥4 when a=t^r,b=t^s, including a=1. To extend this, prime-valuation vectors of arbitrary a,b would have to be proportional. For a=2,b=3 these vectors are independent; the square equation constrains a^n+1 and b^n+1, not their bases' valuations. Its same-base gcd identity gcd(t^r+1,t^s+1)=t^g+1 or 1/2 is unavailable with two bases. **Failed reduction; a new base-dependence theorem would be needed.**

<a id="q1608-a3"></a>
### A3. Use primitive divisors to force an odd unmatched valuation

A primitive divisor q of a^{2n}−1 belonging to a^n+1 has ord_q(a)=2n, subject to the usual exceptions. This proves a divisor exists; it proves neither that v_q(a^n+1) is odd nor that q does not also divide b^n+1. For any such q and b≡a mod q the second divisibility occurs, even with b>a. Avoiding squares in one factor requires an odd **unmatched** valuation in the two factors, which primitive-divisor existence does not supply. **Failed parity-of-valuations proof.**

<a id="q1608-a4"></a>
### A4. Reduce odd composite exponents to the cubic classification

For 3|n, set A=a^{n/3}, B=b^{n/3}. If Q1609 were fully proved, for n≥6 each of its three listed pairs would be excluded because neither 23,6,20 is a perfect h-th power with h=n/3≥2 in its respective pair. This gives a sufficient conditional result. It depends on the unresolved full cubic classification and says nothing about prime exponents ≥5 or n≡2 mod4 not divisible by 3. **Failed unconditional full-exponent route.**

<a id="q1608-a5"></a>
### A5. Find a universal finite congruence obstruction

For every modulus M≥2 and every fixed n≥4, the distinct bases a=M,b=2M and x=1 satisfy (a^n+1)(b^n+1)≡x² mod M. They satisfy all positivity/order hypotheses, and a=1 need not be used. Thus no finite set of congruences can exclude all pairs: combine it into its lcm M. A congruence proof can restrict actual bases and then use additional global input, but the attempted uniform finite modular contradiction is false. **Failed finite local certificate.**

## Q1609 — complete plus-cubic list

<a id="q1609-a1"></a>
### A1. Exact squarefree-kernel collision search

Group all a³+1 by sf(a³+1) and substitute each collision. The bounded run b≤5000 reproduces the exact listed pairs with kernels 2,217,889. It is finite and exact but the kernel can grow with a and no bound on b follows. The earlier reported b≤10⁷ exclusion has a missing original archive and also is finite. **Failed full search; no repetition of that earlier exclusion as a new theorem.**

<a id="q1609-a2"></a>
### A2. Compute all integral points on every fixed twist

For a fixed squarefree d, the curve d u²=a³+1 has genus one, and exact integral-point methods can find its finitely many a. The target is whether any d other than the listed collision kernels supports two a; d is unbounded. Even an effective height bound depending on d would require testing infinitely many twists. The explicit twist transformation in the common reduction confirms this is a genuine elliptic-family problem, not one elliptic curve. **Failed finite-twist reduction.**

<a id="q1609-a3"></a>
### A3. Separate the linear and cyclotomic factors

a³+1=(a+1)(a²−a+1), with gcd(a+1,a²−a+1)|3. Within one base these factors are almost coprime. Cross-base gcds are unrestricted: the actual solution (1,23) has a+1=2 dividing b+1=24. Thus treating the four factors as pairwise coprime would falsely exclude a known solution. The source's same-base quotient theorem requires proportional bases, unavailable here. **Failed independent-factor parity argument.**

<a id="q1609-a4"></a>
### A4. Put the product between successive squares

If ab is a square, write a=d u²,b=d v². The leading square is M² with M=d³u³v³, and the correction is d³(u⁶+v⁶)+1. Its ratio to the first square gap 2M+1 is approximately (u³/v³+v³/u³)/2, unbounded as v/u grows. Hence the correction is not uniformly less than one gap. If ab is nonsquare, even the leading (ab)^{3/2} is nonintegral. The proposed universal first-gap proof leaves the unrestricted ratio and approximation problem. **Failed gap bound.**

<a id="q1609-a5"></a>
### A5. Descend by the distance between bases

Set b=a+h. Expanding gives (a³+1)((a+h)³+1), a sextic in a. Fixing h produces a fixed curve and may permit a finite analysis; h=b−a is itself unbounded. The replacement h↦smaller h is not a symmetry of the equation: changing b changes its squarefree kernel. The listed solutions already have gaps 22,20,342, so no monotone uniform small-gap premise follows from the three examples. **Failed parameter descent; requires a proved h bound.**

## Q1610 — minus equation, all n≥5

<a id="q1610-a1"></a>
### A1. Import the negative-Pell quartic uniqueness proof

For minus one the simultaneous equations are X⁴−dY²=+1, not −1. The actual n=4 pair a=13,b=239 gives two distinct fourth-power Pell coordinates, verified by substitution, so the at-most-one statement used for the plus case is false in this sign. The source cites Cohn's separate complete 4|n classification: only n=4,(13,239), giving a sourced restricted exclusion for n≥5 divisible by 4. It does not address remaining odd/even exponents. **Failed full sign-transfer proof.**

<a id="q1610-a2"></a>
### A2. Obtain a uniform perfect-power classification in Pell sequences

For n=2h, equality of kernels gives a^h and b^h as X-coordinates of X²−dY²=1. Fixed d has a recurrence and perfect-power methods, but its fundamental unit varies with d and both recurrence indices are unrestricted. There is no source theorem here excluding two such h-th-power coordinates uniformly in d,h≥3. The n=4 example also cautions against excluding all two-power coordinates. **Failed uniform recurrence route.**

<a id="q1610-a3"></a>
### A3. Apply primitive-divisor existence to a^n−1

A primitive q has ord_q(a)=n (outside exceptions), but b≡a mod q makes q divide b^n−1 too. Higher q-adic lifting can also produce even valuations. Thus existence supplies neither required parity nor absence in the other factor. This is the sign-specific worked primitive-divisor reduction, with the same disclosed unmatched-valuation obstruction as Q1608 A3, not an assertion that the questions are equivalent. **Failed valuation proof.**

<a id="q1610-a4"></a>
### A4. Reduce 3|n to the complete minus-cubic list

For n=3h,h≥2, set A=a^h,B=b^h. If Q1611 were proved, each listed pair is excluded: (2,4),(2,22),(3,313),(4,22) cannot have both entries h-th powers with h≥2. The unproved cubic completeness and prime exponents ≥5 remain. **Failed unconditional exponent reduction.**

<a id="q1610-a5"></a>
### A5. Complete an exclusion using a fixed modular sieve

For every M≥2 choose a=1+M,b=1+2M,x=M. Then a,b>1 and (a^n−1)(b^n−1)≡0≡x² mod M, for every n≥5. Combining finitely many congruence tests cannot exclude all admissible bases. A successful adaptive sieve needs an additional finite global height/exponent bound. **Failed universal finite local certificate.**

## Q1611 — complete minus-cubic list

<a id="q1611-a1"></a>
### A1. Exact kernel collision search

The independent b≤5000 search gives precisely (2,4,21),(2,22,273),(3,313,28236),(4,22,819), with kernels 7,7,26,7. It checks the data and all collisions in that interval, but no proof bounds the next collision. The earlier retained b≤10⁷ claim also leaves all larger b. **Failed full exhaustion.**

<a id="q1611-a2"></a>
### A2. Use fixed-twist integral-point finiteness

d u²=a³−1 is a genus-one twist. Computing integral points at d=7,26 explains the displayed collisions; computing any finite set of twists excludes no arbitrarily large unexamined d. Effectivity for each fixed d is not a uniform finite list of d with two points. **Failed global twist route.**

<a id="q1611-a3"></a>
### A3. Force square factors separately in a³−1

a³−1=(a−1)(a²+a+1), whose same-base gcd divides 3. The actual pair (2,4) has a²+a+1=7 dividing b²+b+1=21. It therefore refutes the needed cross-base pairwise coprimality. Shared primes permit kernel cancellation between two distinct bases. **Failed cyclotomic-factor separation.**

<a id="q1611-a4"></a>
### A4. Use the first gap below the leading square

For a=d u²,b=d v² the product is M²−d³(u⁶+v⁶)+1, with M=d³u³v³. The magnitude of the correction divided by 2M−1 again grows like (u³/v³+v³/u³)/2. It is not confined to the first gap below M². The nonsquare-ab case adds a separate rational-approximation issue. **Failed uniform square-gap proof.**

<a id="q1611-a5"></a>
### A5. Apply polynomial Vieta jumping to the second base

For fixed a and x the equation reads (a³−1)b³=(x²+a³−1); as a cubic in b it has only the one real root b, with the other two multiplied by complex cube roots of unity. There is no second positive integral Vieta root that decreases b. Treating it instead as quadratic in x only gives x↦−x, which preserves both bases and yields no descent. **Failed elementary root-jump descent.**

## Q1511 — Terai uniqueness for all k>1,y,z>0

<a id="q1511-a1"></a>
### A1. Complete a direct exponent search

Exact x²=k^z−(2k−1)^y testing for 2≤k≤100 and 1≤y,z≤20 finds only (x,y,z)=(k−1,1,2). This is a finite box. Since y,z are unbounded even for fixed k, the lack of new witnesses supplies no exponent cap or uniform proof. **Failed full search.**

<a id="q1511-a2"></a>
### A2. Extend the even-z coprime factorization to all y

For z=2h, gcd(x,k)=1 and k^h±x are odd coprime positive integers. Thus k^h+x=f^y,k^h−x=g^y with f>g≥1, fg=2k−1, and 2k^h=f^y+g^y. Hence 2k^h≤(2k−1)^y+1< (2k)^y+1, so h is bounded in terms of y, not uniformly. The source's y=3,5 proof turns this into finitely many polynomial gaps; with y unbounded there are infinitely many gap polynomials and no common exclusion. Odd z is untouched. **Failed unrestricted factorization route; prior repaired subcase is not recounted.**

<a id="q1511-a3"></a>
### A3. Force a small odd exponent by modular residues

Modulo k one gets x²≡−(−1)^y: odd y gives x²≡1, even y requires −1 to be a square modulo k. These restrictions exclude some bases/exponents but allow all odd y at every k via x≡±1. For k=2 the congruence also has no parity distinction. Thus this modulus cannot force y=1. Further fixed residues for selected k are useful necessary conditions but not an exponent-independent contradiction across every k. **Failed residue reduction.**

<a id="q1511-a4"></a>
### A4. Classify the generalized norm equation by units

For odd z, put Y=k^{(z−1)/2}; then x²−kY²=−(2k−1)^y. The source parametrization uses primitive norm solutions, class-number divisors and arbitrary Pell unit powers. It still needs the second coordinate to be a pure power of k and a uniform exclusion of all y. The field, class number and fundamental unit vary with k; class-number divisibility does not bound y absolutely. Finite tests of specified norm classes do not solve this varying-field intersection. **Failed norm/recurrence route.**

<a id="q1511-a5"></a>
### A5. Turn density-one exclusions into a universal theorem

The source's divisor criterion d|2k−1, d≡±3 mod8 excludes y=3,5 for many k. An exceptional k can remain: k=4 has 2k−1=7 and positive divisors only 1,7, neither ±3 mod8. Even if the excluded set has density one, it need not contain every k and it covers only two y. Uniform Terai uniqueness therefore requires an independent treatment of exceptional bases and all other exponents. **Failed density-to-universality proof.**

## Filing boundaries

Q1608's 4|n and even coprime subcases are primary-source results whose proofs/reductions were reread. Q1610's 4|n exclusion is a source-cited classification, not independently reproved here. Cubic controls do not strengthen the older numerical bounds. Terai gap results retain their repaired original scope. All five full targets stop after five substantive failed routes; exact conjectures remain open.

