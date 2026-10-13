# Q2751: five worked full-target routes

The general q-Fibonomial unimodality question remains unresolved. The
parameter-four theorem in N4-PROOF.md is partial and resets no counter.
These five distinct full-target failures pass the retained agent's
independent review in ../stirling/FIBONOMIAL-REVIEW.md.

## Q2751-F01: construct an asymmetric coefficient valley beyond known tests

The primary paper reports all m+n<=20 and the diagonal m=n<=16.
Try actual asymmetric pairs with m+n=21,...,24 and5<=n<m, expanding
the q-integer quotient exactly. Denominator divisions are checked by
reconvolution; every coefficient, symmetry and lower-half difference
is inspected. No actual counterexample occurs on this finite family.
All pairs, exact degrees, masses and central coefficients are preserved
in ROUTE-CHECK.json. This is one unsuccessful finite construction,
not a proof at arbitrary m,n or one attempt per pair.

## Q2751-F02: prove all lower-half differences by vector-partition bounds

Without loss n<=m. Put

    p_n(s)=[q^s]1/((1-q) product_(i=3)^n(1-q^F_i)),
    D=F_(m+n+2)-F_(m+2)-F_(n+2)+1.

For negative arguments p_n=0. Exact inclusion-exclusion gives

    q^jB_(m,n)
      =sum_(S subset{1,...,n})(-1)^|S|
           p_n(j-sum_(i in S)F_(m+i)).                    (2)

This reduces the full question to nonnegativity of (2) for0<=j<=D/2.
At n=4, the two Fibonacci additive identities cancel enough subset
terms to leave four terms. The partition count is a quadratic with
six bounded residue errors. N4-PROOF.md proves all m by a concave
quadratic on the first region, a positive linear margin on the last,
and six exact bases. Thus this full-proof attempt produces a new
all-size boundary theorem.

At n=5, the additional denominator1-q^5 changes p_n to a cubic
quasipolynomial with period30. At general n its degree is n-2,
with period dividing lcm(F_3,...,F_n); the subset terms and breakpoints
also grow with n. The n=4 two-region bound does not supply a uniform
sign estimate for (2). I worked the exact reduction and cancellations,
but did not obtain that missing uniform bound. The full-target proof
attempt fails at this stated obligation. This is not a mathematical
disproof of a higher-order estimate or a claim that fixed n cannot be
treated similarly. Its partial theorem is retained separately.

## Q2751-F03: match whole denominator q-integers to separate numerator factors

Try pairing each [F_i],1<=i<=n, with a distinct numerator [F_(m+j)]
divisible by it. Each quotient would then be a positive dilated uniform
factor, to which smoothing/overlap criteria might apply. Even the pairing
step fails at actual m=n=10. Denominator indices{4,6,8,9,10} have
divisible numerator indices in11,...,20 respectively

    4:{12,16,20}, 6:{12,18}, 8:{16}, 9:{18}, 10:{20}.

Five demands have only four neighbors, so Hall's condition excludes
every whole-factor pairing. The checker uses actual Fibonacci divisibility,
not just divisibility of indices. This does not obstruct polynomiality:
splitting cyclotomic factors or grouping several denominators can work.
Those groupings do not automatically give positive unimodal factors;
for example [ab]/([a][b]) has coefficient-1 at q when a,b>1 are
coprime. A different grouped certificate is still possible.

## Q2751-F04: induct from the symmetry/unimodality and numerical invariants of predecessors

The thesis tiling recursion is

    B_(m,n)=[F_(m+1)]_(q^F_n) B_(m,n-1)
       +q^(F_n F_(m+1)) [F_(n-1)]_(q^F_m) B_(m-1,n).

Try a two-input preservation lemma requiring nonnegative integer
coefficients, symmetry, unimodality, the correct degree/mass and unit
endpoints of the two preceding polynomials. At actual m=n=3 both
predecessors have degree6 and mass15. The synthetic polynomial

    A=B=1+q+q^2+9q^3+q^4+q^5+q^6

has all these invariants. The recursion sends it to

    (1,1,2,10,3,11,4,11,3,10,2,1,1),

a symmetric nonnegative row with valleys. Thus those invariants do not
close an induction; cross-rank or additional coefficient relations are
needed. The synthetic inputs are not actual q-Fibonomials. This is a
relaxed preservation obstruction, not an actual target counterexample.

## Q2751-F05: lift a unimodal chain decomposition separately inside every fixed path

Try decomposing each fixed-path tiling fiber into consecutive-weight
chains, so summing fibers would reduce to aligned unimodal components.
On the actual2x3 rectangle, the path NNEEN forces vertical dominoes
in both columns in rows1,2. Their special weights are q and q^2.
The top row can contain two monominoes or one horizontal domino of
weight q^2. The complete fiber generating polynomial is therefore

    q^3(1+q^2).

Its rank4 is empty between occupied ranks3 and5. No saturated chain
decomposition confined to this path can repair this gap. The full
B_(2,3) is unimodal, through contributions from other paths. A successful
chain action may need to change the path, as the existing parameter-two
construction indeed permits. This is a failure of a specified fixed-path
method, distinct from F04's unrestricted recursion-input lemma.

No stronger-property obstruction is counted separately. The source-known
B_(3,3) non-log-concavity is recorded only as a control, not a sixth
attempt. Source/download mistakes and the corrected draft degree count
are zero failures.
