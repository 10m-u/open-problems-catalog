# Domination ULC and symmetric interval APP: failed proof architectures

13 October 2026. Exact targets: Q164 and B3C-Q01. The October 7
[interval report](../../b3-continuation-2026-10-07/compositions/REPORT.md)
was read in full, including its conditional-APP reduction, all-size laminar
case, support lemma, bounded exhaustive lemma, and failed one-bit matching.
Those results remain intact. No old matching experiment or larger parameter
sample is counted as a fresh attempt.

I pursued the sufficient proof mechanisms below and worked out their precise
obstructions. Two mechanisms are shared by the targets; the others have
different contracts. All are failures to solve the full targets, not
counterexamples to those targets. Each fifth failure stops only that problem.

## Shared stronger-structure routes

### R: real-rooted rank polynomials

Real-rootedness of the complete rank polynomial would imply the required
binomial-normalized inequalities by Newton's inequalities. This would prove
Q164 directly and imply APP for every symmetric interval family. It fails
for actual objects in both classes, rather than merely for a generic operator.

For the five-vertex path, the domination polynomial is

    D_5(x)=x^2(3+8x+5x^2+x^3).

The cubic has discriminant -31 and therefore a nonreal pair. The stronger
real-rooted theorem cannot be used to close Q164. The polynomial itself
satisfies ULC; its nonreal roots do not refute the target. Real-rootedness of
the parity polynomials in Q165 has a different contract.

For B3C-Q01 take six coordinates and the single full-interval band
|2|x|-6|<=2. Its rank polynomial is x^2(15+20x+15x^2), whose quadratic
discriminant is -500. It satisfies the central inequality with equality,
3*20=4*15. Thus real-rootedness of these symmetric interval rank polynomials
is also an invalid universal sufficient structure.

### L: multivariate Lorentzian homogenization

A second route was to prove Lorentzianity of the squarefree multivariate
rank polynomial after homogenizing with one extra variable. Such a theorem
would yield the desired normalized diagonal inequalities, but requires
M-convex support. The support requirement fails explicitly.

For the five-vertex path, complements of dominating sets are precisely
sets containing none of the three minimal neighborhood circuits
{1,2}, {2,3,4}, {4,5}. Take I={1,3,4}, J={2,4}. Both complements are allowed,
but no element of I\J can augment J: adjoining 1 creates {1,2}, adjoining 3
creates {2,3,4}. The associated domination supports are S={2,5} and
T={1,3,5}. In total degree five, the homogenized exponent vectors are
x_0^3*x_2*x_5 and x_0^2*x_1*x_3*x_5. Exchanging the excess x_2 from the
first vector to either deficient coordinate x_1 or x_3 gives {1,5} or
{3,5}, respectively, neither of which dominates. Coordinate x_0 is not
deficient. Thus the actual homogenized support is not M-convex, preventing
this Lorentzian proof architecture.

For B3C-Q01 use the symmetric interval equations
x_1+x_2=x_2+x_3=x_4+x_5=x_5+x_6=1. The rank-three supports are exactly
010101 and 101010. No single basis exchange between them preserves the
equations, so the homogeneous middle slice already fails M-convexity.
This reuses the old family's description to test a different proposed
Lorentzian support invariant; it does not recount the old one-bit matching
failure as a new matching attempt. Rank ULC can hold despite these support
obstructions, as the checker confirms.

### P: nonlocal prefix averaging and normalized multiplicities

The earlier failed matching changed one bit. I instead tried an explicit
nonlocal height transformation. For x and y write h_j=sum_(i<=j)x_i and
g_j=sum_(i<=j)y_i; round (h+g)/2 down and up coordinatewise, then take
successive differences to obtain two binary words. Integer interval bounds
are preserved under each rounding, so this is a valid feasibility mechanism.
At ranks q-1,q+1 both output ranks are q.

It loses too much multiplicity to supply a direct normalized injection.
For y=1-x the average height is always j/2. In dimension six all fifteen
rank-two words of the unconstrained cube, paired with their complements,
map to the single ordered central pair (010101,101010). This is not an
injection from antipodal rank-two pairs to central pairs and provides no
4-to-3 normalized comparison. The words are actual feasible interval
examples, not an enlarged noninterval class. An additional reversible label
system with a uniform fiber bound is the missing obligation.

For Q164 this leaves the all-size conditional-APP lemma used for path powers
unproved, and the cycle case still needs its own reduction. For B3C-Q01 the
missing multiplicity inequality is the full target itself; mere feasibility
of midpoint rounding does not settle it.

## Q164-specific routes

