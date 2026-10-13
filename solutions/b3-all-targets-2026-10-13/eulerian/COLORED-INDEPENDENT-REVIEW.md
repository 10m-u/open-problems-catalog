# Q1262/Q1263 independent scope, proof and attempt-count review

Reviewed 2026-10-13 by the retained second agent. **Q1263 has five accepted
distinct failed full-target constructions. Q1262 has four: E02–E05. E01 is
useful new finite evidence from an existing recognizer, and is not counted
again.** Neither full catalog question is solved. No new solve attempt was
initiated in this audit, and root global status was not edited.

## Exact source and target conventions

I read the frozen Q1262/Q1263 entries and the final
[Deligeorgaki–Han–Solus paper](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf),
especially printed pp.2,14,21 and23, Questions4.1/4.7 and Proposition4.2.
Colors start at1, comparisons are strict in color-first order, and the
last sentinel is(n+1)^1. The programs' zero-based symbols and sentinel
(1,n) give exactly the same comparisons. Q1262 permits representing s of
any length. Q1263 concerns both gamma vectors whenever the actual input
is bi-gamma-positive, rather than just the sufficient family of Corollary3.12.
Published uniform-color representations and uncolored interpretations
are dependencies, not newly solved catalog questions.

The frozen ledger already treats the general finite membership recognizer
as a partial answer and retains structural classification as Q1262's
remaining obligation. This review uses that established contract. It does
not infer from unsuccessful constructions that a structural answer or
natural interpretation is impossible.

## Endpoint proof and small gamma orbits: accepted

For N>=1 distinct symbols, common r>=2, let J replace (c,i) by
(r+1-c,N+1-i) without reversing positions. This is an involutive bijection
of the same word set. An internal comparison cannot be an equality,
including when the colors agree, so each of the N−1 internal descent
indicators changes to its complement.

For extreme last colors, the sentinel indicator changes from0 to1 or
from1 to0, giving d(Jw)=N−d(w). Thus U=x^N U(1/x). For interior last
colors, the old and new sentinel indicators are both1, giving
d(Jw)=N+1−d(w), and V=x^(N+1)V(1/x). Since V is divisible by x,
V/x is symmetric with respect to N−1. The full polynomial has degree N:
the descending symbol word with every color r has N descents. Uniqueness
of symmetric decomposition therefore proves a=U,b=V/x at the catalog's
actual degree. This is an all-size **ordinary-coefficient** interpretation,
not an all-size gamma interpretation.

I corrected two small presentation issues in ENDPOINT-COLORS.md. Symmetry
is with respect to the stated degree, with degree at most that bound;
b=0 when r=2. Also the four distinguished N=2 words now have an explicit
action: swap their underlying order and toggle their common color between
1 and r. These two commuting involutions act transitively, producing the
Boolean-square orbit with row(1,2,1). Every other extreme word is a
one-descent singleton, and J pairs interior words with descents1 and2.
Consequently the stated gamma counts(1,4(r−1)) and(r(r−2)) hold for every
r>=2. The N=1 singleton/interior interpretation also holds for every r>=2.

Repeated letters invalidate the internal-comparison argument, and symbol
complementation need not preserve a general multiplicity vector. Literal
enumeration of m=(2,1),r=(3,3) gives

    h=(1,36,42,2), a=(1,35,35,1), b=(1,7,1),
    extreme-last-color row=(1,31,22,0),
    interior-last-color row=(0,5,20,2).

The endpoint partition therefore fails on an actual bi-gamma-positive
multiset input. It refutes that extension, rather than Q1263 itself.

## Recognition and growth calculations: accepted at their stated scopes

I reread the previously reviewed degree-compression proof: each nonconstant
representable polynomial of degree d has some representing sequence of
length<=2d−1. Together with volume and unit removal, this makes the finite
ordered-factor/separator search exhaustive for existence, including
representations whose original length exceeds that bound. The exclusions
(1,20,15),(1,13,10),(1,24,45,10) and their candidate counts27,22,158 are
correct. The stronger statements exclude arbitrary representing length;
the finite computer work relies on the written compression theorem.

