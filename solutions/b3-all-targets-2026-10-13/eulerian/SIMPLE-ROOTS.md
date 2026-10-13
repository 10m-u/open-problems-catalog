# Simple roots and sharp s-Eulerian representation length

13 October 2026. Internally reviewed all-size solutions of the broader B3C-Q07 and
B3C-Q06. These are separate from the full coloured classification in Q1262.
The argument uses the published weak interlacing theorem and adds an explicit
strictness argument. The retained subagent's [independent review](../stirling/EULERIAN-REVIEW.md)
and the [root review](../ROOT-REVIEW.md#eulerian) accept these scopes; no priority claim is made.

## Definitions and published input

For a positive integer vector s=(s_1,...,s_N), let

    E_s(x)=sum_(0<=e_i<s_i) x^(asc(e)),

where asc counts e_i/s_i<e_(i+1)/s_(i+1), with e_0=0 and s_0=1.
Let f_i(x) refine E_s by the final numerator e_N=i. Appending a denominator
b gives refined polynomials

    g_j(x)=x sum_(i<t_j) f_i(x)+sum_(i>=t_j) f_i(x),
    t_j=ceil(j*a/b), 0<=j<b, a=s_N.

Savage–Visontai, [The s-Eulerian polynomials have only real roots](https://arxiv.org/pdf/1208.3831),
Lemma 2.1, Theorem 2.3 and Lemma 2.5, imply that f_i interlaces f_j
for i<j, in the orientation deg f_i<=deg f_j<=deg f_i+1 and
...<=root_2(f_i)<=root_2(f_j)<=root_1(f_i)<=root_1(f_j).
Theorem 2.7 says E_s interlaces E_(s,b). These are weak interlacings;
neither theorem alone gives simplicity. All refined polynomials have
nonnegative coefficients and positive leading coefficient. Also f_0=E_(s_1,...,s_(N-1)).

## Two interlacing observations

Suppose f_0,...,f_(a-1) have the orientation above. At a real point z where
a selected f_i is nonzero, its sign is (-1)^(number of roots greater than z),
because its leading coefficient is positive. For i<j with both nonzero,
interlacing makes those root counts nondecreasing with difference at most one.
Consequently the nonzero values f_i(z) have at most one sign change in their
index order.

If z is a root of the last polynomial f_(a-1), every nonzero earlier f_i(z)
has the same sign. Indeed, for a simple k-th largest root z of the last
polynomial, interlacing locates exactly k-1 roots of every nonzero f_i to its
right. If that last root is repeated, every interlacing f_i vanishes at z
between two equal consecutive roots. Thus a positive sum of the f_i can
vanish at a root of the last one only if every f_i vanishes there.

It follows that if F=sum_i f_i has F(z)=0 and f_0(z)!=0, then the last
value is nonzero and has the opposite sign from f_0(z). If sigma is the
sign of f_0(z), every proper prefix sum

    P_i(z)=sum_(h=0)^i f_h(z), 0<=i<a-1,

has strict sign sigma. Before the single sign change it is a positive sum
after multiplication by sigma; after the change it equals the negative of
the remaining tail, which includes the strictly opposite last value.

## Strict interlacing for nonunit vectors

**Theorem.** If all entries of s are at least two, E_s has simple strictly
negative roots. Consecutive prefix polynomials have no common root and
strictly interlace wherever their weak interlacing has a root comparison.

Proof by prefix induction. E_empty=1 and E_(a)=1+(a-1)x for a>=2, so the
base case is immediate. Suppose E_s has simple negative roots and shares no
root with its preceding prefix polynomial f_0. Consider a root z<0 of E_s.
The previous observations give strictly signed proper prefix sums P_i(z).

Summing the appended refinements counts each f_i with coefficient

    w_i(x)=b+(x-1)k_i,
    k_i=#{j in {0,...,b-1}: ceil(j*a/b)>i}
       =b-1-floor(i*b/a).

At z<0, the w_i(z) are nondecreasing, and

    w_(a-1)(z)-w_0(z)=(1-z)floor((a-1)b/a)>0

when a,b>=2. Since sum_i f_i(z)=0, summation by parts gives

    E_(s,b)(z)=-sum_(i=0)^(a-2) [w_(i+1)(z)-w_i(z)] P_i(z).

All nonzero summands have the same strict sign, and at least one exists.
Thus E_(s,b)(z)!=0: no old root is shared. The published weak interlacing
now forces the new roots to be simple. A repeated new root would place an
old root between its two equal copies, which would be a shared root.
Every new root is negative because E_(s,b) has nonnegative coefficients
and constant term one. This completes the induction. In particular the
argument covers nonmonotone denominator vectors and degree-preserving steps;
it assumes neither strictly increasing denominators nor distinct refinements.

## Sharp representation length

**Corollary.** For integers d,u>=1, the shortest positive integer vector s
with E_s(x)=(1+u*x)^d has length exactly 2d-1.

Delete leading and trailing unit entries and merge adjacent units. A remaining
unit entry separates independent ascent statistics:

    E_(s,1,t)=E_s E_t.

The canonical vector therefore consists of nonempty nonunit blocks, separated
by single units. Every block polynomial has constant term one, positive
degree and, by the theorem, simple negative roots. Its factors must divide
(1+u*x)^d, so each block has degree exactly one and equals 1+u*x. There must
be d blocks. The vector has at least d nonunit entries and d-1 separators,
giving length at least 2d-1; deleting entries only shortened the original.
Conversely (u+1,1,u+1,...,1,u+1), with d nonunit entries, realizes the
polynomial and attains that length.

This supplies the missing lower bound for the previously proved universal
representation upper bound. It does not characterize all coloured multiset
Eulerian polynomials or assert that every representing vector is canonical.
No old missing proof or certificate is recovered by this new argument.
