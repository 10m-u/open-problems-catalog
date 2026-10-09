# B3 continuation: weighted interval log-concavity, Stirling and interpolation results

Continuation of B3 with written proofs, a human proof review and exact computational controls (run `python3 run_all.py`). Not peer reviewed.

| Problem | Title | Status | Result |
|---|---|---|---|
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | auxiliary | For every integer 0<=m<=9, every binary family on m positions defined by arbitrary integer lower/upper bounds on sums over linear intervals, and all nonnegative real position weights, its weighted rank sequence is ultra-log-concave of… |
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | auxiliary | For every such linear interval family in every integer dimension m>=0 and every nonnegative weight vector, k(m-k)f_k^2 >= (k+1)(m-k+1)f_(k-1)f_(k+1) at k in {1,2,3,4,m-4,m-3,m-2,m-1} intersect {1,...,m-1}. Limits: Middle inequalities in… |
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | auxiliary | For every integer m>=0, every laminar family of integer-bounded linear intervals on m binary positions, and all nonnegative position weights, the weighted feasible-word ranks are ULC of order m. Limits: Typical overlapping path… |
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | counterexample | In dimension six, equations x1+x2=x2+x3=x4+x5=x5+x6=1 give rank counts (0,0,1,2,1,0,0). The unique rank-two word 010010 has no feasible rank-three superset. Limits: Refutes the stated stronger matching route, not APP or ULC. The stalled… |
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | counterexample | The unrestricted two-variable family has central normalized ULC defect w1^2-2\*w1\*w2+w2^2, whose mixed coefficient is -2. Limits: Numerical nonnegativity survives, since the defect is (w1-w2)^2. |
| [Q164](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q164) | For every path or cycle G on n vertices and integer ℓ ≥ 1, is the sequence γₖ(G^… | partial | For every power of a path, domination counts are log-concave, including arbitrary nonnegative multiplicative vertex weights; more generally for interval-neighborhood graphs. Remaining: Binomial-normalized ultra-log-concavity and the… |
| [Q166](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q166) | For positive n and ℓ ≥ 2, let Aℓ(n,k) count compositions of n into k positive pa… | auxiliary | For every integer 0<=m<=9, every binary family on m positions defined by arbitrary integer lower/upper bounds on sums over linear intervals, and all nonnegative real position weights, its weighted rank sequence is ultra-log-concave of… |
| [Q166](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q166) | For positive n and ℓ ≥ 2, let Aℓ(n,k) count compositions of n into k positive pa… | auxiliary | For every integer m>=0, every laminar family of integer-bounded linear intervals on m binary positions, and all nonnegative position weights, the weighted feasible-word ranks are ULC of order m. Limits: Typical overlapping path… |
| [Q166](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q166) | For positive n and ℓ ≥ 2, let Aℓ(n,k) count compositions of n into k positive pa… | proved | For every n>0 and ell>=2, compositions avoiding ell consecutive unit parts have log-concave counts by number of parts. The proof covers any interval-sum constraints on binary words and all fixed nonnegative position weights. Remaining:… |
| [Q1160](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1160) | Hankel positivity for higher-order cycle polynomials | auxiliary | For every integer r>=2, all nonempty minors of (c_(r,i+j)(x))\_(i,j=0)^2 are coefficientwise nonnegative, with positive coefficients throughout each stated nonzero support. The 3x3 determinant has support exactly degrees 2 through 6.… |
| [Q1160](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1160) | Hankel positivity for higher-order cycle polynomials | partial | For every r>=2 and every cycle Hankel minor on increasing nonnegative index sets I,J, the degree is sum(I)+sum(J), the vanishing order is \|I\|-1_{0 in I and 0 in J}, and both extreme coefficients are strictly positive. Remaining:… |
| [Q1262](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1262) | Which colored multiset polynomials are s-Eulerian? | auxiliary | Every nonconstant s-Eulerian polynomial of integer degree d>=1 has a representing positive integer vector of length at most 2d-1. Limits: Existential bound after deleting units and contracting all-two blocks; all-degree sharpness for… |
| [Q1262](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1262) | Which colored multiset polynomials are s-Eulerian? | auxiliary | For every positive integer vector s with all entries >=2, if E_s(x)=1+h_1 x+h_2 x^2 has degree exactly two, then h_1>h_2>0. Limits: Degree-two blocks only; does not establish simple roots for every nonunit block. Exceptional (2,6,3)… |
| [Q1262](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1262) | Which colored multiset polynomials are s-Eulerian? | auxiliary | For every positive integer b, A_(2,b)(x)=1+2b x+binom(b,2)x^2 is s-Eulerian for some positive integer vector of arbitrary length iff b=2 or b(b+1)/2 is an integer square. Limits: Exact subfamily of general coloured multiset question… |
| [Q1262](../../problems/mathematics/combinatorics-graph-theory-part-1.md#q1262) | Which colored multiset polynomials are s-Eulerian? | partial | Finite recognition for arbitrary allowed vector length: enumerate ordered factorizations of N=p(1) with optional unit separators; length at most 2\*Omega(N)-1 suffices. Complete exclusion for multiplicities (2,3). Infinite Pell family:… |
| [Q1442](../../problems/mathematics/analysis.md#q1442) | Sharp outer zero radius for TP interpolation | auxiliary | For every integer 1<=n<=5 and every real parameter tuple (a_1,...,a_n) in [0,1]^n, all zeros of P(z)=sum_(j=0)^n e_(n-j)(a) binom(z,j) satisfy \|z+1/2\|<=n-1/2. Boundary zeros occur only at the all-zero and all-one parameter polynomials.… |
| [Q1442](../../problems/mathematics/analysis.md#q1442) | Sharp outer zero radius for TP interpolation | auxiliary | For every integer n>=1 and every real a in [0,1], all zeros of the polynomial with L(P)(u)=(u+a)^n satisfy \|z+1/2\|<=n-1/2, strictly for 0&lt;a<1. For n>=2, \|z+1/2\|^2 <= (n-1/2)^2-8a(1-a)(n-1). Limits: One-parameter family; arbitrary… |
| [Q1442](../../problems/mathematics/analysis.md#q1442) | Sharp outer zero radius for TP interpolation | counterexample | For n=4, P(z)=binom(z,4)+binom(z+4,4) has a root with \|z+1/2\|>7/2; 24P(w-1/2)=2w^4+43w^2+105/8. Limits: Outside the TP class: sampled numerator 1+t^4 is not real-rooted. Does not refute Q1442. |
| [Q1442](../../problems/mathematics/analysis.md#q1442) | Sharp outer zero radius for TP interpolation | partial | R_2=2 and R_3=3. Complete degree-two root locus. All fixed-degree interpolation extrema are attained after normalization; their imaginary extent is strictly below the corresponding SNN bound for degrees>=2. Remaining: R_n=n for n>=4… |

## Files

- [NEW-QUESTIONS.json](NEW-QUESTIONS.json)
- [NEW-QUESTIONS.md](NEW-QUESTIONS.md)
- [REPORT.md](REPORT.md)
- [RESULTS.json](RESULTS.json)
- [audit/PROOF-REVIEW.md](audit/PROOF-REVIEW.md)
- [audit/eulerian-independent-review.md](audit/eulerian-independent-review.md)
- [audit/eulerian-report.md](audit/eulerian-report.md)
- [audit/eulerian_checks.json](audit/eulerian_checks.json)
- [audit/eulerian_checks.py](audit/eulerian_checks.py)
- [audit/independent_checks.json](audit/independent_checks.json)
- [audit/independent_checks.py](audit/independent_checks.py)
- [compositions/REPORT.md](compositions/REPORT.md)
- [compositions/checks.json](compositions/checks.json)
- [compositions/checks.py](compositions/checks.py)
- [compositions/conjectures.json](compositions/conjectures.json)
- [interpolation/REPORT.md](interpolation/REPORT.md)
- [interpolation/checks.json](interpolation/checks.json)
- [interpolation/checks.py](interpolation/checks.py)
- [interpolation/conjectures.json](interpolation/conjectures.json)
- [interpolation/degree-2-certificate.json](interpolation/degree-2-certificate.json)
- [interpolation/degree-3-certificate.json](interpolation/degree-3-certificate.json)
- [interpolation/degree-4-certificate.json](interpolation/degree-4-certificate.json)
- [interpolation/degree-5-certificate.json](interpolation/degree-5-certificate.json)
- [run_all.py](run_all.py)
- [stirling/REPORT.md](stirling/REPORT.md)
- [stirling/checks.json](stirling/checks.json)
- [stirling/checks.py](stirling/checks.py)
- [stirling/conjectures.json](stirling/conjectures.json)

