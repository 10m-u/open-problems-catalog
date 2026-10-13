# Independent review of the full Q4082 proof

Accepted at the exact frozen Q4082 scope on 13 October 2026. I found no
remaining mathematical gap in the four-component proof. This is an internal
review of a local proof, with no novelty or external peer-review claim.

I read the frozen statement and the actual primary
[Definition 1.1 and Conjecture 4.7](https://arxiv.org/html/2610.05439v1),
then independently rederived the comparisons and algebra in
[MEAN-MATCHED-COMPARISON.md](../concave-laws/MEAN-MATCHED-COMPARISON.md),
[WIDE-TAIL.md](../concave-laws/WIDE-TAIL.md),
[ONE-SIDED.md](../concave-laws/ONE-SIDED.md) and
[FULL-PROOF.md](../concave-laws/FULL-PROOF.md).
The target is every discrete alpha-concave probability law on an integer
interval, including finite intervals, with -1/3<alpha<0. Put beta=-1/alpha>3.
The displayed k=(beta-2)^2(beta-3)/(beta-1)^3 is precisely the conjectured
coefficient. No symmetry, finite support or special slope is being imposed
on the original law.

## Mean matching and convex order

For fixed C=M(X)<1, translate an integer mode to zero and put
s=(1-C)/C. The affine open-tail mass S(lambda) is continuous and strictly
decreasing from infinity to zero. The corresponding first moment A(lambda)
is continuous, strictly decreasing, and tends to zero at infinity. These
facts follow from termwise dominated convergence on each compact positive
lambda interval, integral lower bounds as lambda tends to zero, and the
summable j^(1-beta) majorant at lambda>=1.

Allocating t of the unnormalized tail mass to the right and s-t to the left
therefore gives a continuous increasing mean ranging between
-C A(S^{-1}(s)) and +C A(S^{-1}(s)). Endpoint tails of mass zero mean
lambda=infinity. They are legitimate limiting comparators; no positive
finite slope is asserted for an absent tail.

For each tail of X, compare against the affine tail with the same C and
that tail's mass. The sequence q(j)=p_j^(-1/beta) is convex on its support,
and q(0) equals the comparator's affine value. The slopes
(q(j)-q(0))/j are nondecreasing. Consequently p minus the affine tail is
nonnegative initially and nonpositive thereafter. Equal tail mass yields
first-moment domination by summing (j-a) times this difference, where a is
a crossing cutoff. The endpoint comparator using all mass s has at least
this affine first moment. Hence the original mean lies between the family
endpoints, and the intermediate value theorem supplies equal means.

For that mean-matched comparator Z, on each half-line h=p_X-p_Z has its
positive entries in an initial interval next to zero, and h(0)=0. Thus,
over all integers, its positive entries lie in one interval. Finite support
of X is handled by q=+infinity outside its interval; it creates no further
positive segment.

The matching identities are sum h=0 and sum jh(j)=0. If the positive
interval is unbounded in one direction only, h has one crossing; all
nonzero (j-a)h(j) have the same strict sign, contradicting the latter
identity. If it is unbounded in both directions, h>=0 everywhere and the
mass identity forces h=0. Otherwise choose finite real a<b around its
positive entries, with h>=0 inside and h<=0 outside. The cutoffs can be
chosen between integers, so even a single positive integer presents no
degenerate secant.

A convex function minus its secant through a,b is nonpositive inside and
nonnegative outside. The affine secant contributes zero by matching mass
and mean. Therefore X is dominated by Z in convex order. All quadratic
sums converge: a normalizable convex q has linear growth along any infinite
tail, so p_j=O(|j|^-beta); beta>3 suffices. Applying the comparison to j^2
proves Var(X)<=Var(Z). The C=1 case is a point mass. This reduction does
match the mean, beyond the source's separate mode-centered comparison.

## One-sided bounds

I independently checked the Gamma identity
(1+lambda j)^-beta=E exp(-lambda jG), G~Gamma(beta,1), and the moment kernels.
The coefficient ratio in the sinh-series proof of the first-moment kernel
is bounded by 1/3; its rearrangement has the claimed direction. In the
second-moment kernel, differentiating the stated logarithmic expression
gives 4sinh(v)[v cosh(v)-sinh(v)] after the second differentiation. Its
sign proves the global bound. These do not rely on sampled inequalities.

For 0<r=lambda(beta-1)<=1, set x=1/r and D=(beta-1)/(beta-2). Substitution
into L=F^4-F^2-kBF+kA^2 gives the cubic in WIDE-TAIL.md: its x^4 coefficient
is exactly zero. The remaining bound
x^3+x^2/3-x/2-3/16 is 31/48 at x=1 and has positive derivative for x>=1.
The lower bound for A is positive; the replacement of F by x+1/2 is valid
because the relevant expression is increasing throughout the required
range.

For 1<=r<=2, the improved kernel's power-series coefficients vanish at
j=0,1,2 and equal the displayed positive rational expression at every j>=3.
Integrating gives F_0. Its correction is positive uniformly because
r^2(1+2u)(1+3u)<=20, with u=1/(beta-1) in (0,1/2).
Thus F_0>1. The A lower bound is also positive. The derivative with respect
to F is at least 2-2(1-u)/r^3>=0, so the direction of all replacements
is justified.

The resulting polynomial P is exactly the certificate's polynomial.
I rebuilt it using a separate standard-library Fraction Laurent-polynomial
implementation, then expanded each stored Bernstein basis polynomial
directly. All 221 power-coefficient slots agree exactly. All 221 Bernstein
coefficients are positive, with the stated minimum
386066666641/268738560000. This is a uniform rectangle certificate,
not a mesh or floating-point check.

For r>=2, I checked the source sum-integral argument directly: h is
unimodal, its integral gives the retained exact expression, and its
interior maximum is at most 4/r^2 after multiplying by c. The endpoint
maximum is at most one. Thus c sup h<=1 on this whole region, including
both possible locations of the maximum.

Since k/c=1-u, this gives precisely R in ONE-SIDED.md. Its derivative in
u is negative, its derivative in r is negative, and
R<=B_0 follows from its displayed expansion (the cubic u term cannot
outweigh the negative quadratic term when u<=1/2).
The Jensen bound uses the convex kernel 1/(exp(t)-1) at
E(lambda G)=r(1+u); hence F(F+1)>=H(exp(-r(1+u))) with increasing H.
I checked every interval endpoint and the four exponential upper bounds
using exact rational Taylor sums and geometric remainder estimates.
The intervals cover r>=2 without a gap and the u>=1/4 branch covers the
otherwise omitted upper portion of u. It follows that
kB<=w_1F(F+1)<=SF(F+1)=F^3-F. Dropping kA^2 here is safe.
The one-sided theorem is established for every positive lambda, and its
zero-tail endpoint is immediate.

## Gamma first-moment comparison

Let f(x)=1/(exp(lambda x)-1), h=f-Ef and
g(x)=rho(x)^-1 integral_x^infinity h(t)rho(t)dt.
Because (g rho)'=-h rho, one has h=V'g-g'. Integrating by parts gives
E h^2=E h'g and E h^2=E[g'^2+V''g^2], with V''=(beta-1)/x^2.
Cauchy-Schwarz yields the asserted variance inequality.

