# Exact partial results for percolation with constant freezing

Catalog IDs: Q276 and Q277. Date: 2026-10-09.

## 1. Statements and scope

Let `G=(V,E)` be a finite simple graph. Initially every vertex is warm and every
edge is closed. A closed edge with two warm endpoints opens at rate one. Each
warm open-edge component freezes at rate `a>0`, independently of its size; its
vertices then stay frozen. Let `mu[G,a]` denote the law of the final set of open
edges. This is the model in Mottram's Definition 2.1 and the two questions in
his Section 1.4, [S1].

An event is increasing if it is preserved when edges are added. Q276 asks
whether `mu[G,b](A) <= mu[G,a](A)` always holds for `0<a<b` and increasing `A`.
Q277 asks whether `mu[G,a](A intersect B) >= mu[G,a](A) mu[G,a](B)` always holds
for increasing `A,B`.

**Theorem 1 (Q276, restricted graph class).** If each connected component of a
finite simple graph `G` has at most five edges, then Q276 holds for `G`, for all
positive real freezing rates.

**Theorem 2 (Q277, restricted graph class).** If each connected component of a
finite simple graph `G` has at most four edges, then Q277 holds for `G`, for all
positive real freezing rates.

The proof consists of exact polynomial identities and nonnegativity checks on
a completely enumerated finite set, followed by a product-measure argument.
Neither theorem resolves its unrestricted catalog question.

## 2. An exact recursion for the final law

Write a state as `(O,W)`, where `O` is the set of open edges and `W` is the set
of warm vertices. Every component of the graph `(V,O)` is either entirely warm
or entirely frozen. Let

```math
E_*(O,W)=\{uv\in E\setminus O:u,v\in W\},\qquad e=|E_*(O,W)|.
```

Call a warm open component relevant if it has an endpoint of at least one
edge in `E_*`, and let `k` be the number of relevant warm components.

**Lemma 3 (deleting irrelevant clocks).** Ignoring the freezing clocks of
irrelevant warm components does not change the final open-edge law.

**Proof.** No closed edge incident to an irrelevant warm component has two
warm endpoints. Every such edge is permanently blocked by a frozen endpoint.
The component therefore can never merge with another warm component or affect
an opening. Its eventual freezing is irrelevant to the final edge set. Deleting
that clock leaves the rates of all relevant transitions unchanged. This is
equivalently the usual removal of events that do not affect an observed
finite-state continuous-time Markov chain. The same reasoning applies after
each state transition. QED.

If `e=0`, the edge set is final. If `e>0`, the next relevant event has total
rate `e+k*a`. Each active edge opens with rate one, and each of the `k` relevant
components freezes with rate `a`. Every such transition reduces `e` strictly.
Opening an edge removes that edge from `E_*`; freezing a relevant component
removes at least one active incident edge and cannot create a new one.

For a final mask `s`, let `P_(O,W),s(a)` be its probability from the current
state. The exact first-step recursion is

```math
P_{(O,W),s}(a)=
\frac{\displaystyle\sum_{f\in E_*}P_{(O\cup\{f\},W),s}(a)
       +a\displaystyle\sum_{C\text{ relevant}}P_{(O,W\setminus C),s}(a)}
     {e+ka}.
```

The boundary condition at `e=0` is `P_(O,W),s=1{O=s}`. Since `e` strictly
decreases, this recursion terminates and has a unique solution. No stationary
distribution approximation or time cutoff is involved.

## 3. A common denominator with integer coefficients

Fix `n=|V|`. Since every relevant component contains an endpoint of an active
edge,

```math
1\le k\le \min(n,2e).
```

Define

```math
L_e(a)=\prod_{j=1}^{\min(n,2e)}(e+ja),\qquad
D_0(a)=1,\qquad D_e(a)=\prod_{h=1}^{e}L_h(a).
```

Every factor is positive for `a>0`. The polynomials have integer coefficients.

**Lemma 4.** From every state with `e` active edges, each final-mask probability
has the form `N_s(a)/D_e(a)`, where `N_s` is an integer polynomial with
nonnegative coefficients. The recursion in Section 2 constructs these
polynomials exactly.

