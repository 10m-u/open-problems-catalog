# Q4443: five proposed full-target failures

The all-size endpoint proofs are partial and reset no counter. Source-known
obstructions are explicitly attributed; no theorem here refutes unimodality.
The independent review accepts the endpoint proofs and V02--V05.
The fresh V01 continuation below awaits its short final review.

## Q4443-V01: actual horizontal-strip counterexample construction

Generate every partition lambda of n<=14 and every mu interlacing it,
lambda_i>=mu_i>=lambda_(i+1), which is exactly the horizontal-strip
condition. Compute every rank with the source's exact recursion. All7,567
strips and31,038 polynomials are unimodal. The source had already reported
n<=28, so this is an independent exact construction/control, not new
coverage. A further weighted-selector exploration does not produce a
counterexample. No all-size argument or actual target counterexample was
obtained. The independent audit correctly treats this replay alone as
validation, rather than an additional failed solve attempt.

Continue the actual counter-construction on the three-row family

    mu=(j-1,1), lambda=(j+N-b-1,b,1), 2<=b<=N,

with j in{28,41,70,100} and3<=N<=12. The interlacing inequalities hold
because j-1>=b and N>=b. The strip has N boxes; every ambient size
j+N exceeds28. The appended second/third rows include low contents,
while the first-row additions have arbitrarily separated high contents;
this tests a concrete attempt to force the intermediate summands' peaks
apart enough to create a coefficient valley. Compute every intermediate
rank2<=k<N exactly. All260 actual strips and1,760 intermediate
polynomials remain unimodal, at ambient sizes31--112 in the listed ranges.
The proposed valley construction fails on this finite family. No all-size
proof follows, and the family does not exhaust those ambient sizes.
The full receipt is LARGE-FAMILY-CHECK.json; the source recursion and
interlacing predicates are in check_large_family.py. This is one continued
construction route, not260 attempts. Endpoint identities are unaffected.

## Q4443-V02: obtain a log-concavity certificate

Try proving the stronger ordinary log-concavity of the coefficient row,
by a positive Toeplitz or real-rooted certificate, to imply unimodality.
The actual strip lambda=(2,1,1),mu=(1,1),k=1 has contents(1,-2) and

    E(q)=1+2q+q^2+q^3+q^4.

Its coefficient at q^2 has square1 below the neighboring product2.
The proposed universal log-concavity bridge is false, and real-rootedness
is excluded as well. This exact example is already noted in Question5.28;
the checker rebuilds it. It remains unimodal and does not refute the target.

## Q4443-V03: give all selection summands a common mode

Each tuple summand is a shifted product of q-integers, hence symmetric
unimodal. Try proving that all these summands share a peak; their sum
would then be unimodal. For lambda=(3,1),mu=(1),k=2, the three actual
tuple summands, ordered by labels(2,3),(2,4),(3,4), are

    q^2[3]_q[4]_q, q[3]_q[2]_q, [5]_q[2]_q.

Their mode sets are{4,5},{2,3},{1,2,3,4}. The intersection is empty.
The total is(1,3,5,6,6,4,2,1), which is unimodal. Thus common-mode
alignment is too strong, even at n=4. The endpoint arguments succeed
because uniform intervals overlap (k=1) or there is one tuple (k=N);
those reasons do not extend to intermediate k. A more flexible
coefficient comparison could still work.

## Q4443-V04: make the eigenvalue recursion preserve all unimodal pairs

Try an induction using only nonnegative unimodality of the two preceding
rank polynomials in

    E_n(k)=q^k E_(n-1)(k)+[n+1-k+c]_q E_(n-1)(k-1).

Such a universal two-input preservation lemma is false. With actual
parameter values n=6,k=2,c=-2, the operator q^2 A+[3]_q B sends the
unimodal nonnegative polynomials A=1,B=q^5 to

    q^2+q^5+q^6+q^7,

which is not unimodal. These inputs are a relaxation, not the preceding
eigenvalues of an actual common strip; hence this is no target counterexample.
The actual n=4 strip from V03 also has recursion terms with disjoint modes,
but the universal-operator counterexample is a separate obligation from
requiring common modes among the original selected-tuple summands.
The missing lemma must exploit relations between neighboring eigenvalue
ranks; individual unimodality alone does not supply them.

## Q4443-V05: extend the one-row Gaussian-product formula

Try a closed multiplicative formula consisting of a monomial shift and
positive q-integers/Gaussian binomial factors for every strip. The source's
Theorem C gives such a formula for hook shapes with all new boxes in one
row; the full-rank identity in RESULTS.md supplies another all-strip
product instance. Since products of these factors are palindromic on
their support, the actual V02 polynomial(1,2,1,1,1) cannot have such a
formula. Thus this general product reduction fails. This differs from
V02's log-concavity bridge: Gaussian binomials need not be log-concave,
so its sufficient contract is multiplicative palindromic unimodality,
rather than Toeplitz positivity. The same actual example supplies both
different obstructions, and that shared witness is disclosed.

A positive sum of shifted Gaussian products with controlled asymmetric
centers remains a possible different approach. No general control was
obtained. Five distinct contracts are proposed for the stopping rule;
the independent audit may merge any overlapping routes before acceptance.
