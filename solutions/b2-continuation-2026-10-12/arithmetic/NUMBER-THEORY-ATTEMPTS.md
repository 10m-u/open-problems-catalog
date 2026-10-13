# Powerful progressions, quadratic orders and shifted-prime divisors

Root took these five unstarted targets while the retained agent's same handle
was awaiting initialization. A connection interruption is not a failed solve
attempt. Cached primary texts read: van Doorn, §§3–5; Pollack, introduction
and §4 of maximallyelastic.pdf; Fan–Pollack, the final remark of
AMS-UMI-elasticity.pdf; Fan–Pollack2510.14167, introduction and moment/maximal
order discussion. Primary arXiv pages and current author sources were checked.
The supplied cross-link2607.08985 concerns two prime squares, not the shifted
prime divisor function; it supplies no closure of Q2816/Q2817.

## Positive scopes and exact computation

For Q2814, the **elasticity∞** branch is known for every real quadratic K:
the source's Halter-Koch input says an order has infinite elasticity exactly
when its conductor contains a split prime. Fix such a prime p; all conductors
p^j, j≥1, are distinct witnesses. This is an unconditional sourced subcase,
without an independent reproof of that factorization theorem. Finite
prescribed elasticities in each field are the unresolved part.

For Q2817 there is an exact finite identity, for integer X≥1:

    M_k(X) = X^−1 Σ_{p₁,...,p_k≤X+1}
                         floor[X/lcm(p₁−1,...,p_k−1)].

The sum runs over ordered prime tuples, allowing repeats. Expand ω*(n)^k
and interchange the two finite sums; membership of every p_i−1 in the
divisors of n is equivalent to their lcm dividing n. This identity is useful
for exact checking and exposes the correlated-prime counting problem; it is
not a new asymptotic formula or novelty claim.

<a id="q2616-a1"></a>
## Q2616 A1 — Promote the Pell progression into consecutive-powerful counts

The primary constructs x²−7³y²=2, giving
((x−2)²,(x−1)²,x²−2), a three-term powerful progression with two squares.
The cached plain text's73 means7³, verified against the primary HTML.
The exact seed is(x,y)=(11427,617). Its exponential recurrence gives Θ(log X)
candidates below X, but the progression need not consist of consecutive
powerful numbers. The checker lists all intervening powerful values at the
seed, explicitly rejecting its consecutivity. No positive proportion of the
recurrence is proved accepted, and this construction says nothing about the
zero- or one-square classes. **Failed consecutive/logarithmic transfer.**

<a id="q2616-a2"></a>
## Q2616 A2 — Scale one consecutive example into infinitely many

Multiplication by a square preserves powerfulness and the arithmetic
progression, but not the absence of other powerful numbers in the gaps.
Scaling(1728,1764,1800) by9 gives(15552,15876,16200), but the powerful
square125²=15625 lies strictly between the first two entries. This exact
witness disproves the proposed universal scaling-preservation lemma.
Successful individual multipliers would still require an infinite acceptance
argument and controlled size growth. **Failed square-scaling infinitude route.**

<a id="q2616-a3"></a>
## Q2616 A3 — Apply an interval-density theorem along the Pell subsequence

The source discusses the density of integer square intervals having prescribed
powerful occupants. A positive-density set of all integer endpoints can miss
an exponentially sparse Pell sequence entirely. The necessary estimate is
equidistribution of that specific recurrence against simultaneous fractional
parts x/m^(3/2), with an unbounded collection of squarefree m. Neither
ordinary endpoint density nor fixed finitely many coordinates controls this
intersection. **Failed density-to-sparse-recurrence proof.**

<a id="q2616-a4"></a>
## Q2616 A4 — Turn the independent gap heuristic into two-sided bounds

Powerful numbers have unique form a³b² with a squarefree. Treating their local
occupancy events as independent gives the source's logarithmic heuristic,
but different a share algebraic and congruence constraints, and the two gaps
must exclude *every* other powerful value. Bounding one expected count does
not prove a positive acceptance probability or concentration in each square
class. No uniform joint-correlation/error estimate was obtained.
**Failed independent-occupancy proof.**

<a id="q2616-a5"></a>
## Q2616 A5 — Infer growth and missing square classes from exact finite enumeration

Generate every a³b²≤10⁹, with a squarefree, sort the unique values and test
each consecutive triple for equal differences. This is a complete bounded
algorithm, checked independently against prime-factor classification on a
smaller prefix. It neither proves infinitely many hits in any class nor
supplies a logarithmic upper bound beyond its last value. The source's larger
reported table likewise does not establish such an asymptotic. Also no triple
of consecutive powerful values can have three squares: it would be three
consecutive square values, whose two gaps are unequal. That elementary fact
explains the index set{0,1,2}, without resolving any of those classes.
**Failed finite growth classification.**

<a id="q2814-a1"></a>
## Q2814 A1 — Use the general conditional maximal-elasticity theorem unconditionally

