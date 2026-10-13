# Q1443: a real-root gap of 14/5

13 October 2026. Full counterexample accepted after internal independent review; see
[ROOT-REVIEW.md](../ROOT-REVIEW.md#q1443-root-gap-counterexample).
The question asks for a universal 1<=d<2 bounding every consecutive real-root
gap of every real-rooted polynomial whose sampled values form a TP sequence.
Here TP means nonnegative minors, as in the frozen catalog and the primary
[July source](https://arxiv.org/html/2607.06207v1).

Consider the integer polynomial

    P(z) = (2z+1)^32 (5z+2)^2 (5z-12)^2.

Its degree is 36, its leading coefficient is positive, and its complete real
root multiset consists of -1/2 with multiplicity 32, -2/5 with multiplicity
2, and 12/5 with multiplicity 2. Thus its final two distinct roots are
consecutive in the multiset and have gap 12/5-(-2/5)=14/5>2.

It remains to certify all-length TP of (P(k))_(k>=0). Define the degree-36
integer polynomial H(t)=sum_(j=0)^36 h_j t^j by

    h_j = sum_(k=0)^j (-1)^(j-k) binom(37,j-k)
                         (2k+1)^32 (5k+2)^2 (5k-12)^2.

The finite-difference identity for every degree-36 polynomial gives

    sum_(k>=0) P(k)t^k = H(t)/(1-t)^37.

For completeness, write d_j=Delta^j P(0). The Newton expansion of P gives
H(t)=sum_j d_j t^j(1-t)^(36-j), so the displayed h_j formula and the
generating-function identity hold at every coefficient, not only at the
first 37 sampled values.

[Q1443-COUNTEREXAMPLE-CERTIFICATE.json](Q1443-COUNTEREXAMPLE-CERTIFICATE.json)
contains all 37 positive integer h_j and 36 disjoint rational intervals
strictly below zero. H has opposite nonzero signs at the endpoints of each
interval. Exact integer arithmetic verifies those signs. The intermediate
value theorem therefore supplies 36 distinct negative roots, exhausting
the degree. In particular all roots of H are negative.

The [checker](check_gap_certificates.py), run with `--counterexample`,
reconstructs H independently from the Newton differences, verifies the
coefficient list and every disjoint sign-change bracket, and checks two
additional generating-function coefficients beyond the interpolation
samples. It uses only the Python standard library for verification.
Arb was used to propose the brackets during generation; its numerical root
classification is not needed for the proof. The exact receipt is
[Q1443-COUNTEREXAMPLE-CHECK.json](Q1443-COUNTEREXAMPLE-CHECK.json).

Consequently H(t)=h_0 product_i(1+alpha_i t) with h_0>0 and alpha_i>0.
Together with the 37 positive factors (1-t)^(-1), this is the generating
function form in the Aissen–Edrei–Schoenberg–Whitney theorem, stated as
Theorem A in the primary source. Hence (P(k))_(k>=0) is TP and P belongs
to U_36. The proposed universal bound below 2 is false. This is a complete
counterexample, rather than a bounded screen of Toeplitz minors.

## G01: construction route and earlier controls

This was the first full-target construction attempt in the present run.
The initial family was

    (2z+1)^M ((bz-b+a)(bz-b-a))^2.

For a/b<1 its two quadratic roots are 1-a/b and 1+a/b. Exact Sturm
counts at a/b=9/10 yielded 54 negative numerator roots out of 56 when
M=52, and all 68 when M=64. Subsequent Arb proposals suggested gaps
1.9, 1.98, 1.998 and 1.9998 at larger degrees. Those experiments alone
would not resolve the universal bound. Testing a/b>1 produced the much
smaller certified witness above. Only its exact rational bracket certificate
is required for the resolution. No claimed limit or eventual-real-rootedness
theorem is used.

The full solution passed independent review, so Q1443 is stopped immediately
under the user's rule. Earlier dated lower-bound submissions remain intact;
this counterexample supersedes their unresolved status without changing
their proof scopes. No novelty or external peer-review claim is made.
