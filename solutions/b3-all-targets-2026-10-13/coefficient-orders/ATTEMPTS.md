# Q167 attempts

## Q167-O01: exhaustive low-degree order classification

Attempt: derive every realizable order by using r_i>=1, integer reciprocal
bounds and an exact witness enumeration, then extend by degree induction.
LOW-DEGREES.md gives a complete classification through n=4. The bounded
enumeration has explicit witnesses through n=6. It cannot certify completeness
for n>=5, and no inductive exhaustion argument was found. This constitutes
one partial advance and one failed attempt at the all-n classification.

## Q167-O02: coefficientwise dominance plus unimodality as a criterion

Attempt: characterize realizability by c_i<=c_j for i<j with i+j<=n,
together with the strongly unimodal order restriction and the exceptional
all-unit ties. This necessary criterion is insufficient already at n=4.
The index order 01432 respects those universal dominance relations and is
compatible with strict unimodality of an abstract coefficient sequence,
for example (1,2,5,4,3). But it requires c_4>=c_1 and c_2>=c_3, which
the exact integer degree-four obstruction rules out. Thus this proposed
general classification criterion fails, independently of the bounded
enumeration. More arithmetic constraints are needed; two consecutive
full-target failures are recorded, with the partial theorem retained.

## Q167-O03: reciprocal bounds and unit-factor induction

Attempt: extend the low-degree classification to every degree by separating
unit factors and applying reciprocal elementary-symmetric inequalities.
DEGREE-FIVE.md proves completeness through degree five, improving the
previous degree-four scope. It derives three exact arithmetic implications
and fourteen orders, including ties. The unit-count step cannot continue
with the same finite branch list: already in degree six the all-nonunit
vector r=(2,2,2,2,2,2) has e_2(1/r)>e_1(1/r), so the degree-five assertion
that this case forces a unique all-two boundary equality does not extend.
Higher reciprocal comparisons require new branches and no all-degree
exhaustion is obtained. Independent review merges this with O01 as a
continuation of the same reciprocal/unit-factor induction. It supplies a
new degree-five partial theorem but **no additional failure count**.
The earlier degree<=4 result is retained, not newly claimed.

## Q167-O04: recurrence on coefficient-order states

Attempt: build all realizable index orders inductively, retaining only the
current ordering and the next positive integer factor. Multiplication by
1+sx gives c'_j=c_j+s c_(j-1), but this is not an operation on order states.
The two inputs r=(1,2) and (1,4) have the same strict order 021. Adjoining
s=2 produces (1,5,8,4), order 0312, and (1,7,14,8), order 0132.
In particular 0132 is invalid for the first input but valid for the second.
The quantitative gaps discarded by the state are necessary. This defeats
the proposed induction contract; it does not rule out an enriched state
construction. After merging O01/O03, this is the third distinct full-target
failure.

## Q167-O05: real-root chambers followed by local integer rounding

Attempt: obtain an integer classification by solving the real r_i>=1
chambers and rounding each coordinate to one of its neighboring integers.
The strictly ordered real input (1,1,5/3,5) gives
(1,26/3,68/3,70/3,25/3), order 04123. Its only two neighboring integer
vectors (1,1,1,5) and (1,1,2,5) give (1,8,18,16,5) and (1,9,25,27,10).
Neither satisfies 04123. Thus even choosing floor/ceiling independently
cannot prove the required passage from a real chamber to an integer witness.
That order does have a different integer witness (1,1,2,3); this is a
counterexample to the proposed local rounding step, not to realizability.
A global arithmetic chamber theorem remains missing. After merging O01/O03,
this is the fourth distinct full-target failure. A fifth distinct route is
required before stopping.

O03 uses reciprocal inequalities and an arithmetic branch exhaustion;
O04 tests the information retained in degree induction; O05 tests a real
feasibility-to-integer lifting contract. Their mathematical obstructions
and obligations differ. Exact controls are in ORDER-CHECK.json. O01/O03 are
explicitly counted only once after the independent review correction.

## Q167-O06: extremal coefficient bounds from sum and product

Attempt: classify the integer coefficient chambers using the endpoint
statistics S=sum r_i=c_1 and P=product r_i=c_n, with Maclaurin bounds

    binomial(n,k) P^(k/n)<=c_k<=binomial(n,k)(S/n)^k.

These follow respectively by AM-GM over the k-subset products and the
standard elementary-symmetric mean inequality. Where disjoint bounds
separate two coefficients, they rigorously determine their order for
every input having these endpoints. The proposed full construction was
to make this endpoint separation decide the intermediate chamber as well.
It fails on two actual positive-integer degree-four inputs with identical
S=28 and P=168:

    (1,1,12,14) -> (1,28,221,362,168), strict order 01423;
    (1,2,4,21)  -> (1,28,161,302,168), strict order 01243.

In particular c_2 versus c_4 is not determined by the endpoint statistics;
the same exact bounds must admit both opposite signs. This is a failure of
the proposed sufficient extremal separation contract, not a claim that
no set-valued classification could use S,P together with further arithmetic
data. No all-n chamber theorem results. This fifth distinct full-target
failure stops Q167 unresolved. O04 loses information in a degree-extension
state; O06 fixes all degrees/endpoints and tests global extremal separation.
