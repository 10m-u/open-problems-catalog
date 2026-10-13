# Q1454 worked full-target attempts

The exact all-principal-class/all-n target and prior calibrations are in
[SOURCE-SCOPE.md](SOURCE-SCOPE.md). The count below is local and pending
independent root review. No global status or canonical files are edited.

<a id="q1454-a1"></a>
## A1 — a positive RSK avoidance kernel extending the unitary construction

For increasing forbidden patterns the known Rains construction realizes
avoidance counts as moments of |Tr(U)|² for Haar U of a fixed size.
The RSK step uses a restriction on the common tableau shape, preserving
all pairs of standard tableaux of an allowed shape. Try extending this
proof to arbitrary beta by replacing the allowed-shape indicator with
the literal avoidance kernel on tableau pairs, factored as a positive
Gram kernel. Coherent kernels across n would be needed for a fixed
positive operator/measure; even positivity at a single n is a necessary
first step of this prescribed construction.

Let K^beta_lambda[P,Q]=1 if the unique inverse-RSK permutation of(P,Q)
avoids beta, and0 otherwise, for standard tableaux P,Q of shape lambda.
Then a_n=sum_lambda sum_(P,Q)K^beta_lambda[P,Q]. If K were positive
semidefinite, the summand could be written as a squared norm of a sum
of tableau vectors. For a monotone beta, each K is an all-one matrix
or zero, agreeing with the classical shape selection. No such positive
kernel exists for the literal condition of a nonmonotone beta.

**Exact obstruction for every nonmonotone beta.** At n=k=|beta|, only
the permutation beta fails avoidance. All RSK shape kernels are all-one
matrices except the one containing(P_beta,Q_beta), where precisely that
one entry is changed to0. Its tableau dimension is at least2: only
one-row or one-column shapes have a unique standard tableau, and those
shapes correspond precisely to increasing or decreasing permutations.

If beta is not an involution, P_beta!=Q_beta, by RSK's inverse symmetry.
The kernel has one off-diagonal zero and its transpose entry remains1;
it is not Hermitian and cannot be a Gram matrix. If beta is an involution,
P_beta=Q_beta=T. Choose another tableau S of that shape. The principal
two-by-two submatrix on(T,S) is

    [[0,1],[1,1]],

with determinant−1 and quadratic value−1 at vector(1,−1). Thus it is
not positive semidefinite. These alternatives cover every nonmonotone
beta, not just the finite controls.

The actual open-family representative beta=1324 is an involution with
shape(3,1), so it gives the latter obstruction. This proves neither a
negative Hankel minor nor failure of its conjectured moment measure:
the scalar sum of kernel entries is still nonnegative, and a different
Hilbert-space representation may exist. Symmetrizing or changing kernels
would abandon the literal Gram contract and require a new proof.

**Outcome:** one failed full-target sufficient construction. The all-size
first-forbidden-rank kernel obstruction is a retained exact partial.
It is not a rerun of Catalan/atomic Hankel controls, nor a counterexample
to Q1454. Exact enumeration of RSK pairs through length6 is a checker
for the proof and counts zero additional attempts.

<a id="q1454-a2"></a>
## A2 — an active-site production rule for maximum-insertion histories

Avoiders are generated uniquely by inserting a new maximum into a smaller
avoider. Try collapsing that insertion tree to the number of active sites,
then constructing a positive path/production rule as in continued-fraction
proofs. A uniform transition rule on that label, even allowing the current
length as an additional parameter, is a necessary first step of this
particular scalar-state construction. Positivity/coherence of the eventual
operator would be further obligations; a generic generating tree alone
does not prove the moment property.

**Exact failure for every forbidden beta of length k>=4.** Every parent
of length k−2 avoids beta and has k−1 active sites. Every child sigma
of length k−1 also avoids beta. All its k maximum-insertion sites are
active except when sigma is obtained by deleting the maximum k from
beta: for that unique sigma, exactly one site creates beta, so its
active-site count is k−1.

Let tau be obtained from beta by deleting its two largest entries.
It is the unique parent of that exceptional sigma under maximum insertion.
Its child-label multiset is

    {k−1 once, k repeated k−2 times}.

Every other length k−2 parent has child labels k repeated k−1 times.
Since (k−2)!>=2, both parent types exist. They have the same length and
the same active-site count, but different child-label multiplicities.
The proposed quotient is not lumpable. Thus no uniform scalar active-site
transition describes the actual insertion tree for any k>=4.

For the actual beta=1324, parents12 and21 both have three sites. The
children312,132,123 of12 have respectively4,3,4 active sites. The
children321,231,213 of21 each have4. This witness is independent of
RSK tableau positivity; it obstructs a transition quotient, rather than
a Gram kernel. Tracking richer avoidance-prefix states or using an
unrelated continued fraction remains possible.

