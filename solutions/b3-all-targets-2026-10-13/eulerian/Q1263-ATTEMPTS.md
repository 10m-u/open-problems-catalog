# Q1263: five proposed full combinatorial-interpretation failures

Independent review pending. We require natural interpretations of both
gamma vectors whenever the actual colored polynomial is bi-gamma-positive.
Encoding integers as arbitrary numbered sets does not meet this scope.
The actual words use color-first lexicographic order, colors beginning
at1, and final sentinel(n+1)^1. All methods below were worked explicitly.

<a id="q1263-g01"></a>
## G01 — freeze colors in the classical Foata--Strehl action

Try the uncolored valley-hopping action while leaving assigned colors
unchanged. Actual m=(1,1),r=(3,3) has h=1+13x+4x², degree2, and
a=1+10x+x²,b=3+3x. The all-color1 pair of underlying words12 and21
is a classical two-element orbit with enumerator1+x. An orbit of
the required degree-two gamma form must be(1+x)², x, or x(1+x)
(up to multiplicity), so1+x cannot be such a complete orbit.
It is centered at1/2 instead of either target center1 or3/2.
Thus this literal frozen-color orbit system cannot directly yield
the two gamma bases. Boundary color toggles or a changed action
are needed; no general corrected action was obtained.

<a id="q1263-g02"></a>
## G02 — extend the endpoint-color partition to all colored multisets

The endpoint-color partition does succeed for ordinary permutations
with a common number r>=2 of colors: last color1 or r gives a, and
interior last colors give x b. The all-size involution proof and the
two-letter gamma orbit construction are in ENDPOINT-COLORS.md. Try
to extend that successful structure to repeated letters.

The actual m=(2,1),r=(3,3) has h=(1,36,42,2), a=(1,35,35,1),
b=(1,7,1). But extreme last colors1 or3 give row(1,31,22,0),
while interior last color2 gives(0,5,20,2). They are not the required
symmetric parts. Equality of colored repeated letters prevents
complementing every internal descent; the permutation involution
cannot have the same statistic effect. A corrected multiset state
partition remains possible, but none was obtained generally.
This is a positive subset-partition generalization failure, distinct
from G01's classical frozen-color orbit shapes. The successful
uniform-color permutation and two-letter gamma partials do not
reset the full-target count.

<a id="q1263-g03"></a>
## G03 — decorate uncolored gamma objects independently by colors

Try taking the existing uncolored weakly increasing-tree gamma objects
and assigning independent colors to each occurrence, retaining their
gamma index and symmetric-part type. For m=(1,1), the uncolored
polynomial is1+x, with first gamma vector(1), second zero. There
are9 independent color assignments at r=(3,3). This construction
would merely multiply the old gamma counts, while the actual
colored decomposition has first vector(1,8), second(3), and larger
polynomial degree. The first gamma count remains1, not9, and a new
second part exists. Color changes affect both internal comparisons
and the sentinel descent; they cannot be independent decorations
that preserve the original statistic/type. A statistic-changing
colored-tree bijection remains possible, but none was constructed
for all bi-gamma inputs. The one-letter paired-color partial in
COLORED-RESULTS.md works and does not reset the full-target count.

<a id="q1263-g04"></a>
## G04 — use independent integer choices from reciprocal root pairs

Try to read gamma coefficients as products of independent finite
choices supplied by each reciprocal root pair of the real-rooted
symmetric parts. The actual colored Eulerian input m=(1,1,1,1),
r=(2,2,2,2) has h=a=1+76x+230x²+76x³+x⁴,b=0, and
gamma=(1,72,80). Factoring its gamma into two linear independent-
choice factors(1+u y)(1+v y) would require

    u+v=72, uv=80, u,v=36±8sqrt(19).

These are positive irrational numbers, so they cannot be cardinalities
of finite decoration sets. The real-root proof gives a positive
weighted factorization, not this unweighted orbit interpretation.
The example's gamma interpretation may already be known; we make
no novelty claim and do not count a literature replay. The failed
new full construction is the specified root-by-root integer-choice
method; grouped or dependent objects remain possible. It is an
analytic-to-discrete factorization obligation, distinct from G03's
independent coloring of known uncolored tree objects.

<a id="q1263-g05"></a>
## G05 — a termwise positive gamma insertion recurrence

Use the exact multiplicity-growth operator T_c=[1+(c(M+1)-1)x]+
c x(1-x)d/dx to build all interpretations recursively from smaller
colored multiplicities. Try positive transitions for each individual
gamma-basis object. With M=2,c=3/2, the formal first-part basis
input(1+x)² is bi-gamma-positive, but

    T_c(1+x)²=1+(17/2)x+8x²+(1/2)x³.

Its degree-three second symmetric part is

    b=-(1/2)(1+x)²,

so this individual gamma branch has a negative eta0 transition.
This is a **formal basis test**, not an actual colored input with
those fixed parameters and not a target counterexample. The actual
m=(1,1),r=(3,3) grows to m=(2,1),r=(3,3), producing positive
vectors gamma=(1,32),eta=(1,5); other input branches compensate
for the negative basis transition. Thus the prescribed termwise
nonnegative-object insertion cannot be read off from the differential
operator without extra inequalities, cancellations or a different
state space. No such full combinatorial recursion was found.

The full interpretation remains unresolved after these five proposed
methods. All claimed word rows, gamma transforms and formal witnesses
are exact in check_colored_routes.py and its receipt.
