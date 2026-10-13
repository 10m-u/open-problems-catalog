# Q4665: weighted midpoint Schur inequalities

The full four-function Schur-positive Klartag--Lehec conjecture remains
unresolved. Primary: Chan--Chen--Pak--Soskin,
[Conjecture11.5](https://arxiv.org/html/2606.06688v1#S11.SS2),
local collections-221c62a81993aeb9.txt.gz. The condition uses coordinatewise
rounded **midpoints**, not meet and join. The source's old computation
uses length<=3 and size<=10. It is not counted as a new attempt.

For partitions lambda,mu padded to length l put
U(lambda,mu)=ceil((lambda+mu)/2) and V(lambda,mu)=floor((lambda+mu)/2).
Both are partitions, and U+V=lambda+mu. Functions a,b,c,d have finite
support, take nonnegative real values and satisfy

    a(lambda)b(mu)<=c(U(lambda,mu))d(V(lambda,mu)).       (1)

Write A=sum a(lambda)s_lambda and similarly B,C,D. The goal is that
CD-AB has nonnegative coefficients in the full Schur basis.

## A useful all-support sufficient criterion

For every output pair (u,v) define the **summed** input weight

    w(u,v)=sum_(U(lambda,mu)=u,V(lambda,mu)=v) a(lambda)b(mu).

If w(u,v)<=c(u)d(v) for every pair, then the requested inequality holds.
Indeed the established pairwise midpoint theorem gives
s_lambda s_mu<=_s s_U s_V. Summing with nonnegative weights yields
AB<=_s sum w(u,v)s_u s_v<=_s CD. The second inequality includes unused
CD pairs with nonnegative coefficients. This criterion is stronger than
(1), which bounds each input separately rather than their sum.

In particular (1) proves the full conjecture whenever the map
(lambda,mu)->(U,V) is injective on supp(a)x supp(b). It is injective if
either a or b has singleton support: U+V determines the other input once
one is fixed. Thus this is a proved arbitrary-l, arbitrary-size, arbitrary
real-weight family. It is not the conjecture for general colliding supports.
The pairwise midpoint theorem is prior literature:
[Lam--Postnikov--Pylyavskyy, Theorem11](https://math.mit.edu/~apost/papers/schurpositivity.pdf)
(straight shapes are the empty-inner-shape case), also Theorem3.3 in
the current source. No novelty is claimed for that underlying theorem.

## An actual failure of the naive fiber-budget inference

Already at l1, take a=b=1 on partitions0 and2, and c=d=1 on0,1,2.
Every local condition (1) holds. Two inputs (0,2) and(2,0) both map to
(1,1); their summed weight is2 but the output budget c1d1 is1.

Use h_k=s_(k), h_0=1. Here A=B=1+h2, C=D=1+h1+h2, and the **actual**
target difference is

    CD-AB=2s_(1)+s_(2)+s_(1,1)+2s_(3)+2s_(2,1),

which is Schur-positive. Pushing every input pair independently produces
P=1+2h1^2+h2^2, however, and

    CD-P=2s_(1)+s_(2)-s_(1,1)+2s_(3)+2s_(2,1).

The second stage of that proposed decomposition has a negative Schur
coefficient. The positive part P-AB=2s_(1,1) compensates it in the full
expression. Therefore a proof cannot discard that compensation by
asserting summed fiber budgets follow from (1). This is a failure of the
specified decomposition, not a conjecture counterexample.

## No fixed relabeling converts midpoint conditions into ADS conditions

At l1, let a0=b2=c1=d1=1 and all other weights zero. The sole nonzero
input pair satisfies (1). The meet/join condition instead requires the
positive input weight to be bounded by c2d0=0, and fails. The actual
Schur difference h1^2-h2=s_(1,1) is positive.

More structurally, any injective relabeling of the integer chain sends
two distinct inputs to distinct labels, so their minimum and maximum
stay distinct. Their midpoint outputs for input0,2 are both1. Thus no
common injective coordinate relabeling can conjugate these two pair
operations on all inputs, regardless of whether it preserves order.
The same obstruction embeds in any partition length using one-row
partitions. A more elaborate lifting to an auxiliary lattice is not
excluded; a direct or conjugated use of the proved ADS theorem fails
its hypothesis. The primary source's general non-comparability observation
is attributed, while this contract and explicit operation obstruction
are the worked route here.

## All nonnegative evaluations are a weaker consequence

Fix any finite nonnegative alphabet x. Multiply each weight by the
nonnegative number s_lambda(x). The pairwise midpoint Schur theorem
implies its numerical counterpart, so the four multiplied functions
satisfy the scalar KL hypothesis. Extend them by zero outside partitions
in Z^l and apply the scalar KL theorem. This proves

    CD(x)-AB(x)>=0

for every such x and every actual legal input, at all sizes. The use of
the known scalar KL and pairwise midpoint theorems is explicit; this is
a numerical consequence, not a new full Schur theorem.

The hoped-for final inference from evaluation positivity to Schur positivity
is false in the ambient symmetric-function ring. The formal comparison

    f=s_(2)-s_(1,1)=sum_i x_i^2

is nonnegative on every nonnegative alphabet, and even has nonnegative
monomial coefficients, but has a negative Schur coefficient. It is **not**
asserted to arise from legal four-function inputs. Thus scalar evaluations
alone cannot supply the needed final coefficient proof without an additional
theorem about this special family of differences.

## A fixed-output LR domain is not closed under uniform coordinate rounding

One coefficient approach fixes nu and sums c_(lambda,mu)^nu with the
four weights. Try applying scalar midpoint KL on the joint boundary
indices and their Littlewood--Richardson objects. Uniformly rounding all
coordinates of a joint midpoint requires the fixed-output domain to stay
closed. It does not, already for nu=(N), N>=2. Both joint boundary pairs

    (lambda,mu)=(0,N), (1,N-1)

have LR coefficient1 to nu=(N). Their coordinatewise uniform ceiling
and floor in the **joint** (lambda,mu) space are (1,N) and(0,N-1).
Their total degrees are N+1 and N-1, so both have LR coefficient0 to
the same nu. No tableau interior coordinates can repair the violated
degree equality. This proves an all-N fixed-boundary support obstruction
to that particular KL lifting.

These joint midpoints differ from U,V in (1); the proposed proof tried
to use them to handle two summands in a fixed coefficient. Balanced
rounding, changing the output, or another combinatorial kernel may
still work. This is separate from the one-pair fiber collision and
from min/max ADS substitution.

## Fresh exact weighted construction attempt

check_schur_routes.py builds32 actual instances with two inputs in each
of supp(a) and supp(b), every a-partition of size>10, including length4.
Weights are positive integers and rational numbers. Choose c on the
ceiling images, then set each d(v) to the maximum of
a(lambda)b(mu)/c(U) over pairs mapping to floor v. This enforces every
local condition exactly, including colliding outputs; all other inputs
have zero left-hand side. The checker records the full a,b,c,d functions
and every coefficient of CD-AB using literal ballot skew LR tableaux.
All32 differences are Schur-positive.

This is one bounded attempted counter-construction beyond the source
range, not32 separate failures and not an all-support proof. It retains
reproducible exact evidence, with a second product-expansion review still
required. The all-size partials above are proofs, not extrapolations of
these finite checks.
