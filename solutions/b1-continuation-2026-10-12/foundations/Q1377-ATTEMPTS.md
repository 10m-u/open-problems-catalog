# Q1377: five finite-axiomatization constructions

12 October 2026. Full target: is the complete theory
\(BA_k=\operatorname{Th}(\mathbb N,0,S,+,V_k,\leq)\), for fixed
\(k\geq2\), finitely axiomatizable? The five routes below fail to answer
that question. They are not five counterexamples to finite axiomatizability.
The first two test explicit binary packages; the last three address proposed
general compression/negative-proof methods. No novelty is claimed.

Primary source read: Kovalyov, *A natural axiomatization of Büchi Arithmetic*,
[arXiv:2605.28408v1](https://arxiv.org/abs/2605.28408), local
`texts/papers/collections-f70a421dfda29eee.txt.gz`, Definition 1, Theorem 6,
Remark 1 and Question 1(1), printed pp.3–5,13. Its complete system
contains bounded comprehension, or bounded induction on powers. Its
\(\Pi_1\) matrices allow bounded quantifiers. This packet does not
mistake them for quantifier-free universal axioms. The dated initial report's
universal-axiom obstruction is retained but is **not** counted here.

<a id="a1"></a>

## A1 — keep the finite valuation and order core

**Construction attempted.** Use the finitely many order/addition and
valuation clauses (Add), (Ord0–1), (Mod), (V0–5) from Definition 1, and
derive bounded comprehension rather than postulate it. In base two, this
finite package has the following explicit wrong model.

Let
\[
 G=\mathbb Z[1/2]\times\mathbb Z
\]
with lexicographic order, componentwise addition, unit \((0,1)\), and
domain its nonnegative cone. For a positive element \(x=(a,b)\), put
\[
 V(x)=
 \begin{cases}
  (0,2^{v_2(|b|)}),&b\ne0,\\
  (2^{v_2(a)},0),&b=0,
 \end{cases}
 \qquad V(0)=0.
\]
Here \(a>0\) in the second case, and a dyadic rational has the usual
integer-valued exponent \(v_2\). Its odd numerator is positive. The
powers are exactly \((0,2^j)\), \(j\geq0\), and
\((2^t,0)\), \(t\in\mathbb Z\).

This is a discretely ordered cancellative commutative monoid with successor
addition by the unit. Subtraction between ordered elements stays in the
cone. Every \((a,b)\) has remainder \(b\bmod2\), since its quotient is
\((a/2,\lfloor b/2\rfloor)\). Scaling by two scales \(V\) by two.
If two valuation values differ, the valuation of their sum is the smaller:
for two finite values this is the elementary 2-adic fact for their integer
second coordinates; for a finite and an infinite value the latter has second
coordinate zero; for two infinite values it is the same dyadic 2-adic fact.
Removing \(V(x)\) leaves either zero or a nonnegative element of larger
valuation. A finite positive element is bracketed by standard binary powers;
an infinite one is bracketed by dyadic powers in its first coordinate,
adjusting down one power if its first coordinate is exactly a power and its
second coordinate is negative. Idempotence of \(V\) is immediate. This
checks each of (V0–5), including the order requirement in (V3).

But \((1,0)\) has no quotient/remainder on division by three: an equation
\((1,0)=3(a,b)+(0,r)\), \(0\leq r<3\), would require \(a=1/3\).
Thus even a Presburger theorem fails. No appeal to a merely abstract
nonstandard substructure is needed.

**Outcome:** full-target failure 1. This defeats the specified finite core,
not an arbitrary finite strengthening. In particular one cannot append
finitely many further modulus axioms to this particular split group without
reconsidering its construction.

<a id="a2"></a>

## A2 — replace comprehension by a finite digit Boolean algebra

**Construction attempted.** Add total bitwise union, intersection and
symmetric difference, their generalized Boolean-algebra laws, and a shift
compatible with multiplication by two. Perhaps these finite operations
already provide all bounded digit sets used in the completeness proof.

**An actual richer model.** The model from A1 admits these operations.
Its digit positions form the ordered set
\(T=\mathbb N\sqcup\mathbb Z\), with every bottom position below every
top position. The bottom atoms represent \((0,2^j)\), and the top ones
represent \((2^t,0)\). Codes are precisely subsets satisfying:

* the bottom digit string is eventually a constant \(c\in\{0,1\}\);
* the top string is zero above some bound and eventually the **same**
  constant \(c\) as \(t\to-\infty\).

For \((a,b)>0\), if \(b\geq0\), use the finite binary supports of
the dyadic \(a\) and integer \(b\). If \(b<0\), use the cofinite
two's-complement support of \(b\), and borrow from the lowest top one
in \(a\): remove that one and include every smaller top position.
This gives exactly the displayed code class. Conversely that class recovers
a unique pair \((a,b)\) in the positive cone. It agrees with the source's
digit definition, by splitting off the part below the selected power and
the part above it. Every nonzero code has a least occupied atom, which is
the valuation from A1.

The class is closed under the three Boolean operations: eventual constants
combine by the same Boolean rule on each side of the cut. Shifting every
bottom and top index up one preserves it and corresponds to multiplying
by two. The Boolean identities and shift compatibility therefore hold.
These are genuine total operations; this is not a multiset relaxation.

Now take the bounded formula
\[
 \psi(d)\equiv\exists z\leq d\ (d=3z+1).
\]
On bottom powers \(d=(0,2^j)\), it is true exactly when \(j\) is even.
On top powers it is false, since their first coordinates are dyadic powers
and dividing one by three leaves the group. Below the top power \((1,0)\),
comprehension for \(\psi\) would require a code with alternating bottom
digits forever. Every code's bottom digits are eventually constant, so no
such code exists. The enriched finite Boolean package still does not
derive this one bounded-comprehension instance.

**Outcome:** full-target failure 2. A1 and A2 deliberately share a model,
but A2 verifies additional total operations and a different objective:
finite Boolean digit closure does not entail bounded definable digit
closure. This overlap is disclosed for the parent's count review.

<a id="a3"></a>

## A3 — one universal bounded-formula evaluator

**Construction attempted.** Code bounded formulas or finite automata by
numbers, add one definable relation \(U(x,e)\) evaluating the coded unary
predicate, and replace infinitely many comprehension instances by a single
axiom quantifying over \(e\).

**Exact obstruction.** No BA-definable relation with finitely many parameter
coordinates can have all unary regular sets among its sections. Let a
complete synchronous least-significant-digit DFA for that relation have
\(q\) states. Fix parameters \(e\), and let \(\ell\) exceed the lengths
of all their expansions. Read \(\ell\) zero digits on the object track
and the parameter digits. Thereafter the parameter tracks stay zero, so
the section on objects \(x=k^\ell y\) is recognized by a unary DFA with
at most \(q\) states.

Choose a prime \(r>q\) coprime to \(k\). If that section were
\(r\mid x\), its suffix language would be \(r\mid y\).
This padded digit language needs at least \(r\) DFA states. To see this
directly, read a fixed sufficiently large number \(L\) of digits: the
\(r\) possible normalized residues of the read value are reachable.
Given two distinct residues, a further word whose value cancels one of
them modulo \(r\) accepts that one and rejects the other. Multiplication
by \(k^L\) is invertible modulo \(r\), so both reachability and the
continuation argument are valid in the least-significant-digit convention.
Myhill–Nerode gives the lower bound.

Divisibility by \(r\) itself has a bounded formula
\(\exists y\leq x\,x=ry\). Therefore even a universal bounded-formula
evaluator is impossible. Padding is included in the argument: after the
parameter ends, all longer object representations still have zero parameter
tracks.

**Outcome:** full-target failure 3. This rules out the proposed *definable
universal evaluator* compression. Finite axiomatizability does not imply
that such an evaluator exists, so the full question remains open.

<a id="a4"></a>

## A4 — use incompleteness through arithmetic coding

**Construction attempted.** The source says BA interprets all automatic
structures. Try to code arithmetic computations sufficiently richly to
interpret Robinson arithmetic and invoke essential undecidability against
a finite complete axiomatization.

**Worked obstruction.** A definable multiplication relation on the original
number sort is impossible. Intersect its digit language with the regular
condition \(x=y=k^n\), \(n\geq1\). The resulting least-significant-digit
convolution has the pattern
\[
  A^n B A^{n-1} C,
 \quad A=(0,0,0),\ B=(1,1,0),\ C=(0,0,1),
\]
up to harmless high zero padding. This language is not regular: pumping
the initial block changes its length while preserving the second block,
violating the square relation \(k^n k^n=k^{2n}\). An automatic
multiplication graph would make this regular intersection regular.

More generally, any effective first-order interpretation of an essentially
undecidable arithmetic theory in BA would transfer its sentence decision
problem to decidable BA. Thus the prerequisite for this incompleteness
argument fails, not merely the simple same-sort multiplication coding.
Interpreting all **automatic** structures supplies no such prerequisite.

**Outcome:** full-target failure 4. This attempted negative proof uses
computability of interpretations, not finite digit closure or evaluator
compression. It does not show that a complete finite theory must be simple.

<a id="a5"></a>

## A5 — finite proof search gives an elementary decision bound

**Construction attempted.** If a single sentence \(\theta\) axiomatized
BA, enumerate proofs of \(\varphi\) and \(\neg\varphi\) from
\(\theta\). Combine finiteness with the source's non-elementary lower
bound to obtain a contradiction.

**Worked reduction and exact missing bound.** Completeness does make this
two-sided proof search terminate. For each fixed input length \(n\), let
\(b_\theta(n)\) be the maximum, over sentences of length at most \(n\),
of the shortest proof length of the correct side. It is a finite computable
function: dovetail all those finitely many proof searches until they finish.
If \(b_\theta\) had an elementary upper bound, enumeration over a finite
proof alphabet would give an elementary decision procedure, contradicting
the established lower bound. Consequently a putative finite basis would
have no elementary uniform bound on these proofs.

Finiteness of \(\theta\) does not supply that bound. The source's
automata completeness proof itself incurs unbounded towers as formula
alternations grow. Replacing its infinitely many induction instances by a
finite basis, if possible, need not shorten the resulting proofs. This
route therefore derives a constraint on any proposed basis's proof lengths,
not a contradiction to the existence of a basis. No general theorem that
finite complete axioms imply elementary proof length was established.

**Outcome:** full-target failure 5. The exact failed obligation is the
proof-length upper bound. Computational lower bounds alone do not settle
finite axiomatizability.

## Disposition and checks

The five constructions are respectively finite valuation axioms, finite
Boolean digit operations, definable universal evaluation, incompleteness
via arithmetic interpretation, and proof-search complexity. A1/A2 overlap
in their model but verify different packages; the count is pending parent
review. All five fail at the indicated full-target step. Q1377 is unresolved.

`check_q1377.py` exactly checks the dyadic model's finite core over a
bounded grid (including negative lower coordinates), shift/Boolean code
controls, alternating finite-atom truth, and finite residue-distinguishing
automata controls. Its receipt is `Q1377-CHECK-RESULTS.json`. The infinite
model, evaluator and pumping claims are proved above, not inferred from
these checks.
