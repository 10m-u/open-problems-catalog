# Q4396: coefficientwise connectivity correlation for cactus graphs

Partial theorem; independent review pending. For every finite cactus graph,
the polynomial Z_ab,cd Z-Z_ab Z_cd has nonnegative monomial coefficients,
for any two terminal pairs (including pairs sharing a vertex). A cactus
graph has every edge in at most one simple cycle. This does not settle the
catalog question for arbitrary graphs. The primary source is
[arXiv:2610.00549v1, Section 6](https://arxiv.org/html/2610.00549v1).
No originality claim is made.

## Forests: an explicit factorization

If either terminal pair has no path in the ambient forest, the defect is
zero. Otherwise let U,V be its two unique paths and S=U intersection V,
W=U symmetric-difference V, O=E minus (U union V). Direct factorization gives

    defect = product_(e in W) z_e(1+z_e)
             product_(e in O) (1+z_e)^2
             product_(e in S) z_e
             [product_(e in S)(1+z_e)-product_(e in S)z_e].

The bracket has nonnegative coefficients (its highest monomial cancels).
Empty S gives a zero bracket, as expected for independent disjoint paths.

## A single cycle, with arbitrary terminal pairs

If both pairs coincide, Z_ab,cd=Z_ab=Z_cd=A, and the defect A(Z-A)
has nonnegative coefficients by its event/complement sums. If one pair
has equal endpoints its event is certain and the defect is zero.
It remains to consider three or four distinct marked vertices on a cycle.
Divide the cycle into the three or four arcs between consecutive marked
vertices. For arc i put

    D_i=product_(e in arc i) z_e,
    C_i=product_(e in arc i)(1+z_e)-D_i.

C_i is its polynomial for incomplete arc configurations; D_i is its
complete-arc weight. Both are coefficientwise nonnegative. All configurations
are forests except the fully occupied cycle. Connectivity between marked
vertices depends exactly on which arcs are complete. Consequently, with
t_i=D_i/C_i, all four partition functions equal product C_i times their
counterparts on the triangle or four-cycle. This is an identity of rational
functions, hence of polynomials after clearing denominators.

The triangle case with pairs (0,1),(0,2), and both four-cycle pair patterns
(adjacent or alternating pairs) have coefficientwise nonnegative defects,
as directly enumerated in check_routes.py. These are finite base identities,
not a check over larger cycle lengths. Each base polynomial has degree at
most two in each edge variable, because it is a difference of products of
multiaffine forest sums. Thus substituting a monomial product t_i^e_i and
multiplying by product C_i^2 gives

    product_i D_i^e_i C_i^(2-e_i),  0<=e_i<=2,

which has nonnegative coefficients. This proves the assertion for cycles
of every length, regardless of the number of edges in the arcs.

## Cactus block factorization

The blocks of a cactus graph are bridges and simple cycles. Their edge
sets are disjoint. A configuration is a forest precisely when its
restriction to every cycle block is incomplete, so its partition function
factors over blocks. For a terminal pair, the unique route in the block-cut
tree prescribes a connection between two vertices in every traversed block.
Blocks outside that route impose no condition. Therefore write global
partition functions as products of local Z_i,A_i,B_i,J_i, where inactive
local events have A_i=Z_i or B_i=Z_i. The block-cut tree also shows that
the simultaneous global event is exactly the product of the simultaneous
local events. This remains true when terminal routes share bridges or
cutvertices. Disconnected terminal pairs give a zero defect separately.

Every bridge has nonnegative local defect: if both pairs use it the defect
is z(1+z)-z^2=z; otherwise it is zero. Every cycle block has the proved
nonnegative local defect, including shared-entry terminal pairs. Finally

    global defect = product_i(J_i Z_i)-product_i(A_i B_i)

is nonnegative coefficientwise by telescoping the product difference, since
J_i Z_i-A_i B_i and every factor are nonnegative coefficientwise. This
establishes the all-size cactus theorem.

## Exact bounded arbitrary-graph control

check_forests.py directly sums ordered forest pairs in K_4,K_5,K_6 using
ternary edge-exponent encodings. No negative coefficient occurs: the K_6
control has 2932 forests, 9,266,444 contributing ordered-pair terms and
120,622 nonzero coefficients. Deleting edge variables proves the same
statement for every simple graph on at most six vertices and every four
distinct terminals (complete-graph relabeling is symmetric). These bounded
controls do not prove the arbitrary-graph statement or the cactus theorem;
the latter follows from the displayed block identities.
