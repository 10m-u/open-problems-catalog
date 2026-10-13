# Q3206: the arbitrary-coefficient anti-recurrence

Full question: for positive coefficients \(a_1,\ldots,a_k\), \(k>1\),
let B be the increasing complement of A and
\(A_n=\sum_{j=1}^k a_j B_{k(n-1)+j}\).
Put \(\tau=\sum a_j\), \(\kappa=k\tau+1\).
Must \(D_n=A_n-\kappa n\) always be \(\tau\)-automatic?

The source's bounded-initial-value theorem already solves the case
\(A_1=\sum j a_j\le(k-1)\tau+2\). That restricted theorem remains intact.
The following five attempts address extension beyond that hypothesis.
The source is texts/papers/collections-643f5569923aac95.txt.gz;
[published paper](https://math.colgate.edu/~integers/aa24/aa24.pdf).
The executable experiment generates 20,000 terms for each of eight tuples.

1. **Retain one A per aligned interval.** Partition the positive integers
   into \(I_n=[\kappa(n-1)+1,\kappa n]\) and reuse the source's aligned
   block argument without the initial-value bound. For \(a=(1,4)\),
   \(\tau=5,\kappa=11,A_1=9>7\), the first term outside its own \(I_n\)
   occurs at n=348. Thus the one-per-own-interval induction needed for
   this extension has a concrete false conclusion. The complementary
   construction in check.py verifies each term is increasing and beyond
   the B values already consumed; its mex implementation is exact.
2. **Residue-only substitution.** Try to replace the original alignment
   proof by a substitution determined by \(A_j\bmod\kappa\).
   Parents 344 and 349 both have residue zero but yield child defect
   blocks \((-2,-3,-4,-5,-6)\) and \((-3,-3,-4,-5,-6)\).
   Their parent defects are both zero, so adding only that defect does
   not repair the transition. This disproves the proposed state rule;
   it does not disprove an automaton with more information.
3. **Finite-kernel inference.** Generate base-\(\tau\) decimations and
   close a putative finite kernel from observed prefixes. For (1,4),
   64-term prefixes at exponents 0–3 distinguish 1,5,13,22 sequences.
   There is no established closure after a finite sample. A transition
   inferred from it may first fail later, as the aligned progression
   \(A_{5j+1}=A_1+55j\) itself first fails at j=348. Kernel counts bound
   LSD-first DFAO states; they cannot be compared directly with the
   source's MSD-first state bound. This attempt produced no all-index
   equality certificate or finite closed kernel.
4. **Bounded defects imply automaticity.** Use the observed defect range
   to argue that a finite alphabet suffices. For (1,4) the sample has
   defects from −6 through 1. Even a proof of this bound for all n would
   not settle the question: sequences over a two-element alphabet can
   be nonautomatic. For example the characteristic sequence of
   \(\{2^{2^j}:j\ge0\}\) is not 2-automatic, since its accepted binary
   words would be a one followed by a non-ultimately-periodic set of
   zero-run lengths. A finite alphabet is different from finite
   base-\(\tau\) kernel. No recurrence closing that kernel was derived.
5. **Enlarge the state by neighboring context.** Test
   \((A_j\bmod\kappa,D_{j-r},\ldots,D_{j+r})\) as a parent state
   producing its \(\tau\) children. Radius zero has the explicit
   conflict above. Radii 1–4 have no conflict within the 20,000-term
   experiment, with 26,40,58,76 observed states for (1,4).
   This is encouraging finite evidence but not a recursive construction:
   producing the *child's whole radius-r neighborhood* can require
   adjacent parents and an unproved carry/alignment bound. Neither
   a uniform bound on required context nor closure of these proposed
   transitions for all n and all coefficient tuples was proved.

The full question reaches five substantive failed routes and remains open.
The two explicit counterexamples refute particular extensions, not
automaticity itself. Finite tests, additional coefficient tuples, and
different context radii are evidence within the routes, not extra attempts.
