# Sharp conjectured bound for one-sided wide affine tails

Partial theorem for Q4082; independent review pending. For beta>3 and
lambda>0, let P(X=j)=(1+lambda j)^(-beta)/F for j>=0. If
lambda(beta-1)<=1, then the conjectured sharp inequality holds:

    M(X)^2[1+k Var(X)]<=1,
    k=(beta-2)^2(beta-3)/(beta-1)^3.

No originality claim is made. This does not cover all one-sided slopes,
two-sided affine laws, or every discrete alpha-concave law.

Put x=1/[lambda(beta-1)]>=1, D=(beta-1)/(beta-2), and define the unnormalized
moments F=sum w_j, A=sum j w_j, B=sum j^2 w_j. Gamma integral representation
and Tonelli give

    F >= x+1/2,
    A >= D x^2-1/12,
    B <= 2 (beta-1)^2 x^3/[(beta-2)(beta-3)].

The elementary kernels used are, for u>0,

    1/(e^u-1) >= 1/u-1/2,
    e^-u/(1-e^-u)^2 >= 1/u^2-1/12,
    sum_(j>=1) j^2 e^(-uj) <= 2/u^3.

The first follows from coth(v)>=1/v. For the second, if v=u/2>=sqrt(3)
the right side is nonpositive. For 0<v<sqrt(3), the power series identity

    (sinh(v)/v)^2=sum_(j>=0) 2^(2j+1) v^(2j)/(2j+2)!

has coefficients 1,1/3, then successive coefficient ratios at most 1/3.
Thus (sinh(v)/v)^2<=1/(1-v^2/3), which rearranges to the second kernel bound.
For the third, the source proves cosh(v)/(sinh(v)/v)^3<=1 (Lazarevic's
inequality); a direct proof is to differentiate
3 log(sinh(v)/v)-log(cosh(v)). After multiplication by v sinh(v)cosh(v),
the numerator is 3v+2v sinh(v)^2-3sinh(v)cosh(v). Its derivative is
4sinh(v)[v cosh(v)-sinh(v)]>=0, and it vanishes at zero. The logarithmic
difference is therefore nonnegative. These proofs cover all u>0.

Since M=1/F and Var=B/F-A^2/F^2, the desired inequality is exactly

    L=F^4-F^2-k B F+k A^2>=0.

The moment bounds give kB<=2x^3/D. The function
F^4-F^2-(2/D)x^3 F is increasing for F>=x+1/2: its derivative is at least

    (4-2/D)x^3+6x^2+x-1/2>0,

because 1<D<2 and x>=1. The lower bound for A is positive here. Hence

    L >= (x+1/2)^4-(x+1/2)^2
         -(2/D)x^3(x+1/2)+k(Dx^2-1/12)^2.

The fourth-degree coefficient cancels. The resulting cubic is

    [beta/(beta-1)]x^3
    +[1/2-kD/6]x^2-x/2-3/16+k/144.

We have beta/(beta-1)>1 and 0<kD<1. It is therefore at least
x^3+x^2/3-x/2-3/16. This polynomial is positive at x=1 (31/48) and
strictly increasing for x>=1. This proves the proposed bound in the
stated wide-tail parameter region. The regime lambda(beta-1)>1 remains.
