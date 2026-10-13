# Model-theoretic targets

Exact questions are in the snapshot.
The five routes recorded for an open target are mathematical failed
constructions or proof approaches, not claims that the statement is false.
Their obstructions may overlap. A restricted successful lemma does not
reset the full-question count.

## Q2168: retained exact solution

Root read Part I of the original B1 report in full. The rational-function
space W=Q[t]+span_Q{1/(t+n):n≥1}, for positive transcendental t,
and P=W×Z use the correct distinguished 1=(0,1). Multiplication
by t+n identifies W with the proper subspace omitting the pole at -n.
Every finite subset eventually lies in that subspace. Its inclusion in P
is elementary because its residues and linear comparisons agree.

The characteristic divisible part is W×{0}. An ordered additive
automorphism of the Archimedean W is scalar multiplication, by
comparison with rational cuts. Sending the real unit to 1/(t+n)
would create a double pole, which is absent from W. Π₂ downward
preservation along the elementary subspace therefore prevents a
Σ₃ definition of the real-unit orbit. The cited orbit theorem excludes
Π₄ Scott sentences. Naming that unit gives singleton rational-cut
and residue definitions of every element; the explicit labelled
diagram Scott sentence is Π₃ in that expansion, and existentially
forgetting the unit gives Σ₄. The argument also excludes lower
d-Σ₃ complexity.

