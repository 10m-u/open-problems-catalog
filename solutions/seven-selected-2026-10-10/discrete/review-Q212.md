# Independent review of Q212

**Review date:** 2026-10-10. **Outcome:** no blocking mathematical issue found. The construction answers the catalog's nonnegative locally finite question negatively. It does not answer the separate standard-grading restriction.

Reviewed [212.md](../algebra/212.md) and [verify_212.py](../algebra/verify_212.py). The exact checker completed successfully. The conclusions below were also reconstructed without relying on the checker to establish module nonfreeness or the automorphism obstruction.

## Primary-source scope

Independently inspected Dramburg–Sandøy, [*On compatibility of Koszul- and higher preprojective gradings*](https://arxiv.org/pdf/2411.13283), Question 3.10, printed p. 15. Its hypotheses are local finiteness and a nonnegative grading, and its second part concerns a complete orthogonal primitive set. Independently inspected [Dramburg's September 2026 Question 6.2](https://arxiv.org/html/2609.03288v1#S6), which distinguishes a standard-grading question from the broader variant. The thesis endpoint timed out during this review; no claim is made to have independently read that endpoint.

The proposed algebra `M_2(k[t^2,t^3])` has a four-dimensional degree-zero component, zero degree-one component, and four-dimensional components in each degree at least two. Thus it satisfies the stated locally finite nonnegative hypotheses over an algebraically closed characteristic-zero field. It is not standard graded. The question does not require its degree-zero algebra to be basic.

## Reconstruction of the obstruction

The determinant identity gives an inverse to `S` over `B=k[t]`. Consequently `e=SE11S^-1` and `f=SE22S^-1` are complementary nonzero idempotents in `M_2(B)`. Their displayed entries have no coefficient of `t`, so they lie in `A=M_2(R)`, for `R=k+t^2k[t]`.

A useful intersection identity makes the descent to `A` exact:

$$
 eAf=eM_2(B)f\cap M_2(R).
$$

The inclusion from left to right is immediate. Conversely, an element `X` of the intersection satisfies `eXf=X`; since `X` is already in `A`, this expression places it in `eAf`. The same argument applies to diagonal corners.

In the normalized basis over `B`, the cross-corner consists of the unique elements `S(uE12)S^-1` with `u` in `B`. Modulo `t^2`, the sole potentially nonzero linear coefficient is the upper-right one, equal to `u_1+2u_0`. Thus the central `R`-module `eAf` is exactly the module

$$
 L_{-2}=\{u\in k[t]:u_1=-2u_0\}.
$$

It is an `R`-module because coefficients of `t` vanish in `R`. Its extension inside `B` generates the unit ideal: `1-2t` and `t^2` belong to it and have no common polynomial factor. If it were isomorphic to `R`, the image of `1` under an isomorphism would be a generator `u` with `L_-2=Ru`. Extending gives `Bu=B`, forcing `u` to be a nonzero constant. Such a constant does not satisfy `u_1=-2u_0` in characteristic different from two. This proves nonfreeness, without assuming that a nonfree ideal is automatically nonprincipal or invoking a Picard-group classification.

For the diagonal corners the corresponding coefficient condition is simply `u_1=0`. Hence each corner is isomorphic to the domain `R` and has no nontrivial idempotents. This proves primitivity of both `e` and `f`.

Every nonzero homogeneous idempotent has degree zero. A possible primitive target in `M_2(k)` is a rank-one idempotent, so constant change of basis makes its complementary cross-corner a free rank-one `R`-module. An arbitrary algebra automorphism induces an automorphism of the center `R`, not necessarily the identity. Nevertheless its map between cross-corners is semilinear for that center automorphism. A semilinear bijection with an invertible coefficient-ring map preserves freeness of rank one, as shown by pulling back a target basis vector. Thus allowing outer automorphisms cannot evade the obstruction.

This rules out all homogeneous targets, and therefore also the particular degree-zero targets in Question 3.10. It covers the whole orthogonal set because an automorphism carrying that set to homogeneous idempotents would in particular carry `e` to one.

## Verification limits

The integer-polynomial checker verifies the identities and reductions used in the construction. The infinite module argument, primitivity argument, and center-semilinear obstruction are mathematical proofs, not conclusions inferred from finitely many polynomial examples. Characteristic zero is enough for a counterexample to the universal question; no conclusion for characteristic two is needed or claimed.
