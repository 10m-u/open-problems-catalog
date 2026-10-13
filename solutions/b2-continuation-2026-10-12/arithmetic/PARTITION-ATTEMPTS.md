# Q4642/Q4643: partitions in real quadratic fields

Read the cached primary sources `texts/papers/collections-dd6c814c6214da1f.txt.gz`, introduction and §§2–4, and `texts/papers/collections-c33c5cb9936060db.txt.gz`, §§4–5. The first target asks for infinitely many **distinct partition-count values** divisible by m in each fixed field. Infinitely many elements with one repeated count are insufficient. The second concerns positive rational integers n, for every squarefree D≡1 mod4.

## A parity generating function from the conjugation involution

Conjugation acts on partitions of a rational integer. Nonfixed partitions pair and cancel modulo 2. A fixed partition contains arbitrary rational-integer parts and equal multiplicities of each noninteger conjugate pair. Each pair contributes its positive integer trace. Consequently in F₂q

    Σ_{n≥0}p_K(n)q^n
      = ∏_{j≥1}(1−q^j)^−1
        ∏_{unordered noninteger pairs {α,α'}}(1−q^(Tr α))^−1.

All coefficient computations are locally finite: trace bounds leave only finitely many totally positive algebraic integers. For D≡1 mod4 write α=(a+b√D)/2, b>0, a≡b mod2, a>b√D. The number t_D(a) of conjugate pairs of trace a is the number of such positive b; exactly

    t_D(a)=floor(a/(2√D))                  if a even,
    t_D(a)=floor((a/√D+1)/2)              if a odd.

Thus the Euler exponent at a is 1+t_D(a). Integer-square comparisons give an exact algorithm without floating-point floors. This is a proved structural reduction, not an infinitude theorem. For D=5 it includes an odd-trace pair at a=3, namely (3±√5)/2, which explains why a blanket even-trace assumption fails.

<a id="q4642-a1"></a>
## Q4642 A1 — Use the density-one range theorem across fields

The source proves that for each fixed requested finite range, almost all real quadratic fields attain it. The quantifiers are over varying D, with a density-zero exceptional set depending on the range. The target fixes arbitrary D and requires infinitely many distinct multiples. One cannot exchange these quantifiers or remove the exceptional fields by density. **Failed field-density transfer.**

<a id="q4642-a2"></a>
## Q4642 A2 — Multiply an element by infinitely many positive units

If η is a totally positive unit, multiplication of every part gives a bijection between partitions of α and ηα, with inverse η^−1. Hence p_K(ηα)=p_K(α). This creates infinitely many elements at one count, precisely failing the target's distinct-values requirement. **Failed unit-orbit construction.**

<a id="q4642-a3"></a>
## Q4642 A3 — Deduce divisible values from increasing integer inputs

Appending a part 1 injects partitions of n into those of n+1. The singleton partition (n+1) is outside its image for n≥1, so p_K(n+1)>p_K(n). The range is therefore infinite and unbounded. This gives no residue distribution: a strictly increasing integer sequence can avoid all multiples of m, for instance mn+1. No control of the increments modulo m is proved. **Failed monotonicity-to-divisibility argument.**

<a id="q4642-a4"></a>
## Q4642 A4 — Import ordinary partition congruences

The source's Theorem 7 gives p_K(n)=p(n) when D exceeds an explicit bound depending on n. At fixed D it covers only a finite initial range. The ordinary congruence progressions have unbounded n and eventually leave that range. Moreover all totally positive noninteger parts then contribute; a proof for integer-only partitions is not a bijection for p_K. **Failed classical-congruence transfer.**

<a id="q4642-a5"></a>
## Q4642 A5 — Make the exact recurrence into an infinitude certificate

The source's recurrence over 0≺β⪯α computes each value exactly. Unrolling it is a correct finite algorithm, but carries an expanding set of β and divisor sums depending on α. No fixed finite residue-state recurrence or periodic progression forces a zero class modulo every m. Finite divisibility hits cannot certify infinitely many distinct values. The failure is of the proposed finite-state inference, rather than of the computation itself. **Failed recurrence-to-infinitude route.**

<a id="q4643-a1"></a>
## Q4643 A1 — Extend the source's D≡2,3 parity proof unchanged

In those fields Tr(α)/2 is always integral and the number of parts at each such weight is odd. For D≡1, odd traces occur: at D=5 the pair (3±√5)/2 has half-integral trace weight. The same product/odd-exponent argument therefore does not apply. The displayed fixed-partition product correctly retains those odd traces, but its coefficients have no proved eventual-parity exclusion. **Failed unchanged parity-proof transfer.**

<a id="q4643-a2"></a>
## Q4643 A2 — Pair every partition with its conjugate

Nonfixed partitions cancel modulo 2, but fixed partitions survive. Rational-integer-only partitions are fixed, and so are partitions containing equal counts of a noninteger pair. For example 3=(3+√5)/2+(3−√5)/2 is fixed. Thus the involution does not force all large counts even or reduce their parity to ordinary p(n). It yields exactly the structural Euler product above, still requiring an analysis of its coefficients. **Failed complete-cancellation argument.**

<a id="q4643-a3"></a>
## Q4643 A3 — Transport parity along positive units while keeping integer arguments

Multiplication by a positive unit preserves count parity. A nontrivial positive unit η of a real quadratic field is irrational; ηn is irrational for nonzero integer n, so this operation leaves the rational-integer slice asked about by Q4643. Conjugation and norm do not provide a partition-preserving map back to integers. **Failed unit-orbit integer construction.**

<a id="q4643-a4"></a>
## Q4643 A4 — Use the logarithmic derivative of the parity product

For b_j=1+t_D(j), the product gives in characteristic 2

    n p_K(n)=Σ_{k=1}^n (Σ_{j|k}j b_j)p_K(n−k).

Only odd j contribute, while b_j is a nonconstant irrational-floor sequence. Unlike the source's uniform odd-exponent case, the divisor sum cannot be replaced by σ(k), whose odd support is squares and twice squares. Also at even n the leading coefficient vanishes, leaving no recursive determination of that parity. A new sparse-support or coefficient theorem is needed; the formal recurrence alone does not replicate the known contradiction proof. **Failed logarithmic-derivative closure.**

<a id="q4643-a5"></a>
## Q4643 A5 — Replace the fixed field by a large-discriminant ordinary prefix

For each finite prefix one can choose a new D large enough to identify it with ordinary partitions and obtain both parities. The target fixes every D before n grows. At D=5 the extra trace-three pair already changes the ordinary parity sequence at n=3. A finite prefix or an unbounded sequence of different fields gives no infinite same-field parity subsequence. **Failed prefix-to-infinitude route.**

Both full targets stop at five routes. Unit invariance, monotonicity and the explicit fixed-partition Euler reduction are retained at their actual scopes. The submitted paper named in the provenance record has no read text and is not assumed to resolve these questions.