**Proof.** Induct on `e`. The claim at zero is the boundary condition. For a
transition to a state with `e'<e` active edges, multiplying its numerator by
its rate (`1` or `a`) and by

```math
\frac{L_e(a)}{e+ka}\prod_{h=e'+1}^{e-1}L_h(a)
```

puts its contribution over `D_e`. The displayed quotient means deleting the
single indicated factor from the defining product for `L_e`; it is a
polynomial. Every operation is multiplication or addition of polynomials with
nonnegative integer coefficients. Summing all transition contributions gives
the claim. QED.

The initial state has `m=|E|` active edges. The verifier outputs `D=D_m` and
`N_s` for every one of the `2^m` final masks. It also checks the exact identity

```math
\sum_s N_s(a)=D(a).
```

The file `constant_freezing_laws.json` records these polynomials. A coefficient
list `[c0,c1,...]` denotes `c0+c1*a+...`. Edges have the order recorded in each
graph entry; bit `i` of mask `s` says whether edge `i` is open.

## 4. Reducing both questions to polynomial signs

For an increasing event `A`, put

```math
C_A(a)=\sum_{s\in A}N_s(a).
```

For monotonicity define

```math
M_A(a)=C_A(a)D'(a)-C_A'(a)D(a).
```

Then

```math
\frac{d}{da}\mu_{G,a}(A)=-\frac{M_A(a)}{D(a)^2}.
```

Thus nonnegative coefficients of `M_A` prove a nonpositive derivative for
every positive real `a`. Integrating from `a` to `b` proves the required
ordering. The program checks all coefficients, including the constant term.
For every connected graph examined, only the empty and full events have the
zero polynomial, so each other event is in fact strictly decreasing.

For positive association define

```math
H_{A,B}(a)=C_{A\cap B}(a)D(a)-C_A(a)C_B(a).
```

The covariance of the two event indicators is exactly `H_(A,B)/D^2`. Its
coefficientwise nonnegativity therefore proves the required inequality for
every positive real `a`.

Coefficientwise nonnegativity is a sufficient condition, not a necessary one.
A negative coefficient would require additional analysis and would not by
itself constitute a counterexample. In the claimed ranges every polynomial
passes this sufficient test.

## 5. Exhaustiveness of the finite search

### Connected graphs

Begin with the one-vertex graph. At each step either add an edge between
nonadjacent existing vertices or attach one new leaf to an existing vertex.
Canonicalize the resulting graph by taking the lexicographically least edge
list over all labelings within its degree classes, with the degree classes
ordered by increasing degree.

Every produced graph is connected and simple. Conversely, a connected graph
with a cycle can lose an edge of that cycle while staying connected. A tree
with at least two vertices can lose a leaf and its incident edge. Induction
therefore proves that the augmentation generates every connected simple graph.
Any isomorphism preserves degree, so canonicalization within degree classes
identifies exactly the isomorphism classes; it cannot discard a new graph.

### Increasing events

Represent the truth table of an event on `m` edge bits by an integer with
`2^m` bits. At zero edge bits there are exactly two events, false and true.
An increasing event on `m` bits has two increasing sections `A0,A1` on `m-1`
bits, satisfying `A0 subseteq A1`. Conversely, every such ordered pair defines
an increasing event. This recursion is used literally in `upsets`.

The resulting exhaustive counts are:

| Edges per connected graph | Connected graphs | Increasing events per graph | Monotonicity certificates | Association certificates |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 3 | 3 | 6 |
| 2 | 1 | 6 | 6 | 21 |
| 3 | 3 | 20 | 60 | 630 |
| 4 | 5 | 168 | 840 | 70,980 |
| 5 | 12 | 7,581 | 90,972 | Outside association scope |
| **Total** | **22** | | **91,881** | **71,637** |

Association is symmetric, so its count uses the `u(u+1)/2` unordered event
pairs with repetition on each graph. Constant events are included. Every
coefficient of every counted certificate is nonnegative in the exact run.
This finite statement is fully reproducible by the supplied verifier; no
floating point or randomized checks enter it.

## 6. From connected graphs to arbitrary finite disjoint unions

The PCF processes on distinct connected components depend on disjoint clocks,
so their final edge sets are independent.

