# Independent Q2400 proof and count review

Reviewed on 2026-10-13 by the same retained subagent. I accept the five
specified full-target failed routes and the stated all-size partials.
The catalog conjecture remains unresolved; none of these obstructions
is a counterexample to its unweighted probability limit.

The frozen target and [Heilman's journal Question 8.1](https://onlinelibrary.wiley.com/doi/full/10.1002/jgt.23225)
concern the complete independent-set row of G(n,d/n), for sufficiently
large **fixed** d, with probability tending to one. This is distinct
from the regular-graph question. I read the original question, the three
proof/attempt packets, implementations and receipts. Finite controls
support exact witnesses; the arguments below supply the unbounded scope.

## Second-order prefix

The inclusion--exclusion bounds in [BONFERRONI-PREFIX](BONFERRONI-PREFIX.md)
correctly distinguish adjacent edge pairs (three union vertices) from
disjoint pairs (four). The conditions at k+1 imply all relevant lower
bounds L are at least 1/2, so squaring them is legitimate. Writing
a=m/[n(n-1)], direct expansion gives

    L_k²-L_(k-1)L_(k+1)=2a L_k+4a² k(k-1).

The binomial ratio has deficit (n+1)/[(k+1)(n-k+1)] at least 1/(k+1).
The resulting error 2v+v² is dominated by the displayed positive
binomial margin when v<=1/[12(k+1)]. All inequalities have the required
direction; nonnegative bounds permit multiplication and squaring.

For fixed d>0, the edge Chernoff threshold dn is at least twice its mean,
and the wedge expectation and Markov bound require no independence of
wedges. The falling-factorial estimates hold for n>=6. On their joint
event the bound on nu is sufficient, with L=floor[(n²/(384d²))^(1/5)],
to make 12l nu_l<=1/2 for l<=L under the stated size conditions. These
conditions eventually hold for every fixed d>0. Thus the simultaneous
n^(2/5) prefix and its failure probability are proved at the claimed
scope. The weaker probability tail than the older n^(1/3) result is
explicitly retained. At linear k, the lower bound becomes negative;
using its square then would be invalid. No complete-row conclusion is
implied by this proof.

## Isolated-component and certificate obstructions

In [ISOLATED-TREES](ISOLATED-TREES.md), injections modulo automorphisms
count distinct specified component events exactly. Each has h-1 present
edges and B=h(n-h)+binom(h,2)-(h-1) absent edges. Different overlapping
events are incompatible; disjoint events share h² absent cross edges.
Their covariance factor is therefore q^(-h²)-1. The variance bound and
Chebyshev inequality prove the stated O_(T,d)(1/n) failure probability.
As a further exact check, the second moment is

    E X_T²=E X_T+(n)_(2h)/A² * p^(2h-2) q^(2B-h²),

where the second term is zero if n<2h. No estimate uniform in growing d
is supplied or needed.

The claw's discriminant is -31, and multiplication by other component
polynomials cannot remove its nonreal roots. The support-exchange
failure instead concerns two legal independent sets on an induced path;
the slack variable creates no additional deficient exchange coordinate.
The weighted claw has defect 3²-13=-4, which persists when all other
vertices receive sufficiently small positive weights. These are exact
failures of stronger root/support/weight certificates, while the
unweighted claw is log-concave.

The rebuilt 26-vertex tree agrees with the already published tree of
[Kadrawi--Levit, Section 2](https://arxiv.org/html/2305.01784).
Branch counting and a separate included/excluded tree recursion yield
the stated row, tail defect -378 and automorphism count 6912. Applying
the fixed-tree second moment proves that requiring **every** component
to be log-concave is asymptotically false. A bad factor can be compensated
by convolution; this does not refute the full random-graph conjecture.

## Attempt dispositions

| Route | Independent disposition |
|---|---|
| A1 | Accept one worked full-target failure: exact second-order correlation proof produces a larger growing prefix, but its developed truncation fails at linear indices. It is not the old union-bound prefix replay. |
| A2 | Accept: actual asymptotic obstruction to a real-rootedness strengthening, using isolated claws. |
| A3 | Accept: actual support and all-weight obstructions to a multivariate strengthening. It shares the claw with A2, but the attempted theorem and its failure condition are distinct. |
| A4 | Accept one bounded actual complete-row construction attempt. All 144 fresh samples pass; this proves no probability limit and is not counted once per sample. |
| A5 | Accept: a developed componentwise coefficient reduction fails with high probability. The published tree calibration alone counts zero; its isolated-component probability application supplies the new attempted reduction. Root and weight conditions of A2/A3 are not required here. |

All five are substantive failed **sufficient routes** or constructions,
not five impossibility results for Q2400. Their overlaps are disclosed.
No sixth solving route is needed under the user's stopping rule.

## Independent finite receipt

[check_graph_review.py](check_graph_review.py) and
[GRAPH-REVIEW-CHECK.json](GRAPH-REVIEW-CHECK.json) pass. The checker does
not import the root implementation. Its minimum-element decomposition
recomputes all 144 full rows, versus the root's deletion/closed-neighborhood
recursion. It also checks all 1,024 five-vertex graphs by literal subsets,
651 sufficient-criterion indices, 4,096 curvature identities, and exact
claw expectations/second moments over all 1,024 five-vertex and 32,768
six-vertex graphs at p=1/4. The 26-vertex tree row and automorphism count
come from rooted-type recursion. The receipt hashes the reviewed inputs
and own checker; these bounded controls complement the analytical review.
