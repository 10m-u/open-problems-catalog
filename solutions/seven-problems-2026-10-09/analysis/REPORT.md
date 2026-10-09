# Q3286 and Q3287: endpoint limits of Pareto-record dispersion

Date: 2026-10-09.

Evidence: proposed analytic proofs, with all parameter-limit interchanges justified below. The fixed-parameter asymptotic variance formula is an explicit dependency on Sun's Theorem 4.8. The supplementary computations check algebra and quadrature; they are not proofs. No external peer review is claimed.

## Results and exact scope

Fix an integer $d\ge2$. Let $X_1,X_2,\ldots$ be independent copies of the first $d$ coordinates of a $\operatorname{Dirichlet}(1,\ldots,1,a)$ random vector, where $a>0$. A point sets a Pareto record if no earlier point is larger in every coordinate. Let $R_n$ count records set through time $n$, and define

$$
B_d(a)=\lim_{n\to\infty}\frac{\operatorname{Var}R_n}{\mathbb ER_n}.
$$

This is Sun's $L_d(a)$, not the dispersion of the number of records *remaining*. The results are:

1. **Q3287, affirmative.** As $a\downarrow0$,
   $$B_d(a)=1-\frac{2a}{d-1}+O_d(a^2).$$
   In particular, the requested limit is $1$.
2. **Q3286, affirmative.** As $a\to\infty$,
   $$
   B_d(a)\longrightarrow C_d
   :=1+\sum_{q=1}^{d-1}
   \frac{\binom dq}{(d-q-1)!(q-1)!}
   \int_0^\infty\!\int_0^\infty
   \frac{x^{d-q-1}y^{q-1}}{e^x+e^y-1}\,dx\,dy.
   $$
   The constant satisfies $1<C_d<\infty$. For example,
   $$C_2=1+\frac{\pi^2}{3},\qquad C_3=1+12\zeta(3).$$

The order of limits is exactly the catalog's: first $n\to\infty$ at fixed $a,d$, then the limit in $a$ at fixed $d$. No exchange between $n$ and $a$, and no uniformity in growing dimension, is asserted. The formulas for these constants need not be new in other record models; the claim here is the two parameter limits in Sun's model.

## Source and normalization

