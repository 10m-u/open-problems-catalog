# Independent review of the Eulerian reconstruction

7 October 2026. Reviewed `eulerian-report.md` as supplied to this audit. One finite coefficient error requires correction; no gap was found in the stated proofs of E1, E2 after that correction, or E3. This is an independent mathematical reading and exact enumeration, not formal verification or a priority assessment.

## Required correction

The exceptional vector `(2,6,3)` has

\[
E_{(2,6,3)}(x)=1+19x+16x^2,
\]

not `1+18x+17x²`. Both have volume 36, so checking volume alone misses the error. The correct linear-minus-quadratic gap is three, which preserves E2 and the argument in E3.

An exact hand count: for `e_1=0`, two ascents require `0<e_2/6<e_3/3`, giving one choice at `e_3=1` and three at `e_3=2`, hence four. For `e_1=1`, the initial ascent is already present; exactly one of `1/2<e_2/6` and `e_2/6<e_3/3` must hold. For `e_2=0,1,2,3,4,5` the counts are respectively `2,2,1,1,3,3`, totaling twelve. Thus the quadratic coefficient is sixteen, the constant coefficient is one, and the linear coefficient is `36-1-16=19`.

## E1: contraction to length `2d−1`

The unit deletions and separator factorization are valid because a transition to a unit coordinate has ratio zero and never contributes an ascent; the next block starts from the same zero ratio as an independent sequence. The degrees of the nonunit blocks add under multiplication.

For a nonunit block of length L, alternating positive odd coordinates and zero even coordinates gives `ceil(L/2)` ascents. Thus `L<=2D` when its polynomial degree is D. If `L=2D`, take any odd/even pair `(A,B)!=(2,2)` and choose its entries `1` and `B-1`. Their ratios satisfy `1/A<(B-1)/B`. Before that pair, use positive/zero pairs; after it, use zero/positive pairs. The earlier `j-1` pairs give `j-1` ascents, the chosen pair gives two, and the later `D-j` pairs give `D-j`. The total is exactly `D+1`. The boundary before the chosen pair is zero (or the initial zero when j=1); the boundary after it is a decrease to zero, so no ascent was accidentally counted or lost. Therefore every such pair must be `(2,2)`.

The all-two final-pair contraction is an exact conditional identity. With incoming ratio zero the two binary coordinates contribute `1+3x`; with incoming ratio one half they contribute `3+x`. A single final denominator-four coordinate gives exactly the same two polynomials. This holds also for a two-entry block, whose incoming ratio is the initial zero. Reinserting b−1 separators after contracting blocks gives `sum_i(2D_i-1)+(b-1)=2d-1`. The theorem is existential, as the report states; original vectors may have arbitrarily many unit entries.

## E2: connected degree-two blocks

The length-two formula counts lattice points strictly above the diagonal and is correct, including the gcd correction. In particular `h1-h2=A+B+gcd(A,B)-3>0`. Degree-one exceptional pairs, such as `(2,2)`, are outside the hypothesis `deg=2`; including their zero quadratic coefficient in formula controls is harmless.

Reversal is justified by the affine integral map of lecture-hall simplices, a signed permutation followed by integral translation. It preserves Ehrhart counts after dilation, hence the numerator used for `E_s`. In dimension three, degree three is equivalent to an integer `j` in the strict interval `(B/A,B(C-1)/C)`: choosing the least first positive coordinate and greatest final coordinate suffices, and necessity follows from those extrema. The strict inequalities are essential at `(3,3,3)` and `(2,6,3)`.

After arranging `A<=C`, the classification given in the report is complete. If `A,C>=3`, all cases except `(3,3,3)` admit a strict middle integer. If `A=2,C>=3`, the least candidate is `floor(B/2)+1`; failure occurs precisely at `B=2` (all C), `(B,C)=(3,3),(4,3),(4,4),(6,3)`. If C=2 there is never a degree-three ascent chain. For `B=5` or `B>=7`, that candidate lies strictly below `2B/3`. The two infinite-family coefficient formulas are correct. The exceptional coefficient pairs, in report order, should be

`(10,7), (12,11), (18,13), (19,16), (16,10)`.

Every corrected gap is strictly positive. Thus E2 survives the correction.

## E3: exact `(2,b)` classification and its boundary

For `b>=2`, the target has degree two. Its canonical nonunit-block decomposition has one degree-two block or two degree-one blocks; each nonunit block has positive degree. In the two-block case the sum and product equations for the positive integral linear coefficients are exact. Their discriminant condition is equivalent to `b(b+1)/2=t²`: the discriminant is `4t²`, and the constructive vector has coefficients `b-t,b+t`. For `b>1`, `t<b`, so both coefficients are positive. For b=1 the separate one-entry realization is correctly supplied.

In the connected case E2 gives `2b>b(b-1)/2`, hence `b<5`. In particular **b=5 is excluded by equality**, not accidentally included in the small cases. Its triangular number is 15 and is nonsquare, so the disconnected case also excludes it. For b=2,3,4 the volumes are six, ten, and fifteen. Each volume has exactly two prime factors **counted with multiplicity**, so a nonunit vector of length at least three is impossible. The listed length-two possibilities and their coefficients are correct. This proves precisely the claimed criterion, after the E2 coefficient correction.

The all-degree sharpness claim and simple-root claim are explicitly not used in this report; this audit does not recover or endorse them.

## Independent exact controls

A separate literal inversion-sequence enumerator, using cross multiplication of integers for every ascent comparison, checked:

- every length-two vector with entries from 2 through 15 against the gcd formula;
- every length-three vector with entries from 2 through 12 against the complete degree-two classification and its reversal;
- both infinite-family formulas through parameter 99;
- all-two final-pair contraction through length 12;
- each of the five exceptional triples, locating the `(2,6,3)` error above.

The first two groups comprise 1,527 independent vector cases. All identities passed except the report's incorrect displayed coefficient pair, whose corrected value passes. The finite checks audit calculations; the all-degree conclusion relies on the written block and ascent arguments.
