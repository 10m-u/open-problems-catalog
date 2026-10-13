# Q3500: exact Boolean controls and information needed for induction

The primary [Conjecture 6.9](https://arxiv.org/html/2504.05123v5) asks
real-rootedness for every Boolean lattice. It remains unresolved here.
No novelty or external-review claim is made.

## Exact bounded roots

The ideal DP in check_boolean.py computes the naturally labelled linear
extension descent polynomial, equal to the order-polytope h*. Removing
the unique minimum and maximum changes neither descents nor h*. For
n=0,...,5 exact gamma Sturm certificates give only negative real roots.
The complete arrays and ideal-state counts are BOOLEAN-CHECK.json; n=5
uses 7,579 internal ideals and degree26. These are bounded certificates.
The route checker independently reconstructs n=0,...,4 without removing
the extrema.

## The scalar input polynomial does not determine doubling

Let P be the four-element star with one minimum and three incomparable
maxima, and Q the disjoint union of two two-element chains. Both have

    h*_P=h*_Q=1+4t+t².

Yet direct naturally labelled extension DP gives

    h*_(P×C2)=1+27t+116t²+116t³+27t⁴+t⁵,
    h*_(Q×C2)=1+27t+112t²+112t³+27t⁴+t⁵.

They have the same input size and polynomial, but different output
coefficients and extension totals. Thus no deterministic scalar operator
on the pair (|P|,h*_P) computes h*_(P×C2) for every finite poset.
Both outputs remain real-rooted: their gamma rows are(1,22,40) and
(1,22,36). This does not disprove the source's real-rootedness-preservation
proposal. A valid induction may need a richer invariant of P, or may be
a Boolean-specific recurrence rather than a universal scalar transform.

Further exact ordinary-root, stability and gamma information obstructions
are recorded in BOOLEAN-ATTEMPTS.md. Formal polynomial examples there
are not asserted to be Boolean h* polynomials.
