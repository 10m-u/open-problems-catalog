# Independent review of Q549 and Q550 attempts

**Verdict:** the mathematical obstructions and the stated narrow outcomes pass internal review. Each packet records five distinct specified sufficient routes. Neither catalog question is resolved or disproved. These are five failed methods per question, not five independent lower-bound theorems. The overlap and limitations below must stay with any stopping-rule record.

Reviewed [Q549-ATTEMPTS.md](../certificates/Q549-ATTEMPTS.md), [Q550-ATTEMPTS.md](../certificates/Q550-ATTEMPTS.md), their exact synthesizer and receipt. I also read the retained Gläser dissertation at collections-f76a80f301f33456.txt.gz: Theorems 1.1–1.2, Question 5.26, Proposition 5.27, the precursor signatures in §5.5.2, Theorem 5.36 in §5.6, and the discussion around Conjecture 6.8. [Primary dissertation](https://tuprints.ulb.tu-darmstadt.de/server/api/core/bitstreams/3c676d11-8374-4609-b9d5-8f98004ba917/content).

## Q549: valid claims with a shared separation

For the parallelogram P_N, write x=Ny+t with 0≤y≤N and 1/3≤t≤2/3. This proves integer-freeness and the two-leaf split (1,−N). At the N+1 witnesses (Nj+1/2,j), an allowed normal (a,b) takes values ajN+a/2+bj. If a=0 these are integral; otherwise |aN+b|≥2 when |a|,|b|≤N−2. One open unit gap therefore removes at most one witness. Every witness must disappear at an internal split, proving at least N+1 internal nodes and N+2 leaves. This is an encoding-length separation, since the input uses O(log N) bits.

The same coordinates give width N|aN+b|+|a|/3. A primitive normal admitting a two-leaf refutation must have aN+b=0, hence be ±(1,−N). This validates the exponential delay of the **specified increasing-magnitude enumeration**. It is not a lower bound on geometry-aware enumeration orders. The facet-only triangle obstruction is also exact: (0,1/2) evaluates integrally under each primitive facet normal and survives every such split. The continuous label relaxation admits the invalid label (0,−1/2), including as the midpoint of two genuine opposite labels; this disproves a lossless continuous relaxation, not all rounding algorithms.

The attempt distinctions are:

| Attempt | Rejected sufficient hypothesis | Overlap/scope |
|---|---|---|
| A1 | Polynomial **magnitude** cutoff still permits a polynomial-size proof | Fails correctness/output-size completeness |
| A2 | Input facet normals suffice | A different triangle survives every allowed split |
| A3 | Complete increasing-magnitude enumeration is output-polynomial | Repairs A1's completeness but fails its runtime argument |
| A4 | Continuous feasibility supplies an integer split label | Rejects the specified relaxation only |
| A5 | General proofs can be converted to variable proofs with polynomial overhead | A negative-answer hardness-transfer route |

**Counting caution:** A1, A3 and A5 reuse one geometric separation. They are distinct attempts because the admissible algorithms or reduction hypothesis differ, but they do not produce three new separations. A5 correctly blocks even size-only polynomial simulation in the direction needed to transfer variable-system non-automatizability; it does not rule out reductions confined to particular hard instances. The source's coefficient recompilation theorem changes size by O(n) and bounds total binary encoding; it does not give a polynomial number of labels. Also, Conjecture 6.8 is a particular reflection-principle conjecture implying conditional non-automatizability, rather than the literal automatizability question itself.

## Q550: exact original-system distinctions

The bowtie has fractional matching value 5/2 but integer value 2. Fixing outer edge 12 to one leaves the other triangle and a two-leaf presolved refutation. In the original system, every root has a feasible child at the cutoff 5/2, while branching on 12 leaves an empty zero child and a two-leaf one subtree: exactly three leaves. C_5 has the same n, treewidth, integral/fractional values and deficiency parameter, but exactly two leaves.

For the friendship graph F_q, the q half-integral witnesses put a half triangle at one petal and an integral outer edge at each other petal. Every variable is fractional in at most one witness; the others all choose the same child. Following that child retains all but at most one witness per level, proving depth at least q. Branching successively on outer-pair edges attains depth q and q+1 leaves. The stated zero-child bound follows from z_i≤1 and total hub coverage Σz_j≤1: the value is at most q−1+z_i+(1−z_i)/2≤q.

The disjoint-triangle calculations are correct at both cutoffs. With δ=q, branching on a single original-orbit representative leaves fractional maximum 1+3(q−1)/2≥q+1/2 in both children. With δ=1, that same branch already makes both children empty at cutoff 3q/2, so T_var=2 although a blind product of all q component refutations has 2^q leaves.

The five route classes—unchanged presolve transfer, matching-value state compression, balanced-tree restriction, fixed original automorphism orbits, and blind component products—are distinct. **A1 and A2 reject stronger intermediate claims than Q550 requires:** a 2-versus-3 minimum-size discrepancy does not exclude polynomial-overhead lifting or an approximate proof-discovery DP. A3 rules out depth balancing in this variable calculus; A4 permits the usual repair using stabilizers of the current assignments; A5 permits threshold-aware early pruning. None is a hardness theorem for the requested f(tw(G))·poly(input,δ,T_var) discovery algorithm.

## Independent finite controls

[check_final_reviews.py](check_final_reviews.py) and its [receipt](FINAL-REVIEW-CHECK-RESULTS.json) reproduce the matching optima with an independent LP oracle enumerating vertex-disjoint odd cycles and integral edges. Fixed-zero/fixed-one constraints define faces, so filtering these fractional matching vertices is exact. It recovers C_5/bowtie leaf counts 2/3; friendship leaf/depth pairs (2,1),(3,2),(4,3); and disjoint-triangle leaf counts 2 at δ=1 and 2^q at δ=q for q≤3. It also checks 1,619 restricted normals and both unique primitive two-leaf labels on three parallelograms.

These are bounded checks of the written proofs, not a general discovery algorithm or an external peer review. I accept the five specified failed-route counts for each packet with the overlap and stronger-hypothesis qualifications above preserved.
