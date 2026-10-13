# Q4443: endpoint ranks for every horizontal strip

Partial proof, independent review accepted. The full target is unimodality
of every E_(lambda/mu)(k) in the frozen statement. We read the actual
[Brauner–Commins–Grinberg–Saliola v3](https://arxiv.org/pdf/2503.17580v3),
definitions5.6, formula5.8, Proposition5.11 and Question5.28; cached text
is texts/papers/collections-e44da3d71dfbfd55.txt.gz. The source already
proves every one-row strip and reports bounded verification through n=28.
It also already points out a non-log-concave eigenvalue. No novelty claim.

Put n=|lambda|, j=|mu|, N=n-j, and c_l=column minus row of the box
with label l in the prescribed row order. Every content satisfies c_l>=-j:
mu has at most j rows and a horizontal strip adds at most one new row.
The source's proof of Theorem5.12 gives this bound explicitly.

## Every strip at k=1

The formula simplifies to

    E(1)=sum_(l=j+1)^n q^(n-l)[l+c_l]_q.

Each summand has coefficient1 on the integer interval

    [n-l,n+c_l-1].

All these intervals contain the same integer N-1: their left ends are
at most N-1 and their right ends are at least n-j-1=N-1. Thus the
sum's coefficients weakly increase through N-1 and weakly decrease after
it. This proves unimodality for every horizontal strip at k=1, including
multirow strips. The empty-strip k=1 polynomial is zero.

## Every strip at full rank k=N

There is only one selected tuple, l_m=j+m. Its exterior q-power cancels
exactly because nN-binomial(N,2)-sum_(m=1)^N(j+m)=0. Consequently

    E(N)=product_(l=j+1)^n [j+1+c_l]_q.

All factors are positive q-integers. Their product is palindromic and
unimodal. A self-contained closure argument: any palindromic unimodal
nonnegative coefficient row of degree d is a nonnegative sum of the
centered interval rows q^i[d-2i+1]_q, with weights the consecutive
increases up to its center. The convolution of two centered interval
rows is a symmetric trapezoid with the sum of their centers. Expanding
two such sums therefore proves closure under multiplication. This applies
successively to every factor above. The empty product is1.

Together with E(0)=1 this closes every k for N<=2, for all ambient sizes
and every strip. General intermediate ranks2<=k<N remain unresolved.

## Controls and limitations

[check_eigenvalues.py](check_eigenvalues.py) uses the exact source recursion
and integer arrays to check every horizontal strip with n<=14:7,567
strips and31,038 polynomials, with no unimodality counterexample. It
compares14,118 endpoint formulas and directly expands the displayed
summand example independently of the recursion. These are supporting
controls, not an extension of the source's bounded n<=28 assertion.

The k=1 proof also permits arbitrary positive weights on its interval
summands, but the other ranks do not follow from that argument. An
additional weighted-selection screen through n=12 found no counterexample
for two distinguished box weights100 and all others1; this was an
exploratory extension of the bounded construction, not another failure.
