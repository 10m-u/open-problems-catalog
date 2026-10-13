# Q2778: global linear cardinality constraints

2026-10-12. Work on the exact catalog question Q2778 (`751e0d4f3c49d9c5e284`): is finite satisfiability decidable for GP² sentences conjoined with global integer linear comparisons among cardinalities of unary GP²-definable sets? The source is [Benedikt–Lu–Tan, CSL 2026, Section 6, after Theorem 38](https://doi.org/10.4230/LIPIcs.CSL.2026.27), locally `../../../texts/papers/collections-2f5eb9092358afd8.txt.gz`.

Q2777's semilinearity proof is a separate positive result. It does not decide this question. Failed routes below refer to proposed **full-question algorithms or proof routes**, not to failures of the conjectured decidability statement. Counts remain subject to independent review; a restricted positive theorem does not reset the full-question failure streak.

## A1. Internalize linear constraints by token copies and injections

**Proposed full route.** Replace every global cardinality comparison by guarded matching conditions on fresh token objects, then invoke ordinary GP² finite satisfiability. Work through coefficients, overlapping definable sets, domain expansion, strict comparisons, and affine constants rather than treating an equicardinality slogan as a complete reduction.

**Positive restricted theorem.** Finite satisfiability of GP² with any finite conjunction of *homogeneous* global integer linear constraints is decidable. Here homogeneous means that the compared integer linear combination has constant 0. We also cover conjunctions of comparisons L≥k with k≥0, and equivalently L≤k with k≤0, where L is any integer linear combination of definable-set cardinalities. No complexity claim beyond an effective reduction is needed.

**Relativization.** Let O mark the original domain. Require ∃x O(x). Replace every original unary quantifier ∃x θ by ∃x(O(x)∧θ^O), and in every local count insert O on its counted variable. Relativize φ and each unary θ_i in this way. Then a structure on an enlarged domain satisfies φ^O exactly when its induced original-vocabulary structure on O satisfies φ. This follows by induction, also when θ_i contains closed subformulas. Fresh token objects and new roles have no effect on φ^O.

Write a constraint's integer linear expression as

    L = Σ_{i∈I+} a_i |θ_i| − Σ_{j∈I−} b_j |θ_j|,

where all a_i,b_j are positive integers. For each occurrence introduce a fresh, separate token class T_i and a fresh owner relation H_i. Require all these token classes to be disjoint from O and from one another. Owner edges have source O and target T_i, expressed by forbidding guarded bad edges. Every T_i object has exactly one incoming H_i edge. Every original object satisfying θ_i^O has exactly a_i outgoing H_i edges, and every other original object has zero such edges; use b_j on the negative side. These conditions are GP² formulas. They force

    |T_i| = a_i |θ_i|  (or b_i |θ_i|).

Conversely, starting with an original finite model, create these tokens separately for each owner. Overlapping θ_i are harmless: their tokens remain separate.

Let P be the union of the positive token classes and N the union of the negative token classes. They are disjoint. Introduce a fresh matching relation F whose edges have source N and target P.

* For L≥0 require every N token to have exactly one outgoing F edge and every P token to have at most one incoming F edge. This is precisely an injection N→P in a finite structure.
* For L=0 require every P token to have exactly one incoming F edge too. This gives a bijection.
* For L>0 use the injection and additionally require an unmatched P token to exist. The unary formula for unmatched is `P(x) ∧ #y[F(y,x)]=0`.
* Reverse P and N for L≤0 or L<0. For L≠0 use the disjunction of the two strict constructions, with the corresponding fresh predicates and roles.

Each forward construction follows by double-counting owner and matching edges. Each reverse construction follows by creating the required number of tokens and choosing a finite injection or bijection. Thus every homogeneous comparison is internalized exactly, and conjunctions use distinct auxiliary roles/classes. The resulting sentence lies in GP², whose finite satisfiability is decidable by [CSL 2026, Theorem 9](https://doi.org/10.4230/LIPIcs.CSL.2026.27).

For L≥k>0, use the injection N→P and add a fresh center class disjoint from original objects and tokens. Require a center with exactly k distinct outgoing G-neighbors satisfying the unmatched-P formula. This asserts that at least k P tokens remain unmatched. A center can be created whenever the surplus is at least k. It need not be globally unique. All added objects can be partitioned into O, the token classes and the center classes by a unary universal sentence.

**Exact full-scope failure.** An affine equation L=k>0 would require precisely k unmatched P tokens, rather than merely at least k. The immediate completion by a fresh constant token class C with |C|=k is unavailable in GP². Indeed, if a GP² sentence ζ had a finite model M with |C|=k>0 and forced |C|=k in *all* its finite models, then M⊔M would be another model by the same-profile lemma in `Q2777-RESULT.md`, but would have |C|=2k. The same reasoning applies to a unary GP²-definable constant class.

More generally, no model-preserving expansion into GP² can enforce a fixed nonzero global difference |A|−|B|=k on its entire designated original domain: copying a model doubles the difference while preserving the sentence. This is an obstruction to this token-and-projection translation, not to every possible satisfiability reduction; a reduction that extracts a smaller domain or otherwise changes original cardinalities remains conceivable.

**Outcome.** A full worked reduction succeeds on homogeneous constraints and one-sided positive-surplus bounds, but fails to internalize general affine equalities. Proposed full-Q2778 failure count: **1**, pending review. Missing step: an alternative effective treatment of finite affine offsets that does not assume a globally fixed token class can be expressed in GP².

**Literature scope control.** [Baader–Bednarczyk–Rudolph, ECAI 2020](https://doi.org/10.3233/FAIA200146) studies a stronger language that mixes global and local counts inside its concept constructors. Its result with inverse roles cannot be applied merely by observing that Q2778 has both kinds of counts: Q2778 restricts global comparisons to sentences, so a syntax-preserving reduction would still be needed. This reading is not a separate solve attempt.

## A2. Augment the pseudomodel linear system with exact vertex counts

**Proposed full route.** The paper's Section 4 replaces actual graphs by compatible behavior vectors and a colored multigraph. Append a vertex-count coordinate 1 to each behavior vector before taking its Kleene star, then conjoin the external linear constraints on these coordinates. The resulting semilinear arithmetic feasibility problem is decidable. It would settle Q2778 if a feasible multigraph could always be converted to a simple relational model with those same unary cardinalities.

**Exact counterexample to that last lemma.** Take P,Q partitioning the domain, forbid E self-loops, and impose the following GP² conditions:

    each P element: #outgoing E to P = #outgoing E to Q;
    each Q element: #incoming E from P = 1.

This is the source's Section 6 example, with the loop exclusion explicit. Conjoin the affine global equations

    |P|=2,  |Q|=4.

Every actual model has |Q| equal to the number of directed internal E edges on P, by summing the two local equations. With two P elements and no loops there are at most 2 such edges, so this constrained instance is unsatisfiable.

There is nevertheless a matching-compatible colored multigraph with these exact vertex counts. Let its P elements be p0,p1 and its Q elements q0,…,q3. Put two parallel mutual-E colored edges between p0 and p1. Put directed edges p0→q0,p0→q1,p1→q2,p1→q3. In the pseudomodel's behavior-vector interpretation, each P has two outgoing E occurrences toward P and two toward Q; each Q has one incoming occurrence from P. Aggregate stub counts match their dual 2-types. All unary and guarded binary requirements hold. The appended vertex-count coordinates are exactly (2,4).

There is a simple model after scaling those counts to (4,8): use four P elements, the bidirected K_{2,2} relation on them, and two private Q successors of each P element. Its local degrees are still (2,2) on P and 1 incoming on Q. This makes the distinction between satisfiability-preserving lifting and cardinality-preserving lifting concrete.

**Outcome.** The augmented arithmetic system accepts a constrained instance with no relational model. Proposed full-Q2778 failure count: **2**, pending review. Missing step: an exact simple-graph realization test or a construction that respects affine vertex-count constraints. The obstruction is about multiplicities and simple-graph capacities, unlike A1's inability to express constant token classes. The paper already warns that its pseudomodel construction changes cardinalities; the new work here is the explicit false-positive arithmetic witness for the proposed extension, rather than a claim to discover that warning.

## A3. Transfer the earlier GP²→C² offset/period reduction

**Proposed full route.** Instead of the multigraph system, use the earlier finite-satisfiability reduction to C², then use decidability of C² with global constraints. The relevant primary source is [Bednarczyk–Orłowska–Pacanowska–Tan, FSTTCS 2021, Sections 4.1–4.2, Lemmas 12–14](https://doi.org/10.4230/LIPIcs.FSTTCS.2021.36). Its crucial operation separates a local semilinear degree vector into one offset vector and several period vectors on separate vertices. The converse uses copies and merges. Satisfiability equivalence does not assert that named unary classes keep their cardinalities.

**Worked arithmetic obstruction.** Let A,B,C be disjoint unary classes partitioning the domain. Permit R edges only from A to B, and S edges only from A to C. Require each B to have exactly one incoming R edge and each C exactly one incoming S edge. For each A require

    #y[R(x,y)] − 2 #y[S(x,y)] = 1.

All are GP² conditions. Its A behaviors in these two outgoing coordinates form the single linear set

    (1,0) + N·(2,1).

Conjoin the global cardinalities

    |A|=2, |B|=3, |C|=1.

No model exists, even allowing parallel edges: summing the A equation and applying the leaf incoming-degree constraints gives the necessary identity

    |B| − 2|C| = |A|,

but the proposed vector has 3−2=1≠2.

Now replace A's allowed degree set by its offset/period pieces (1,0) and (2,1), requiring a period A vertex to have a same-unary-type offset A witness. This is exactly the local replacement used in the typed version of that C² splitting strategy. Its six-element relaxed structure exists: take A={u,v}, B={b0,b1,b2}, C={c0}; put R(u,b0),R(v,b1),R(v,b2),S(v,c0). Vertex u is the offset witness and v is periodic; all leaves have incoming degree 1. The unchanged global constraints therefore accept the relaxed structure. It is not an original model because v has local difference 0 rather than 1.

Merging u and v would produce an original A vertex with degree (3,1), but changes |A| from 2 to 1. Conversely, splitting the valid one-A model into those two pieces changes its unary counts. This demonstrates a different loss from A2: A2's arithmetic is exact for multigraphs and fails at simple-graph realization, whereas this relaxation already loses vertex counts under purely linear degree equations.

**Attempted repair.** Count only offset vertices as “original,” excluding periodic vertices from external cardinality constraints. This corrects the displayed handshaking identity, but the general converse still requires merging periodic pieces into offsets while avoiding loops and repeated neighbors. The cited construction ensures safe merges by duplicating the entire model first, and these copies multiply the newly designated original counts. No modification proving an exact-count, collision-free converse was obtained. This is the missing theorem; merely labelling offsets does not supply it.

**Outcome.** The unmodified C² transfer has a concrete false positive, and the natural offset-only accounting repair lacks a cardinality-preserving merge proof. Proposed full-Q2778 failure count: **3**, pending review. This does not invalidate the published unconstrained satisfiability reduction. The six-element example concerns the explicitly stated typed offset/period replacement, not a claim to have run an implementation of every preliminary renaming in the source.

## A4. Homogenize every affine constraint with a scale variable

**Proposed full route.** A1 supplies decidability for homogeneous constraints. Given affine constraints C v=d on the original unary cardinality vector v, introduce a fresh disjoint class T with t=|T|>0, and replace them by C v=d t. The enlarged constraints are homogeneous and therefore decidable by A1. Try to prove that a feasible model can be chosen with t=1, or divided by t to recover an original model. This is a natural way to remove the exact-constant token issue, and is stronger than simply repeating A1's syntactic failure.

**Exact obstruction: divisibility of model sizes.** Let original elements be partitioned into A and B, with a matching relation R from A to B. Every A has exactly one outgoing R edge and every B exactly one incoming R edge. Forbid all other R edges and require A to be nonempty. This is a GP² sentence and forces

    |A|=|B|>0, hence |Original|=2|A| is positive and even.

The affine instance |Original|=1 is unsatisfiable. Its homogenization

    |Original|=|T|>0

has a model with one A, one B, their matching edge, and two T elements. There is even a primitive full class-cardinality vector (|A|,|B|,|T|)=(1,1,2), whose entries have gcd 1, but its scale coordinate is 2. “Take a primitive integer solution” does not force the scale to 1.

If T elements are themselves paired bijectively with original elements to implement the homogeneous equality, every connected matching block still accounts for two original elements and two T elements. It cannot be divided into a valid one-original-element structure. At the arithmetic level (1/2,1/2,1) is not an integer cardinality vector; at the relational level a matching edge cannot have half a vertex at each end.

**Outcome.** The homogenized satisfiability test gives a false positive for this affine instance. Proposed full-Q2778 failure count: **4**, pending review. Missing step: an effective test for a genuine scale-one model, rather than a positive-scale rational or integer model. This obstruction uses unavoidable parity, not A2's simple-graph capacity or A3's choice of vertex splitting.

## A5. Extend Q2777 by learning finitely many component-vector generators

**Proposed full route.** Q2777 partitions models into finitely many truth-profile classes closed under disjoint union. Replace each profile's one-dimensional size semigroup by a multivariate semigroup of unary class counts. Try to enumerate a finite set of valid model vectors generating each such semigroup. With a known complete finite generating family, intersection with external linear constraints reduces to Presburger arithmetic, which would decide Q2778.

**Worked obstruction to the finite-generation lemma.** Use exactly A2's universal P/Q sentence, without its fixed affine constraints. Its possible vectors are

    S = { (a,b) : a≥1, 0≤b≤a(a−1) }.

The bound follows from directed internal-P edge capacity. Conversely, for any b≤a(a−1), choose a loop-free directed graph with exactly b edges on a P elements. For each edge create one private Q element and a new E edge from that original edge's tail to that Q element. Every P has equal outgoing counts toward P and Q, and every Q has one incoming edge. Thus every displayed vector is realized.

Every model of this universal conjunction has the same closed-subformula profile: all its closed universal conjuncts are true (or their negated-existential forms have the corresponding fixed truth values). The infinitely many vectors below therefore belong to **one** profile class; adding more of Q2777's sentence truth profiles does not remove this example.

The set is additive since

    a(a−1)+c(c−1) ≤ (a+c)(a+c−1).

But every boundary vector

    v_a = (a,a(a−1)),  a≥2,

is additively indecomposable into two nonzero vectors of S. For a split a=r+s with r,s≥1, the second coordinates of the summands are bounded by

    r(r−1)+s(s−1) = a(a−1)−2rs < a(a−1).

The same argument handles any number of nonzero summands by first grouping them into two. Hence every v_a must occur in any family of valid model vectors generating S. That family must be infinite, so enumerating a sufficient finite component library cannot terminate with the claimed completeness property.

For clarity, even allowing arbitrary finite linear-set bases and periods does not give a representation of S. A period with first coordinate 0 and second coordinate positive would generate arbitrarily large b for a fixed a, so none is possible. All other nonzero periods have a finite ratio b/a; a finite union of linear sets would therefore satisfy b≤K a+C for some finite K,C. The quadratic boundary a(a−1) violates every such bound. This independently reconstructs the source's nonsemilinearity example.

**Outcome.** The finite-generator extension of Q2777 fails on an explicit all-size, single-profile family. Proposed full-Q2778 failure count: **5**, pending review. The source already supplies the nonsemilinearity example; this attempt works out the precise obstruction to the component-generator algorithm. It does not imply that deciding intersection with linear constraints is impossible by a different method. The quadratic family's individual linear-constraint instances can still be much easier than the general question.

## Current disposition

Five proposed full-question routes have been worked. Q2778 remains unresolved and is submitted for stopping under the user's five-failures-per-question rule, subject to independent count review. A1/A4 both concern affine offsets but test different completions (literal constant-token expansion versus scale normalization); A2/A3 both adapt published finite-satisfiability machinery but fail at different invariants (simple-graph capacity versus vertex-count bookkeeping). A5 concerns finite multivariate model-vector generation. These are five sufficient proof/algorithm routes, not five unrelated counterexample families. If review finds an overlap, the counter must be reduced rather than treating a repeated limitation as an attempt.

The homogeneous restricted theorem is a separate partial result, submitted for independent review. Exact construction and obstruction controls are recorded in `check_global_routes.py` and `GLOBAL-ROUTE-CHECK-RESULTS.json`. No software or source-access failure is counted. No decidability or undecidability claim for full Q2778 is made.
