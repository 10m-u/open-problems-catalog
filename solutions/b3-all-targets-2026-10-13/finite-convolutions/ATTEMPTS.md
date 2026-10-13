# Finite-convolution attempts

Exact frozen targets are Q3436 (all Hermitian commutators) and Q3437
(all alpha>-1 generalized rectangular convolutions). This packet records
failed attempts at those full targets and the partial results separately.
Five routes per target are proposed for independent audit; no conjecture
counterexample or all-degree closure is asserted. All source and execution
errors count zero. See the two result notes and EXACT-CHECK.json.

## Q3436-F01: centered moments and degree induction

Attempt: express every coefficient using centered spectral moments, then
prove nonnegative roots of the half polynomial by moment inequalities in
each degree. Exact coefficient extraction produces c_2 and c_4 in
MOMENT-RESULTS.md. A sharp constrained fourth-moment argument completes
degrees 1 through 5, and a rank-two argument completes all degrees when
one input is rank one modulo scalars. The all-degree extension fails at
the next obligation: n>=6 introduces c_6 and a cubic (then higher-degree)
half polynomial, for which c_2,c_4 inequalities supply no root certificate.
No inductive relation controlling every higher half-polynomial root was
obtained. This is a partial proof and one failed full-target route.

## Q3436-F02: expectation of Hermitian characteristic polynomials

Attempt: use pointwise Hermitian real rootedness, paired spectra, and
convexity to pass to the expected characteristic polynomial. This would
need a common-interlacing theorem for the actual Haar orbit. Real
rootedness and spectral pairing by themselves do not provide it:

    [(x^2-1)^2+(x^2-9)^2]/2 = x^4-10x^2+41.

The half quadratic has discriminant -64. Both summands are characteristic
polynomials of Hermitian matrices with paired spectra. Thus averaging in
that relaxed class fails, and the desired common-interlacing certificate
for a fixed commutator orbit remains missing. These two generic matrices
are not claimed to belong to one such orbit; this is a proof obstruction,
not a counterexample to Q3436.

## Q3436-F03: a universal positive half-polynomial multiplier

Attempt: discard the special symmetrization constraints and use finite
multiplicative closure on all nonnegative-rooted half polynomials. Extract
the multiplier forced by every coefficient of formula 5.4. For n=4,
m=2 it has elementary vector (1,16/15,3/5), hence polynomial

    K(y)=y^2-(16/15)y+3/5,
    discriminant(K)=-284/225.

The forced kernel is not nonnegative rooted. Taking the multiplicative
identity inputs (y-1)^2 would output K and disproves the relaxed closure.
The identity inputs need not be realizable symmetrizations; that is exactly
the discarded constraint. The source already cautions that this multiplier
is not real rooted (Remark 5.5); the present exact extraction quantifies
the failed extension, not a new source theorem or conjecture counterexample.
It does not rule out an argument that preserves the special input constraints.

## Q3436-F04: make the Hermite-factor hypothesis automatic

Attempt: use the source's conditional Theorem 5.6 in every instance by
recovering a nonnegative-rooted finite multiplicative quotient. For the
actual allowed input q(x)=(x^2-1)^2, its symmetrization is

    Sym(q)=x^4-4x^2+8/3,
    Q_2(Sym(q))=y^2-4y+8/3.

The theorem's monic Hermite factor H_2[1-1/4; dot] has elementary vector
(1,3,3/4). Every coefficient is nonzero, so the finite multiplicative
quotient is unique, with vector (1,8/3,32/9). Its discriminant is -64/9.
Thus no admissible quotient exists for this actual input, and the conditional
proof cannot automatically cover every q. Remark 5.7 already states that
the condition is restrictive; this worked actual-spectrum obstruction is
filed without claiming a new counterexample to the conjecture.

F03 and F04 share finite multiplicative algebra but impose different
contracts: F03 extends the output multiplier to every positive-rooted
half input; F04 tests an extra factorization on actual input spectra.

## Q3436-F05: joint stability in the spectral parameters

Attempt: certify the expected polynomial as upper-half-plane stable jointly
in x and the eigenvalue parameters, then specialize those parameters to
real numbers. In degree two, fix B with spectrum {0,1}. Exact coefficient
extraction gives

    F(x,a_1,a_2)=x^2-(a_1-a_2)^2/6.

