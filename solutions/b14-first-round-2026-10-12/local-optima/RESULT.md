# B14 P5 — A cycle bound for the number of 2-opt local optima

**Review state:** internally reviewed local proof, 2026-10-12. The argument establishes Q3818 with an exponential improvement, for every integer $n$. The main thread independently reviewed the mathematical steps and ran separate exact checks; see [COUNT-REVIEW.md](../COUNT-REVIEW.md) and [COUNT-CHECK-RESULTS.json](../COUNT-CHECK-RESULTS.json). No originality claim or external peer-review claim is made. The checkers verify finite identities and inequalities; they do not replace the proof.

Let the edges of $K_n$ have independent uniform $[0,1]$ weights. Count undirected tours up to rotation and reversal, and let $M_n$ be the number with no strictly improving cycle-preserving two-edge exchange. Set

$$
c=\sqrt\pi\,\operatorname{erfc}(1/2)=0.8498918\ldots<6/7.
$$

**Theorem.** For every $n\geq12$,

$$
\frac{\mathbb E[M_n]}{\sqrt{n!}}
\leq \frac{e^{13/2}}{2\sqrt n}\,c^n.
\tag{1}
$$

Consequently $\mathbb E[M_n]=O((6/7)^n\sqrt{n!})$, and in particular $O(\sqrt{n!})$. The deliberately loose finite constant in (1) makes the passage from the finite probability estimate explicit. Stirling's formula improves the polynomial factor to $n^{-3/4}$, but is not needed here.

## The published baseline and its loss

Manthey and van Rhijn's MFCS 2025 paper poses the $O(\sqrt{n!})$ bound as Conjecture 17. Its Theorem 3 proves the $O(1.2098^n\sqrt{n!})$ bound **for $n=2^k+1$**. The restriction is stated again in §5, where extending it to other $n$ is left as further work. The PDF text extraction flattens the superscript; the publisher's HTML preserves it. [Paper, §§4–5](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.73/LIPIcs.MFCS.2025.73.html)

