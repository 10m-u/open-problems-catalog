# A second-order prefix for Q2400

The full target is simultaneous log-concavity of the entire independent-set
row of G(n,d/n), for every sufficiently large fixed d, with probability
tending to one. It remains open locally. This partial strengthens the
previous n^(1/3) initial range to n^(2/5), with a weaker probability bound
that still tends to one. All constants below are explicit. No novelty
claim is made.

## Deterministic second-order criterion

For a simple graph on n vertices let m be its edge count and
W=sum_v binom(deg(v),2) its number of unordered adjacent edge pairs.
For l<=n put

    mu_l = m (l)_2/(n)_2,
    nu_l = W (l)_3/(n)_3 + [binom(m,2)-W] (l)_4/(n)_4.

Falling factorial ratios with l below the subscript are zero. For n>=4,
the probability that a uniformly selected l-set is not independent is
bounded below and above by the first two inclusion--exclusion sums:

    1-mu_l <= x_l/binom(n,l) <= 1-mu_l+nu_l.       (1)

Indeed a forbidden edge is present with probability (l)_2/(n)_2;
two distinct edges have a union of three vertices exactly when they
are adjacent, otherwise four. No higher intersections are assumed.

Fix 1<=k<=n-1 and assume

    mu_(k+1)<=1/2,   nu_(k+1)<=1/[12(k+1)].        (2)

Both mu and nu increase with their index. Write L_l=1-mu_l>=1/2
for l=k-1,k,k+1, and v=nu_(k+1). With a=m/[n(n-1)],

    L_k^2-L_(k-1)L_(k+1)
      =2a L_k+4a^2 k(k-1)>=0.                    (3)

This identity retains the cancellation lost by separately comparing
each count with the empty-graph row. Put

    R=binom(n,k-1)binom(n,k+1)/binom(n,k)^2,
    T=1-R=(n+1)/[(k+1)(n-k+1)]>=1/(k+1).

By (1), the normalized lower bound on x_k^2 minus the upper bound
on x_(k-1)x_(k+1) is at least

    L_k^2-R[L_(k-1)+nu_(k-1)][L_(k+1)+nu_(k+1)]
      >= T L_k^2-(2v+v^2)
      >= 1/[4(k+1)]-1/[6(k+1)]-1/[144(k+1)^2]>0.

In the first inequality use (3), R<=1 and 0<=L_l<=1. Thus (2)
proves the actual graph inequality x_k^2>=x_(k-1)x_(k+1).
Support has no internal zeros for any graph: every subset of an
independent set is independent. The criterion is sufficient only.

## Random graph and an n^(2/5) simultaneous prefix

Fix d>0, n>=max(6,d), and set p=d/n. The edge count has mean
d(n-1)/2. Chernoff's bound gives

    P(m>dn)<=exp[-d(n-1)/6].

Each wedge uses two specified edges. Its expectation is

    E W = n binom(n-1,2) p^2 <= d^2 n/2.

Markov's inequality therefore gives

    P(W>d^2 n log n)<=1/(2 log n).

On the intersection of these events, for every l<=n, elementary
falling-factorial bounds (n)_3>=(n/2)^3 and (n)_4>=(n/2)^4
for n>=6 give

    mu_l <= d l^2/(n-1),
    nu_l <= 8d^2 [l^4+(log n)l^3]/n^2.             (4)

The second bound uses binom(m,2)-W<=m^2/2. Keeping the exact
first term would improve constants; no independence of wedges is needed.

Define

    L=floor[(n^2/(384d^2))^(1/5)],  K=L-1.

For any n satisfying L>=max(2,log n), L<=n and
dL^2/(n-1)<=1/2, (4) implies

    12l nu_l <=96d^2[l^5+(log n)l^4]/n^2
              <=192d^2 L^5/n^2<=1/2<1

for every 1<=l<=L. Consequently the deterministic criterion applies
simultaneously to every 1<=k<=K. For each fixed d>0 all the displayed
size conditions hold for all sufficiently large n, and

    K ~ (384d^2)^(-1/5) n^(2/5),
    P(all x_k^2>=x_(k-1)x_(k+1), 1<=k<=K)
       >=1-exp[-d(n-1)/6]-1/(2 log n) ->1.

This establishes a larger growing prefix with an explicit bound. The
previous exponentially small failure probability at the smaller prefix
remains a separate result; it is not replaced by an exponential claim
here. d=0 is the empty graph and has a fully log-concave binomial row.

## Full-target limitation of this route

At linear k=rho n with any fixed rho>0 and m of order n, mu_k is of
order n. The first Bonferroni lower bound1-mu_k is then negative; it
cannot supply the squared nonnegative lower bound used in (3).
The second-order error bounds also cease to be small. Extending this
specific truncation to the full row would require an unbounded-order
resummation or a different comparison. This developed partial therefore
does not resolve Q2400 and resets no failure counter.
