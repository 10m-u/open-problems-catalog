# Q1366: unimodality of classical permutation-pattern intervals

Exact target: every interval [sigma,tau] in classical subsequence containment
has a unimodal sequence counting **distinct** permutations at each length.
The primary [McNamara--Steingrimsson, Conjecture9.4](https://arxiv.org/html/1305.5569)
and [Vatter, Conjecture2.2](https://arxiv.org/html/2602.16355v2) use this
scope. The consecutive-pattern theorem does not apply. The earlier B3
return enumerated every top of length<=7 and already recorded a failure
of the stronger log-concavity assertion. Those replays count zero here.

Five proposed distinct worked full-target failures follow; independent
count review remains pending. New all-size partial proofs are in
[LAYERED-INTERVALS](LAYERED-INTERVALS.md). Partial results reset no counter.

<a id="q1366-a1"></a>
## A1: construct a valley using longer interacting blocks and random tops

Construct actual intervals beyond the initial length-seven bound: 80
distinct tops of lengths8--12, consisting of two decreasing layers with
every split, even-then-odd interleavings, and eight deterministic seeded
random permutations at each length. For each top, take every distinct
contained nonempty bottom of length<=4. This gives1573 actual intervals.
Recursive deletion is independently compared with literal position-subset
standardization for all80 tops. Every coefficient of every row is counted;
none has a decrease followed by an increase. Full rows remain in
[PATTERN-PROBE](PATTERN-PROBE.json).

This is one failed actual valley construction, not one attempt per family
or interval. The structured two-layer case subsequently has an all-size
partial proof, but the interleavings and generic overlapping occurrences
have only these bounded controls. The unresolved obligation is an
arbitrary-top theorem or an actual valley. No old length<=7 enumeration
is counted in this route.

<a id="q1366-a2"></a>
## A2: inject the smaller adjacent rank through containment covers

Try to build a unimodal chain decomposition: before a rank peak, inject
each rank into the next by a containment cover; after a peak, inject in
the reverse direction. The resulting chains would give the required
rank inequalities. In particular, two tied adjacent ranks require a
perfect matching in their cover graph regardless of which side of the
peak they occupy. That necessary matching fails in an actual interval.

For bottom213, top2574613, the rank row is [1,3,7,7,1]. The following five
length-five patterns are in the interval:

    13524, 14352, 24351, 35241, 43512.

Their complete length-six upper-neighbor set inside the interval is

    146352, 246351, 254613, 463512.

Literal containment tests certify both memberships and completeness;
there are five vertices and only four neighbors. Hall's condition fails,
so no perfect matching pairs the tied ranks. The exact rank row remains
unimodal; no counterexample to Q1366 is asserted. The stronger cover-chain
certificate cannot apply uniformly. A proof may instead compare counts
using maps outside the cover relation, nonintegral weights or a different
global argument. The auxiliary smaller-top matching search is a new
lemma test, not another rank-valley construction or an old-data replay.

<a id="q1366-a3"></a>
## A3: descend a Boolean chain proof by dividing occurrence fibers

Every position subset of a fixed top standardizes to a pattern, but the
target counts the quotient patterns only once. Try to descend Boolean
rank counts or chain maps by a rankwise common occurrence multiplicity.
A valid uniform-fiber lemma would justify dividing the Boolean data and
transporting the rank argument without retaining individual embeddings.

The all-size unique-inversion family in LAYERED-INTERVALS gives exact
fibers. For top=iota_p direct-sum21 direct-sum iota_q and bottom21, each
actual intermediate is determined by (u,v), and has binom(p,u)binom(q,v)
representing subsets. At p=q=2, top124356, the actual interval row is
[1,2,3,2,1] while the occurrence cube row is [1,4,6,4,1]. Three patterns
at the same middle rank have fiber sizes1,4,1. Hence a single rankwise
division or unweighted quotient of Boolean chains loses essential data.

The grid model proves this family for every p,q, and the full fiber
formula identifies exactly what a weighted replacement must retain.
No such globally compatible weighted chain rule was obtained for
arbitrary top/bottom. This is a failed quotient-fiber inference, distinct
from the actual-cover matching route. It is also different from A4's
coverage failure: here **every** occurrence contains the same unique
bottom embedding and coverage is perfect; unequal fiber weights alone
block the attempted reduction.

<a id="q1366-a4"></a>
## A4: represent the whole interval above a fixed bottom occurrence

Try to choose one canonical occurrence E of the bottom, then identify
the interval with the patterns of supersets of E. The remaining positions
give a Boolean cube, after which one could seek a chain/product proof.
This requires every intermediate pattern to have some realization
containing E; it does not hold, independently of fiber weights.

Take bottom21, top2143, and the lexicographically first occurrence E={1,2}
(one-based positions). Its supersets give rank row [1,1,1]; every
length-three pattern from such a superset is213. The actual interval also
contains132, realized using one entry of the first layer and the entire
second layer, and has row [1,2,1]. There is no realization of132 containing
E. More generally in top=21 direct-sum...direct-sum21 with k>=2 layers,
the first fixed inversion yields only213 at the next length, whereas the
full interval contains both132 and213. This proves an all-size failure
of that coverage lemma, rather than only a convention mismatch.

Multiple occurrence cubes could repair coverage, but then their overlaps
and distinct-pattern identifications must be controlled. A3 handled
unequal fibers even under unique occurrence; this route fails earlier,
when a fixed occurrence cannot represent all target objects. These are
different proposed sufficient contracts, although both begin with
position subsets. Neither disproves the conjecture or rules out a more
careful occurrence-based proof.

<a id="q1366-a5"></a>
## A5: close induction under deletion unions and interval intersections

Every proper pattern of top tau is contained in a permutation formed by
deleting one entry of tau. Thus the desired rank polynomial is a union
of the lower intervals below these deletions, followed by the single
top term. Try induction on top length and an inclusion--exclusion or
unimodal-gluing lemma. Such an induction needs intersection structure
and quantitative inequalities, not merely the individual rank profiles.

For bottom1 and top2413, delete the first or last entry. The resulting
tops312 and231 each give an interval with row [1,2,1]. Their intersection
is {1,12,21}, with two incomparable maxima. It is not an interval with
one top, so induction over intervals is not closed under this actual
operation. All four deletions give distinct nonmonotone length-three
tops; each common intersection has those same two maximal patterns.
The actual union plus top has row [1,2,4,1] and is unimodal.

Even knowing unimodality for each piece and its intersection is too weak
as a scalar gluing hypothesis. Formal bounded nonnegative rank rows
A=B=[1,3,3,3,1], H=[1,1,3,1,1] are individually unimodal and H<=A,B
coefficientwise, but A+B-H=[1,5,3,5,1] has a valley. These rows are **not**
claimed permutation intervals. They refute only the proposed scalar
closure lemma. The actual intersection shows why one cannot avoid that
obligation by applying the same interval induction to a unique top.

The general deletion identity is valid, but no sharper overlap inequality
was derived that preserves unimodality for arbitrary top. This is a
failed recursive-gluing proof, distinct from A4's single-embedding
coverage, A3's fiber division and A2's actual-cover matching.

## Pending disposition

All-size equal-layer-count intervals, all nonempty-bottom intervals
below at most two decreasing layers, and the unique-inversion grid
families are proved log-concave. The full catalog conjecture remains
unresolved. The five proposed full-target routes stop here pending
independent mathematics and honest count review; no sixth route is
started unless a proposed count is rejected. Checks are in
[PATTERN-ROUTES-CHECK](PATTERN-ROUTES-CHECK.json).


## Accepted independent disposition

The retained-agent and root reviews accept five distinct failures and the scoped all-size partials. The original paper already covered all tops through length8: those14 tops and240 intervals here count as old-range controls only. The66 tops and1333 intervals at lengths9--12 supply the fresh part of A1. Q1366 stops unresolved; no sixth route. See Q1366-INDEPENDENT-REVIEW.md.
