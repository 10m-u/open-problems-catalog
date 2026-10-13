# Q3846: four-parameter coefficientwise total positivity

13 October 2026. The target is every finite minor of the triangle

    T(n,k)=[a(n-k)+c]T(n-1,k-1)+(dk+e)T(n-1,k),
    T(0,k)=delta_(k,0),

with coefficients in Z[a,c,d,e] all nonnegative. I read the actual
[2021 Conjecture 1.3 and its d=0 theorem](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2021/30Chen.pdf),
and the [2026 numerical Eulerian TP3 result](https://arxiv.org/html/2608.29224v1).
Neither supplies this full coefficientwise four-parameter conclusion.
The known planar proof at d=0 is not claimed as a new result here.

Five routes below fail on the full target. Actual triangle minors in the
bounded controls have nonnegative coefficients. Auxiliary negative minors
are tests of proposed sufficient constructions, not catalog counterexamples.
[check_four_parameters.py](check_four_parameters.py) and
[FOUR-PARAMETER-CHECK.json](FOUR-PARAMETER-CHECK.json) contain exact checks.

<a id="a1"></a>
## A1: a constant nonnegative production matrix

Try to realize T as the output matrix of a single coefficientwise TN
production matrix P, with T shifted by one row equal to T*P. Since the
diagonal of T is c^n, P is uniquely forced over the rational-function
field. Its first offending entry is

    P(2,1)=-a*e*(a*e+c*d)/c^3.

It is strictly negative at a=c=d=e=1. Multiplying rows or columns of this
forced P by positive diagonal factors cannot change that entry's sign.
This does not exclude changing the output triangle by time-dependent row
scalings and deriving a different production matrix. Thus the usual
nonnegative-production sufficient theorem cannot be applied to this output
representation. Another factorization or different output encoding would
be needed. Failure 1.

<a id="a2"></a>
## A2: a planar birth/stay network with common edge weights

Each entry is a positive weighted path sum on a two-coordinate lattice:
the coordinates count stays and births; a birth has weight a times the
number of previous stays plus c, and a stay has weight d times the number
of previous births plus e. To turn this into an LGV path matrix, try sources
S_n=(-n,0) and sinks U_k=(-k,k), using horizontal stays and vertical births.
Every S_n-to-U_k path then has n-k stays and k births, exactly as required.
However a vertical edge at horizontal coordinate x must have weight
a(x+n)+c for source S_n. The edge at (-1,0) needs a+c when reached from
S_2 but 2a+c when reached from S_3. A single common network edge cannot
carry both weights if a is an independent variable.

This worked encoding therefore fails the source-independence required by
LGV. The issue is not negativity of entry weights. Expanding a*stays into
decorations records source history and has not produced a common planar
network. The source's different d=0 construction remains valid; the failed
encoding here does not rule out another network for the full family.
Failure 2.

<a id="a3"></a>
## A3: extend an arbitrary TN prefix by the actual recurrence

Try to induct by remembering only total nonnegativity of the preceding
prefix. At a=c=d=e=1, the first two rows of the following prefix match
the actual triangle:

    (1,0,0), (1,1,0), (1,1,2).

Every minor of this prefix is nonnegative. Applying the actual n=3 row
operator to its last row gives (1,5,8,2). The adjacent minor using the
last two rows and columns one and two is 1*8-2*5=-2. The arbitrary third
row is not the actual T(2)=(1,4,1), and no actual negative minor follows.
This refutes the proposed TN-prefix preservation lemma; an induction must
retain further structure specific to actual rows. Failure 3.

<a id="a4"></a>
## A4: transfer numerical minor positivity to coefficient positivity

Numerical row-root arguments can certify signs of certain minors after
nonnegative parameter substitution. Try to use this type of sign theorem
as the coefficientwise conclusion. Even with polynomial entries having
nonnegative coefficients, numerical TP cannot make that transfer. The
matrix

    [[1,1],[2a,1+a^2]]

is totally nonnegative at every a>=0, but its determinant is
(a-1)^2=1-2a+a^2. Thus a negative coefficient can be hidden by a positive
polynomial on the whole parameter orthant. This is an auxiliary matrix,
not a submatrix of T. The 2026 Eulerian order-three result also has a
smaller parameter and order scope. Neither numerical specialization nor
its root argument gives the missing coefficientwise certificate.
Failure 4 on this transfer route.

<a id="a5"></a>
## A5: direct initial minors and positive polynomial elimination

Work with actual entries and seek positive formulas for the initial minors,
then a sign-controlled elimination for every higher order. This gives the
following all-size partial theorem, with no novelty claim.

**Theorem.** Every minor using only columns zero and one has nonnegative
coefficients in a,c,d,e.

The entries themselves are positive recurrence sums. For n>=1,

    T(n,0)=e^n,
    T(n,1)=sum_(j=0)^(n-1) (a*j+c)e^j(d+e)^(n-1-j).

The second identity follows by solving the one-column recurrence, whose
new contribution at step j+1 is (a*j+c)e^j. For 0<=m<n, use T(0,1)=0 to
obtain

    det T({m,n},{0,1}) =
      e^m[(d+e)^(n-m)-e^(n-m)]T(m,1)
      +e^m sum_(j=m)^(n-1)(a*j+c)e^j(d+e)^(n-1-j).

Every factor and summand has nonnegative coefficients: the bracket is a
binomial expansion with its pure-e term removed. This proves the theorem
for arbitrary row gaps, including m=0, without polynomial division.

The checker verifies this identity independently against the source
recurrence and checks further bounded minors. An all-orders elimination
would need every relevant initial minor, not just these two columns.
Determinant condensation introduces differences of products, whose signs
are not controlled by the boundary formula. No uniform higher-order
positive factorization was obtained. Failure 5 on the full target, retaining
the all-size boundary theorem. Stop this target under the five-failure rule;
the full catalog conjecture remains open.
