# Independent review of the Q3818 counting proof

**Disposition:** the main thread accepts the local proof at its stated scope. It proves

$$
\mathbb E[M_n]=O((6/7)^n\sqrt{n!})
$$

for independent uniform $[0,1]$ costs on the complete undirected graph, counting tours up to rotation and reversal. This implies the exact catalog question Q3818. It is an internal mathematical review, supported by finite checks, with no formal proof assistant or external peer review. Originality is not established by the limited literature search.

## Complete exchange accounting

Removing two disjoint edges from a cycle leaves two paths. Of the two other endpoint pairings, exactly one reconnects them into a Hamiltonian cycle. In the indexed tour this adds $\{i,j\}$ and $\{i+1,j+1\}$. Every chord occurs in exactly two exchanges. Conditional on tour-edge weights, the remaining costs are independent uniforms; the constraint graph on these variables is a union of cycles. The diameter component for even $n$ has $n/2$ variables, and for $n=4$ it has two parallel constraints. The proof handles those cases explicitly. Shared tour weights prevent an unconditional factorization; the proof factors only conditional chord components.

## Probability inequality and normalization

The cycle integral is a trace of a product of finite matrices with entries divided by grid size $q$. There are $m$ factors and $m$ integrated variables, so the normalization is $q^{-m}$. Trace Cauchy–Schwarz and submultiplicativity bound this by the product of Frobenius norms. Each squared norm is the fraction of grid pairs satisfying its single inequality. Thus the bound has the square root of each exchange probability, including a length-two component; it never assumes independence of exchanges.

The grid kernels are bounded and converge almost everywhere: their possible failures are threshold hyperplanes of Lebesgue measure zero. Dominated convergence therefore passes both the cycle integral and squared norms to their continuous values. No unproved infinite-dimensional trace estimate is needed for the main theorem.

## Quadratic and integral estimates

The single-exchange tail is $h(t)=1-t^2/2$ below one and $(2-t)^2/2$ above one. The claimed bound $h(t)\leq e^{-t^2/2}$ holds on both intervals. Taking square roots gives the exponent $-\frac14\sum_{\{i,j\}\text{ nonadjacent}}(x_i+x_j)^2$.

Writing $A=\sum x_i^2$, $S=\sum x_i$, and $B=\sum x_ix_{i+1}$, the sum is $(n-4)A+S^2-2B$. Since $B\leq A$, its lower bound is $(n-6)A+S^2$. All exponent inequalities have the correct direction: decreasing the quadratic increases the upper bound on probability.

For $n\geq7$, the positive quadratic coefficient permits the change of variable used in the proof. The tangent inequality $S^2\geq2\sqrt n S-n$ separates the integral, and extending the positive integrand to infinity increases it. Completing the square gives

$$
p_n\leq\left[\frac{\sqrt e\,c}{\sqrt{n-6}}\right]^n,
\qquad c=\sqrt\pi\,\operatorname{erfc}(1/2).
$$

The proof of $c<6/7$ uses an elementary integral lower bound and $\pi<22/7$, with a positive rational margin $25/7056$. It requires no numerical rounding assumption.

## Probability to count

There are $(n-1)!/2$ undirected tours. Linearity of expectation requires no independence among their local-optimality events. The elementary upper bound $n!\leq en(n/e)^n$ gives the stated ratio to $\sqrt{n!}$. For $n\geq12$, the remaining factor $(n/(n-6))^{n/2}$ is bounded by $e^6$. Thus

$$
\frac{\mathbb E[M_n]}{\sqrt{n!}}
\leq\frac{e^{13/2}}{2\sqrt n}\,c^n.
$$

The finitely many $3\leq n<12$ are absorbed into the asymptotic constant. In particular the proof neither assumes the published restriction $n=2^k+1$ nor extends a positive Gaussian integral to sizes where its coefficient is negative.

## Independent finite checks

audit_count.py imports neither research implementation. It reconstructs exchanges by testing the alternative endpoint reconnections for Hamiltonicity, then directly enumerates all chord assignments for each tour-weight assignment on three small grids. It does not use a transfer matrix for those joint probabilities.

The receipt records:

- 4,032 exchanges for every $3\leq n\leq30$, with exactly two uses of every chord;
- 388 full-grid conditional cases for $n=4,5,6$, each satisfying the exact squared joint-probability inequality;
- 784 exact quadratic identities and lower bounds through $n=100$;
- a separate verification of all 1,022 proper Petersen cuts and all 45 optimal-edge witnesses for the elimination line.

These finite computations help detect modeling and coefficient mistakes. The all-size conclusion rests on the mathematical derivation above. The original subagent checks independently cover transfer matrices, even diameter cycles, homogeneous conditional volumes, and the rational constant comparison.

## Scope retained in the catalog

Q3818 asks only for the expectation bound in the independent-uniform complete-graph model. That statement is established locally and can be marked proved with links to this review and the full derivation. The result gives no metric-TSP approximation guarantee, basin-size estimate, bound on descent time, or efficient exact solver. Those remain separate B14 targets.
