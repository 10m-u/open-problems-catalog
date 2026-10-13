# Complete integer coefficient-order classification in degree five

New partial theorem for Q167; independent review accepted (ROOT-REVIEW.md#rook-and-coefficient-order-final-review). The earlier packet
and catalog already classified n<=4. This note extends that scope to n=5;
it does not classify arbitrary n. All compatible tie orders are included.

Let c_j=e_j(r_1,...,r_5), with positive integer r_i, and put u_i=1/r_i.
The all-unit vector has coefficients (1,5,10,10,5,1). Otherwise the
dominance lemma in LOW-DEGREES.md gives

    c_0<c_1<c_2<c_3, c_1<c_4, c_0<c_5.

Newton inequalities give unimodality, with at most two adjacent equal
maximal coefficients. Three additional implications suffice:

    (I)   c_4<=c_2 implies c_5<c_1;
    (II)  c_4>=c_3 implies c_5>c_1;
    (III) c_3>=c_4 implies c_5<c_2.

## Proof of (I)

The assumption is e_1(u)<=e_3(u). It forces at least three r_i to be one.
If no u_i=1, the identity
3e_3=sum_i u_i e_2(u with i omitted) gives e_3<=e_1/2.
With one u_i=1 and four remaining v_i<=1/2,
e_3-e_1=e_2(v)+e_3(v)-1-e_1(v). This multi-affine expression has maximum
on the cube at a vertex. With j of the four v_i equal to 1/2 it is
binomial(j,2)/4+binomial(j,3)/8-1-j/2, negative for j=0,...,4.
With two u_i=1 and three v_i<=1/2,
e_3-e_1=2e_2(v)+e_3(v)-2<=3/2+1/8-2<0.

Thus write r=(1,1,1,a,b), allowing a or b also to be one. Directly,

    c_4-c_2=2(a-1)(b-1)-5,
    c_5-c_1=(a-1)(b-1)-4.

The integer (a-1)(b-1) is at most two under the assumption, so the
second expression is negative. This proves (I).

## Proof of (II)

Prove its contrapositive. If c_5<=c_1 and there are no unit factors,
e_4(u)<=5/16<1; with only one unit, e_4(u)<=1/16+4/8=9/16<1.
But c_1/c_5=e_4(u), so both cases are impossible.
With exactly two unit factors write r=(1,1,a,b,c), a,b,c>=2.
The function abc-a-b-c-2 is increasing in each variable, has minimum
zero at (2,2,2), and thus c_5<=c_1 forces that triple. At this vector
e_2(u)=19/4>7/2=e_1(u), so c_4<c_3.
With at least three unit factors, r=(1,1,1,a,b), and
c_4-c_3=-1-2(a+b)<0. This includes the cases of four or five units.

## Proof of (III)

The assumption is e_2(u)>=e_1(u). With no unit factor,
2e_2=sum_i u_i sum_(j!=i)u_j<=2e_1, with equality only when all u_i=1/2.
Thus all r_i=2 and e_3(u)=5/4>1.
With one unit, e_2-e_1=e_2(v)-1, and e_3=e_2(v)+e_3(v)>1.
With two units, e_2-e_1=S+e_2(v)-1, whereas
e_3=S+2e_2(v)+e_3(v)>1. With three or more units, e_3>1 directly
(three unit variables give one, and the other positive variables add terms).
Consequently c_2/c_5=e_3(u)>1 in every case.

## Exhaustion and witnesses

For non-unit inputs, if c_4>=c_3, unimodality and (II) insert index 5
into the chain 0,1,2,3,4 after index 1, giving
015234,012534,012354,012345. If c_4<=c_3, unimodality orders
c_5<=c_4<=c_3; (III) forces c_5<c_2. If c_4<=c_2, (I) forces c_5<c_1.
The resulting orders are 051423,051243,015243. Adjacent equality can
choose either of the bordering cases just listed; it adds no new order.

All-unit input additionally permits independent exchanges of the pairs
(0,5),(1,4),(2,3). Combining the seven non-unit orders with these eight,
and removing the common 051423, gives exactly fourteen orders:

    012345 012354 012534 015234 015243 051243 051423
    051432 054123 054132 501423 501432 504123 504132.

Every order has an exact witness in BOUNDED-ORDERS.json. The analytic
exhaustion above proves completeness beyond the bounded enumeration.
check_orders.py replays witnesses and exact controls of the three lemmas;
the finite checks accompany, rather than replace, these proofs.
