# Q4666: a non-log-concave offspring law with increasing conditioned trees

13 October 2026. **Full counterexample accepted after main-thread independent
proof and source review.** See [ROOT-REVIEW.md](../ROOT-REVIEW.md#q4666-tree-growth-converse).
No novelty or external peer-review claim is made.

Let
\[
\mu(0)=1/11,\quad \mu(1)=2/11,\quad
\mu(2)=3/11,\quad \mu(3)=5/11,\quad \mu(k)=0\ (k\ge4).
\]
The proposed theorem is that its conditioned plane-tree laws admit a
simultaneous increasing Markov coupling under literal Ulam–Harris
inclusion for every size \(n\ge1\). Yet
\(\mu(2)^2=9/121<10/121=\mu(1)\mu(3)\).
This refutes the log-concavity necessity clause of exact Q4666. The
no-internal-zeros clause is satisfied here;
the root's [T01 argument](../trees/ATTEMPTS.md#t01-support-and-root-star-inequalities)
proves it necessary for every increasing coupling.

I read the full relevant primary setup, §§2.1–2.3 and §§3.1–3.4 of
[Fleurat, v3](https://arxiv.org/html/2411.03065v3), local
texts/papers/collections-a37d9cf2ead4d1e5.txt.gz.
The proof uses Proposition 2.8 and Proposition 3.2 at their stated scopes,
without assuming the log-concavity hypotheses used later in that paper.

## Setup and the two published reduction steps

Use unnormalized weights \(w=(1,2,3,5,0,\ldots)\). A tree of size \(n\)
has weight \(\omega(T)=\prod_{v\in T}w_{k_v(T)}\), and write
\(b_n=\sum_{|T|=n}\omega(T)\), \(n\ge1\).
Normalizing \(w\) by 11 multiplies every size-n weight by \(11^{-n}\)
and leaves its conditioned law unchanged. Unary paths show \(b_n>0\).

Let \(B(z)=\sum_{n\ge1}b_nz^n\).
The root decomposition gives
\[
B=z\phi(B),\qquad \phi(u)=1+2u+3u^2+5u^3.
\]
Let \(F_{n,k}=[z^n]B(z)^k\) for \(n,k\ge1\), the total weight of
ordered forests of \(k\) trees and total size \(n\). It vanishes for \(k>n\).
Removing the first forest root gives the exact recurrence
\[
F_{n+1,k}=\sum_{j\ge1}F_{n,j}P_{j,k},\qquad
P_{j,k}=w_{j-k+1},
\tag{1}
\]
where out-of-range weights are zero. Thus, writing \(f_n=(F_{n,k})_{k\ge1}\),
\(f_{n+1}=f_nP\), and \(b_n=F_{n,1}\).
All products below are finite at each \(n\).

For a weight vector \(a\) define
\[
Z^a_n=[z^n]\sum_{k\ge0}a_kB(z)^k .
\]
The corresponding weighted composition of \(n\) has mass
\(a_k b_{n_1}\cdots b_{n_k}/Z^a_n\) at \(n_1\cdots n_k\).
It grows by increasing one part or appending a last part 1.
Write \(a^+=(a_1,a_2,\ldots)\).

The two reduction steps, also proved by the source, are these:

- If \(a=(a_0,a_1,0,\ldots)\) with \(a_0a_1>0\), its composition is the
  deterministic one-part composition for \(n>0\), hence has an increasing
  coupling.
- If \((a^+,b)\) has an increasing composition coupling, and for every
  \(n\ge1,\ 1\le m\le n\),
  \[
  \frac{Z^{a^+}_{n+1-m}}{Z^{a^+}_{n-m}}
  \le\frac{Z^a_{n+1}}{Z^a_n},
  \qquad
  \frac{b_{m+1}}{b_m}\le\frac{Z^a_{n+1}}{Z^a_n},
  \tag{2}
  \]
  then \((a,b)\) also has one (Proposition 2.8).
  Indeed, the first-part marginal is
  \(b_m Z^{a^+}_{n-m}/Z^a_n\). Inequalities (2) bound each new marginal
  mass at \(m\) and \(m+1\) by the old mass at \(m\); the cumulative
  quantile coupling increases that first part by zero or one. Independently
  coupling the remaining shifted composition supplies the full step.
- If the root-composition pair \((w,b)\) is admissible, independently
  growing the corresponding child subtrees converts a root-composition
  growth step to literal plane-tree inclusion (Proposition 3.2).
  Its induction constructs each finite-size transition kernel and
  concatenates those kernels into a simultaneous Markov process.

We establish (2) twice below, first for \(a=w^+\), then for \(a=w\).

<a id="t02"></a>
## T02 — the simpler Corollary 2.9 certificate fails

This is one full-target failed proof route, preserving the finite literal
transport evidence in the [root packet](../trees/ATTEMPTS.md).
It does not refute the candidate law.

Corollary 2.9 would require, at each shift and size, its normalizer ratio
to lie between \(b_{n+1}/b_n\) and \(b_{n+2}/b_{n+1}\).
For \(w^+=(2,3,5)\),
\[
Z^{w^+}_0=2,\qquad Z^{w^+}_1=3,\qquad Z^{w^+}_2=11,
\]
while \(b_1=1,b_2=2,b_3=7\).
At \(n=1\), its upper bound is false:
\[
11/3>7/2.
\]
The zero-size bounds checked in the root packet are correct, but do not
extend to all sizes. More generally this cubic endpoint is exactly the
missing inequality \(w_1w_3\le w_2^2\) when \(w_0=1\).
The underlying criterion (2) has an additional size lag and avoids this
unnecessary comparison.

<a id="t03"></a>
## T03 — a two-step forest matrix and the exact size lag

This is a different direct sufficient-criterion route. It yields the
accepted full solution below, rather than a third failed attempt.

### 1. The square production matrix is TN2

Put \(Q=P^2\). The convolution coefficients of \(\phi^2\) are
\[
c=(1,4,10,22,29,30,25).
\]
Its internal log-concavity defects are
\[
6,\quad12,\quad194,\quad181,\quad175,
\]
all positive. Extending \(c\) by zeros gives a TN2 Toeplitz matrix: the
ratios \(c_{i+1}/c_i\) decrease on positive support, which proves every
two-by-two minor inequality by multiplying ratios. For \(k\ge2\),
\[
Q_{j,k}=c_{j-k+2}.
\]
The only omitted intermediate index in \(P^2\) is index zero when \(k=1\),
so
\[
Q_{j,1}=c_{j+1}-w_0w_{j+1}
=(7,17,29,30,25,0,\ldots)_j .
\]
The adjacent minors involving columns 1,2, for rows \(j,j+1\), are
\[
2,\quad84,\quad181,\quad175,\quad625,\quad0,\ldots .
\]
All other adjacent minors come from the Toeplitz kernel \(c\).

These adjacent checks imply **all** minors of order two here. To see the
zero-boundary issue explicitly, the positive support of \(Q\) is exactly
\[
0\le j-k+2\le6,\qquad j,k\ge1.
\]
For rows \(a<b\) and columns \(u<v\), if the potentially negative product
\(Q_{a,v}Q_{b,u}\) is zero the desired inequality is automatic.
Otherwise the full rectangle \([a,b]\times[u,v]\) lies in positive
support: its extreme shifted indices are between those at \((a,v)\)
and \((b,u)\). On that rectangle each adjacent-column ratio is
nondecreasing in the row, by the adjacent minors. Multiplying those
ratios across columns proves the desired arbitrary-gap minor.
Thus \(Q\) is TN2 despite \(P\) not being TN2.

### 2. Every forest-row pair is TN2

A pair of nonnegative row vectors with nonnegative order-two minors
retains that property when both are multiplied by \(Q\), by the finite
Cauchy–Binet formula. This is valid for these finite-support rows even
though the matrix itself is infinite.

The first four forest rows are
\[
f_1=(1),\quad f_2=(2,1),\quad
f_3=(7,4,1),\quad f_4=(31,18,6,1).
\]
The pair \(f_1,f_3\) is TN2 because \(f_1\) has only its first entry.
The pair \(f_2,f_4\) is TN2: the only nontrivial possibly negative minor
is \(2\cdot18-31=5>0\); minors with a later column are automatic.
Multiplication by \(Q\) proves TN2 for every same-parity consecutive pair
\((f_{2i-1},f_{2i+1})\) and \((f_{2i},f_{2i+2})\).
Consequently \(F_{m,2}/F_{m,1}\) increases separately on both parities.
Its even base is \(1/2\), and its odd base at \(m=3\) is \(4/7>1/2\).
Thus for every \(m\ge2\),
\[
2F_{m,2}\ge F_{m,1}.
\tag{3}
\]

Now prove TN2 of arbitrary \(f_n,f_m,\ n\le m\), by induction on \(n\),
uniformly over all \(m\ge n\).
For \(n=1\) it is automatic. For \(n=2\), (3) proves the only nontrivial
minor at columns 1,2; all later-column minors are nonnegative.
For \(n\ge3\), the pair \(f_{n-2},f_{m-2}\) is TN2 by the induction
hypothesis, and multiplication by \(Q\) proves the desired pair.
This includes all finite sizes and every column pair. Therefore
\[
F_{n,i}F_{m,j}\ge F_{n,j}F_{m,i}
\quad(n\le m,\ i\le j).
\tag{4}
\]

### 3. Three normalizer-ratio inequalities

For nonnegative finitely supported column vectors \(a,v\), if
\(a_iv_j-a_jv_i\ge0\) for \(i<j\), (4) gives
\[
(f_ma)(f_nv)\le(f_na)(f_mv)\qquad(n\le m).
\tag{5}
\]
This follows by grouping the expansion into the products
\((a_iv_j-a_jv_i)(F_{n,i}F_{m,j}-F_{n,j}F_{m,i})\).
No ratio is taken at a zero normalizer.

Take \(a=e_1,\ v=Pe_1=(2,3,5,0,\ldots)\) in (5).
Then
\[
R_n:=b_{n+1}/b_n
\quad\hbox{is nondecreasing for }n\ge1,\qquad R_1=2.
\tag{6}
\]
Put \(z_n=Z^{w^+}_n\). For \(n\ge1\),
\(z_n=3F_{n,1}+5F_{n,2}=f_nh\), where \(h=(3,5,0,\ldots)\).
Using \(a=e_1,v=h\) in (5) proves
\[
r_n:=z_{n+1}/z_n\ge R_n\qquad(n\ge1).
\tag{7}
\]
Finally take \(a=h,\ v=Qe_1=(7,17,29,30,25,0,\ldots)\).
Their only potentially negative ordered coefficient is
\(3\cdot17-5\cdot7=16>0\); all later ones are nonnegative.
Since \(f_nQe_1=b_{n+2}\), (5) proves the precise relaxed upper bound
\[
r_n\le b_{n+3}/b_{n+2}=R_{n+2}\qquad(n\ge1).
\tag{8}
\]
The zero-size value, handled separately, is \(r_0=z_1/z_0=3/2\).

### 4. Both shifted composition pairs are admissible

The terminal shift \(w^{+2}=(3,5,0,\ldots)\) is the deterministic
one-part case. Its normalizers are
\(s_0=3,\ s_q=5b_q\) for \(q\ge1\), so
\(s_1/s_0=5/3\), and \(s_{q+1}/s_q=R_q\) for \(q\ge1\).

For \(a=w^+\), let \(n\ge1,1\le m\le n\), and \(q=n-m\).
If \(q=0\), then \(s_{q+1}/s_q=5/3\le2\le R_n\le r_n\).
If \(q\ge1\), it is \(R_q\le R_n\le r_n\).
Also \(R_m\le R_n\le r_n\).
These are exactly both inequalities (2), so \((w^+,b)\) is admissible.

For \(a=w\), the root decomposition gives \(Z^w_n=b_{n+1}\), including
\(Z^w_0=b_1=1\). Hence its next ratio is \(R_{n+1}\).
Again let \(q=n-m\le n-1\).
If \(q=0\), \(r_0=3/2\le2\le R_{n+1}\).
If \(q\ge1\), (8) and (6) give
\[
r_q\le R_{q+2}\le R_{n+1},
\]
where the final index comparison uses \(q\le n-1\).
Also \(R_m\le R_{n+1}\).
Thus (2) holds for \((w,b)\), and it is admissible.

Proposition 3.2 now supplies the increasing conditioned plane-tree
Markov coupling at every size. Equivalently, one can follow its explicit
induction: sample the coupled root compositions, couple every unchanged
child index using already constructed smaller-size transitions, and append
the new last child when its size is 1. This preserves the Ulam–Harris
vertex labels, parents and left siblings, hence literal inclusion.
The normalized law is exactly the stated \(\mu\), and all size normalizers
are positive. This completes the counterexample.

## Checks, attempt count and limits

[check_q4666.py](check_q4666.py) and
[Q4666-CHECK.json](Q4666-CHECK.json) check the finite production identities,
the exceptional TN2 boundaries, forest rows via independent generating
coefficients, and all relevant ratio/criterion controls in a bounded range.
The proof of arbitrary size is the two-step argument above, not the finite
max-flow campaign. The earlier literal transports remain preserved.

The root's T01 is a failed necessity proof with a useful support theorem.
T02 above is a failed sufficient-certificate route for the finite candidate.
T03 is an accepted full solution by a different, weaker size-lag criterion.
It stops further solve attempts. Nothing here claims that
every non-log-concave offspring law grows, or that the published
log-concavity sufficient theorem is false.

