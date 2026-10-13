# Exact rectangular-convolution identities

Partial results for Q3437; independent review accepted (ROOT-REVIEW.md#finite-convolution-final-proofs-and-counts). Definition 3.10 in
[Campbell–Morales–Perales](https://sigma-journal.com/2025/108/sigma25-108.pdf)
uses falling factorials, including (m+alpha)_k.

For m=1 the output is x-(a+b). For m=2 write the elementary coefficients
of the inputs as (1,S,P) and (1,T,Q). The output is

    x^2-(S+T)x+P+Q+c ST,
    c=(1+alpha)/(2(2+alpha)).

For alpha>-1, 0<c<1/2. Its discriminant is

    (S^2-4P)+(T^2-4Q)+(2-4c)ST >= 0.

All input roots are nonnegative, so S,T,P,Q>=0 and the first two
discriminants are nonnegative. The output roots have nonnegative sum
and product, hence are nonnegative. This proves the full target for
m<=2 and every permitted alpha, including zero or repeated input roots.
No originality claim is made.

## Differentiation identity

In every m>=2, exact coefficient comparison gives

    (p boxplus_m^alpha q)'/m
      = (p'/m) boxplus_(m-1)^(alpha+1) (q'/m).

Indeed e_k(p'/m)=(m-k)e_k(p)/m, (m-1)_k=(m-k)(m)_k/m,
and the second falling factorial on the smaller side is again
(m+alpha)_k. This proves the identity without a real-root hypothesis.
It permits a degree induction only if one also proves the required signs
of the antiderivative at every critical point. Real nonnegative critical
points alone do not suffice: x^2-2x+2 has critical point 1 and no real root.

## Scope of the 2026 operator theorem

[Campbell–Jalowy, arXiv:2605.31356v1](https://arxiv.org/html/2605.31356v1)
Lemma 3.10 characterizes operators commuting with rectangular
differentiation whose values on x^n have nonnegative roots for all n.
It tests monomials, not every positive-rooted input. Its formulation does
not prove arbitrary p boxplus_m^alpha q is positive rooted. Appendix A
and equation (7.2) were read; no all-input closure is inferred from them.

The bounded screen uses exact rational coefficients and Arb enclosures.
It found no counterexample among 8,400 cases, degrees 3 through 12,
seven rational alpha values and the pinned seed. It is a failed bounded
counterexample construction, not a proof in any new degree.
