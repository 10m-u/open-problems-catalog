# All-size corner coefficients of the Hurwitz determinants

13 October 2026. New partial scope for B3C-Q04, independent review pending.
Use the exact F_n(t;x) and Delta_r of [the earlier report](../../b3-continuation-2026-10-07/interpolation/REPORT.md).
For every n>=2, 1<=r<n and subset I of {1,...,n}, the coefficient of
product_(i in I) x_i^r in Delta_r is strictly positive.
These are the corners of the exponent box, with each exponent zero or r.
For r>1 they do not cover the intermediate exponent values.

Put k=|I| and V_k(t)=product_(j=0)^(n-1)
[(n+k-j-1)+(n-k+j)t]. Every entry b_i(x) of the Hurwitz determinant is
multi-affine, with coefficient b_i(k) at every squarefree monomial of
cardinality k. In a product of r such entries, a variable with exponent r
must occur in all r factors, and one with exponent zero occurs in none.
Hence there is exactly one choice per factor: the same monomial x_I.
The determinant signs remain, giving the coefficient exactly as Delta_r(V_k).

For 0<k<n, V_k has positive leading coefficient B and n strictly negative
real roots -u_1,...,-u_n, with u_j>0. Its coefficients in descending powers
are b_i=B e_i(u). Transposing the Hurwitz matrix and reversing both rows
and columns turns det[e_(2j-i+1)]_(i,j=0)^(r-1) into the dual
Jacobi–Trudi determinant of the staircase partition (r,r-1,...,1).
Thus

    Delta_r(V_k) = B^r s_(r,r-1,...,1)(u_1,...,u_n) > 0.

Schur polynomials have nonnegative tableau coefficients and at least one
positive monomial when the number of positive variables is at least the
number r of rows.

At k=0, V_0 has positive leading coefficient, one zero root and n-1
strictly negative roots. The same Schur identity is still positive for
r<=n-1, since its staircase has r rows and there remain n-1 positive u_j.

At k=n, V_n has degree n-1 and n-1 strictly negative roots, with positive
leading coefficient b_1; the padded coefficient b_0 is zero. Expanding
the first column of the Hurwitz determinant gives

    Delta_r(V_n) = b_1 Delta_(r-1)(V_n as a degree-(n-1) polynomial).

Take Delta_0=1. The smaller determinant is positive by the same staircase
identity, since r-1<=n-2. This proves strict positivity also at that endpoint.

The dual Jacobi–Trudi identity and the nonnegative tableau definition of
Schur polynomials are the only symmetric-function facts used. Finite
controls directly recompute both determinants through degree12 and all
orders r<n. The all-size conclusion rests on the displayed identities.

This supplies every corner coefficient for every determinant order and
degree, and recovers the full Delta_1 exponent box as a special case.
It does not assert all mixed-exponent coefficients, numeric disk stability
of arbitrary mixtures, or the complete B3C-Q04 ambition.
