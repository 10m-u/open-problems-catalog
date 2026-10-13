# Arithmetic sequences, prime cycles and exact algorithms

12 October 2026. Exact targets and setups are in the parent snapshot.
Each numbered route below is one full-target failed construction or proof.
Restricted deductions and finite checks do not reset a target's counter.
Shared obstacles are disclosed; these are not five impossibility theorems.

Primary readings: MacHale's partition question in the local Kourovka notebook
21.89; Yurkevich's Catalan discussion and Bostan's
[lecture](https://mathexp.eu/bostan/ExpMath19/expmath19-l1.pdf);
the signed Lehmer paper [Integers aa33](https://math.colgate.edu/~integers/aa33/aa33.pdf);
the prime-cycle discussion [2610.10572](https://arxiv.org/abs/2610.10572v1);
the divisors-in-residue-classes thesis and its Chapter 3;
and Uppal's [Sections 9.1–9.4](https://arxiv.org/html/2204.13472).
Local source paths are preserved in QUESTION-SNAPSHOT.json.

## Q2613 — partition numbers dividing factorials

<a id="q2613-a1"></a>

1. **An exhaustive witness search.** Compute p(n) from Euler's pentagonal
   recurrence and n! by successive multiplication; test the exact remainder,
   without factoring p(n). Through n=2000 the last division occurs at39.
   This gives a finite certificate, but neither an unbounded witness nor
   an argument excluding later division. The stopping gap is an upper bound
   on any exceptional n, not computational precision.
<a id="q2613-a2"></a>

2. **An asymptotic size contradiction.** The partition asymptotic gives
   log p(n)=O(√n), whereas log(n!) is of order n log n. Thus p(n)<n!
   eventually. Divisors of n! can be much smaller than n!, so the direction
   needed for a size obstruction is reversed. This candidate proof supplies
   no nondivisibility criterion.
<a id="q2613-a3"></a>

3. **A large prime factor obstruction.** A prime q>n dividing p(n) would
   certify the target at n; for n=40, p(n)=2·3·7²·127 illustrates it exactly.
   The proposed universal proof therefore asks P⁺(p(n))>n for every n>39.
   No such uniform prime-factor theorem follows from the pentagonal
   recurrence or the size asymptotic; replacing it by a typical-factor
   heuristic leaves precisely the universal step unproved.
<a id="q2613-a4"></a>

4. **Ramanujan residue classes as a valuation obstruction.** On classes
   5t+4, 7t+5 and11t+6, the standard congruences force divisibility by the
   corresponding prime. But n! already contains those primes with valuations
   linear in n. A lower bound of one on v_q(p(n)) cannot exceed
   Σ_j⌊n/q^j⌋. This route needs a uniformly excessive valuation, which those
   congruences do not provide.
<a id="q2613-a5"></a>

5. **Induction through the pentagonal recurrence.** Nonzero residues of
   separate summands modulo a prime outside n! need not have a nonzero
   signed sum: cancellation invalidates the proposed invariant. The recurrence
   also refers to earlier indices with potentially different obstructing
   primes. No fixed prime or compatible residue invariant was obtained to
   carry a certificate from all earlier n to the next one.

## Q3715 — odd Catalan numbers

For C_n=binom(2n,n)/(n+1), Legendre's formula gives
v₂(C_n)=s₂(n+1)−1. Thus the relevant indices are n=2^k−1, with k≥9.
Because 5 does not divide n+1, v₅(C_n) is the number of carries in
base-five addition n+n. Consequently the exact target is:
**every 2^k−1 with k≥9 has at least one base-five digit3 or4**.
For an odd integer divisibility by5 is equivalent to last decimal digit5.

<a id="q3715-a1"></a>

1. **The carry reduction and direct exhaustion.** Test the exact base-five
   criterion for k≤5000, checking agreement with direct binomial integers
   at small k. The only carry-free positive k are1,3,5,7,8 in that range.
   The reduction is exact; the proposed global proof fails at extrapolating
   this finite list without a bound on an additional carry-free exponent.
<a id="q3715-a2"></a>

2. **A finite modular cover of the exponents.** Looking only at the first
   J base-five digits cannot suffice: for k divisible by4·5^(J−1),
   2^k−1≡0 modulo5^J. All those inspected digits are zero.
   The uncovered exponent progression survives every fixed J; a proof
   needs a digit at an unbounded position.
<a id="q3715-a3"></a>

3. **Density exclusion.** The integers whose base-five digits are0,1,2
   number about X^(log₅3) up to X, and have density zero. The sequence
   2^k−1 is itself much sparser. Zero density does not imply that its
   intersection with this digit set is finite; the proposed counting
   comparison cannot eliminate even infinitely many sparse hits.
<a id="q3715-a4"></a>

4. **A synchronized automaton intersection.** The digit set is regular in
   base five and the powers-of-two-minus-one set is regular in base two.
   Their numerical comparison is not a synchronous same-base product
   construction. Cobham's conclusion for one set recognizable in both
   independent bases does not decide this intersection. No effective
   bounded cross-base state representation was constructed.
<a id="q3715-a5"></a>

5. **A fixed-term logarithmic approximation proof.** Writing
   2^k−1=Σ_j d_j5^j introduces a number of terms proportional to k,
   with independently varying d_j∈{0,1,2}. A two-term linear-form bound
   controls proximity to one power of five, not this expanding sum.
   Uniformly reducing the surviving digit pattern to boundedly many terms
   is the missing lemma; assuming it would change the exact problem.

## Q3314 — distinct signed primes in a Lehmer factorization

<a id="q3314-a1"></a>

1. **Repair the known repeated-prime witness.** The exact equality
   2(−7−1)(3−1)(3−1)=−7·3·3−1 gives k=2, but repeats3.
   Replacing its final3 by q and preserving k=2 gives
   −32(q−1)=−21q−1, hence q=3 again. This local repair has no admissible
   distinct-prime specialization.
<a id="q3314-a2"></a>

2. **Solve the two-factor construction.** With r=2,
   [(k−1)x−k][(k−1)y−k]=1. Both integer factors are1 or both−1,
   so x=y; in the latter case x=y=1. Thus no two distinct signed primes
   work for any k≥2. This is a proved restricted exclusion, but the
   attempted r=2 solution does not settle r≥3.
<a id="q3314-a3"></a>

3. **Append a prime to a known seed.** If P=∏x_i and D=∏(x_i−1),
   the required appended value is q=(kD−1)/(kD−P).
   For the distinct k=1 seed(−3,5,17), k=2 gives513/257.
   This recursion does not preserve integrality or primality, and it can
   repeat an existing factor. No seed invariant ensuring an admissible
   appended prime was obtained.
<a id="q3314-a4"></a>

4. **Exact signed-prime enumeration.** Enumerate all2–5 element subsets
   of signed primes of absolute value≤51 and test the rational quotient
   (P−1)/D exactly. None is an integer≥2. Finite failure excludes this
   box only; there is no established bound on r or the prime sizes.
<a id="q3314-a5"></a>

5. **Import a positive Lehmer construction.** Distinct positive prime
   factors with k≥2 would already give a counterexample to Lehmer's
   totient conjecture. The integer equation's extra negative signs do
   not produce such a construction automatically: they change both P
   and D, and the known signed examples have k=1 or repeated/composite
   bases. This proposed transfer has no qualifying source witness.

## Q4196 — prime cycles for g(t)=t²−t+1

<a id="q4196-a1"></a>

1. **A finite forward-search construction.** Factor g(p) along a breadth
   first traversal, looking for a return to the starting prime.
   Eight explicit cycles, including7→43→13→157→7, are verified exactly.
   A cap at10^6 on new primes gives only a finite successful subset, not
   a bound ensuring a return for every starting prime.
<a id="q4196-a2"></a>

2. **A decreasing-factor recursion.** Taking the least prime factor of
   g(p) can enter an existing cycle while omitting the start.
   From19 this rule follows19→7→43→13→157→7, so it does not return19.
   Moreover g(7)=43 is prime and increases. An eventual small cycle
   therefore does not prove the requested cycle through p₁.
<a id="q4196-a3"></a>

3. **Construct an incoming edge by Dirichlet.** Since p≡1 mod6, g has
   roots modulo p, and their CRT classes with q≡1 mod6 yield infinitely
   many primes q with p|g(q). The method constructs incoming edges.
   It does not prove any such q is reachable along outgoing factors
   from p. Directed reachability cannot be replaced by an undirected
   connectivity argument.
<a id="q4196-a4"></a>

4. **Close a finite prime-factor set.** A finite set closed under choosing
   one outgoing factor has a directed cycle, by the functional-graph
   argument. Closure containing p can instead put p in a tree feeding
   another cycle. Requiring a cycle through p is precisely the missing
   stronger closure property, as the least-factor19 example shows.
<a id="q4196-a5"></a>

5. **Use repeated residue trials to force a return.** The source's
   Bernoulli model gives two favorable classes modulo p₁, but factor
   choices are deterministic and can revisit an old finite cycle.
   For the least-factor path above there are no fresh trials after
   reaching7. Independence and full residue sampling were not proved,
   so a geometric success heuristic gives no universal finite return.

## Q4585 — seven divisors in one large-modulus class

<a id="q4585-a1"></a>

1. **Augment a certified six-divisor seed greedily.** At N=245784,S=65,
   the complete class1 divisor set is1,66,196,456,2926,12936;
   gcd(N,S)=1 and S³=274625>N. Among all new d≡1 mod65 below S³,
   the smallest lcm(N,d) is983136. Thus this seed cannot gain a seventh
   divisor by augmentation while preserving the threshold.
<a id="q4585-a2"></a>

2. **Scale and duplicate its divisor class.** Multiplying by t≡1 mod65
   would add a second collection of class1 divisors. The first t>1
   is66, already giving tN>S³. Increasing S while keeping the six
   original congruences is unavailable: S must divide their difference
   gcd65. This scaling construction fails its required size inequality.
<a id="q4585-a3"></a>

3. **Use a short arithmetic progression.** Set d_i=1+iS for i=1,…,7
   and N=lcm(d₁,…,d₇). Since gcd(d_i,S)=1, gcd(d_i,d_j) divides j−i.
   Prime by prime, the lcm is at least the product divided by all
   pairwise gcds, hence N≥∏_i(1+iS)/∏_{i<j}(j−i)=Ω(S⁷).
   This explicit seven-divisor construction exceeds S³ for all large S.
   CRT gives the desired residues, but this progression supplies
   insufficient factor overlap; a different design is required.
<a id="q4585-a4"></a>

4. **Count complementary divisors in the same class.** If d≡r mod S,
   then N/d≡Nr^(−1) mod S. Complementation preserves the chosen class
   only if N≡r² mod S. The six-divisor seed has N≡19, r²≡1 mod65,
   so its complementary divisors lie elsewhere. No seventh same-class
   divisor follows from the pairing.
<a id="q4585-a5"></a>

5. **Force a populous class by total divisor count.** Pigeonholing all
   divisors over the invertible classes would need τ(N)>6φ(S).
   But S>N^(1/3), τ(N)=N^o(1), and φ(S)=S^(1−o(1));
   the proposed sufficient inequality fails asymptotically.
   Any construction must concentrate divisors in a particular class,
   not rely on their average count.

## Q4580 — sub-square-root single-prime Wilson quotient

The target is bit operations for one binary input p, not an amortized
table of all smaller primes. Computation needs (p−1)! modulo p², since
w_p=((p−1)!+1)/p modulo p.

<a id="q4580-a1"></a>

1. **Direct modular accumulation.** Multiplying residues1,…,p−1 modulo
   p² gives an exact algorithm, but uses Θ(p) factors. Polynomial costs
   in log p do not turn this into O(p^(1/2−ε)).
<a id="q4580-a2"></a>

2. **Optimize fixed-block baby-step/giant-step evaluation.** For block
   length m, construct f(X)=∏_{i=1}^m(X+i) and evaluate at roughly p/m
   block starts. The basic work balance m+p/m is minimized at√p.
   A different choice of m cannot give the required strict exponent
   saving; a new way of sharing the product work is missing.
<a id="q4580-a3"></a>

3. **Work only over the field F_p.** Wilson's theorem makes the computed
   factorial identically−1 modulo p. This loses the coefficient of p
   in its lift modulo p², which is precisely w_p. A fast field-only
   factorial evaluation therefore has insufficient output precision.
<a id="q4580-a4"></a>

4. **Use a simultaneous remainder table.** Even a quasilinear algorithm
   for all primes up to X does not imply the desired running time on
   one input near X; charging the full table to that input costs about X.
   Precomputation of an unbounded table is absent from the stated model.
   The missing step is a single-query algorithm, not a new amortized mean.
<a id="q4580-a5"></a>

5. **Pair opposite residues recursively.** For h=(p−1)/2,
   (p−1)!≡(−1)^h(h!)²[1−pΣ_{a=1}^h a^(−1)] modulo p².
   This exact identity halves the range but still requires h! at
   p² precision and the harmonic residue. Repeating halving changes
   constants, with the largest block still order p; it supplies no
   strict exponent saving over the optimized square-root block method.

## Q4190 — three generalized tetrahedral numbers

<a id="q4190-a1"></a>

1. **Reduce to the triangular-number theorem.** The exact identity
   T(v)+T(−v−1)=v(v+1)/2 gives a triangular number from two
   tetrahedral numbers. Three triangular numbers would use six
   tetrahedral summands. Keeping only three asks whether a triangular
   number plus one T(u) represents every n, which was not proved.
<a id="q4190-a2"></a>

2. **Force the centered coordinates to sum to zero.** With
   x=u+1,y=v+1,z=w+1 and x+y+z=0, the target becomes
   n=xyz/2=−xy(x+y)/2. This family misses n=2: the finitely many
   factor allocations for |xy(x+y)|=4 give no integer x,y.
   The imposed sum constraint is too restrictive for a universal formula.
<a id="q4190-a3"></a>

3. **Promote local solubility to integral existence.** Uppal's source
   proves local solubility and absence of an integral Brauer–Manin
   obstruction for every n. There is no proved integral Hasse principle
   for this family turning those conditions into a global integer point.
   Local certificates cannot finish this attempted existence proof.
<a id="q4190-a4"></a>

4. **Apply a three-variable circle-method estimate.** For
   S(α)=Σ_{|u|≤M}e(αT(u)), a generic cubic Weyl bound combined with
   ∫|S|²=O(M) gives an absolute minor-arc estimate as large as
   M^(7/4+o(1)). This does not supply the delicate fixed-level
   three-variable main term or a positive count for every n.
   The missing result is strong cancellation for this exact cubic form.
<a id="q4190-a5"></a>

5. **Choose one near tetrahedral summand and fill the remainder.**
   Near n>0 the consecutive T gap is order n^(2/3).
   No two-summand theorem fills every integer in this residual interval.
   Counting two bounded indices gives only O(M²) pairs over an
   O(M³) value range; it cannot assert complete coverage. Negative
   indices allow larger cancellations and remove a proposed finite
   height cutoff, rather than proving the required coverage.

Each of these seven full targets stops at five failures. Exact restricted
criteria, cycles and exclusions above remain reusable; none is a full
catalog closure.

Audit note: Q4196 routes 2, 4 and 5 share the least-factor-cycle witness. They test respectively greedy descent, finite functional closure, and an independent-trials probabilistic argument; they are not three independent impossibility theorems.
