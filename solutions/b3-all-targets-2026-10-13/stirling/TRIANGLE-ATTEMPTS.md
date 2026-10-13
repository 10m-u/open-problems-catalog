# Full triangle TN: five worked proof routes for Q1158 and Q1159

13 October 2026. Both exact catalog targets require **all minors**, for every
integer \(r\ge2\). The five routes below each fail to prove that full scope.
They preserve the accepted all-r TN2 theorem and add an all-r order-three
minor formula. Nothing here refutes either catalog conjecture.

The two targets share recurrences and normalization, so corresponding routes
use the same architecture. This overlap is disclosed: no additional attempt
is counted for a parameter sample, a determinant size, or running a checker.
Each target has five different sufficient-proof constructions: inheritance
under column lifting; a renewal network; Hadamard composition; recurrence
extension; and symbolic Neville factorization.

Primary definitions are [Deb–Sokal, Lemma 1.1](https://arxiv.org/abs/2507.18959),
read from local `texts/papers/collections-ef08a76bc65e2c1f.txt.gz`.
The October 6 report's negative *ordinary production matrix* entries are
preserved prior evidence; rechecking them is not one of these new attempts.
Let \(p=r-1\), \(A=C\) or \(S\), and

\[
H(n,k)=\frac{k!A(n,k)}{(n+pk)!},\qquad
W(n,k)=\frac{(n+pk)!}{k!}.
\]

## Shared worked reductions

### L: lifting an associated TN triangle is insufficient

The original associated numbers use size \(N\), while the questioned
matrix takes entry \((n+pk,k)\). One tempting proof is to establish TN of
the associated triangle and invoke preservation under this column lifting.
The preservation lemma is false even with the associated triangle's support.

Define \(D(0,0)=1\), \(D(N,0)=0\) for \(N>0\), and, for \(k\ge1\),

\[
D(N,k)=2^{-N^2}\mathbf1_{N\ge rk}.
\]

This is TN: its nontrivial part is positive row scaling of the staircase
matrix \(\mathbf1_{N\ge rk}\). The latter is obtained by taking selected
columns of the lower-triangular matrix of ones, a TN matrix (its minors are
zero or one). After lifting, \(B(n,k)=D(n+pk,k)\) has support \(n\ge k\),
but its minor on rows \(2,3\) and columns \(1,2\) is

\[
2^{-((r+1)^2+(2r+1)^2)}
-2^{-((r+2)^2+(2r)^2)}<0,
\]

because the first exponent exceeds the second by \(2r-2>0\).
Thus preserving the support, the zeroth column and TN before shifting is
not sufficient. The missing lemma must use actual associated Stirling
weights; it cannot be a general column-lifting theorem.

### N: the natural labelled-assembly renewal network has signed minors

The labelled-assembly formula is

\[
H(n,k)=[z^{n-k}]g(z)^k,
\quad g_C(z)=\sum_{j\ge0}\frac{z^j}{r+j},
\quad g_S(z)=\sum_{j\ge0}\frac{z^j}{(r+j)!}.
\]

This identifies a natural repeated convolution, or renewal, network. A
standard sufficient way to replace each convolution step by a nonnegative
planar network is TN of the Toeplitz matrix of the atom coefficients.
That sufficient condition fails at explicit low orders.

For cycles, writing \(g_j=1/(r+j)\), its adjacent Toeplitz order-two minor is

\[
g_1^2-g_0g_2=-\frac1{r(r+1)^2(r+2)}<0.
\]

For subsets, \(g_j=1/(r+j)!\) and the order-three Toeplitz minor with rows
\(0,1,2\), columns \(1,2,3\), is

\[
g_1^3-2g_0g_1g_2+g_0^2g_3
=\frac{1-r}{(r!)^3(r+1)^3(r+2)(r+3)}<0.
\]

Therefore the natural local step cannot itself be the path matrix of a
nonnegative planar network. This does not disprove TN of \(H\) or \(A\):
an enlarged state network or a different factorization could avoid these
local step matrices. That additional construction is the precise missing
obligation.

### H: multiplication by the factorial kernel is not a generic TN transfer

Even a successful TN proof for \(H\) would leave \(A=W\circ H\), an
entrywise product. The kernel \(W\) is TN: up to the positive column scale
\(1/k!\), it is the moment kernel

\[
(n+pk)!=\int_0^\infty t^n t^{pk}e^{-t}\,dt;
\]

generalized Vandermonde determinants and the integral determinant identity
give TN (for \(p>0\), strict positivity on distinct positive indices).
However, entrywise multiplication does not preserve TN in general.

The following two rank-two TN matrices have the forms \(1+x_i y_j\) with
strictly increasing positive lists on both sides:

\[
U=\begin{pmatrix}2&3&4\\3&5&7\\4&7&10\end{pmatrix},\qquad
V=\begin{pmatrix}2&6&7\\3&11&13\\5&21&25\end{pmatrix}.
\]

All their order-two minors are positive and their order-three determinants
are zero. But

\[
\det(U\circ V)=
\det\begin{pmatrix}4&18&28\\9&55&91\\20&147&250\end{pmatrix}=-4.
\]

So this full-target reduction needs a theorem for the *particular joint
factorial/convolution kernels*, not two separate TN claims followed by a
Schur-product assertion. The example refutes the attempted preservation
lemma, not either actual Stirling matrix.

### R: the actual recurrence does not extend an arbitrary TN prefix

Take a prefix with trivial zeroth row/column and nontrivial rows

\[
(1,0,0),\quad(1,1,0),\quad(1,1,1).
\]

This prefix is TN. Apply the *actual Stirling birth/stay recurrence* at
\(n=4\) to its third row. Write its first three new entries as

\[
(v_{4,1},\ u_{4,2}+v_{4,2},\ u_{4,3}+v_{4,3}).
\]

The new minor on rows \(2,3,4\), columns \(1,2,3\), is

\[
v_{4,1}-v_{4,2}-u_{4,2}.
\]

For cycles this is \(-p-(2r+1)_{\underline p}<0\). For subsets it is
\(-1-\binom{2r+1}{p}<0\). These prefixes are artificial, not the actual
preceding Stirling rows. The result shows that an induction storing only TN
of the prefix cannot work by generic recurrence preservation. It must
retain an additional quantitative invariant of actual rows. In contrast,
the normalized log-concavity invariant in [HANKEL-TN2.md](HANKEL-TN2.md)
does suffice at order two; no higher-order extension has been obtained.

### E: symbolic Neville elimination gives a positive first minor, not a closure

To avoid the preceding generic-preserver failures, I tried a direct symbolic
Neville-factor proof. For a positive lower-triangular block, its elimination
multipliers are quotients of initial solid minors. An all-size proof would
follow from a positive formula or sign-controlled recurrence for those
initial minors.

The first nontrivial solid order-three minor can be evaluated for all \(r\).
Put

\[
a=(r-1)!,\quad B=\frac{(2r)!}{2(r!)^2},\quad
T=\frac{(3r)!}{6(r!)^3}.
\]

Counting the possible atom sizes, or applying the recurrence, gives

\[
\det(C(n,k))_{n=2,3,4;\ k=1,2,3}
=a^6BT\frac{2r(2r+1)(4r^4+5r^3-8r^2-r+2)}{(r+1)^2(r+2)}>0,
\tag{C3}
\]

\[
\det(S(n,k))_{n=2,3,4;\ k=1,2,3}
=BT\frac{2r(8r^2+21r+7)}{(r+1)^2(r+2)}>0.
\tag{S3}
\]

For (C3), putting \(r=t+2\) makes the last quartic
\(4t^4+37t^3+118t^2+155t+72\), so positivity is explicit for every \(r\ge2\).
For (S3), every displayed factor is positive already for \(r\ge1\).

Here is a symbolic derivation, independent of the parameter substitutions.
Normalize cycle column \(k\) by \(a^k\); subset columns need no normalization.
With

\[
A=\frac{2(2r+1)}{r+1},\quad
D=\frac{2(2r+1)(3r+4)}{(r+1)(r+2)},\quad
E=\frac{3(3r+1)}{r+1},
\]

the subset rows restricted to columns \(1,2,3\) are

\[
(1,B,0),\quad(1,AB,T),\quad(1,DB,ET).
\]

For example, the two-block entries are the labelled-size sums

\[
S(3,2)=\frac{(2r+1)!}{r!(r+1)!}=AB,
\]

\[
S(4,2)=\frac{(2r+2)!}{r!(r+2)!}
+\frac{(2r+2)!}{2((r+1)!)^2}=DB.
\]

The three-block entry has one block of size \(r+1\) and two of size \(r\),
giving \(S(4,3)=(3r+1)!/[2(r!)^2(r+1)!]=ET\). Therefore

\[
\det=BT\{E(A-1)-D+1\}
=BT\frac{2r(8r^2+21r+7)}{(r+1)^2(r+2)}.
\]

For normalized cycles put

\[
A_C=rA,\quad D_C=\frac{2r(2r+1)(3r^2+6r+2)}{(r+1)(r+2)},\quad E_C=rE.
\]

The rows are

\[
(r,B,0),\quad(r(r+1),A_CB,T),\quad
(r(r+1)(r+2),D_CB,E_CT).
\]

The coefficient \(D_CB\), for instance, is exactly

\[
\frac{(2r+2)!}{a^2}
\left(\frac1{r(r+2)}+\frac1{2(r+1)^2}\right),
\]

from the unordered cycle-size pairs \((r,r+2)\) and \((r+1,r+1)\).
The three-cycle entry is
\((3r+1)!/[2a^3r^2(r+1)]=E_CT\). Expansion gives

\[
rBT\{(A_C-r-1)E_C-D_C+(r+1)(r+2)\}
=BT\frac{2r(2r+1)(4r^4+5r^3-8r^2-r+2)}{(r+1)^2(r+2)}.
\]

Restoring column scales contributes \(a^{1+2+3}=a^6\), giving (C3).
Every equality is a rational-function identity reduced from factorial
ratios, so the all-r status does not come from finitely many substitutions.

This is genuine all-parameter order-three progress. It does not supply
initial minors at every height and order. Dodgson's determinant recurrence
expresses a new solid minor as a *difference* of products of earlier ones;
positivity of those products does not control their difference. To close
the Neville proof one must establish the required cross-product inequality
for the exact initial minors, uniformly in height, order and \(r\).

As a scope control, even knowing all minors of order at most three cannot
be used as a generic induction to order four. Let

\[
M_{ij}=1+ij+i^2j^2\quad(1\le i,j\le4),
\]

and decrease \(M_{11}\) by \(1/1000\). The rank-three unperturbed matrix
has positive minors of orders at most three. The checker verifies that
all those minors remain positive after this perturbation, while the
order-four determinant is negative. This is separate from the row-update
obstruction R: it refutes extending *bounded-order determinant signs*;
R refutes extending *a complete TN prefix by a particular row operator*.

## Per-target records

<a id="q1158-a1"></a>
### Q1158 A1 — associated-triangle column lifting

Attempt L: the all-size lifting inheritance lemma is false, including the
correct support and isolated zeroth column. Full cycle target unresolved.

<a id="q1158-a2"></a>
### Q1158 A2 — natural convolution path network

Attempt N: the cycle atom Toeplitz minor is negative at order two. The
natural local renewal network cannot be made planar and nonnegative with
that path matrix; a different state space is needed. Full target unresolved.

<a id="q1158-a3"></a>
### Q1158 A3 — normalized TN plus factorial-kernel TN

Attempt H: the proposed general entrywise-product transfer fails at order
three. A joint-kernel theorem is missing. Full target unresolved.

<a id="q1158-a4"></a>
### Q1158 A4 — TN-prefix induction by actual birth/stay coefficients

Attempt R: an explicit TN prefix becomes negative at order three under the
cycle recurrence. TN alone is not a sufficient induction invariant.
Full target unresolved.

<a id="q1158-a5"></a>
### Q1158 A5 — symbolic Neville closure

Attempt E: (C3) is proved for all integer \(r\ge2\), but the exact
cross-product comparison for arbitrary initial minors is missing. The
all-order conclusion does not follow from bounded-order signs. Fifth
consecutive full-target failure; stop Q1158 pending root count review.

<a id="q1159-a1"></a>
### Q1159 A1 — associated-triangle column lifting

Attempt L applies to subset support too. It disproves the generic inheritance
lemma, with no counterexample to the actual subset matrix.

<a id="q1159-a2"></a>
### Q1159 A2 — natural convolution path network

Attempt N has a different subset calculation: the atom sequence is
log-concave, but its exact Toeplitz order-three determinant is negative for
every \(r\ge2\). Thus checking only its order-two signs does not repair this
network route. A different network is missing.

<a id="q1159-a3"></a>
### Q1159 A3 — normalized TN plus factorial-kernel TN

Attempt H applies to the normalized subset kernel and the same \(W\).
The general TN product theorem needed by this proof is false.

<a id="q1159-a4"></a>
### Q1159 A4 — TN-prefix induction by actual birth/stay coefficients

Attempt R uses the distinct subset row operator and gives
\(-1-\binom{2r+1}{r-1}<0\). The prefix-TN invariant does not close.

<a id="q1159-a5"></a>
### Q1159 A5 — symbolic Neville closure

Attempt E proves (S3) uniformly but leaves arbitrary initial-minor comparisons
uncontrolled. Fifth consecutive full-target failure; stop Q1159 pending root
count review. None of these five failures means the conjecture is false.

## Exact receipt

[check_triangle_routes.py](check_triangle_routes.py) and
[TRIANGLE-CHECK-RESULTS.json](TRIANGLE-CHECK-RESULTS.json) verify the
counter-witnesses, independently compare the new order-three formulas with
recurrence rows, and check all minor orders claimed for the small control
matrices. No large enumeration or extrapolation is used.
