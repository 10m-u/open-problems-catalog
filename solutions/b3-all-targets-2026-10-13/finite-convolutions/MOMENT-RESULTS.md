# Finite free commutators through degree five

Partial theorem for Q3436; independent review pending. No claim of originality.
Definitions are Notation 3.7 and 5.1 in Campbell–Morales–Perales,
[SIGMA 21 (2025), 108](https://sigma-journal.com/2025/108/sigma25-108.pdf).
The conjecture concerns all degrees, not merely these cases.

Let the real roots of p be a_i and put

    S_A = sum_i (a_i - mean(a))^2,
    T_A = sum_i (a_i - mean(a))^4,

with S_B,T_B defined from q. Translation does not change Sym(p).
Write Sym(p)=p boxplus_n Dil_{-1}(p). Its odd elementary coefficients vanish.
Finite additive convolution and Newton's identities give

    e_2(Sym(p)) = -S_A,
    E_A := e_4(Sym(p))
        = (n^2-3n+3) S_A^2 / (2n(n-1)) - T_A/2.

The second formula is used only for n>=4. Indeed, for centered p,
e_2(p)=-S_A/2, e_4(p)=S_A^2/8-T_A/4, and

    e_4(Sym(p)) = 2e_4(p)
        + (n-2)(n-3)e_2(p)^2/[n(n-1)].

Sym(p) is even and real rooted by ordinary finite additive convolution.
Consequently E_A>=0; the same holds for E_B. The defining triple finite
multiplicative convolution with z_n gives

    p square_n q = x^n - c_2 x^(n-2) + c_4 x^(n-4) - ...,
    c_2 = n S_A S_B/(n^2-1),
    c_4 = e_4(z_n) E_A E_B / binomial(n,4)^2.

For n=1 the polynomial is x. For n=2,3 it is
x^(n-2)(x^2-c_2), so its roots are real.

For n=4, Cauchy gives T_A>=S_A^2/4, hence
0<=E_A<=S_A^2/6. Here e_4(z_4)=3/5, and therefore

    c_2^2 - 4c_4 >= S_A^2 S_B^2/225 >= 0.

The quadratic y^2-c_2 y+c_4 has nonnegative real roots: its sum and product
are nonnegative and its discriminant is nonnegative. Substituting y=x^2
proves the assertion in degree four, including constant-spectrum cases.

## Sharp fourth moment for five centered real numbers

If sum_i a_i=0 for five real numbers, then

    sum_i a_i^4 >= (7/30)(sum_i a_i^2)^2.

For a nonzero vector normalize sum a_i^2=1 and minimize sum a_i^4 on
the compact constrained sphere. The constraint gradients are independent.
Lagrange multipliers imply that every coordinate is a root of
4t^3-2lambda t-mu=0. Multiplying the critical equations by a_i and summing
gives lambda=2 sum a_i^4>0.

There are at most three distinct coordinate values. If there are three,
write x<y<z. Since the cubic has no quadratic term, x+y+z=0. At its middle
root, the Hessian entry is

    12y^2-2lambda = 4(y-x)(y-z)<0.

If y occurred twice, the vector with entries +1,-1 at those two equal
coordinates would be tangent to both constraints and give negative second
variation, contradicting a minimum. Thus y occurs once. The outer
multiplicities add to four. Multiplicities (1,1,3) would force z=0 by
subtracting x+y+z=0 from x+y+3z=0, contradicting the weighted zero sum;
(3,1,1) is excluded similarly. The remaining (2,1,2) forces y=0 and z=-x,
giving fourth-moment ratio 1/4.

With two distinct values of multiplicities a and 5-a, the zero-sum
constraint gives the ratio

    (25-15a+3a^2) / [5a(5-a)].

It equals 13/20 for a=1,4 and 7/30 for a=2,3. One distinct value cannot
have both zero sum and unit second moment. These exhaust all minima and
prove the bound, with equality at a two-value vector of multiplicities 2,3.

For n=5 the bound gives 0<=E_A<=5 S_A^2/24, and likewise for B.
Here e_4(z_5)/binomial(5,4)^2=2/9, so

    c_2^2 - 4c_4 >= 25 S_A^2 S_B^2/5184 >= 0.

The same nonnegative quadratic argument proves real rootedness of
x(x^4-c_2 x^2+c_4). Thus Q3436 holds for every Hermitian input in degrees
1 through 5. The all-degree target still needs control of every higher
coefficient and the corresponding half-polynomial roots.

## Rank one modulo scalars in arbitrary degree

If A=lambda I+u vv* with ||v||=1, every actual commutator has rank at most
two and trace zero. Its characteristic polynomial is
x^(n-2)(x^2-w(U)) with w(U)>=0. Taking expectation preserves this form,
and E w(U)=c_2=u^2 S_B/(n+1). This proves real rootedness for this class
in every n>=2. This is a direct special-case derivation, not an extension
to arbitrary spectra or a closure of Q3436.
