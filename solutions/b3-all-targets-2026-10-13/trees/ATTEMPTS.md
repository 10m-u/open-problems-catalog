# Q4666: converse for conditioned BGW tree growth

13 October 2026. The exact plane-tree inclusion convention, conditioned
weights and positivity assumptions are in the frozen register. The primary
[paper](https://arxiv.org/html/2411.03065v3#S1.SS3) and its root-composition
criteria were read. The binary-support converse is already stated there;
the derivation below is an independent elementary control, without a claim
of priority.

## T01: support and root-star inequalities

Outcome: failed full-target proof route, with a complete support conclusion.

An increasing coupling forces the positive offspring support to be an initial
interval. If mu(k)>0 with k>=2, the plane star with k leaves has positive
P_(k+1) probability. Its only plane subtree with k vertices is the star with
k-1 leaves: deleting a nonfinal sibling is forbidden by the left-sibling
convention. In the coupling, that subtree must have positive P_k probability,
so mu(k-1)>0. Induction proves the claim; mu(1)>0 also follows from Z_2>0.
Thus the no-internal-zeros portion of Q4666 is proved for arbitrary support.

I then tried to extract the local log-concavity inequalities from the same
small-size increasing events. Let

    b=mu(1)^2, a=mu(0)*mu(2), t=mu(0)^2*mu(3)/mu(1).

At size three the probability that the root has at least two children is
a/(b+a). At size four it is (2a+t)/(b+3a+t). Monotonicity therefore yields

    a^2 <= a*b+b*t,

or mu(0)*mu(2)^2<=mu(1)^2*mu(2)+mu(0)*mu(1)*mu(3).
If mu(3)=0 and mu(2)>0, this implies mu(1)^2>=mu(0)*mu(2), completing the
known binary-support converse. With larger support the extra mu(3) term
prevents that deduction. The height-at-least-two event gives the distinct
necessary inequality b*t<=a*b+3a^2, which also fails to isolate log-concavity.
The general root-star event at sizes k+1 and k+2 involves the full
normalizers Z_(k+1), Z_(k+2), rather than only three neighboring weights.
An all-k argument eliminating those normalizers has not been obtained.

## T02: finite transport candidate — active

I searched for a counterexample through exact finite inclusion transports.
The candidate mu=(1,2,3,5)/11 is not log-concave, since 3^2<2*5. All of its
support entries are positive. For every n=1,...,11, the exact law at n can
be coupled to the law at n+1 under literal plane-tree inclusion.

The [checker](check_transport.py) enumerates plane trees, independently
compares its legal deletion relations with literal Ulam–Harris vertex-set
inclusions through size eight, and verifies Catalan enumeration through
size nine. It uses integer max flow with source capacities weight(T_n)*Z_(n+1)
and sink capacities weight(T_(n+1))*Z_n. Thus flow saturation is an exact
coupling certificate, with no floating-point feasibility tolerance.
Normalizing the offspring weights cancels in each fixed-size law.
The [receipt](TRANSPORT-CHECK.json) stores both capacities and actual flow.

Controls include a binary non-log-concave law that fails at n=3, a
log-concave binary law that passes every tested pair, and other non-log-concave
laws that fail at n=4. This candidate's success is consequently substantive
finite evidence, not merely a test that accepts every positive law.
It supplies no coupling for arbitrary n and does not refute Q4666.

The next obligation is an all-size certificate for this candidate, or an
exact obstruction at some later size. Fleurat's Corollary 2.9 only requires
the shifted composition normalizer ratios to lie between the two successive
tree-normalizer ratios. Its stronger chain in Proposition 3.9 explicitly
uses log-concavity. For the candidate, the n=0 endpoint bounds in the weaker
criterion pass: 3/2 and 5/3 are both <=2, although their ordering violates
log-concavity. Whether the remaining all-n bounds hold is active work;
the finite search has not yet been declared a failed attempt.
