# Q3107/Q3109/Q3110: consecutive multiplicative dependencies

Read primary sources: the 2024 West Coast problem list, `texts/papers/collections-537a4f597ee374ec.txt.gz`, and Bennett–Pink–Vukusic, `texts/papers/collections-04189765ac775005.txt.gz`, introduction, Theorems 1.2, 1.3, 1.7 and Definition 1.5. Dependence of a triple is valuation-matrix rank at most two. **3-dependence also requires every pair to have rank two.** Neither rank≤2 nor three perfect powers by themselves meet that stronger condition.

[SHIFT-CHECK.json](SHIFT-CHECK.json) records exact ranks for the eight source examples and the excluded power family. [SHIFT-BOX-CHECK.json](SHIFT-BOX-CHECK.json) exhausts 1<a<b<c≤200: 1,293,699 triples, five witnesses to two consecutive 3-dependencies, and none to three. The finite domain is not an infinity or unbounded nonexistence result.

## A source-case correction and a useful a=2 exclusion

Theorem 1.3 states an implication whose allowed cases include (2,6,16). Its shift (3,7,17) is independent by unique prime valuations. Thus it is not a witness to the theorem's premise. This extraneous permitted case does **not** refute an if-then classification. It must not be counted as an example.

The same theorem does exclude all a=2 possibilities for Q3110: the (2,8,c) family already has a dependent initial pair; in the other family

    (2,2^x−2,2^(2x)−2^(x+1)), x≥3,

the shift-one last entry is (2^x−1)², so its last pair is dependent. The isolated (2,4,14) and (2,6,16) likewise have an initial dependent pair. Hence **no Q3110 witness has minimum entry 2**, conditional only on the cited established classification, without an independent reproof of that classification.

<a id="q3107-a1"></a>
## Q3107 A1 — Search exact valuation ranks for an infinite pattern

The complete box gives (7,23,161), (9,49,63), (10,32,80), (12,24,64), (16,50,80). Each is 3-dependent at shifts zero and one, with pairs checked separately. They have differing kernels and powers; no parameter formula maintaining both valuation relations follows. The algorithm proves finite examples, not infinitely many. **Failed bounded pattern search.**

<a id="q3107-a2"></a>
## Q3107 A2 — Use the elementary c=ab product family at both shifts

The initial relation is automatic and can be minimal when a,b are independent. Requiring the same simplest shifted relation c+1=(a+1)(b+1) gives ab+1=ab+a+b+1, hence a+b=0, impossible for positive a,b. Raising the shifted product to a positive integer power only increases its already-too-large value. Different exponents or orientations are still possible, but not supplied by this two-product construction. **Failed matching-product family.**

<a id="q3107-a3"></a>
## Q3107 A3 — Import the known infinite three-shift families

For (2,8,c), the initial pair is dependent, and for the power family above the shift-one pair is dependent. These are genuine dependent families, but they never satisfy both required minimality conditions. Infinitude at the weaker rank condition does not transfer. **Failed known-family transfer.**

<a id="q3107-a4"></a>
## Q3107 A4 — Preserve a witness by taking common powers

If (a,b,c) is minimally dependent, (a^r,b^r,c^r) keeps the exact valuation ranks at shift zero. Its shifted entries are a^r+1,b^r+1,c^r+1 rather than powers of a+1,b+1,c+1. For r=2 on the witness (7,23,161), the shifted triple is (50,530,25922): prime 53 occurs only in 530 and prime 13 only in 25922, then 50 has its own remaining relation, giving rank three. Thus the proposed universal powering operation does not preserve the target. A different exponent family requires new identities. **Failed witness-powering extension.**

<a id="q3107-a5"></a>
## Q3107 A5 — Keep a finite prime basis throughout a construction

