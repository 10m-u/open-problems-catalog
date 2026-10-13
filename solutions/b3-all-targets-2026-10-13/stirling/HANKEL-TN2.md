# Both higher-order Stirling families have coefficientwise Hankel TN2

13 October 2026. Local proof accepted after main-thread mathematical review (ROOT-REVIEW.md#hankel-tn2).
This proves the full separate target **B3C-Q02**, with no priority claim. It
strengthens the known triangle TN2 statement and the finite Hankel controls in
the older B3 packets. It does not prove Q1160, which requires every order.

## Source, definitions and result

[Deb–Sokal, Lemma 1.1 and (1.17)–(1.18)](https://arxiv.org/abs/2507.18959)
define the shifted arrays used here. The locally read primary text is
`../../../texts/papers/collections-ef08a76bc65e2c1f.txt.gz` (relative to the
thesis-catalog home, `texts/papers/collections-ef08a76bc65e2c1f.txt.gz`).
The prior all-parameter triangle TN2 proof is in the submitted
[initial report](../../b3-2026-10-06/B3_Research_Report.pdf), pp.19–21;
its needed argument is rederived below. The
[October 7 checkpoint](../../b3-continuation-2026-10-07/stirling/REPORT.md)
explicitly leaves the present Hankel statement unverified.

Put (p=r-1\ge0), and extend entries outside (0\le k\le n) by zero.
Both arrays have (A(0,0)=1), (A(n,0)=0) for (n>0), and recurrence

\[
A(n,k)=u_{n,k}A(n-1,k-1)+v_{n,k}A(n-1,k),
\]

where

\[
\begin{array}{c|cc}
&u_{n,k}&v_{n,k}\\\hline
C&(n+pk-1)_{\underline p}&n+pk-1\\
S&\binom{n+pk-1}{p}&k.
\end{array}
\]

The falling factorial of order zero is one. Set

\[
f_n(x)=\sum_{k\ge0}A(n,k)x^k,\qquad f_0(x)=1.
\]

**Theorem.** For either family, every integer (r\ge1), and every

\[
0\le i_1<i_2,\qquad0\le j_1<j_2,
\]

the polynomial

\[
f_{i_1+j_1}f_{i_2+j_2}-f_{i_1+j_2}f_{i_2+j_1}
\]

has nonnegative coefficients. No restriction is placed on gaps or on zero
indices.

## 1. Reestablishing triangle TN2

This section concerns the numerical matrix (A(n,k)), not its Hankel matrix.
Define

\[
H(n,k)=\frac{k!A(n,k)}{(n+pk)!}.
\]

Direct factorial cancellation gives, with (N=n+pk),

\[
H_C(n,k)=\frac{N-1}{N}H_C(n-1,k)+\frac{k}{N}H_C(n-1,k-1),
\]

\[
H_S(n,k)=\frac{k}{N}\left(H_S(n-1,k)+\frac1{p!}H_S(n-1,k-1)\right).
\]

Every row (H(n,\cdot)) is log-concave with no internal zeros. Here is the
preservation calculation so this proof does not rely on finite checks.
If (x_k) is log-concave with interval support and

\[
y_k=d_kx_k+c_kx_{k-1},
\]

then log-concavity follows when (c,d) are nonnegative log-concave sequences
and

\[
2c_kd_k\ge c_{k-1}d_{k+1}+c_{k+1}d_{k-1}.
\]

Indeed, expansion of (y_k^2-y_{k-1}y_{k+1}), followed by

\[
x_k^2\ge x_{k-1}x_{k+1},\quad
x_{k-1}^2\ge x_{k-2}x_k,\quad
x_{k-1}x_k\ge x_{k-2}x_{k+1},
\]

leaves the three stated nonnegative coefficient defects. The last inequality
follows from the decreasing ratios on positive support and also holds at zero
boundaries.

For the cycle recurrence use (c_k=k/N,d_k=(N-1)/N). For (n\ge2) and
(1\le k\le n-1), put (Q=N^2(N-p)(N+p)>0). The three defects are

\[
d_k^2-d_{k-1}d_{k+1}=\frac{p^2(2N-1)}Q,
\]

\[
c_k^2-c_{k-1}c_{k+1}=\frac{n(2N-n)}Q,
\]

\[
2c_kd_k-c_{k-1}d_{k+1}-c_{k+1}d_{k-1}
=\frac{2p((n+1)N-n)}Q.
\]

These are nonnegative for (p\ge0). The subset coefficients are proportional
to (k/N), so their defects follow from the second identity. Initial rows and
the ends of support are immediate, proving the assertion by induction.

Write (W(n,k)=(n+pk)!/k!). For (k\ge1),

\[
\frac{W(n,k)^2}{W(n,k-1)W(n,k+1)}
=\frac{k+1}{k}\frac{u_{n+1,k}}{u_{n+1,k+1}}.
\]

Consequently the normalized log-concavity yields

\[
u_{n+1,k+1}A(n,k)^2\ge
\frac{k+1}{k}u_{n+1,k}A(n,k-1)A(n,k+1).
\]

The adjacent row-and-column minor is

\[
\begin{aligned}
&A(n,k)A(n+1,k+1)-A(n,k+1)A(n+1,k)\\
&=u_{n+1,k+1}A(n,k)^2-u_{n+1,k}A(n,k-1)A(n,k+1)\\
&\quad +(v_{n+1,k+1}-v_{n+1,k})A(n,k)A(n,k+1)\ge0,
\end{aligned}
\]

because the last coefficient difference is (p) for cycles and one for
subsets. On positive support, chaining the row ratios first across columns,
then across rows, proves

\[
A(m,i)A(n,j)\ge A(m,j)A(n,i)
\qquad(m<n,\ i<j).
\tag{T2}
\]

If (m<i), the first row entries are both zero. If (i\le m<j), the
upper-right entry is zero. Column zero contains only (A(0,0)=1). These cover
all boundary cases. Thus (T2) holds for the entire infinite triangle.

## 2. The recurrence pairing lemma

**Lemma.** Suppose a nonnegative finite-support array (A) satisfies (T2) and
the birth/stay recurrence above. Suppose, on their used ranges, (u_{n,k})
and (v_{n,k}) are nondecreasing separately in (n) and (k). Then

\[
f_mf_{n+1}-f_{m+1}f_n\ge_{\mathrm{coeff}}0
\qquad(0\le m<n).
\tag{P}
\]

Proof. Extend the recurrence coefficients to all (k\ge0) if necessary; only
the ranges (v_{n,k}) with (k\ge0) and (u_{n,k+1}) with (k\ge0) occur.
The expansions are

\[
\begin{aligned}
f_mf_{n+1}-f_{m+1}f_n
&=\sum_{i,j\ge0}A(m,i)A(n,j)
 [v_{n+1,j}-v_{m+1,i}]x^{i+j}\\
&\quad+\sum_{i,j\ge0}A(m,i)A(n,j)
 [u_{n+1,j+1}-u_{m+1,i+1}]x^{i+j+1}.
\end{aligned}
\tag{E}
\]

For each sum, let (h_n(k)) be its coefficient function: respectively
(v_{n+1,k}) or (u_{n+1,k+1}). Diagonal terms (i=j) are nonnegative by
monotonicity in (n). For (i<j), set

\[
w=A(m,i)A(n,j),\quad z=A(m,j)A(n,i),
\]

so (w\ge z\ge0) by (T2), and set

\[
d_1=h_n(j)-h_m(i),\qquad d_2=h_n(i)-h_m(j).
\]

Separate monotonicity gives (d_1\ge0) and

\[
d_1+d_2=[h_n(i)-h_m(i)]+[h_n(j)-h_m(j)]\ge0.
\]

The entire paired coefficient contribution is therefore

\[
wd_1+zd_2=(w-z)d_1+z(d_1+d_2)\ge0.
\tag{PAIR}
\]

Pairing occurs within the same degree, so every coefficient in (E) is
nonnegative. Finite support makes every sum finite. This proves (P).

For the present arrays all conditions hold. For (n\ge1,k\ge1), the
falling factorial in (u) is a product of (p) positive nondecreasing
factors. The binomial version differs by the constant \(p!\). When (p=0),
both birth coefficients are one. The cycle stay coefficient (n+pk-1) is
nonnegative and separately nondecreasing for (n\ge1,k\ge0); the subset
stay coefficient is (k), independent of (n). In particular (m=0) is
included and (f_0=1) is not discarded.

## 3. All row and column gaps

Put (a=i_1+j_1), (u=i_2-i_1>0), (v=j_2-j_1>0). The required minor is

\[
f_af_{a+u+v}-f_{a+u}f_{a+v}.
\]

Interchanging (u,v) changes nothing, so assume (u\le v). An exact
telescoping identity writes it as

\[
\sum_{t=0}^{u-1}
\left(f_{a+t}f_{a+u+v-t}-f_{a+t+1}f_{a+u+v-t-1}\right).
\]

Every summand is (P) with (m=a+t) and (n=a+u+v-t-1); their difference
is at least one even at (t=u-1,v=u). Therefore every summand has
nonnegative coefficients. No division, specialization at a positive (x),
or passage to a limit is used. This completes the full theorem.

## Controls and scope

[check_hankel_tn2.py](check_hankel_tn2.py) regenerates entries independently
from the labelled-assembly formula, verifies the normalization identities,
checks each paired contribution (not only the final determinant), and checks
irregular-gap minors against the telescoping expression. Its receipt is
[HANKEL-TN2-CHECK-RESULTS.json](HANKEL-TN2-CHECK-RESULTS.json). These finite
controls guard transcription; Sections 1–3 supply all quantifiers.

The theorem proves B3C-Q02. It adds an order-two partial to Q1160 but does not
close Q1160 or B3C-Q03. Numerical triangle TN2 and coefficientwise Hankel TN2
are different assertions, linked here by the recurrence and (PAIR), not by
an identification of the two matrices.
