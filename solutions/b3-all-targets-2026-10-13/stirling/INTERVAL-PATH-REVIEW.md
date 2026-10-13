# Independent interval and path-height review

13 October 2026. I read the root's full
[interval packet](../intervals/ATTEMPTS.md), its checker and receipt, and the
earlier [conditional-APP reduction](../../b3-continuation-2026-10-07/compositions/REPORT.md).
I checked the exact Q164 statement against Zhang's thesis,
Conjecture 4.1.8, printed p.57, local
texts/collections-50d43464a7d6a3f4.txt.gz. It includes every path and cycle
power. B3C-Q01 is the all-dimensional symmetric **linear** interval APP
inequality; the bounded-dimensional and laminar results remain partial.

I also read [UPPER-TAIL.md](../paths/UPPER-TAIL.md),
[the path attempts](../paths/ATTEMPTS.md), their checker/receipt, and
the actual [primary source, Corollary 3.15 and §6](https://arxiv.org/html/2609.38084v1),
local texts/papers/collections-f4791b55c6b1d968.txt.gz.
Q4331 concerns A/B despite the appended Motzkin definitions in its catalog
text. Q4332 concerns M/R with the source's length-versus-vertex shift
handled explicitly in the root packet.

## Interval correctness and attempt counts

The five Q164 routes have distinct obligations: actual real-rootedness;
Lorentzian homogenization; closure of the actual three-length recurrence
using only ULC; normalized nonlocal midpoint transport; and cycle-cut
recombination. The five B3C-Q01 routes are real-rootedness; Lorentzian
support; midpoint transport; APP-only constraint intersection; and
rotation-based orbit transport. Shared mechanisms across these two
separate targets are disclosed. I accept five full-target failures for
each, with the following scope qualifications.

The real-rootedness witnesses are actual objects and merely refute a
stronger property. The homogenized domination exponent vectors genuinely
fail M-convex exchange: transferring the excess coordinate 2 to either
deficient coordinate 1 or 3 yields a nondominating set. The symmetric
interval example also fails basis exchange in its homogeneous middle
slice. Neither conclusion is a ULC or APP counterexample.

Midpoint rounding is a valid all-dimensional feasibility construction.
If original integer interval sums lie in [L,U], the difference of either
rounded pair of averaged prefix heights is between the floor and ceiling
of their averaged interval sum, hence also in [L,U]. Adjacent differences
remain binary, and the averaged endpoint rank is the central integer.
The fifteen-to-one antipodal collapse refutes its use as an unlabelled
normalized injection. Reversible labels and a suitable uniform fiber bound
would constitute extra work, not a consequence of feasibility.

The recurrence and cut-state controls test genuinely different closure
lemmas. Their artificial inputs do not contradict actual path/cycle ULC.
The Q01 intersection and rotation controls likewise do not contradict
actual interval APP. The rotation route fails to stay inside a fixed
constraint system; rotating the constraints too would change the system.

**Audit refinement of Q01 A4, at the same attempt count.** Retain the
generic APP family
\[
F=\{0011,1100,1000,0111\}.
\]
Instead of intersecting two arbitrary symmetric families, take the actual
single symmetric interval band \(x_1+x_2=1\).
The intersection is exactly \(\{1000,0111\}\). Its ranks are
\((0,1,0,1,0)\), so \(2c_2\ge3c_1\) fails. Thus an induction remembering
only APP of the old family fails even when the newly added predicate is
an admissible band. The old \(F\) is still not asserted to be an
interval-band intersection. This refinement makes the missing geometric
invariant precise; it is not a new solve attempt.

## Path-height all-size partial proofs

The Q4331 upper-tail normalization proof passes. For
\(W_i=i!(d-i)!/[(n-2i+1)!(n+2i+\sigma)!]\), direct factorial cancellation
gives exactly the two parity ratios displayed by the root. Their numerator
differences after removing the factor two are \(2d+1-4i\) and
\(2d-1-4i\). These are negative throughout the stated formula ranges,
where the denominators are positive and increasing. The linear factors
are log-concave, and each displayed quadratic has negative logarithmic
second derivative wherever positive. The strict lower endpoint on the
inequality ensures that its predecessor also has the single-image formula.
Small empty ranges and the zero constant coefficient cause no exception.
This proves the catalog's degree-normalized inequality in the stated
upper ranges, rather than only ordinary log-concavity.

The Q4332 final nontrivial inequality also passes at every length.
Deleting horizontals preserves maximum height. A Dyck core of semilength
j has 2j+1 insertion slots; excluding height-zero slots leaves 2j-k for
a core with k irreducible components. Multiset insertion then gives
exactly the Motzkin and Riordan table.

For a semilength-m core of height m-2, m>=5 ensures one component attains
that height. The k=1 count comes from removing its enclosing steps:
\(2m^2-11m+12\). For k=2, the other irreducible component has size one
or two, giving \(4m-12\), with order included. For k=3 there are three
placements of the tall component, giving 3. The sum is \(2m^2-7m+3\).
This verifies the component refinement, including why ordinary Catalan
counts for the size-two remainder would overcount k=2.
The four defects have exactly the positive expansions displayed after
m=u+5. Exact smaller-length checks complete the endpoint theorem;
arbitrary interior heights remain outside it.

## Path attempt-count disposition

I accept five distinct full-target failures for each Q4331 and Q4332:
actual root property; a stronger finer-height or normalized invariant;
first-return shape closure; positive-Jacobi spectral transfer; and actual
coefficient/slot formulas with the stated remaining interior gap.
Root properties and ULC failures already anticipated by the primary paper
are identified as prior knowledge, not novelty. The packet nonetheless
works out the precise attempted sufficient contracts and exact witnesses.
No additional attempt is attributed to restarting or enlarging a finite
calculation.

The first-return operation and its length shifts are correct.
Generic sum witnesses do not say the actual summands violate the claim.
The weighted Jacobi controls preserve positive diagonal similarity and
spectral interlacing, so they refute a solely spectral sufficient lemma;
they do not refute the unweighted conjectures. The last routes supply
new all-size partial proofs but leave a specified region uncontrolled,
rather than converting finite full-array checks into closure.

## Independent exact controls

[check_independent_reviews.py](check_independent_reviews.py) and
[INDEPENDENT-REVIEW-CHECK.json](INDEPENDENT-REVIEW-CHECK.json) passed:
4,096 midpoint pairs with every interval checked, the single-band
intersection refinement, four squarefree exact Sturm controls, 248
independent ceiling-count tail formulas, four symbolic parity-ratio
identities, 32 endpoint-table comparisons and four complete Dyck-core
component counts. The independent bounded-ceiling recursion does not import
the root's walk-state DP. These checks support the written proofs and
arithmetic; they are not all-size proof substitutes. No external
peer-review or novelty claim is made.

