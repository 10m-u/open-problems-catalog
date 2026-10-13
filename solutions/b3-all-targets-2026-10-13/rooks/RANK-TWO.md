# Every non-nesting rook polynomial of degree at most two is real rooted

Partial theorem for Q183; independent review pending. It applies to every
finite board, without assuming a skew shape or forbidden-pattern condition.
No originality claim is made.

Let N be the number of cells. Form the graph whose vertices are cells and
whose edges join compatible pairs of rooks: two distinct rows and columns
with the columns decreasing as the row increases. Every clique is exactly
a non-nesting rook placement, since compatibility is pairwise. If no
placement has three rooks this graph is triangle free. The number of its
edges is r_2, and r_1=N. Mantel's bound gives r_2<=N^2/4, proving that
1+Nt+r_2 t^2 has nonnegative discriminant and all roots negative (with
the linear and constant degeneracies interpreted separately).

For completeness the required bound has a short elementary proof. If
uv is an edge in a triangle-free graph then d(u)+d(v)<=N, because their
neighbor sets are disjoint. Sum this over edges to get

    sum_v d(v)^2 <= N r_2.

Cauchy gives sum_v d(v)^2 >= (2r_2)^2/N. If r_2>0, division yields
r_2<=N^2/4. If r_2=0 the assertion is immediate. This proves the full
statement for all board sizes at rank at most two.

At degree three and beyond, pair counts and extremal clique bounds alone
do not supply signs at every critical point or total positivity of the
coefficient Toeplitz matrix. No higher-rank induction was obtained.