Pollack's Proposition4.2 proves the desired all-field statement assuming
GRH and a zero-density hypothesis for quadratic-field Wieferich primes.
Both inputs remain unproved in this run. Even GRH alone is explicitly
insufficient for the general source proof, unlike its special K=Q(√2)
theorem. The full conjunction cannot be discarded. **Failed unconditional theorem import.**

<a id="q2814-a2"></a>
## Q2814 A2 — Obtain all finite values from the split-prime construction

The unconditional conductor family p^j above realizes∞ at every j.
It never realizes any finite prescribed e. The fact that the infinite
elasticity branch is solved cannot close the remaining half-integer values.
Changing the exponent j preserves the same obstruction rather than tuning a
finite ratio. **Failed all-value construction; sourced∞ branch retained.**

<a id="q2814-a3"></a>
## Q2814 A3 — Force maximal unit index by a finite Chebotarev condition

For an inert prime, the unit residue lies in a group of size dividing p+1;
the source's ring-class formulas use its actual index. Requiring full order
means excluding missing prime factors of p+1, an unbounded moving collection
of Kummer/Frobenius restrictions. Chebotarev for any fixed finite collection
does not enforce all of them. The source's GRH proof controls an infinite
sieve tail, and its general-field lifting also avoids Wieferich primes.
No unconditional uniform tail estimate is produced. **Failed finite-Frobenius full-index proof.**

<a id="q2814-a4"></a>
## Q2814 A4 — Inherit half-factoriality from the maximal-order UFD

The hypothesis h_K=1 makes O_K a UFD, with elasticity1. It does not make
every suborder half-factorial: in this very field, a split-prime conductor
has elasticity∞ by the source theorem above. Inclusion changes irreducibles
and factorization lengths. Thus the proposed inheritance would contradict a
known family inside the exact scope. **Failed UFD-to-all-orders transfer.**

<a id="q2814-a5"></a>
## Q2814 A5 — Repeat one finite-elasticity witness by multiplying its conductor

Given a conductor f realizing finite e, multiplying by any new split prime
p makes the conductor divisible by a split prime and forces elasticity∞.
So even a harmless-looking independent prime multiplier fails to preserve
the desired finite value. Restricting to inert primes or powers requires
new control of unit indices and class groups; neither multiplicativity of
elasticity nor a preserving infinite family is proved. **Failed conductor-multiplier infinitude.**

<a id="q2815-a1"></a>
## Q2815 A1 — Use primitive-divisor existence in the Lucas sequence

A primitive prime factor, when guaranteed, grows at least with its rank of
appearance m. The target requires p>v_m^δ, exponential in m because
v_m grows like ε^m. A linear rank lower bound is therefore far too small.
Primitive-divisor existence also does not itself impose inertness.
**Failed primitive-factor size proof.**

<a id="q2815-a2"></a>
## Q2815 A2 — Reverse the inert-prime Chebotarev construction

Every sufficiently good inert p divides some v_m with m≤p+1: Frobenius
interchanges the two embeddings, so ε^(p+1)=N(ε)=±1 modulo p, a scalar.
Infinitely many inert p therefore give divisibility pairs. But m≤p+1 is
not m=O(log p), the bound needed to compare p to exponential v_m.
Divisibility in some possibly long index does not give the required large
factor. **Failed inversion of the inert-prime existence theorem.**

<a id="q2815-a3"></a>
## Q2815 A3 — Deduce a large inert factor from coefficient size and congruences

The norm equation u_m²−D v_m²=4N(ε)^m constrains a product, not an individual
prime factor or its splitting type. Large integer size can come from many
small primes or repeated factors. At K=Q(√2), v₇=338=2·13², with13 inert;
its inert contribution already has multiplicity two. This is not an
asymptotic counterexample; it rejects the assumption that the norm/size
identity makes an inert divisor appear to exponent one or dominate v_m.
A uniform lower bound on the largest *inert* factor remains missing.
**Failed norm/size-only factor proof.**

<a id="q2815-a4"></a>
## Q2815 A4 — Use infinitely many inert Pell primes

For K=Q(√2), if v_m/2 is prime and inert for infinitely many m, then every
fixed δ<1 works eventually. The finite examples satisfy this conditional
construction, but even infinitude of Pell primes is unproved here; imposing
inertness adds a restriction. General fields have different recurrences.
An unproved Lucas-prime family cannot close an unconditional all-field
claim. **Failed prime-sequence construction; conditional implication retained.**

<a id="q2815-a5"></a>
## Q2815 A5 — Apply the existing GRH unit-index construction at its current scale

The source proof obtains inert primes with unit-index parameter ℓ(p)
bounded on the scale p^(3/4+η), by forcing a divisor q of p+1 of size about
p^(1/4−η). This is a valuable conditional elasticity construction.
The present large-factor claim needs an index O(log p), a much smaller
scale. Replacing the power bound by that logarithmic one requires a new
prime-distribution argument; it does not follow by choosing η small.
**Failed conditional power-scale-to-log-scale transfer.**

<a id="q2816-a1"></a>
## Q2816 A1 — Match the current upper and lower constants

The elementary comparison ω*(n)≤τ(n), with the maximal-order theorem for
τ, gives the upper constant log2. The primary's unconditional lower constant
is0.6736log2, while its GRH lower constant log((1+√5)/2) is also strictly
below log2. Neither closes the fixed positive gap. **Failed bound matching.**

