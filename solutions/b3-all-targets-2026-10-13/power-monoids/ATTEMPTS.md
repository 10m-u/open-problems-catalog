# Q2212: five full-target attempts

13 October2026. Each route below was worked toward arbitrary numerical
monoids and arbitrary cutoff. Five proposed consecutive failures, pending
independent review; the boundary theorem is partial and resets no counter.
No example below refutes the actual unimodality conjecture.

## Q2212-U01: construct an actual counterexample across numerical-monoid cuts

Enumerate every additive-closed restriction through l=18, extend it by all
larger integers, and enumerate sumsets of every possible pair of nonunit
factors. Since0 belongs to both factors, B,C are subsets of B+C. Thus a
decomposition of a set A in H cannot use a factor outside H, and the single
ambient precomputation is exact. It finds no counterexample among1,655
actual restrictions. The maximum-based analysis additionally proves all
cutoffs l<=2m in RESULTS.md. Neither covers arbitrary l; this complete
bounded construction attempt fails to produce a full solution or counterexample.
EXPLORATION.json retains the exact counts and checker hash.

## Q2212-U02: a Boolean upper-family rank matching

Try to inherit Boolean-lattice rank matchings by asserting that atomic sets
form an upper family under adjoining positive elements. It fails already
in H=N, l=3: A={0,1,3} is an atom but A union{2}={0,1,2,3}
equals {0,1}+{0,2}. To verify the atom directly, any nontrivial factor
maxima must sum to3, forcing maxima1 and2 and hence the forbidden element2
into A. The proposed inclusion-closure needed for that upper-family
argument is false. This excludes that sufficient contract, not all possible
matchings between the ranks of atoms.

## Q2212-U03: real-rooted atom enumerators

Try proving the much stronger real-rootedness of
P_(H,l)(x)=sum_k alpha_(k,l)x^k, which would imply log-concavity and
unimodality. Exact enumeration for H=N,l=4 gives

    P(x)=4x^2+4x^3+2x^4=2x^2((x+1)^2+1).

The nonzero factor has discriminant -4. Thus no uniform real-rooted
certificate for these actual unweighted enumerators exists. Their actual
coefficient row is unimodal and log-concave; the stronger claim is refuted.

## Q2212-U04: subtract a factor-pair generating function

Try recovering the atomic rank row by subtracting the nonunit factor-pair
enumerator from the binomial subset enumerator. Sumset multiplication loses
factorization multiplicity. At l=4 the set[0,4] has five different unordered
nonunit two-factor decompositions, including

    {0,1}+{0,1,3}, {0,1}+{0,2,3}, {0,1}+{0,1,2,3},
    {0,2}+{0,1,2}, {0,1,2}+{0,1,2}.

There are five distinct decomposable sets but ten factor pairs. Ranked by
output size, their distinct-set counts at k=3,4,5 are2,2,1; pair counts
are2,3,5. The pair subtraction therefore gives the wrong row, including
negative coefficients. An exact formula needs overlap/fibre control;
no positive overlap correction for all sizes was obtained. This is a
counting/product-recursion route, rather than U03's root certificate.

## Q2212-U05: induct on the cutoff using the previous rank row

Try an exact induction that retains the previous alpha row, the cutoff,
and whether the new integer belongs to H. The transition is not determined
by those data. Consider the actual numerical monoids

    H1={0,2,4} union[5,infinity), H2={0,3,4} union[5,infinity).

At l=3 they both have alpha row(0,0,1,0), and both include the new element4.
At l=4 their rows are respectively(0,0,2,0,0) and(0,0,2,1,0).
The former triple{0,2,4} decomposes as{0,2}+{0,2}, whereas the latter
triple{0,3,4} is atomic because two positive factor maxima are at least3
each. This defeats a transition based only on the previous rank state.
Additional additive geometry may support another induction; none is supplied
by this route. It differs from U02's claimed setwise upper closure and U04's
factorization-multiplicity subtraction.

The [exact route checker](check_routes.py) validates all displayed atoms,
decompositions, rows and multiplicities. Five route failures are proposed;
their distinctness and scope await the same retained agent's audit.
