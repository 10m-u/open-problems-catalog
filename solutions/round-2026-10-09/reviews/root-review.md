# Independent internal reviews: Q1653, Q3236, Q3454 and Q3489

Date: 2026-10-09. These are mathematical reviews by a second AI research agent within the same research round. They are not external peer review, formal verification, or a certification of historical novelty. The reviewer read the complete reports and checked the relevant primary-source definitions and targets.

## Q1653 — accepted as a counterexample to the exact statement

The source's Definition 6.1 requires factor closure without an extension condition. Definition 6.5(3) requires equality of complexity at every length. Conjecture 6.36 is therefore contradicted by the language in the report.

The language $0^*1^*\cup\{10\}$ is factor closed. Its complexity is $2,4,4,5,6,\ldots$. Every recurrent factor of a one-sided infinite word has a recurrent right extension, by the finite-alphabet pigeonhole principle. Equality of the numbers of recurrent factors at two consecutive lengths makes the right extension unique. A sliding length-$n$ window then determines every longer recurrent factor from its prefix. Prefix deletion is also surjective, so a plateau persists at every later length. The values at lengths 2, 3 and 4 give the contradiction.

This argument compares cardinalities, not equality of the actual languages, and so addresses the weaker realization requirement in the question. The finite forbidden-factor description was also checked. The proof does not decide eventual complexity equivalence or any separate growth-rate conjecture.

Source: [Jarvis, *Pin Classes*](https://oro.open.ac.uk/108335/1/Pin%20Classes.pdf), Definitions 6.1 and 6.5, Conjecture 6.36.

## Q3236 — accepted as a full affirmative proof proposal

The target is the exact infimum quasinorm, with the parent spaces and resonant measure space specified in the source. The proof addresses both the exact Fatou property and exact rearrangement invariance.

The following potentially delicate steps were checked individually:

- Nonnegative splits suffice, and bounded split costs force the monotone limit to be finite almost everywhere.
- An inequality between superlevel distributions yields the needed lower semicontinuity through decreasing rearrangements and the parent Fatou property. It does not assert norm continuity under weak convergence.
- Tight laws on finite-measure blocks admit a common diagonal subsequence. Their limit is supported on $t=x+y$, as follows by testing the bounded continuous function $\min(1,|t-x-y|)$.
- Realizing the limiting joint laws separately on geometric value bins requires only nonatomicity. It does not require an independent uniform variable conditional on the original function, or an isomorphism with a standard probability space.
- The order of the inequalities in the countable-block Portmanteau/Fatou calculation is correct. The constructed marginal distributions therefore give the required bounds on both parent quasinorms.
- The geometric-bin inequality $f\le r(g+h)$ gives cost at most $rL$ for each $r>1$. Taking the infimum over $r$ proves the exact Fatou constant without claiming an attained decomposition.
- The atomic argument uses coordinatewise subsequences and Fatou. Exact rearrangement invariance follows by transferring finite simple functions and then using the newly proved Fatou property. Infinite total measure is covered by finite-support simple approximations.

The auxiliary nonattainment example was checked separately: its integral lower bound, approximate decompositions, and the contradiction obtained by differentiating the required tail measures are consistent. It is not needed to prove the main theorem.

Source: [Peša, arXiv:2508.10825v2](https://arxiv.org/html/2508.10825v2), Definition 1.1 and Section 1.2.

## Q3454 — accepted only in the stated commuting-support scope

The report's quantitative theorem is valid when the two initial support idempotents commute and the two final support idempotents commute. For a hermitian idempotent $e$, the identity $e^{i\pi e}=1-2e$ makes both $e$ and $1-e$ contractions. Each off-support product has norm less than one under the report's strict distance condition. Commutativity makes it an idempotent, so it must vanish. Repeating the argument in the opposite order proves equality of both support pairs.

With equal supports, the identity

$$
b^\dagger-a^\dagger=b^\dagger(a-b)a^\dagger
$$

gives the claimed Lipschitz bound. The proof does not need a product of commuting hermitian idempotents to be hermitian. The scalar boundary example confirms that the strict threshold cannot be replaced by a non-strict one in this argument.

The noncommuting case of Conjecture 2.22 is unresolved by this report. No strict separation example between the source's hypotheses and this theorem is claimed.

Source: [Gardella–Palmstrøm–Thiel, arXiv:2506.09563v1](https://arxiv.org/html/2506.09563v1), Conjecture 2.22, Theorem 2.23 and Remark 2.24.

## Q3489 — accepted as a counting-complexity classification

The primary source's evaluation at node-reliability argument 2 is equivalent to $C_G(-2)$ by the stated sign factor. The leaf attachment identity counts connected vertex sets directly and is valid for disconnected input graphs. Its specialization maps evaluation at 2 to evaluation at $-2$.

The one-call reduction was checked beyond that identity: clique replacement gives substitution $(1+x)^k-1$; choosing $k=n+1$ gives an integer base larger than every connected-set coefficient; all coefficients can be decoded without carry. The constructed graph and all arithmetic have polynomial bit length. The signed evaluation lies in GapP, and the conditional equivalence with $\mathrm{FP}=\#\mathrm P$ is stated correctly.

The extension to every nonzero fixed algebraic evaluation point was also checked. The rooted-attachment formula has the correct correction term. A rooted 5-cycle maps $-1$ to 1. One leaf handles roots of unity except the zero image and the two fourth roots, and two leaves handle the latter. The fixed-number-field interpolation argument covers the remaining generic points with polynomial bit complexity.

The only imported hardness premise is the established #P-completeness of counting connected induced vertex subsets. Its primary publisher abstract and the thesis's related theorem were checked; the original 1991 proof was not re-derived. No unconditional separation of complexity classes follows. The catalog conservatively retains an open/partial status for the literal polynomial-time-existence question while recording the complete hardness theorem.

Sources: [Mol, *On Connectedness and Graph Polynomials*](https://central.bac-lac.gc.ca/.item?app=Library&id=TC-NSHD-71408&oclc_number=1033184059&op=pdf), Chapter 4 and Section 6.4; [Sutner–Satyanarayana–Suffel, DOI 10.1137/0220009](https://doi.org/10.1137/0220009).