The primary source is Ao Sun, *Studies in Multivariate Pareto Records* (Johns Hopkins University, 2025), [official thesis PDF](https://jscholarship.library.jhu.edu/server/api/core/bitstreams/7ca48c8a-5406-49b2-979f-adf49c725f4d/content), Theorem 4.8 on printed pp. 72–73, and Remark D.6 on printed p. 263. The question and the variance formula were checked directly; the formula on p. 72 was also checked visually against the PDF. Appendix D.3.1 supplies related integral reductions, but the calculations used below are given explicitly.

Write

$$
\delta=a+d-1,\qquad b=\frac a\delta,\qquad h=1-b=\frac{d-1}\delta,
\qquad P=(a)_d=\prod_{j=0}^{d-1}(a+j).
$$

Here $(a)_d$ is a **rising factorial**. Replacing it by the ordinary power $a^d$ would invalidate the small-parameter argument.

The fixed-parameter mean coefficient is

$$M=\frac{P\Gamma(b)}{(d-1)!(d-1)}.$$

Use the following names for the integrals in the variance coefficient. For $p,q\ge1$, $p+q=d$, put

$$
\begin{aligned}
H_{p,q}={}&\int_0^1\!\int_v^1\!\int_0^\infty\!\int_0^\infty\!\int_0^\infty
\theta^{p-1}\eta^{q-1}(t+\theta)^{a-1}(t+\eta)^{a-1}\\
&\quad\times e^{-u(t+\theta)^\delta-v(t+\eta)^\delta}
 (e^{vt^\delta}-1)\,d\eta\,d\theta\,dt\,du\,dv,\\
J_2={}&\int_0^1\!\int_v^1\!\int_0^\infty\!\int_0^\infty
\eta^{d-1}(t+\eta)^{a-1}t^{a-1}
e^{-ut^\delta-v(t+\eta)^\delta}(e^{vt^\delta}-1)
\,d\eta\,dt\,du\,dv.
\end{aligned}
$$

Sun's formula, including the one-dimensional expression in Remark 4.10, gives

$$B_d(a)=1+T_1+T_2-T_3, \tag{1}$$

where all $T_i$ are nonnegative and

$$
\begin{aligned}
T_1&=\frac{2P(d-1)}{\Gamma(b)}
\sum_{q=1}^{d-1}w_{p,q}H_{p,q},
&w_{p,q}&=\frac{\binom dq}{(p-1)!(q-1)!},\quad p=d-q,\\
T_2&=\frac{2P(d-1)}{(d-1)!\Gamma(b)}J_2,\\
T_3&=\frac{2P}{(d-1)!}\int_0^1
(1-x)^{d-1}x^{-d}[1-(1+x^\delta)^{-b}]\,dx.
\end{aligned} \tag{2}
$$

All subsequent work concerns these explicit integrals. In particular, it does not require the lower bounds for the variance in Appendix D.3.2.

## 1. Two positive kernels and a useful bound

For $0<b<1$ and $0<c,z<1$, define

$$
\begin{aligned}
G_A(b,c,z)&=bc\int_0^1
\big[(c+w(1-cz))^{-1-b}-(c+w)^{-1-b}\big]\,dw,\\
G_B(b,c,z)&=b\int_0^1
\big[(1+wc(1-z))^{-1-b}-(1+wc)^{-1-b}\big]\,dw.
\end{aligned} \tag{3}
$$

These definitions show $G_A,G_B\ge0$. Let $A=1+c$ and $D=1+c-cz$. Elementary integration, or integration by parts, also gives

$$
\begin{aligned}
G_A={}&D^{-b}-A^{-b}
+h\int_0^1[(c+w)^{-b}-(c+w(1-cz))^{-b}]\,dw,\\
G_B={}&D^{-b}-A^{-b}
+h\int_0^1[(1+wc)^{-b}-(1+wc(1-z))^{-b}]\,dw.
\end{aligned} \tag{4}
$$

The integrals in (4) are nonpositive. The mean value theorem, with $D\ge1$, therefore proves

$$0\le G_A(b,c,z),G_B(b,c,z)\le D^{-b}-A^{-b}\le bcz. \tag{5}$$

For fixed $0<c,z<1$, (4) further gives

$$
\lim_{b\uparrow1}G_A(b,c,z)
=\lim_{b\uparrow1}G_B(b,c,z)
=\frac{cz}{(1+c)(1+c-cz)}.
\tag{6}
$$

The integrals multiplied by $h$ remain bounded for fixed $c,z$ as $b\uparrow1$. Thus no singular endpoint in the auxiliary variable $w$ is hidden in (6).

For convenient reproduction, the same kernels have closed forms

$$
\begin{aligned}
G_A&=\frac{c}{1-cz}
\big[(1-cz)(1+c)^{-b}-(1+c-cz)^{-b}+z c^{1-b}\big],\\
G_B&=\frac{(1-z)(1+c)^{-b}-(1+c-cz)^{-b}+z}{c(1-z)}.
\end{aligned} \tag{7}
$$

Values at an endpoint, when needed, mean continuous one-sided limits.

## 2. Reduction of the variance integrals

Define $S_{p,q}=(d-1)H_{p,q}/\Gamma(b)$. Then

$$
\begin{aligned}
S_{p,q}={}&\int_0^1\!\int_0^1
(1-r)^{p-1}(1-rs)^{q-1}s^{-q}
G_A(b,s^\delta,r^\delta)\,dr\,ds\\
&+\int_0^1\!\int_0^1
(1-r)^{q-1}(1-rs)^{p-1}s^{a+q-1}
G_B(b,s^\delta,r^\delta)\,dr\,ds.
\end{aligned} \tag{8}
$$

Here is a derivation that tracks the Jacobians and the time integral. Put $x=t+\theta$, $y=t+\eta$, and first restrict to $x\le y$. Set

$$x=sy,\qquad t=rsy,\qquad 0<r,s<1.$$

The Jacobian in $(t,x)$ is $sy^2$. The resulting power of $y$ is $y^{\delta+a-1}$ and the power of $s$ is $s^{a+p-1}$. For $K>0$,

$$\int_0^\infty y^{\delta+a-1}e^{-Ky^\delta}\,dy
=\frac{\Gamma(1+b)}\delta K^{-1-b}.$$

The two rates are $u s^\delta+v(1-r^\delta s^\delta)$ and $u s^\delta+v$. Write $v=uw$ on $0<v<u<1$; the time integral contributes

$$\int_0^1u^{-b}\,du=\frac1h.$$

Using $\Gamma(1+b)=b\Gamma(b)$ and $\delta h=d-1$ leaves exactly the first line of (8), with $s^{a+p-1}/s^\delta=s^{-q}$. On $x>y$, set $y=sx$, $t=rsx$, using $x$ as radial variable. The rates become $u+v s^\delta(1-r^\delta)$ and $u+vs^\delta$. This gives the second line of (8). All original differences are nonnegative, so these substitutions and integrations are justified by Tonelli's theorem. Bound (5) also proves finiteness of the reduced integrals.

For $T_2$, use $t=xy$, $t+\eta=y$ instead. The Jacobian is $y$, the radial power is again $y^{\delta+a-1}$, and the same time substitution gives

$$
\frac{d-1}{\Gamma(b)}J_2
=\int_0^1(1-x)^{d-1}x^{-d}G_A(b,x^\delta,1)\,dx.
$$

Formula (7) at $z=1$ shows

$$G_A(b,c,1)=cQ_b(c),\qquad
Q_b(c)=(1+c)^{-b}-\frac{1-c^{1-b}}{1-c}.$$

Consequently,

$$T_2=\frac{2P}{(d-1)!}\int_0^1
(1-x)^{d-1}x^{a-1}Q_b(x^\delta)\,dx. \tag{9}$$

Positivity follows from (3), and $\delta(1-b)=d-1$ gives the bounds

$$
0\le Q_b(x^\delta)
\le\frac{x^{d-1}-x^\delta}{1-x^\delta}
\le x^{d-1}\le1.
\tag{10}
$$

## 3. Q3287: the small-parameter limit, with a first-order term

The kernel bound (5), followed by dropping the factors $(1-r)^{p-1},(1-rs)^{q-1}\le1$, gives

$$
0\le S_{p,q}\le\frac b{\delta+1}
\left(\frac1{a+p}+\frac1{a+q+\delta}\right).
\tag{11}
$$

Since $T_1=2P\sum_qw_{p,q}S_{p,q}$, while $P=O_d(a)$ and $b=O_d(a)$, this proves $T_1=O_d(a^2)$.

A sharper use of (10) gives $T_2=O_d(a^2)$ as well. Indeed,

$$
Q_b(x^\delta)
\le\frac{x^{d-1}(1-x^a)}{1-x^\delta}
\le\frac{a x^{d-1}(-\log x)}{1-x^{d-1}}.
$$

For $0<x<1$, use $x^{a+d-2}\le x^{d-2}$ and
$(1-x)^{d-1}/(1-x^{d-1})\le1$. Then (9) yields

$$
0\le T_2\le
\frac{2Pa}{(d-1)!}\int_0^1x^{d-2}(-\log x)\,dx
=\frac{2Pa}{(d-1)!(d-1)^2}.
\tag{12}
$$

Finally, for $0\le c\le1$, Taylor's theorem gives

$$
0\le bc-[1-(1+c)^{-b}]\le\tfrac12b(b+1)c^2.
$$

The beta-integral identity

$$\int_0^1(1-x)^{d-1}x^{a-1}\,dx=\frac{(d-1)!}{P}$$

therefore gives

$$
0\le2b-T_3
\le\frac{P b(b+1)}{(2a+d-1)_d}
=O_d(a^2).
\tag{13}
$$

Combining (1) and (11)–(13) proves the stronger explicit estimate

$$
0\le B_d(a)-(1-2b)\le
\frac{2Pb}{\delta+1}\sum_{q=1}^{d-1}w_{p,q}
\left(\frac1{a+p}+\frac1{a+q+\delta}\right)
+\frac{2Pa}{(d-1)!(d-1)^2}
+\frac{P b(b+1)}{(2a+d-1)_d}.
\tag{14}
$$

The right side is $O_d(a^2)$. Since $2b=2a/(d-1)+O_d(a^2)$, the asserted expansion follows. This also proves $B_d(a)<1$ for all sufficiently small positive $a$ at each fixed dimension.

## 4. Q3286: the large-parameter limit

Throughout this section, $d$ is fixed and $a\to\infty$, so $b\to1$, $h\to0$, and

$$\frac P{\delta^d}=\prod_{j=0}^{d-1}\frac{a+j}{a+d-1}\longrightarrow1.$$

### 4.1. Cancellation of $T_2$ and $T_3$

In (9), put $x=e^{-t/\delta}$. After taking out the factor $\delta^{-d}$, the integrand is

$$
[\delta(1-e^{-t/\delta})]^{d-1}e^{-bt}Q_b(e^{-t}).
$$

It converges for every $t>0$ to $t^{d-1}/(e^t+1)$. For $a\ge d-1$ we have $b\ge1/2$; by (10) and $1-e^{-u}\le u$, its absolute value is bounded by

$$t^{d-1}e^{-t/2},$$

which is integrable independently of $a$. Dominated convergence gives

$$T_2\longrightarrow\lambda_d
:=\frac2{(d-1)!}\int_0^\infty\frac{t^{d-1}}{e^t+1}\,dt. \tag{15}$$

The same substitution in $T_3$ gives the scaled integrand

$$
[\delta(1-e^{-t/\delta})]^{d-1}
e^{ht}[1-(1+e^{-t})^{-b}].
$$

Its pointwise limit is identical. The inequality
$1-(1+c)^{-b}\le bc\le c$, together with $h\le1/2$, gives the same dominating function $t^{d-1}e^{-t/2}$. Thus

$$T_3\longrightarrow\lambda_d,\qquad T_2-T_3\longrightarrow0. \tag{16}$$

### 4.2. Limit of $T_1$

In (8), put $r=e^{-R/\delta}$ and $s=e^{-S/\delta}$. After multiplying by $\delta^d$, its two integrands converge respectively to

$$
R^{p-1}(R+S)^{q-1}g(R,S)
\quad\hbox{and}\quad
R^{q-1}(R+S)^{p-1}e^{-S}g(R,S),
$$

where (6) gives

$$g(R,S)=\frac{e^{-R-S}}{(1+e^{-S})(1+e^{-S}-e^{-R-S})}.$$

For completeness, the first scaled integrand before taking limits is

$$
[\delta(1-e^{-R/\delta})]^{p-1}
[\delta(1-e^{-(R+S)/\delta})]^{q-1}
e^{-R/\delta}e^{(q-1)S/\delta}G_A(b,e^{-S},e^{-R}).
$$

For $a\ge d-1$, (5) bounds it by

$$R^{p-1}(R+S)^{q-1}e^{-R-S/2}.$$

Indeed, $1-(q-1)/\delta=(a+p)/\delta\ge1/2$. The second scaled integrand has the additional factor $e^{-(a+q)S/\delta}$ in place of $e^{(q-1)S/\delta}$ and is bounded by

$$R^{q-1}(R+S)^{p-1}e^{-R-S/2}.$$

Both bounds are integrable on the positive quadrant and independent of $a$. Therefore dominated convergence applies to each integral in (8).

Recall that $T_1=2P\sum_qw_{p,q}S_{p,q}$. The weights satisfy $w_{p,q}=w_{q,p}$. Relabeling $p,q$ in the second sum combines the two limits, cancels the factor $1+e^{-S}$ in $g$, and gives

$$
\lim_{a\to\infty}T_1
=2\sum_{q=1}^{d-1}w_{p,q}
\int_0^\infty\!\int_0^\infty
\frac{R^{p-1}(R+S)^{q-1}}{e^{R+S}+e^R-1}\,dS\,dR.
$$

Set $x=R$, $y=R+S$. Symmetry of the weighted sum in $x,y$ turns twice the integral over $0<x<y$ into the integral over the whole positive quadrant. This proves the formula for $C_d$.

Its strict inequality $C_d>1$ follows from positive integrands. To prove finiteness directly, observe

$$e^x+e^y-1\ge e^{(x+y)/2}\quad(x,y\ge0).$$

Each double integral is at most
$2^d(p-1)!(q-1)!$. In particular,

$$1<C_d\le1+2^d(2^d-2)<\infty.$$

### 4.3. The constants in dimensions two and three

For an integer $p\ge1$, integrate in $y$ first to obtain

$$
\int_0^\infty\frac{dy}{e^x+e^y-1}=\frac{x}{e^x-1},
\qquad
\int_0^\infty\!\int_0^\infty
\frac{x^{p-1}}{e^x+e^y-1}\,dx\,dy=p!\zeta(p+1).
$$

The second identity follows by expanding $(e^x-1)^{-1}$ as its nonnegative exponential series and using Tonelli. Substituting $p=1$ proves $C_2=1+\pi^2/3$. In dimension three, the two symmetric terms each have weight $3$ and integral $2\zeta(3)$, proving $C_3=1+12\zeta(3)$.

## Validation, dependencies, and literature boundary

[`checks.py`](checks.py) independently compares the defining positive integrals (3) with their closed forms (7) at 60 rational parameter triples, compares the two representations (4), checks the exact identity $G_A(b,c,1)=cQ_b(c)$, and evaluates the bounds in (14) using rational arithmetic. It also checks the two low-dimensional limiting integrals numerically. Numerical checks are diagnostics; the sign, convergence, and all-dimension conclusions come from the proofs above.

The catalog's two entries were open, nonprovisional, and had no previous result links at selection. A bounded search on 2026-10-09 found no later resolution of these exact endpoint questions. The precise search log and sources are in [`SEARCH_LOG.md`](SEARCH_LOG.md). This does not assert an exhaustive novelty search. Related results for a different order of limits or independent-coordinate records do not, by themselves, justify either interchange proved here.

The only substantive imported theorem is the fixed-$a,d$ asymptotic coefficient formula of Sun's Theorem 4.8 and Remark 4.10. The thesis itself uses some numerical arguments for positivity of its variance coefficient in low dimensions; this report does not use those positivity arguments. It uses the integral identity in parts (a)–(b), and proves directly that the parameter limits are positive.