Stochastic domination of each component law implies domination of their
product: integrate an increasing function over all but one component, replace
that component law by the dominating one, and repeat. Each intermediate
function is still increasing in the component being replaced. An inequality
for increasing events gives the same inequality for arbitrary increasing
functions on the finite state space by their finite threshold decomposition.
This proves Theorem 1 from the connected-graph certificates.

For association, suppose independent `X,Y` each have associated laws, and
`f(X,Y),g(X,Y)` are increasing. The covariance decomposition gives

```math
\operatorname{Cov}(f,g)=
\mathbb E[\operatorname{Cov}(f,g\mid Y)]
+\operatorname{Cov}(\mathbb E[f\mid Y],\mathbb E[g\mid Y]).
```

The first term is nonnegative by association of `X`, applied for each fixed
`Y`. The two conditional expectations in the second term are increasing
functions of `Y`, so that term is nonnegative by association of `Y`.
Induction handles any finite number of components and proves Theorem 2.
Isolated vertices have deterministic empty edge sets and cause no change.

## 7. Controls against model and inequality errors

The certificate program performs the following independent or adversarial
controls in addition to the proof computation:

1. A forward rational-probability Markov calculation retains every warm
   component's freezing clock, including irrelevant components, and runs until
   every vertex is frozen. This uses a different recursion direction and a
   different terminal condition from the symbolic calculation. On all 22
   connected graphs its entire final distribution agrees exactly with the
   symbolic law at `a=1/7`, `a=1`, and `a=11/3` (66 comparisons).
2. On one edge, both methods agree with the direct exponential race:
   `P(open)=1/(1+2*a)`.
3. On three independent fair bits every enumerated increasing-event covariance
   is nonnegative. A deliberately anticorrelated two-bit law produces a
   strictly negative covariance under the same event arithmetic.
4. The calculation reproduces the stronger lattice inequality's known failure
   on the four-vertex path, which Mottram explicitly distinguishes from the
   association question [S1, Section 1.4].

For the last control, index the path's edges in their path order and let
`a=1`. In mask order `0,...,7`, the exact probabilities are

```math
\left(\frac{34}{105},\frac17,\frac{13}{105},\frac8{105},
\frac17,\frac2{35},\frac8{105},\frac2{35}\right).
```

The atoms with masks `1` and `4` have intersection `0` and union `5`, giving

```math
\mu(0)\mu(5)-\mu(1)\mu(4)
=\frac{34}{105}\frac2{35}-\frac17\frac17=-\frac1{525}<0.
```

This is a counterexample to the lattice condition only. At the same parameter
and on the same graph, every increasing-event covariance has the sign claimed
in Theorem 2. The distinction is therefore enforced by an exact negative
control rather than just an explanatory caveat.

## 8. What is and is not established

Theorems 1 and 2 cover all positive real parameters in the specified component
classes. A finite parameter grid would not give that conclusion; the polynomial
certificates do. The controls at three rational parameters are checks on the
implementation, not substitutes for the all-parameter proof.

The general monotonicity and association questions remain open. The present
work does not infer either property for larger connected graphs, all trees,
multigraphs, infinite-volume processes, or conditional laws. It does not assert
the FKG lattice condition. The search log records what was checked about the
literature; it does not establish priority for these restricted cases.

## Sources

[S1] Edward Mottram, *Percolation with constant freezing*,
[arXiv:1309.1752v2](https://arxiv.org/abs/1309.1752v2),
[primary PDF](https://arxiv.org/pdf/1309.1752), Section 1.4 (open questions) and
Definition 2.1 (finite-graph generator). Checked 2026-10-09.

[S2] Edward John Mottram, *The geometry of non-Markovian interacting systems*,
PhD dissertation, University of Cambridge, 2015,
[catalog primary-source URL](https://www.repository.cam.ac.uk/bitstreams/72e98faf-8e12-4374-9a2e-c0c8ad6840e1/download).
The catalog attributes Q276 to Section 3.1.4, equation (3.1.1), and Q277 to
Section 3.1.4 and Example 3.1.5. The dissertation URL was inaccessible through
the research tool on 2026-10-09; the author's primary paper [S1] supplies the
model and the exact two open questions directly.
