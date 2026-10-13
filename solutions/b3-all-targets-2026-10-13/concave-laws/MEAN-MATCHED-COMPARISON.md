# Mean-matched affine comparison for Q4082

Partial reduction; internal proof review pending. Let alpha=-1/beta with
beta>3. The claim below strengthens the source's mode-centered second-moment
comparison, but does not prove the proposed sharp variance constant.
Primary source: [Alqasem–Aravinda–Marsiglietti, arXiv:2610.05439v1](https://arxiv.org/html/2610.05439v1),
Definition 1.1, Proposition 4.2 and Conjecture 4.7.

If X is discrete alpha-concave with mode 0 and maximum probability C<1,
there is a two-sided alpha-affine law Z with the same C and the same mean
such that Var(X)<=Var(Z). We include one-sided affine laws as limiting
two-sided laws whose probability on one open half-line is zero.

## Existence of a mean-matched law

Put S(lambda)=sum_(k>=1)(1+lambda k)^(-beta), and
A(lambda)=sum_(k>=1)k(1+lambda k)^(-beta). Both are continuous, strictly
decreasing from infinity to zero as lambda ranges from 0 to infinity.
Set S_total=(1-C)/C. For t in [0,S_total], choose the right slope to have
tail sum t and the left slope to have tail sum S_total-t. This defines a
probability law with atom C at zero; at an endpoint one tail vanishes.
Its mean is C[A(S^{-1}(t))-A(S^{-1}(S_total-t))], a continuous increasing
function of t. Continuity at a zero tail follows by dominated convergence
and A(lambda)->0 as lambda->infinity. The endpoint means are opposite.

Compare each tail of X with the one-sided affine tail with the same C
and the same tail mass. On the nonnegative integers, the difference
between the convex sequence p(k)^(-1/beta) and the affine comparator
starts at zero. The set where p exceeds the comparator is an initial
interval. Equal tail mass therefore implies that X's tail first moment
is at most that of the affine tail. This is the same single-crossing
argument as in source Proposition 4.2, now applied to the first moment.
The positive first moment of X is at most the endpoint affine first moment
using all S_total; the negative first moment obeys the analogous bound.
Thus E X lies between the two endpoint means. The intermediate value
theorem gives a member Z of the family with E Z=E X.

## Convex-order comparison

Let h(k)=P(X=k)-P(Z=k). On each open half-line, h is positive only on an
initial interval adjacent to zero. Indeed the positive set is where a
convex sequence minus an affine sequence (equal at zero) is negative.
Extend the convex sequence by +infinity outside a finite support; this
preserves the same interval assertion. The two positive intervals together
give one interval, possibly empty or unbounded; h(0)=0.

We have sum h=0 and sum k h(k)=0. If the positive interval were unbounded
in exactly one direction, h would have at most one sign change. For a
real cutoff a at that sign change, every nonzero term of (k-a)h(k) would
have the same sign, contradicting
sum(k-a)h(k)=0. If the positive interval were unbounded both ways,
sum h=0 would already force h=0. Consequently, unless X=Z, there are
finite real cutoffs a<b with h>=0 between them and h<=0 outside.

For a convex function phi, subtract its affine secant through a,b.
The remainder is nonpositive inside [a,b] and nonnegative outside.
Multiplying by h and summing gives sum phi(k)h(k)<=0, since the secant
contributes zero by the matching mass and mean. For phi(k)=k^2 all sums
are finite: beta>3 gives finite second moments for the affine comparator,
and the source ensures the same for X. Thus E X^2<=E Z^2; subtract the
matched mean squared to obtain Var(X)<=Var(Z).

For C=1 both laws are the point mass at zero. Translation handles an
arbitrary integer mode. Endpoint one-sided comparators use +infinity on
the absent half-line and the same sign argument. This reduces the all-law
variance bound to two-sided affine laws, but their full sharp bound remains
an analytic obligation.
