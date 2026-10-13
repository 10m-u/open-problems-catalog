# Q2751: every q-Fibonomial with one parameter four is unimodal

Local partial proof, independent review accepted; no novelty claim. The
frozen question concerns all positive m,n. The cached Küstner thesis,
Chapter4, defines exactly this quotient. [Connelly--Ito--Martinez--
Shevchenko--Yang](https://arxiv.org/html/2605.12822v1), Theorem1.2,
proves min(m,n)<=3; its Section5.1 reports computations for m+n<=20
and m=n<=16. Those results are background, rather than new local proofs.

We prove B_(m,4) unimodal for every m>=1. Symmetry in m,n then extends
the known parameter-three boundary to min(m,n)<=4. This still leaves
the full catalog question unresolved for min(m,n)>=5.

Put A=F_(m+1), B=F_(m+2). Then B>=A, and

    P(q)=B_(m,4)(q)=[A][B][A+B][A+2B]/([2][3]).

The source's tiling theorem proves that this is a nonnegative integer
polynomial. Alternatively its polynomial divisibility follows because
four consecutive Fibonacci indices include an index divisible by3
and an index divisible by4; their Fibonacci values are divisible by2
and3 respectively. If both indices coincide, that value is divisible
by6 and its q-integer contains both required relatively prime
cyclotomic factors [2] and [3]. Divisibility follows in either case.
The quotient of reciprocal polynomials is reciprocal, of degree

    D=(A-1)+(B-1)+(A+B-1)+(A+2B-1)-1-2
      =3A+4B-7.

It suffices to prove its coefficient differences d_i>=0 for0<=i<=floor(D/2).

## Exact difference identity

Let p(s)=0 for s<0, and for s>=0 let p(s) count solutions
x+2y+3z=s with nonnegative integers x,y,z. Direct summation over z gives

    p(s)=floor((s^2+6s+12)/12).

For completeness, writing s=6t+r,0<=r<=5, the same sum is
3t^2+(r+3)t+p(r), with p(0),...,p(5)=(1,1,2,3,4,5).
Thus if Q(s)=(s^2+6s+12)/12, then

    0<=Q(s)-p(s)<=7/12.

Its six errors are 0,7/12,1/3,1/4,1/3,7/12.

The numerator of (1-q)P, over denominator
(1-q)(1-q^2)(1-q^3), expands to

    1-q^A-q^B+q^(2A+B)+q^(A+3B)
      -q^(3A+3B)-q^(2A+4B)+q^(3A+4B).

Since B>=A and i<=D/2, all terms of exponent at least A+3B
lie beyond the range in question. Hence exactly

    d_i=p(i)-p(i-A)-p(i-B)+p(i-2A-B).             (1)

## All m>=7

Here A>=21. For i<A, (1) is p(i)>=0. For A<=i<B, it is
p(i)-p(i-A)>=0, since p is nondecreasing (add one to x).

For B<=i<2A+B, all three displayed arguments are nonnegative.
The corresponding quadratic difference is

    G(i)=[-i^2+2(A+B)i-A^2-B^2+6(A+B-i)-12]/12.

It is concave. On the entire real interval [B,2A+B] its minimum
is the smaller endpoint value

    G(2A+B)=[A(2B-A-6)-12]/12.

Since B>=A>=21, this is at least [A(A-6)-12]/12>=303/12.
The floor errors in p(i)-p(i-A)-p(i-B) can reduce G by at most7/12.
Therefore d_i>0 on this interval, also when the half-degree cutoff
truncates it.

For 2A+B<=i<=D/2, all four arguments in (1) are nonnegative.
Their quadratic difference collapses to

    H(i)=A(3A+4B-6-2i)/12.

The half-degree bound gives H(i)>=A/12. The two positive floor terms
can reduce H by at most7/6, while the two subtracted floor terms
increase it. Consequently

    d_i>=A/12-7/6>=21/12-14/12=7/12>0.

This proves all m>=7. All four intervals, including possible empty
intervals, cover the entire lower half of the coefficient row.

## Six remaining cases

For m=1,...,6, the pairs (A,B) are (1,2),(2,3),(3,5),(5,8),
(8,13),(13,21). Formula (1) gives finitely many exact integer
differences on their respective lower halves; all are nonnegative.
The complete six coefficient arrays and controls are in CHECK.json,
produced by the stdlib checker. Polynomial division is independently
verified by multiplying each quotient back by its divisor. These finite
cases, together with the inequalities above, complete the all-m proof.

The same checker also checks (1) against actual quotient coefficients
for m=1,...,18. This is supporting validation, not the reason the
assertion holds at arbitrary m. The draft's first degree calculation
was corrected by the exact checker before review; that implementation
correction is not a separate research failure.
