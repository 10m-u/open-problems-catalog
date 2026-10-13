# Q3846 independent proof and attempt-count review

13 October 2026. I read the full
[root packet](../matrices/Q3846-ATTEMPTS.md), its checker and receipt,
the exact frozen statement, and
[Chen et al., Conjecture 1.3 and Theorem 1.5](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2021/30Chen.pdf),
also local texts/papers/collections-e7f30a3485a8a919.txt.gz.
The target is all finite minors coefficientwise in four independent
indeterminates. The d=0 theorem and numerical Eulerian results do not
close that scope.

I accept the five worked failed routes as distinct: one constant
production matrix for this output encoding; a specific common planar
birth/stay network; TN-only prefix extension by the actual row operator;
numerical-to-coefficientwise transfer; and direct actual initial-minor
elimination. None is an actual catalog counterexample.

A1's negative entry is forced by triangular inversion. The first rows
give \(T(2,1)=ae+cd+2ce\), and solving the next row identities yields
\(P(2,1)=-ae(ae+cd)/c^3\), negative at a=c=d=e=1.
Positive diagonal factors on **P** cannot change that sign.
This does not exclude arbitrary time-dependent rescalings of the output
rows T, which would define a different production problem; the packet
already leaves other encodings/factorizations open. I recommend making
that interpretation explicit if the diagonal-scaling sentence is retained.

A2's two coordinate counts are right: a birth edge sees the number of
previous stays, so its weight depends on the source index in the proposed
translated network. The common edge at (-1,0) indeed requires different
weights from S2 and S3. This refutes that encoding, not all possible networks.

The artificial TN prefix in A3 and its extension give exactly the
negative minor -2. The preceding third row is disclosed as artificial.
A4's positive-entry 2-by-2 matrix is numerically TN for every a>=0,
while its determinant has coefficient -2 at a; the transfer lemma is
false at precisely that generic contract.

The all-size two-column theorem in A5 passes. Solving the scalar
column-one recurrence gives
\[
T(n,1)=\sum_{j=0}^{n-1}(aj+c)e^j(d+e)^{n-1-j}.
\]
Splitting at m isolates the old row multiplied by (d+e)^(n-m).
Subtracting e^(n-m) times that row yields exactly the displayed determinant
identity. The binomial difference has its pure-e term removed, and every
remaining factor is coefficientwise nonnegative. The m=0 case uses
T(0,1)=0 and introduces no division or exception. All 1-by-1 minors are
positive recurrence sums; no higher minor can use only those two columns.

[MATRIX-REVIEW-CHECK.json](MATRIX-REVIEW-CHECK.json) records 21 independently
expanded boundary minors through row six and a fresh symbolic computation
of the forced production entry. I also inspected the root's complete
bounded-control code and receipt. These checks support the exact algebra;
the all-size conclusion rests on the split-sum identity. Accept the full
question as unresolved at five failed proof routes and retain the stated
all-size boundary theorem. No external review or novelty claim is made.

