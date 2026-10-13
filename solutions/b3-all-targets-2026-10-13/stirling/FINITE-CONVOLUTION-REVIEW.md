# Independent finite-convolution review

13 October 2026. Accept the partial proofs and five distinct failed
full-target routes per Q3436 and Q3437. Neither conjecture is solved or
refuted here. I read the frozen statements, result notes, attempts, code
and receipts, and the actual primary
[Campbell–Morales–Perales final paper](https://sigma-journal.com/2025/108/sigma25-108.pdf),
in particular Definitions 2.9/3.10, formula 5.4, Theorem 5.6 and its
adjacent remarks. I also read the exact scope of
[Campbell–Jalowy Lemma 3.10](https://arxiv.org/html/2605.31356v1).

## Partial proofs

In [MOMENT-RESULTS.md](../finite-convolutions/MOMENT-RESULTS.md), centering
is legitimate because translating either spectrum translates the two
additive inputs oppositely. Odd symmetrized coefficients cancel.
The convolution weights give e_2(Sym(p))=-S_A, and its e_4 term is exactly
2e_4(p)+(n-2)(n-3)e_2(p)^2/[n(n-1)].
Newton's identities then give the displayed E_A. Ordinary additive
real-rootedness makes the even half polynomial positive rooted, hence E_A>=0.

For n=4 the E_A upper bound S_A^2/6 follows from T_A>=S_A^2/4.
The output discriminant remainder is exactly 1/225 times
S_A^2S_B^2. For n=5 the sharp moment proof is complete: the constrained
sphere is compact; its two constraint gradients are independent; the
stationary cubic has at most three real coordinate values. A repeated
middle value gives a tangent direction with strictly negative second
variation, excluding a minimum. Outer multiplicities (1,3) or (3,1)
with one middle value contradict zero sum and strict ordering.
Multiplicities (2,2) give ratio 1/4. The two-value cases give
13/20 or 7/30, proving the stated minimum. This argument covers repeated
coordinates and the zero vector separately. It yields E_A<=5S_A^2/24,
and the output discriminant remainder is 25/5184 times S_A^2S_B^2.
Nonnegative sums/products of the real half-quadratic roots then prove
all Hermitian cases n<=5, including degenerate spectra.

For a rank-one perturbation of a scalar, every commutator is Hermitian,
trace zero and rank at most two. Its characteristic polynomial is
x^(n-2)(x^2-w), w>=0. Averaging preserves that form.
S_A=u^2(n-1)/n gives E w=u^2S_B/(n+1), as claimed. This is an all-degree
restricted theorem, without asserting the rank bound for other spectra.

In [RECTANGULAR-RESULTS.md](../finite-convolutions/RECTANGULAR-RESULTS.md),
the degree-two constant and discriminant are correct, with
0<c<1/2 for every alpha>-1. Nonnegative sum/product then prove the two
output roots nonnegative. The derivative identity also has the right
parameter shift: (m-1)+(alpha+1)=m+alpha, while the first factorial
changes by (m-k)/m. This proves every coefficient, not just the checked
range. It does not settle the antiderivative's critical-value signs.

The 2026 weak operator lemma explicitly tests T[z^n] for every n and
characterizes commuting operators. Its wording does not assert preservation
on every nonnegative-rooted input. No full Q3437 closure follows by
silently strengthening that lemma.

## Q3436 attempt count

| Route | Contract and precise failure | Decision |
|---|---|---|
| F01 | Centered moment induction; low degrees close, but n>=6 introduces c_6 and higher half-root obligations not implied by c_2/c_4. | One substantive failed full-target proof with useful partials. |
| F02 | Average paired Hermitian characteristic polynomials using only pointwise real-rootedness. | The generic average has half-discriminant -64; a fixed-orbit interlacing theorem remains missing. |
| F03 | Extend the forced half-polynomial multiplier to all positive-rooted inputs. | The unique n=4 multiplier has discriminant -284/225. |
| F04 | Make the conditional Hermite factorization automatic for actual spectra. | Actual q=(x^2-1)^2 forces a unique quotient with discriminant -64/9. |
| F05 | Certify joint upper-half-plane stability in x and the spectral parameters. | The degree-two joint symbol has the stated all-upper-half-plane zero. |

I accept F03/F04 as distinct worked routes, despite the source anticipating
that these extensions fail. F03 extracts the exact universal output kernel
and tests multiplicative identity inputs after discarding symmetrization
constraints. F04 preserves an actual real-rooted input and computes the
only possible quotient by the specific Hermite factor. The nonzero factor
coefficients make uniqueness exact. These are different sufficient
hypotheses, with different obstructions; neither is merely a repeated
literature search. The packet correctly attributes the source's warnings
and claims neither novelty nor a conjecture counterexample.

F02's two matrices are not asserted to come from one fixed commutator
Haar orbit. Thus it refutes only the pointwise-plus-averaging argument.
F05 enlarges real parameters to a joint complex domain, so it likewise
does not refute the actual real-spectrum target.

## Q3437 attempt count

| Route | Contract and precise failure | Decision |
|---|---|---|
| R01 | Construct a counterexample in the difficult alpha range, alongside exact low-degree analysis. | The pinned 8,400 actual outputs found none; low-degree theorems do not supply an all-degree result. Counted once. |
| R02 | Use the diagonal transfer to ordinary finite additive closure. | Actual (x-1)^2 transfers to a nonreal-rooted polynomial for every alpha>-1. |
| R03 | Recover real roots from positive critical points and alternating coefficients. | The relaxed antiderivative x^2-2x+2 defeats that proposed completion invariant. |
| R04 | Establish unrestricted real-root preservation for fixed-q convolution. | Negative-rooted p=(x+1)^2 gives a nonreal output with q=(x-1)^2. |
| R05 | Represent noninteger output as a positive normalized mixture of known alpha cases. | For p=q=(x-1)^2 the alpha=-3/4 constant 12/5 is below every available known-case constant. |

These are distinct counterexample construction, coefficient transfer,
degree induction, input-domain extension and parameter mixture routes.
R01 is a bounded construction effort, not proof in degrees 3,...,12.
The exact coefficients and bounded Arb screen are disclosed. No numerical
restart or source check is counted separately. R03/R04 distinguish their
relaxed inputs from actual counterexamples, and R05 leaves signed mixtures
and additional rescalings open.

The original [EXACT-CHECK.json](../finite-convolutions/EXACT-CHECK.json)
and its checker give coherent controls: 420 moment identities and
528 derivative identities, with the stated rational obstructions.
My acceptance of the all-size restricted claims rests on the symbolic
derivations above, not on extrapolating those finite receipts.

