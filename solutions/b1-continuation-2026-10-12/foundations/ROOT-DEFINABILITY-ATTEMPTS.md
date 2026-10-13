# Fixed alternation and relative existential definability

These are new continuation routes for Q1375, Q1376 and Q1481. The original
Part IV semidecision, SCC triage, ultimately-periodic relative case and
normalization obstruction remain prior partial results; merely rerunning
them adds no failures. Each question below has five new proposed full-target
routes with the exact failed inference identified.

The local survey is texts/papers/collections-8ab70c73fdf607cd.txt.gz,
Sections3–4, especially Theorems1–4. BA_p uses the base-p valuation relation,
not just the power predicate. Coefficients are encoded in binary and p is
fixed. A switch means a change between existential and universal blocks;
we retain the explicit prefix whenever convention matters.

## Q1375: exact complexity at every fixed alternation

1. **Boolean-game reduction.** Restrict every quantified variable to {0,1}
   and replace a propositional atom by x=1. Existential restrictions are
   conjuncts; universal restrictions are implication antecedents.
   This gives the usual polynomial-hierarchy hardness for each prescribed
   starting block and switch count. It supplies no matching upper bound
   for unbounded integer witnesses or valuation constraints. Thus it
   settles a lower-bound slice, not the exact arithmetic complexity.
2. **Online alternating automaton.** Try to avoid repeated determinization
   by alternating choices of quantified *bits* as each input column is
   read. Quantification of a whole integer must instead commit all its
   bits before the next quantified integer. Concretely,
   \(\exists y<4\ \forall z<4:\lfloor y/2\rfloor=z\bmod2\)
   is false. In the LSB online game, first choose y's low bit0, observe
   z's low bit, and choose y's high bit equal to it; the remaining
   z bit does not matter. That interleaved game is true. The matrix
   here is even a finite disjunction of linear equalities, so this
   is not an exponentiation issue. The proposed alternating machine
   decides the wrong quantifier dependence.
3. **Representation lower bound as a decision lower bound.** Minimal NFAs
   after universal projection can require doubly exponential states.
   Try to infer the matching exact BA decision lower bound from that
   language size. An emptiness algorithm need not emit a minimal NFA,
   and arbitrary input NFAs have no free polynomial-size encoding by
   quantifier-free BA formulas. The arithmetization itself uses quantifiers.
   No size-and-prefix-preserving reduction establishing the desired
   decision lower bound was constructed. This failure differs from
   A2's wrong bit game: it concerns a lower-bound transfer.
4. **Iterate exponential rulers.** The updated primary paper proves
   EXPSPACE-hardness for E*A*E* and 2-EXPSPACE-hardness for E*A*E*A*.
   Attempt to nest its ruler/width construction at every additional
   switch. A width macro is not an atomic predicate: its existential
   witnesses and the universal checks inside ruler guards move through
   positive and negative implication positions. Replacing each width
   symbol by the preceding construction does not automatically append
   exactly one block, and can duplicate the defining formula. No
   polynomial-size uniform tower-ruler construction with controlled
   prefix was proved. The source's two specific prefixes therefore
   do not become a theorem for every k by iteration.
5. **Polynomial numerical game bound.** Guess polynomial-bit witnesses
   at each existential block and restrict universal blocks to the same
   polynomial-bit domain. If uniformly sound for a fixed E*A*E* formula,
   this would give a polynomial-hierarchy decision algorithm, hence
   membership in PSPACE. Its EXPSPACE-hardness contradicts this by the
   deterministic space hierarchy theorem. Thus this proposed bound cannot
   cover the full fragment. The NP existential theorem supplies no such
   alternating-game bound; a tighter nonpolynomial bound is still needed.