**Outcome:** a second failed full-target sufficient construction, with
a retained all-beta length>=4 state-collapse obstruction. The finite
checker enumerates literal insertions and treats the unique forbidden
length-k permutation exactly; no avoidance-prefix moment rerun is counted.

<a id="q1454-a3"></a>
## A3 — upgrade scalar enumeration bounds to all Hankel quadratic forms

Try bypassing tableau and insertion states: deduce the moment property
from scalar enumeration constraints, granting even conjectured
log-convexity. The proposed sufficient contract uses nonnegative integer
counts, a0=a1=1, monotonicity, log-convexity, supermultiplicativity,
the factorial upper bound, an exponential bound/known growth constant,
and an actual principal-class starting segment. Direct or skew-sum
closure motivates supermultiplicativity; it is not a substitute for
higher Hankel inequalities. This scalar contract is false, even with
all-n versions of those properties and an actual prefix through n=6.

Define a **formal comparison sequence**, not avoidance counts, by

    b0,...,b5=(1,1,2,6,23,103),
    b_n=512*8^(n−6) for n>=6.

Its first seven terms agree with the actual1342-avoidance counts, and
its exponential growth is8, also the known growth of that class. All
b_n are positive integers and b_n<=n!. For n<=8 the latter is checked
directly; for n>=8 it propagates because b_(n+1)=8b_n and8<=n+1.
The sequence is nondecreasing. Adjacent log-convexity defects through
n=6 are(1,2,10,89,1167,159744); all later defects are0. Thus every
order-two Hankel cross inequality holds, not just a few finite tests.

Supermultiplicativity holds for all m,n. If both indices are>=6,
b_m*b_n=b_(m+n)/512. If only n>=6, use b_m<=8^m for m<=5.
If both indices are<=5, direct checking of the36 pairs suffices.
Consequently the relaxed contract retains these strong enumeration
bounds for every index, and cannot be dismissed for a tail-bound failure.

Nevertheless its degree-four polynomial

    f(x)=x−8x³+x⁴

has a negative moment quadratic form:

    L_b(f²)=b2−16b4+2b5+64b6−16b7+b8=−160.

A representing nonnegative measure would make this integral nonnegative.
Equivalently the five-by-five H0 block has determinant−5959888.
For a structural explanation let q=x³(x−8). Then L_b(q²)=0 but
L_b(xq)=103−8*23=−81; positivity would force every such cross form
with a null vector to vanish. Local ratio constraints have no access
to that higher-order obstruction.

**Outcome:** a third failed full-target sufficient inference, distinct
from RSK kernels and state lumpability. The negative form belongs only
to the explicitly formal sequence. The actual1342 class is already known
Stieltjes; its prefix was used to prevent a trivial initial mismatch,
not counted as a new result or a new calibration attempt. A proof of
actual principal-class higher-order positivity still needs structure
beyond these scalar conditions.

<a id="q1454-a4"></a>
## A4 — a normal extension of the full maximum-insertion operator

Repair the loss of states in A2 by retaining **every** avoiding permutation
as an orthonormal state. Let C e_pi be the sum of basis vectors for the
allowed maximum-insertion children of pi. Each child has a unique parent,
so on finite-support vectors

    C^n e_empty=sum_(pi in Av_n(beta)) e_pi,
    ||C^n e_empty||²=a_n.

This is an exact all-n norm identity for every beta. Try proving that C
has a normal extension: an isometric embedding J into a Hilbert space with
a normal operator N, such that NJf=JCf for every finite-support f. Such
a construction would solve Q1454, because the spectral measure of N at
J e_empty, pushed forward by z->|z|², has nth moment||N^n J e_empty||².
All powers are defined on the root vector by the invariant finite-support
domain. No boundedness of the insertion operator is assumed.

This exact-state operator already violates a necessary inequality on an
actual principal class. A normal extension would imply

    ||C* f||<=||N* Jf||=||N Jf||=||C f||

for finite-support f: C* f is the orthogonal projection of N* Jf onto
the original space. Normality supplies the equality of the middle norms.
Thus the quadratic form C*C−CC* must be nonnegative on that domain.

For siblings q1,...,qj under one parent, write d_i for the active-site
count of q_i. Distinct children have disjoint sets of grandchildren, so
on their span the difference form is diag(d_i)−all_ones. If all d_i>0,
testing coefficients1/d_i shows that positivity requires
sum_i(1/d_i)<=1. This is a concrete positivity obligation of the **full**
operator, not lumpability or a scalar enumeration condition.

For actual beta=1324 and parent1234, all five insertion sites are allowed.
Its children and their active-site counts are

    51234:6, 15234:3, 12534:4, 12354:5, 12345:6.

