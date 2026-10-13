# Q3579: complementary-sum Chern plethysm

13 October 2026. The exact target is final Problem 26 of
[Libman–Orelowitz, Combinatorics and Representation Theory of Special Cases
of Chern Plethysm](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v31i2p20),
DOI 10.37236/12430. I read the final local paper
texts/papers/collections-6d715b4a78e968d2.txt.gz, in particular Definitions
2/4, Lemma 5, Corollary 7 and the concluding problem. The frozen statement
is in ../QUESTION-SNAPSHOT.json, stable ID c19d35eac63099d2b01b.

For n>=1, partitions lambda,mu of the same size and length at most n, put
X=sum x_i and
\[
\Phi_n(s_\lambda)=s_\lambda(X-x_1,\ldots,X-x_n),\qquad
c_{\lambda\mu}(n)=[s_\mu]\Phi_n(s_\lambda).
\]
The request is a general cancellation-free combinatorial interpretation
of these coefficients. The geometric Schur-positivity theorem and a
signed exact coefficient algorithm do not provide such a rule.
The source's row/column input rules and selected output-shape rules are
preserved as prior results. A bounded current primary-source search found
the final paper and its preprint, without establishing a later full rule;
no exhaustive current-openness claim is made.

## Exact degenerate scopes

At n=2, the substituted alphabet is (x2,x1). By symmetry,
c(lambda,mu;2)=1 if lambda=mu and 0 otherwise, for every permitted pair.
This is a full rule at n=2, with the unique empty object or singleton object.
At n=1, every positive-degree substituted polynomial is zero; degree zero
has coefficient one. These special cases do not resolve the all-n target
or reset its full-target failure counter.

<a id="q3579-a1"></a>
## A1: a crystal on forbidden-index decorated tableaux

The monomial model is entirely positive. Choose a semistandard tableau T
of outer shape lambda with labels i in [n]. Independently decorate each
box by a color j!=i. Its weight is the product of x_j over boxes.
Summing over these objects is exactly Phi_n(s_lambda). Try to partition
them into type-A highest-weight crystal components; highest-weight
objects would then count the desired Schur coefficients.

A single decorated box is a pair (i,j), i!=j. There are n-1 pairs at each
color j, so identify it with copy a of the vector crystal, where a is the
rank of i in the increasing list [n]\{j}. Under f_j, replace color j
by j+1, keep a fixed, and recover the new forbidden index from that list.
Extend by the ordinary tensor-crystal rule on the row reading word.

This candidate does not preserve the tableau condition. At n=3 and
lambda=(2), take T=(2,2) with both decorations color 1. Both boxes have
copy a=1. The standard row-crystal move f1 sends colors (1,1) to (1,2).
The first forbidden index stays 2, while the second becomes 1, because
copy 1 at color 2 has forbidden index 1. Thus the new forbidden-index
row is (2,1), which is not semistandard. The decorated object set is not
closed under this explicitly defined candidate crystal.

A related full-Schur-functor shortcut already disagrees in degree two.
Replacing the single-box model by n-1 copies of the vector representation
would give s_lambda evaluated on an alphabet with every x_i repeated
n-1 times. At n=3 and lambda=(2), this is
\[
h_2(X+X)=3s_{(2)}+s_{(1,1)}.
\]
Direct substitution instead gives
\[
h_2(X-x_1,X-x_2,X-x_3)=3s_{(2)}+2s_{(1,1)}.
\]
At x1=x2=x3=1 their dimensions are 21 and 24, respectively.
The Chern-root operation is not that character-alphabet operation.

**Full-target outcome: failure 1.** The positive monomial model survives,
but the specified crystal lift and representation replacement fail.
This does not exclude another crystal with a nonlocal repair of the
forbidden-index tableau, nor does it refute Schur positivity. A complete
route would need operators that preserve this object set, satisfy the
crystal axioms and give the required complete highest-weight decomposition.

<a id="q3579-a2"></a>
## A2: subtraction-free assembly from the known row/column rules

