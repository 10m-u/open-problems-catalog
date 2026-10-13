# Arithmetic decision targets and worked failed routes

The exact input statements and stable IDs are preserved in
QUESTION-SNAPSHOT.json. Each numbered item
below is one mathematical route directed at the full target. Its endpoint
is a counterexample to a proposed simplification or a precise unproved
algorithmic step. Five such failures stop that target; they do not establish
undecidability. The short finite computations in
[EXPERIMENT.json](EXPERIMENT.json) have explicit bounds.

Primary setups read locally:

- [Karimov et al., two power predicates and exponential functions](https://arxiv.org/abs/2407.05191v2),
  local collections-9f4bae832e047770, Theorems 1–2 and Sections 3, 7–8.
- [Rich sequences and arithmetic theories](https://arxiv.org/abs/2609.20415v1),
  local collections-a31afab513f3c751, repeated-root and arithmetic-predicate sections.
- [Bacik et al., bounded-variable polynomial-predicate arithmetic](https://doi.org/10.4230/LIPIcs.LICS.2026.7),
  local collections-547ff4cb440d28aa, introductory reductions and Section 5.
- [Haase et al., two-base Büchi existential arithmetic](https://arxiv.org/abs/2608.24410v1),
  local collections-110da6a2f0bd83f3, final three-base discussion.

These source versions establish the stated baselines; the analysis below
does not claim an exhaustive current-literature census.

## Q2978: the two-block power-predicate fragment

The target is ∃*∀* over Z with two fixed multiplicatively independent
power predicates. The following new observation is useful: its true
sentences are uniformly computably enumerable. Enumerate the integer
tuples for the first block. For each tuple c, decide the existential
sentence ∃y ¬ψ(c,y) using the two-power existential decision theorem;
its negation decides ∀y ψ(c,y). A successful c is a positive certificate.
This is a semidecision at the full signature, not a terminating decision.

1. **Turn that observation into a decision by witness bounds.**
   The algorithm reduces truth to a search through a decidable set of
   acceptable outer tuples. The derived test says nothing about the
   largest necessary tuple or about recognizing an empty acceptable
   set. No computable bound B(ψ) on an outer witness was derived.
   Without it, the negative branch still runs forever.
2. **Eliminate the universal block as complement intervals between
   powers.** A single literal ¬P_a(t) can be represented by adjacency
   between consecutive a-powers. For example, an integer strictly
   between a^n and a^(n+1) is not a power. But universal linear
   combinations of several y variables have unboundedly many such
   intervals, with boundaries from both bases. Introducing interval
   endpoints requires additional power witnesses that depend on y;
   moving those witnesses outward changes ∃x∀y∃p into ∃x∃p∀y,
   which is false in general. The attempted prefix-preserving
   interval elimination therefore does not close.
3. **Use one synchronous base for both predicates.** For a=2,b=3,
   P_3 is 3-automatic and not ultimately periodic. If it were
   2-automatic, Cobham's theorem would force ultimate periodicity.
   Thus the actual predicate needed by a binary automaton is not
   regular. The argument obstructs this common-base algorithm,
   not all decision methods.
4. **Lift the existential Baker-inequality algorithm uniformly.**
   Fixing an outer tuple yields a concrete inequality system that
   the published algorithm decides. Its reductions and separation
   thresholds depend on those tuple values. Replacing them by free
   variables leaves an infinite family of case-dependent systems;
   no finite symbolic partition with effective bounds was obtained.
   Pointwise decidability does not justify quantifier elimination
   uniform in the still-quantified tuple.
5. **Reduce the known three-block undecidable fragment.**
   Attempted prenex contraction takes ∃u∀v∃z θ to two blocks.
   The last z supplies a different response for each v. Existential
   naming of one tuple z before ∀v is invalid, while encoding the
   entire response function needs a sequence-coding relation absent
   from the signature. No two-block reduction was constructed.

Outcome: five failures; the full-question semidecision is partial.

## Q2979: two exponential functions

1. **Flatten function terms into power predicates.** Replace a^x
   by a fresh p and assert P_a(p). This loses the relation between
   index x and value p. Already x=1,p=4 passes P_2(p) and fails
   p=2^x. Nesting and shared indices create further lost relations.
   The predicate decision theorem cannot decide the flattened formula.
2. **Build an automatic exponent graph.** For a=2, graph values
   have output bit length x+1 and input bit length O(log x).
   An N-state synchronized functional automaton permits only a fixed
   additive length increase, by pumping an output-only padded tail.
   Hence no such automaton recognizes p=2^x at every x. The
   general automatic word-arithmetic lane does not extend here.
3. **Use logarithms to linearize the exponent equations.**
   p=a^x is equivalent to log p=x log a, but p is an integer
   quantified value. Linear expressions such as a^x+b^y turn into
   log sums, and equalities require exact integral membership.
   The resulting conditions are not linear forms in the original
   integer variables. No integer-preserving elimination was found.
4. **Infer a negative decision from transcendental digit sampling.**
   The source reduction connects function-fragment decidability to
   occurrence questions for digits of log_b(a), including positions
   sampled exponentially. A finite prefix can certify an occurrence;
   absence in every longer prefix has no effective certificate here.
   Neither a uniform recurrence modulus nor the required sampled
   occurrence theorem was proved. This route gives search, not NO.
5. **Simulate multiplication via exponent addition.**
   a^(x+y)=a^x a^y is a true identity, but it multiplies power
   values, not arbitrary x,y. The signature lacks a logarithm or
   an index-encoding map turning arbitrary products into the needed
   exponent relation. An actual existential multiplication definition
   was not obtained. The identity alone proves no undecidability.

Outcome: five failures; predicate and function signatures remain distinct.

## Q2980: U={n 2^n} with addition

1. **Automatic recognition.** The slice of U consisting of powers
   of two is exactly {2^(2^k+k):k≥0}: n2^n is a power of two iff
   n is a power of two. Its binary words have a one followed by 2^k+k zeros.
   Their lengths have unbounded gaps and are not eventually periodic.
   Intersection with the regular power-of-two language would preserve
   regularity. Thus U is not binary automatic. This is a genuine
   new encoding obstruction, not a decision result.
2. **Apply a simple-root recurrence proof by limiting ratios.**
   The ratio u_(n+1)/u_n tends to 2, but is exactly 2+2/n.
   The polynomial prefactor remains relevant to equalities:
   u_(n+1)-2u_n=2^(n+1). Treating it as a geometric sequence
   erases this residue and gap information. No verified replacement
   of the simple-root effectiveness hypotheses was obtained.
3. **Recover the index from consecutive U-elements.**
   In the ordered predicate, adjacency of u and v can be defined.
   For consecutive u_n,u_(n+1), the identity v-2u=2^(n+1)
   supplies a power-like gap. Recovering n then requires logarithm
   or the relation u=n2^n, which is the original index problem.
   There is no additive term that divides u by that variable gap.
4. **Define multiplication from those gaps.**
   The gap identity supplies particular products n2^n, not arbitrary
   xy. The proposed interpolation would require arbitrary variable
   scaling of a gap; fixed linear combinations are the only arithmetic
   terms in the language. No interpretation of integer multiplication
   follows from the recovered consecutive-value identity.
5. **Sparse-set effective elimination.**
   For a sum Σ c_i n_i2^(n_i), dominance separates indices that
   are very far apart. Near equal indices can cancel their leading
   powers and leave polynomial factors. Sorting indices does not
   bound the near-cancellation clusters uniformly through quantifier
   alternation. No effective bounded-cancellation theorem satisfying
   the sparse-predicate elimination contract was proved.

Outcome: five failures; binary nonautomaticity is a partial result.

## Q2981: addition with the prime predicate

1. **Finite automata.** Prime counts at digit length n behave like
   a constant times b^n/n by the prime number theorem. A regular
   language's counting generating function is rational; at a fixed
   exponential rate its coefficients have polynomial factors with
   nonnegative integer degrees, not n^(-1). Thus primes cannot be
   recognized by a synchronous unary base-b automaton. This excludes
   the proposed automatic decision method.
2. **Residue quantifier elimination.** Sieve away finitely many
   primes and replace P(x) by the remaining congruence conditions.
   A composite whose two prime factors exceed every sieving prime
   passes those conditions. Therefore no fixed sieve equals P.
   Refining the sieve indefinitely has no finite QE stopping rule.
3. **Prime-tuples theorem as an oracle.**
   A formula with several P(a_i x+b_i) literals asks exact
   simultaneous primality, and arbitrary sentences also use
   negations and alternating quantifiers. Local congruence
   admissibility alone does not prove existence of all admissible
   prime patterns. No unconditional uniform prime-tuples decision
   theorem was produced or assumed.
4. **Finite search for all existential queries.**
   With one parameter n, the formula asking primes p,q with p+q=n
   has a finite interval bound. A sentence asking infinitely many
   adjacent primes instead ranges over every interval. Explicitly
   bounding each fixed-n query does not give a bound on all
   quantified n. No full-theory reduction to bounded queries follows.
5. **Undecidability through factorization.**
   Naming primes does not give the multiplication term pq or
   variable divisibility p|n. The attempted recovery of factors
   would first need a definable variable multiplication/divisibility
   relation, with proof. Reusing ordinary product factorizations
   in the metalanguage cannot supply that missing interpretation.

Outcome: five failures. No claim of a prime-theory solution.

## Q2982: order and r-power-free numbers, without addition

1. **Transfer the additive undecidability construction.**
   The source uses equalities between variable differences and
   translates integer patterns. Such expressions as y=x+c for
   fixed c are order-definable through c successors; variable
   translation and equal differences are not. Removing addition
   destroys the stated arithmetic coding. No order-only simulation
   was constructed.
2. **Decide every finite word using a power-free sieve.**
   For a requested finite pattern, its positive positions must avoid
   covering all residues modulo p^r. There are only finitely many
   relevant small p for that admissibility test, and CRT can assign
   fresh prime-power divisors to requested zero positions. This is
   promising for fixed finite patterns. FO order formulas may
   describe intervals with arbitrarily many positions, however;
   deciding each finite pattern individually is not a terminating
   test for intersection with an arbitrary formula's interval-type
   language. That further uniform intersection theorem was not proved.
3. **Uniform recurrence of the characteristic word.**
   Assign different primes p_j and solve n+j≡0 modulo p_j^r.
   CRT gives zero runs of any prescribed length. Thus the one
   symbol, despite recurring, has no bounded-gap recurrence
   modulus. A procedure needing uniform recurrence cannot apply.
4. **Finite local type implies global FO decision.**
   A rank bound produces finitely many abstract interval types,
   but it does not decide which occur or recur in the arithmetic
   word. The proposed induction needs an effective test for all
   realizable concatenations of these types, including unbounded
   intervals. No such realization test was supplied.
5. **Add only successor and invoke an automatic presentation.**
   Successor is definable from the given order, but that does not
   make the power-free word regular. Long CRT zero runs defeat
   the recurrence shortcut, and a digitwise automaton has not been
   constructed. Neither the order-only signature nor its definable
   successor permits adding variable arithmetic at no cost.

Outcome: five failures. None of the additive undecidability results is
silently transferred to this order-only question.

## Q2990: one-variable polynomial image predicates

1. **One-variable quantifier normalization.**
   With one reusable variable name, an inner quantified subformula
   is closed. Recursively replace its truth value by a Boolean
   constant. This reduces the decision problem to existential
   one-variable quantifier-free Boolean combinations of linear
   comparisons, congruences and polynomial-image atoms. It is a
   useful reduction but does not decide their intersections.
2. **Eliminate x from two positive image atoms.**
   R_f(ax+b) and R_g(cx+d) give
   c f(u)-a g(v)=c b-a d, together with the integral residue
   condition for x. This is a separated-variable Diophantine
   curve; for arbitrary fixed polynomial families its degree and
   genus need not be low. The concrete example
   R_(t^5+t)(2x+1) ∧ R_(t^4+t)(3x-2) gives
   3(u^5+u)-2(v^4+v)=7. The checked box is empty, but it supplies
   no unbounded integral-point decision. Note that coprimality
   of 2 and 3 recovers the necessary x residue here.
3. **Use polynomial dominance for a search bound.**
   Leading terms can cancel on a curve with u and v growing at
   different rates. Comparing magnitudes bounds one variable
   relative to the other, not both absolutely. No effective
   absolute bound on all isolated integer solutions was derived.
4. **Classify curves by genus.**
   Low-genus special cases are available in the primary paper.
   Merely recognizing that a remaining curve has finitely many
   integral points does not furnish their effective height bound.
   Moreover negative image atoms require deciding complements
   jointly, not just listing roots of one positive equation.
5. **Encode unrestricted Hilbert tenth undecidability.**
   Replacing each image predicate by an existential root
   introduces hidden variables, but only separated univariate
   polynomial equations tied to linear forms in the same x.
   An arbitrary multivariate polynomial circuit is not obtained.
   No root-packing map preserving this restricted fixed-F
   signature was built, so general Hilbert tenth hardness is
   insufficient for a negative answer.

Outcome: five failures. One-variable normalization is a partial reduction.

## Q2991: two-variable FO arithmetic with squares

1. **Replace the square predicate by a square function.**
   S(x) means that some root exists, not that a named output
   equals x². A definition y=x² requires linking x to that
   root. Introducing a third witness variable exceeds FO²;
   the attempted function replacement changes the signature.
2. **Reuse variable names in a multiplication definition.**
   The identity 4xy=(x+y)²-(x-y)² needs square values while
   retaining x and y. Binding either of the two names to an
   auxiliary square overwrites a live argument. The concrete
   flattening therefore needs extra names; no two-variable
   multiplication definition was proved.
3. **Apply the existential square-predicate undecidability proof.**
   Its Büchi-sequence encoding uses an array of square values
   and a multiplication circuit. It does not bound all live
   variables by two. No prefix/variable-preserving reduction
   from that construction was obtained.
4. **Reduce each matrix to a planar algebraic curve.**
   A quantifier-free matrix does give constraints on affine
   forms in x,y. FO² then alternates quantifiers and asks
   whole-fiber statements, rather than existence of one point.
   Eliminating roots in each fiber neither bounds the fibers
   uniformly nor provides a two-variable QE procedure.
5. **Finite congruence types for square literals.**
   Square membership passes many congruence tests but is not
   any finite congruence union. Quantified formulas can exploit
   arbitrarily large gaps between squares. A fixed modulus
   abstraction cannot certify equivalence of all these fibers;
   no complete finite-state refinement was constructed.

Outcome: five failures; no reduction changes FO² into unrestricted FO.

## Q2992: two existential variables and cubes

1. **Reduce to independent one-variable cube tests.**
   The permitted formula C(x)∧C(y)∧C(n-x-y) already couples
   both variables. It is equivalent to u³+v³+w³=n over signed
   integers. Thus independent intersection algorithms discard
   the most basic allowed third affine cube atom.
2. **Bound roots using positivity.**
   If all roots were nonnegative, u,v,w≤n^(1/3). The actual
   domain is Z. Taking u=T,v=-T,w=1 solves n=1 for arbitrarily
   large T, so positivity-based global root bounds are false
   even on a satisfiable instance of this exact fragment.
3. **Decide by congruence obstruction.**
   Cubes modulo nine are 0,±1, excluding n≡±4. The test n=114
   passes (three residues -1 give 6). Congruence admissibility
   is a filter, not a proof of integer solutions or a general
   exact decision theorem.
4. **Exhaustive bounded root search.**
   The complete signed cube box |u|,|v|,|w|≤1000 for n=114
   has no witness. The exact program checks every pair and
   dictionary-tests the third cube. Without an effective
   completeness bound, its empty result cannot be a NO answer.
   This single bounded solve attempt counts once; its millions
   of pairs are not separate attempts.
5. **Fiberwise elliptic methods.**
   Fixing u turns v³+w³=n-u³ into a family of cubic curves.
   Even if each fixed fiber's integral points can be computed,
   u still ranges over every integer. No uniform height bound
   or finite set of fibers containing all solutions was proved.

Outcome: five failures. The date-specific literature status of n=114 is
not promoted here; only the explicitly bounded computation is asserted.

## Q2993: three power predicates

1. **Repeated application of the two-base decision procedure.**
   Keep a 5-power variable as a parameter and decide the
   remaining 2/3 system. This is a decidable test for each
   parameter value and yields a positive search. It supplies
   no finite bound on the 5-power parameter in negative cases.
2. **Combine two predicates into one composite-base predicate.**
   P_6 captures synchronized exponents 6^n=2^n3^n. Independent
   2- and 3-power variables have unequal exponents, and their
   product is not an additive-language term. Composite bases
   therefore do not represent the original free choices.
3. **Multidimensional Kronecker density.**
   The two-base argument uses irrationality of one logarithm
   ratio. The three-base extension needs the relevant rational
   independence in a higher-dimensional torus, involving
   reciprocal logarithms. Unique prime factorization proves
   independence of log2,log3,log5, not of their reciprocals.
   No unconditional proof of the needed independence was found.
4. **Decide equality cases by S-unit equations.**
   Linear equations in finitely many prime-power values are
   related to effective S-unit methods. The actual existential
   fragment also allows strict inequalities and complements of
   predicates. Solving the equality subproblem does not settle
   orbit visits to all permitted inequality regions. A verified
   extension to those regions was not constructed.
5. **Effective separation of all cancellation clusters.**
   Sorting the largest values suggests a Baker-style dominance
   recursion. With three bases, two distinct near-cancellation
   clusters can constrain one shared exponent and each other's
   ratio windows. The attempted recursion has no proved
   uniform termination or effective final bound in these
   coupled cases. Assuming Schanuel would change the requested
   unconditional result and is not adopted.

Outcome: five failures, with the exact unconditional gap retained.
