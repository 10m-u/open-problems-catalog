# Review of the first two returned B2 rounds

Reviewed 13 October 2026 from the complete submitted manuscripts, result ledgers,
source notes and copied checkers. The first two rounds pass at their stated scopes.
This is an internal mathematical review and replay, without external peer review
or a claim of worldwide priority. The finite checks support the arguments; they
do not prove their unrestricted dimensional statements.

## Midpoint partitions

The first round combines Fourier density increments with weighted affine avoidance.
The random affine-subspace argument first bounds the probability of meeting any of
the covering cosets by M p^(-s), then conditions a nonnegative cost on avoidance.
Its loss is therefore at most 1/(1-M p^(-s)); independence of cost and avoidance
is unnecessary. The covering result used is the established bounded-torsion PFR
theorem: [Gowers–Green–Manners–Tao, Theorem 1.1](https://arxiv.org/html/2404.02244v2)
provides M=(2k)^(O(p^3)) cosets of a subgroup with size at most |A|.

In the density-increment phase, Parseval and the forbidden-midpoint condition give
the largest relevant Fourier coefficient at least (1-a)/k. The selected hyperplane
increases remainder density by a factor at least 1+1/(2k). In the clearing phase,
one removes a color at a time. The final selected color density is at most 2 tau,
which is smaller than p^(-s), so the quotient has enough dimensions for the
avoidance step. This also resolves the small-ambient-dimension case. Summing the
increment and clearing costs proves the displayed min(n,T+ks) bound, hence
O_p(k(log(2k)+log(1/alpha))) codimension. It improves the stated quadratic bound
in [Kościuszko, Theorem 3 and Problem 4](https://arxiv.org/html/2610.11847v1).
The exact extremal function and the logarithmic gap remain open.

The block-zero coloring is admissible because two points with opposite first
nonzero entries cannot share a color when their midpoint would enter the
remainder. Every affine subspace in the remainder loses at least one dimension
in each independent block; the displayed affine slice attains n-k. This is a
construction within the source's already-known linear-loss direction.

The second round's line-free two-color classification follows from the plane
case and incidence counts, rather than extrapolation from the enumerator. Three
noncollinear remainder points force incompatible colors on their pairwise
midpoints. Plane caps thus have sizes 0,1,2,4, with every four-cap a parallelogram.
In three dimensions the point, pair and triple incidence moments, together with
the parallel-plane bound s<=12, again allow only 0,1,2,4. Four noncoplanar points
would contradict this restriction, giving the all-dimensional classification.

Full-fibre inheritance chooses one colored representative per nonfull fibre;
a midpoint over a full remainder fibre yields the required contradiction.
It does not preserve density. Along a maximal-flat direction, the full-fibre
quotient is line-free and consequently has 1,2,4 points. Ambient extension reuses
colors on opposite nonzero quotient pairs, so does not require new colors.
These facts prove f(1,2)=f(2,2)=f(3,2)=0 and f(4,2)=1 at density 1/10, and the
k+2 dimensional-loss construction under its displayed n and k conditions.

## Entropy

Both entropy certificates use exact integer convolutions and rational bounds for
logarithms. The atanh expansion has a geometric remainder bound; all subsequent
rounding is outward. The denominator interval is positive, so the ratio endpoints
use the correct monotone division. Replaying certifiers in separate verification
directories reproduced their certified intervals. The eight-point law gives
1.4051809660756335725451283471012647256861 < rho
< 1.4051809660756335725451283471012647256862. The twelve-point law strengthens this to
1.4051810329220149462009831947934829507300 < rho
< 1.4051810329220149462009831947934829507301.
Shifting supplies positive integer support. Independent digit copies in base 16
preserve sums, differences and their entropies, giving arbitrarily large entropy.

For the boundary variation, newly populated sum and difference sites contribute
2u_plus and 2u_minus to the epsilon log(1/epsilon) coefficients; the new input
atom contributes one. Differentiating the quotient produces precisely
[2u_minus-1-rho(2u_plus-1)]/Delta_plus. Outside (A+A-A)\A both u's equal one, so
the leading term is negative for rho>1. This is a necessary finite candidate
screen and is not sufficient for optimality. The submitted sparse three-point
negative control makes that limitation concrete.

For a fully occupied arithmetic progression with at least three support points,
the two adjacent-candidate coefficients sum to
2(rho-1)(1-p_0-p_N)>0. The asymmetric two-point case is handled separately;
the fair case has rho=1. The endpoint-mass construction z=2b-a similarly gives a
positive coefficient when an endpoint has mass at least 1/2, except the excluded
fair two-point case. These are nonattainment criteria for the specified finite
laws, without a characterization of all possible extremizers.

The imported Q4660 locator calls this Conjecture 1.10. In the primary source,
[Li, Section 8](https://arxiv.org/html/2607.29042v1), the sum–difference constant is
discussed separately; Conjecture 1.10 concerns sum–product. The submitted originals
and catalog source statements remain preserved; the correction is recorded here.
Neither round settles Q4659 or the exact constant in Q4660. The upper bound two
is unchanged.

## Reproduced controls

Round 1 passed 282,339 labelled plane partitions, 29,706 admissible density-increment
controls, 285,184 cover/avoidance pairs, 6,684 weighted checks, the rational loss
controls and eight affine-block construction cases. Round 2 passed its plane-cap,
two-color, quotient, support-boundary and exact entropy controls. The three
checkers in each round ran from copied sources; commands, hashes and logs are in
the adjacent round1/REPLAY.json and round2/REPLAY.json. All submission files are
retained unchanged. The historical B2 run and its five-failure counters are also
unchanged; these are later external continuations.
