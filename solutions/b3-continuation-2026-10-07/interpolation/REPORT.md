# B3 continuation: interpolation disk bounds

Date: 2026-10-07. Targets: Q1441 (`60c1fcde2d3a853de2a4`), Q1442
(`137dfefda1eae06911d7`), Q1443 (`6c25aadb176292f25ffa`).

The reconstructed results are a uniform disk theorem through degree five and
an all-degree theorem for equal parameters. The interrupted agent's degree-eight certificates
were not available and are not treated as supplied proofs.

## Exact class and target

After positive scaling, every member of the sampled-value TP class has

\[
 L(P)(u)=\prod_{i=1}^n(u+a_i),\quad 0\leq a_i\leq1,
 \qquad P(z)=\sum_{j=0}^n e_{n-j}(a_1,\ldots,a_n)\binom zj.
\]

The stronger disk target is

\[
 |z+1/2|\leq n-1/2\qquad(P(z)=0).
\]

It implies Q1442's upper bound \(|z|\leq n\). The endpoint
\(a_i=1\) has \(P(z)=\binom{z+n}{n}\), attaining \(z=-n\), so
the upper bound gives \(R_n=n\). Boundary claims refer to this centered
disk, not just to a numerical largest-root computation.

## All-degree theorem for equal parameters

**Proved here.** For every integer \(n\geq1\) and real \(a\in[0,1]\),
every zero of the polynomial with \(L(P)(u)=(u+a)^n\) belongs to the
target disk. If \(0<a<1\), every zero lies strictly inside it. At the two
endpoints the only disk-boundary zeros are \(n-1\) and \(-n\), respectively.

Put \(q_n(z)=n!P(z)\), with \(q_0=1\). Direct summation gives the formal
generating function

\[
 \sum_{n\geq0}q_n(z)\frac{t^n}{n!}
 =\frac{(1+(1-a)t)^z}{(1-at)^{z+1}}.
\]

Differentiating and comparing coefficients proves, for \(n\geq1\),

\[
 q_{n+1}(z)=[z+a-(1-2a)n]q_n(z)
             +a(1-a)n^2q_{n-1}(z),\qquad q_1=z+a.
\]

Write \(w=z+1/2\) and \(\tau=1-2a\). The polynomial
\(q_n(w-1/2)\) is the characteristic polynomial of

\[
 J_n=\tau D_n+i\sqrt{1-\tau^2}\,K_n,
\]

where \(D_n=\operatorname{diag}(1/2,3/2,\ldots,n-1/2)\), and the real
symmetric \(K_n\) has zero diagonal and adjacent entries
\((K_n)_{k-1,k}=(K_n)_{k,k-1}=k/2\), \(1\leq k<n\).
The characteristic-determinant recurrence is exactly the displayed recurrence.

For an eigenvector \(v\) normalized to Euclidean norm one,

\[
 w=\tau\langle v,D_nv\rangle
     +i\sqrt{1-\tau^2}\langle v,K_nv\rangle.
\]

Both inner products are real, \(1/2\leq\langle v,D_nv\rangle\leq n-1/2\),
and, for \(n\geq2\), the maximum absolute row sum gives
\(\|K_n\|_2\leq n-3/2\). Therefore

\[
 |w|^2\leq\tau^2(n-1/2)^2+(1-\tau^2)(n-3/2)^2.
\]

Equivalently, for \(n\geq2\), this supplies the quantitative strengthening
\( |z+1/2|^2\leq(n-1/2)^2-8a(1-a)(n-1)\).

This is strictly below \((n-1/2)^2\) if \(0<a<1\). For \(n=1\),
\(w=1/2-a\) proves the same statement directly. At \(a=0,1\), the
polynomials are falling and rising factorials, giving the stated boundary
zeros. No finite-degree extrapolation enters this argument.

This recurrence identifies a Meixner-type family; the proof above is derived
from the generating function and does not require a theorem about zeros of
orthogonal polynomials outside their usual parameter range.

## Exact certificate scheme for independent parameters

Set \(a_i=x_i/(1+x_i)\), initially \(x_i\geq0\). Use the Cayley map

