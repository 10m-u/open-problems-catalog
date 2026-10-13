# Q1262: structural-classification route register

E02--E05 are independently accepted; E01 is auxiliary and rejected as a count. E06 is a new proposed fifth route pending review. The target covers all positive m,r and
representing s of arbitrary length; finite membership decisions remain
partials. No repeated old uncolored exclusion is counted.

<a id="q1262-e01"></a>
## E01 — auxiliary exact heterogeneous recognition (not counted)

The new36-case colored list in COLORED-RESULTS.md uses the existing
proved length compression and factorization volume. It decides the
recorded heterogeneous cases completely, with literal word controls,
but admits both representations and exclusions depending on m,r.
Known uniform cases are controls rather than separate new attempts.
This constructive recognition approach provides a terminating test
for any supplied pair but does not yield the requested general
structural classification. Its missing full obligation is a uniform
description replacing the unbounded family of ordered-factor searches.

<a id="q1262-e02"></a>
## E02 — real roots and connected-quadratic coefficient criteria

Try to characterize representability using real-rootedness, positive
integer coefficients, simple roots and the necessary connected degree-two
shape h1>h2>0. Actual A_(1,2)^(3,2)=1+20x+15x² meets all these tests: its
discriminant is340>0 and its two roots are negative. Yet exhaustive
all-length recognition at volume36 returns no match among27 candidates.
Thus even these strengthened scalar root/shape conditions are insufficient
for actual colored inputs. This differs from E01's constructive enumeration
obligation; it refutes a proposed coarse structural criterion.

<a id="q1262-e03"></a>
## E03 — concatenate representations of the scaled-simplex factors

Each component r_iΔ_(m_i) is integrally equivalent to the constant-
denominator lecture-hall simplex. Try concatenating its denominator
blocks, with units to separate independent ascent statistics. For
m=(1,2),r=(3,2), the separated vector(3,1,2,2) gives

    (1+2x)(1+3x)=1+5x+6x²,

not1+20x+15x². Direct concatenation also has volume12 rather than36.
The product polytope contributes the multinomial interleaving factor
M!/prod(m_i!), whereas unit separation multiplies the factor h* rows.
An ascent-preserving shuffle construction would have to account for
those interleavings; no such general s construction was obtained. This
is a geometric/product construction failure, not a root criterion.

<a id="q1262-e04"></a>
## E04 — scale known uniform-color vectors coordinatewise

Try extending the published uniform-color representations to different
colors by multiplying each multiplicity block by its own r_i. For
m=(2,2), the known uncolored length-four vector(1,1,3,2) can be
scaled uniformly to model uniform colors. The proposed heterogeneous
block scaling for r=(1,2) gives(1,1,6,4), with1+16x+7x² instead of
the actual1+13x+10x². More strongly, all-length recognition proves
the actual numerator has no s representation at all. Thus the
heterogeneous extension of this published family cannot be universal,
regardless of how that one vector is repaired. This specific scaling
mechanism differs from E03's independent component multiplication.

<a id="q1262-e05"></a>
## E05 — append a denominator for each multiplicity increment

Work the exact growth operator in COLORED-RESULTS.md. Its volume ratio
is b=r(M+1)/(a+1). Try retaining an existing representing vector and
appending b when it is an integer, with refined Eulerian insertion
supposed to implement the differential identity. Start m=(1,1),
r=(3,2), where A=1+9x+2x²=E_(2,6). Increasing the second multiplicity
from1 to2 gives b=3 and the exact operator output1+20x+15x². But
appending3 gives E_(2,6,3)=1+19x+16x². The target output is in fact
unrepresentable, so no general membership-preserving insertion
induction is possible. This actual transition differs from E04's
static heterogeneous rescaling. Richer restricted insertion families
may still exist; no all-pair classification resulted.

All five full-target attempts fail while their exact finite decisions
and operator formulas remain useful. No universal nonrepresentability
or impossibility of other classifications is asserted.


## Independent count correction

The retained-agent review accepts E02--E05 as four failures. E01 supplies fresh finite evidence only and does not recount the earlier general recognizer. Q1262 remains active at four; no five-failure stop is claimed. See COLORED-INDEPENDENT-REVIEW.md.


<a id="q1262-e06"></a>
## E06 — classify primitive color rays and recover membership by dilation

The new dimension-matched forward dilation lemma and full worked inference are in [DILATION-FAMILIES](DILATION-FAMILIES.md). If an input has an s-representation of length at most M=sum(m), padding leading units and dilating the equal-dimensional Ehrhart polytopes proves representability after every common integral color scaling. Try to make this a classification by primitive color vectors: remove the common gcd, decide the primitive inputs, then recover membership on their rays by that equivalence.

The converse fails on an actual colored pair: m=(1,1), r=(4,5) gives(1,27,12), unrepresentable at any length by all22 canonical degree-two candidates; multiplying both colors by3 gives r=(12,15), numerator(1,205,154)=E_(8,45). More strongly every r=(12t,15t) is E_(8t,45t), with row(1,180t^2+27t-2,180t^2-27t+1). The two-coordinate formula proves that infinite family exactly. DILATION-CHECK.json retains all candidate rows and1,600 independent-formula controls.

Thus primitive-ray membership is not an equivalence, despite forward closure at matched dimensions. The residual classification must track arithmetic on the ray multiplier as well as the primitive input. This differs from E04's heterogeneous static scaling of the source vector and E05's multiplicity increment: here m is unchanged and every color is scaled by the same number; the valid forward lemma does not supply the proposed inverse. This developed structural inference is the proposed replacement fifth failure, not a recount of E01's finite-input recognizer. Partial proofs do not reset the count. No sixth route starts pending honest independent review.
