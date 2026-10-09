# Q1060: an exact four-variable counterexample

**Result:** the answer to Q1060 is **no**. Four centered, bounded, two-point marginals have unrestricted optimum $16$, but their best negatively correlated coupling has objective $920/57=16+8/57$. Every unrestricted minimizer necessarily has $\operatorname{Cov}(X_2,X_3)\geq1/2$.

This report supplies exact rational primal and dual certificates. The mathematical argument is independent of floating-point optimization. It is a result submitted in this research round, subject to independent mathematical review; publication status and historical novelty are not asserted.

## 1. Exact source and previous repository work

The question is Remark 4 of Takaaki Koike, Liyuan Lin and Ruodu Wang, *Joint Mixability and Notions of Negative Dependence*, **Mathematics of Operations Research** 49(4), 2786–2802 (2024), DOI [10.1287/moor.2022.0121](https://doi.org/10.1287/moor.2022.0121).

- [Author-hosted primary PDF](https://www.math.uwaterloo.ca/~wang/papers/2024Koike-Lin-Wang-MOR.pdf), §4.3, Remark 4, printed page 16, and equation (12).
- [Publisher record](https://pubsonline.informs.org/doi/10.1287/moor.2022.0121), confirming publication and bibliographic details.

For centered finite-variance marginals, the objective is

$$
T(X)=\max_{A\subseteq[n]}\mathbb E\left[\left(\sum_{i\in A}X_i\right)^2\right].
\tag{1}
$$

Negative correlation dependence (NCD) means $\operatorname{Cov}(X_i,X_j)\leq0$ for every distinct pair. The source explicitly asks about general heterogeneous marginals for $n\geq4$. Thus two-point marginals are within the exact stated scope. The paper's separate Gaussian examples and its objective with a *fixed subset cardinality* are not substitutes for (1).

The repository already contains a counterexample concerning a **different**, general-convex-cost question from this same paper in `solutions/packet-2026-10-05/01_solutions.md`, §2. That result concerns the optimality of homogeneous-marginal joint mixes for a nonquadratic participation cost. It does not answer this heterogeneous-marginal quadratic NCD question. No previous Q1060 certificate was found in the solution reports at base commit `8967f4f70776856b3dfc0b2494ed73167b15ee0c`.

The primary question, publisher record, and focused searches for “NCD minimizer,” “heterogeneous marginal,” and the paper title were checked on 9 October 2026. No earlier resolution of this exact question was located. These searches do not establish novelty.

## 2. Four simple marginals

Let $B_i\in\{0,1\}$ have fixed marginal means

$$
(p_1,p_2,p_3,p_4)=\left(\frac12,\frac13,\frac16,\frac12\right),
$$

and define

$$
X_1=8B_1-4,\qquad X_2=3B_2-1,
\qquad X_3=6B_3-1,\qquad X_4=8B_4-4.
\tag{2}
$$

Thus $X_1,X_4$ are each uniform on $\{-4,4\}$; $X_2$ is $-1$ with probability $2/3$ and $2$ with probability $1/3$; $X_3$ is $-1$ with probability $5/6$ and $5$ with probability $1/6$. Every coordinate is centered, nondegenerate, and bounded. Their variances are $(16,2,5,16)$.

All possible couplings are probability distributions on the sixteen bit vectors $b\in\{0,1\}^4$ with these means. This is a nonempty compact polytope. The objective is the maximum of finitely many linear functions of its probabilities, so a minimizer exists. The NCD-constrained feasible set is also a nonempty compact polytope: independence is feasible.

## 3. An unrestricted optimizer with objective 16

Define $P^*$ by the following atom probabilities; all unlisted bit vectors have probability zero. The second probability column is an optional certificate of the NCD optimum, proved below.

| $b_1b_2b_3b_4$ | $48P^*(b)$ | $5472P^{\rm NCD}(b)$ |
|---|---:|---:|
| 0001 | 11 | 1175 |
| 0010 | 2 | 266 |
| 0011 | 1 | 171 |
| 0100 | 0 | 120 |
| 0101 | 6 | 700 |
| 0110 | 4 | 304 |
| 1000 | 11 | 1175 |
| 1001 | 6 | 690 |
| 1010 | 1 | 171 |
| 1100 | 6 | 700 |

The numerators in the first column sum to 48. Their coordinate-wise sums are $(24,16,8,24)$, so the prescribed Bernoulli marginals hold. Its covariance matrix is

$$
\Sigma^*=
\begin{pmatrix}
16&-1&-3&-8\\
-1&2&1/2&-1\\
-3&1/2&5&-3\\
-8&-1&-3&16
\end{pmatrix}.
\tag{3}
$$

For any subset $A$, its objective term is $\mathbf1_A^\top\Sigma^*\mathbf1_A$. The values for all subsets are:

| Subset size | Subsets in the displayed order | Objective values |
|---:|---|---|
| 0 | $\varnothing$ | $0$ |
| 1 | $1,2,3,4$ | $16,2,5,16$ |
| 2 | $12,13,14,23,24,34$ | $16,15,16,8,16,15$ |
| 3 | $123,124,134,234$ | $16,14,9,16$ |
| 4 | $1234$ | $8$ |

Hence $T(P^*)=16$. Conversely, every coupling has the singleton term $\mathbb E X_1^2=16$, so

$$
\min T=16.
\tag{4}
$$

## 4. A pointwise integer identity excludes every NCD optimizer

For any deterministic bit vector $b$, write $s=b_1+b_2+b_3+b_4$ and define $x$ from (2). Direct expansion, using $b_i^2=b_i$, gives

$$
\begin{aligned}
&12\bigl[(x_2+x_4)^2+(x_2+x_3+x_4)^2
 +(x_1+x_2)^2+(x_1+x_2+x_3)^2\bigr]\\
&\qquad+9(x_1+x_4)^2+16x_2x_3\\
&=904-48b_2+192b_3+576(s-1)(s-2).
\end{aligned}
\tag{5}
$$

Because $s\in\{0,1,2,3,4}$, the last factor $(s-1)(s-2)$ is always nonnegative. Taking expectations in (5) for **any** coupling of the specified marginals gives

$$
\begin{aligned}
&12\Bigl[\mathbb E(X_2+X_4)^2+\mathbb E(X_2+X_3+X_4)^2
 +\mathbb E(X_1+X_2)^2+\mathbb E(X_1+X_2+X_3)^2\Bigr]\\
&\qquad+9\mathbb E(X_1+X_4)^2+16\operatorname{Cov}(X_2,X_3)
\geq904-48\cdot\frac13+192\cdot\frac16=920.
\end{aligned}
$$

The five coefficients on squared subset sums add to $4\cdot12+9=57$. Each squared subset sum has expectation at most $T$. Therefore

$$
57T+16\operatorname{Cov}(X_2,X_3)\geq920.
\tag{6}
$$

For an NCD coupling, $\operatorname{Cov}(X_2,X_3)\leq0$, and (6) yields

$$
T\geq\frac{920}{57}=16+\frac8{57}>16.
\tag{7}
$$

Together with (4), this proves that no minimizer is NCD. In fact, substituting $T=16$ into (6) forces

$$
\operatorname{Cov}(X_2,X_3)\geq\frac{920-57\cdot16}{16}=\frac12.
\tag{8}
$$

Thus the counterexample concerns **all** global minimizers, not merely one optimizer that happens to have a positive covariance.

Equation (5) is a dual certificate written as a finite pointwise polynomial identity. Its validity can be verified algebraically or on the complete sixteen-point support. The inference from (5) to (7) holds for every coupling and does not rely on a sampled search.

## 5. The NCD lower bound is attained

The distribution $P^{\rm NCD}$ in the third column of the atom table has total probability one and the same marginal means. Its covariance matrix is

$$
\Sigma^{\rm NCD}=
\begin{pmatrix}
16&-53/57&-5/2&-452/57\\
-53/57&2&0&-53/57\\
-5/2&0&5&-5/2\\
-452/57&-53/57&-5/2&16
\end{pmatrix}.
\tag{9}
$$

Every off-diagonal entry is nonpositive. Its five subset terms in (5) all equal $920/57$; direct evaluation of the remaining eleven terms gives no larger value. Therefore

$$
\min_{\text{NCD couplings}}T=\frac{920}{57}.
\tag{10}
$$

The verifier records all sixteen objective values for both couplings, their exact marginals and covariance matrices, and the pointwise identity residual at every atom.

## 6. Extension to every $n\geq4$, with nondegenerate marginals

For $n>4$, let $k=n-4$ and append $k$ centered variables, each uniform on

$$
\left\{-\frac1{4k},\frac1{4k}\right\}.
$$

Couple the first four variables according to $P^*$, and take all additional variables independent of one another and of the first four. Every subset variance is at most

$$
16+k\left(\frac1{4k}\right)^2
=16+\frac1{16k}
<16+\frac8{57}.
$$

For any NCD coupling of these $n$ marginals, its first four coordinates are NCD and retain the four original marginals. Equation (7) applied to that subvector forces its full objective to be at least $920/57$. Hence no global minimizer is NCD for this $n$-tuple either. Compactness again guarantees a minimizer. All marginals remain centered, bounded, finite-support, and nondegenerate.

## 7. Reproduction and scope of computation

Run, from the repository root:

```sh
python solutions/round-2026-10-09/probability/verify_probability.py
```

The verifier uses Python's exact `fractions.Fraction` arithmetic. It needs no numerical optimizer. The separate exploratory file `search_q1060.py` uses SciPy only to search for examples; its output is not used as proof. The certified conclusion rests on the explicit distributions and identity above.