There is no unproved regularity assumption in this use. Near zero,
f=O(x^-1), g=O(1), rho=O(x^(beta-1));
h g rho and V'g^2 rho vanish for beta>2.
The derivative integral E[h'^2/V''] behaves as
integral x^(beta-3)dx there. At infinity g is bounded and exponential
decay kills the boundary terms. These estimates also justify the second
integration by parts.

The identity A=S+S^2+Var(f(G)) is exact. Moreover
x^2 f'(x)^2<=f(x)(1+f(x)) follows from
(lambda x)^2 f(x)(1+f(x))<=1, equivalently
sinh(lambda x/2)>=lambda x/2.
Hence Var(f(G))<=A/(beta-1), and rearrangement proves
A<=D S(S+1). This additional estimate is what controls the cross-tail
mean contribution.

## Gluing and final scope

I expanded the substituted one-sided inequalities independently. They
give exactly
L_T>=3TS_1S_2(T+1)-k[S_2A_1^2/F_1+S_1A_2^2/F_2+2A_1A_2].
The bracket is increasing in each nonnegative A_i, so replacing them by
D S_iF_i is valid. The remaining factor identity is
S_1F_1+S_2F_2+2F_1F_2=T(T+1). Therefore
L_T>=(3-kD^2)S_1S_2T(T+1)>=0, since
kD^2=(beta-3)/(beta-1)<1. One-sided endpoint cases are already covered.

Since M(Z)=M(X) and the means match, the established affine inequality
passes to X via Var(X)<=Var(Z). This proves the complete catalog target.
The exact source's asymptotic one-sided calculation in Remark 4.6 supplies
sharpness of k at each fixed beta, but is not used to prove the inequality.

## Receipt and independence limits

[check_q4082_review.py](check_q4082_review.py) is read-only with respect to
the root certificate and writes only its own
[Q4082-REVIEW-CHECK.json](Q4082-REVIEW-CHECK.json).
It independently passes 221 coefficient slots, four exponential bounds,
five interval comparisons, 41 kernel coefficients including the three
zeros, and 36 exact gluing controls. The analytic arguments above were
reviewed mathematically; finite controls alone do not prove them. This
audit did not rewrite the candidate proof or canonical data.

