# Nearest-root partial theorems

13 October 2026. Q1441 asks whether sup_n r_n is finite. The following
results improve partial bounds and expose one construction's limitation;
they do not provide a degree-independent upper bound. Internal review pending.

## A larger all-even-degree lower bound

Let q(z)=10z^2+10z+19. Its two conjugate zeros have squared modulus19/10,
since their product is19/10. Neither is real. Exact certificates prove

    q^128 in U_256,       q^129 in U_258.

The complete numerator coefficients and integer sign brackets are in
[NEAREST-CERTIFICATES.json](NEAREST-CERTIFICATES.json); their standard-library
verification is [check_nearest_family.py](check_nearest_family.py).
Generation used Arb only to propose brackets.

Here is the exact certificate mechanism. For m=128 or129, put n=2m,
v_k=(10k^2+10k+19)^m and

    h_j=sum_(k=0)^j (-1)^(j-k) binom(n+1,j-k) v_k.

As in the Q1443 proof, H(t)=sum_j h_j t^j satisfies
sum_k v_k t^k=H(t)/(1-t)^(n+1) at every coefficient. All h_j are positive.
The reflection q(-z-1)=q(z) makes H reciprocal; the explicit computation
also verifies h_j=h_(2m-j). Write

    H(t)=t^m g(t+t^-1),
    g(v)=h_m+sum_(j=1)^m h_(m+j) C_j(v),
    C_0=2, C_1=v, C_(j+1)=v C_j-C_(j-1).

For each base the certificate lists m disjoint rational sign-change
intervals for g, all strictly below -2. Exact integer endpoint arithmetic
and the intermediate value theorem give all m roots there. Every such
root v gives two distinct negative roots of t^2-vt+1; disjoint v values
give disjoint pairs. Thus H has all2m roots negative. Its positive
coefficients and the denominator's positive pole factors give TP of
the sampled polynomial by the AESW theorem. The verifier independently
expands t^m g(t+t^-1) and checks the entire numerator coefficient list.

The source's polynomial product-closure theorem now implies q^m in U_(2m)
whenever m=128u+129v with nonnegative integers u,v not both zero. For any
m>=128*127=16256, take v equal to m mod128, with0<=v<=127, and set
u=(m-129v)/128. This is an integer, and m-129v>=-127; divisibility by128
forces u>=0. Consequently

    r_n >= sqrt(19/10) = approximately1.378404875
    for every even n>=32512.

The two base degrees and all their nonzero nonnegative combinations also
have the bound. Earlier lower bounds at smaller degrees are preserved.
This is an all-size family derived from exact finite bases and a structural
closure theorem, not an extrapolation from numerical roots.

## Ceiling for this quadratic-power construction

For c>0, suppose (z^2+z+c)^m belongs to U_(2m), with m>=1. TP implies
sample log-concavity at k=0,1,2. Cancelling positive mth powers yields

    (c+2)^2 >= c(c+6), hence c<=2.

The endpoint c=2 is also impossible: its first four samples are
(2^m,4^m,8^m,14^m). The Toeplitz minor with rows0,1,2 and columns1,2,3 is

    v1^3 - 2v0 v1 v2 + v0^2 v3 = 56^m - 64^m < 0.

Thus c<2 for every admissible power. When c>1/4 the two root moduli
are sqrt(c), so this entire nonreal-quadratic family stays strictly
below sqrt2. Allowing m to grow cannot make its nearest roots unbounded.
No corresponding ceiling is asserted for arbitrary TP interpolation
polynomials.

## A degree-dependent upper bound from both endpoints

Normalize any member by L(P)(u)=product_i(u+a_i), 0<=a_i<=1. Its leading
coefficient is1/n!, and P(0)=product a_i,
|P(-1)|=product(1-a_i). For its n roots z_i, counted with multiplicity,

    product_i |z_i(z_i+1)| = (n!)^2 product_i a_i(1-a_i)
                         <= (n!)^2 / 4^n.

At least one root therefore has |z(z+1)|<=(n!)^(2/n)/4. Writing w=z+1/2
and using |w^2-1/4|>=|w|^2-1/4 gives

    min_(P(z)=0) |z| <= 1/2+sqrt(1/4+(n!)^(2/n)/4).

The identity includes endpoint zeros without division by P(0) or P(-1).
The upper bound grows as n/(2e), so it does not settle Q1441.

## Failure of a degree-six generator factorization

The certified polynomial q^128 cannot be written as a nontrivial product
of TP interpolation polynomials of degrees at most6. Over the reals q is
irreducible; every nonconstant real divisor is a scalar times q^j.
Such a small factor would have j=1,2 or3.

For j=1 the sampled numerator has coefficients(19,-18,19); for j=2 it
has coefficients(361,-284,2246,-284,361). These violate the necessary
nonnegative numerator condition. For j=3 the reciprocal reduction is

    g(v)=6859v^3+11306v^2+201268v+217368,
    g(y-2)=6859y^3-29848y^2+238352y-194816.

If all six numerator roots were negative, all three g roots would be
at most-2, forcing g(y-2) to have only nonpositive roots and therefore
nonnegative coefficients. Its displayed negative coefficients contradict
that requirement. Thus none of q,q^2,q^3 is admissible. This excludes
the tested generator-degree cutoff6, without making a claim about all
larger cutoffs or arbitrary factorization architectures.
