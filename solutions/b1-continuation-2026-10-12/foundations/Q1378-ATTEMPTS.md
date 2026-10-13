# Q1378: five finite-expansion quantifier-elimination routes

12 October 2026. Exact full question: does \(BA_k\) have an expansion by
finitely many **definable** functions or predicates whose theory eliminates
quantifiers? Parameters, if allowed for these definitions, can be included
as fixed tracks in the arguments below. None of the five routes settles
the unrestricted question. No novelty is claimed.

Read Kovalyov, *A natural axiomatization of Büchi Arithmetic*, Question
1(4), [primary source](https://arxiv.org/abs/2605.28408), local
`texts/papers/collections-f70a421dfda29eee.txt.gz`; and Haase–Starčak's
DLT2025 survey, Theorem 2, the discussion of bitwise minimum and Open
Problem 6, [primary source](https://doi.org/10.1007/978-3-032-01475-7_1),
local `texts/papers/collections-8ab70c73fdf607cd.txt.gz`.
The existing Part IV result excluding expansions whose positive and
negative atomic definitions are existential is **not** a new attempt in
this packet. A3 tests an added predicate outside that restriction.

<a id="a1"></a>

## A1 — a universal automata-recognition predicate

**Construction attempted.** Add one definable \(U(x,e)\) saying that the
finite automaton coded by \(e\) accepts \(x\). Then every regular unary
predicate would be a single quantifier-free instance, with finitely many
symbols, and the same idea could be extended to tuple tracks.

**Obstruction proved.** Suppose the synchronous padded digit DFA for \(U\)
has \(q\) states. For fixed parameters, choose \(\ell\) past the end
of all parameter digits, and fix the first \(\ell\) object digits to
zero. The remaining unary language, on objects \(k^\ell y\), is
recognized by at most \(q\) states, since every remaining parameter
digit is zero. For a prime \(r>q\) coprime to \(k\), divisibility
by \(r\) remains divisibility by \(r\) after this scaling and needs
at least \(r\) DFA states. Reach the \(r\) distinct normalized
residues by equal-length prefixes, and distinguish them by a continuation
cancelling one residue. Thus no fixed BA-definable relation, even with a
finite parameter tuple, has every unary regular set among its sections.

The full proof and the padding details are also recorded in
`Q1377-ATTEMPTS.md`, A3, where the same obstruction addresses a different
target's universal-comprehension construction. It is counted once here.

**Outcome:** failed full-target route 1. General finite QE need not use
such a universal predicate; arbitrarily complicated terms and formulas
are permitted in the expansion.

<a id="a2"></a>

## A2 — finitely many residues and quotient functions

**Construction attempted.** Mimic Presburger quantifier elimination using
the original \(+\) and total \(V_k\), finitely many predicates for
fixed residues, and finitely many functions
\(f_m(x)=\lfloor x/m\rfloor\). Could the base valuation replace the
remaining infinitely many congruence predicates?

**A term-freezing lemma.** Let \(S\) be the finite set of prime divisors
of \(k\) and the named positive moduli. For any finite list of terms in
this language, there is an arithmetic progression
\(x=A n+B\), \(A>0\), whose modulus has only prime factors in
\(S\), on which every term is affine in \(n\). Prove this by structural
induction, allowing further subprogressions as needed:

* addition preserves affine terms;
* for \(f_m(a n+b)\), refine \(n\) modulo \(m\), making its slope
  divisible by \(m\), so the quotient is affine;
* for \(V_k(a n+b)\) with positive slope, choose a residue \(n_0\)
  where the input is positive. Refine \(n\equiv n_0\pmod{k^L}\),
  with \(L\) large enough that the input changes by a multiple of
  \(k^{v_k(a n_0+b)+1}\). Its valuation is then constant. Zero slope
  gives a constant directly.

Previously established affine forms and constant valuations survive each
refinement. Constants and natural-number terms give nonnegative slopes;
the same eventual argument allows finitely many signed linear comparisons.
Refine once more to freeze every named residue predicate. Every equality
or inequality between affine terms has constant truth for all sufficiently
large \(n\). Consequently **every unary quantifier-free formula in this
particular expansion is eventually constant on some such progression**.

Choose a prime \(r\notin S\). The set \(r\mid x\) is not eventually
constant on any progression with modulus supported in \(S\), since
\(A\) is invertible modulo \(r\). It is definable in BA, so this finite
expansion does not eliminate quantifiers. The argument covers nested
quotient and valuation terms, not just a bounded number of occurrences.

**Outcome:** failed full-target route 2. This is a rigorous obstruction
to a concrete familiar expansion. Arbitrary definable functions, which can
read more than residues and a first nonzero digit, are outside the lemma.

<a id="a3"></a>

## A3 — add a predicate already giving all regular sets existentially

**Construction attempted.** For binary BA, add the unary predicate
\[
 K=[(01\cup10)^*].
\]
The source explains that existential formulas with \(+,\leq,K\) can
define all regular predicates. Perhaps this single powerful symbol also
gives quantifier elimination, avoiding A1's universal evaluator.

**A stronger obstruction than the initial existential-definitions test.**
The predicate \(K\) itself is not existentially definable in the original
BA. But \(|K\cap[0,N)|=O(\sqrt N)\): each pair of binary digits has
only two choices. Allow \(K\) as well as the finite quotient/residue
symbols of A2. Freeze every term on a progression \(x=A n+B\) as in
A2. An atom \(K(a n+b)\) is constant if \(a=0\). If \(a>0\), it
holds for at most \(O(\sqrt N)\) values \(0\leq n<N\), since its
values lie in an interval of length \(O(N)\) and are distinct.

Away from the union of finitely many such zero-density exceptional sets,
all \(K\)-atoms are false and all other atoms have their eventual
constant values. Hence any quantifier-free formula in this expansion is
constant except on a zero-density subset of that progression. For a fresh
prime \(r\nmid A\), divisibility by \(r\) instead has relative density
\(1/r\), strictly between zero and one. It cannot be such a formula.

Thus the candidate provides universal **existential expressive power**,
but fails quantifier elimination. This is an actual candidate containing a
nonexistential predicate, beyond the restriction of the preserved initial
result. Its elementary density proof also handles any finite collection
of zero-density regular unary predicates in place of \(K\).

**Outcome:** failed full-target route 3, demonstrated in the binary case.
It does not exclude arbitrary positive-density or higher-arity predicates.

<a id="a4"></a>

## A4 — force a strict quantifier-alternation hierarchy

**Construction attempted.** In any proposed finite definitional expansion,
the finitely many defining formulas have a maximum quantifier-alternation
depth. Translate its quantifier-free formulas back to BA. If their depth
were uniformly bounded, perhaps a BA predicate at a higher level would
contradict QE.

**Worked translation.** Replace nested function terms by fresh variables
and their total, unique graph formulas. Negated atoms can still use those
same positive graph formulas, because the computed values are unique.
For a finite collection of defining formulas, their prenex prefixes can
be padded to a common alternating pattern. Boolean combinations of
\(\Sigma_r\) and \(\Pi_r\) matrices can be put in
\(\Sigma_{r+1}\) (and in \(\Pi_{r+1}\)), and the outer variables for
term values add at most one block. This gives a fixed alternation bound
depending on the finite expansion, despite arbitrary term depth. It gives
no bound on the length of the equivalent formula.

That conclusion is compatible with BA: arithmetized finite-automaton runs
already define every regular relation with an existential block followed
by a bounded universal block, and hence ordinary \(\Sigma_2\)
formulas. A relation needing unbounded alternations for **expressibility**
does not exist here. Decision complexity of an input syntax and size of
a translation are different issues; non-elementary decision lower bounds
do not contradict this expressive collapse. The proposed hierarchy witness
is therefore absent, rather than merely not found in a finite search.

**Outcome:** failed full-target route 4. This is a negative logical route,
not a failure of a particular finite set of regular symbols. It leaves the
problem of effective or concise QE entirely separate.

<a id="a5"></a>

## A5 — preserve automaton aperiodicity through function substitution

**Construction attempted.** The atomic arithmetic relations have highly
restricted transition maps. Try to bound the groups appearing in every
quantifier-free relation of a finite expansion by the groups appearing in
its finitely many atomic/function-graph automata. Arbitrarily large prime
divisibility languages would then exclude QE.

**Exact failure of the proposed invariant.** Even an aperiodic automatic
function graph can produce a periodic predicate by term substitution.
Take \(f_q(x)=\lfloor x/q\rfloor\), for a prime \(q\nmid k\).
Its graph is the union, over \(0\leq r<q\), of the relations
\(x=qy+r\). Reading least-significant digits, a carry starts at \(r\)
and updates by
\[
 c'=(q y_i+c-x_i)/k
\]
when the result is an integer in \(\{0,\ldots,q-1\}\); otherwise
the transition is undefined. The final carry must be zero. Start with all
possible remainders to recognize the quotient graph.

Every word of length \(L>0\) induces a partial affine carry map of
slope \(k^{-L}\), hence a strictly increasing contraction on its domain.
It has no cycle of length greater than one. For each such map, its powers
eventually stabilize, including the undefined state. The induced maps on
subsets do the same. Thus this finite carry/subset automaton's transition
monoid is aperiodic, including the union over remainders.

But the quantifier-free formula \(q f_q(x)=x\) defines divisibility
by \(q\). Let \(L\) be the multiplicative order of \(k\) modulo
\(q\), and let a length-\(L\) least-significant-digit word represent
one. Repeating it \(j\) times represents a number congruent to \(j\)
modulo \(q\). Acceptance along its repetitions has period \(q\),
so the divisibility language is not aperiodic. Equivalently its residue
transition monoid contains translation by one, of order \(q\).

Function substitution computes a preimage through a functional graph and
implicitly projects the graph's output track. Aperiodicity is not preserved
by that projection. For every fresh prime, the same example starts with an
aperiodic graph, so simply recording the groups of the graph automata is
not a viable invariant. A replacement invariant for the entire automatic
function clone was not proved.

**Outcome:** failed full-target route 5. This is an attempted algebraic
nonexistence proof, different from the finite quotient candidate in A2:
here quotient functions are counterexamples to a closure theorem, rather
than the proposed expansion being tested.

## Disposition

The five routes target universal parameterization, finite congruence/quotient
symbols, a powerful nonexistential unary symbol, alternation-hierarchy
obstructions, and monoid invariants under functions. A2/A3 share a freezing
lemma but concern different expansions and distinct eventual behaviors
(constant versus constant outside a sparse set). A5 explicitly explains
why the first-order definability of function graphs cannot be treated as
quantifier-free substitution without projection. Counts are pending parent
review. Q1378 itself remains unresolved.

`check_q1378.py` verifies a bounded symbolic-freezing example, exact
quotient-graph recognition and its complete transition monoid for binary
\(q=3\), the new cyclic residue map, and the sparse-predicate counts.
Receipt: `Q1378-CHECK-RESULTS.json`. These checks do not decide unrestricted
finite-expansion existence.