Set a_1=i, a_2=3i, x=i sqrt(2/3). All three variables have positive
imaginary part and F=0. This stronger joint-stability property fails even
in degree two where the actual real-spectrum target holds. The attempted
joint-symbol proof therefore fails; a stability certificate respecting
differences or a smaller complex domain might still work.

## Q3437-R01: construct an actual counterexample and settle low degrees

Attempt: search the difficult noninteger alpha range while deriving exact
low-degree conditions. RECTANGULAR-RESULTS.md proves every permitted alpha
for m<=2. The pinned actual-input search checked 8,400 convolutions in
degrees 3 through 12 and found no counterexample. Inputs include zeros,
repeated roots and roots with differing magnitudes; the seven alpha values
are -99/100,-9/10,-3/4,-1/2,-1/4,1/4,3/2. Exact rational coefficients and
Arb root enclosures generated no candidate requiring an exact follow-up.
This bounded construction route did not solve the all-degree target.
The search does not prove real rootedness for any whole new degree.

## Q3437-R02: transfer to ordinary finite additive convolution

Attempt: apply the diagonal coefficient map

    e_k(T_alpha p)=e_k(p)/(m+alpha)_k

and use ordinary additive closure, since
T_alpha(p boxplus_m^alpha q)=T_alpha(p) boxplus_m T_alpha(q).
This map is the one in source Remark 3.11. It must preserve nonnegative
real roots for this closure argument to apply. Already at m=2, for the
allowed p=(x-1)^2,

    T_alpha(p)=x^2-2x/(2+alpha)+1/[(2+alpha)(1+alpha)]

has discriminant -4/[(alpha+1)(alpha+2)^2]<0. Thus this transfer does not
supply real-rooted intermediate inputs, for any alpha>-1. The identity
itself remains valid; the attempted proof through its intermediates fails.

## Q3437-R03: differentiation and Rolle induction

Attempt: reduce degree through the exact derivative identity in
RECTANGULAR-RESULTS.md, using positive real critical points and alternating
coefficients to recover positive real roots. The identity is proved for
every coefficient and checked exactly in 528 cases. However these data do
not determine the critical values of the antiderivative. The monic
x^2-2x+2 has alternating elementary signs, positive constant, and derivative
with sole root 1, yet is not real rooted. This relaxed induction invariant
therefore fails. It is not claimed to be an actual convolution output of
allowed inputs. The required all-critical-value signs were not obtained.

## Q3437-R04: an unrestricted real-root-preserving operator symbol

Attempt: fix q and prove its convolution operator preserves all real-rooted
p, allowing the standard real-root-preserver framework before checking
output nonnegativity. For m=2 take p=(x+1)^2 and q=(x-1)^2. The output is

    x^2+2/(2+alpha),

which is nonreal rooted for every alpha>-1. The p input has negative roots
and is outside Q3437. Thus the attempted unrestricted operator theorem is
false; any successful operator proof must retain the input's nonnegative
root restriction. This obstruction is separate from R02's diagonal map.

## Q3437-R05: positive mixtures of the known matrix dimensions

Attempt: represent a noninteger parameter convolution as a positive mixture
of the proved alpha=-1/2 and nonnegative integer parameter convolutions,
then seek interlacing to preserve roots. Even the coefficient identity
required before interlacing is impossible for p=q=(x-1)^2. The output
constant is (6+4alpha)/(2+alpha), strictly increasing for alpha>-1. At
alpha=-3/4 it is 12/5; every known-case constant is at least 8/3.
No normalized nonnegative mixture of those cases has constant 12/5.
This disproves this precise mixture representation, even with input-dependent
weights. Other integral models, signed combinations or extra spectral
rescalings are not excluded; none was obtained by this route.

## Review and counting

The numerical search and its low-degree theorem constitute one R01 route,
not multiple failures. The newer rectangular-differentiation paper was read
for scope and is not an additional failure. F03 and F04 are explicit attempted
extensions with worked obstructions, despite their failure being anticipated
in source remarks; the reviewer should reject their counts if that makes
them insufficiently substantive. No full solution intervened between the
five attempts for either target. Stop decisions are pending that review.
