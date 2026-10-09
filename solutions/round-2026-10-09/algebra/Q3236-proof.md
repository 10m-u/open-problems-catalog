# Q3236: exact Fatou property and rearrangement invariance of the sum quasinorm

Date: 2026-10-09. Status: proposed full proof, accepted in a [separate internal AI review](../reviews/root-review.md); external mathematical review remains outstanding.

## Scope and provenance

The target is the actual infimum quasinorm

$$
 q(f)=\inf_{f=a+b}\bigl(\|a\|_A+\|b\|_B\bigr),
$$

not an equivalent replacement. The underlying measure space is sigma-finite and resonant: either nonatomic, or completely atomic with atoms of equal positive measure. Both parent quasinorms have the lattice and exact Fatou properties and depend only on decreasing rearrangements.

Primary source: Dalimil Peša, [On the sums of rearrangement-invariant quasi-Banach function spaces and their relationship to amalgams](https://arxiv.org/html/2508.10825v2), Definition 1.1 and Section 1.2. The source proves the Banach case and develops equivalence results for more general quasinorms. The [arXiv record](https://arxiv.org/abs/2508.10825) identifies v2, dated 5 November 2025, as the latest listed version when checked on 9 October 2026.

No previous solution for the exact identifier Q3236 was found under this repository's `solutions/` directory at the starting commit `8967f4f70776856b3dfc0b2494ed73167b15ee0c`. The argument below is independent of those reports. A literature search did not locate this proof. That is not a priority or novelty certification.

## Theorem

Under the hypotheses above, for every sequence of nonnegative measurable functions with $f_n\uparrow f$ almost everywhere,

$$
q(f_n)\uparrow q(f).
\tag{1}
$$

Furthermore, $f^*=g^*$ implies $q(f)=q(g)$. Thus both questions in Q3236 have affirmative answers, in the stated full scope.

The proof does not assume convex unit balls, a Hardy–Littlewood–Pólya principle, order continuity, separability of the parent spaces, or a standard underlying probability space. It does not assert attainment of the defining infimum on nonatomic spaces. Section 7 gives an example where attainment fails.

## 1. Elementary reductions

For nonnegative $f$, the infimum defining $q(f)$ can be restricted to decompositions

$$
f=a+b,\qquad 0\leq a,b\leq f.
\tag{2}
$$

Indeed, given a complex decomposition $f=a_0+b_0$, put

$$
a=f\frac{|a_0|}{|a_0|+|b_0|},\qquad
b=f\frac{|b_0|}{|a_0|+|b_0|},
$$

with both values zero when the denominator is zero. Since $f\leq |a_0|+|b_0|$, the lattice property gives $\|a\|_A\leq\|a_0\|_A$ and $\|b\|_B\leq\|b_0\|_B$. The same argument with the phase of $f$ shows $q(f)=q(|f|)$.

Restriction of (2) also shows that $q$ is lattice monotone. It is absolutely homogeneous. In particular, if $f_n\uparrow f$, the values $q(f_n)$ have a limit $L\leq q(f)$. Only $L<\infty$ needs consideration.

The usual sum quasinorm is definite and its finite elements are finite almost everywhere; these are also part of Lemma 1.2 and its setup in the primary source. One may check finiteness of the limit here directly. If $f=\infty$ on a set $E$ of finite positive measure, then for each $T>0$, eventually $f_n>T$ on a subset of $E$ of measure at least $\mu(E)/2$. In each nonnegative split, one of $a_n,b_n$ exceeds $T/2$ on a subset of measure at least $\mu(E)/4$. Rearrangement invariance and positivity of indicator quasinorms give a lower bound proportional to $T$ for its cost. On the atomic space use one atom instead. Bounded costs therefore imply $f<\infty$ almost everywhere.

For a parent lattice quasinorm with the Fatou property, pointwise convergence has the lower semicontinuity consequence

$$
u_n\longrightarrow u\quad\Longrightarrow\quad
\|u\|\leq\liminf_n\|u_n\|.
\tag{3}
$$

To prove this for nonnegative functions, use $v_N=\inf_{n\geq N}u_n$, so that $v_N\uparrow\liminf_nu_n$, and apply lattice monotonicity followed by Fatou. Absolute values handle the general case.

## 2. A lower semicontinuity lemma for distributions

Write

$$
d_u(t)=\mu\{u>t\},\qquad
u^*(s)=\inf\{t\geq0:d_u(t)\leq s\}.
$$

Suppose that the space is nonatomic, $u,u_n\geq0$, and

$$
d_u(t)\leq\liminf_n d_{u_n}(t)\quad(t>0).
\tag{4}
$$

Then every rearrangement-invariant parent quasinorm with the Fatou property satisfies

$$
\|u\|\leq\liminf_n\|u_n\|.
\tag{5}
$$

For $t<u^*(s)$, one has $d_u(t)>s$. Equation (4) implies $d_{u_n}(t)>s$ eventually, hence $u_n^*(s)\geq t$ eventually. Consequently

$$
u^*(s)\leq\liminf_n u_n^*(s).
\tag{6}
$$

Put all the rearrangements on a common copy of the original space. A nonatomic sigma-finite space of total measure $M\in(0,\infty]$ admits a measure-preserving measurable map $\tau$ onto $(0,M)$ with Lebesgue measure. For finite pieces this follows by successive bisection into equal-measure sets and binary expansion; concatenate countably many finite pieces when $M=\infty$. Thus $u^*\circ\tau$ and $u_n^*\circ\tau$ have the same decreasing rearrangements as $u$ and $u_n$, respectively. Applying the tail-infimum argument (3) to (6), then using rearrangement invariance, proves (5). No continuity of a quasinorm under weak convergence is being assumed.

## 3. Finite-measure distribution compactness and realization

Two elementary measure facts used below are recorded with their justification.

**Compactness.** Let $E$ have finite measure, let $F:E\to[0,\infty)$ be finite almost everywhere, and let $0\leq U_n,V_n\leq F$. The finite Borel measures on $[0,\infty)^3$ that are the laws of $(F,U_n,V_n)$ have a weakly convergent subsequence.

For each $R$, the mass outside $[0,R]^3$ is at most $\mu\{F>R\}$, which tends to zero. Thus the measures are uniformly tight and have the same total mass. The usual elementary proof of tight subsequence compactness applies: take a countable set dense in the continuous functions of compact support, diagonalize their integrals, and extend the resulting positive bounded functional to a finite Borel measure. Tightness preserves the total mass and upgrades convergence on compactly supported functions to convergence on bounded continuous functions. For the resulting weak limit $\nu$, the open-set inequality is

$$
\nu(O)\leq\liminf_n\nu_n(O).
\tag{7}
$$

**Realization.** If $E$ is nonatomic with finite positive measure and $\lambda$ is any finite Borel measure on $[0,\infty)^2$ of total mass $\mu(E)$, there are measurable $G,H:E\to[0,\infty)$ whose joint law is $\lambda$.

Normalize both measures to probabilities. Successive equal bisections of $E$ give a uniformly distributed variable on $(0,1)$. Every Borel probability on the standard Borel space $[0,\infty)^2$ is the image of the uniform distribution: this can be constructed by recursively subdividing a countable generating family of rectangles and assigning intervals of the prescribed probabilities. Composition gives the claim. This is a map *from* $E$, and requires no measure-space isomorphism and no countable-generation assumption on $E$'s sigma-algebra.

## 4. Proof of Fatou on a nonatomic space

Let $f_n\uparrow f$ and $L=\lim_nq(f_n)<\infty$. Choose nonnegative splits

$$
f_n=a_n+b_n,\qquad
q(f_n)\leq\|a_n\|_A+\|b_n\|_B\leq q(f_n)+1/n.
$$

After passing to a subsequence, their individual costs converge:

$$
\|a_n\|_A\longrightarrow\alpha,\qquad
\|b_n\|_B\longrightarrow\beta,\qquad
\alpha+\beta=L.
\tag{8}
$$

Partition the space into countably many disjoint measurable sets $E_m$ of finite measure. On each $E_m$, take the law $\nu_{m,n}$ of $(f,a_n,b_n)$. The compactness fact, followed by a diagonal subsequence, gives simultaneous weak limits $\nu_m$ for all $m$.

The first marginal of $\nu_m$ is the law of $f|_{E_m}$, since this marginal is independent of $n$. Moreover, $\nu_m$ is supported on

$$
\{(t,x,y):t=x+y\}.
\tag{9}
$$

For completeness, the bounded continuous function $\min(1,|t-x-y|)$ has $\nu_{m,n}$-integral

$$
\int_{E_m}\min(1,f-f_n)\,d\mu\longrightarrow0
$$

by bounded convergence. Its integral against $\nu_m$ is therefore zero, proving (9).

Fix $r>1$. For each integer $k$, put

$$
E_{m,k}=E_m\cap\{r^k\leq f<r^{k+1}\}.
$$

The restriction of $\nu_m$ to $r^k\leq t<r^{k+1}$, projected onto $(x,y)$, has total mass $\mu(E_{m,k})$. Realize precisely this joint law as a pair $(g,h)$ on $E_{m,k}$. Do this for all countably many cells and set $g=h=0$ where $f=0$. By (9), the two positive quantities $f$ and $g+h$ belong to the same geometric interval almost everywhere. Therefore

$$
f\leq r(g+h).
\tag{10}
$$

The global marginal distributions of these newly realized functions are exactly

$$
d_g(t)=\sum_m\nu_m\{x>t\},\qquad
d_h(t)=\sum_m\nu_m\{y>t\}.
$$

The open-set inequality (7) and Fatou's lemma for a nonnegative series imply

$$
\begin{aligned}
d_g(t)
&\leq\sum_m\liminf_n\mu(E_m\cap\{a_n>t\})\\
&\leq\liminf_n\sum_m\mu(E_m\cap\{a_n>t\})
=\liminf_n d_{a_n}(t).
\end{aligned}
\tag{11}
$$

The same inequality holds for $h,b_n$. The lemma in Section 2 and (8) now give

$$
\|g\|_A\leq\alpha,\qquad \|h\|_B\leq\beta.
\tag{12}
$$

Finally, on $\{g+h>0\}$ define

$$
a=f\frac{g}{g+h},\qquad b=f\frac{h}{g+h},
$$

and set both to zero elsewhere. They sum to $f$, and (10) gives $a\leq rg$, $b\leq rh$. Hence

$$
q(f)\leq r(\|g\|_A+\|h\|_B)\leq rL.
$$

As $r>1$ was arbitrary, $q(f)\leq L$. Together with monotonicity, this proves (1).

## 5. Proof of Fatou on a completely atomic space

Sigma-finiteness leaves at most countably many atoms, so functions can be treated as scalar sequences. Again choose splits with (8). Since

$$
0\leq a_n(j)\leq f(j)<\infty
$$

at every atom, diagonal subsequence selection gives a coordinatewise limit $a(j)$. Necessarily $b_n(j)\to f(j)-a(j)=b(j)$. Equation (3), applied to each parent, gives $\|a\|_A\leq\alpha$ and $\|b\|_B\leq\beta$, hence $q(f)\leq L$.

This part does not require equal atom measures or rearrangement invariance. It proves the Fatou assertion for any two Fatou lattice quasinorms on a countable atomic space. It also proves that the infimum defining $q(f)$ is attained there whenever $q(f)<\infty$.

## 6. Exact rearrangement invariance

First consider two nonnegative finite simple functions with equal distributions and finite-measure support. Their distinct positive level sets have matching finite measures. A split (2) on any one level set can be transferred to the matching level set with exactly the same joint distribution of its two summands. On a nonatomic space use the realization fact; on an equal-atom space use a bijection of the finitely many atoms. Extending by zero preserves both summand distributions. Applying this in both directions proves equality of the two sum quasinorms.

Now let $f,g\geq0$ satisfy $f^*=g^*$, and let

$$
h=\sum_{i=1}^k c_i\mathbf1_{F_i}\leq f,
\qquad c_1>\cdots>c_k>0,
$$

where the $F_i$ are disjoint and have finite measure. Fix $0<\gamma<1$. Equality of rearrangements implies equality of superlevel measures; consequently

$$
\mu\{g>\gamma c_i\}
=\mu\{f>\gamma c_i\}
\geq\sum_{j=1}^i\mu(F_j).
\tag{13}
$$

The superlevel sets on the left are nested as $i$ increases. Choose disjoint sets $G_i\subset\{g>\gamma c_i\}$ with $\mu(G_i)=\mu(F_i)$, successively starting at $i=1$. Equation (13) guarantees enough remaining measure at every step. On the atomic space the desired sizes are integer multiples of the atom measure, so the same selection is possible.

Then $u=\sum_i\gamma c_i\mathbf1_{G_i}\leq g$, and $u$ has the same distribution as $\gamma h$. The finite-simple-function result, homogeneity, and lattice monotonicity imply

$$
\gamma q(h)=q(u)\leq q(g).
$$

Take finite simple $h_n\uparrow f$; such a sequence exists by sigma-finiteness. Sections 4–5 give $q(h_n)\uparrow q(f)$. Thus $\gamma q(f)\leq q(g)$, and letting $\gamma\uparrow1$ gives $q(f)\leq q(g)$. Interchanging $f,g$ proves equality, including when the common value is infinite. Absolute-value reduction finishes the complex-valued case. QED.

## 7. Why the infimum need not be attained

This example is auxiliary, and makes explicit the point where a direct compactness proof without the geometric-bin step would fail.

On $(0,1)$ with Lebesgue measure, define

$$
u(s)=\begin{cases}2-2s,&0<s<1/2,\\1,&1/2\leq s<1,\end{cases}
\qquad
N(v)=\operatorname*{ess\,sup}_{0<s<1}\frac{v^*(s)}{u(s)}.
$$

This is an exact Fatou, rearrangement-invariant lattice quasinorm. Since $1\leq u\leq2$,

$$
\tfrac12\|v\|_\infty\leq N(v)\leq\|v\|_\infty,
$$

so it is complete, finite on indicators, and satisfies the quasi-triangle inequality with constant 2. The Fatou property follows from the monotone convergence of decreasing rearrangements almost everywhere. Let $A=B=(L^\infty,N)$ and $f(t)=2+t$.

As $\int_0^1u=5/4$, one has $\int|v|\leq(5/4)N(v)$. Every split of $f$ therefore has total cost at least

$$
\frac{\int_0^1 f}{5/4}=2.
$$

Let

$$
E_n=\bigcup_{j=0}^{n-1}[j/n,(j+1/2)/n),\qquad
a_n(t)=1+t\mathbf1_{E_n}(t),\qquad
b_n(t)=1+t\mathbf1_{E_n^c}(t).
$$

Then $a_n+b_n=f$. Direct decreasing rearrangement gives

$$
N(a_n)=1,\qquad N(b_n)=1+\frac1{2n}.
\tag{14}
$$

Indeed, the top half of $a_n^*$ is bounded above by $2-2s$. On the top half, $b_n^*\leq2-2s+1/(2n)$, and the ratio approaches $1+1/(2n)$ as $s\uparrow1/2$. Both rearrangements equal 1 on the bottom half. It follows that $q(f)=2$.

Suppose that this infimum were attained. By Section 1 there would be a nonnegative minimizing split $f=a+b$. Put $\alpha=N(a),\beta=N(b)$, so $\alpha+\beta=2$. Equality in the integral lower bound forces

$$
a^*=\alpha u,\qquad b^*=\beta u
\quad\text{almost everywhere}.
$$

Neither $\alpha$ nor $\beta$ can be zero: otherwise the nonzero summand would have essential supremum 4 while $f$ has essential supremum 3. Thus $a\geq\alpha$, $b\geq\beta$ almost everywhere, and the sets $\{a>\alpha\}$, $\{b>\beta\}$ both have measure $1/2$. Their union is almost all of $(0,1)$, since $a+b>\alpha+\beta$ there. They must therefore be disjoint modulo null sets.

On the first set $a-\alpha=t$; on the second $b-\beta=t$. Since $t<1$, the essential supremum of $a-\alpha$, which is $\alpha$, is at most 1, and similarly $\beta\leq1$. Hence $\alpha=\beta=1$. Writing $E=\{a>1\}$, the distribution $a^*=u$ would require

$$
\mu(E\cap(t,1))=\frac{1-t}{2}\quad(0<t<1).
$$

Differentiation almost everywhere gives $\mathbf1_E(t)=1/2$, an impossibility. Thus $q(f)=2$ is not attained.

The exact rational breakpoint calculation in `verify_results.py` checks (14). It is a check of this example, not a computational substitute for the general theorem.

## 8. Literature and verification limits

The exact target was checked against the definitions and discussion in the primary source, rather than inferred from a catalog paraphrase. The later [Peša–Kotalík compactness paper](https://arxiv.org/abs/2606.25419) and [Kotalík's amalgam paper](https://arxiv.org/pdf/2608.05907) concern additional compactness and amalgam constructions; their abstracts and the latter's introduction do not supply the theorem proved here. This search is not exhaustive.

The argument is a new proof proposal in this research round. The catalog status should not be promoted to an established literature resolution before independent mathematical review. The exact points requiring particular scrutiny are the distribution lower semicontinuity lemma, countable-block Portmanteau argument, and geometric-bin realization. Each is proved explicitly above.
