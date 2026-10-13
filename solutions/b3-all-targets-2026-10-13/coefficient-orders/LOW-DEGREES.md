# Integer coefficient orders through degree four

Partial classification for Q167; independent review pending. The full target
asks for every n. This note includes every ordering compatible with ties,
as the frozen catalog statement requires.

Write c_k=e_k(r_1,...,r_n), r_i positive integers. Put r_i=1+s_i, s_i>=0.
Expansion gives

    c_k = sum_(d=0)^k binomial(n-d,k-d)e_d(s).

If i<j and i+j<=n, every coefficient of c_j-c_i in the s variables is
nonnegative. For d<=i this uses
binomial(n-d,j-d)>=binomial(n-d,i-d); the remaining terms are nonnegative.
If i+j<n the constant difference is positive. If i+j=n, the difference
vanishes at s=0 but has strictly positive linear coefficients. Thus for
n>=2, every non-all-unit input has c_i<c_j whenever i<j and i+j<=n.
Also c_0=1<c_k for 1<=k<n, and c_n>=1, with equality only when all r_i=1.

## The extra degree-four obstruction

For positive integer r_i in degree four,

    c_2>=c_3 implies c_4<c_1.

To prove it let u_i=1/r_i. Then c_2/c_4=e_2(u) and c_3/c_4=e_1(u).
If all r_i>=2 then u_i<=1/2 and
2e_2(u)=sum_i u_i sum_(j!=i)u_j <= (3/2)e_1(u), so e_2(u)<e_1(u).
If exactly one r_i=1, take u_1=1 and u_2,u_3,u_4<=1/2. The polynomial
e_2(u)-e_1(u) is increasing in each of u_2,u_3,u_4 because its derivative
is the sum of the other two such variables, and its maximum at (1,1/2,1/2,1/2)
is -1/4. This also contradicts c_2>=c_3. At least two r_i therefore equal 1.
Write the input as (1,1,a,b). Direct calculation gives

    c_2-c_3 = 2-(a-1)(b-1),
    c_4-c_1 = (a-1)(b-1)-3.

The first is nonnegative only if the second is at most -1. This proves the
assertion, including coefficient ties and all-unit inputs.

## Complete lists

These are all possible permutations, in one-line index notation:

| n | Compatible coefficient orders |
|---|---|
| 1 | 01, 10 |
| 2 | 012, 021, 201 |
| 3 | 0123, 0132, 0312, 0321, 3012, 3021 |
| 4 | 01234, 01243, 01423, 04123, 04132, 04312, 40132, 40312 |

For n=2, non-all-unit inputs have c_0<c_1,c_2; comparing the remaining
two coefficients gives the first two orders. All-unit coefficients (1,2,1)
add 201. For n=3, non-all-unit inputs have c_0<c_1<c_2 and c_0<c_3,
so inserting 3 gives 0123,0132,0312. The all-unit vector (1,3,3,1)
allows 0312,0321,3012,3021.

For n=4, every non-all-unit input has c_0<c_1<c_2 and c_1<c_3, and c_4>c_0.
Unimodality orders the right side from 4 towards the mode. If c_2>=c_3,
the extra obstruction forces 04132 (or 04123 at the c_2=c_3 tie).
If c_2<c_3, insert 4 before 1, between 1 and 2, between 2 and 3, or after 3;
these give 04123,01423,01243,01234. The all-unit vector (1,4,6,4,1)
permits 04132,04312,40132,40312. These exhaust the list.

Every order has an exact integer witness in BOUNDED-ORDERS.json. In degree
four the five nonexceptional orders have witnesses (2,3,10,15), (1,2,4,14),
(1,1,2,4), (1,1,2,3), and (1,1,1,1), respectively; the last witness also
realizes the three additional all-unit tie orders. A bounded enumeration
found 14 orders for n=5 and 17 for n=6 but supplies no exhaustion proof
in those degrees. No general classification follows from this note.