Full outcome: five failed exact-complexity routes. The source's NP
existential result, specific higher-prefix hardness and conservative
elementary fixed-prefix upper bounds are retained, without inventing a
matching classification.
[Updated primary paper, Sections6–7](https://arxiv.org/html/2306.10432v5).
Its February2026 revision still distinguishes the known hardness from the
unresolved exact arbitrary-fixed-prefix classification.

## Q1376: existential BA_p definability of a regular unary set

Let K be the numbers represented by (01|10)* in base2, including0.
Its canonical language is {0} ∪ (1|10)(01|10)*, with intermediate
exponential growth; the source's growth-gap theorem excludes an
existential BA₂ definition.

1. **Bound the generator parameters.** The source characterizes existential
   languages by finite unions/concatenations from C_(ell,m). A fixed
   ell,m representation test is decidable. Try to bound ell,m by the
   input minimal DFA. Pumping bounds behavior in the target automaton,
   but generator congruences can have much larger moduli and be hidden
   by unions. For example all residues modulo an arbitrary m can be
   unioned to the same fixed small full-number language. This does *not* disprove
   a bound on the smallest representation; it shows that bounding every
   representation is the wrong lemma. No elimination of redundant
   large generator parameters preserving the allowed atom class was
   obtained, so the needed minimum bound remains unproved.
2. **Bounded affine growth tests.** Strengthen prior SCC triage by testing
   all preimages L(an+b), but use a fixed coefficient cutoff B. Choose
   a prime q>B and
   \(M_q=\{x:x\not\equiv1\pmod q\}\cup\{qn+1:n\in K\}\).
   This is regular and not existential BA₂-definable, since substituting
   qn+1 would define K. Yet for every 1≤a≤B and every b, its affine
   preimage contains all but one residue modulo q, since a is invertible.
   Its canonical growth is consequently full, not intermediate.
   Every test at that fixed cutoff misses the obstruction. A cutoff
   depending effectively on the input automaton might work, but neither
   its completeness nor such a bound is proved here.
3. **Finite syntactic-monoid images.** Reduce language representations to
   operations on subsets of the input syntactic monoid. This loses word
   coverage. For every regular L choose one representative word from each
   attained accepting monoid element. The finite language A of those words
   is existentially definable and has exactly the same monoid image as L.
   In particular this holds for K, which is not existentially definable.
   An image-only existential-representation test therefore accepts every
   regular language and is false. Saturating A to recover L is not an
   operation known to preserve the allowed language class.
4. **Existentially encode a deterministic run.** Introduce integer bitsets
   for states at every digit position, then try to impose all local
   transition conditions existentially in BA. A finite run is determined
   by its input, but its verification is a condition at *every* active
   bit position. Bitwise subset/disjointness would replace these checks
   by existential equations in the AND expansion, whose existential
   theory does express all regular sets (source Theorem4). Valuation
   alone does not supply that binary bitset operation. A uniform
   existential BA implementation would define K and contradict the
   proven strictness. Uniqueness of a run does not remove its validation.
5. **Forbidden regular sublanguage basis.** Try to decide existential
   definability by absence of a finite list of nondefinable regular
   sublanguages, starting with K. The full language is existentially
   definable and contains K, so this rejection rule already returns
   a false NO. Neither upward nor downward closure under arbitrary
   regular-language inclusion holds: the empty definable language also
   lies inside K. A different ordering with a proved finite obstruction
   basis is needed; inclusion itself cannot support this algorithm.

Full outcome: five failures. The old positive semidecision and exact triage
remain, without a terminating NO test. The new finite-cutoff counterexample
and monoid-image obstruction identify specific failed enhancements.

## Q1481: existential definition relative to an input unary predicate

1. **Promote the weakest nonperiodic predicate to existential universality.**
   The source's Bès result gives first-order definability of powers from
   any non-Presburger automatic predicate. Try to turn it into every
   regular predicate's existential definition. Take R₂=P₂ and R₁=K.
   P₂ is itself nonperiodic, but the weaker powers-only structure cannot
   define K even first-order, by source Theorem1. The claimed universal
   transfer is false. First-order definability of powers is far less
   than a definition of the valuation relation or all regular predicates.
2. **Apply the absolute BA growth obstruction.** Test R₁ by the same
   polynomial/full-growth gap used for Q1376. With R₂=K and R₁=K the
   definition R₂(x) is quantifier-free and thus existential, despite
   intermediate growth. This is an exact false NO. The arbitrary input
   predicate lies outside the absolute existential BA class; its use
   cannot be erased while applying that class's growth theorem.
3. **Pack a universal ternary predicate into one unary word.** Encode the
   regular ternary AND relation by interleaving three bit tracks into a
   single regular unary language, then invoke the source's existential
   universality theorem for AND. Decoding requires the graph of the
   packing map from three numerical coordinates. Its output can have
   three times their maximum bit length. A synchronized automatic
   function has at most a fixed additive length increase, so ordinary
   automatic arithmetic cannot supply this uniform interleaving map.
   No existential definition of the needed packing relation *using*
   the new unary predicate was obtained. A regular encoding of tuples
   by words is not yet a usable numerical interpretation.
4. **Extend the positive language algebra by one atom.** Add L₂ to the
   C_(ell,m) union/concatenation generators and use that as a relative
   characterization. There is an explicit negation obstruction.
   The complement of K is existential BA₂-definable: some aligned
   base4 digit is 0 or3 below the highest active digit. Choose h=4^j≤x,
   write x=u+d h+r with d∈{0,3}, 0≤r<h, and require u=0 or
   V₂(s,u) with s≥4h. The condition h=4^j is V₂(h,h) and
   h≡1 mod3. All coefficients are fixed, so this is existential.
   Now let L₂ be this complement. Adding its already-existential
   language to the positive algebra adds no expressive power, yet
   ¬R₂(x) defines K quantifier-free in the relative structure.
   Hence the proposed positive characterization misses a true YES.
5. **Use self-embedding preservation.** Try to recognize definability
   from invariance under self-embeddings of (N,0,1,+,R₂,≤).
   Any such embedding fixes1 and therefore every standard numeral
   by addition; it is the identity. Thus every unary subset passes
   this preservation test. In particular K passes with R₂=P₂ although
   A1 proves it is not definable there. Embeddings of elementary
   extensions may constrain existential definitions, but no effective
   finite criterion for them is supplied by the input automata.

Full outcome: five failures; the original uniform positive semidecision
and ultimately-periodic R₂ decision case are preserved. All R₂ in these
routes are unary as required by the catalog. None silently substitutes
the ternary AND relation as the actual input signature.

Bounded controls and the concrete Boolean game are in check_definability.py
and ROOT-DEFINABILITY-CHECK.json. They verify examples, not unbounded
definability decisions or complexity classes.
