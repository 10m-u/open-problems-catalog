# Torsion and unit routes: Q2307–Q2309, Q2010–Q2011, Q3603

12 October 2026. Primary Dujella supplement (Problems 2.2–2.3,3.8), [Lorenzini 2024](https://dinolorenzini.franklinresearch.uga.edu/sites/default/files/Lorenzini2024August1.pdf) introduction, §4.1–4.10, Questions 7.5,7.9, and [Visser–Ziegler](https://arxiv.org/abs/2608.15903) introduction, Conjecture 1, unit-matching setup and Lemmas 5–6 reread locally. Every exact statement and setup remains as in QUESTION-REGISTER.md. No rank computation or missing software installation is counted as a solve attempt.

## A concrete C₂×C₈ model

Put t=(v²−1)/(2v), u=t² and E_v:y²=x(x+1)(x+u²), omitting v=0 and the finitely many singular cases u=0,1. The rational point Q=(u,u(u+1)) doubles to the two-torsion point (0,0). Indeed the tangent doubling formula gives x(2Q)=0. Since u=t² and u+1=((v²+1)/(2v))², the three differences between x(Q)=u and the roots 0,−1,−u² are squares. The standard full-two-torsion halving criterion gives a rational half of Q of order 8. Together with full two-torsion, Mazur's classification yields exactly C₂×C₈ in this nonsingular rational family. These points are torsion; this calculation does **not** give positive rank. No novelty claim.

## Q2307 — a rank-exactly-four curve with this torsion

<a id="q2307-a1"></a>
### A1. Count four visible rational points on the model
The roots give three order-two points, Q has order four, and its rational halves have order eight. Four or more displayed points therefore lie in the finite torsion group and give no rank lower bound. Independence modulo torsion, not the number of affine points, is required. **Failed direct four-point construction.**

<a id="q2307-a2"></a>
### A2. Twist a high-rank curve while preserving eight-torsion
A nontrivial rational quadratic twist preserves the root locations but changes the halving square classes. The order-four point at x=u would require the ordinate u(u+1)/√d in y²=d x(x+1)(x+u²), rational only when d is a rational square. Thus the standard visible eight-torsion chain is lost on a nonsquare twist; a high-rank twist cannot be imported without a new torsion verification. **Failed rank-by-twisting route.**

<a id="q2307-a3"></a>
### A3. Import high-rank families with C₈ or C₂×C₆ torsion
C₈ has one nontrivial rational two-torsion point, whereas the target has three; C₂×C₆ contains rational three-torsion absent from the target. Rational isomorphisms preserve torsion and rank. These other high-rank families cannot be relabeled as C₂×C₈, and a base change to a quadratic field violates E/Q. **Failed torsion-group transfer.**

<a id="q2307-a4"></a>
### A4. Force an additional point in a known rank-three specialization
On the concrete model, x=1 demands y²=2(1+t⁴). This is a new genus-one condition on t, not automatic from t²+1 square; the two simultaneous conditions have to be solved along with independence from three existing points. Rationality alone would yield rank≥4 at most, not rank=4 without an upper bound. No fourth independent point satisfying this specialization has been constructed. **Failed forced-section route.**

<a id="q2307-a5"></a>
### A5. Use a predicted rank jump to certify existence
Root number −1 or +1, even with a parity theorem, constrains rank only modulo two. A curve with even parity may have rank zero or two. An analytic rank estimate also needs a certified identification with algebraic rank or independent point construction. Thus parity or a heuristic expected rank-four specialization supplies no exact witness or rank upper bound. **Failed parity/existence route.**

## Q2308 — infinitely many rank-at-least-two Q-isomorphism classes

<a id="q2308-a1"></a>
### A1. Count the torsion sections as two independent sections
The preceding E_v construction has multiple rational sections, but all those explicitly guaranteed by halving are torsion. Their specialization remains torsion; no rank-two subgroup is obtained. **Failed generic-rank construction.**

<a id="q2308-a2"></a>
### A2. Duplicate the known rank-one section by group operations
If P has infinite order, P+T,−P and mP for torsion T and integer m all have the same rational span modulo torsion. Choosing two distinct such points yields a rank-one subgroup. An independent second section is still needed. **Failed second-section construction.**

<a id="q2308-a3"></a>
### A3. Specialize a single rank-two curve infinitely often
Changing a Weierstrass model by x=c²X+r,y=c³Y+… changes coefficients but preserves its Q-isomorphism class and j-invariant. Infinitely many presentations of one curve therefore do not meet the target. A parameter with nonconstant j and two independent sections would suffice via specialization, but neither is supplied by model changes. **Failed infinite-class construction.**

<a id="q2308-a4"></a>
### A4. Choose infinitely many even-parity fibers of a rank-one family
Conditional on algebraic-rank parity, a **certified** infinite set of even-parity smooth fibers retaining a non-torsion section would force rank≥2. The source's existence of a rank-one family does not prove that root-number sign occurs infinitely often in it, nor that j varies along the proposed restricted set. The required sign-distribution/specialization argument has not been obtained. **Failed conditional-to-unconditional infinitude route.**

<a id="q2308-a5"></a>
### A5. Impose a second square-value section and assume infinitely many parameters
For E_v the x=1 condition y²=2(1+t⁴) must coexist with t²+1 square. The fiber product is a degree-four cover branched at the two roots of t²+1 and the four roots of 2(1+t⁴), with disjoint branch loci; Riemann–Hurwitz gives 2g−2=−8+6·2=4, hence g=3. There are only finitely many rational t on this fixed cover by Faltings. This particular section-forcing scheme cannot yield infinitely many parameter values, even before checking independence. **Failed infinite forced-section construction.**

## Q2309 — positive integer Diophantine triple inducing C₂×C₆

<a id="q2309-a1"></a>
### A1. Use the regular integer triple family
For ab+1=r², c=a+b+2r gives a triple. The current supplement cites Adžaga 2608.01057 proving C₂×C₆ impossible on regular triples. Thus the regular construction itself cannot supply a witness, and that restricted theorem does not classify all positive integer triples. **Failed regular-family construction.**

<a id="q2309-a2"></a>
### A2. Infer six-torsion from full two-torsion and the point (0,1)
Every nonsingular induced curve has three rational roots −1/a,−1/b,−1/c and the rational point (0,1). Full two-torsion does not imply a rational point of order three; (0,1) need not be three-torsion. After X=abc x,Y=abc y, the monic cubic is Y²=(X+ab)(X+ac)(X+bc). A three-torsion point must additionally solve its degree-four three-division polynomial. **Failed automatic torsion inference.**

<a id="q2309-a3"></a>
### A3. Use a rational induced C₂×C₆ curve and clear its triple denominators
Scaling a,b,c by D changes each required product-plus-one by D²−1. It also changes the induced branch roots and the curve in general, so an existing rational triple does not become a positive integer triple with the same torsion. **Failed integral transfer.**

<a id="q2309-a4"></a>
### A4. Set the three-division polynomial root equal to the visible point
For Y²=X³+A X²+B X+C, ψ₃(X)=3X⁴+4A X³+6B X²+12C X+(4AC−B²). At X=0, order three requires 4AC=B². Here A=ab+ac+bc, B=abc(a+b+c), C=(abc)², so it requires 4(ab+ac+bc)=(a+b+c)². This is an explicit extra Diophantine equation, not implied by ab+1,ac+1,bc+1 square. It excludes many triples but does not prove other rational three-torsion roots are impossible. No positive integral triple satisfying it has been constructed. **Failed visible-point route.**

<a id="q2309-a5"></a>
### A5. Parametrize C₂×C₆ first and factor its branch differences
A torsion normal form supplies three rational branch roots. Recovering a,b,c from ab,ac,bc requires a²=(ab)(ac)/(bc), then positive **integer** a,b,c and all three pair-products plus one square. Rational branch factorization does not force those square and integrality conditions. The inverse map leaves a nontrivial square-class/valuation intersection; no integer specialization has been produced. **Failed torsion-normal-form construction.**

## Q2010 — M(K)≥(N−1)/2 for every N-special prime N≥29

<a id="q2010-a1"></a>
### A1. Extend the finite raw-form factor tables uniformly
The source proposes the explicit exceptional sequence 0,1,x₃,…,x_(N−1)/2 in Tate normal form. Its §4.4 sufficient polynomial properties require F_N monic in r with constant term ±s^a, its top s coefficient ±r^b, and controlled divisors of x_i−x_j. The tables verify only bounded indices (the stated theorem reaches M≥11 for 23≤N≤101). Increasing that table finitely still leaves arbitrarily large N. **Failed universal table induction; no established recurrence proving all boundary coefficients.**

<a id="q2010-a2"></a>
### A2. Use the general division-polynomial difference identity
On a fixed Weierstrass curve,
x(mP)−x(nP)=−ψ_(m+n)(P)ψ_(m−n)(P)/(ψ_m(P)²ψ_n(P)²)
up to the standard n-sign convention. This controls divisors and is the right general group-law mechanism. It does not by itself prove that the source's normalized r,s and every needed factor are global units on every N-special curve; integrality of the normalized Tate coordinates is required first. Thus the formula reduces one obligation but leaves the local cusp/valuation analysis behind §4.4(1)–(2). **Failed full unit-sequence proof.**

<a id="q2010-a3"></a>
### A3. Use torsion reduction to make all x-coordinate differences units
Distinct mP in characteristic zero may meet in reduction at bad places or after the normalization x↦x/b. N∤c controls the component-group order, not every denominator of x/b. Even when points in the identity component reduce distinctly, proving x/b integral and differences units needs an integral minimal/group model compatible with b. That compatibility is precisely the source's local claims (a)–(d), proved there with boundary coefficients in the known range. **Failed denominator-free reduction argument.**

<a id="q2010-a4"></a>
### A4. Import the everywhere-potentially-good theorem
The source states Mestre proves the lower bound when j(E) is integral. N-special curves can still have split multiplicative reduction of type I_m with m prime to N; N∤c does not rule out those places. Thus the general hypothesis does not imply j integral. The remaining multiplicative places are outside that input. **Failed hypothesis reduction.**

<a id="q2010-a5"></a>
### A5. Deduce a large clique from many exceptional units
Finding many units u with 1−u unit gives many triangles {0,1,u}, but u−v need not be a unit for two such u,v. M(K) is a maximum clique in the unit-difference graph, not the count of its exceptional vertices. A pairwise-difference certificate of length (N−1)/2 remains necessary. **Failed count-to-clique route.**

## Q2011 — finitely many sextic/septic fields with M(K)>7

<a id="q2011-a1"></a>
### A1. Normalize a clique and use fixed-field unit-equation finiteness
Normalize to 0,1,u₃,…,u₈. Each u_i and 1−u_i is a unit; the usual two-unit theorem makes this finite for a specified K. The constants and the units depend on K. It neither bounds discriminants nor the number of fields K. **Failed varying-field finiteness proof.**

<a id="q2011-a2"></a>
### A2. Use small residue fields as a uniform exclusion
Reduction injects a unit-difference clique into O_K/𝔭, so M(K)≤min_𝔭N𝔭. M(K)>7 therefore excludes prime ideals with norm≤7. This is a finite set of local splitting constraints (above 2,3,5,7), not a discriminant bound. Number fields can satisfy local irreducibility conditions while coefficients/discriminants vary. A global large-clique condition beyond these residue exclusions is needed. **Failed local-to-finite-fields proof.**

<a id="q2011-a3"></a>
### A3. Obtain a coefficient bound from eight unit differences
If u_i is integral, its minimal polynomial has constant term ±1; 1−u_i unit adds f_i(1)=±1. Monic degree-six/seven polynomials can obey both evaluations with unbounded coefficients (add T X(X−1) to a fixed monic polynomial). Thus even these simultaneous norms impose no direct height bound. The further u_i−u_j norm conditions have to be used; ignoring them loses the clique hypothesis. **Failed norm-evaluation height proof.**

<a id="q2011-a4"></a>
### A4. Construct infinitely many exceptions by quadratic base extension
The source notes Q(ζ₇)^+ has M=7, so its infinitely many quadratic extensions are sextic with M≥7. The target requires **>7**. Unit-difference cliques embed, but base extension supplies no eighth vertex. The construction is a useful sharp boundary example and does not refute the conjecture. **Failed infinite counterfamily.**

<a id="q2011-a5"></a>
### A5. Use bounded degree and Northcott directly
Northcott gives finitely many algebraic numbers of bounded degree **and height**. Unit status permits arbitrarily high heights in a fixed field, and varying field discriminants are unrestricted. An effective upper bound on the heights of a normalized eight-clique or its defining field is absent. Degree alone cannot invoke the theorem. **Failed bounded-degree compactness route.**

## Q3603 — effective two-unit height bound outside the quadratic exception

<a id="q3603-a1"></a>
### A1. Normalize ε+δ=n into a fixed S-unit equation
Dividing by n gives ε/n+δ/n=1, but introduces every prime dividing n into S. As n ranges, S and its rank are unbounded. A fixed-S effective unit theorem cannot give a constant depending only on K by this normalization. **Failed fixed-S application.**

<a id="q3603-a2"></a>
### A2. Use the source's unit-matching logarithms without its nonconjugacy premise
Matching compares ε^(i)+δ^(i)=ε^(j)+δ^(j) and needs nonzero logarithmic forms. If a conjugacy pairs ε^(i) with δ^(j), that form vanishes exactly and Matveev's nonzero-form lower bound does not apply. Excluding real-quadratic ε alone does not establish the source's stronger assumption that no higher-degree unit is conjugate to n−ε. **Failed unconditional Baker extension.**

<a id="q3603-a3"></a>
### A3. Classify higher-degree conjugate partners by polynomial symmetry
If δ=n−ε is a conjugate, the irreducible polynomial's root set is invariant under x↦n−x. It has even degree 2m and f(x)=g(x²−nx) after centering (over Q). The source derives imprimitive C₂-wreath-product constraints, not necessarily m=1. For m>1 the product t=ε(n−ε) can lie in a proper subfield and be a unit there. Eliminating every such higher-degree unit arrangement is still a relative-unit problem; symmetry alone does not imply ε quadratic. **Failed conjugacy classification.**

<a id="q3603-a4"></a>
### A4. Use finiteness of the allowed integer sums to bound all unit heights effectively
The earlier theorem quoted in the source makes the nonquadratic integer-sum set finite using unit equations, but with no effective enumeration in arbitrary K. Moreover the requested C_K bounds heights of both units, not merely |n|. For each fixed n a separate effective unit equation can be solved, but obtaining the finite list of possible n is the missing effective step. **Failed ineffective-to-effective transfer.**

<a id="q3603-a5"></a>
### A5. Bound integer sums by the embeddings and triangle inequality
n=σ(ε)+σ(δ) gives |n|≤|σ(ε)|+|σ(δ)|, an upper bound in terms of unknown unit sizes. The norm constraints ∏|σ(ε)|=∏|σ(δ)|=1 permit one very large embedding balanced by small others, and cancellations permit a small n despite high heights. Real-quadratic conjugate unit powers exhibit exactly this behavior; removing that known family requires quantitative matching/classification, not the norm equalities alone. **Failed elementary height inequality.**

## Status and limits

Six exact catalog targets have five full-target failed routes each. The explicit C₂×C₈ family and genus-three obstruction concern those particular section constructions. Lorenzini's small-N/exact-degree partials and Visser–Ziegler's odd-degree/primitive-field effective theorem are source inputs retained at their original scopes. No full catalog closure or unconditional rank witness has been added.

