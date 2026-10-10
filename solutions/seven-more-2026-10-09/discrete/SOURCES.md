# Source and literature checks for the discrete pair

Checked 2026-10-09. These are bounded searches, not certificates of literature completeness. Source texts are linked rather than copied into the repository. The mathematical derivations and executable certificates in this folder are original work for this research round; no priority or peer-review claim is made.

## Q3499: polygon-face Ehrhart coefficients

Primary source: Teemu Lundström and Leonardo Saud Maia Leite, *Order polytopes of crown posets*, arXiv:2504.05123v5, 1 October 2026.

- [Versioned full text](https://arxiv.org/html/2504.05123v5).
- [Versioned PDF](https://arxiv.org/pdf/2504.05123v5).
- [Published article record](https://www.sciencedirect.com/science/article/pii/S0195669825001969).

Read the definitions in Section 2, the crown order-polynomial section, and Section 6 around Question 6.5. Verified that the face lattice includes both extreme faces and that the relevant question is about the polynomial \(E(m)=\Omega(m+1)\). The primary source explicitly retains Question 6.5. Its negative order-polynomial coefficient for the 7-gon is distinct from the present result and is used as an independent shift control.

Searches performed:

- `"polygon" "Ehrhart" "nonnegative" "crown"`.
- `"Order polytopes of crown posets" "Question 6.5"`, with a one-year recency filter.
- `"13-gon" "Ehrhart"`.
- `"298495711" "Ehrhart"`.

Outcome: the versioned primary source remained the substantive result for this exact question. No earlier 13-gon coefficient counterexample or later resolution was located. The source's proof of positivity for crown order polynomials does not apply to the face lattice after adding its bottom and top elements.

## Q3480: twice-hare-sortable Cayley words

Primary source: Giulio Cerbai, *Sorting Cayley permutations with pattern-avoiding machines*, Australasian Journal of Combinatorics 80(3) (2021), 322–341.

- [Journal PDF](https://ajc.maths.uq.edu.au/pdf/80/ajc_v80_p322.pdf).
- [Author thesis/preprint containing Open Problem 8.1](https://arxiv.org/pdf/2210.03621).
- [Earlier paper version](https://arxiv.org/html/2003.02536v2), consulted only to locate related work; the journal's notation and theorem numbering govern the report.

Read the journal's stack definition, Theorem 3.8 on printed pages 329–330, and Open Problem 1 on page 330. Checked that equal letters are allowed together in the hare stack. Read the proof's inequality requiring an intermediate value at least as large as the 4-role in a rescued 3241 occurrence. This is essential for repeated-letter words such as 34241.

Searches performed:

- `"two" "hare" "sortable" "Cayley" enumeration`, with a two-year recency filter.
- `"21-sortable" Cayley enumeration`.

A recent related primary paper was located: [*The Insertion Encoding of Cayley Permutations*, Electronic Journal of Combinatorics 33(3), 2026](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v33i3p26/pdf/). Its abstract explicitly addresses Cerbai's hare **pop-stack** question. The pop-stack empties the entire stack on a pop, whereas Q3480 pops individual entries as necessary and uses two passes. That paper therefore does not supply a resolution of Q3480.

Outcome: no unrestricted two-pass enumeration was located. The present report retains partial status and confines its explicit rational closed formula to the four-symbol slice, while giving a general finite-state algorithm separately.
