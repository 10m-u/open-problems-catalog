# B3 continuation: new questions and recovery targets

7 October 2026. These are research-local IDs. They do not extend or renumber the thesis catalog. Proved scopes are in [RESULTS.json](RESULTS.json); original targets and stable IDs are in B3_statement_ledger.json.

## B3C-Q01: conjecture

For every integer q>=1 and every collection of integer bandwidths B_I>=0 on linear intervals I of {1,...,2q}, let H={x in {0,1}^{2q}: abs(2*sum_(i in I)x_i-|I|)<=B_I for all I}, and c_j=number of x in H with sum_i x_i=j. Is q*c_q >= (q+1)*c_(q-1)?

Evidence: Complete symmetric-interval enumeration q<=4; all-dimensional laminar case and endpoint consequences proved.

Next direction: Seek a nonlocal exchange on prefix-height vectors for crossing intervals. One-bit inclusion matching is disproved.

Related catalog target(s): Q164.

## B3C-Q02: unverified-proof-lead-and-conjecture

For every integer r>=1, every 2x2 minor det(f_(i_a+j_b)(x)) with 0<=i_1<i_2 and 0<=j_1<j_2 has nonnegative coefficients, for f=c_r or f=s_r.

Evidence: User-reported proof unavailable; 23328 exact finite minors pass; leading cycle block proved.

Next direction: Prove the adjacent fixed-sum inequality f_m f_(n+1)-f_(m+1)f_n >=_coeff 0 for all 0<=m<n; telescoping then supplies arbitrary gaps.

Related catalog target(s): Q1160.

## B3C-Q03: existing-question-subproblem

For every integer r>=3 and every pair of increasing nonnegative triples I,J, det(c_r,i_a+j_b(x)) has nonnegative coefficients.

Evidence: Leading cycle block all-r>=2, and initial extreme coefficients for arbitrary minors.

Next direction: Next symbolic block I=J=(1,2,3), followed by unequal gaps; subset order-three failure is not a cycle counterexample.

Related catalog target(s): Q1160.

## B3C-Q04: conjecture

For every integer n >= 2 and every 1 <= r < n, Delta_r(x)=det[b_(2*j-i+1)]_(i,j=0)^(r-1), where F_n(t;x)=sum_(k=0)^n e_k(x) product_(j=0)^(n-1)((n+k-j-1)+(n-k+j)t)=sum_(i=0)^n b_i t^(n-i), has a strictly positive coefficient for every monomial product_i x_i^d_i with 0 <= d_i <= r, and has no other monomials.

Evidence: All 4816 coefficient values for n2..5,r<n are strictly positive.

Next direction: Derive a structural positive expansion of the Hurwitz determinants; preserve independent Bernoulli parameters.

Related catalog target(s): Q1442.

## B3C-Q05: conjecture-stronger-than-catalog-target

For every integer n>=1 and every (a_1,...,a_n) in [0,1]^n, all zeros of P(z)=sum_j e_(n-j)(a) binom(z,j) lie in |z+1/2|<=n-1/2; boundary only for all-zero/all-one parameter polynomials.

Evidence: Uniform n<=5 certificate; all n for equal parameters. Degree6..8 claim has no supplied certificate.

Next direction: Use Q04 or another argument respecting the TP parameterization; arbitrary shift mixtures are an invalid relaxation.

Related catalog target(s): Q1442.

## B3C-Q06: unverified-recovery-lead

For every pair of integers d,u>=1, every s-Eulerian vector representing (1+u x)^d has length at least 2d-1, and a length 2d-1 representation exists.

Evidence: Upper bound proved. Explicit vector (u+1,1,u+1,...,1,u+1) realizes the polynomial. Universal lower bound claimed remotely but not recovered.

Next direction: Recover L13 simple negative roots for each nonunit block, or prove directly that repeated linear factors must occur in separate blocks.

Related catalog target(s): Q1262.

## B3C-Q07: unverified-recovery-lead

For every nonempty positive integer vector s with all entries >=2, every root of E_s(x) is negative and simple.

Evidence: Stalled-agent claim only. General real-rootedness alone does not imply simplicity. Degree-two coefficient classification is not an all-degree proof.

Next direction: Audit strict interlacing of refined ascent polynomials with all endpoint and equality cases. Do not infer strictness from weak interlacing.

Related catalog target(s): Q1262.

## B3C-R01: missing-certificate-recovery

Recover exact degree-six, degree-seven and degree-eight independent-parameter interpolation disk certificates and endpoint classification.

Evidence: Intermediate messages from the external agent; no corresponding files survived.

Next direction: Prefer obtaining or structurally replacing missing certificates; no unbounded n8 brute-force determinant run authorized by this checkpoint.

Related catalog target(s): Q1442.

## B3C-R02: missing-statement-recovery

Identify the two stronger Schur-positivity claims and exact counterexamples mentioned in the stalled output.

Evidence: Neither exact quantifiers nor witnesses supplied.

Next direction: Recover original statements before recording a refutation. No historical Schur counterexample asserted.

Related catalog target(s): Q1160, Q1442.
