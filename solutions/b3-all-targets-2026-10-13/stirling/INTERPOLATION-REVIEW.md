# Independent interpolation proof and stopping-count review

13 October 2026. Accept the stated partial theorems and the five failed
full-target routes per Q1441, Q1442, B3C-Q04 and B3C-Q05. These questions
remain unresolved. Q1443's separately reviewed counterexample is not part
of these counters. No source or software failure is counted.

I read [ATTEMPTS.md](../interpolation/ATTEMPTS.md),
[HURWITZ-CORNERS.md](../interpolation/HURWITZ-CORNERS.md),
[NEAREST-RESULTS.md](../interpolation/NEAREST-RESULTS.md), their exact
checkers/receipts, the earlier
[interpolation report](../../b3-continuation-2026-10-07/interpolation/REPORT.md),
and the primary [Vishnyakova paper](https://arxiv.org/html/2607.06207v1).
The normalized class is L(P)=product(u+a_i), a_i in [0,1]; this distinction
from arbitrary Newton-positive polynomials and shift mixtures is essential.

## All-degree/all-order corner theorem

The coefficient argument is correct: to obtain x_I^r from a product of
r multi-affine entries, every factor must contribute exactly x_I.
Thus that determinant coefficient is exactly Delta_r(V_|I|), with the
determinant signs retained rather than ignored.

If V_k=B product(t+u_j), its descending coefficients are B e_i(u).
Transpose and reverse both row and column order in the Hurwitz matrix.
The entry index 2j-i+1 becomes r-2i+j, which is the dual Jacobi–Trudi
index of the self-conjugate staircase (r,r-1,...,1), in zero-based indexing.
The two reversals have the same sign, so their product has sign +1.
Therefore the determinant is B^r times that staircase Schur polynomial.

For interior k there are n positive u variables. For k=0 there are n-1
positive variables and one zero; r<n still guarantees a positive tableau
monomial. For k=n the padded coefficient b_0 is zero. First-column
expansion gives b_1 Delta_(r-1) of the degree-(n-1) row; for r=1 this
uses Delta_0=1. These are valid boundary cases, not limits with lost strictness.
The theorem supplies exactly the 0/r corners of each exponent box.
It supplies the entire box only for r=1.

The separate order-two orbit coefficient formula also has the correct
binomial multiplicity: each degree-one variable is assigned to one of
the two factors, and each degree-two variable to both. The checker does
enumerate every orbit at n=3,...,32; the proof does not extrapolate that
finite range. The signed vertex-pair obstruction -475 does not contradict
the positivity of these aggregated coefficients.

## Q1442 and B3C-Q05 counts

The same five constructions target both nested disks. This is five per
question, with their shared evidence disclosed, not ten independent
constructions. Every control fails the requisite contract for both disks.

| Route | Full-target sufficient contract actually tested | Review |
|---|---|---|
| I01 | Extend common parameters to the polarization disk so circular coincidence reduces all independent parameters. | The diagonal complex-parameter roots leave even the radius-two disk. The complex examples are not real-cube counterexamples. |
| I04 | Append using only Newton positivity and the previous disk/numeric Hurwitz invariant. | The explicitly artificial previous square satisfies those invariants but its appended roots violate both new disks. Additional TP/cube data are required. |
| I08 | Bound numerical radius of the Newton companion after positive diagonal similarity. | Its unchanged final diagonal has modulus exceeding the target radius at actual all-one parameters; actual eigenvalues remain admissible. |
| I09 | Replace the Bernoulli/PF shift law by full-support ordinary log-concavity. | The actual uniform LC law has an IVT root with centered modulus >6 and uncentered modulus >6; it is outside U_6. |
| I10 | Isolate the leading Newton term by the triangle majorant everywhere outside the disk. | At actual a_1=a_2=1 and z=-5/2, 35/8<6. The polynomial is nonzero there, but the specified termwise certificate cannot show it. |

These are respectively a polarization domain, an operator induction
invariant, a particular matrix norm encoding, a distribution-class
relaxation, and an analytic majorant. I04 and I09 both enlarge the class
but impose different retained invariants and have different exact controls.
I10 rejects the specified dominance inequality; it does not reject every
Rouche proof or all possible contour changes. The packets state these limits.

## B3C-Q04 counts

| Route | Full-target sufficient contract actually tested | Review |
|---|---|---|
| I02 | Pair each two Bernstein vertices into a nonnegative determinant contribution. | The mixed pair -475 is a precise failure, even though the real aggregated coefficients may be positive. |
| I04 | Append using only prior numerical Hurwitz stability and Newton positivity. | The new Delta_2=-8275/1152 rejects this invariant on its enlarged class. |
| I05 | Certify the resulting coefficient row by all-order Toeplitz TN. | Actual F_2 at odds (1,1) has the -1264 Toeplitz minor; the stronger row certificate is false. |
| I06 | Complete Routh positivity from strict LC plus Delta_1,Delta_2. | The full-support degree-six artificial row has Delta_3=-216. |
| I07 | Convert numeric orthant stability plus nonnegative multi-affine entries to coefficientwise determinant positivity. | The positive cubic has Delta_2=4x^2-8x+6>0 numerically but a negative coefficient. |

The contracts are distinct: termwise expansion, operator propagation,
a global stronger matrix class, low-order completion, and numerical-to-
coefficient transfer. I06/I07 are generic completion obstructions, not
actual F_n counterexamples. I03 is a positive auxiliary theorem and is
correctly excluded from the five failure count.

## Nearest-root results and Q1441 counts

I independently rebuilt each numerator from sampled values and derived
its reciprocal reduction by descending binomial elimination. This does
not use the root checker's Chebyshev recurrence. I then used a direct
homogenized integer power sum to check every rational bracket, rather than
the root checker's Horner evaluator.

For q^128 and q^129 all numerator coefficients are positive, reciprocity
is exact, and the respective 128 and 129 disjoint sign-change intervals
are strictly below -2. The IVT exhausts the degrees of the reductions g.
Each v<-2 gives two distinct negative roots of t^2-vt+1, exhausting
the numerator degree. AESW therefore certifies the full sampled-value TP
class. The primary paper's Theorem C is specifically closure for polynomial-
sampled TP sequences; it is not the false general Hadamard closure of TP.

The semigroup calculation is correct: with v=m mod128 in [0,127],
m-129v is divisible by 128 and is at least -127 for m>=16256,
so it is nonnegative. Product closure thus gives the lower bound
sqrt(19/10) at every even degree >=32512. It is a lower bound, with no
uniform upper conclusion.

The quadratic-power ceiling is exact. The 2-by-2 sample inequality gives
c<=2; at c=2 the 3-by-3 minor is 56^m-64^m<0. The two-endpoint Viete
identity and the subsequent centered triangle inequality also have the
correct direction, including endpoint zeros. Their bound is degree-dependent.

| Route | Full-target route actually explored | Review |
|---|---|---|
| N01 | Produce unbounded nearest radii from nonreal quadratic powers by increasing c. | The exact sample minors force c<2 throughout that family; two larger TP bases give a useful but bounded lower family. |
| N02 | Derive a uniform upper bound from both endpoint products and Viete. | The worked exact estimate grows linearly in degree. That product argument as carried out does not close the uniform target. |
| N03 | Extend the odd-degree real-root reduction to all parities. | An actual admissible quadratic has no real root; a complex witness is necessary in even degrees. |
| N04 | Pass through finite differences to the odd-degree theorem. | The actual difference of binom(z+2,2) has transform root -2, so the needed operator closure is false. |
| N05 | Factor every member into admissible generators of degree at most six. | q^128 has no nonconstant admissible divisor of such a degree. |

N05 is a failure of the concrete cutoff-six sufficient construction,
not a proof that no finite cutoff works. Because q is irreducible over
the reals, its low-degree divisors are scalar multiples of q,q^2,q^3.
The first two have negative numerator coefficients. If q^3 were
admissible, all its reciprocal g roots would be <=-2, so g(y-2) would
have nonpositive roots and nonnegative coefficients. Its negative
coefficients contradict this. This closes the stated cutoff-six test,
while a larger-cutoff factorization remains an open alternative.

N02 is a worked inequality route ending in an inadequate estimate,
not an impossibility theorem about every endpoint method. N03/N04 use
small controls but their full-target obligations are the different real-
witness and finite-difference closure reductions. The accepted five
attempts do not count the finite examples or certificate replays as
additional failures.

## Independent receipt

[check_interpolation_review.py](check_interpolation_review.py) and
[INTERPOLATION-REVIEW-CHECK.json](INTERPOLATION-REVIEW-CHECK.json) record
638 direct rational determinant controls, the two large reciprocal bases,
257 below-minus-two root brackets with 514 integer endpoint signs,
128 semigroup residue controls, and the small generator obstructions.
All substantive all-size conclusions use the displayed structural proofs.
No older archive or missing degree-eight certificate was recovered.

