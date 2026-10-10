# Q3499: a 13-gon disproves polygon-face Ehrhart nonnegativity

Date: 2026-10-09. Proposed catalog status: **disproved**.

## Result and scope

Let \(P_n\) be a convex polygon with \(n\) vertices, let \(\mathcal L(P_n)\) be its face lattice **including the empty face and the full polygon**, and let

\[
E_n(m)=\#\bigl(m\mathcal O(\mathcal L(P_n))\cap\mathbb Z^{2n+2}\bigr).
\]

Then

\[
\boxed{[m]E_{13}(m)=-\frac{298495711}{35302608}<0.}
\]

This answers Q3499 negatively at its full stated scope. The counterexample has 28 poset elements and a degree-28 Ehrhart polynomial. Its linear coefficient is its only negative coefficient. Exact calculation also gives strictly positive coefficients for every \(3\leq n\leq12\), so 13 is the smallest polygon size in this family that fails coefficient nonnegativity.

This is an exact computational proof with two distinct arithmetic derivations and a complete finite certificate. It has not received external or peer review. No claim about other families of posets is made.

## Source alignment

Lundström and Leite, *Order polytopes of crown posets*, [arXiv:2504.05123v5](https://arxiv.org/html/2504.05123v5), dated 1 October 2026, identify \(\mathcal L(P_n)=\hat0\oplus\mathcal C_{2n}\oplus\hat1\) in Section 6 and ask the Ehrhart-nonnegativity question as Question 6.5, printed page 33. Their observation immediately preceding that question concerns a negative **order-polynomial** coefficient for the 7-gon. The present result concerns the **Ehrhart polynomial**, whose argument differs by one. The distinction is explicitly checked below.

## 1. Count lattice points by fixing the extreme faces

Write the elements of the crown as \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with cyclic cover relations

\[
a_i<b_i,\qquad a_{i+1}<b_i,
\]

where subscripts are taken modulo \(n\). The bottom face lies below every \(a_i\), and the top face lies above every \(b_i\).

An integer point of the dilated order polytope is a weakly order-preserving assignment of integers from \(0\) through \(m\) to these \(2n+2\) elements. Fix the bottom and top values \(u\leq v\), and put \(d=v-u\). Subtracting \(u\) leaves a crown assignment with all values in \(\{0,\ldots,d\}\). There are exactly \(m-d+1\) possible pairs \((u,v)\) having this difference. Consequently,

\[
E_n(m)=\sum_{d=0}^{m}(m-d+1)\,\Omega_{\mathcal C_{2n}}(d+1). \tag{1}
\]

This formula includes both extreme faces. Omitting either one would compute a different polynomial.

## 2. A transfer matrix for the crown

For a positive integer \(q\), fix the lower crown values \(a_i\in\{0,\ldots,q-1\}\). Each upper value \(b_i\) then has

\[
q-\max(a_i,a_{i+1})
\]

choices, independently of the other upper values. Therefore

\[
\Omega_{\mathcal C_{2n}}(q)
=\sum_{a_1,\ldots,a_n=0}^{q-1}
\prod_{i=1}^{n}\bigl(q-\max(a_i,a_{i+1})\bigr)
=\operatorname{tr}(M_q^n), \tag{2}
\]

where \(M_q=(\min(i,j))_{1\leq i,j\leq q}\). The last equality follows by reversing the order of the row and column indices in the displayed transition weights, and then expanding the trace of a matrix power as a sum over cyclic index sequences.

Combining (1) and (2) gives the entirely finite integer formula

\[
\boxed{E_n(m)=\sum_{q=1}^{m+1}(m-q+2)\operatorname{tr}(M_q^n).} \tag{3}
\]

The independent verifier evaluates (3) using literal integer matrix multiplication.

## 3. A separate fast evaluation route

For the generator, set

\[
D_q(z)=\det(I-zM_q).
\]

The matrix \(M_q\) factors as \(LL^{\mathsf T}\), where \(L\) is lower triangular with every entry on or below its diagonal equal to 1. Its determinant is 1. Its inverse is tridiagonal: the diagonal is \(2,\ldots,2,1\), and the neighboring off-diagonal entries are \(-1\). Thus tridiagonal determinant expansion gives

\[
D_0(z)=1,\qquad D_1(z)=1-z,\qquad
D_q(z)=(2-z)D_{q-1}(z)-D_{q-2}(z).
\]

Induction in this recurrence, or two applications of Pascal's identity, gives

\[
D_q(z)=\sum_{k=0}^{q}(-1)^k\binom{q+k}{2k}z^k. \tag{4}
\]

Let \(c_k=(-1)^k\binom{q+k}{2k}\), with \(c_k=0\) when \(k>q\), and write \(s_r=\operatorname{tr}(M_q^r)\). Newton's identities give

\[
s_r=-r c_r-\sum_{k=1}^{r-1}c_ks_{r-k}\qquad(r\geq1). \tag{5}
\]

Equations (3) and (5) are the generator's counting route. They do not use numerical eigenvalues, decimal polynomial fitting, or approximate arithmetic.

## 4. Recover the coefficient exactly

The order polytope has dimension 28: every finite poset's order polytope has nonempty interior in one coordinate per element, for example by assigning strictly increasing values along any linear extension. Its Ehrhart function is therefore a polynomial of degree 28. Values at the 29 distinct integers \(0,1,\ldots,28\) determine it uniquely.

For a polynomial \(E\) of degree at most \(D\), differentiation of its Lagrange interpolation formula at zero yields

\[
E'(0)=-H_D E(0)+\sum_{j=1}^{D}\frac{(-1)^{j-1}}{j}\binom Dj E(j),
\qquad H_D=\sum_{j=1}^{D}\frac1j. \tag{6}
\]

Indeed, the Lagrange basis element for zero is \(\prod_{r=1}^D(1-m/r)\), whose derivative at zero is \(-H_D\). For the basis element indexed by \(j\geq1\), factoring out its zero at the origin gives derivative \((-1)^{j-1}\binom Dj/j\).

Taking \(D=28\), substituting the exact integers from (3) into (6), and reducing the resulting rational number gives

\[
-H_{28}+\sum_{j=1}^{28}\frac{(-1)^{j-1}}j\binom{28}{j}
\sum_{q=1}^{j+1}(j-q+2)\operatorname{tr}(M_q^{13})
=-\frac{298495711}{35302608}.
\]

Every matrix, sum, and limit in this identity is explicitly bounded. The certificate records all 29 interpolation values, two further values, and every rational coefficient of the resulting polynomial. For orientation, its first values are

| \(m\) | \(E_{13}(m)\) |
|---:|---:|
| 0 | 1 |
| 1 | 271445 |
| 2 | 1385949918 |
| 3 | 877340735462 |
| 4 | 156177488055984 |

The generator recovers the full polynomial through finite differences in the falling-factorial basis. The independent verifier recovers the critical coefficient by (6). Their routes are algebraically different.

## 5. Reproducibility and controls

Run these commands from the repository root:

```sh
python solutions/seven-more-2026-10-09/discrete/q3499_generate.py
python solutions/seven-more-2026-10-09/discrete/q3499_verify.py
```

Both scripts require only the Python standard library. The verifier imports no generator code. It recomputes the 31 integer counts by literal dense matrix multiplication, checks the full coefficient list at all these arguments, independently evaluates the Lagrange derivative, and verifies that only the linear coefficient is negative. Two points beyond the interpolation range agree. The roots at \(-1,-2,-3,-4\) also agree with the expected absence of strictly increasing assignments along a four-element chain at the corresponding small ranges.

Five small controls enumerate assignments directly to all face-poset elements and test every cover inequality. A separate source-alignment control computes \(E_7'(-1)=-3/1430\), reproducing the source's \([t]\Omega_{\mathcal L(P_7)}(t)\) value under \(\Omega(t)=E(t-1)\). This verifies the order/Ehrhart shift rather than assuming it.

Artifacts: [q3499_certificate.json](q3499_certificate.json), [q3499_generate.py](q3499_generate.py), [q3499_verify.py](q3499_verify.py), and the dated [source log](SOURCES.md).