In its Lemmas 10–16, a chord-disjoint subset $S$ permits a product after conditioning on tour weights. A Gaussian bound contributes $\prod_{e:k_e>0}\sqrt{\pi/(2k_e)}$, while a further interaction estimate contributes $G(S)=O(e^{-n/(9\pi)})$. Their combination gives the base $\sqrt{\pi/2}e^{-1/(9\pi)}<1.2098$. Both discarding exchanges and estimating the remaining integral can lose information. This derivation establishes an upper bound; it does not show that either loss is necessary. [Same paper, §4](https://doi.org/10.4230/LIPIcs.MFCS.2025.73)

Local source files: PDF and extracted text. The source question is Q3818, stable ID `1ab793013b1b4b6d4773`.

## 1. Every conditional dependency component is a cycle

Fix the tour $0,1,\ldots,n-1,0$, with indices modulo $n$. Write $X_i$ for the cost of tour edge $\{i,i+1\}$. If $\{i,j\}$ is a nonadjacent unordered pair of tour-edge indices, its unique nontrivial cycle-preserving exchange removes those edges and adds

$$
\{i,j\},\qquad\{i+1,j+1\}.
\tag{2}
$$

For $2\leq d<n/2$, put $Y_{i,d}=w_{\{i,i+d\}}$, $0\leq i<n$. These are $n$ distinct chord variables. The exchanges at this circular separation are exactly

$$
Y_{i,d}+Y_{i+1,d}\geq X_i+X_{i+d},\qquad0\leq i<n.
\tag{3}
$$

If $n$ is even, its diameter chords form one additional component. Put $m=n/2$ and $Y_{i,m}=w_{\{i,i+m\}}$ for $0\leq i<m$. Its exchanges are (3) for $0\leq i<m$, with $Y$ indices taken modulo $m$. There are only $m$ distinct constraints here, because swapping $i$ and $i+m$ gives the same removed pair. For $n=4$, this is a cycle of length two: two different constraints involve the same two chord variables. It must not be replaced by two independent events.

Every chord belongs to exactly one component; every nonadjacent unordered pair of removed tour edges occurs exactly once. Indeed, orient its shorter circular separation to select $d<n/2$ and its unique initial index; in the diameter case select the initial index modulo $m$. Thus the number of constraints is $n(n-3)/2$. Each chord variable occurs in exactly two constraints, with parallel constraints allowed when $n=4$.

Conditioning on $X=x$ leaves independent uniform chord variables. Define

$$
Z_m(t_0,\ldots,t_{m-1})=
\int_{[0,1]^m}\prod_{i=0}^{m-1}
\mathbf1\{y_i+y_{i+1}\geq t_i\}\,dy,
\qquad y_m=y_0.
\tag{4}
$$

The exact conditional probability of local optimality is the product of (4) over the components above, using thresholds $t_i=x_i+x_{i+d}$. This is a factorization over chord components, **not** a factorization over exchanges. Unconditionally, the components share the random tour weights.

## 2. A cycle version of the read-two inequality

For thresholds $t_i\in[0,2]$, let

$$
h(t)=\Pr(U+V\geq t)=
\begin{cases}
1-t^2/2,&0\leq t\leq1,\\
(2-t)^2/2,&1\leq t\leq2,
\end{cases}
\tag{5}
$$

where $U,V$ are independent uniform $[0,1]$. For every $m\geq2$,

$$
Z_m(t_0,\ldots,t_{m-1})
\leq\prod_{i=0}^{m-1}\sqrt{h(t_i)}.
\tag{6}
$$

Here is a finite-matrix proof that also justifies passage to the continuous integral. Replace each kernel $\mathbf1\{u+v\geq t_i\}$ by its grid step approximation and let $A_i$ be its matrix, with entries divided by the number of grid cells. The cycle integral of these step functions is $\operatorname{tr}(A_0\cdots A_{m-1})$. The Hilbert–Schmidt/Frobenius inequality gives

$$
|\operatorname{tr}(A_0\cdots A_{m-1})|
\leq\prod_i\|A_i\|_F.
$$

For completeness, first bound the trace of the product of its first $m-1$ factors and its last factor by the product of their Frobenius norms. Then use $\|AB\|_F\leq\|A\|_F\|B\|_{\rm op}$ and $\|B\|_{\rm op}\leq\|B\|_F$ on the first product. This also covers $m=2$. As the grid is refined, the kernels converge outside finitely many hyperplanes. Dominated convergence gives (4), and each squared Frobenius norm converges to the area of $u+v\geq t_i$, namely $h(t_i)$. This proves (6).

Applying (6) to **all** components gives

$$
\Pr(T\text{ is 2-optimal}\mid X=x)
\leq\prod_{\{i,j\}\text{ nonadjacent}}\sqrt{h(x_i+x_j)}.
\tag{7}
$$

The square roots are essential. Multiplying unsquared single-exchange probabilities is generally too small to upper-bound the joint event.

## 3. A full quadratic bound

For every $0\leq t\leq2$,

$$
h(t)\leq e^{-t^2/2}.
\tag{8}
$$

On $[0,1]$, use $1-z\leq e^{-z}$. On $[1,2)$, put $g(t)=\log((2-t)^2/2)+t^2/2$. Its derivative is $t-2/(2-t)<0$, since $t(2-t)\leq1<2$. At $t=1$, $g(1)=1/2-\log2<0$. The endpoint $t=2$ is immediate.

Let $p_n$ be the probability that a fixed tour is 2-optimal, and define $S=\sum_i x_i$, $A=\sum_i x_i^2$, and $B=\sum_i x_ix_{i+1}$. Direct expansion over unordered nonadjacent pairs gives

$$
Q(x):=\sum_{\{i,j\}\text{ nonadjacent}}(x_i+x_j)^2
=(n-4)A+S^2-2B.
\tag{9}
$$

Each $x_i^2$ occurs in $n-3$ pairs; also $2\sum_{i<j}x_ix_j=S^2-A$, and deleting the $n$ adjacent pairs subtracts $2B$. Because $B\leq A$ by $2x_ix_{i+1}\leq x_i^2+x_{i+1}^2$,

$$
Q(x)\geq(n-6)A+S^2.
\tag{10}
$$

Combining (7)–(10), for $n\geq7$,

$$
p_n\leq\int_{[0,1]^n}
\exp\left[-\frac{n-6}{4}\sum_i x_i^2-\frac14\left(\sum_i x_i\right)^2\right]dx.
\tag{11}
$$

The contribution of the sum of tour costs is retained. Discarding that term leaves a weaker exponential base.

## 4. Evaluate an upper bound without an asymptotic interchange

The elementary tangent inequality $(S-\sqrt n)^2\geq0$ implies $S^2\geq2\sqrt n S-n$. Therefore (11) is at most

$$
e^{n/4}
\left[\int_0^1e^{-(n-6)x^2/4-\sqrt n x/2}\,dx\right]^n.
$$

Substitute $u=\sqrt{n-6}\,x/2$, extend the positive integral to infinity, and use $\sqrt{n/(n-6)}\geq1$:

$$
p_n\leq
\left[\frac{2e^{1/4}}{\sqrt{n-6}}
\int_0^\infty e^{-u^2-u}\,du\right]^n
=\left[\frac{\sqrt e\,c}{\sqrt{n-6}}\right]^n.
\tag{12}
$$

The equality follows by completing the square, with $\operatorname{erfc}(a)=\frac2{\sqrt\pi}\int_a^\infty e^{-u^2}du$.

For an exact certificate that $c<1$, $e^{-u^2}\geq1-u^2$ on $[0,1/2]$ gives

$$
c=\sqrt\pi-2\int_0^{1/2}e^{-u^2}du
\leq\sqrt\pi-\frac{11}{12}
<\sqrt{22/7}-\frac{11}{12}<\frac67.
\tag{13}
$$

The last comparison is rational after squaring: $(149/84)^2-22/7=25/7056>0$. The classical bound $\pi<22/7$ is sufficient; the decimal evaluation of $c$ is unnecessary for the proof.

There are $(n-1)!/2$ undirected tours, all with the same probability $p_n$. Thus

$$
\mathbb E[M_n]=\frac{(n-1)!}{2}p_n.
\tag{14}
$$

One can bound the factorial using only monotonicity of $\log x$:

$$
\log(n!)\leq\int_1^n\log x\,dx+\log n,
\qquad n!\leq en(n/e)^n.
$$

Use $\frac{(n-1)!}{\sqrt{n!}}=\frac{\sqrt{n!}}n$ and (12). For $n\geq12$,

$$
\frac{\mathbb E[M_n]}{\sqrt{n!}}
\leq\frac{\sqrt e}{2\sqrt n}\,c^n
\left(\frac n{n-6}\right)^{n/2}
\leq\frac{e^{13/2}}{2\sqrt n}\,c^n,
$$

since $-\log(1-z)\leq z/(1-z)$ and $z=6/n\leq1/2$ bound the last power by $e^6$. This proves (1). The finitely many cases $3\leq n<12$ are absorbed into the big-$O$ constant; they do not require extending (11) to a negative Gaussian coefficient.

## 5. Exact special cases and checks

If every tour weight is $1/2$, a component of length $m$ has the homogeneous integral $Z_m(1,\ldots,1)$. The symmetric kernel $K(u,v)=\mathbf1\{u+v\geq1\}$ on $L^2[0,1]$ has eigenfunctions $\sin((k+1/2)\pi u)$ and eigenvalues

$$
\lambda_k=\frac{(-1)^k}{(k+1/2)\pi},\qquad k\geq0.
$$

To verify this, differentiate $\lambda f(u)=\int_{1-u}^1f(v)dv$. Then $f(0)=0$, $f'(1)=0$, and $f''=-f/\lambda^2$; substitution supplies the eigenvalue sign. The mixed-boundary sine basis is complete. For $m\geq2$, the cycle integral is $\operatorname{tr}(K^m)=\sum_k\lambda_k^m$, an absolutely convergent sum. In particular

| $m$ | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|
| $Z_m(1,\ldots,1)$ | $1/2$ | $1/4$ | $1/6$ | $5/48$ | $1/15$ |

Already $Z_5=5/48>(1/2)^5$ rules out an upper bound by multiplying the five single-exchange probabilities. These homogeneous conditional values are not the unconditioned $p_n$: an equal-weight conditioning event has probability zero in the continuous model.

For $n=4$, the two constraints require one chord-edge sum to exceed both opposite tour-edge sums. Those three sums are independent, identically distributed and continuous, so $p_4=1/3$ and $\mathbb E[M_4]=1$. For $n=3$ every tour is locally optimal and $M_3=1$.

[check.py](check.py) checks the following independently:

- The exchange list obtained by removing edges and testing Hamiltonicity matches the circular-separation list, including diameter components, for $3\leq n\leq40$.
- Direct enumeration of small discrete chord assignments agrees exactly with a transfer-matrix cycle product.
- The squared conditional probability satisfies the exact rational form of (7) on discrete grids, where the single-constraint survival probabilities are counted directly.
- Expansion (9), lower bound (10), and the rational comparison in (13) hold in explicit exact checks.
- Certified lower/upper grid sums contain the homogeneous conditional volumes in the table.

Run `python3 solutions/b14-first-round-2026-10-12/local-optima/check.py`. Its finite checks are bounded deterministic computations, with no rare-event sampling. Output is filed in [CHECK-RESULTS.json](CHECK-RESULTS.json).

## Review scope and remaining questions

The argument depends on independent uniform **complete-graph** edge weights. Such instances are generally nonmetric. It gives a bound on the number of local optima; it establishes no approximation ratio, basin-size estimate, descent-time bound, or efficient exact TSP solver.

The [main-thread review](../COUNT-REVIEW.md) passed the complete cycle accounting, finite matrix normalization and continuous limit, quadratic coefficients, tangent integral, exact $c<6/7$ certificate, factorial conversion and finite-$n$ handling. Its [separate checker receipt](../COUNT-CHECK-RESULTS.json) records 388 full-grid joint inequalities, 4,032 exchange constraints for $3\leq n\leq30$, and 784 quadratic identities through $n=100$. These checks supplement the proof and the independently written checker in this directory.

The [bounded literature comparison](LITERATURE-CHECK.md) found no later resolution, but does not establish originality. The explicit constant is an upper bound, rather than the asymptotic growth rate of $\mathbb E[M_n]$. Matching lower bounds, a sharp exponential rate, and any implication for local-search runtime remain separate research questions.
