# Q1454 source and prior-evidence scope

The frozen target is statement `6ef0a2abf8519bc3a655`: for every single
classical forbidden permutation beta of length>=2, with a0=1, find a
nonnegative Borel measure on[0,infinity) whose nth moment is
|Av_n(beta)| for every n>=0. Avoiding multiple patterns is not the target.

Read the local primary text
`projects/thesis-catalog/texts/papers/collections-423c4663f7c533e0.txt.gz`,
especially Section1.2/Theorem1, Section3.1/equation(19), and Section4.2
Remark1, printed p.40; also
[Vatter, Question2.7](https://arxiv.org/html/2602.16355v2#S2.SS1).
The relevant moment criterion is positive semidefiniteness of both infinite
Hankel forms (a_(i+j)) and (a_(i+j+1)), meaning every finite quadratic
form is nonnegative. Nonnegative S-fraction coefficients are another
criterion. Our exact computations use finite matrices or coefficients and
do not extrapolate their positivity to all orders.

The primary already proves monotone forbidden-pattern families by the
[Rains unitary-trace representation](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v5i1r12/0)
and the1342 Wilf class by its explicit generating function. The1324
and length-five statements are numerical evidence, not closures.

The initial B3 report, printed pp.41–42, gives the known Catalan measure
and a shifted three-atom calibration. Its revised October7 ledger records
no new Q1454 theorem. These calibrations and known monotone cases may
check an implementation but supply zero new failed attempts or new
full-target solutions here. The same applies to a rerun of published
1324/length-five prefixes.

This packet pursues one new sufficient construction at a time. A failed
construction does not imply the avoidance sequence lacks a representing
measure. Useful partial theorems preserve their actual quantifiers and
do not reset the full-target failure counter. No novelty is claimed.
