# Boundary inequalities and normalization obstructions for subsums

13 October 2026. These are partial results for Q3702 and Q3703, which
remain open at their full scopes. No publication-priority claim is made.
I read the definitions and Conjectures 4 and 7 in
[Reciprocals of subsum polynomials](https://link.springer.com/article/10.1007/s11139-026-01419-0).
The first-three binary coefficient identities and symmetry already appear
in its Proposition 4.1. The inequalities, variance comparison and limiting
argument below are supplied here. Exact independent expansions are in
[check_boundaries.py](check_boundaries.py) and [BOUNDARY-CHECK.json](BOUNDARY-CHECK.json).

## Q3702: the first two inequalities

Let F_n be the product in Q3702 and L=floor(log_2 n)+1. Its constant
coefficient is one, and its first three other coefficients are

    c1=L,
    c2=binom(L,2)+(L-1),                         n>=2,
    c3=binom(L,3)+L(L-1)+m3,
    m3=floor(log_2(n/3))+1 if n>=3, otherwise 0.

This simply selects parts of sizes one, two and three from the product.
Every factor is palindromic, so the same inequalities hold at the other end.
The first defect is

    c1^2-c0*c2=(L^2-L+2)/2>0.

For n>=8 we have L>=4 and m3<=L-1. Hence

    c2=(L-1)(L+2)/2,
    c3<=(L-1)(L^2+4L+6)/6,
    c2^2-c1*c3 >= (L-1)(L+1)(L^2-12)/12>0.

Thus both the first and second nontrivial log-concavity inequalities,
and their reflected counterparts, hold strictly for every n>=8.
For n=1,2,4 the applicable inequalities can be read from their finite
products. The other four small n are excluded by the catalog statement.
An arbitrary interior coefficient is not covered.

## Q3703: strict first and last inequalities at every n>=4

Let H_n be the binary-partition sum in Q3703, let N=floor(n/2), and write
b(t) for the number of binary partitions of t. Choosing the non-one parts
of a binary partition of n is equivalent to choosing t in 0..N and a
binary partition of t, then doubling all its parts. Consequently

    B:=c0=b(n)=sum_(t=0)^N b(t),
    c1=2 sum_(t=0)^N t*b(t).

For each summand, put e1=n-m_lambda(1) and e2=N-m_lambda(2). Then
0<=e1<=2N, 0<=e2<=N, and its coefficient of x^2 is
binom(e1,2)+e2. Therefore

    c2 <= (N-1/2)c1+N*B.                         (1)

Appending a one injects binary partitions of t into those of t+1.
Thus b is nondecreasing, with b(0)=b(1)=1 and b(2)=2.
For a fixed N>=2, decompose its weights as

    b(t)=1+1_(t>=2)+sum_(j=3)^N [b(j)-b(j-1)]1_(t>=j).

The first two terms have total mass 2N and mean of 2t equal to
N+1-1/N. Every further nonnegative step has mean N+j>=N+3.
Adding these steps cannot decrease that initial mean. Hence, with u=c1/B,

    u>=N+1-1/N>=N+1/2.

Use (1) to obtain

    c1^2-B*c2 >= B^2[u^2-(N-1/2)u-N] >= B^2/2>0.

The last inequality follows by evaluating the increasing quadratic at
u=N+1/2. Every summand is palindromic of the same degree
d=sum_(j>=1)2^j floor(n/2^j), so H_n is palindromic. The final inequality
is equally strict. This proves two boundary inequalities for every n>=4,
including all n in the full conjecture, but leaves the interior open.

## Q3703: ultra-log-concavity fails at every power of two n>=4

This is a stronger-property obstruction, not a disproof of Q3703.
Normalize the coefficients of H_n to a probability distribution X.
Choose a partition lambda with probability proportional to 2^(-length(lambda)),
then independently select each of the e_j=floor(n/2^j)-m_lambda(2^j)
available parts of size 2^j with probability one half. This is exactly X,
because a summand evaluates at one to 2^(sum e_j), and the first term in
sum e_j is independent of lambda. All conditional means are d/2. Thus

    Var(X)=(S_n-E_weighted sum_(parts p in lambda) p^2)/4,
    S_n=sum_(j>=0)4^j floor(n/2^j).                (2)

If n=2^s, then S_n=2n^2-n and sum p^2<=n^2, so

    Var(X)>=(n^2-n)/4.

A symmetric ultra-log-concave distribution with positive coefficients
throughout 0..d has variance at most d/4. Here is a proof of that fact,
to fix the normalization. Divide
its probability masses by the Binomial(d,1/2) masses. Symmetry and
log-concavity make the positive ratios nonincreasing with distance from
d/2. The squared distance is nondecreasing with that distance. Their
covariance under the binomial distribution is nonpositive, as follows
by expanding it into one half the average of
(ratio_i-ratio_j)(distance_i^2-distance_j^2). Since the ratio has mean
one, the tilted variance is at most the binomial variance d/4.

The full-support condition holds here: the partition lambda=(n) contributes
product_(j=0)^(s-1)(1+x^(2^j))^(2^(s-j)). Its first factor covers 0..n;
each successive step size is at most one plus the accumulated degree,
so its positive support remains a full interval through degree s*n.
For H_(2^s), d=s*n and n-1>s at every s>=2. Its lower variance bound
therefore exceeds d/4. Consequently H_(2^s) is not ultra-log-concave
for any s>=2. In particular a Lorentzian homogenization demanding that
stronger property cannot prove the ordinary log-concavity conjecture.

## Q3702: a central normal limit

Normalize F_n's coefficients at x=1. They are the distribution of
Y_n=sum_(i=1)^n i*sum_(h=1)^(m_i) B_(i,h), with independent fair
Bernoulli variables and m_i=floor(log_2(n/i))+1. Exactly,

    E Y_n=deg(F_n)/2,
    sigma_n^2=Var(Y_n)=sum_i m_i*i^2/4.

The identities

    sum_i m_i*i^q = sum_(j>=0) sum_(i=1)^(floor(n/2^j)) i^q

give deg(F_n)~2n^2/3 and sigma_n^2~2n^3/21. Summing the ordinary
power-sum error bounds over j proves these asymptotics: their errors
are O(n) for q=1 and O(n^2) for q=2, while the main geometric series
have ratios 1/4 and 1/8, respectively.

For fixed real t the centered, standardized characteristic function is

    phi_n(t)=product_i cos(i*t/(2*sigma_n))^m_i.

Its largest cosine argument is O_t(n^(-1/2)). Taylor expansion of log cos
therefore gives

    log phi_n(t)=-t^2/2+O_t(sum_i m_i*i^4/sigma_n^4)
               =-t^2/2+O_t(1/n),

because sum m_i*i^4<=n^2 sum m_i*i^2 and sigma_n^2 is of order n^3.
The continuity theorem proves convergence to the standard normal law.
This is an all-size asymptotic distribution theorem. It does not control
the sign of an exact adjacent-coefficient defect. Normal convergence is
compatible with small local violations, and the tails are outside this
central limiting argument.
