# Subsum attempts: Q3702 and Q3703

13 October 2026. Each full catalog target stops unresolved after five
consecutive failed full-target routes below, pending independent count
review. New boundary results do not reset those counters. No source,
execution or service error is counted. Exact controls and universal partial
proofs are in [BOUNDARIES.md](BOUNDARIES.md),
[check_boundaries.py](check_boundaries.py) and [BOUNDARY-CHECK.json](BOUNDARY-CHECK.json).
The definitions, exclusions and existing coefficient/symmetry identities
were read in the [primary source](https://link.springer.com/article/10.1007/s11139-026-01419-0).
Known nonreal factors are not claimed as new discoveries.

Let F_n be the product in Q3702 and H_n the binary-partition sum in Q3703.

<a id="q3702-a1"></a>
## Q3702 A1: direct coefficient-ratio inequalities

Extract low coefficients in terms of L=floor(log_2 n)+1 and the exponent
of the size-three factor. Bounding that exponent by L-1 gives the strict
first two inequalities at every n>=8, including their reflected versions.
The remaining admissible n=1,2,4 are direct finite products.
For an arbitrary index, the coefficient is a bounded-multiplicity partition
sum with several weights and no single factorial-ratio formula. The
low-degree bound does not continue to an all-index ratio inequality.
Failure 1, retaining the all-size boundary theorem in BOUNDARIES.md.

<a id="q3702-a2"></a>
## Q3702 A2: Newton inequalities through real roots

Try to prove negative real roots and apply Newton inequalities. For every
n>=2, the actual product contains 1+x^2 to a positive power and therefore
has the nonreal roots i and -i. The checker independently verifies the
actual F_8 evaluation in the quotient by x^2+1. The proposed sufficient
root class is impossible even at admissible n. Failure 2; this does not
refute ordinary log-concavity.

<a id="q3702-a3"></a>
## Q3702 A3: induct in n using the exact added factors

The exponents count the integers j>=0 for which 2^j*i<=n. Subtracting
their values at n-1 gives the exact recurrence

    F_n=F_(n-1) product_(j>=0, 2^j divides n)(1+x^(n/2^j)).

Try to propagate only symmetry, positivity on full support and ordinary
log-concavity through these gapped factors. The generic preservation claim
fails: the positive symmetric LC array (1,100,1) multiplied by 1+x^2 gives
(1,100,2,100,1), which is not LC. The smaller degree of this control is
not asserted to match an actual F_(n-1). Even support longer than the gap
does not repair the sole-shape invariant: a sharply peaked symmetric
geometric array also develops two peaks after a shift. The actual rows
would need quantitative bounds connecting the gap to their curvature.
Those bounds were not obtained uniformly in n and index. Failure 3 on
this recurrence-preservation route.

<a id="q3702-a4"></a>
## Q3702 A4: regroup into geometric factors for a Toeplitz TN2 certificate

Try a different fixed-factorization proof, rather than the n-recursion.
For each odd j<=n put s_j=floor(log_2(n/j)). Binary telescoping gives

    F_n=product_(j odd<=n) product_(b=0)^(s_j)
          (1+x^j+x^(2j)+...+x^((2^(b+1)-1)j)).

Indeed a factor 1+x^(j*2^a) occurs in exactly s_j-a+1 of the inner
geometric products, its required exponent. The j=1 geometric factors
have constant positive coefficient sequences and are LC. For j>1 each
nonconstant factor has gaps, and its Toeplitz matrix has negative order-two
minors. For 1+x^3, rows 0,1 and columns 1,3 give [[0,1],[1,0]], determinant
-1. Therefore a product of TN2 Toeplitz factors is unavailable in this
regrouping. Simply using a long uniform factor is also insufficient:
(1+x+x^2+x^3)(1+x^3) has array (1,1,1,2,1,1,1), which fails LC.
Absorbing whole odd chains into the complete j=1 smoothing product would
require a new joint inequality, not the factor theorem. Failure 4.
This route supplies an exact regrouping and tests its factor certificates;
A3 instead tests an invariant for already generated full rows.

<a id="q3702-a5"></a>
## Q3702 A5: derive global coefficient shape from the central normal limit

Interpret normalized coefficients as weighted fair-Bernoulli sums. The
explicit characteristic function proves an all-size central normal limit,
with variance asymptotic 2n^3/21 and degree asymptotic 2n^2/3, as detailed
in BOUNDARIES.md. Try to use its smooth limiting density to certify every
adjacent-coefficient inequality. Weak convergence supplies no such local
sign bound and does not control the far tails.

This limitation persists even for probabilities arbitrarily close to
binomial ones: decrease the middle coefficient of a degree-2m binomial
array by relative size 2/(m+1), keeping all other coefficients, then
renormalize. At m>=2 it is positive but violates the middle LC inequality,
because its neighbor-to-middle ratio is m/(m+1). Its total variation
distance from the binomial law tends to zero, hence it has the same central
normal limit. This is an auxiliary family, not F_n. A uniform discrete
second-difference estimate with tail control remains missing. Failure 5;
retain the proved central limit and stop the complete target unresolved.

<a id="q3703-a1"></a>
## Q3703 A1: coefficient-ratio bounds from binary partition counts

Use the known first-three coefficient expressions and split each partition
according to its non-one mass. Monotonicity of binary partition counts
forces c1/c0>=floor(n/2)+1/2 for n>=4. Bounding c2 then proves
c1^2-c0*c2>=c0^2/2>0, and symmetry gives the final inequality. The proof
is in BOUNDARIES.md. Higher coefficients mix additional multiplicities and
their correlations, so this first-moment bound does not close a general
coefficient ratio argument. Failure 1, retaining both all-size endpoints.

<a id="q3703-a2"></a>
## Q3703 A2: negative real roots

Try to obtain LC from Newton's real-rooted class. The source already
identifies 1+x+x^2 as an actual factor for n>1. The checker verifies this
directly at admissible n=6: H_6=(6,22,54,80,100,100,100,80,54,22,6)
has equal coefficient sums in all three residue classes modulo three,
and hence vanishes at primitive third roots of unity. Its nonreal roots
rule out the proposed stronger class. Failure 2, not an LC disproof.

<a id="q3703-a3"></a>
## Q3703 A3: termwise binomial LC and synchronized summation

Try to prove LC for each explicit partition summand and combine the
same-degree symmetric summands. For the actual partition lambda=(1^n),
the exponent of 1+x is zero. Its summand is a nonconstant product in x^2
for n>=2, with zero odd coefficients and positive constant and quadratic
coefficients. It fails LC at index one. Thus the proposed termwise
condition already fails on actual summands, although their sum is positive
throughout and passes the bounded full-array controls. Moreover a sum of
LC arrays is not generically LC. A valid argument must use interactions
between different partitions rather than certify each independently.
Failure 3.

<a id="q3703-a4"></a>
## Q3703 A4: a probabilistic mean/variance certificate

Represent normalized H_n as a mixture of fair-Bernoulli subset sums.
All summands have the same mean d/2. Their mixing weights are proportional
to 2^(-length(lambda)), and total variance is exactly equation (2) of
BOUNDARIES.md. Try to deduce LC from this probability structure's
symmetry, full support, variance bounds and the proved endpoint coefficients.
Those retained data do not determine the local shape.

The actual H_6 array above is LC. Perturb only its middle five entries
by 10*(1,-4,6,-4,1), giving
(6,22,54,90,60,160,60,90,54,22,6). This positive symmetric auxiliary array
has the same degree, mass, mean, variance 176/39, and first three
coefficients. Its order-four LC defect is 60^2-90*160<0. The perturbation
has zero moments through order two, so every variance bound remains
identical. It is not asserted to arise from any binary-partition sum.
Controlling the mixture's complete local correlations is an extra
obligation; the global moment representation does not supply it.
Failure 4, retaining the exact all-size variance identity.

<a id="q3703-a5"></a>
## Q3703 A5: Lorentzian homogenization and ultra-log-concavity

Try to obtain a homogeneous Lorentzian certificate, which would imply
binomial-normalized LC and hence the ordinary target. This stronger
property is false on infinitely many actual H_n. At n=2^s, s>=2,
the common-degree mixture has degree d=s*n and variance at least
(n^2-n)/4>d/4. A positive symmetric ULC array has variance at most d/4;
the full-support covariance proof and explicit support argument are in
BOUNDARIES.md. Thus H_(2^s) is not ULC at any such size, including
arbitrarily large admissible n. The exact receipt verifies initial powers,
but the obstruction is the all-size variance proof.
Failure 5. Stop the full LC target unresolved; do not mistake this stronger
normalization obstruction for a counterexample to it.
