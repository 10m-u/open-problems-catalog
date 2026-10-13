# Diophantine tuple routes: Q1903–Q1908 and Q2306

12 October 2026. Primary [Dujella open problems](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf), cached 5 October text `collections-fb24239be0f27fe6.txt.gz`, Problems 1.3–1.5,1.11,1.15,3.1–3.2 reread. Current primary supplement also consulted during this run. These exact questions remain open there. The following are worked constructions/reductions with explicit failures, not a claim that a finite local test settles existence.

`check_tuples.py` / `TUPLE-CHECK.json` verify the source sextuple and almost septuple, the corrected almost strong quadruple, all K₃,₃ candidates with six entries≤300, mixed-sign regularity extensions with a,b,c≤300 and d≤5000, and the five displayed integer x for (1,55,276). These bounded domains leave all omitted heights open.

The almost strong example uses **2223/30464**, verified in the original [Dujella–Petričević 2008 paper §5](https://web.math.pmf.unizg.hr/~duje/pdf/strong2.pdf). The cached supplement extraction has 2223/3046, which fails several conditions. This is a recorded extraction discrepancy; no question statement is changed.

## Two auxiliary exact reductions

For a fixed rational sextuple a₁,…,a₆, simultaneous y_i²=a_i x+1 forms a degree-64 multiquadratic cover of P¹. Distinct nonzero a_i give six finite branch points and ∞, each inertia 2. Riemann–Hurwitz yields 2g−2=−128+7·32=96, so g=49. This explains why freely adjoining a seventh rational element is not an elliptic group-law operation. x=0 supplies a trivial rational point but is forbidden as a tuple element.

For nonzero rational sets A={a_i},B={b_j}, there is a rational L such that every La_i and b_j/L is integral **iff all a_i b_j are integral**. At each prime ℓ the necessary and sufficient interval for v_ℓ(L) is
max_i(−v_ℓ(a_i)) ≤ v_ℓ(L) ≤ min_j v_ℓ(b_j).
It is nonempty exactly when v_ℓ(a_i b_j)≥0 for every i,j; choose exponents independently, with finitely many nonzero. This scaling preserves cross products and hence their square-plus-one conditions. To obtain Q1906 one must additionally ensure positivity and that all six resulting integers are distinct; the criterion alone does not guarantee that. The checked Piezas sextuple has no 3+3 partition with all cross products integral, so it cannot provide even the integrality prerequisite by this two-sided scaling. This exact rescaling criterion is useful partial methodology, not a new K₃,₃ existence or nonexistence theorem.

## Q1903 — rational septuple

<a id="q1903-a1"></a>
### A1. Complete the known almost septuple
For {243/560,1147/5040,1100/63,7820/567,95/112,38269/6480,196/45}, exactly the last pair fails: its product plus one is 1948081/72900, not a square. The checker substitutes all 21 pairs. Deleting one of those elements gives a sextuple, but repairing that pair while holding the other five fixed imposes six simultaneous equations on its replacement. The existing almost witness is not a septuple. **Failed direct witness.**

<a id="q1903-a2"></a>
### A2. Adjoin a seventh by elliptic multiplication
The three-condition curve y²=(a₁x+1)(a₂x+1)(a₃x+1) is genus one, but a square product does not ensure that each factor is square. Even points satisfying the first three individual conditions need three more. The full fixed-sextuple cover has genus 49 as computed above, with no elliptic addition law. **Failed group-law extension.**

<a id="q1903-a3"></a>
### A3. Convert fixed-sextuple finiteness into uniform nonexistence
Faltings makes the rational points on each genus-49 extension curve finite. It gives neither emptiness of its nontrivial extension points nor a finite list of all rational sextuples to test. In particular x=0 is already a rational point. No effective uniform height bound or all-sextuple classification follows. **Failed global finiteness route.**

<a id="q1903-a4"></a>
### A4. Clear denominators and import the integer quintuple exclusion
Scaling all elements by D changes a_i a_j+1 to D²a_i a_j+1; the old square scales to D²(a_i a_j+1), which differs by D²−1. Clearing denominators thus produces a D(D²)-tuple, not a D(1)-tuple. Integer quintuple nonexistence cannot exclude rational septuples by this operation. **Failed integral transfer.**

<a id="q1903-a5"></a>
### A5. Use generic square-value density to choose a common extension
For one a, x=(t²−1)/a supplies infinitely many rational extensions. Substitution into a second gives a conic; further independent square conditions double the multiquadratic cover. Density or infinitude for each separate condition does not guarantee an intersection, as the genus-49 calculation quantifies. A simultaneous rational-point construction or descent is missing. **Failed independent-conditions construction.**

## Q1904 — rational sextuple with two integer elements

<a id="q1904-a1"></a>
### A1. Use the known one-integer sextuple
The checked Piezas set is {34440,23001/280,840/68921,1121/11480,19383/1640,2530/287}. Every pair works, but only 34440 is integral after reducing the fractions. None of its other denominators is 1. **Failed direct witness.**

<a id="q1904-a2"></a>
### A2. Scale that sextuple to make another element integral
Uniform scaling does not preserve the +1 condition, by the exact D²−1 discrepancy above. Multiplying by a common denominator yields the wrong D parameter, irrespective of how many elements become integers. **Failed common-denominator construction.**

<a id="q1904-a3"></a>
### A3. Apply a fractional-linear transformation to create two integers
For a_i'=(a_i+t)/(1−t a_i),
a_i'a_j'+1=(1+t²)(a_i a_j+1)/[(1−t a_i)(1−t a_j)].
Making two transformed entries integers does not make the new quotient factors rational squares. A sufficient repair requires 1+t² and all six denominators 1−t a_i to be squares, plus nonzero/distinctness. That is another simultaneous square-value problem; solving the two integrality equations alone is insufficient. **Failed automorphism claim.**

<a id="q1904-a4"></a>
### A4. Start with a two-integer pair and regular extension
The regular construction takes ab+1=r² and c=a+b+2r; then ac+1=(a+r)²,bc+1=(b+r)². It builds a triple while preserving the integer pair, and its regular fourth element builds a quadruple. Iterating this formula preserves only the chosen pair/triple conditions, not every edge to all existing elements. It supplies no fifth and sixth rational elements simultaneously adjacent to all four. **Failed unrestricted regular iteration.**

<a id="q1904-a5"></a>
### A5. Use elliptic rational infinitude to meet integrality
An extension variable on a positive-rank elliptic curve has infinitely many rational points, but imposing that one coordinate be an integer restricts to integral/S-integral points, which are finite on a fixed curve. Infinitude of rational points therefore cannot by itself force another integer entry. Here a varying family with an integral section satisfying all sextuple conditions is needed. **Failed rank-to-integrality implication.**

## Q1905 — strong rational quadruple

<a id="q1905-a1"></a>
### A1. Complete the source's almost strong example
With the corrected denominator, {140/51,2223/30464,278817/33856,3182740/17661} satisfies nine conditions and fails a₃a₄+1=459627303/309488. Exact numerator/denominator square tests reject it. Nine of ten conditions do not solve the tenth. **Failed witness.**

<a id="q1905-a2"></a>
### A2. Parametrize each diagonal and assume cross conditions follow
a=2t/(1−t²) makes a²+1=((1+t²)/(1−t²))². Four independent t's do not force cross squares: a=3/4 and b=4/3 both satisfy the diagonal and are distinct, but ab+1=2 is nonsquare. The six cross equations remain. **Failed diagonal-only construction.**

<a id="q1905-a3"></a>
### A3. Extend a fixed strong triple on an elliptic curve
To adjoin d one needs d²+1 and three independent a_i d+1 all square. The multiquadratic degree-16 cover has the three linear finite branch points, ±i from d²+1 and ∞, generically six, so 2g−2=−32+6·8=16 and g=9. Solving just the product's elliptic equation discards the diagonal and individual square classes. **Failed elliptic extension route.**

<a id="q1905-a4"></a>
### A4. Use an ordinary rational sextuple containing a strong pair
A strong pair guarantees two diagonals and its edge. Taking any additional two elements of a sextuple guarantees their cross edges but no diagonals at those elements. Diagonal constraints a_i²+1 are absent from the ordinary tuple definition, including the strong-pair family in the source. A separate two-diagonal construction remains necessary. **Failed tuple-to-strong transfer.**

<a id="q1905-a5"></a>
### A5. Force all ten conditions by one global scaling
For a fixed ordinary quadruple scaled by L, the ten requested values are L²a_i a_j+1. Rational L must satisfy ten square equations simultaneously; the diagonal ones alone form intersections of four conics, not an automatic scale normalization. L=0 solves all equations but violates nonzero/distinctness, while L=±1 need not satisfy the diagonals. No nontrivial common rational L has been constructed. **Failed scaling route.**

## Q1906 — integral K₃,₃

<a id="q1906-a1"></a>
### A1. Exhaust a finite positive-integer graph
The exact graph on [1,300] has no triple of left vertices with three distinct outside common neighbors: all binom(300,3) left triples are checked by bitsets. This rules out K₃,₃ with all six entries in that interval only. There is no proved largest-entry bound. **Failed full finite search.**

<a id="q1906-a2"></a>
### A2. Rescale a rational sextuple across a 3+3 partition
The exact valuation criterion above is necessary and sufficient for this construction's integrality. All ten partitions of the source sextuple fail it because at least one cross product is nonintegral. Even a partition satisfying it would require six distinct positive scaled values. **Failed source-sextuple construction; preserve the exact criterion.**

<a id="q1906-a3"></a>
### A3. Extend the known K₂,t construction by a third left vertex
A K₂,t construction solves two Pell conditions for each right value. A third a imposes a b_j+1 squares simultaneously at three chosen b_j. These are three new constraints on a, not consequences of the old two rows. Having infinitely many common neighbors of two vertices does not guarantee a third vertex adjacent to three of them. **Failed unrestricted bipartite extension.**

<a id="q1906-a4"></a>
### A4. Import integer K₅ nonexistence
K₃,₃ imposes nine cross edges, while a six-element Diophantine tuple imposes all fifteen edges. Its within-part triples can have nonsquare products. K₃,₃ contains no K₅ as a graph, so the known K₅ exclusion has no logical application without six additional within-part equations. **Failed graph implication.**

<a id="q1906-a5"></a>
### A5. Make every cross product a square before adding 1
Taking a_i=u_i²,b_j=v_j² makes a_i b_j=(u_i v_j)², but the next value (u_i v_j)²+1 lies strictly between that square and (u_i v_j+1)² for positive integers. Hence this entire tempting construction is impossible. Allowing common factors returns to Pell equations rather than fixing it. **Failed square-product construction.**

## Q1907 — six integer points on a product cubic

<a id="q1907-a1"></a>
### A1. Extend the displayed five-point example
The checker substitutes x=4,8,17,89,4870844 for (a₁,a₂,a₃)=(1,55,276), giving five distinct positive points. The explicit family supplies only those five expressions; none supplies a sixth. Enumerating the five does not certify a new witness. **Failed direct construction.**

<a id="q1907-a2"></a>
### A2. Use all multiples of a rational non-torsion point
On the cubic, rational group-law multiples usually have nontrivial denominators. For a fixed integral model, Siegel gives finitely many integral points; positive rank does not force six integral x. Integral x also may be ≤0, excluded here. **Failed rank-to-six-integral-points argument.**

<a id="q1907-a3"></a>
### A3. Clear the denominators of six rational x simultaneously
Changing variable x=X/D gives factors (a_i X+D)/D and product denominator D³. Clearing its square denominator does not normalize the three constant terms to 1 with positive integer coefficients unless additional divisibilities hold. Scaling coefficients to keep a_i x unchanged changes integrality of the new x in the opposite direction. The model's three prescribed intercepts are a genuine obstruction. **Failed coordinate-scaling construction.**

<a id="q1907-a4"></a>
### A4. Count triple extensions as product-square points
Individual-square extensions are sufficient product-square points, but a positive integral Diophantine triple has no generic sixth simultaneous extension (integer tuple-size theorems prevent freely adjoining many). Product-square points can instead have three nonsquare factors with canceling squarefree kernels. A method restricted to ordinary tuple extensions does not explore this necessary extra class. **Failed extension-only enumeration.**

<a id="q1907-a5"></a>
### A5. Use the five-point Pell family to force a sixth by infinitude
The source family a=(1,12t+7,12t²+19t+8), s²=33t²+46t+17 gives five explicit x, including (21t+13±3s)/2. The Pell condition guarantees their stated square products, but a sixth x would impose a new equation on t. Infinitely many Pell t's do not force that equation, and the five formulas stay five even at large t. **Failed family-infinitude deduction.**

## Q1908 — regularity of mixed D(−1)/D(1) extensions

<a id="q1908-a1"></a>
### A1. Seek a small nonregular extension
The checker intersects exact square-plus-one extension sets at a,b,c≤300 and d≤5000 for every distinct D(−1) triple in that box. All checked extensions satisfy the proposed identity. This finite test does not bound any coordinate of a counterexample. **Failed full witness/exclusion search.**

<a id="q1908-a2"></a>
### A2. Obtain the identity from square constraints by expansion
The difference between its two sides expands to
a²+b²+c²+d²+2d(a+b+c)−2(ab+ac+bc)−4abcd+4.
Knowing six separate numbers are squares imposes six equations with six independent square-root variables; eliminating their squares does not set this polynomial to zero. A nontrivial relation between the roots is still required. The displayed polynomial is symmetric in a,b,c, so reordering cannot create a counterexample either. **Failed tautological elimination.**

<a id="q1908-a3"></a>
### A3. Use Vieta descent on the proposed identity
If the identity already holds, its quadratic in d permits a second regular root and descent. For an arbitrary extension its satisfaction is the target itself; using that quadratic as a premise is circular. The simultaneous Pell equations do not by themselves force d to be one of those two roots. **Failed unconditional regular-root jump.**

<a id="q1908-a4"></a>
### A4. Extend the proved special families to all triples
The primary supplement lists affirmative results for {1,2,c}, Fibonacci triples and {1,k²+1,k²+2k+2}. A general D(−1) triple need not have a=1 or those prescribed recurrences. No reduction of every triple to one of these families is given by their pairwise square conditions. **Failed family classification route.**

<a id="q1908-a5"></a>
### A5. Transfer ordinary D(1) quadruple regularity by a sign change
Replacing a,b,c by negatives preserves their pairwise products, so ab−1 remains a minus-one square condition; it does not become ab+1. Scaling all three would change the D parameter to a negative square multiple rather than +1. Thus there is no rational sign/scale map of this problem to ordinary quadruple regularity with the same d. **Failed sign-transfer proof.**

## Q2306 — an imaginary-quadratic integral D(1) quintuple

<a id="q2306-a1"></a>
### A1. Embed and clear a rational quintuple
A rational algebraic integer is an integer. Enlarging Q to an imaginary quadratic field cannot make the denominators of rational tuple elements integral. Clearing them again changes D(1) to D(D²). **Failed rational embedding construction.**

<a id="q2306-a2"></a>
### A2. Specialize a universal polynomial quadruple and iterate
{u−1,u+1,4u,16u³−4u} is a polynomial D(1) quadruple and specializes integrally at u∈O_K. It has only four elements. Its rational fifth-extension formulas need division by nonunit denominators; O_K does not contain inverses of arbitrary algebraic integers. No fifth integral specialization has been constructed. **Failed regular-quadruple iteration.**

<a id="q2306-a3"></a>
### A3. Reduce to rational integer elements
If a rational integral tuple had mixed signs, a positive-negative product plus 1 is ≤0, and can be a rational square only when that product is −1; this permits just the pair {1,−1}, with no distinct third nonzero integer. All-five-same-sign would give a positive integer quintuple after absolute values, excluded by the classical integer theorem. This exhausts the rational-elements subcase, not algebraic nonrational elements. **Failed full-field reduction.**

<a id="q2306-a4"></a>
### A4. Take pure imaginary elements and use complex squares
For a_i=s_i√(−D), a_i a_j+1=1−D s_i s_j∈Q. A rational number q is a square in Q(√−D) exactly when q is a rational square or q=−D times a rational square: writing (u+v√−D)² shows uv=0. Arbitrary negative q is therefore not automatically a field square. Nine/ten independent products still have specific square classes, and s_i must satisfy ring integrality. **Failed “negative means square” construction.**

<a id="q2306-a5"></a>
### A5. Use the recent uniform quadratic-field tuple bound
The primary source's recent degree-dependent tuple-size bound permits cardinalities far larger than five. A finite upper bound, even in every quadratic field, proves neither existence nor exclusion at size five. Its height/Subspace-Theorem input supplies no classified list of every imaginary-quadratic quintuple. **Failed bound-to-existence/emptiness deduction.**

## Terminal interpretation

Seven targets, five substantive failed routes each. Numerical exclusions and auxiliary cover/scaling calculations retain their exact domains. The full existence and regularity questions remain mathematically open.

