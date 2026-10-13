# Q3568: ordinal sums of layers of size at most two

Local all-size partial proof, independent review accepted; no novelty claim.
The full question asks nonnegative ordinary coefficients for every
width-two poset. [Ferroni--Morales--Panova](https://arxiv.org/html/2503.16403v3),
Section7.1, reduces the general question to the linear coefficient and
retains Conjecture7.1. Skew cell posets and their associated two-chain
posets are distinct, and the source's cell-poset theorem does not settle
this question in general.

We prove the assertion for every weak order that is an ordinal sum of
antichains of size one or two. Let N be its number of elements and k
its number of two-element layers. Thus N>=2k. Empty and chain cases
are included.

## Exact order polynomial

Naturally label the layers consecutively. A linear extension can choose
either order in each two-element layer. The second order contributes
one descent, while boundaries between layers never contribute descents.
The descent polynomial is therefore(1+z)^k, and the standard weak
P-partition expansion gives

    N! Omega(t)=sum_(j=0)^k binom(k,j)
                       product_(s=-j)^(N-1-j)(t+s).             (1)

Put b=N-k. The common factor in(1) is

    t^(rising b)=product_(s=0)^(b-1)(t+s).

After extracting it, the remaining polynomial is

    Q_k(t;b)=sum_(j=0)^k binom(k,j)
          product_(a=1)^j(t-a)
          product_(a=0)^(k-j-1)(t+b+a).                         (2)

Formula(1) and its factorization are exact finite identities.

## Vertical root line for the residual factor

The exponential generating function of(2), with b fixed, is

    sum_(k>=0) Q_k(t;b) z^k/k!
       =(1+z)^(t-1)(1-z)^(-t-b).

Let x=t+(b-1)/2 and c=(b+1)/2. This becomes
(1-z^2)^(-c)((1+z)/(1-z))^x. Logarithmic differentiation gives

    Q_0=1, Q_1=2x,
    Q_(k+1)=2x Q_k+k(k+b)Q_(k-1).                              (3)

Define R_k(y)=i^(-k)Q_k(iy;b), where Q is now expressed in x.
Then R_0=1,R_1=2y and

    R_(k+1)=2y R_k-k(k+b)R_(k-1).

For b>0 its coefficient k(k+b) is positive. The usual elementary
interlacing induction proves that every R_k has simple real roots:
at each root of R_k, R_(k+1) has the opposite sign to R_(k-1),
yielding roots in every consecutive gap, with one extra on each
outer side from the positive leading coefficient. The starting pair
is immediate. Rescaling to monic polynomials gives the same induction
with coefficient k(k+b)/4>0.

Thus every root of Q_k, as a polynomial in t, has real part
-(b-1)/2. Its coefficients are real and its leading coefficient is
2^k. For b>=1, write c_0=(b-1)/2>=0. The factors are positive
multiples of real linear factors t+c_0 and conjugate-pair factors
(t+c_0)^2+y^2. Each has nonnegative ordinary coefficients, and so
does Q_k. The rising factor also has nonnegative coefficients.
Consequently every ordinary coefficient of Omega is nonnegative.

For a nonempty weak order N>=2k implies b>=1 except k=0, where
the direct chain formula t^(rising N)/N! proves the claim. The empty
poset has Omega=1. This completes the all-size partial theorem.

The argument permits arbitrary numbers and positions of singleton
layers, and arbitrary k. It does not cover two-chain posets with
incomplete cross-layer comparabilities. No reduction of every width-two
poset to these layers has been proved.
