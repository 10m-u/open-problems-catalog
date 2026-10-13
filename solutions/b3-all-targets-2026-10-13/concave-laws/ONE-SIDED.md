# Sharp concentration bound for every one-sided affine law

Candidate proof; independent review pending. Write beta>3,
k=(beta-2)^2(beta-3)/(beta-1)^3, and

    w_j=(1+lambda j)^(-beta), j>=0,
    F=sum w_j, A=sum j w_j, B=sum j^2 w_j.

For the normalized one-sided law, M=1/F and Var=B/F-A^2/F^2. We prove

    L=F^4-F^2-kBF+kA^2>=0

for every lambda>0. Put r=lambda(beta-1), u=1/(beta-1) in (0,1/2),
and D=1/(1-u). This proof has three parameter regions, all exact.

## Region 0<r<=1

WIDE-TAIL.md supplies the analytic proof, with x=1/r. Its elementary
Gamma kernel inequalities and the resulting positive cubic cover the
entire region. This is an all-parameter proof, not a sampled screen.

## Region 1<=r<=2

Gamma integration gives the bounds from WIDE-TAIL.md, with a sharper F:

    F >= F_0=1/r+1/2+r(1+u)/12
                -r^3(1+u)(1+2u)(1+3u)/720,
    A >= 1/[(1-u)r^2]-1/12,
    kB <= 2(1-u)/r^3.

To prove the new kernel bound globally, put v=t/2. The assertion

    1/(e^t-1)>=1/t-1/2+t/12-t^3/720

is equivalent to
v cosh(v)-(1+v^2/3-v^4/45)sinh(v)>=0. Its power-series coefficient
at v^(2j+1) is zero for j=0,1,2 and is

    16j(j-1)(j-2)(j+2)/[45(2j+1)!]>0

for j>=3. Hence the inequality holds for all t>0. Integrating against
the Gamma(beta,1) density gives F_0 using its first and third moments.

Here F_0>1: the first two terms are >=1 and the correction is at least
r(1+u)[1/12-20/720]>0. The lower A bound is positive. As a function of
F>=1, F^4-F^2-[2(1-u)/r^3]F is increasing, since its derivative is
at least 2-2(1-u)/r^3>=0. Therefore r^4 L is at least

    P(r,u)=r^4[F_0^4-F_0^2-2(1-u)F_0/r^3
                   +(1-2u)(1/r^2-(1-u)/12)^2].

This is a polynomial. After r=1+z,u=y/2 it has bidegree (16,12).
ONE-SIDED-CERTIFICATE.json gives all 221 rational coefficients in the
Bernstein basis on [0,1]^2. Every coefficient is strictly positive; the
least is 386066666641/268738560000. The Bernstein basis functions are
nonnegative and sum to one, so P>0 throughout this rectangle. The exact
checker reconstructs all 221 power coefficients independently from the
stored Bernstein representation. This finite rational certificate proves
the entire middle parameter region.

## Region r>=2

Let S=F-1 and w_1=(1+lambda)^(-beta). Source Lemma 4.3, equations (13)–(16),
gives the following uniform estimate (its exact integral expression is
retained here, before the source's final coarse bound):

    kB/w_1 <= R(r,u)
      =(1-u)[1+1/r+2/r^2+2/r^3
                    +u(1+1/r+2/r^2)-u^2].

Indeed c=(1-u)(1-2u), k/c=1-u, the source's integral term is
1/r+2/r^2+2/r^3+u(1/r+2/r^2)+u(1-u), and c sup h<=1 when r>=2.
The sum-integral argument and the explicit h maximum are as in that proof.
Define B_0(r)=1+1/r+2/r^2+2/r^3. Exact expansion shows

    R=B_0-2u/r^3-(2+1/r+2/r^2)u^2+u^3<=B_0.

R decreases with r and with u on the stated domain. For u the derivative
is -2/r^3-2(2+1/r+2/r^2)u+3u^2<0. The r derivative is also negative
directly in the first expression for R.

Gamma representation and Jensen applied to the convex function
1/(e^t-1) give F>=1/(1-e^(-r(1+u))). Put
H(q)=(2-q)/(1-q)^2; H is increasing for q in (0,1). Thus
F(F+1)>=H(e^(-r(1+u))). We verify R<=F(F+1) as follows:

* For r>=3, R<=B_0(3)<2<F(F+1).
* For 2<=r<=3 and u>=1/4, R<=R(2,1/4)=129/64.
  Here r(1+u)<=9/2 and e^(9/2)<100, so F(F+1)>H(1/100)>129/64.
* For u<=1/4 and 2<=r<=33/16, use
  e^(165/64)<53/4 and H(4/53)>B_0(2).
* For u<=1/4 and 33/16<=r<=9/4, use
  e^(45/16)<50/3 and H(3/50)>B_0(33/16).
* For u<=1/4 and 9/4<=r<=3, use
  e^(15/4)<43 and H(1/43)>B_0(9/4).

Every exponential upper bound has an exact rational Taylor certificate:
sum through order 40, followed by a geometric bound on the positive
remainder. The other comparisons are rational arithmetic. All are stored
in ONE-SIDED-CERTIFICATE.json and independently reproduced by check_affine.py.

Finally w_1<=S, so kB<=w_1 F(F+1)<=S F(F+1)=F^3-F. Hence
F^4-F^2-kBF>=0 even without the nonnegative term kA^2. This completes
the concentrated region and the full one-sided affine theorem. A vanishing
tail is the limiting point mass F=1,A=B=0 and obeys the same conclusion.

The source estimates are from [arXiv:2610.05439v1](https://arxiv.org/html/2610.05439v1).
They are used here with additional mean subtraction and sharper parameter
comparisons; their original weaker theorem alone does not imply this claim.