<a id="q2816-a2"></a>
## Q2816 A2 — Make all primorial divisors into shifted primes

For n equal to a primorial, τ(n) is exponentially large in its number of
prime factors. To transfer that scale to ω*(n), one must show exponentially
many divisors d have d+1 prime, with the desired leading constant. Ordinary
prime counting or Dirichlet's theorem does not count this finite sparse
divisor family. The necessary smooth shifted-prime population estimate is
exactly missing. **Failed primorial/primality transfer.**

<a id="q2816-a3"></a>
## Q2816 A3 — Use n=lcm(1,...,y) to capture all small primes

All primes p≤y+1 satisfy p−1|n, supplying about y/log y witnesses.
But log n is of order y, so the guaranteed count has normalized logarithm
of order (log y)²/y, tending to0 rather than log2. The construction may
have additional shifted-prime divisors, but this simple guaranteed family
does not reach the desired scale. **Failed guaranteed-small-prime construction.**

<a id="q2816-a4"></a>
## Q2816 A4 — Replace shifted-prime divisor counts by divisor counts

Divisor abundance alone is insufficient. For n=2^a, τ(n)=a+1, while
d+1=2^j+1 can be prime only when j=0 or j is a power of two. For j with
an odd factor>1, X^r+1 factors, proving the exclusion. Hence
ω*(2^a)≤2+floor(log₂a). This family is not maximal for τ and is not a
catalog counterexample; it refutes a generic cardinality-proxy lemma.
Maximal-divisor constructions still need their own primality estimates.
**Failed divisor-count-only lower bound.**

<a id="q2816-a5"></a>
## Q2816 A5 — Extract the maximal constant from fixed moments

For any fixed k, the known moment order supplies only a power of log x
as a lower bound on the largest value below x. Markov's upper estimate
gives a power x^(1/k), much too large for the target subpower maximum.
Letting k grow with x would require uniform constants and errors; the
exponent2^k−k−1 itself then grows rapidly. No growing-k theorem is supplied
by results for each fixed k. **Failed fixed-moment maximal-order inference.**

<a id="q2817-a1"></a>
## Q2817 A1 — Upgrade correct moment order to an asymptotic constant

The primary cites M_k(x)≍(log x)^(2^k−k−1) for fixed k. Two-sided
constant bounds do not imply convergence of the normalized ratio;
1+(1/10)sin(log log x) is a positive bounded nonconvergent model.
This is not claimed to be an actual moment ratio. A limiting constant
and a vanishing relative error remain unproved. **Failed order-to-asymptotic transfer.**

<a id="q2817-a2"></a>
## Q2817 A2 — Replace every floor in the exact tuple identity by its argument

For lcm≤X the error per prime tuple is at most1. Summing that error needs
a sharp count of feasible tuples; the crude all-tuple bound is of order
(X/log X)^k, far too large after division by X. Tuples with lcm>X must
also be excluded before making this replacement, since their exact floor
is zero. No uniformly negligible weighted floor error has been obtained.
**Failed unconditional main-term extraction from the exact identity.**

<a id="q2817-a3"></a>
## Q2817 A3 — Model shifted-prime divisibility events independently

The intersection density for p−1 and q−1 is1/lcm(p−1,q−1), rather than
1/((p−1)(q−1)); it includes a gcd factor. For p=3,q=5 these are1/4
and1/8. The all-equal prime diagonal contributes only M₁(x)≈log log x,
also too small for any k≥2. Off-diagonal correlated shifted primes supply
the substantial moment growth; a Poisson model based on the first moment
misses even its correct power of log x. **Failed independent-events/diagonal main term.**

<a id="q2817-a4"></a>
## Q2817 A4 — Sum fixed-modulus prime asymptotics through the gcd expansion

For k=2 use gcd(a,b)=Σ_{d|a,d|b}φ(d). The reciprocal-lcm sum becomes
a sum over d of prime counts p,q≡1 mod d, with size cutoffs and weights.
The moduli grow with X, and the floor/lcm restriction couples the two
primes. A fixed-d prime asymptotic cannot be summed without uniform
weighted errors; large moduli and their correlations remain uncontrolled.
Higher moments have still more coupled divisibility patterns. A proposed
Euler-product constant is not a proof of such error estimates.
**Failed fixed-modulus-to-global correlation asymptotic.**

<a id="q2817-a5"></a>
## Q2817 A5 — Certify C_k from exact finite moment tables

The checker sieves ω*(n) and computes exact integer sums for k=2,3,4
through a declared bound. At small X it independently checks the ordered
prime-tuple floor identity. Ratios to log powers at finitely many X have
no effective asymptotic error or universal limiting-constant certificate.
Larger tables would remain one finite route, not additional solve attempts.
**Failed finite-table asymptotic certification.**

Five substantive routes per target fail. Conditional inputs, candidate Pell
counts, the unconditional∞ elasticity subcase, fixed-moment orders and exact
finite identities retain their stated scopes. None is a full catalog closure.
