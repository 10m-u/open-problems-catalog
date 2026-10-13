# Q1249: preserved subclasses and exact route obstructions

Partial work; [independent review](../stirling/HADAMARD-REVIEW.md) accepted. The target is Conjecture 1.12 of
[Katkova–Vishnyakova](https://arxiv.org/html/2512.06468v1): for entire
nonnegative A, all tails R_l A in LP-I should imply preservation of every
TP-infinity sequence. The necessity is source Theorem 1.11; polynomial
degrees two through four were already treated in the authors' earlier work.
None of the results below proves the unresolved sufficiency.

## Every shifted single pole, of every multiplicity

Assume all tails of A are in LP-I. For any l>=0, t>0 and integer m>=1,
termwise multiplication preserves the TP-infinity input

    B(z)=z^l/(1-tz)^m.

Indeed put C_l(z)=sum_(j>=0) a_(j+l) z^j, in LP-I after removing the
zero factor from R_l A. Its output is

    z^l/(m-1)! product_(h=1)^(m-1) (theta+h) C_l(tz), theta=z d/dz.

Each operator theta+h preserves LP-I. For a polynomial with nonpositive
real roots this follows from interlacing of z p'+h p with p: at a simple
negative root of p its value is z p', whose signs alternate, and the signs
at zero and negative infinity supply the remaining root. Repeated and zero
roots follow by approximation/factoring z powers. The leading and all other
coefficients remain nonnegative. Locally uniform polynomial approximations
and derivative convergence extend the result to LP-I entire functions.
The displayed output is thus in LP-I, and ASWE proves TP-infinity.
Zero tails and m=1 are included. t=0 reduces to a monomial.

For all entire TP-infinity B the classical polynomial Hadamard theorem
([Csordas–Dimitrov, Theorem 2.4(4)](https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/czdssurvey.pdf))
gives preservation from A in LP-I alone, followed by an entire limit.
Choose nonnegative LP-I polynomial approximations to both functions.
At every radius R, their coefficient sums on a larger radius than sqrt(R)
are uniformly bounded; this supplies a geometric bound on the Hadamard
tails and locally uniform convergence of the coefficient products.
The target paper does not explicitly state this classical theorem.
These cover large input
subclasses, but no proof for arbitrary distinct poles or pole/numerator
combinations follows from their union. No originality claim is made.

## Exact examples delimiting the missing step

A=1+z+27z^2/100+z^3/100 has every tail in LP-I. Its cubic discriminant
is 17/250000>0; all three roots are negative by positive coefficients.
R_1 A /z has discriminant 329/10000>0, and the later tails are linear
or monomial. Nevertheless q_2=100/27<4. Thus the necessary all-tail
condition cannot simply be upgraded to Hutchinson's sufficient q>=4 bound.

For A=1+z+z^2/10, every tail is in LP-I, but A+100 R_2 A has quadratic
discriminant -197/5. Arbitrary positive sums of tails need not be real-rooted.
This is an obstruction to a proposed cone argument; its coefficient weights
(1,1,101) are not a TP-infinity input, so it is not a catalog counterexample.

An entire TP-infinity B with B(0)=1 satisfies b_2<=b_1^2/2, by expanding
the ASWE exponential/product representation. Hence the geometric TP input
1/(1-z), whose first three coefficients are all one, cannot be approximated
coefficientwise by such entire inputs. Extending the entire-input theorem
by that density assertion fails already in three coefficients.

Finally take the partial theta function a_j=q^(-j(j-1)/2), q=18/5.
Source Theorem 1.18 proves the corresponding sequence preserves TP-infinity
because q>=3.503. In particular A is in LP-I. Its tails are a scaled
z^l A(q^(-l)z), so all are in LP-I as well. Yet its degree-two Taylor
section 1+z+5z^2/18 has discriminant -1/9. Literal Taylor truncation
does not preserve the all-tail hypothesis. The source's finite-degree
closures therefore do not pass to arbitrary entire A by this truncation.