Try to reduce arbitrary input shapes to products and nonnegative sums of
single-row/single-column inputs. The source supplies positive rules for
each such factor; ordinary LR multiplication would keep the resulting
Schur expansion positive and combinatorial. This route requires Phi_n(s_lambda)
to lie in the nonnegative cone of same-degree products of transformed
h_k and e_k.

The requirement already fails at n=3, degree three, lambda=(2,1).
Write vectors in the Schur basis (s3,s21,s111). Every degree-three product
of complete and elementary generators is one of the following, up to
the equality h1=e1:
\[
\begin{array}{c|c}
\text{product after }\Phi_3 &\text{coefficient vector}\\\hline
h_3&(4,5,0)\\
e_3&(0,1,0)\\
h_2h_1&(6,10,4)\\
e_2h_1&(2,6,4)\\
h_1^3&(8,16,8).
\end{array}
\]
Each vector satisfies the linear inequality v21-v3-v111>=0.
Direct actual extraction gives
\[
\Phi_3(s_{21})=2s_3+5s_{21}+4s_{111},
\]
which has v21-v3-v111=-1. It cannot be a nonnegative combination of
these factor-counts, even with arbitrary nonnegative real coefficients.

For example the actual Jacobi–Trudi/Pieri identity is
Phi_3(s21)=Phi_3(e2)Phi_3(e1)-Phi_3(e3); it needs a subtraction.
This is an obstruction to the specified factor-assembly cone, not to
a rule that takes a carefully described subset or pairs combinatorial
objects. It also does not exclude generators outside the row/column
family or a new global model.

**Full-target outcome: failure 2.** The row/column rules cannot be promoted
to the general rule by this subtraction-free assembly alone. The exact
degree-three separating inequality supplies the missing obstruction.

<a id="q3579-a3"></a>
## A3: a full symmetric-group homological lift before finite-n truncation

The source's Section 6 realizes a column case as a Frobenius characteristic
of homology concentrated in one degree. Try to lift the general
Corollary 7 alternating expression to symmetric functions, then build
a complex concentrated in one degree whose basis would provide a positive
representation model. This requires the *untruncated* symmetric function
\[
\widehat\Phi_n(s_\lambda)=
\sum_{\nu\subseteq\lambda}(-1)^{|\nu|}
\frac{f^{\lambda/\nu}\prod_{(r,c)\in\lambda/\nu}(n-r+c)}
{(|\lambda|-|\nu|)!}\,s_\nu s_1^{|\lambda|-|\nu|}
\]
to be Schur-positive at every allowed input n,lambda.

It is not. Take n=2, lambda=(3), a valid input of length one. The content
products give
\[
\widehat\Phi_2(s_3)
=4s_1^3-6s_1^3+4s_2s_1-s_3
=s_3-2s_{111}.
\]
The coefficient -2 cannot be the multiplicity of an irreducible in a
genuine symmetric-group module. A complex with this Euler characteristic
cannot have homology concentrated in a degree with the proposed positive
overall sign. This is an exact obstruction to this stable lift.

The offending output partition has length three, so it vanishes in two
variables and is outside the catalog's permissible output range. Indeed
the actual finite-variable target at n=2 remains the identity rule already
proved. The failure is the route's additional requirement, not a catalog
counterexample. For n>=|lambda| all output lengths fit in n variables,
and the geometric positivity no longer gives this obstruction; an
abstract existence of a module still supplies no explicit combinatorial
basis. A general route needs to handle the finite-n quotient from the
start, or exhibit a different model not having this full stable character.

**Full-target outcome: failure 3.** The concentrated-homology strategy
with this untruncated Euler characteristic cannot work uniformly over
the target's n-range.

<a id="q3579-a4"></a>
## A4: inductive construction from the forward Pieri equations

