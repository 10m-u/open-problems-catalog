# Independent review of the simple-root and sharp-length argument

13 October 2026. Same retained agent, no extra proof search. I read
[SIMPLE-ROOTS.md](../eulerian/SIMPLE-ROOTS.md) and the primary
[Savage–Visontai paper](https://arxiv.org/html/1208.3831), Section 2. The
all-size mathematical argument passes review for B3C-Q07 and B3C-Q06;
publication priority and external peer review are not asserted.

The published input has the required orientation, not merely unordered
compatibility: Lemma 2.5 converts compatibility of both (f_i,f_j) and
(xf_i,f_j) into \(f_i\) interlacing \(f_j\) when \(i<j\). The recurrence
and Theorem 2.3 preserve these two properties. Theorem 2.7 supplies prefix
interlacing for arbitrary positive denominator vectors. No monotonicity
of their denominators is part of those hypotheses.

At a point where both refinements are nonzero, the number of roots to its
right is nondecreasing with refinement index, and changes by at most one
over the entire list. This implies at most one sign change, even if some
intermediate refinements vanish. If the last refinement has a simple
\(k\)-th largest root \(z\), every earlier refinement that is nonzero at
\(z\) has exactly \(k-1\) roots to the right. If its last root is repeated,
the two equal consecutive roots force each earlier refinement to vanish
there. These observations justify the endpoint-root claim including
degree differences and repeated-root cases.

At a root of the total, the induction hypothesis makes \(f_0(z)\ne0\).
The last refinement must then be nonzero and of opposite sign. Every
proper prefix sum has the strict sign of \(f_0(z)\): before the sole sign
change it is a nonzero signed sum, and afterward it is the negative of
the remaining tail, which includes the nonzero last refinement. Thus
zeros among intermediate refinements create no equality loophole.

I independently recounted the appended weights:

\[
\#\{j: \lceil ja/b\rceil>i\}=b-1-\lfloor ib/a\rfloor.
\]

At \(z<0\), their increments are nonnegative and their total increment is

\[
(1-z)\lfloor(a-1)b/a\rfloor>0\qquad(a,b\ge2).
\]

Summation by parts therefore gives a nonzero new polynomial at every old
root. Weak prefix interlacing upgrades to simplicity: two coincident new
roots would trap a shared old root. This applies whether the degree stays
the same or increases by one. Constant term one excludes zero; positive
coefficients exclude positive roots. The degree-zero starting case and
the one-entry linear base case are both covered.

For the length corollary, trailing/leading units contribute no ascents,
and a unit separator resets the next block to numerator zero. Therefore
the displayed block factorization is exact. A nonempty block with all
denominators at least two has positive degree. If its polynomial divides
\((1+ux)^d\), simplicity forces its degree to be one. Exactly \(d\) such
blocks, at least \(d\) nonunit entries and \(d-1\) separators are necessary;
the alternating explicit vector attains the bound. The full colored
classification Q1262 remains separate and unresolved by this argument.

This review establishes the mathematical proof obligations. Bounded
checker coverage is a separate receipt and is not the source of the
universal claims.
