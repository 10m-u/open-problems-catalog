# Q3892: ordering families and failed extensions

The full Koszul Roller Coaster conjecture is unresolved. The target asks
for **every** permutation of the entire first half for every sufficiently
large socle degree, not just one nonunimodal algebra or a subsequence.
This packet proves the descending order in every degree, and obstructions
to five worked extension methods. Independent review is pending.

Primary setup: Holleben--Nicklasson, *Roller Coaster Gorenstein algebras
and Koszul algebras failing the weak Lefschetz property*, JPAA230 (2026),
108238, [final DOI](https://doi.org/10.1016/j.jpaa.2026.108238),
local text collections-144d1501001defb3.txt.gz. Sections4--5 and
Conjecture5.8 were read. The known unrestricted Gorenstein theorem5.7
and known whiskered WLP failures are prior evidence, not new solve attempts.
For the topology-to-Koszul implication use the original
[D'Alì--Venturello paper](https://arxiv.org/abs/2106.05051), Section8:
the relevant complexes here are explicitly **flag** and pure.

## A descending Koszul family in every socle degree

Let q=d-1>=2. Let Delta be the join of q discrete sets of size s>=1.
Its facets choose exactly one vertex from each set. It is pure, flag and
shellable. One explicit shelling orders the facet tuples lexicographically:
the preceding-facet intersection for a new tuple is the union of its
codimension-one faces obtained by changing a coordinate that is not first
in its coordinate order. Every previously appearing face is contained
in one such face, which gives the shelling condition. For s=1 it is a
simplex. The algebra with dual generator

    F_Delta=sum_(facet T) X_T product_(v in T) U_v

is Artinian Gorenstein, has socle degree d, and is G-quadratic/Koszul by
the primary Section8 result (also cited in final Theorem4.4). Its face
polynomial is (1+sz)^q, so direct derivative/apolar idealization gives

    h_i=binom(q,i)s^i+binom(q,i-1)s^(d-i),  1<=i<=d-1,
    h_0=h_d=1.                                         (1)

For s>=2q+1 and 1<=i<floor(d/2), the second term in h_i alone exceeds
h_(i+1). Indeed i+1<=d-i-1 and s>=1 give

    h_i >= binom(q,i-1)s^(d-i),
    h_(i+1) <= 2 binom(q,i)s^(d-i-1),

and s>2 binom(q,i)/binom(q,i-1)=2(q-i+1)/i. Thus

    h_1>h_2>...>h_floor(d/2)

in **every** d>=3. This realizes the descending permutation, even though
it requires rapidly growing embedding dimension. The ascending permutation
is already realized by a quadratic complete intersection, or s=1 in (1),
which gives h_i=binom(d,i). No arbitrary-permutation theorem follows.

## Why the published approximate-graph transfer cannot simply be made CM

In the known unrestricted proof, put q=d-1, k=ceil(q/2),
b=binom(q,k+1), N=3^q, and take the approximate independence coefficients

    a_i=binom(q,i), i<k;   a_i=N+pi(i)b, k<=i<=q,

where pi permutes k,...,q. We prove that for q>=10 **no** well-covered
epsilon-certificate with epsilon<=1 can have Cohen--Macaulay independence
complex. This strengthens the mere observation that the known existence
theorem does not assert CM; it gives a uniform obstruction to these
particular target coefficients.

Suppose a pure rank-q complex has face numbers f_i (i-element faces),
with |f_i/T-a_i|<epsilon for 1<=i<=q. If it is CM, every coefficient of
its ordinary h-polynomial

    c_j=sum_(i=0)^j (-1)^(j-i) binom(q-i,j-i) f_i

is nonnegative. Set j=k+1 and t=q-k>=2. The high-index contribution
is at most (1-t)N+qb <= -N+q2^q. The exact contribution from i=1,...,k-1
to the target values is

    binom(q,j)[k-(-1)^j].

Since f_1>=q and f_1/T<q+epsilon, 1/T<=1+epsilon/q<=2. The empty-face
contribution is at most2 binom(q,j). The sum of absolute coefficients
of the other errors is

    sum_(i=1)^j binom(q-i,j-i)=binom(q,j-1)<=2^q.

It follows that

    c_j/T <= -3^q+(q+k+4)2^q < 0,                    (2)

for q>=10. The final strict inequality holds at q10 and propagates:
when q increases by1 the linear factor q+k+4 increases by at most2,
while (3/2)^q multiplies by3/2. This contradicts CM nonnegativity.
The actual graph certificate is well-covered and flag, but its resulting
apolar algebra therefore fails the CM/Koszul condition in this construction.
The unrestricted existence theorem is not a proof of Q3892.

## Limits of one-parameter joins

For fixed q, all first-half entries in (1) are polynomials in the single
size parameter s of degree at most q. If k=floor((q+1)/2), each of the
binom(k,2) differences has at most q real zeros unless it is identically
zero (which would only forbid strict orderings). Therefore at most

    q binom(k,2)+1

strict permutations occur as s ranges over the positive real line;
at a comparison zero a strict permutation cannot occur. Restricting
to positive integers cannot increase this bound. For d>=12 the bound
is smaller than k!: at k6 it is at most12*15+1<720, and the factorial
growth dominates the cubic bound thereafter. Consequently this **equal
part size** join family cannot prove the full conjecture for any sufficiently
large degree. This does not restrict joins with unequal sizes or general
CM flag complexes.

## Tensoring a fixed nonunimodal seed washes out its order

The q3,s6 join gives the actual G-quadratic seed
h=(1,234,216,234,1). Tensor it with r copies of K[t]/(t^2).
The result stays Artinian Gorenstein and Koszul, but for every r>=1
its first half is **strictly increasing**. Thus the seed's h_1>h_2
cannot be preserved by this degree-raising operation.

Put N=r+4. Its Hilbert polynomial is

    (1+z)^N+230z(1+z)^(N-2)-250z^2(1+z)^(N-4).

For i=0 the next coefficient is larger. For i=1 its difference is
(N-3)(N/2+230)-250>0 when N>=5. For 2<=i<floor(N/2), write the difference
as A+230B-250C, with

    A=binom(N,i)(N-2i-1)/(i+1),
    B=binom(N-2,i-1)(N-2i-1)/i,
    C=binom(N-4,i-2)(N-2i-1)/(i-1).

These are positive and
C/B=i(N-i-1)/[(N-2)(N-3)]<=1/2 in this range, N>=6.
Hence the difference is at least A+105B>0. This exact all-r proof is
stronger than a finite smoothing observation. It does not exclude
using a degree-dependent seed or another tensor factor.

## Reciprocal Hilbert positivity does not imply a Koszul realization

For r>=3, the actual complete intersection

    C_r=K[u,v,t_1,...,t_r]/(u^3,v^3,t_1^2,...,t_r^2)

is Artinian Gorenstein, has
H_r(z)=(1+z+z^2)^2(1+z)^r, embedding dimension r+2 and socle degree r+4.
Its formal reciprocal 1/H_r(-z) has nonnegative coefficients in every
degree. For r3 this follows from the exact identity

    1/H_3(-z)=(1+z)^2(1+z+z^2)^3(1+z^3)/(1-z^6)^3;

for larger r multiply by (1-z)^(-(r-3)). Thus the usual Koszul Poincare
necessary positivity test passes at all orders.

Nevertheless **no** standard graded Artinian quadratic algebra can have
this Hilbert function. Any m-primary ideal generated by quadrics in N
variables over an infinite field contains a regular sequence of N quadrics:
successively choose an element of the quadratic span outside the finitely
many associated primes, using prime avoidance and the m-primary property.
The corresponding quadratic complete-intersection quotient vanishes
above degree N; every further quotient does too. Here d=r+4>N=r+2.
In particular no Koszul algebra realizes H_r. This actual Gorenstein
all-r family refutes a sufficient numerical test, not the conjecture's
orders with freely chosen embedding dimension.

## Additive assembly by connected sums leaves the Koszul class

Take two quadratic complete intersections on separate d-variable sets,
d>=3, and identify their socles after annihilating all cross products.
The resulting standard graded Artinian Gorenstein connected sum is

    K[x_1,...,x_d,y_1,...,y_d]/
    (x_i^2,y_i^2,x_i y_j, x_1...x_d-y_1...y_d).

Its Hilbert vector is (1,2binom(d,1),...,2binom(d,d-1),1).
The displayed degree-d relation is necessary: modulo the quadratic
relations alone the two degree-d squarefree products remain independent.
Thus the ideal has a minimal generator of degree d>=3 and the algebra
cannot be Koszul. It also equals the simplicial algebra of two disjoint
(d-2)-simplices, a pure flag complex which is not CM (its reduced H_0
is nonzero). Consequently this natural operation for adding contributions
to prescribed Hilbert entries cannot serve as a Koszul assembly lemma.
Tensor products preserve Koszulness but convolve the rows; connected sums
add internal entries but fail this required algebraic property.

## Scope of the executable controls

The checker uses integer/Fraction polynomial operations: it verifies51
CM coefficient bounds,58 descending degree rows, literal join faces,
ordering-region bounds,80 padding rows, all-r reciprocal identities with
ten coefficient controls, and18 connected-sum rows. These support the
written infinite-family proofs. No computation claims the full conjecture
false or realized for arbitrary permutations.
