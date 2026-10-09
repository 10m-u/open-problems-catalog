# Independent internal review of Q1715

Date: 2026-10-09. Reviewer: the discrete-problems agent, separate from the algebra-problems author.

**Verdict: no blocking mathematical issue found.** The proposed 13-dimensional example disproves the full characterization in Q1715. The universal generating-pair argument is a proof, not an extrapolation from sampled pairs.

## Source and scope

Independently opened [Burde–Dekimpe–Moens, arXiv:1711.01964v1](https://arxiv.org/html/1711.01964v1), read Definition 5.1 and the final open problem in Section 5, and compared them with the catalog entry. The source requires every generating pair, a triple in the derived subalgebra, and characteristic zero. The proposed algebra and conclusion satisfy precisely these hypotheses. The source also warns that checking one generating pair is not generally enough; the report addresses that issue explicitly.

## Checks on the argument

- Re-derived the possible nonautomatic Jacobi identities from the grading. Aside from repeated entries, only \((x,y,z)\), \((x,y,u)\), and \((x,y,v)\) can have total degree at most five. The displayed bracket table makes each sum zero, including the essential \([x,c]=r+w\), \([z,v]=w\) cancellation.
- Checked generation, the two-dimensional abelianization, and class five. In particular, \(w=[z,v]\) is generated and the nonzero \(p\) is an iterated bracket of length five.
- Re-derived the equations for the three maps \(T_d\). Their injectivity follows directly from coefficient comparison. For degree four, the independent \(w\)-coordinate removes the kernel that would otherwise contain \((c,-b,a)\).
- Checked the generator-change lemma. Writing the two equations as the row-bracket product \((x,y)PS=0\) is correct. Multiplication on the right by \(P^{\mathsf T}\) produces a symmetric vector-valued matrix \(PSP^{\mathsf T}\); injectivity for the original pair forces it to vanish. Invertibility of \(P\) then forces \(S=0\). No lift of \(P\) to an automorphism of the quotient algebra is needed.
- Checked the passage to arbitrary generating pairs with higher-degree terms. Their images form a basis of the abelianization. A smallest noncentral input degree \(d\) contributes to output degree \(d+1\) only through those degree-one generator parts; every higher-degree perturbation lands later. The injectivity argument therefore excludes all components in degrees two through four.
- Confirmed that the center is exactly the degree-five subspace. The freeness obstruction is then immediate from class five and dimensions: the two-generated free nilpotent algebra of class five has dimension 14, whereas this one has dimension 13.

## Computational evidence reviewed

Read the complete `check_q1715.py` implementation and ran it from the algebra folder using standard-library Python. It returned `PASS`, with 2,197 ordered Jacobi triples, lower-central dimensions \((13,11,10,8,5,0)\), center dimension five, and graded ranks \(3,6,9\). The maximal minors are \(1,-1,1\), so these rank conclusions require no floating-point decision. The higher-degree generator perturbation control has rank 18. The further quotient killing \(w\) exposes the claimed noncentral solution.

This rerun validates the finite checks; the review of the congruence and grading arguments is what validates the unbounded quantifier over generating pairs and characteristic-zero fields. No smallest-dimension or complete classification claim has been inferred.

## Limits of this review

This is internal AI-assisted review, not external peer review or a formal proof-assistant verification. The source was checked directly, and the proof's main steps were re-derived, but literature priority was not independently established. No correction is required for the stated counterexample result.
