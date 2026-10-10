# Independent internal review of Q2305

Date: 2026-10-09. Reviewer: the discrete-problems agent, separate from the algebra-problems author.

**Verdict: no blocking mathematical issue found.** The rectangular-domain/conjugation model gives the requested isomorphism description over every field in every finite dimension. It specifies its elements, equality relation, multiplication, inverses, and boundary cases.

## Source and scope

Independently opened [Araújo et al., arXiv:2605.00041v1](https://arxiv.org/html/2605.00041v1), read Definition 3.8, the adjacent generator convention, and Problem 7.9, and compared them with Q2305 in the catalog. The source asks for finite-dimensional vector spaces over an arbitrary field. The report's ordinary function-composition convention is explicit and consistent within its model.

## Generator domains and invertible extensions

The identity

\[
D_{g,h}=D(\ker(gh-I),\operatorname{im}(gh-I))
\]

follows independently from the two equations \((gh)a=a=a(gh)\). Rank-nullity makes the dimensions complementary; it does not imply a direct sum. The report preserves this distinction, so nonsemisimple eigenvalue-one cases are included.

Re-derived the Fitting argument for \(t=gh\), \(s=hg\). For a stable power, \(h\) gives a bijection between the stable image of \(t\) and that of \(s\): injectivity follows from \(hv=0\Rightarrow tv=0\), and surjectivity from \(s^{m+1}=ht^mg\). The complements have equal dimension and can be matched arbitrarily to extend this restriction to an invertible \(H\).

For every domain element \(a\), its image is in the stable image of \(t\), it vanishes on the nilpotent part, and \(at=a\). These identities give \(HaH^{-1}=hag\) on the stable image of \(s\). Both sides vanish on its nilpotent part, since \(tg=gs\). Thus each original partial inner automorphism is the restriction of a full conjugation. This proof uses finite-dimensional linear algebra and remains valid over nonclosed fields and in positive characteristic.

## Exact generated domain semilattice

Checked both inclusions in the claimed semilattice. Intersections take the form

\[
D(U,W)\cap D(U',W')=D(U\cap U',W+W').
\]

Conjugation transports both subspaces by the same invertible map. A nonzero intersection involving a proper initial domain cannot acquire full image allowance or a zero mandatory kernel, so the two excluded one-sided families \(D(U,0)\) and \(D(V,W)\) do not accidentally enter the model.

For the reverse inclusion, the two dimension cases are valid. If \(\dim U+\dim W\leq n\), coordinate subspaces in a complement of \(U\) construct finitely many superspaces of dimension \(n-\dim W\) whose intersection is \(U\). If the sum is at least \(n\), coordinate subspaces inside \(W\) of dimension \(n-\dim U\) span \(W\). The strict nonzero/proper hypotheses ensure the needed coordinate sizes. Every component is an actual identity generator obtained from a linear map with prescribed kernel and image. This proves generation over finite and infinite fields alike.

## Equality, multiplication, and boundaries

Checked the rank-one argument for equality of representatives. A nonzero domain recovers \(U\) as the span of all images and \(W\) as the intersection of all kernels. A matrix commuting with every \(u\otimes\ell\), \(u\in U\), \(\ell\in W^\perp\), must act by one common scalar on \(U\) and induce that same scalar on \(V/W\). Equivalently it is \(\lambda I+N\) with \(N(U)=0\) and image contained in \(W\). Invertibility forces \(\lambda\ne0\). The converse follows from \(Na=aN=0\).

The multiplication formula uses the correct preimage \(K^{-1}D\) when \(c_K\) is applied first, and conjugations compose to \(c_{HK}\). The inversion formula transports the domain to \(D(HU,HW)\). All original generators contain and fix the zero matrix, so the generated monoid's zero is the identity on \(\{0\}\); it is not the empty partial map. The full domain gives the units, with scalar conjugations identified, hence \(\operatorname{PGL}(V)\) in positive dimension. The dimension-zero singleton and dimension-one two-element cases agree with the construction.

Recomputed the dimension-two finite-field cardinality from the two types of pairs of lines. The stabilizers have orders \(q(q-1)\) when the lines agree and \((q-1)^2\) when they differ. Adding the units and zero gives exactly \(q^4+4q^3+2q^2-2q\).

## Computational evidence reviewed

Read the complete `check_q2305.py` implementation and ran it from the algebra folder. It returned `PASS`. Direct closure of all original generator maps agrees with the model for \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\), with 52 and 201 elements respectively. The checker verifies every model composition, tests the equality quotient, and verifies that 100 initial domains in dimension three over \(\mathbb F_2\) generate the predicted 198 domains. Its singular, nonsemisimple control agrees with an invertible extension on the entire original domain.

These finite controls support the implementation and boundary cases. The general theorem rests on the source-aligned linear-algebra arguments reviewed above.

## Limits and editorial note

This is internal AI-assisted review, not external peer review or proof-assistant verification. No claim of literature priority follows from it. The original title's phrase “finite matrix monoid” could suggest finite cardinality; “finite-dimensional matrix monoid” more accurately describes the arbitrary-field scope. This wording issue does not affect the proof.
