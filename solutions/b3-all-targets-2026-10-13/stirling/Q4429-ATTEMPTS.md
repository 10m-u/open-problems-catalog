# Q4429: the concave–convex–concave row pattern

13 October 2026. Five full-target proof routes fail below. The catalog claim
is not refuted. Positive endpoint and parameter-limit results are retained
at their displayed scopes and do not reset the full-target counter.

I read [Chen–Wang, Conjecture 5.1, p.36](https://arxiv.org/abs/2610.09362v1)
in local texts/papers/collections-9a577842dae9ce2c.txt.gz. For cycles
\(r\ge6\), and subsets \(r\ge7\), every \(n\ge3\) should admit
\(2\le\ell\le u\le n-1\) so that segments \(1..\ell\),
\(\ell-1..u+1\), and \(u..n\) are strictly concave, strictly convex,
and strictly concave. Length-two outer segments are allowed.

Define \(R_{n,k}=A(n,k)^2/[A(n,k-1)A(n,k+1)]\), \(2\le k\le n-1\).
The target says its signs relative to one are a possibly empty positive
prefix, a **nonempty contiguous negative block**, then a possibly empty
positive suffix, with no equalities. Recurrences and normalization are
those in [HANKEL-TN2.md](HANKEL-TN2.md).

<a id="a1"></a>
## A1 — propagate a single convex zone through the actual recurrence

Generic preservation of this pattern would supply an induction, but it
fails for positive inputs of the correct degree and support.
At the cycle threshold \(r=6,n=6\), the preceding row

    a=(0,7,4,4,5,8)

has three negative internal defects. The actual recurrence produces

    b=(0,70,2522580,7442000,25502525,85503840,311646720),

whose internal signs are \(+,-,+,-\), with two separated convex zones.
At the subset threshold \(r=7,n=6\), the preceding row

    a=(0,6,3,3,4,7)

also has all internal defects negative. Its actual recurrence output is

    b=(0,6,74262,302850,1425076,6492675,31474716),

again with signs \(+,-,+,-\). These are artificial preceding rows, not
actual Stirling counterexamples. Extra constraints on the actual rows
must be carried by a valid induction. One witness per family is the same
route, not two attempts. Outcome: full-target failure.

<a id="a2"></a>
## A2 — normalized log-concavity plus the smooth factorial curvature

The known normalized row \(H_k=k!A(n,k)/(n+pk)!\), \(p=r-1\), is
log-concave. This alone does not bound the number of curvature crossings
after multiplying by the explicit factorial weights.
Put \(W_k=(n+pk)!/k!\) and \(q_k=W_k^2/(W_{k-1}W_{k+1})\).
At \(n=6,p=5\) and at \(n=6,p=6\), exact factorial cancellation gives
\(0<q_k<10/11\) for \(k=2,3,4,5\).

Construct \(h_1=h_2=1\), then
\[
h_{k+1}=\frac{h_k^2}{h_{k-1}t_k},\qquad
t_k=\begin{cases}11/10&k=2,4,\\2/q_k&k=3,5.\end{cases}
\]
Every \(t_k>1\), so the positive rational row \(h\) is strictly log-concave.
The ratios of \(W_kh_k\) are \(q_kt_k\), with signs \(-,+,-,+\).
Thus normalized log-concavity does not force connected convex zones.
Unlike A1's row-update attempt, this is a single-row invariant transfer.
A stronger shape bound on normalized curvature is missing.
Outcome: full-target failure.

<a id="a3"></a>
## A3 — fixed-r endpoint asymptotics, followed by a bulk saddle

This yields genuine endpoint concavity but lacks uniform middle control.
Fix \(r\ge1,k\ge2\). As \(n\to\infty\), for cycles
\[
R_{n,k}\longrightarrow k/(k-1)>1,
\]
and for subsets \(R_{n,k}\to\infty\).
For cycles the associated atom is \(L(z)-P_{r-1}(z)\), where
\(L=-\log(1-z)\), \(P_{r-1}=\sum_{j<r}z^j/j\).
For fixed \(k\),
\[
[z^N]L^k\sim k(\log N)^{k-1}/N.
\]
An elementary induction proves this: differentiating gives
\(N[z^N]L^k=k\sum_{t<N}[z^t]L^{k-1}\); integral comparison of
\((k-1)(\log t)^{k-2}/t\) gives the next log power. Subtracting a finite
polynomial changes only lower log powers, by expanding and taking its
finitely many shifts. Hence
\[
C(n,k)\sim (n+pk-1)!(\log n)^{k-1}/(k-1)!.
\]
Fixed-offset factorial/log ratios tend to one; the factorial in \(k\)
gives \(k/(k-1)\). For subsets, excluding bounded-size blocks changes the
ordinary Stirling estimate by \(O(N^{r-1}(k-1)^N)\); thus
\[
S(n,k)\sim k^{n+pk}/k!.
\]
Its curvature contains \([k^2/((k-1)(k+1))]^n>1\).

Also, fix \(r\ge1\) and right excess \(t\ge1\). In both families,
\[
R_{n,n-t}\longrightarrow(t+1)/t>1.
\]
To verify this, for the atom series \(g\) in the assembly formula and
fixed \(t\), its finite coefficient sum gives
\[
[z^t]g(z)^k\sim g_0^k\,k^t(g_1/g_0)^t/t!\quad(k\to\infty).
\]
Choosing \(t\) distinct atoms of excess one is its only degree-\(t\) term
in \(k\); other terms have degree at most \(t-1\). Relative to the diagonal
\(d_n=A(n,n)\), factorial cancellation gives
\[
A(n,n-t)/d_n\sim (K_r n^{3-r})^t/t!,
\quad K_r=g_0^{-1}r^{-(r-1)}g_1/g_0>0.
\]
Adjacent excess ratios then leave \((t+1)/t\).

For a bulk index \(k\sim\alpha n\), the saddle reduction instead yields
\[
F_r''(\alpha)=p^2/(1+p\alpha)-1/\alpha-1/(\alpha^3V(\rho)),
\]
where \(\rho g'/g=(1-\alpha)/\alpha\) and
\(V=d(\rho g'/g)/d\log\rho\). This is obtained by differentiating the
Legendre expression
\[
F_r=(1+p\alpha)\log(1+p\alpha)-(1+p\alpha)
-\alpha\log\alpha+\alpha+\alpha\log g(\rho)
-(1-\alpha)\log\rho.
\]
A full proof needs exactly one positive-curvature interval, error bounds
at moving transition indices, and every finite-size equality case.
None follows from the proved fixed-end limits. The saddle expression is
a reduction, not a claimed uniform sign theorem.
Outcome: full-target failure with fixed-r endpoint theorems.

<a id="a4"></a>
## A4 — fixed-n, large-r factorial domination

This distinct limit shows the **entire row is convex** for sufficiently
large \(r\), when \(n\) is fixed. It does not give a uniform two-parameter
bound. Fix \(n,k\), put \(e=n-k,N=rk+e\). The finite atom sums give
\[
C(n,k)\sim\frac{N!}{k!r^k}\binom{n-1}{k-1},\qquad
S(n,k)\sim\frac{N!}{k!(r!)^kr^{n-k}}\binom{n-1}{k-1}.
\]
Indeed \(r/(r+j)\to1\), and \(r!r^j/(r+j)!\to1\), for each finite \(j\).
Stirling's formula at the fixed offsets \(N=rk+e\) then gives, for
\(2\le k\le n-1\), in both cases,
\[
\frac{\log R_{n,k}}r\longrightarrow
2k\log k-(k-1)\log(k-1)-(k+1)\log(k+1)<0,
\]
by strict convexity of \(t\log t\). The finitely many internal \(k\) imply
that the full row is strictly convex beyond some \(r_0(n)\). The target
then holds with \(\ell=2,u=n-1\).

This and A3 are nonuniform in opposite directions: endpoints become
concave with \(n\) at fixed \(r\), and convex with \(r\) at fixed \(n\).
Their union does not cover every pair. A uniform cutoff \(r_0(n)\) and
control of the intervening strip remain missing.
Outcome: full-target failure with a proved fixed-row large-r subcase.

<a id="a5"></a>
## A5 — fixed-column curvature monotonicity in n

A possible boundary-propagation proof would establish \(R_{n,k}\)
nondecreasing in \(n\), plus an ordering of crossings. Its first premise
already fails on actual rows. For cycles \(r=6,k=2\),
\[
R_{3,2}=5148/5831,\qquad R_{4,2}=762047/1012928<5148/5831.
\]
For subsets \(r=7,k=2\),
\[
R_{3,2}=6435/10336,\qquad R_{4,2}=40625/69768<6435/10336.
\]
These are exact source-recurrence values, not artificial rows. Triangle
TN2 makes \(A(n,k+1)/A(n,k)\) nondecreasing in \(n\); a quotient of two
such increasing ratios need not be monotone. Eventual or weaker boundary
monotonicity might still hold but has not been proved.
Outcome: fifth consecutive full-target failure. Stop pending count review.

## Receipt and limits

[check_row_pattern.py](check_row_pattern.py) and
[ROW-PATTERN-CHECK-RESULTS.json](ROW-PATTERN-CHECK-RESULTS.json) verify
the operator witnesses, normalized-curvature constructions and actual
fixed-column drops, plus the fixed-excess formula's finite transcription.
The endpoint/large-parameter theorems rely on the written limits, not
fitting or a passing finite range. None settles the complete conjecture.