\[
 z=-\tfrac12+(n-\tfrac12)\frac{1+t}{1-t}.
\]

The disk interior corresponds to \(\Re t<0\). Clearing the positive factors
gives the polynomial

\[
 F_n(t;x)=\sum_{k=0}^n e_k(x)\prod_{j=0}^{n-1}
 [(n+k-j-1)+(n-k+j)t].
\]

Indeed a vertex with exactly \(k\) parameters equal to one gives
\(n!P(z)=(z+k)_n\); the multi-affine interpolation over these vertices
gives this formula. Every coefficient of every summand is nonnegative.

Write \(F_n=b_0t^n+b_1t^{n-1}+\cdots+b_n\). Let
\(\Delta_r=\det[b_{2j-i+1}]_{i,j=0}^{r-1}\), with out-of-range
coefficients zero. Strict Hurwitz stability follows when \(b_0>0\) and
\(\Delta_r>0\), \(1\leq r\leq n\). Also
\(\Delta_n=b_n\Delta_{n-1}\).

Exact reconstruction establishes that, for \(2\leq n\leq5\)
and \(1\leq r<n\), every monomial \(x_1^{d_1}\cdots x_n^{d_n}\) with
\(0\leq d_i\leq r\) has a strictly positive coefficient in \(\Delta_r\).
The per-degree certificate files and exact recomputation are saved alongside
this report. Their 4,816 positive integer coefficients are compressed by
permutation symmetry into orbit records. After homogenizing separately in
each pair \((a_i,1-a_i)\),
these positive coefficients prove \(\Delta_r>0\) on the entire closed cube.
The leading coefficient \(b_0\) vanishes only at all \(a_i=1\), and the
constant coefficient \(b_n\) only at all \(a_i=0\). Hence the disk holds
uniformly through degree five, with boundary only at those two endpoint
polynomials. Degree one is immediate.

## Obstruction to dropping independence

Replacing the Bernoulli sum by an arbitrary distribution is a genuine
enlargement. In degree four the SNN polynomial

\[
 P(z)=\binom z4+\binom{z+4}{4}
\]

has, in the centered variable \(w=z+1/2\), the equation

\[
 24P(w-1/2)=2w^4+43w^2+105/8.
\]

Its zeros include
\(w=\pm i\sqrt{43/4+\sqrt{109}}\), whose modulus exceeds \(7/2\).
Thus the disk claim fails for arbitrary shift mixtures. Its sampled-value
generating numerator is \(1+t^4\), which has nonreal zeros, so this is not
a counterexample in the TP class.

## Remaining research

The all-degree independent-parameter disk target remains open here. A useful
precise conjecture is positivity of every coefficient of every
\(\Delta_r\), \(1\leq r<n\), after the rational parameter change above.
This would prove the target and the boundary classification in every degree.
The interrupted degree-eight claim still needs its exact certificates or an
independent reconstruction. No new result on the all-even-degree Q1441 bound
or the universal real-gap Q1443 bound is claimed.

## Reproduction and sources

Run `python3 checks.py --max-degree 5` from this directory. It checks the
equal-parameter recurrence symbolically through degree nine, recomputes the
integer-polynomial Hurwitz determinants using their Leibniz expansions, and
rewrites `checks.json` and `degree-N-certificate.json`. This is an exact
fixed-degree certificate, not floating-point root sampling. A degree-five
check using Sympy's independent symbolic determinant implementation agreed
with the same coefficient count and extrema; it was slower and is not the
default verifier. No result is promoted to the catalog resolution ledger.

The exact target definitions and parameter representation were read in the
root B3 handoff and the initial report, pp. 27–31
(`solutions/b3-2026-10-06/report-extracted.txt`).
The underlying source is Anna Vishnyakova,
[Polynomials interpolated totally positive sequences](https://arxiv.org/abs/2607.06207).
The stability criterion used in the certificate proof is the classical
Routh–Hurwitz criterion; a primary mathematical reference with a proof is
Olga Holtz, [Hermite–Biehler, Routh–Hurwitz, and total positivity](https://arxiv.org/abs/math/0512591).
