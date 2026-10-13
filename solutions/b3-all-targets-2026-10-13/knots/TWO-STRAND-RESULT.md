# Exact two-strand ruling formula and all-size row inequalities

This is an elementary derivation of a subfamily already covered by the primary [Su–Xie–Yu, Theorem 5.4 and Corollary 5.7](https://arxiv.org/pdf/2603.27888v2). It supplies no new full resolution of Q2924 and resets no counter.

For beta=sigma1^m on two strands, let F_m(z) count w0-to-w0 walks by the number of stays. There are only two states. At w0 the generator is a descent, allowing either a swap to the other state or a z-weighted stay. At the other state it is an ascent, so the return swap is mandatory. Thus

    F_0=1, F_1=z, F_m=z F_(m-1)+F_(m-2).

Each walk is tiled by a one-step stay or a two-step out-and-back swap. Choosing k two-step tiles gives binom(m-k,k) walks with m-2k stays, so

    F_m(z)=sum_(0<=k<=floor(m/2)) binom(m-k,k) z^(m-2k).

Write m=2d+e, e in {0,1}. The number of closure components is b=2-e. Since R=z^-2 F_m, the normalization removes z^e. Its row is

    a_j=binom(d+j+e,d-j),       0<=j<=d.

Every coefficient is positive. For j<d,

    a_(j+1)/a_j = (d+j+e+1)(d-j) / [(2j+e+2)(2j+e+1)].

The numerator equals d(d+e+1)-j(j+e+1), which decreases as j increases, while the positive denominator increases. These ratios therefore decrease, proving a_j²>=a_(j-1)a_(j+1), with no internal zeros, for every m. Boundaries m=0,1 have one coefficient and no inequalities; an empty braid has two components and normalized row [1].

The exact checker compares all formulas against the permutation-walk DP for 0<=m<=60, and independently enumerates switch masks for separate small controls. The proof, rather than those finite controls, handles all m.

## All-size composition defect

In the two-state order (w0,other), the switch-count transfer matrix is

    M(z)=[[z,1],[1,0]].

For a>=1 its upper-left entry in M^a is F_a, and both off-diagonal entries are F_(a-1). This follows directly by multiplying M and the same two-step recurrence (with F_-1=0 at a=1). Hence for every a,b>=1,

    F_(a+b)=F_a F_b+F_(a-1) F_(b-1).                 (6)

The second summand counts paths whose intermediate endpoint is the other state. It is strictly nonzero for all a,b>=1. Thus same-strand concatenation never gives just the product of the two returning-walk polynomials.

Let G_m(w)=z^(-e_m)F_m(z), w=z², e_m=m mod2. Converting (6) with the component normalization gives the exact formula

    G_(a+b)(w)=w^(e_a e_b) G_a(w)G_b(w)
              +w^((1-e_a)(1-e_b)) G_(a-1)(w)G_(b-1)(w).

Both exponents are0 or1. This identifies the precise extra term and the parity shifts omitted by a naive multiplicative proof. The checker verifies400 pairs1<=a,b<=20; the matrix proof handles all positive a,b. The two-strand formula already proves log-concavity of the sum in this subfamily. No theorem about arbitrary sums of log-concave factors is inferred.
