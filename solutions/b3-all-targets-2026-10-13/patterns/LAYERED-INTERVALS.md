# All-size interval families for Q1366

The order is classical subsequence containment, counting distinct standardized
permutations, not occurrences. These are partial elementary proofs; no claim
of novelty or general closure is made. The primary
[Vatter, Conjecture 2.2 and layered setup](https://arxiv.org/html/2602.16355v2)
uses the same order and explains why a componentwise composition theorem
does not cover arbitrary layered permutations.

Write delta_a for a decreasing block of length a. A layered permutation is
delta_(a1) direct-sum ... direct-sum delta_(aL), with all a_j positive.
Its decreasing-layer decomposition is unique. Containment between layered
permutations means embedding the lower composition as a subsequence of the
upper composition, with coordinatewise bounds on the selected parts.

## Equal numbers of layers

If bottom b and top a both have L layers, every intermediate permutation
also has exactly L layers: containment cannot increase the number of
layers. Consequently its composition c satisfies b_j<=c_j<=a_j for every
j; the increasing embedding of L indices in L positions is the identity.
The interval is the product of chains of lengths a_j-b_j+1, and its rank
polynomial is

    product_j (1+x+...+x^(a_j-b_j)).

Each factor has positive, log-concave coefficients with interval support.
Convolution preserves these two properties. One elementary proof uses the
Toeplitz matrices T(u)[i,j]=u_(j-i), extending u by zeros: every order-two
minor is nonnegative because decreasing neighboring ratios imply all
longer cross inequalities. T(u*v)=T(u)T(v), so the order-two Cauchy--Binet
formula proves the same inequalities for the convolution. Only finitely
many intermediate indices contribute to each fixed minor. This handles
every number of layers and arbitrary gaps. Rank zero factors are allowed.

## Every interval below two decreasing layers

Let top=delta_a direct-sum delta_b, a,b>=1. A two-layer bottom is covered
above. For a one-layer bottom delta_s, assume a<=b by reversing the two
layers; then s<=b. Every intermediate is either delta_r with s<=r<=b,
or delta_i direct-sum delta_j with 1<=i<=a,1<=j<=b and max(i,j)>=s.
These types are disjoint and have unique parameters.

Let c_r count elements of length r, for s<=r<=a+b, and let (u)_+=max(u,0).
Counting bounded positive pairs gives the following exact formulas:

    if s<=a:
      c_r=1+2(r-s)-(r-a-1)_+-(r-b)_+-(r-2s+1)_+;
    if s>a:
      c_r=1+(r-s)-(r-b)_+-(r-a-s)_+.

For example the unrestricted pair count is
(r-1)_+-(r-a-1)_+-(r-b-1)_++(r-a-b-1)_+.
Subtract the pairs with both coordinates<s and add the single-block
indicator. On the stated range the final unrestricted term vanishes;
the indicator combines with -(r-b-1)_+ to give 1-(r-b)_+.
These operations give exactly the displayed formulas in both cases.

Each formula is an affine function minus nonnegative hinge functions.
Thus c_(r-1)+c_(r+1)<=2c_r at every interior index. Every c_r is positive:
a saturated chain between the endpoints supplies every length. For
positive numbers, arithmetic concavity implies log-concavity by
c_(r-1)c_(r+1)<=((c_(r-1)+c_(r+1))/2)^2<=c_r^2.
The rank row is therefore log-concave for every a,b,s. One-layer tops
give chains. This proves Q1366 for every nonempty-bottom interval whose
top has at most two decreasing layers. Empty-bottom intervals are outside
this particular log-concavity claim.

## A unique inversion and the exact occurrence fibers

For p,q>=0 take top=iota_p direct-sum 21 direct-sum iota_q, with iota_k
increasing. Its only inversion is the central pair. Every intermediate
above bottom21 must use that pair and is uniquely
iota_u direct-sum21 direct-sum iota_v, 0<=u<=p,0<=v<=q.
Containment is coordinatewise in (u,v). Its rank polynomial is again a
product of two chain polynomials, hence log-concave for all p,q.

The subsets of the fixed top representing that intermediate have exact
cardinality binom(p,u)binom(q,v). At p=q=2 the actual interval
[21,124356] has rank row [1,2,3,2,1], whereas its occurrence cube has
[1,4,6,4,1]. The rank-two fibers at (u,v)=(0,2),(1,1),(2,0) have
sizes1,4,1. Thus uniform division of Boolean ranks or a descent of
Boolean chains that ignores these fibers cannot prove the general
interval result. The successful grid proof uses their actual pattern
parameters instead. General permutations need not have that grid model.