### D: direct ULC induction along the domination recurrence

For ordinary paths, D_n=x(D_(n-1)+D_(n-2)+D_(n-3)), n>=4. I tried to
make ULC of the preceding three rank sequences the induction invariant.
The recurrence does not preserve that invariant generically even when the
three sequences have consecutive support and the correct ambient orders.
At n=4 use 10x^2+x^3, 10x+x^2, 10+x at ambient orders three, two and one.
All have full degree, consecutive support, and ULC coefficients; their output
10x+11x^2+11x^3+x^4 fails ULC at k=2, since 4*11^2<9*10*11.
Thus a proof using only those three
ULC hypotheses cannot close. The actual consecutive path polynomials
need an additional cross-sequence comparison, uniformly in n; no such
invariant was proved. Arbitrary powers and cycles remain beyond this recurrence.

### C: unroll a cycle and recombine conditioned linear intervals

After fixing coordinates around a cut, circular neighborhood conditions
become linear interval bounds. This suggests proving each cut state ULC
and then summing the state polynomials to prove the original cycle ULC.
The final preservation lemma is false. Already one conditioned coordinate
with two residual coordinates can have ULC residual polynomials
(1+x)^2 and x^2; unconditioning gives (1+x)^2+x*x^2. Its ambient-order-three
counts are (1,2,1,1), failing the k=2 inequality 2<12.

This is a counterexample to generic cut-state recombination, not the
domination states of an actual cycle. A full cycle proof must exploit
relations between the actual boundary states, or prove circular APP
directly. The all-size linear interval theorem, even if obtained, would
not by itself supply this additional lemma.

## B3C-Q01-specific routes

### A: preserve APP by intersecting symmetric constraints

I tried an induction adding a band at a time while retaining only central
APP or normalized ULC of the intermediate symmetric family. Those properties
are not preserved by generic symmetric-family intersection. On four bits set

    F={0011,1100,1000,0111}, G={0101,1010,1000,0111}.

Each family is complement invariant and has counts (0,1,2,1,0), satisfying
normalized ULC and APP. Their intersection is {1000,0111}, with counts
(0,1,0,1,0), violating 2*c_2>=3*c_1. These two control families are not
asserted to be interval-band intersections. Their role is to disprove the
generic property-preservation lemma that the attempted induction requires.
A valid induction must track an additional geometric invariant of crossing
intervals, rather than just APP of the preceding family and the new predicate.

### V: cycle-lemma averaging of linear words

The normalization (q+1)/q suggests marking a zero and rotating a word to
transfer the extra unit to the central rank, with counts handled by cyclic
orbits. I tried to justify that averaging by rotation invariance of the
feasible set. Arbitrary linear interval bands break that invariance.
For six bits with x_1+x_2=x_2+x_3=1, the central word 010011 is feasible,
but its left rotation 100110 violates the second equation. The rotated
constraint system is a different target family. Thus a cycle-lemma orbit
count cannot act inside a fixed arbitrary H by this rule. A transformation
that respects the endpoints and every crossing interval would be needed;
no such orbit construction was obtained.

## Per-target attempt order and stopping record

<a id="q164-a1"></a> Q164 A1: R, actual real-rootedness obstruction.

<a id="q164-a2"></a> Q164 A2: L, actual homogenized support obstruction.

<a id="q164-a3"></a> Q164 A3: D, the exact recurrence lacks generic ULC closure.

<a id="q164-a4"></a> Q164 A4: P, feasible nonlocal averaging loses normalized multiplicities.

<a id="q164-a5"></a> Q164 A5: C, cut-state ULC does not survive generic recombination.

<a id="b3c-q01-a1"></a> B3C-Q01 A1: R, actual global-band real-rootedness obstruction.

<a id="b3c-q01-a2"></a> B3C-Q01 A2: L, actual middle-slice support obstruction.

<a id="b3c-q01-a3"></a> B3C-Q01 A3: P, antipodal prefix averaging has fifteen-to-one collapse.

<a id="b3c-q01-a4"></a> B3C-Q01 A4: A, generic symmetric APP intersection fails.

<a id="b3c-q01-a5"></a> B3C-Q01 A5: V, a fixed interval family does not contain its cyclic orbits.

Both problems have five consecutive substantive full-target failures and
are stopped under the user's rule. Their conjectures remain unresolved.
The [exact checker](check_routes.py) and [receipt](CHECK-RESULTS.json)
verify the stated obstructions and 100 unweighted path/cycle-power ULC
examples through 14 vertices. Those examples extend finite evidence; they
do not prove an arbitrary-size assertion or reset the failed-route counters.