I added the missing degree-zero qualification in COLORED-RESULTS.md:
P=1 is represented by s=(1) and is handled separately. The provided probe
only scans nonconstant cases; its factor-string routine should not be
advertised as implementing that special case for every possible input.

For growth a→a+1 at fixed color r, let c=r/(a+1) and M=sum(m). The
Ehrhart series changes from H to H+c xH'. Substituting
H=A/(1−x)^(M+1) gives the stated operator. Its coefficient rule is

    [x^j]A_new=(1+cj)h_j+[c(M+2−j)−1]h_(j−1).

This independently reproduces the actual membership-loss transition and
86 admissible growth controls. For G05 it gives the formal output
(1,17/2,8,1/2); decomposition at degree3 gives
b=−(1/2)(1+x)^2. This is a negative **formal basis transition**, not an
actual colored-input counterexample. The actual input's other branches
compensate, and its grown gamma vectors(1,32),(1,5) are positive.

## Per-target count disposition

| Q1262 route | Disposition and full-scope obligation |
|---|---|
| E01 | **Do not count.** Thirty-six fresh evaluations of the already general recognizer add exact cases, but no new structural inference is worked in this packet. Repeating its previously recorded missing classification step is not another failed full-target route. |
| E02 | Accept: actual root/coefficient criteria hold for an unrepresentable colored numerator. This defeats the specified scalar structural criterion. |
| E03 | Accept: concatenating or unit-separating component simplex representations loses the actual multinomial interleavings and volume. A geometric product construction fails. |
| E04 | Accept: heterogeneous scaling of the known all-two vector has the **correct** volume24 but the wrong numerator. This differs from E03's volume loss. |
| E05 | Accept: an actual representable input becomes unrepresentable after a multiplicity increment; appending the integral volume-ratio denominator gives a different numerator. This is a dynamic insertion obstruction, rather than E04's static scaling. |

E02–E05 reuse some actual inputs and all-length certificates, but the
proposed mechanisms and failed obligations differ. Q1262 remains active
at **four accepted consecutive substantive failures**, pending a genuinely
distinct fifth route from the root. This review itself supplies none.

| Q1263 route | Accepted contract and scope |
|---|---|
| G01 | Frozen-color classical action has an orbit1+x with the wrong center for either target gamma basis. An orbit-action construction fails. |
| G02 | The successful endpoint subset partition cannot extend literally to repeated letters. This is a subset/decomposition failure, with a preserved all-size partial. |
| G03 | Independent colors on existing uncolored tree objects cannot preserve their gamma index and part: degree, gamma0, and the new second part disagree. This differs from G01's individual classical orbit shapes, although both use the same small input. |
| G04 | Root-pair factors would require finite choice counts36±8sqrt(19). Only the specified independent integer-choice factorization is excluded; weighted analytic factors and dependent/grouped objects remain possible. |
| G05 | Termwise nonnegative gamma insertion fails on an individual formal basis branch with admissible operator parameters. It differs from static decoration and is explicitly weaker than an actual-input counterexample. |

These are five distinct sufficient-construction failures, with shared
small witnesses and independence assumptions disclosed. They do not
establish that all repairs of those constructions fail. I accept the
five-attempt stop of the full Q1263 target, retaining the named partials.

## Independent controls and receipt

[check_colored_review.py](check_colored_review.py) imports none of the root
implementations. Recursive literal multiset words replace permutation-set
enumeration; literal inversion-sequence products replace the refined
Eulerian recurrence; factor/unit strings are built directly. Exact Fraction
arithmetic handles the growth branch.

[COLORED-REVIEW-CHECK.json](COLORED-REVIEW-CHECK.json) passes all36 recorded
cases,2,087 literal colored words,4,012 canonical candidates,86 actual
growth checks,90,416 wordwise involution checks across22(N,r) pairs,
nine explicit four-word orbits,276 interior pair orbits, and19 one-letter
gamma controls. It includes reviewed-file hashes. These finite checks
support the proof audit and individual witnesses; they do not supply
unbounded classification or gamma constructions. No novelty or external
peer-review claim is made.
