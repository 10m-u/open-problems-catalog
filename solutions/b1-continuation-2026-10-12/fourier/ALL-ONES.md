# Exact all-ones Walsh column maximum

For width \(w\ge1\), put \(P=2^w\) and
\[
 M_w[a,b]=P^{-1}\sum_{x<P}e^{-2\pi iax/P}(-1)^{b\cdot x}.
\]
The all-ones column has the exact maximum
\[
 \max_{a\ne0}|M_w[a,P-1]|
 =\prod_{j=1}^w\sin(\pi q_j),\qquad
 q_j={1\over3}+{(-1)^{j-1}\over3\,2^j}.
\]
It is attained at \(a=(2^w+(-1)^{w-1})/3\) and \(P-a\).
These are integers and are odd. The result answers inverse Q4.3,
also called B1-INVERSE-ALL-ONES-MASK. Normalization is essential:
the unnormalized Fourier sum has an additional factor \(P\).

## Backward orbit argument

Digit factorization gives
\[
 |M_w[a,P-1]|=\prod_{j=1}^w|\sin(\pi a/2^j)|.
\]
Even frequencies give zero. For odd \(a\), fold each \(a/2^j\)
modulo one into \(t_j\in[0,1/2]\). Then \(t_1=1/2\) and
\[
 t_{j+1}\in\{t_j/2,(1-t_j)/2\}.
\]
Every such finite backward path is realized by an odd residue modulo \(2^w\).
Write \(g(t)=(1-t)/2\), the larger inverse branch. We prove that
always choosing \(g\) maximizes the product for every finite horizon.
Greedy maximization of one factor alone would not prove this.

Let \(h(t)=\sin(\pi t)\) and
\[
 f(t)=h(t)h(g(t))=\sin(\pi t)\cos(\pi t/2).
\]
For a pair of initial alternatives \(u=(1-t)/2\), \(v=t/2\),
we have \(u\ge v\), \(u+v=1/2\), \(u\in[1/4,1/2]\),
and \(v\in[0,1/4]\).
Differentiation shows that \(f\) increases up to
\(t_*=(2/\pi)\arcsin(1/\sqrt3)\) and then decreases.
Moreover \(3/8<t_*<1/2\), and
\[
 f(1/2)=1/\sqrt2>
 f(1/4)=\sin(\pi/4)\cos(\pi/8).
\]
Consequently \(f(u)\ge f(1/4)\ge f(v)\).

After two applications of \(g\), both alternatives lie in
\([1/4,3/8]\). Subsequent iterates stay in that interval.
Their order reverses after each application; after an even number
of applications the \(u\) orbit is the larger one.
The function \(f\) is increasing on this whole interval.
Group a product of the two greedy continuations into consecutive
pairs of factors. Its first pair favors \(u\) by the preceding
inequality, and each later pair favors \(u\) by monotonicity of \(f\).
If the number of factors is odd, the last unpaired factor also
favors \(u\), since \(h\) is increasing on \([0,1/2]\).
Thus a greedy continuation from \(u\) has product at least as large
as a greedy continuation from \(v\), for every horizon.

Induction on the horizon now proves optimality: after either first
branch, the induction hypothesis replaces its tail by a greedy
tail, and the comparison just proved selects the larger branch.
The initial case is one factor. Endpoint zero factors cause no
problem; no division by a zero factor was used.

Starting at \(1/2\), solving \(q_{j+1}=g(q_j)\) gives the displayed
formula. At \(j=w\), \(Pq_w=(2^w+(-1)^{w-1})/3\), which supplies
an attaining frequency. Reflection supplies its negative.
No assertion that these are the only maximizers is needed.

## Exponential rate

There is a finite positive constant
\[
 K=\prod_{j=1}^\infty{\sin(\pi q_j)\over\sqrt3/2}
\]
such that the maximum equals
\(K(\sqrt3/2)^w(1+O(2^{-w}))\).
This follows because \(q_j-1/3=O(2^{-j})\) and log sine is
smooth on a neighborhood of \(1/3\); the finitely many early
positive factors are harmless. This is the familiar Thue–Morse
Fourier product, but the finite dyadic maximum above needs its
own backward-path comparison. Literature leads:
[Allouche et al.](https://arxiv.org/abs/math/0610525),
[Fan, Schmeling and Shen](https://arxiv.org/abs/1903.09425).
Novelty of this finite maximum has not been established.

## Verification

Root enumerated all odd frequencies through width 19. The predicted
frequency attained the numerical maximum at every width (floating
ties between reflected frequencies are expected). These finite
checks support the implementation; the argument above covers all
widths. A separate reviewer should check the paired comparison,
rather than replacing it with one-step greedy reasoning.
