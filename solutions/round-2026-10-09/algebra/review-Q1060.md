# Independent review of the Q1060 counterexample

**Verdict: the proposed negative answer is mathematically sound.** The four specified centered two-point marginals have unrestricted optimum $16$ and NCD-constrained optimum $920/57$. The exact gap is $8/57$, and every unrestricted minimizer has $\operatorname{Cov}(X_2,X_3)\geq 1/2$. This answers the general heterogeneous-marginal question in the cited source. The extension to every $n\geq4$ with nondegenerate bounded marginals is also valid.

This is an independent mathematical audit within the 9 October 2026 research round. It does not establish historical priority or constitute external peer review.

## Materials and source scope

Reviewed files:

- `../probability/Q1060-negative-covariance-counterexample.md`.
- `../probability/verify_probability.py`.
- The exact output `../probability/probability-certificates.json` produced by running that verifier.

The primary source was read directly: Koike, Lin and Wang, *Joint Mixability and Notions of Negative Dependence*, [author-hosted PDF](https://www.math.uwaterloo.ca/~wang/papers/2024Koike-Lin-Wang-MOR.pdf), Definition 1(i), equation (12), and §4.3 Remark 4. Equation (12) minimizes the maximum expected squared sum over **all** coordinate subsets. Definition 1(i) requires all distinct-pair covariances to be nonpositive for NCD. Section 4.3 relaxes homogeneous marginals, and Remark 4 asks about general heterogeneous constraints for $n\geq4$. Thus the two-point distributions are in scope. They also satisfy the zero-mean and finite-variance assumptions used in that discussion.

The audit concerns Remark 4. It does not claim to settle the separate Gaussian question in Remark 3 or the fixed-subset-cardinality objective (13).

## Marginals and feasibility

For Bernoulli means $(1/2,1/3,1/6,1/2)$, set

$$
X=(8B_1-4,\;3B_2-1,\;6B_3-1,\;8B_4-4).
$$

Each mean is exactly zero. The coordinate variances are respectively $16,2,5,16$. The support is the full Cartesian product of $\{-4,4\}$, $\{-1,2\}$, $\{-1,5\}$, and $\{-4,4\}$; some states can have zero probability under a particular coupling. Consequently every admissible joint law is a distribution on the same sixteen states with fixed Bernoulli means. Checking a pointwise inequality on those sixteen states is exhaustive for all possible couplings.

Both probability columns in the report have nonnegative entries summing to one, the stated Bernoulli means, and hence the prescribed centered marginals. The set of all such laws is compact and nonempty. Its NCD subset is closed and nonempty because the independent coupling belongs to it. Thus the minima discussed in the report exist.

## Unrestricted optimum

The unrestricted probability column gives the reported covariance matrix

$$
\begin{pmatrix}
16&-1&-3&-8\\
-1&2&1/2&-1\\
-3&1/2&5&-3\\
-8&-1&-3&16
\end{pmatrix}.
$$

All sixteen subset costs were evaluated exactly. Their maximum is $16$. Every coupling has the fixed singleton cost $\mathbb E X_1^2=16$, so the matching lower bound applies without any additional assumption. The unrestricted optimum is therefore exactly $16$.

## Dual certificate and its inequality directions

Let $s=b_1+b_2+b_3+b_4$ and define $x$ by the same affine map as $X$. The identity in the report is

$$
\begin{aligned}
&12\bigl[(x_2+x_4)^2+(x_2+x_3+x_4)^2
 +(x_1+x_2)^2+(x_1+x_2+x_3)^2\bigr]\\
&\quad+9(x_1+x_4)^2+16x_2x_3\\
&=904-48b_2+192b_3+576(s-1)(s-2).
\end{aligned}
$$

It holds on every bit vector, using $b_i^2=b_i$. The complete set of residual values can be grouped by $s$:

| Number of ones $s$ | Number of states | Residual $576(s-1)(s-2)$ |
|---:|---:|---:|
| 0 | 1 | 1152 |
| 1 | 4 | 0 |
| 2 | 6 | 0 |
| 3 | 4 | 1152 |
| 4 | 1 | 3456 |

Every residual is nonnegative. Taking expectations under any admissible law gives an affine right-hand contribution

$$
904-48(1/3)+192(1/6)=920.
$$

The five squared-sum coefficients are positive and total $57$. Each expected squared sum is at most the all-subsets objective $T$. Also $\mathbb E(X_2X_3)=\operatorname{Cov}(X_2,X_3)$ because the means are zero. The resulting two comparisons are

$$
920\leq
\sum_{A\in\{24,234,12,123,14\}}w_A
\mathbb E\left(\sum_{i\in A}X_i\right)^2
+16\operatorname{Cov}(X_2,X_3)
\leq57T+16\operatorname{Cov}(X_2,X_3),
$$

where the weights are $12,12,12,12,9$. Both inequality directions are correct. For an NCD law, the last covariance is nonpositive, so $57T\geq920$. At the unrestricted optimum $T=16$, the same bound yields $16\operatorname{Cov}(X_2,X_3)\geq8$.

This excludes **every** NCD unrestricted minimizer. The proof does not merely exhibit one optimizer with positive covariance, and it does not infer a global result from numerical optimization.

## Attainment of the NCD optimum

The second probability column yields the reported matrix

$$
\begin{pmatrix}
16&-53/57&-5/2&-452/57\\
-53/57&2&0&-53/57\\
-5/2&0&5&-5/2\\
-452/57&-53/57&-5/2&16
\end{pmatrix}.
$$

All distinct-pair covariances are nonpositive. For transparency, its sixteen subset costs are:

| Subsets in the displayed order | Costs |
|---|---|
| $\varnothing$ | $0$ |
| $1,2,3,4$ | $16,2,5,16$ |
| $12,13,14,23,24,34$ | $920/57,16,920/57,7,920/57,16$ |
| $123,124,134,234$ | $920/57,274/19,635/57,920/57$ |
| $1234$ | $179/19$ |

Their maximum is $920/57$, attained at all five weighted subsets in the dual certificate. The exact lower bound is therefore attained, and the optimality gap is

$$
\frac{920}{57}-16=\frac8{57}.
$$

## Higher dimensions and computational check

For $k=n-4\geq1$, append $k$ independent centered variables with values $\pm1/(4k)$, independent of the four-coordinate unrestricted optimizer. Every enlarged subset cost is at most $16+1/(16k)$, which is strictly below $16+8/57$. Any NCD law for the enlarged marginal tuple has an NCD first-four-coordinate marginal, so its full objective is at least $920/57$. Compactness still gives attainment. The claimed extension is correct, and all added marginals are nondegenerate.

The standard-library verifier was run from the repository root:

```sh
python solutions/round-2026-10-09/probability/verify_probability.py
```

Its Q1060 check completed successfully with exact rational arithmetic:

```text
Q1060: exact optima 16 and 920/57; gap 8/57; all 16 dual states certified.
```

I inspected its enumeration of the full state space, both probability tables, all marginal and covariance calculations, all subset costs, and all sixteen pointwise identities. The generated certificate agrees with the displayed mathematical quantities. The separate Q192 checks also ran as part of that command; this review makes no independent assessment of the Q192 theorem. No floating-point solver is needed for the Q1060 proof.
