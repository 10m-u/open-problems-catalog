# Q3500: five proposed full-target failures

Each route addresses arbitrary-n Boolean real-rootedness. Independent
review accepted all five counts. Partials do not reset the counter.

<a id="q3500-b01"></a>
## B01 — actual Boolean root counter-construction

Compute the actual h* by ideal/last-label DP, extract gamma, and count
negative roots with exact Sturm arithmetic for n=0,...,5. Every row
passes. The degree26 n=5 row, with all coefficients and finite control
counts, is retained. The primary's Boolean conjecture supplies no
displayed finite testing bound to compare against; we make no new-range
or novelty claim. This fresh exact construction attempt fails to find
a nonreal root and does not prove arbitrary n.

<a id="q3500-b02"></a>
## B02 — real stability of actual descent-top refinement

Try the naturally labelled multiaffine descent-top polynomial whose
diagonal is Boolean h*. For the actual B3, label all subsets by size
then binary code, starting at1. The minimum is1, singleton labels are
2,3,4, pair labels5,6,7, and maximum8. Set x5=-2,x6=x7=0. Its remaining
polynomial in x=x3,y=x4 is -1-x+3y+xy, with Rayleigh difference-2.
It vanishes at x=i,y=(2+i)/5 in the upper half-plane. A nonzero real
specialization of a stable polynomial would remain stable, so this
actual refinement is not stable. The full Boolean h* diagonal is
real-rooted. A different refinement is not excluded. B3 with its
extrema removed is isomorphic to C6; this structural overlap is
explicit, but the Boolean target is independently checked.

<a id="q3500-b03"></a>
## B03 — certify real input roots before the Eulerian transform

Try sufficient ordinary order-polynomial root-location conditions.
Already for actual B3 the exact weak order polynomial is

    Ω(t)=t(t+1)(t+2)(t+3)
         ·(2t⁴+12t³+25t²+21t+10)/1680.

The displayed quartic has no real roots by exact Sturm counting. Thus
Ω has nonreal roots despite its real-rooted h*; a proof requiring all
ordinary input roots to lie on the real interval cannot cover it.
This is a different input obligation from B02's multivariate descent
stability. It is not a Boolean conjecture counterexample.

<a id="q3500-b04"></a>
## B04 — a universal scalar recurrence for P×C2

Develop the source's proposed doubling induction by computing the
output from |P| and h*_P alone, then applying a root-preserving scalar
operator. The worked P,Q pair in BOOLEAN-RESULTS.md has identical
input data but outputs differing by4t²+4t³. Thus this exact universal
operator cannot exist, linear or nonlinear. The failure is information
loss, not a failure of real-rootedness preservation. Richer state
polynomials or a Boolean-only recurrence remain possible; neither
was obtained for the arbitrary-n target.

<a id="q3500-b05"></a>
## B05 — infer roots from reciprocity, gamma positivity and log concavity

Try to promote nonnegative gamma coefficients and reciprocal, positive,
log-concave h* data to all negative real roots. Strengthen that proposed
lemma by matching the actual B4 degree11, h0=1,h1=151 and extension
total1,680,384. Its actual gamma is

    (1,140,3546,24212,43648,14400).

Move300 from gamma2 to1,200 in gamma3, preserving h1 and total because
the corresponding evaluation-at1 weights differ by a factor4. The
formal gamma becomes(1,140,3246,25412,43648,14400), with transformed h

    (1,151,4561,53339,250964,531176,
     531176,250964,53339,4561,151,1).

Every gamma coefficient is positive. The h row is positive, reciprocal
and log-concave; all these checks are exact. But its degree-five gamma
has only three negative real roots, so the reciprocal h has nonreal
roots. This is a formal polynomial, not asserted a poset h* or actual
Boolean row. The explicit stronger-data relaxation demonstrates that
a full proof needs Boolean structure beyond those scalar properties.
This differs from B04's actual nondeterminacy of the doubling output.

The full conjecture stays unresolved after these five proposed routes.
Code, actual examples and labelled formal controls are retained in
check_poset_routes.py and POSET-ROUTES-CHECK.json.
