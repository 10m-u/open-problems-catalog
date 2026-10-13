# Proof complexity: full-target stopping record

These questions concern the strongest systems stated in the catalog. A failed
translation or a lower bound for a weaker system does not settle either one.
Each numbered route below counts once; source reading and finite checks do not
add failures.

## Q3668 — cyclic arithmetic versus PA shortest proofs

**Five full-target failures; unresolved.** The local source is
texts/collections-5b517b8c700cac7d.txt.gz. The question uses classical ordinary
sequent calculi with cut and symbol-count size, not cut-free or intuitionistic
subsystems.

1. **Automaton determinization witness.** Translate the descending-trace
   acceptance condition of a cyclic proof into a deterministic automaton and
   then a PA induction argument. Exponentially many deterministic states can
   be necessary for an automaton language. To turn this into the desired
   separation one would need every PA proof of the arithmetic conclusion to
   recover such a deterministic automaton. No such extraction was obtained:
   PA may prove the conclusion by another induction invariant or by cuts.
   Blow-up of this translation is an upper bound on a construction, not a
   lower bound on the shortest PA proof.
2. **Unfolding shared diamonds.** An n-layer directed proof graph with two
   alternatives per layer unfolds into exponentially many branch paths.
   Counting these paths gives a candidate separation from a tree proof.
   But PA with cut can introduce a lemma for a shared suffix and reuse it.
   Even ordinary tree sequent syntax can avoid replaying a long proof by
   using the cut formula in its continuation. No argument excludes short
   lemma-based PA proofs of the proposed conclusions. The path count
   therefore measures an unfolding, not the allowed proof minimum.
3. **Hard propositional family embedded in arithmetic.** Encode a family of
   propositional tautologies as closed arithmetic sentences, intending to
   use an exponential propositional lower bound and cyclic descent to
   certify them. A lower bound for resolution or cut-free sequents does
   not survive arbitrary arithmetic cuts and induction. This route needs
   both short cyclic proofs of this family and a restriction/extraction
   theorem converting *all* PA proofs to a system with the requisite lower
   bound. Neither was proved. The embedding alone establishes neither
   requirement.
4. **Finite consistency instances.** Let the conclusion assert absence of
   a contradiction among PA proofs of length at most N, hoping that cyclic
   descent yields a short verification while incompleteness forces PA
   proofs to be exponentially long. Gödel's obstruction concerns the
   unbounded consistency assertion. Each fixed finite instance is a
   different PA-provable sentence; absence of a proof of the universal
   sentence supplies no numerical lower bound for its instances.
   No short cyclic certificate with a matching PA length lower bound
   emerged. Formalizing finite trace soundness can itself use PA induction,
   so that step cannot be assumed to produce the separation.
5. **Counting small cyclic proofs.** There are at most
   \(2^{O(s\log s)}\) directed proof descriptions of symbol size at most s
   (after fixing the finite proof alphabet). PA descriptions up to the
   proposed bound \(L=2^{s^\epsilon}\) have a vastly larger budget,
   \(2^{O(L\log L)}\). A pigeonhole argument from small cyclic descriptions
   therefore has no shortage of PA descriptions to exploit. Moreover
   descriptions can share conclusions. Counting does not force any cyclic
   conclusion to require a PA proof of size L.

These are five failed attempts to establish the quantified shortest-proof
separation, not evidence that polynomial simulation exists.

## Q3824 — polynomial-line CP for all Tseitin CNFs

**Five full-target failures; unresolved.** Here F is the direct CNF encoding
of odd-charge Tseitin constraints on a simple graph; the resource is number
of Cutting Planes lines in terms of the actual CNF encoding length. Coefficient
bit length is unrestricted. The source
texts/papers/collections-f62ec84ea0debfbf.txt.gz, Theorems 1.2–1.3, gives
quasipolynomial simulations and a \(|F|^{O(\log m)}\) upper bound, not the
fixed polynomial requested here. [Primary paper](https://www.theoryofcomputing.org/articles/v022a002/).

1. **Sum the vertex parity equations.** Writing
   \(\sum_{e\ni v}x_e=2q_v+c_v\), then summing over v, immediately
   contradicts odd total charge because every edge occurs twice. But the
   quotient variables \(q_v\) are new variables, and CP starts with the
   original CNF inequalities. Introducing them with parity equations is
   an extension of the stated system, not a CP derivation. No polynomial
   original-variable derivation of these parity identities was obtained.
2. **Balanced branching and merging.** Branch on sums over balanced vertex
   sets, obtain a shallow Stabbing Planes refutation, and merge the branches
   in CP. The source's conversion incurs a factor
   \((cn)^{\log s}\) for SP size s and coefficient bound c. Even polynomial
   s and c leave a logarithmic exponent. A disjunction of branch conclusions
   is not a CP line; no polynomial merging lemma eliminating this factor
   was derived.
3. **Absorb the loss into the CNF length.** At a vertex of degree d the
   direct parity CNF has \(2^{d-1}\) clauses, so for some high-degree graphs
   a large construction is polynomial in its explicit input. On
   bounded-degree graphs, however, \(|F|=\Theta(n)\), up to ordinary
   variable-encoding logarithms. Then \(n^{O(\log n)}\) cannot be bounded
   by a fixed polynomial in \(|F|\). This parameter conversion does not
   cover the quantified graph class.
4. **Turn depth lower bounds into a negative answer.** A line-count bound
   must exceed every fixed power of \(|F|\) to refute the question.
   Any depth lower bound D only implies at least D lines. Polynomial depth
   lower bounds, including superlinear ones, remain compatible with
   polynomial line counts. Coefficient-restricted lower bounds also do
   not apply to the unrestricted target. No superpolynomial unrestricted
   line lower bound follows from this route.
5. **Leaf and separator elimination.** For a tree, remove a leaf. Its parity
   constraint forces its incident edge value, simplify the neighbor's
   clauses using that unit, and continue; odd total charge ends in an
   empty clause. A unit simplification is a CP addition: cancel the
   resolved literal by its opposite unit inequality. Thus this is a
   polynomial-line refutation for trees, and bounded-width separator
   dynamic programming gives useful restricted families. For arbitrary
   graphs the boundary records can have \(2^{\mathrm{width}}\) assignments.
   A balanced separator has no guaranteed logarithmic width, so this
   construction fails to supply the required universal polynomial.

No claim is made that Tseitin is exponentially hard in CP: that older
conjecture is already refuted by the quasipolynomial upper bound. The tree
observation is a restricted result, not closure of Q3824.
