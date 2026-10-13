# Independent Q1262 E06 review

On 2026-10-13 I accept E06 as a distinct fifth failed full-target route.
The earlier rejection of E01 stands. The accepted count is E02, E03,
E04, E05, E06; Q1262 is unresolved and stops under the five-failure rule.

I read [DILATION-FAMILIES](DILATION-FAMILIES.md), the updated attempt
packet, its checker and receipt, and the earlier independently reviewed
degree-compression proof dependency. The claimed forward closure and
infinite family are correct; they are partials, not a classification.

## Forward dilation

The primary [Deligeorgaki--Han--Solus Corollary 2.2 and Section 4.1](https://escholarship.org/content/qt135937h5/qt135937h5_noSplash_af6056425c67947c0d921d43ba376183.pdf)
provide the scaled-simplex and lecture-hall Ehrhart interpretations used
here. If len(s)<=M, prefixing M-len(s) ones preserves the numerator:
the added inversion coordinates are all zero and the first remaining
ascent condition is still e_1/s_1>0. Both polytopes then have dimension M.
Equality of numerators therefore identifies their lattice-count
polynomials with denominator (1-x)^(M+1).

Scaling all colors by t replaces the first lattice count L(u) by L(tu).
Scaling every padded lecture-hall denominator by t gives precisely the
geometric dilate tP, since its ratios z_i/(t s_i) obey the original
ordered inequalities. Its lattice counts are also L(tu). This proves
the forward lemma for every positive integer t. Leading units must be
scaled too: after dilation they are genuine coordinates. Equality of
numerators at unmatched dimensions would not suffice, and the packet
explicitly makes no such claim.

## Exact family and exclusion

For E_(a,b), the coefficient of x² counts pairs of positive coordinates
with e_1/a<e_2/b. Reflection (e_1,e_2)->(a-e_1,b-e_2) exchanges the
strict inequalities. Exactly gcd(a,b)-1 positive pairs have equal ratios,
so its x² coefficient is [(a-1)(b-1)-gcd(a,b)+1]/2. The constant term
is one, and the total number is ab; the displayed x coefficient follows.
This includes a=1 or b=1 by zero trailing coefficients.

For the two singleton symbols with colors c,d, L(u)=(cu+1)(du+1)
and multiplication of its series by (1-x)³ gives

    A_(1,1)^(c,d)=1+(cd+c+d-2)x+(cd-c-d+1)x².

Thus c=12t,d=15t yields the claimed row, and a=8t,b=45t has
gcd(a,b)=t and the same row for **every** positive integer t.
No induction from finite t values is needed.

For c=4,d=5 the numerator is (1,27,12), with volume 40 and degree two.
The earlier all-length compression theorem reduces existence to the
22 canonical factor/unit strings of length at most three. I rebuilt
these strings independently and counted their literal inversion
sequences; none has the target row. This is an all-length exclusion
conditional on that already reviewed theorem, not on an arbitrary
computer cutoff.

## Count and scope

E06 tries a specific structural equivalence: normalize the common color
gcd, decide the primitive input and recover membership by common dilation.
The actual primitive point (4,5) is unrepresentable, whereas every point
(12t,15t) is representable. This disproves the required inverse implication.
It leaves classifications tracking arithmetic of the multiplier open.

Unlike E04, this route scales **all** colors by the same number with
multiplicities fixed and proves a valid forward lemma before testing
the inverse. E04's failed construction instead scales prescribed
denominator blocks differently. E05 changes a multiplicity and appends
a denominator. E02/E03 concern scalar conditions and product construction.
The finite candidate machinery is shared prior evidence and counts zero
by itself; the newly worked dilation equivalence is substantive and
distinct. It supplies the replacement fifth failure without restoring
the rejected finite-search E01 count.

[check_dilation_review.py](check_dilation_review.py) imports only the
retained agent's prior independent literal enumerators, not the root's
implementation. [DILATION-REVIEW-CHECK.json](DILATION-REVIEW-CHECK.json)
records the 22 independently rebuilt candidates, 1,296 literal
two-coordinate formula controls, and direct colored-word/inversion/
Ehrhart agreement for t=1..8. Those finite checks verify arithmetic and
witnesses; the written identities and geometric proof give all-size scope.
