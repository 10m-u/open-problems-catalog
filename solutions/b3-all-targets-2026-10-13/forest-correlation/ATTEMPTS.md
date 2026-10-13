# Q4396 substantive attempts

## Q4396-F01: actual forest-pair coefficients on general small graphs

Attempt: construct a negative monomial coefficient by exact ordered-forest
enumeration on arbitrary simple graphs. The complete-graph controls prove
the entire simple-graph class through six vertices by deletion of variables,
including 9,266,444 contributing ordered pairs in K_6. They give no negative
coefficient and no all-size exhaustion argument. First full-target failure,
with bounded exact evidence preserved.

## Q4396-F02: FKG on the forest configuration support

Attempt: apply FKG directly to the increasing connectivity events. The
forest measure is not log-supermodular on subsets: in a triangle take
F_1={01,12}, F_2={02}. Both have positive weight, their intersection is
empty, and their union is a cycle with weight zero. Thus the FKG lattice
condition fails. This does not refute positive correlation of these
particular connectivity events. Second full-target failure.

## Q4396-F03: matrix-tree determinantal representation

Attempt: transfer a determinant proof for rooted spanning forests to the
unrooted forest partition function here. The determinant det(I+z L_K3)
is 1+6z+9z^2, while the actual unrooted partition sum is 1+3z+3z^2.
The determinant weights each component by its number of possible roots.
Connectivity restrictions inherit those unwanted component-size weights;
there is no fixed scalar correction. The proposed representation does not
prove this target. Third full-target failure.

## Q4396-F04: transfer a whole connecting path between the two forests

Attempt: inject an ordered pair with a-b connected in its first forest and
c-d in its second into one with both connections in one forest, by moving
the full first a-b path. Take a=0,b=1,c=2,d=3,
F_1={04,41}, F_2={45,51,23}. Both configurations are forests, and only
their specified pair is connected. Moving the first path to F_2 creates
the triangle 4-5-1-4. Thus the naive switching map leaves the forest class.
There may be a different, more local cycle-breaking switch; none proving
the general coefficientwise injection is constructed. Fourth full-target
failure, with an actual in-class obstruction to the stated switching rule.

## Q4396-F05: factor over graph blocks and reduce cycles by complete arcs

Attempt: establish arbitrary-graph positivity by block factorization and
arc contraction. RESULTS.md proves the full all-size cactus subclass,
using triangle/four-cycle base identities and nonnegative substitutions.
For a general graph its two-connected blocks need not be cycles: K_4
already has overlapping cycle constraints. Their admissible configurations
do not factor into the independent incomplete arcs used in this proof,
and a universal nonnegative base identity for arbitrary blocks remains
unproved. The finite K_6 result does not cover blocks of unbounded size.
This substantial subclass result is the fifth failed full-target attempt;
stop Q4396 unresolved with the cactus theorem and exact controls retained.

The FKG support, rooted determinant, whole-path injection and block
factorization are distinct proof contracts. Their failed steps are not
claimed as counterexamples to the catalog conjecture. Source/service
interruptions count zero.