This supports retaining the existing exact Q2168 mark. No new
ledger decision, original proof claim or compiled formalization is
needed. The original archive is still absent. Primary dependencies:
[Block v3](https://arxiv.org/abs/2601.21118v3),
[Montalbán's orbit theorem](https://math.berkeley.edu/~antonio/papers/scottRank.pdf).

## Q2169: remove the discrete factor at every Archimedean rank

1. **Enumerate the integer subgroup and form the quotient.**
   In any presentation of P, C=Z·1 is c.e. by listing standard
   multiples. The proposed least-representative quotient also
   requires deciding when x-y is not a multiple. Its negative
   instances need not be enumerable by that construction.
   Merely using the positive list gives duplicate quotient labels,
   not an atomic diagram of V in the same degree.
2. **Replace one least-class anchor by finitely many anchors.**
   Take V=⊕_(n≥0) Qe_n ordered by the first nonzero coefficient.
   The positive classes e_n descend without a least class. Every
   finite set of nonzero anchors has some smallest selected class;
   choose e_n smaller still. No multiple of e_n exceeds that
   anchor, so the least-class dovetail from the old return fails
   to classify this noninteger element. Adding finitely many
   anchors does not repair the full-rank argument.
3. **Use all positive elements as a computable anchor sequence.**
   This list also includes the standard integers. The proposed
   test n|x|>a with a in that list can accept x=1 by taking a=1
   and n=2. Every usable anchor must first be certified outside C.
   That certification is the unresolved quotient problem, so
   the attempted uniform enumeration is circular.
4. **Rationalize the computable group instead of quotienting.**
   P⊗Q is effectively presentable from the group diagram,
   but algebraically it is V×Q with a new least Archimedean
   class. For V=Q, this has two classes, whereas V has one.
   Recovering V still requires removing the new convex Q.
   Rationalization is not an isomorphic replacement for V.
5. **Approximate the quotient by merging labels.**
   A finite-stage quotient can merge representatives when a
   new integer difference appears. Fixing an atomic diagram
   too early then records wrong inequalities or additions;
   allowing late changes yields a limit-computable diagram,
   not a computable one in the original oracle. No finite-injury
   construction producing a different computable copy of V
   was verified. Failure of this presentation-level quotient
   does not prove failure of degree-spectrum equality.

Outcome: five failures. The old least-class theorem is retained exactly.

## Q2170: degree-spectrum universality for Presburger groups

1. **Encode an arbitrary graph by commutators of generators.**
   A Presburger group's addition is abelian. Every commutator
   is identically zero, so the usual graph/group edge coding
   by selective commutation carries no graph information here.
   The attempted general-structure interpretation fails.
2. **Encode edges in a named ordered Q-basis.**
   One can prescribe real cuts or Hahn coordinates for chosen
   basis vectors, but arbitrary copies of the ordered group
   do not provide that chosen basis as a decidable relation.
   Recovering the input graph requires recognizing those
   generators and their coordinates in every presentation.
   No uniform interpretation with that property was built.
3. **Use a single Archimedean cut as a universal code.**
   A chosen pair of independent elements can encode a real
   through their rational comparison cut. Passing to arbitrary
   copies changes the unnamed scale and rational basis.
   A proof is needed that this decoding gives exactly the
   original structure's spectrum, rather than a cone above
   a chosen real code. The proposed cut encoding proves
   no such equivalence for arbitrary structure spectra.
4. **Separate spectra by upward closure.**
   Infinite ordered diagrams can encode any higher degree
   by permuting label pairs according to that degree and
   reading their order. Thus Presburger spectra are upward
   closed. The same spectrum phenomenon is available for
   non-automorphically-trivial structures; upward closure
   alone supplies no forbidden spectrum and no counterexample.
5. **Force a computable copy by Presburger quantifier elimination.**
   QE decides the complete theory, not the isomorphism type.
   Let V=Q+Qt in R with a noncomputable transcendental real
   t. If it had a computable ordered-group copy, choose a
   rationally independent pair as finite program parameters.
   Its ratio cut is computable from comparisons. That ratio
   is a rational fractional-linear transformation of t,
   with nonzero determinant; inversion makes t computable.
   Hence this V has no computable copy. The proposed
   computable-model obstruction is false. It still does not
   furnish the arbitrary spectrum universality theorem.

Outcome: five failures. No universal spectrum construction or
counterexample was obtained.

## Q246: NIP but non-distal unary expansions of ordered integers

Primary syntax and the sparse criterion were checked in Tong's
local thesis, Chapter 3, including Theorem 3.2.19 and 3.4.8.
The existing automatic-predicate exclusion remains partial.

1. **A nonautomatic very sparse candidate.**
   Try R={2^(2^n):n≥0}. Its successive ratios tend to infinity,
   so it is regular/sparse in the source convention. Modulo
   a fixed m, the sequence 2^k is eventually periodic in k;
   the exponents 2^n are themselves eventually periodic
   modulo its eventual period. Thus R is congruence-periodic.
   Tong's criterion makes the expansion distal. This actual
   nonautomatic candidate cannot witness the question.
2. **The repeated-root candidate R={n2^n}.**
   This escapes the previous route. Its ratio tends to 2,
   but the required algebraic minimal operator σ-2 does
   not vanish: r_(n+1)-2r_n=2^(n+1). It is not regular/sparse
   in Tong's convention. This prevents invoking the existing
   sparse NIP/distality arguments. A proof of NIP plus a
   non-distal indiscernible configuration was not obtained.
3. **Merge two sparse geometries into one predicate.**
   For R=2^N∪3^N, P_2(x) is recovered by R(x)∧R(2x),
   and P_3(x) by R(x)∧R(3x), for positive x (including 1).
   Each test rejects the other base except the shared unit.
   Tong's source discussion records IP of this expansion.
   It therefore fails the NIP condition, despite escaping
   any single-base automatic representation.
4. **Import a dense-pair non-distal witness.**
   A proper dense elementary predicate in a real ordered
   structure has the desired model-theoretic behavior in
   familiar examples. Z has isolated points and no proper
   dense subset in its order topology. A unary subset of
   Z is not such a pair; the attempted transfer would need
   a definable quotient or interpretation with NIP and
   non-distality checked in the full ordered expansion.
   No such construction was supplied.
5. **Derive strong honest definitions from NIP alone.**
   NIP bounds shattering of R(x+y)-type families. The
   sparse proof instead uses dominance and eventual
   periodicity of operators to select uniform representative
   formulas. The attempted extension lacks a finite
   representative family without those hypotheses.
   General NIP theories need not be distal, so this missing
   combinatorial selection lemma cannot be replaced by
   the NIP assumption alone.

Outcome: five failures, with no new exact catalog decision.

## Q3268: distal expansions of Mekler groups

The primary paper's Question 4.29 is exactly the general nice-graph
question, not only the case where an order already makes C distal.
Its proposed valuation route was read in the local paper.

1. **Transport the distal graph expansion through interpretation.**
   Interpreting C in M(C) transports graph data, but the
   group also has an infinite central vector space and
   infinitely many finite-support combinations. Its fibers
   are not bounded finite sets. Distality of the interpreted
   graph does not prove distality of the larger group.
2. **Name all elements or a basis to eliminate stability.**
   Constants fix automorphisms of one presented model;
   they do not eliminate indiscernible types in elementary
   extensions. Naming a basis likewise leaves arbitrary
   finite sums and central directions. No proof that the
   resulting complete theory is distal follows.
3. **Add the full support relation on a named vector basis.**
   This is actively harmful. In M(C)/Z, if S(x,e_i) means
   that basis vector e_i has nonzero coefficient in x,
   then for every subset I of {1,...,n}, the sum of e_i
   over I realizes exactly that support pattern. S has IP.
   A proposed expansion revealing all coefficients cannot
   be distal, since it is not even NIP.
4. **Add only a leading-support valuation.**
   This avoids the full-support IP witness, and is the
   natural serious route. But compatibility of a central
   valuation with all commutators and the chosen graph
   enrichment still needs QE or a strong-honest-definition
   theorem for the resulting group theory. The attempted
   construction has not supplied that theorem, especially
   when the given distal graph expansion is not an order.
5. **Disprove expandability using infinite burden.**
   The source lower bound on burden counts arbitrarily
   many independent directions. Distal theories can have
   unbounded dimension; finite burden is not a prerequisite
   for distality. Thus that dimension lower bound alone is
   no obstruction to a distal expansion. No expansion-
   invariant stable configuration was isolated instead.

Outcome: five failures. The support-predicate IP witness is about
that proposed expansion, not about every distal expansion.

## Q3482: categoricity below the halting degree

The source distinguishes d-computable isomorphisms between computable
copies from categoricity relative to d among all d-computable copies.
The catalog explicitly asks the former, weaker property. All routes
here retain that convention. The local thesis Section 2.4.2 was read.

1. **Start with order type ω as a low-degree example.**
   Its standard copy is computable, but a computable copy
   can place an extra point between a labelled pair exactly
   when a machine halts. Enumerate the pairs in order and
   insert a point when the corresponding computation halts;
   comparisons of existing labels never change. The order
   remains ω. Any isomorphism to standard ω decides which
   labelled endpoints are successive and hence the halting
   set. Thus ω cannot witness a degree strictly below 0′.
2. **Relativize the finite-successivity characterization.**
   A finite list of adjacent pairs is sufficient for
   computable categoricity. For an arbitrary computable
   order with infinitely many adjacent pairs, their
   adjacency relation is Π⁰₁, and choosing the sites for
   a halting coding may itself require 0′. The proposed
   relativization lacks a uniform computable sequence
   of suitable coding intervals. The ω argument does
   not immediately generalize to every order.
3. **Encode a chosen incomplete c.e. degree in finite blocks.**
   A computable block order can reflect the enumeration
   of that c.e. set. To prove d-categoricity, however,
   one must compute an isomorphism from d for every
   computable copy, including copies whose block
   boundaries code unrelated 0′ information. The
   construction controlled its own copy only. It has
   no uniform recovery argument for all copies.
4. **Transfer the Boolean-algebra theorem.**
   A Boolean algebra's atoms support operations that
   identify finite partitions. A linear order has only
   comparison; replacing atoms by intervals does not
   give the same definable Boolean operations or the
   required computable back-and-forth. No effective
   interpretation preserving these categoricity
   properties was constructed.
5. **Priority construction against computable isomorphisms.**
   Diagonalizing by splitting a finite interval can
   destroy a candidate computable isomorphism. The
   simultaneous requirement that one incomplete d
   compute isomorphisms to every computable copy
   needs restraints on exactly those splitting events.
   No verified injury strategy meeting both families
   of requirements was obtained. A generic graph
   coding theorem does not preserve the order class.

Outcome: five failures. No transfer between the two categoricity
conventions is counted as a solution.
