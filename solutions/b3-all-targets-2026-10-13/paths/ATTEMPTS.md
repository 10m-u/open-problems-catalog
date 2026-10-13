# Path-height attempts: Q4331 and Q4332

13 October 2026. The two targets remain conjectures. Each of the five routes
below tries to establish its complete target and ends with a specified
obstruction or missing argument. The new partial theorems do not reset the
failure counts. Controls involving weighted walks or arbitrary coefficient
arrays test proposed sufficient lemmas; they are not counterexamples to the
catalog questions. Independent review of the attempt counts is pending.

For Q4331, “both polynomials” means the A_n and B_n defined in the shared
setup. The Motzkin definitions appended to its catalog text belong to the
next question. For Q4332 the targets are M_l and R_l themselves. Source:
[Conjectures 3.14 and 6.8](https://arxiv.org/html/2609.38084v1).
Exact controls are in [check_heights.py](check_heights.py) and
[HEIGHT-CHECK.json](HEIGHT-CHECK.json). The nonreal-root obstruction was
already anticipated by the source; our Sturm calculations verify it for
the actual arrays rather than claiming it as a new phenomenon.

Write D_n(t)=sum_h H(n,h)t^h, with D_0=1. Define a bilinear operation
J(f,g)=sum_(i,j) f_i g_j t^max(i+1,j). First-return decomposition gives

    D_n = sum_(j=0)^(n-1) J(D_j,D_(n-1-j)).

For unshifted height polynomials F_l=M_l/t and G_l=R_l/t, it gives

    F_l=F_(l-1)+sum_(j=0)^(l-2) J(F_j,F_(l-2-j)),
    G_l=sum_(j=0)^(l-2) J(F_j,G_(l-2-j)).

There is no leading-horizontal term in G. The checker verifies these
identities against an independent height-state walk enumeration. They are
exact all-size recurrences; only their proposed shape-preservation arguments
fail below.

<a id="q4331-a1"></a>
## Q4331 attempt 1: real-rooted grouped height polynomials

Try to place A_n and B_n in the negative-real-rooted class and apply Newton
inequalities in their actual degree d=ceil(n/2). The exact A_17 array is
(0,65536,21457825,63739103,35640450,7907108,799799,34475,493,1).
After removing its zero root, its degree is eight and exact Sturm counting
gives six real roots. B_16 has reduced degree seven but five real roots;
its complete array is in the receipt. Both therefore have nonreal roots.
The proposed sufficient property is false for the actual target families.
Failure 1; this does not refute ultra-log-concavity.

<a id="q4331-a2"></a>
## Q4331 attempt 2: retain the finer height distribution

Try to prove ultra-log-concavity before grouping heights and then transfer
it through the two adjacent-height groupings. At semilength seven the
finer Dyck array is (0,1,63,169,132,52,11,1). Its degree-seven normalized
inequality at index six requires 6*11^2 >= 14*52, but 726<728. Thus the
strong fine-height invariant is unavailable even though the grouped arrays
pass. A grouping theorem would have to use information weaker or different
from this invariant. Failure 2, with an actual stronger-property obstruction.

<a id="q4331-a3"></a>
## Q4331 attempt 3: close the normalized first-return induction

Use the displayed exact D recurrence, apply the linear grouping operators
to each summand, and try to close an induction by retaining only their
degree-normalized log-concavity. Even granting that every grouped summand
has this property, addition of such summands does not preserve it. In a
common ambient degree three, f=(1,2,1,0) and g=(0,0,1,3) are both
ultra-log-concave, but f+g=(1,2,2,3) violates the inequality at index one:
2*2^2 < 6*1*2. This is a generic control, not a claim about actual summands.
The first-return argument needs cross-summand synchronization or a stronger
joint invariant. Deriving that invariant from the height states did not
close the induction. Failure 3.

<a id="q4331-a4"></a>
## Q4331 attempt 4: spectral interlacing of ceiling matrices

The bounded-height Dyck count is the (0,0) entry of a power of a path
adjacency matrix. Successive ceilings give interlacing real spectra; adjacent
height differences and grouping then give A/B coefficients. Try to infer
normalized log-concavity from this Jacobi structure alone. Positive edge
weights preserve symmetry after diagonal similarity and preserve spectral
interlacing. Give every up edge weight one except the edge from height six,
which has weight 10000. At semilength seven the grouped A array becomes
(0,64,301,63,10000), which is not ultra-log-concave. The proposed purely
spectral implication therefore fails in its natural positive-Jacobi class.
The unweighted entries contain additional structure that the argument has
not used. Failure 4; the weighted example is not a catalog counterexample.

<a id="q4331-a5"></a>
## Q4331 attempt 5: coefficient formulas and normalized ratios

Use reflection formulas to prove decreasing normalized coefficient ratios
directly, rather than impose a root or matrix-spectrum condition. In the
single-image upper range, the explicit factorial formulas factor into three
positive log-concave sequences. This proves the all-size upper-tail
ultra-log-concavity theorem in [UPPER-TAIL.md](UPPER-TAIL.md): at every
internal index ceil((n+2)/4)<i<ceil(n/2) for A, and
floor((n+2)/4)+1<i<ceil(n/2) for B. Index one is automatic.
The lower-height formulas include further alternating reflected images;
the positive factorization does not extend across those thresholds, and no
sign-definite all-size ratio argument was obtained there. Exact full-array
controls through n=100 are evidence, not a proof for that missing region.
Failure 5 on the complete target, retaining the new partial theorem.

<a id="q4332-a1"></a>
## Q4332 attempt 1: negative real zeros

Try to prove real-rootedness and then use Newton inequalities (which would
give more than ordinary log-concavity). The actual M_11 array is
(0,1,1023,3036,1485,242,11). Its reduced degree is five but it has three
real roots. The actual R_12 array is (0,0,89,1693,1836,540,54,1), again
with reduced degree five and three real roots. Exact Sturm counting proves
the stronger root property false. Failure 1; ordinary log-concavity survives.

<a id="q4332-a2"></a>
## Q4332 attempt 2: strengthen to degree-normalized log-concavity

Try to obtain a binomial-normalized invariant that is preserved by the walk
construction and would imply the target. An exact walk DP finds a failure
of this stronger property for M at length 88 and for R at length 94; the
complete integer arrays are preserved in the receipt. Both still satisfy
ordinary log-concavity in the bounded checks. Thus an induction demanding
ultra-log-concavity of every complete array cannot work. Failure 2.

<a id="q4332-a3"></a>
## Q4332 attempt 3: first-return closure under ordinary log-concavity

Use the exact F/G recurrences above and try to retain log-concavity as the
sole shape invariant. The operation J itself is not asserted to violate
log-concavity; exploratory controls did not establish such an obstruction.
The sum step is already insufficient: f=(1,1,1,0) and g=(0,0,1,2) are
log-concave without internal zeros, whereas f+g=(1,1,2,2) fails at index
one, since 1<2. These arbitrary arrays are a control on generic closure.
To prove the actual recurrence one needs mixed inequalities between its
different length splits, and the proposed single-sequence induction does
not supply them. Failure 3, not a failure of the exact recurrence.

<a id="q4332-a4"></a>
## Q4332 attempt 4: positive Jacobi ceiling differences

Try to extract log-concavity of the exact-height differences from the real
interlacing spectra of the Motzkin ceiling matrices. The diagonal entries
are one, except the forbidden height-zero horizontal entry for Riordan.
Assign positive up-edge weights (1,1,100), with down-edge weights one.
At length six the resulting M array is (0,1,31,18,100), and R is
(0,0,5,9,100). Both violate ordinary log-concavity. Positive diagonal
similarity makes all these ceiling matrices real symmetric, so spectral
interlacing alone persists while the desired difference inequality fails.
Failure 4 in the enlarged weighted class; no unweighted counterexample.

<a id="q4332-a5"></a>
## Q4332 attempt 5: delete and reinsert horizontal steps

Express each maximum-height coefficient by deleting horizontal steps,
counting Dyck cores, then reinserting horizontals in all allowed slots.
The Riordan count additionally records the number of irreducible Dyck
components because height-zero slots are forbidden. This produces exact
formulas for the last three height counts at every length; the four parity
and family cases have positive polynomial log-concavity defects after
writing m=u+5. The finitely many smaller lengths complete an all-size proof
of the final nontrivial inequality, as detailed in UPPER-TAIL.md.
For an arbitrary interior height, more core semilengths and component
counts contribute. Neither the insertion sums nor the remaining reflected
terms have been arranged into a sign-definite general defect. Failure 5
on the complete target, retaining the new endpoint theorem.

## Stopping disposition

Each target has five consecutive full-target failures in this packet. Stop
mathematical work on it under the user's rule, subject to reopening any
count rejected during independent audit. Preserve both conjectures as open
and file the two all-size partial theorems at their actual scopes.
