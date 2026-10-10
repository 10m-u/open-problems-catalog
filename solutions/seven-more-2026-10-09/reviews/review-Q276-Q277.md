# Independent internal review of Q276 and Q277

Date: 2026-10-09. Reviewer: root research agent, separate from the author of
the probability reports. This is an internal mathematical and code review,
not external peer review or formal verification.

## Verdict and scope

The two restricted theorems are accepted on the supplied exact computational
evidence: stochastic monotonicity when every connected component has at most
five edges, and positive association when every component has at most four
edges, for finite simple graphs and every positive real freezing parameter.
The unrestricted catalog questions remain unresolved and receive `partial`
status under the repository's convention.

## Definition check

The reviewer independently opened Mottram's primary paper
([arXiv PDF](https://arxiv.org/pdf/1309.1752)), reading Section 1.4 and
Definition 2.1. The questions concern the final open-edge law. Cluster
freezing has one clock per warm open cluster, not per vertex; the implemented
generator has that rate. Frozen clusters never become warm again.
The unavailable thesis is not needed to infer these definitions because the
author's available paper states them directly.

## Mathematical audit

- An ignored warm component has no active incident edge. Every remaining
  incident closed edge therefore has a frozen endpoint and can never open.
  Deleting that component's freezing clock is valid for the final edge law.
- An opening reduces the number of active edges by one. Freezing a relevant
  component removes at least one active edge. Strict decrease makes the
  common-denominator induction acyclic, including states with closed edges
  internal to a warm open component.
- The possible relevant-component count satisfies `1 <= k <= min(n,2e)`.
  The factor `e+k*a` occurs once in the denominator layer `L_e`; cancelling
  that one factor yields the multiplier used in the code. The symbolic
  recurrence correctly counts every opening separately and every relevant
  freezing transition with rate `a`.
- For an event numerator C and denominator D, the derivative is
  `(C' D - C D')/D^2`. The implementation checks the opposite numerator for
  nonnegativity, so its monotonicity sign is correct. The association
  numerator is `C_(A intersection B) D - C_A C_B`, with the truth-table
  intersection correctly implemented by bitwise AND.
- Coefficientwise nonnegativity proves the signs for all positive real
  parameters; the rational parameter checks are only cross-checks of the
  final-law computation. No implication is made from a finite parameter
  grid to the continuous parameter range.
- The connected-graph augmentation is exhaustive: remove a cycle edge when
  possible, otherwise remove a leaf. Canonicalization enumerates all labels
  within the isomorphism-invariant degree classes. The event recursion is
  bijective with pairs of increasing sections A0 contained in A1.
- Both product arguments are valid for increasing events/functions, including
  events involving several components. Isolated vertices introduce no edge
  randomness. This proves the asserted unbounded-disjoint-union extension.

## Executed independent controls

The complete supplied verifier was rerun. It regenerated 91,881 monotonicity
and 71,637 association certificates with no negative coefficient, and
matched its independent full-clock Markov calculation on all 22 connected
graphs at each of the three rational parameters. The three-edge path's
negative FKG lattice difference is exactly `-1/525`; this confirms that the
claimed association result is not a mistaken lattice-condition assertion.

The reviewer also wrote `check_probability_enumeration.py`. Direct enumeration
of all labeled edge subsets yields 1,685 connected labeled graphs with at
most five edges and exactly the same 22 isomorphism classes as the author's
augmentation. Brute force over Boolean truth tables on up to four bits
reproduces counts `2,3,6,20,168` and matches the recursive event lists exactly.
The five-bit section recursion was reviewed algebraically and retains all
7,581 events; brute-force enumeration of all 2^32 truth tables was unnecessary.

The review does not certify publication novelty, larger component classes,
multigraphs, infinite-volume laws, or a full solution of either question.
