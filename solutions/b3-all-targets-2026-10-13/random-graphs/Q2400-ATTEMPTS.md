# Q2400: full-row log-concavity for sparse Erdős--Rényi graphs

The frozen target is G(n,d/n), **not** the regular-graph model: for every
sufficiently large fixed d, the entire unweighted independent-set row
should be log-concave with probability tending to one. Primary
[Heilman, journal Question8.1](https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.23225)
has this scope. The old n^(1/3) prefix and positive expectation of the
defect are retained; replaying either counts zero. Five new worked
full-target routes follow, pending independent review. Partial results
do not reset a failure counter.

<a id="q2400-a1"></a>
## A1: second-order edge-overlap induction for the complete row

Retain adjacent-edge and disjoint-edge pair intersections in the
Bonferroni estimates, instead of the earlier edge union bound. The
resulting deterministic criterion, exact curvature cancellation and
probability estimates are proved in [BONFERRONI-PREFIX](BONFERRONI-PREFIX.md).
For m edges and W adjacent edge pairs, put
mu_l=m(l)_2/(n)_2 and
`nu_l=W(l)_3/(n)_3+binom(m,2)-W_4/(n)_4`.
The exact sufficient conditions

    mu_(k+1)<=1/2, nu_(k+1)<=1/[12(k+1)]

imply the actual inequality at index k. The important new cancellation
is L_k^2-L_(k-1)L_(k+1)=2aL_k+4a^2 k(k-1), where
L_k=1-mu_k and a=m/[n(n-1)].

Combining edge Chernoff and wedge Markov bounds gives simultaneously
all k<=K, with K asymptotic to (384d^2)^(-1/5)n^(2/5), with probability
at least1-exp[-d(n-1)/6]-1/(2 log n), for the explicit size conditions
in the proof. This is an all-size asymptotic partial improvement, not
another finite rerun of the old prefix. Its failure probability is
weaker than the previous smaller-prefix exponential bound.

The full-target extension fails within this developed truncation:
at k=rho n and m of order n, mu_k is of order n. The lower bound
1-mu_k is negative and cannot be squared as a lower bound on a count.
The second-order error is also not small. No uniform high-order
resummation was obtained. This worked second-order correlation route
counts once, with its stronger partial retained and full scope unresolved.

<a id="q2400-a2"></a>
## A2: strengthen to univariate real-rootedness with high probability

If I_G has real roots, Newton's inequalities prove the desired row.
Try to establish that stronger sufficient property for the exact
random model, using local tree structure or a root-preserving induction.
[ISOLATED-TREES](ISOLATED-TREES.md) proves the opposite strengthening:
every fixed tree occurs as an isolated component with probability
1-O_d(1/n), by an explicit second moment.

For a claw, I_T=1+4x+3x^2+x^3 has discriminant−31. Therefore a pair
of nonreal roots persists as a factor of I_G whenever an isolated claw
is present, and P(I_G real-rooted)=O_d(1/n)->0. This is an actual
random-model asymptotic obstruction, not just an induced subgraph
that might disappear after specialization. The claw's unweighted row
is log-concave, and this does not disprove Q2400. A proof must permit
nonreal roots or avoid that stronger certificate.

<a id="q2400-a3"></a>
## A3: obtain the unweighted theorem from a multivariate exchange certificate

Try to use a homogenized independent-set polynomial with Lorentzian
support/exchange, so its positive specializations would give a
coefficient inequality theorem covering all weights and hence the
unweighted target. The proposed support lemma fails on actual legal
independent sets: in an induced path, compare the singleton center with
the two leaves. Exchanging the center for either deficient leaf would
require an illegal center/other-leaf pair in the second support vector.
Thus the support is not M-convex and cannot be Lorentzian.

The same frequent isolated-claw event from A2 contains this path. The
failure concerns multivariate support, independently of the scalar
root computation. Moreover a claw with center weight10 and leaf
weights1 has row [1,13,3,1], failing3^2>=13. For any graph containing
an induced claw, give all other vertices sufficiently small positive
weights: continuity preserves this strict failure. Hence an all-positive
weight log-concavity theorem would itself be false for such graphs.
These exact support and specialization arguments appear in ISOLATED-TREES.

This excludes the worked universal multivariate/weighted certificate,
not the unweighted conjecture. A2 and A3 share an actual frequent
component but attempt different root and support/weight theorems; their
shared witness is disclosed and is not an extra attempt.

<a id="q2400-a4"></a>
## A4: construct an actual random-model failure in complete coefficient rows

Compute every independent-set coefficient of144 seeded actual
Erdős--Rényi samples: n=24,32,40,48; d=8,12,16; twelve trials per
(n,d). Each possible edge is selected independently with probability
d/n. Deletion/closed-neighborhood recursion with integer arithmetic
counts complete rows through their actual independence numbers; the
initial coefficients1,n,binom(n,2)-m are exact controls. All144 rows
are log-concave with interval support. Actual edge lists and every row
are retained in [GRAPH-PROBE](GRAPH-PROBE.json).

The construction was aimed at the full finite row, including its tail,
and differs from A1's growing initial-range proof. It produced no
counterexample. Even a finite failing sample would not by itself
disprove a probability limit; conversely these passing samples prove
no asymptotic statement at fixed d. No literature data or old prefix
replay is counted. This is one bounded construction route, not one
failure per parameter or random trial. The required asymptotic
sign theorem or positive-probability obstruction remains missing.

<a id="q2400-a5"></a>
## A5: reduce the full row to log-concavity of each connected component

Convolution preserves log-concavity with no holes. Try to prove every
component separately and multiply their rows; this could exploit the
exact component decomposition instead of a scalar root theorem.
The proposed high-probability component condition is false even for
arbitrarily large fixed d.

Use the published26-vertex tree T1 of
[Kadrawi--Levit, Section2](https://arxiv.org/html/2305.01784): center plus
three roots with3,4,4 length-two pendant arms. Direct branch counting
gives product_(k in {3,4,4})[(1+2x)^k+x(1+x)^k]+x(1+2x)^11.
The top three coefficients are2979,51,1, so the penultimate
log-concavity defect is−378. The known tree is independently rebuilt
from its edge list and its complete row matched by deletion recursion.
It is attributed evidence, not a new deterministic tree counterexample.

The new full-target inference applies the isolated-tree second moment
with h=26 and automorphism count6912. An isolated copy occurs with
probability1-O_d(1/n), so the event that **every** random-graph component
has a log-concave row has probabilityO_d(1/n)->0. This is different from
A2's real-root certificate: it attacks direct coefficient positivity
of the factors, even without roots, using an actually non-log-concave
factor. It is also different from A3's vertex-weight strengthening.

A bad factor does not force the product to be bad. The missing proof
must quantify compensation between the other factors, including the
giant component, rather than require them all to satisfy the desired
property separately. No such compensation theorem was obtained.
Replaying the known tree alone is not counted; the worked random-model
component reduction and explicit failure probability constitute this route.

## Pending disposition

The second-order n^(2/5) prefix is a proved partial awaiting independent
scope review. The stronger real-root, support/weight and componentwise
conditions have actual asymptotic obstructions. The catalog question
is unresolved. Five distinct substantive full-target failures are
proposed; no sixth route starts unless a count is rejected. All finite
controls are in [GRAPH-ROUTES-CHECK](GRAPH-ROUTES-CHECK.json).