If all six numbers a,b,c,a+1,b+1,c+1 are units over one fixed finite prime set S, each equation (u+1)−u=1 is a two-variable nondegenerate S-unit equation. The [Evertse–Schlickewei–Schmidt theorem](https://annals.math.princeton.edu/2002/155-3/p04) makes its solution set finite. Therefore the fixed-basis construction can produce only finitely many triples. An infinite solution may use unbounded prime support, but the proposed constant-prime-basis parameterization cannot. **Failed fixed-support construction.**

<a id="q3109-a1"></a>
## Q3109 A1 — Use the explicit power family

At shifts zero, one, two, the power family has profiles 3-dependent, 2-dependent, 2-dependent. It is infinite, but the exact question explicitly excludes every such triple. Reparametrizing x does not remove the exclusion. **Failed excluded-family construction.**

<a id="q3109-a2"></a>
## Q3109 A2 — Vary b,c while fixing one a≥3

The source's Theorem 1.2 proves effective finiteness for every fixed a≥3, with bounds depending on a. Thus no such fixed-minimum construction can give infinitude. Combining the results over all a gives a countable union of finite sets, which may be infinite or finite; it does not answer the question. Any successful new infinite family must have unbounded a. **Failed fixed-a infinity route.**

<a id="q3109-a3"></a>
## Q3109 A3 — Scale a source witness

Scaling preserves dependence at zero but does not commute with shifts. On (3,6,48), scaling by 2 gives (6,12,96); its shift one is (7,13,97), three distinct primes, hence independent. This exact counter-control rejects a universal scaling operation. It leaves open isolated successful multipliers or a more structured scaling theorem, neither constructed here. **Failed scaling-family route.**

<a id="q3109-a4"></a>
## Q3109 A4 — Make all three shifts pair-dependent

Theorem 1.7 classifies these as (2,6,8), (2,8,2^x−2) with x≥4, or (2,8,10^y−2) with y≥2. The two infinite families violate the explicit (a,b)≠(2,8) condition, leaving only one triple. Consequently an admissible infinite family cannot be entirely 2-dependent at every shift; it needs at least one genuinely 3-dependent shift. **Failed fully pair-dependent construction.**

<a id="q3109-a5"></a>
## Q3109 A5 — Extend the source's finite exceptional examples

Use the source witness (6,30,216) to derive the template a=t, b=t²−t, c=t³. Shift zero is dependent through a,c, and shift one has c+1=(t+1)(b+1), so dependence holds identically. The witness's shift-two relation is (b+2)³=(a+2)^5. Retaining this fixed exponent relation gives

    (t²−t+2)³−(t+2)^5
      =(t−6)(t^5+2t⁴+11t³+13t²+16t+4).

The second factor is positive for t>0, so this specific relation permits only t=6. This concrete polynomial family does not produce infinitude. Allowing its shift-two exponent vector to vary leaves a new exponential equation, which is not solved by the fixed-template construction. **Failed exceptional-seed polynomial family.**

<a id="q3110-a1"></a>
## Q3110 A1 — Check the established examples for a witness

The eight displayed source examples are all dependent at each shift, but their exact profiles include at least one 2-dependent shift. The (2,6,16) permissive source case is not even dependent at shift one. None is a Q3110 witness. This resolves these candidate tests without making an all-size claim. **Failed source-example construction.**

<a id="q3110-a2"></a>
## Q3110 A2 — Use the rank determinant as the only search predicate

The Gram determinant being zero detects rank≤2. In the excluded power family, that determinant vanishes at all three shifts while a pair is dependent at each later shift. A valid witness additionally requires all pair Gram determinants positive at every shift. The stronger exact predicate was implemented in the complete 200-box and found no witness. **Failed rank-only construction and bounded corrected search.**

<a id="q3110-a3"></a>
## Q3110 A3 — Start with a=2 and solve its remaining equations

The source classification plus the displayed minimality analysis proves no a=2 witness, with b,c unbounded. This is a complete useful boundary result, but excludes only one minimum value; it does not close the existence problem for a≥3. **Failed full-target construction at a=2; sourced partial retained.**

<a id="q3110-a4"></a>
## Q3110 A4 — Use fixed-a effective finiteness to prove global nonexistence

Theorem 1.2 bounds candidate b,c for a fixed a≥3, but its conclusion allows a nonempty finite candidate set. Exhausting finitely many a cannot certify all a. No uniform cutoff or descending map reduces every candidate to a previously checked minimum. This attempt is logically different from Q3109's fixed-a infinity attempt: here it seeks an all-a exclusion from the individual bounds. **Failed finiteness-to-nonexistence route.**

<a id="q3110-a5"></a>
## Q3110 A5 — Impose one common product relation at every shift

The construction c=ab already fails at the next shift if c+1=(a+1)(b+1); a+b=0 is incompatible with the ordered positive domain. At three shifts, choosing a single common exponent vector instead leads to simultaneous exponential equations and no automatic translation invariance of multiplicative relations. A genuine witness may use three different relation vectors. No consistent construction with those different kernels is obtained. **Failed common-kernel product construction.**

The three exact catalog targets each reach five failed routes. The fixed-a and a=2 boundary statements and finite example lists have their stated scopes; no infinity or all-size existence/nonexistence conclusion is filed.
