# Q1161: third-order row stability

13 October 2026. Five worked full-target routes fail below. The conjecture
is not refuted. A5 proves positivity of the first three Hurwitz
determinants at every size, not all determinants.

I read Deb–Sokal's exact Conjecture 7.7 and setup in
[the primary paper, §7](https://arxiv.org/abs/2507.18959v1), local
texts/papers/collections-ef08a76bc65e2c1f.txt.gz. The target is that all
zeros of both third-order row polynomials have nonpositive real part.
Write \(f_n(x)=\sum_{k=1}^nA(n,k)x^k=xg_n(x)\). Thus the origin root is
harmless, and strict Hurwitz stability of every \(g_n\) would suffice.
Definitions and the assembly identity are in [HANKEL-TN2.md](HANKEL-TN2.md).
I also read Chen–Wang's actual log-concavity proof:
[Theorem 3.1 and §3](https://arxiv.org/abs/2610.09362v1), local
texts/papers/collections-9a577842dae9ce2c.txt.gz. Old B3 generic operator
failures and finite Hurwitz checks are prior evidence, not five new attempts.

For \(P(x)=a_0x^d+\cdots+a_d\), put \(a_j=0\) outside \(0\le j\le d\), and
\(\Delta_j(P)=\det(a_{2v-u+1})_{0\le u,v<j}\). In this convention,
\[
\Delta_1=a_1,\quad \Delta_2=a_1a_2-a_0a_3,\quad
\Delta_3=a_1a_2a_3-a_1^2a_4-a_0a_3^2+a_0a_1a_5.
\]
The strict Routh–Hurwitz criterion is used in this convention.
The negative determinants below concern auxiliary polynomials.

<a id="a1"></a>
## A1 — preserve stability on the known strictly log-concave input class

Applying the actual recurrence to powers of \(x\) gives \(g_n=L_ng_{n-1}\):
\[
\begin{aligned}
L_n^C g&=4x^3g''+((4n+14)x^2+2x)g'
 +((n+2)(n+3)x+n+1)g,\\
L_n^S g&=2x^3g''+((2n+7)x^2+x)g'
 +(((n+2)(n+3)/2)x+1)g.
\end{aligned}
\]
An induction on stable, positive, strictly log-concave inputs of degree
\(n-2\) fails for cycles. At \(n=6\), let
\[
g=(x+1/10)^2(x^2+x/10000+1/100).
\]
The real roots are \(-1/10\), and the quadratic pair has real part
\(-1/20000\). Ascending coefficients are
\[
(1/10000,\ 2001/1000000,\ 1001/50000,\ 2001/10000,\ 1).
\]
All internal log-concavity defects are strictly positive. Its degree,
four, is the actual input degree. Nevertheless \(L_6^Cg\) has ascending
coefficients
\[
(7/10000,\ 25209/1000000,\ 44033/100000,\ 286221/50000,\
57021/1000,\ 272)
\]
and
\[
\Delta_4(L_6^Cg)
=-111702506308959257/1250000000000000000<0.
\]
This strengthens the old unconstrained operator obstruction. These are
not actual rows, and no analogous subset failure is asserted here.
A stronger cycle-specific invariant is required. Outcome: full-target failure.

<a id="a2"></a>
## A2 — deduce stability directly from strict row log-concavity

The polynomial
\[
h(x)=1+(11/10)x+(6/5)x^2+(11/10)x^3+x^4
\]
has positive coefficients and strictly positive internal log-concavity
defects. But \(\Delta_2(h)=11/50>0\) and \(\Delta_3(h)=-121/125<0\).
Strict row log-concavity therefore cannot supply the higher Hurwitz
inequalities. This direct single-row implication differs from A1's
preservation claim for the actual operator. This is not an actual
Stirling row. Outcome: full-target failure.

<a id="a3"></a>
## A3 — turn a positive moment representation into stable polynomial rows

The weighted cycle moment representation in
[CYCLE-HANKEL-ATTEMPTS.md, A1](CYCLE-HANKEL-ATTEMPTS.md#q1160-a1)
motivates strengthening/removing its weight and transferring numerical
moment positivity to row stability. Even a degree-correct unweighted
moment family cannot supply that last implication.

Let \(J\) take \(1,100\) with probabilities \(1-10^{-6},10^{-6}\).
Let \(Z_x\) be the sum of a Poisson(\(x\)) number of independent copies
of \(J\). Its moments \(m_n(x)=\mathbb EZ_x^n\) have degree \(n\),
positive coefficients on \(x,\ldots,x^n\), and zero constant term for
\(n>0\). For each fixed \(x\ge0\) this is a Stieltjes moment sequence.
Every numerical Hankel minor is nonnegative: the integral determinant
formula integrates the product of two generalized Vandermonde
determinants over ordered nonnegative support.

Put \(\kappa_j=\mathbb EJ^j=1-10^{-6}+100^j10^{-6}\). The exact Bell
expansion is
\[
m_4(x)/x=\kappa_4+
(4\kappa_1\kappa_3+3\kappa_2^2)x+
6\kappa_1^2\kappa_2x^2+\kappa_1^4x^3.
\]
Its cubic determinant equals
\[
\Delta_2
=6\kappa_1^2\kappa_2(4\kappa_1\kappa_3+3\kappa_2^2)
-\kappa_1^4\kappa_4
=-33996638137056125099281531049641/10^{30}<0.
\]
Thus numerical all-order Hankel positivity, even with the correct row
degree and positive-coefficient support, does not imply row stability.
This witness does **not** assume or establish coefficientwise Hankel
total positivity for these moments. A coefficientwise transfer would
need an additional theorem; the route here used numerical positive
moments. Outcome: full-target failure.

<a id="a4"></a>
## A4 — reduce the actual rows to a two-parameter Bessel-type family

Second-order rows suggest testing a scalar/rescaled rising-factorial
model
\[
K\sum_{j=0}^d\binom dj(A)_j(tx)^j,\qquad
(A)_j=A(A+1)\cdots(A+j-1).
\]
For a cubic \((b_0,b_1,b_2,b_3)\), its first three coefficients force
\(K=b_0,\ R=b_1/(3b_0)=At,\ V=b_2/(3b_0)=A(A+1)t^2\), hence
\(A=R^2/(V-R^2),t=R/A\). The last must equal \(KA(A+1)(A+2)t^3\).

The actual fourth cycle quotient is \((120,3948,50400,246400)\).
Its forced parameters are \(A=15463/2537,t=2537/1410\), predicting
\(11500720/47\ne246400\). The subset quotient \((1,91,2100,15400)\)
forces \(A=-1183/283,t=-283/39\), predicting
\(431900/39\ne15400\), already outside a positive-parameter model.
The representation therefore fails on actual rows before applying
any stability theorem for this family. A larger class with a proved
stability property has not been constructed. Outcome: full-target failure.

<a id="a5"></a>
## A5 — close Routh induction using exact fixed-excess coefficients

**Restricted theorem.** At every \(n\), in either \(r=3\) family,
all of \(\Delta_1,\Delta_2,\Delta_3\) that occur for \(g_n\) are strictly
positive. The proof does not control determinants of order four or more.

First the source's log-concavity proof is strict internally. If the
preceding row \(a\) is log-concave and \(b_k=c_ka_k+d_ka_{k-1}\), expansion
and \(a_{k-2}a_{k+1}\le a_{k-1}a_k\) yield
\[
b_k^2-b_{k-1}b_{k+1}\ge
(c_k^2-c_{k-1}c_{k+1})a_k^2+
(d_k^2-d_{k-1}d_{k+1})a_{k-1}^2+
\Gamma_k(c,d)a_ka_{k-1}.
\]
At third order the source computes
\(\Delta_k(c)=4,\Gamma_k=8(2k+n-2)>0\) for cycles, and
\(\Delta_k(c)=1,\Gamma_k=2(2k+2n-3)>0\) for subsets; \(\Delta_k(d)\ge0\).
For \(2\le k\le n-1\), the old \(a_k>0\), so the first term is strict.
This includes the last internal index. Thus \(g_n\)'s coefficient
ratios strictly decrease, proving \(\Delta_1>0\) and
\(\Delta_2=a_1a_2-a_0a_3>0\) for degree at least three.
For degree two, \(\Delta_2=a_1a_2>0\).

For a symbolic proof of \(\Delta_3\), normalize by
\(d_n=A(n,n)\) and put \(a_t=A(n,n-t)/d_n,\ a_0=1\).
For \(t=1,\ldots,5\) and \(n\ge6\), the exact assembly identity gives
\[
a_t=
\frac{(n)_{\underline t}h^t}{(3n)_{\underline{2t}}}
\sum_{\substack{m_1,\ldots,m_t\ge0\\\sum j m_j=t}}
\frac{(n-t)_{\underline{\ell}}}{\prod_jm_j!}
\prod_jb_j^{m_j},\qquad \ell=\sum m_j ,
\tag{1}
\]
where \(h=3,b_j=3/(3+j)\) for cycles and
\(h=6,b_j=6/(3+j)!\) for subsets. To derive (1), factor
\(g(z)=g_0(1+\sum_{j\ge1}b_jz^j)\) in
\[
A(n,n-t)=(3n-2t)![z^t]g(z)^{n-t}/(n-t)!.
\]
The finite multinomial expansion supplies the sum. Division by
\(d_n=(3n)!g_0^n/n!\) supplies the prefactor with \(h=g_0^{-1}\).
This is a finite symbolic expression at each fixed \(t\), not a fitted formula.

Substitute (1) in
\(\Delta_3=a_1a_2a_3-a_1^2a_4-a_3^2+a_1a_5\).
With
\[
D(n)=(3n-8)(3n-7)(3n-5)^2(3n-4)^2(3n-2)^2(3n-1)^3 ,
\]
the rational identities are
\[
\Delta_3^C=\frac{Q_C(n-6)}{716800D(n)},\qquad
\Delta_3^S=\frac{Q_S(n-6)}{11200D(n)} ,
\tag{2}
\]
where
\[
\begin{aligned}
Q_C(u)={}&688905u^{11}+33526710u^{10}+741338325u^9
+9828735210u^8+86793244335u^7+535881269178u^6\\
&+2360037326679u^5+7411985227710u^4+16264270861596u^3\\
&+23741850863592u^2+20743904820672u+8215758210240,\\
Q_S(u)={}&945u^{11}+45990u^{10}+1013565u^9+13348370u^8
+116677223u^7+710430074u^6+3073175215u^5\\
&+9439360358u^4+20163334460u^3+28511038824u^2
+24005911168u+9114445760 .
\end{aligned}
\]
The checker verifies (2) as identities of rational functions in an
indeterminate \(n\), using the explicit partitions in (1), and compares
(1) independently against integer recurrence rows. All coefficients
of both \(Q\)'s and all factors of \(D\) are positive for \(n\ge6\).
For \(n=4,5\), actual unnormalized \(\Delta_3\)'s are
\[
C:\ 20329344000,\ 184019656672051200;\qquad
S:\ 175700,\ 335144810000.
\]
For \(n\le3\) there is no third determinant.

The next Routh step requires \(\Delta_4\), and the full size-\(n\) claim
requires every \(\Delta_j,\ 1\le j\le n-1\). Formula (1) becomes a growing
partition sum as \(j\) grows. These fixed-order positivity factorizations
do not give a closed all-order invariant. A1 explains why simply adding
strict log-concavity to a stability induction cannot close that gap.
The all-size partial theorem is retained. Outcome: full-target failure.

## Checks and count disposition

[check_row_stability.py](check_row_stability.py) and
[STABILITY-CHECK-RESULTS.json](STABILITY-CHECK-RESULTS.json) record exact
auxiliary witnesses, symbolic identities (1)–(2), and bounded independent
recurrence comparisons. No actual-row instability is claimed.
The five routes concern operator preservation, a one-row shape implication,
a numerical moment-to-stability transfer, a concrete hypergeometric
representation, and actual-row Routh closure. A1/A2 share log-concavity
but have different obligations. A3 does not silently upgrade numerical
moments to coefficientwise positivity. Subject to independent count
review, the full question stops unresolved at its fifth failed route.

