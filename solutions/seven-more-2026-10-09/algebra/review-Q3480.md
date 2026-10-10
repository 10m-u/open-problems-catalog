# Independent review of Q3480

Reviewer: algebra agent, separate from the discrete author.
Date: 2026-10-09. Outcome: **accepted as partial progress**, with exact
fixed-alphabet enumeration and a complete four-symbol formula. No blocking
defect found. The unrestricted enumeration remains unresolved in this packet.

## Source and operation

The journal PDF did not load in this review's web call. Independently read the
author's [arXiv paper](https://arxiv.org/html/2003.02536v2), including Theorem
3.8, and the [doctoral thesis](https://arxiv.org/pdf/2210.03621), Section 8.1 and
Open Problem 8.1. These confirm the two-stack operation, the initial eight
unrestricted counts, and the repeated-letter rescue of 3241 by an intervening
value at least as large as the selected 4-role. The thesis explicitly supplies
the weak inequality in its proof. This is the hare stack operation; a hare
pop-stack empties the entire stack and is a different question.

## Compression proof

The run compression retains enough information. Each physical stack is weakly
increasing from its top to its bottom. On receiving a larger value, an entire
equal-valued top run is popped before the input is pushed. On the second stack,
only the first of a batch of equal incoming values can trigger pops; remaining
copies change multiplicity alone. Output runs have no internal strict descent.
Consequently retaining the two sets of occupied values and the previous output
value preserves the exact acceptance decision, including final flushes.

The state bound is finite for each fixed alphabet, and the transition-count
matrix yields a rational generating function. The use of values 1 through
\(k\) with sentinel 0 in the prose agrees with values 0 through \(k-1\) and
sentinel -1 in the code. Inclusion-exclusion is legitimate because increasing
relabeling preserves every stack comparison. Summing over alphabet maxima
from 1 through the length counts all nonempty Cayley words exactly once.

## Four-symbol model and algebra

On four symbols the source criterion becomes an occurrence of 2341, or an
occurrence of 3241 without an intervening 4 between its selected 3 and 2. The
six-state table preserves exactly these prefix events. In particular, state 2
must reset on a 4, while a previously formed 23 pair persists. Both behaviors
are present. Each live state accepts the empty suffix, as required.

Checked the five continuation equations and their elimination. They yield

\[
F_4(z)=\frac{1-9z+30z^2-42z^3+19z^4}{(1-z)(1-3z)^4}.
\]

Applying inclusion-exclusion with \(F_0=1\), retaining the empty word's
contribution, gives the displayed exact-maximum series. At \(z=1/3\), the
coefficient of its order-four pole is \(1/54\),
and hence its coefficient asymptotic is \(n^3 3^n/324\). This concerns maximum
exactly four; it is not the growth rate of the unrestricted Cayley count.

## Executed and inspected controls

Read the generator and separate verifier, and ran the latter successfully.
It checks every supplied compressed-state transition and acceptance flag,
then proves reachability of the full supplied state set. Thus the finite
quotient check is closed under every input letter and is not merely a prefix
test. All 700 transitions and all 87,381 literal full-multiplicity words
through length eight passed. The matrix polynomial identity and exact
rational inclusion-exclusion identity also passed.

The successful word 34241 and unsuccessful word 3241 check the equality case
that would be lost by treating repeated symbols as distinct permutation ranks.
The initial unrestricted sequence agrees with the source. The acceptance
compression proof and closed quotient certificate justify the all-length
fixed-alphabet result; the bounded literal-word search alone would not.

## Catalog decision

Retain `partial`: an explicit rational answer is obtained for the four-symbol
slice, and finite-state algorithms are established for every fixed alphabet.
The sum over all maxima is a valid computable formula, but no useful closed
unrestricted generating function or uniform asymptotic is supplied. The
submitted report states this distinction accurately. No external peer-review
or historical-priority claim is supported by this review.
