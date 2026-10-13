# Q1979: Presburger shatter growth — continuation attempts

Research date: 12 October 2026. Full question: for every definable set
system in every model of Presburger arithmetic, is its shatter function
**asymptotic to a polynomial**? This preserves the catalog's exact wording.
The cited semilinear comparator establishes
\(\pi(t)=\Theta(t^s)\) for an integer \(s\geq0\); ratio-equivalence
to a polynomial is stronger. The restricted positive below supplies only
the comparator's \(\Theta\) conclusion. The full target remains unresolved
under either reading. No claim of novelty or external review is made.

Sources read: Eleftheriou–Papadopoulos, *On the global linear Zarankiewicz
problem*, Question 9.3, printed p.60, local
`texts/papers/collections-5af6f28e9439e877.txt.gz`
([primary source](https://arxiv.org/abs/2510.03546v2)); Basit–Tran,
*On the shatter function of semilinear set systems*, Theorem 7.4 and
Lemma 7.2 ([primary source](https://arxiv.org/html/2501.10032v1)).
The former question includes parameters and nonstandard models. The latter
theorem treats dense ordered vector spaces, rather than discrete
Presburger groups.

<a id="a1"></a>

## A1 — divisible-hull transfer

**Proposed full route.** Eliminate Presburger quantifiers, split finitely
many congruence classes, extend each linear family to the divisible hull
of the ordered group, apply the dense-vector-space theorem, and transfer
its exponent back.

**A genuine positive step.** Let \(G\) be an ordered abelian group and
\(D=G\otimes_{\mathbb Z}\mathbb Q\) its divisible ordered hull. Consider
a set system given by a Boolean combination of homogeneous integer
linear comparisons in the object and parameter variables, with a
homogeneous parameter domain. There are no nonzero named constants or
congruence predicates. The object domain may be the positive cone.
Its shatter functions on \(G\) and \(D\) agree exactly.

Indeed, any finite sample and finitely many parameters witnessing distinct
traces in \(D\) have a common positive integer denominator \(d\).
Multiplying every coordinate by \(d\) puts all of them in \(G\),
preserves every homogeneous equality and inequality, and preserves both
domain predicates and the distinction between traces. Conversely any
witness in \(G\) is already a witness in \(D\). Thus the two maxima
coincide for every finite \(t\). In this restricted case Theorem 7.4
supplies the desired integer-power conclusion (or the constant case for
a finite family). A family without enough object points should be treated
on its available sample sizes, rather than assigning a nonexistent maximum.

**Exact affine obstruction.** On the integer line take
\[
 S_{y,z}=\{x:y\leq x\leq z\},\qquad y\leq z\leq y+1.
\]
On a sample of \(t\) integers, every nonempty trace is a singleton or a
pair of consecutive integers. There are at most \(t\) singleton traces,
at most \(t-1\) pair traces, and the empty trace. Consecutive sample
integers attain \(2t\) traces for \(t\geq1\). Thus
\(\pi_{\mathbb Z}(t)=2t\).
On the rational or real line, put all \(t\) sample points in an interval
of length strictly less than one. Every consecutive block of the ordered
sample can be cut out by an allowed interval, and the empty trace is
available. Intervals never realize a nonconsecutive trace, so
\[
 \pi_{\mathbb Q}(t)=\pi_{\mathbb R}(t)
 =1+t(t+1)/2.
\]
Even the exponent changes under divisible-hull extension. Clearing
denominators changes the upper bound \(1\) to \(d\); it does not give
a witness in the original fixed-constant family.

**Outcome:** failed full-Q1979 route, failure count 1. The homogeneous
transfer theorem remains valid. A general comparison theorem must account
for lattice-scale affine constraints, rather than merely preserving
finite rational linear diagrams by scaling.

<a id="a2"></a>

## A2 — quotient-and-fibre induction

**Proposed full route.** In a nonstandard Presburger group \(G\), the
standard integer subgroup is convex and \(G/\mathbb Z\) is divisible.
Use the dense quotient theorem and discrete fibres separately, then add
their exponents. Divisibility follows by choosing, for every standard
\(n>0\), a remainder \(0\leq r<n\) in \(g=nq+r\); the remainder
vanishes in the quotient. A nontrivial quotient is densely ordered.

**Worked obstruction to the proposed recombination.** Take the single
parameter family \(S_y=\{y\}\), in a model with nontrivial quotient.
The quotient family is again all singletons, with shatter function
\(t+1\). Inside a fixed coset the translated fibre family is all
integer singletons, also with shatter function \(t+1\). But the full
family has exactly \(t+1\) traces, not order \(t^2\). Choosing which
coset contains a point and choosing its location inside that coset are
two aspects of the **same** parameter. They cannot be optimized on two
independent copies of a sample.

The corrected route needs a trace-combination theorem for coupled quotient
and fibre parameters, not a product of their separate maxima. The quotient
also lacks a definable section in the language used here. This is not an
obstruction to every possible quotient induction: it pinpoints where the
worked exponent-addition proof fails.

**Outcome:** failed full-target route, count 2. This route addresses
nonstandard scales, whereas A1 compares a discrete family to its dense
hull. Both warn about transferring growth, but the failed operations are
different.

<a id="a3"></a>

## A3 — dimension/rank supplies the arrangement lower bound

**Proposed full route.** Presburger quantifier elimination leaves a finite
collection of linear comparisons and congruences. After fixing residues,
the usual parameter-space arrangement bound is polynomial. Try to identify
its exponent with the parameter rank, and obtain a matching lower bound
from a full-rank parameter cell.

**Worked rank-two comparison.** On \(\mathbb Z^2\), the translated
two-point family
\[
 T_{a,b}=\{(a,b),(a+1,b)\}
\]
has a full two-dimensional parameter domain. On a sample of size \(t\),
there are at most \(t\) singleton traces and at most \(t\) two-point
traces, since every two-point trace must be a horizontal unit edge and
each point has degree at most two in that graph. Thus \(\pi_T(t)\leq
2t+1\). A sample consisting of \(t\) points on distinct horizontal
lines realizes all singleton traces and the empty trace, so
\(\pi_T(t)=\Theta(t)\).

In contrast, the same rank-two parameter domain for
\[
 C_{a,b}=\{(x_1,x_2):x_1=a\text{ or }x_2=b\}
\]
has quadratic growth. On \(A=\{(i,i):1\leq i\leq t\}\), every
two-element subset, every singleton, and the empty subset is a trace,
giving \(1+t+\binom t2\). The arrangement bound is \(O(t^2)\), so
the exponent is exactly two.

The coordinates in each description depend nontrivially on both parameters.
The mismatch is not repaired by deleting an unused parameter or merely
counting a parameter cell's dimension. One must control which arrangement
regions distinguish actual sample traces. The geometric deconstruction in
the dense theorem handles this issue there; a Presburger version preserving
discrete lower witnesses has not been obtained here.

**Outcome:** failed full-target route, count 3. This is a proposed geometric
lower-bound principle, distinct from quotient-fibre factorization.

<a id="a4"></a>

## A4 — NIP and polynomial upper bounds force a pure power

**Proposed full route.** Use the polynomial trace upper bound for Presburger
formulas and the integer-valued VC dimension to conclude that the actual
maximum is comparable to an integer power. This would avoid transferring
the fine dense-space deconstruction.

**Exact insufficiency of that input.** Let \(V\) be the finite-support
binary sequences, with an edge between two sequences differing in exactly
one coordinate. Let the set system consist of its edges, all singletons,
and the empty set. Its VC dimension is two, and
\[
 \pi(t)=1+t+\max_{|A|=t}|E(A)|=\Theta(t\log t).
\]
For completeness, \(|E(A)|\leq \frac12t\log_2t\). Split by the highest
varying coordinate into parts of sizes \(a,b\). By induction their
internal edges number at most \((a\log_2a+b\log_2b)/2\), and the
cross edges form a matching of size at most \(\min(a,b)\). The entropy
inequality \(H_2(u)\geq2u\) for \(0\leq u\leq1/2\), obtained from
concavity and its endpoint values, completes the bound. A full
\(k\)-cube has \(2^k\) vertices and \(k2^{k-1}\) edges. Taking
\(k=\lfloor\log_2t\rfloor\) and adding vertices proves the matching
order of growth. No member contains three points, and an edge is shattered,
so the VC dimension assertion is exact.

This system is not asserted to be Presburger-definable. It proves that the
particular combinatorial input proposed in this route is insufficient:
integer VC dimension plus a polynomial upper bound does not exclude a
logarithmic factor. A new Presburger-specific lower/structure theorem is
still needed. It neither refutes Q1979 nor proves its negation.

**Outcome:** failed full-target route, count 4. The obstruction is to a
coarse VC-bound argument, rather than to a geometric transfer.

<a id="a5"></a>

## A5 — transfer a standard-model asymptotic through completeness

**Proposed full route.** Prove a degree for every standard parameter instance
in the standard integers, then use completeness or elementary extension
to give the same asymptotic conclusion for nonstandard parameters. A
pointwise finite-trace statement does transfer; the proposed asymptotic
step needs more.

**Worked family and exact calculation.** For a fixed \(H\geq0\), take
all intervals \([y,z]\) with \(0\leq z-y\leq H\). If \(H=h\) is
a standard integer, an interval trace is a consecutive sample block of
at most \(h+1\) points. The sample of consecutive integers attains the
upper bound, so
\[
 \pi_h(t)=1+\sum_{\ell=1}^{\min(t,h+1)}(t-\ell+1).
\]
For \(t\geq h+1\), this equals
\((h+1)t-h(h+1)/2+1\), hence has degree one. If \(H\) is a positive
nonstandard integer, for **every standard finite** \(t\) the consecutive
sample fits inside length \(H\), and
\[
 \pi_H(t)=1+t(t+1)/2,
\]
which has degree two. The same defining formula and parameter type of
being a nonnegative integer therefore do not support transfer of the
standard instance's degree. For each fixed finite observation range, a
sufficiently large standard \(h\) agrees with the nonstandard instance.

This also shows the exact missing uniformity: the eventual linear regime
starts at a threshold depending on \(h\), and no standard bound works
for all parameter instances. The asymptotic assertion is not a single
first-order sentence to which completeness may be applied. A uniform
finite classification of parameter types and their growth regimes could
repair the strategy, but was not constructed.

**Outcome:** failed full-target route, count 5. This targets an asymptotic
elementarity step; A1 instead exhibits a fixed standard family's changed
exponent after changing the ambient domain.

## Stopping-count and scope disposition

Five proposed full-target routes have failed as specified. Their objectives
are respectively dense-hull comparison, nonstandard quotient recombination,
geometric rank lower bounds, coarse VC combinatorics, and standard-instance
elementary transfer. A1/A5 both expose scale problems, and A2/A3 both expose
an unjustified lower bound; those overlaps are disclosed rather than being
claimed as independent impossibility results. The parent should accept or
adjust this count after reading the worked arguments. Q1979 itself remains
unresolved, with the homogeneous dense-hull theorem retained as partial.

`check_q1979.py` checks bounded interval maxima, the quotient/fibre toy
counts, both rank-two families, and all vertex subsets of the four-cube
for the hypercube edge bound. Receipt: `Q1979-CHECK-RESULTS.json`.
