# Independent review of Q3499

Reviewer: algebra agent, separate from the discrete author.
Date: 2026-10-09. Outcome: **accepted as a full counterexample** to the exact
polygon-face Ehrhart-nonnegativity question. No blocking defect found.

## Source and scope

Independently reopened [the primary v5 source](https://arxiv.org/html/2504.05123v5).
Section 2 includes the empty and full faces. Section 6 explicitly identifies
the polygon face lattice with a crown between a new minimum and maximum.
Question 6.5 concerns Ehrhart coefficients for every polygon with at least
three vertices. Its preceding seven-vertex example concerns the order
polynomial instead. The submitted proof addresses these exact conventions.

## Mathematical checks

Fixing the values of the two extreme faces gives the factor \(m-d+1\) in the
sum over the difference \(d\). Thus neither extreme has been omitted or fixed
at a boundary value. For fixed lower crown labels, each upper label has
\(q-\max(a_i,a_{i+1})\) choices; the cycle trace and its conjugate matrix
\((\min(i,j))\) are therefore correct.

The recurrence for \(\det(I-zM_q)\) agrees with the inverse tridiagonal
matrix, including its different final diagonal entry. Its binomial coefficient
formula has the correct sign and initial cases. Newton's identities as used
in the generator apply for exponents beyond the matrix size by setting missing
characteristic coefficients to zero.

The primary source states that order polytopes are full-dimensional lattice
polytopes. Hence the 28-element poset has a degree-28 Ehrhart polynomial, and
29 exact samples determine it. The Lagrange derivative weight at node
\(j>0\) is \((-1)^{j-1}\binom{28}{j}/j\); the zero-node weight is
\(-H_{28}\). The reported rational coefficient is obtained at the correct
Ehrhart argument, without substituting the order-polynomial argument.

## Executed and inspected controls

Read both `q3499_generate.py` and `q3499_verify.py`. They use different trace
and interpolation routes and share no imported generator code. Ran the
verifier successfully. It recomputed 31 counts with integer matrix products,
matched the complete rational polynomial, and obtained
\(-298495711/35302608\) from the Lagrange derivative.

The five direct enumerations of small face-poset assignments passed. The
seven-vertex source control recomputed the order-polynomial linear coefficient
as \(E_7'(-1)=-3/1430\), so the shift is independently tested. The certificate
contains the complete polygon-size range 3 through 13 and records positivity
for 3 through 12. The only negative coefficient for 13 is linear.

## Interpretation

This is an exact finite computational proof: degree bounds plus exact counts
give a polynomial identity, not a numerical fit. It supports catalog status
`disproved` for Q3499 and the stated minimum of 13 within this polygon family.
It does not imply a general sign classification for other face lattices. This
review is internal mathematical and executable scrutiny, not external peer
review or a historical-priority determination.
