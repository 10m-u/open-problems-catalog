# Full cycle Hankel positivity and all cycle TN3: worked routes

13 October 2026. Q1160 asks for coefficientwise TN at **every order**, every
integer \(r\ge3\). B3C-Q03 asks for **every order-three minor**, with arbitrary
increasing nonnegative row/column triples and every \(r\ge3\). These are
separate contracts. The five proof architectures below were pursued for both:
each would supply its full scope if its stated missing lemma were proved.
Their common mechanisms are disclosed; results on one target are not silently
inherited as a different attempt or a closure on the other.

The accepted [Hankel TN2 theorem](HANKEL-TN2.md) does not reset either counter.
All routes below fail at full scope. Useful positive results are retained;
neither cycle conjecture is refuted, and no priority claim is made.

Definitions and recurrences are [Deb–Sokal, Lemma 1.1 and Conjecture 1.3(d)](https://arxiv.org/abs/2507.18959),
read from local `texts/papers/collections-ef08a76bc65e2c1f.txt.gz`.
Write \(p=r-1\), \(a=p!\), \(c_n=c_{r,n}\), and \(f_n(y)=c_n(y/a)\).
The old extreme-coefficient theorem and the leading \(3\times3\) block proof
are preserved; they are not newly counted attempts by themselves.

## Shared route calculations

### M: a genuine moment representation loses a factorial

I tried to prove all Hankel minors by realizing the row polynomials as
moments. There is an exact representation, but it gives \(n!c_n\), not
\(c_n\). This normalization is a substantive obstruction.

For \(r\ge2\), let \(S\) be exponential of mean one; conditionally on \(S=s\),
let \(Z\) be compound Poisson with rate \(xs^p/p\) and independent jumps
\(J=UV\), where \(U\) has density \(pu^{p-1}\) on \((0,1)\), and \(V\) is
exponential of mean one. For every real \(x\ge0\),

\[
\boxed{\quad n!c_{r,n}(x)=\mathbb E[(SZ)^n]\quad(n\ge0).\quad}
\tag{M}
\]

Indeed, \(\mathbb E[J^j]=p j!/(p+j)\), so the conditional exponential
generating function of \(Z\)'s moments is

\[
\exp\left(xs^p\sum_{j\ge1}\frac{z^j}{p+j}\right).
\]

Its \(z^n\) coefficient, multiplied by \(n!\), is

\[
n!\sum_{k=0}^n\frac{x^ks^{pk}}{k!}
 [z^{n-k}]\left(\sum_{j\ge0}\frac{z^j}{r+j}\right)^k.
\]

Multiplying by \(s^n\) and integrating against \(e^{-s}ds\) gives the
labelled-assembly formula for \(n!c_n\). For each fixed \(n\) this is a finite
sum; its moments are finite. At \(n=0\), including \(x=0\), the identity is
one. Thus the numerical sequence \(n!c_n(x)\) is a Stieltjes moment sequence
and its Hankel matrix is TN for every \(x\ge0\).

The attempted final step, division of a moment sequence by \(n!\), is false.
The moments of the point mass at one are \(m_n=1\). After that division,
the first principal order-two minor is \(1/2-1=-1/2\), and the leading
order-three minor of \(1/(i+j)!\) is \(-1/144\). Hence this normalization
can destroy both required orders. A representation directly for \(c_n\),
or a special normalization theorem using more than the moment property, is
still missing. Numerical moment positivity would also require a separate
coefficientwise argument; it alone is not a closure.

### F: the ordinary positive-polynomial S-fraction route fails at its third weight

A classical S-fraction with nonnegative polynomial coefficients would prove
coefficientwise Hankel TN of every order, hence both targets. The first
weights are determined uniquely by the initial moments. In the normalized
variable \(y=ax\), put

\[
B=\frac{(2r)!}{2(r!)^2},\qquad T=\frac{(3r)!}{6(r!)^3}.
\]

The first rows give

\[
\alpha_1=y,\quad\alpha_2=r+(B-1)y,\quad
\alpha_3=
\frac{r+\frac{2r^2B}{r+1}y+(T-B^2)y^2}{r+(B-1)y}.
\]

At \(r=3\), \(B=10,T=280\), and therefore

\[
\alpha_3=\frac{1+15y+60y^2}{1+3y}
=1+12y+24y^2-72y^3+216y^4-\cdots.
\]

This is not a polynomial, and even its formal power-series coefficients
are not nonnegative. The unique classical S-fraction therefore cannot have
the positive-polynomial weights required by this proof. A different branched
or multistate continued fraction might work, but has not been constructed.
This does not refute Hankel TN: the sufficient fraction condition is far
from necessary, as the primary source emphasizes.

### D: isolating each coefficient degree gives nonmoment kernels

A direct positive-measure proof could write

\[
c_n(x)=\sum_k x^k\int t^n\,d\mu_k(t),\qquad \mu_k\ge0.
\]

Then integral determinant expansions would provide nonnegative polynomial
coefficients. The coefficient-degree kernels cannot have this form.
Already \(C(0,1)=0<C(1,1)\), impossible for a nonnegative measure whose
zeroth moment is zero. Removing index zero and the universal factor \(x\)
does not repair it: \(C(1,2)=0\), \(C(2,2)>0\), and

\[
\det\begin{pmatrix}C(1,2)&C(2,2)\\C(2,2)&C(3,2)\end{pmatrix}
=-C(2,2)^2<0.
\]

Thus even a single isolated degree fails order-two Hankel TN. A proof must
control cross-degree cancellations in a determinant; separate positive
moment kernels for each degree cannot supply it. This route differs from
M: M has a positive probabilistic representation and loses a row-index
factorial; D tries to preserve the original row normalization and fails
because individual coefficient kernels are not positive measures.

### P: the successful two-index pairing does not extend generically to triples

The TN2 proof uses a numerical TN2 triangle, a birth/stay recurrence, and
birth/stay coefficients separately nondecreasing in row and column. A
natural attempted completion is a three-index rearrangement under those
same hypotheses. That completion is false even for an actual source family.

The third-order subset triangle satisfies every hypothesis of that pairing
lemma and now has coefficientwise Hankel TN2 at every size. Nonetheless
its actual Hankel minor with row indices \(1,2,3\) and column indices \(0,1,2\)
is

\[
-16x^5+19110x^6+938700x^7+15309000x^8+79380000x^9.
\]

The checker generates this from the source recurrence. Consequently the
available ordering/recurrence hypotheses do not imply coefficientwise TN3,
and hence do not imply all orders. A cycle-specific condition using the
cycle stay coefficient \(n+pk-1\), beyond separate monotonicity, is missing.
The known subset counterexample is used here to disprove a *newly attempted
extension of the newly proved pairing theorem*, not counted as a new
refutation of the cycle question or as a separate numerical search.

### E: a shifted symbolic order-three block supplies new interior coefficients

I tried to extend the old leading block theorem to every shifted block and
then arbitrary gaps by symbolic determinant expansion. The first next block

\[
K_r(y)=\det(f_{i+j}(y))_{i=1,2,3;\ j=0,1,2}
\]

has the following three lowest nonzero coefficients, all positive for every
integer \(r\ge2\):

\[
[y^3]K_r=2r^2(r+1),
\]

\[
[y^4]K_r=\frac{4Br^3(r^3+5r^2+13r+11)}{(r+2)(r+3)},
\]

\[
[y^5]K_r=\frac{r(TP_r-B^2D_r)}{(r+1)^2(r+2)^2(r+3)},
\tag{E5}
\]

where

\[
P_r=24r^7+162r^6+357r^5+282r^4+129r^3+282r^2+276r+72,
\]

\[
D_r=r^8-r^7-48r^6-134r^5-135r^4+71r^3+330r^2+276r+72.
\]

For clarity, all ingredients in the expansion can be generated from

\[
\begin{aligned}
f_1&=y,\\
f_2&=ry+By^2,\\
f_3&=r(r+1)y+\frac{2r(2r+1)}{r+1}By^2+Ty^3,\\
f_4&=r(r+1)(r+2)y+
\frac{2r(2r+1)(3r^2+6r+2)}{(r+1)(r+2)}By^2+
\frac{3r(3r+1)}{r+1}Ty^3+Uy^4,\\
f_5&=r(r+1)(r+2)(r+3)y+
2r^2(2r+1)(2r+2)(2r+3)
\left(\frac1{r(r+3)}+\frac1{(r+1)(r+2)}\right)By^2\\
&\quad+3r(3r+1)(3r+2)
\left(\frac1{r+2}+\frac r{(r+1)^2}\right)Ty^3
 +\frac{4r(4r+1)}{r+1}Uy^4+Vy^5,
\end{aligned}
\]

with \(U=(4r)!/[24(r!)^4]\), \(V=(5r)!/[120(r!)^5]\).
These come from counting the atom-size compositions of excess at most four,
so (E5) is a finite symbolic identity, not fitted to parameter samples.

To prove (E5)'s positivity, strengthen the old bound to

\[
\frac{T}{B^2}\ge\frac{5r}{6}\qquad(r\ge2).
\]

At \(r=2\) equality holds. The consecutive ratio of \(T/B^2\) is

\[
\frac{3(3r+1)(3r+2)}{4(2r+1)^2}\ge\frac{r+1}{r},
\]

because the numerator difference after cross multiplication is
\(11r^3-5r^2-14r-4\); on writing \(r=t+2\) it becomes
\(11t^3+61t^2+98t+36>0\). Induction proves the bound.
Then \(P_r>0\) and

\[
TP_r-B^2D_r\ge\frac{B^2}{6}(5rP_r-6D_r)>0.
\]

For \(r=t+2\), the last polynomial is

\[
114t^8+2640t^7+26265t^6+146706t^5+504135t^4+
1094112t^3+1467504t^2+1112112t+362880.
\]

This proves the first *two interior* coefficients of this shifted minor,
in addition to its positive extreme coefficient. The remaining degrees
\(6,7,8\) require further factorial comparisons even for this single block;
arbitrary shifted/gapped triples and higher orders require a uniform
determinant invariant. The TN2 telescoping identity cannot be reused for
order three: it telescopes two products, whereas a three-row determinant
has six signed products. No such invariant or sign-controlled telescoping
was obtained. This is substantive symbolic progress but a full-target
failure, rather than a new claim inferred from passing finite minors.

## Q1160 attempt records

<a id="q1160-a1"></a>
### A1 — factorial-weighted Stieltjes moments

Route M proves an all-r positive numerical representation for \(n!c_n\).
The required division step is false at orders two and three. Full all-orders
coefficientwise scope remains unresolved.

<a id="q1160-a2"></a>
### A2 — classical positive-polynomial S-fraction

Route F computes a nonpolynomial third weight with negative formal
coefficients at the actual \(r=3\). This sufficient all-orders fraction
construction fails; branched alternatives remain unconstructed.

<a id="q1160-a3"></a>
### A3 — nonnegative moment kernel at each coefficient degree

Route D rules out the proposed coefficient-preserving measure decomposition
by exact zero-mass/positive-next-moment and negative order-two witnesses.
Cross-degree determinant cancellations are still uncontrolled.

<a id="q1160-a4"></a>
### A4 — extend recurrence pairing to arbitrary determinants

Route P's hypotheses admit an actual negative subset order-three coefficient.
A cycle-specific strengthening is missing. No cycle counterexample is claimed.

<a id="q1160-a5"></a>
### A5 — uniform symbolic shifted-block closure

Route E proves three coefficients of the next shifted order-three minor
uniformly, including two interior coefficients, but lacks a uniform
sign-controlled determinant recurrence for arbitrary indices and orders.
Fifth consecutive full-target failure; stop Q1160 pending count review.

## B3C-Q03 attempt records

<a id="q03-a1"></a>
### A1 — realize every original cycle triple as a moment determinant

Route M fails at the original normalization: division by \(n!\) can make
the leading order-three determinant negative, explicitly \(-1/144\).
The actual factorial-weighted theorem is a useful different scope.

<a id="q03-a2"></a>
### A2 — classical fraction supplies positive three-path determinants

Route F fails already at the unique third fraction weight at \(r=3\).
No alternative positive three-path fraction network was constructed.

<a id="q03-a3"></a>
### A3 — isolate the degrees of a three-row determinant by positive measures

Route D's component kernels fail the necessary moment order-two test.
Their three-fold mixed determinant cannot be certified by independent
positive coefficient measures as proposed.

<a id="q03-a4"></a>
### A4 — three-index version of the successful TN2 rearrangement

Route P is refuted by the actual subset triple under exactly those generic
hypotheses. The additional cycle-only inequality is not supplied by TN2.

<a id="q03-a5"></a>
### A5 — shifted/gapped cycle triple induction

Route E addresses an actual next shifted triple, proving its first three
nonzero coefficients for every \(r\ge2\). It does not control its other
interior coefficients or arbitrary row/column triples. Fifth consecutive
full-target failure; stop B3C-Q03 pending root count review. These stops
leave the conjectures unresolved.

## Receipt

[check_cycle_hankel_routes.py](check_cycle_hankel_routes.py) and
[CYCLE-HANKEL-CHECK-RESULTS.json](CYCLE-HANKEL-CHECK-RESULTS.json) check the
moment coefficient identity, fraction coefficients, negative scope controls,
and all new symbolic formulas with rational arithmetic. Finite values
check transcription; the stated universal partials have proofs above.
