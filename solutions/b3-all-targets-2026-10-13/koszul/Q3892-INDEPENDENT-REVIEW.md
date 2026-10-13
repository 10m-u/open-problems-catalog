# Independent review of Q3892

Reviewed 2026-10-13 on the retained agent. The five failed full-target
routes are accepted as distinct, and the all-degree descending Koszul
family is accepted at its stated scope. The full Roller Coaster
conjecture remains unresolved; this is a stopping-rule disposition,
not a disproof or a novelty claim.

The frozen target requires every strict ordering of the entire first
half, for every sufficiently large socle degree, in characteristic zero.
The primary Holleben--Nicklasson text, Conjecture 5.8, agrees. In the
original [D'Alì--Venturello Section 8](https://arxiv.org/html/2106.05051),
Corollary 8.2 and Proposition 8.3 assume a pure **flag** complex. The
submitted argument explicitly supplies this hypothesis. The shorter
printed restatement in Holleben--Nicklasson is not used to remove it.

The lexicographic shelling of a join of discrete parts is valid: an
earlier facet first differs at a coordinate whose value decreased, and
its intersection is contained in the face obtained by deleting that
coordinate. Conversely each indicated codimension-one face appears
earlier. The apolar ranks give
`h_i=binom(q,i)s^i+binom(q,i-1)s^(q+1-i)` internally. The two endpoint
dimensions are one, rather than the doubled empty-face value. The
inequality for `s>=2q+1` proves every claimed descending ordering. The
one-parameter root bound restricts this family only; it does not exclude
unequal parts or other complexes.

For the CM obstruction, I rederived the coefficient at `j=k+1` from the
ordinary simplicial h transform. The low-index alternating sum, the
empty-face bound `1/T<=2`, and the absolute-error sum are correct. The
loose upper bound is negative at q=10 and stays negative as q increases.
It excludes the specified approximation templates, not all CM flag
face sequences. The smoothing proof handles the first two differences
separately and the remaining positive differences with `C/B<=1/2`;
there is no unhandled middle or odd-degree case.

The reciprocal identity clears exactly to `(1-z^6)^3`. The quadratic
realization obstruction also applies to alternative presentations with
the same Hilbert function: an m-primary quadratic ideal in N variables
over the characteristic-zero field contains N regular quadrics. Choose
each quadric outside the finitely many associated primes of the previous
complete intersection; its quadratic span cannot be contained in such
a prime because the whole ideal is m-primary. The complete-intersection
quotient is zero above N, as is every further quotient. The proposed
rows have socle degree N+2. Finally, the connected-sum socle relation
is independent of all the quadrics and is a minimal relation in degree
d>=3. The stated apolar realization by two disjoint simplices agrees.

The attempt dispositions are:

- A1: failure of the specific approximate-face transfer through a
  uniformly negative CM h coefficient.
- A2: a developed equal-part join construction, with an insufficient
  number of possible orderings despite an all-degree positive partial.
- A3: failure of a fixed-seed degree-raising tensor operation, proved
  for every positive padding degree.
- A4: failure of the proposed numerical realization criterion even
  with an all-orders nonnegative reciprocal.
- A5: failure of additive connected-sum closure on actual Koszul inputs.

A2 and A3 share one input family, but their full-target obligations are
different (capacity within a degree versus transport between degrees).
A1 and A5 both use topology, but one obstructs prescribed approximate
face templates and the other an explicit operation on already valid
inputs. Neither overlap merits merging these routes.

[Independent checker](check_koszul_review.py) imports none of the submitted
checker. It builds literal squarefree apolar derivative matrices for nine
join examples and six connected sums, maximizes the CM coefficient over
all distinct high-index label pairs for q=10..40, and verifies the
reciprocal polynomial identity, 50 padding rows and 89 ordering bounds.
The [receipt](KOSZUL-REVIEW-CHECK.json) records the exact controls. These
finite checks support, and do not replace, the all-size proofs above.