The reciprocal sum is67/60>1. More explicitly take the integer coefficient
vector(10,20,15,12,10) on those five sibling states. Then

    ||C f||²=4020, ||C* f||²=67²=4489,
    <(C*C−CC*)f,f>=−469.

No normal extension of this prescribed full-state/unweighted creation
operator is possible. In fact the same phenomenon occurs in the already
known positive Catalan case, which emphasizes why the stronger operator
claim cannot be read from the root moment sequence. The checker includes
that as a control, not an extra attempt.

**Outcome:** a fourth failed full-target sufficient construction. It is
related to A2 by the insertion-tree starting point, but removes A2's
scalar-state premise completely and fails a different necessary inequality
on the exact uncollapsed operator. The root norm sequence may still be
Stieltjes through another operator, nonorthogonal states, or other weights.
This is not a negative quadratic form for the actual avoidance Hankel
matrix; f here is a vector of permutation states, not a polynomial in
a nonnegative moment variable.

<a id="q1454-a5"></a>
## A5 — sum/skew renewal decomposition and induction on a smaller class

Try proving the full theorem by splitting each avoider into its unique
indecomposable components, then using a positive continued-fraction
renewal construction. Every beta of length>=2 is indecomposable for at
least one of direct sum or skew sum: a proper initial block cannot
simultaneously be a bottom value interval for one cut and a top value
interval for another. Choose an operation for which beta is indecomposable.
Then Av(beta) is closed under that operation, because an occurrence of
an indecomposable beta cannot use entries from two different sum/skew
blocks. Its indecomposable components themselves avoid beta.

Let i_n count nonempty indecomposable avoiders for that operation, and
I(z)=sum_(n>=1)i_n z^n. Unique component decomposition gives the exact
all-size identity

    A(z)=1/(1−I(z)), B(z)=I(z)/z, B(0)=i1=1.

**Positive conditional reduction.** The count sequence of A is Stieltjes
if and only if the coefficient sequence of B is Stieltjes. Indeed,
if B has a nonnegative normalized S-fraction, the relation
A=1/(1−zB) prepends coefficient1 to it. Conversely a Stieltjes A with
a0=a1=1 has first S-fraction coefficient1; removing that first level
gives B=(1−1/A)/z with the remaining nonnegative coefficients. This
uses the source moment/continued-fraction equivalence, including a
terminating fraction in the degenerate cases. It is a genuine exact
reduction, not a numerical assertion about finitely many minors.

The proposed induction now needs B to be an avoidance-count sequence
for a smaller principal pattern or an already proved positive class.
That closure fails uniformly for beta of length>=4. All permutations
of lengths1,2,3 avoid beta, and their indecomposable counts under either
operation are1,1,3. Hence

    B(z)=1+z+3z²+... .

No ordinary permutation class has three permutations of length2.
Thus B is not the unshifted counting series of **any** classical avoidance
class, let alone a smaller principal class, and this induction does not
return to its hypothesis. Keeping the unshifted I counts would make
i0=0,i1=1, which itself cannot be a nonnegative moment sequence; the
shift is essential rather than an indexing repair one can ignore.

Positivity of the component counts also cannot replace the missing
moment assertion. As an exact nonprincipal control, take layered
permutations with every layer of size1 or2, equivalently avoiding
231,312,321. This class is direct-sum closed and has i1=i2=1 and all
other i_n=0. Thus B=1+z has Hankel determinant−1, and
A=1/(1−z−z²) is non-Stieltjes. The generic Fibonacci obstruction is
already known in the source and is not separately counted; here it
only checks the specified positive-component renewal inference. It is
not a counterexample to the single-forbidden-pattern target.

For actual beta=1324, choose skew indecomposability; the checker directly
counts its components and verifies the renewal identity through n=7.
The transformed prefix is(1,1,3,12,56,289,...) and has no interpretation
as ordinary class counts by the length2 obstruction. A new theorem about
these **shifted indecomposable** enumerations could still solve the
problem, but proving it by principal-pattern induction has not worked.

**Outcome:** a fifth failed full-target proof route. It differs from A2's
maximum-insertion quotient and A4's normal extension: its objects are
unique direct/skew components and its exact positive construction is
S-fraction renewal. It also differs from A3's scalar-bounds relaxation.
The missing inductive family-closure lemma is explicitly false; the
remaining B-moment obligation is equivalent to, rather than already
resolved by, the original question.

## Local stopping disposition

Five distinct proposed sufficient constructions have been worked and
failed at their full-target obligations. Their narrower exact results
are retained, and the full Q1454 conjecture remains unresolved. The local
counter is5 pending root mathematical/scope/count review. No sixth solve
route is begun. A2/A4 share the insertion-tree starting point but address
state quotient and full-operator positivity separately; A1 and A5 use
different RSK and direct/skew decompositions. Known-family controls and
source lookups supply zero additional failures.
