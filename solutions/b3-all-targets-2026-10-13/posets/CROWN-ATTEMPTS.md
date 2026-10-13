# Q3498: five distinct full-target failures

All routes below are worked at the exact crown h* target; stronger-method
and relaxed counterexamples are labelled. All five counts accepted after independent review and root replay.

<a id="q3498-c01"></a>
## Q3498-C01: actual root counter-construction at larger crown sizes

Try to locate a first nonreal root by exact h* computation for n=7,...,20,
beyond the source's displayed n<=6 cases. Use the all-size transfer formula,
Newton identities and exact gamma Sturm counting in CROWN-RESULTS.md.
Every tested case has all negative real roots. This finite construction
does not disprove the conjecture or prove the arbitrary-n assertion.
The full arrays and counts are preserved, with no numerical root inference.

<a id="q3498-c02"></a>
## Q3498-C02: use a real-rooted order polynomial as an Ehrhart-transform certificate

Try certifying all roots of the order polynomial in[-1,0], a strong
root-location route to real-rooted Eulerian transforms. It fails even
on the actual four-element crown:

    Omega_(C4)(t)=t(t+1)(t^2+t+1)/6.

The quadratic factor has discriminant-3. Yet its h* is(1+t)^2.
Thus this sufficient input-root certificate is unavailable; the target
can hold without it. This is an actual obstruction to the chosen method,
rather than a counterexample to h* real-rootedness.

<a id="q3498-c03"></a>
## Q3498-C03: infer real-rootedness from the positive transfer spectrum

Equation(1) expresses Ehrhart values as traces of powers of a positive
definite kernel. Try a closure lemma asserting that a positive transfer
spectrum forces a real-rooted numerator after the Ehrhart transform.
Positivity alone is insufficient. The one-by-one kernel

    K(m)=[m^2+m+1]

is positive for all real m. Its trace at power1 has degree2 and values
E(0),E(1),E(2)=(1,3,7), so the dimension-two numerator is1+t^2,
which has nonreal roots. This is a relaxed matrix example, not the
crown kernel or an asserted lattice-polytope Ehrhart polynomial.
A valid proof must use additional structure of the min kernel and
its binomial characteristic coefficients, not just its spectrum's sign.

<a id="q3498-c04"></a>
## Q3498-C04: obtain a first-order Eulerian differential recursion

Try the natural degree-raising operator involving a quadratic multiple
of H_n and a cubic multiple of its first derivative. Reciprocity and
constant coefficient1 reduce the specific ansatz to

    H_(n+1)=[1+b*t+(1+u*D)*t^2]H_n
                  +u*t*(1-t^2)*H'_n, D=2n-2.

This is the full reciprocal family with derivative coefficient
u*t*(1-t^2), not every possible differential operator. Matching the
coefficients of t and t^2 between n=3 and4 uniquely forces
b=1214/69,u=59/69. The candidate minus actual H_4 is
384*t^3/23. Thus no such recursion holds even at that step.
Higher derivatives, other derivative coefficients or extra state
polynomials remain possible; they were not proved here.

<a id="q3498-c05"></a>
## Q3498-C05: stabilize the actual descent-top refinement

Try real stability of the multiaffine polynomial that sums, over the
actual naturally labelled crown linear extensions, the product of
variables indexed by their descent-top values. Its diagonal is H_n,
so stability would prove the full target. On the actual n=3 crown,
set x_4=-2,x_5=x_6=0. The surviving polynomial in x=x_2,y=x_3 is

    -1-x+3y+xy.

Its Rayleigh difference is(-1)*3-(-1)*1=-2. Explicitly it vanishes
at x=i,y=(2+i)/5, both in the upper half-plane. If the original
polynomial were stable, specialization of other variables to real
numbers would remain stable or identically zero. It is not zero;
alternatively perturb these real variables slightly into the upper
half-plane and solve for y continuously to obtain an actual violation.
Thus this refinement cannot supply the proposed stability certificate.
Its diagonal H_3 remains real-rooted; another refinement is not excluded.

C02 targets ordinary input roots, C03 a spectrum-only transfer lemma,
C04 a specific differential identity, C05 actual multivariate stability.
None is merged with the finite actual construction C01. No generic
gamma-positivity obstruction is counted as another attempt.