Because Phi_n is a ring homomorphism and Phi_n(s1)=(n-1)s1, applying
Pieri gives the exact nonnegative equations
\[
\sum_{\rho:\rho/\lambda\text{ one box}}c_{\rho\mu}(n)
=(n-1)\sum_{\nu:\mu/\nu\text{ one box}}c_{\lambda\nu}(n).
\tag{1}
\]
Try to build the degree-d rule from all degree-(d-1) rules, plus the
known row/column input rules and one/two-row or column output rules.
The forward equations do not isolate the required coefficients.

Here is an exact actual-data nonuniqueness control. At n=6,d=6, order
the input partitions as
\[
6,51,42,411,33,321,3111,222,2211,21111,111111.
\]
For every degree-five input lambda, the incidence sum of the entries of
\[
v=(0,0,-1,1,2,-1,0,1,0,0,0)
\tag{2}
\]
over its covers is zero. The row/column input entries of v are also zero.
Thus adding v to the degree-six column indexed by mu=(321) preserves
every equation (1) for that column, every known row/column input value,
and every already specified special-output column.

The actual column at n=6, obtained independently from Corollary 7, is
\[
(2310,5400,5949,4491,2597,4879,1565,975,1071,204,6).
\]
Both this column and this column plus v consist of positive integers,
yet differ at several still-required coefficients. The full incidence
matrix with the two row/column inputs fixed has rank nine on eleven
unknowns; (2) is one of two independent kernel vectors.

This is not a second possible Chern plethysm. It shows that the stated
forward induction information is insufficient for a unique rule.
Further identities, compatibility between columns, or an additional
combinatorial refinement could select the true column; those are
extra obligations beyond (1) and the known special-shape rules.

**Full-target outcome: failure 4.** Forward Pieri induction with these
boundary rules does not determine the general coefficients. The exact
all-n identity (1) is retained as a constraint, not counted as a
full solution.

<a id="q3579-a5"></a>
## A5: alternant cancellation within each fixed underlying tableau

A second way to use the positive decorated monomial model is to extract a
Schur coefficient with the bialternant. Let delta=(n-1,...,0). Then
\[
c_{\lambda\mu}(n)
=[x^{\mu+\delta}]\Bigl(\sum_{\sigma\in S_n}
 \operatorname{sign}(\sigma)x^{\sigma\delta}\Bigr)\Phi_n(s_\lambda).
\]
This gives a signed set of pairs (permutation,decorated tableau).
Try to cancel opposite signs by a reflection/involution acting only on
the decorations and permutation, while retaining the underlying
semistandard forbidden-index tableau T. The unpaired positive objects
would provide a direct rule.

Such a fibrewise involution is impossible. Take n=3, lambda=(2),
mu=(1,1) and T=(2,2). Its decoration polynomial is (x1+x3)^2.
Here mu+delta=(3,2,0). Only the identity permutation and the
transposition (12) can give nonnegative decoration weights:
they require (1,1,0) and (2,0,0), respectively. This fixed T contributes
zero positive objects and one negative object. Its signed fibre total
is -1, so no sign-reversing involution confined to that fibre can leave
only positive fixed points.

For clarity, the six possible underlying rows 11,12,13,22,23,33 have
signed fibre totals 0,1,1,-1,0,1, summing to the correct actual coefficient
c_(2),(11)(3)=2. Positivity needs interaction between different T-fibres.
The ordinary monomial weights alone do not furnish that interaction.

This route shares the initial decorated tableau model with A1.
Its obligation differs: A1 tested a specified tensor-crystal action which
*changes* forbidden indices; A5 tests any sign-cancellation involution
which *preserves* the underlying tableau. The negative fibre rules out
the whole latter contract, rather than repeating A1's failed move.
Neither argument excludes nonlocal involutions that move between fibres.

**Full-target outcome: failure 5.** Stop the full Q3579 target unresolved
under the user's per-problem rule, subject to independent count review.
The exact small-n rules, positive decorated monomial model and all-n
Pieri constraint survive as scoped evidence. The checker and receipt
are [check_chern.py](check_chern.py) and [CHERN-CHECK.json](CHERN-CHECK.json);
their signed coefficient calculations are not promoted to the requested
cancellation-free general rule.




