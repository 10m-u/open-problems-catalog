# Q3498: exact crown transfer and bounded root certificates

The full arbitrary-n real-rootedness question remains unresolved. We read
the actual [Lundström--Saud Maia Leite v5](https://arxiv.org/html/2504.05123v5),
Sections4--6, retaining the distinction between the face polynomial and
the Ehrhart h* polynomial. The source proves gamma nonnegativity and
retains Conjecture5.18; its displayed small cases reach n=6. No novelty
or external review claim is made for this local work.

## An all-n exact transfer formula

For m>=0, put k=m+1 and T_k=(min(i,j))_(1<=i,j<=k). Assigning
values0,...,m to the minimal elements a_i of the crown leaves
m+1-max(a_i,a_(i+1)) choices for b_i. Summing the cyclic product
is therefore

    E_(C_(2n))(m)=trace(T_k^n).                         (1)

Reversing the indexing turns the max kernel into the min kernel above.
This works for every n>=2, including the four-element crown.

For a principal minor on i_1<...<i_j, its determinant is
i_1(i_2-i_1)...(i_j-i_(j-1)), by successive row differences.
The elementary symmetric functions of the eigenvalues are thus

    e_j(T_k)=binom(k+j,2j), 0<=j<=k.                    (2)

Indeed, sum over positive gaps of total at most k with weight their
product. Its generating function in k is z^j/(1-z)^(2j+1), giving
the claimed binomial coefficient. Newton identities now give an exact
integer algorithm for (1) without enumerating linear extensions or
forming matrix powers. The code then applies the defining Ehrhart
transform using dimension2n.

## Exact bounded root checks

For every n=2,...,20 the computed h* is reciprocal of degree2n-2.
Extract gamma from

    h*(t)=(1+t)^(2n-2) gamma(t/(1+t)^2).

Exact rational Sturm counting gives deg(gamma) negative real roots
for each of these19 cases; hence all h* roots are negative and real.
For z<0, the equation t/(1+t)^2=z has two real negative reciprocal
solutions because its discriminant is1-4z>0. Any unused degree in
gamma adds factors1+t. In particular n=2 has gamma=1 and h*=(1+t)^2.
These are exact bounded certificates, not an induction in n.

The complete integer arrays and counts are CROWN-EXPLORATION.json.
The first four displayed source arrays agree; the n=5 row is reconstructed
from the defining counts, avoiding the duplicated entries in the PDF table.
The descent-top refinement of actual linear extensions is also checked
against the complete h* row at n=3, supplying an independent small control.

## Useful method obstructions

The first-order palindromic Eulerian recurrence described in CROWN-ATTEMPTS
already fails between n=3 and4. An actual descent-top multivariate
refinement at n=3 also fails real stability, despite its real-rooted
diagonal. These facts leave the univariate target open.
