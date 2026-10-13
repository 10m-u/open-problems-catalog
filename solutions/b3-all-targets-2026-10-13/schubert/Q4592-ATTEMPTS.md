# Q4592: cancellation-free signed-positive LG K-theory rule

Exact target: for every n and strict lambda,mu,nu in the n staircase, find a cancellation-free combinatorial rule for (-1)^(|nu|-|lambda|-|mu|) c^nu_(lambda,mu), where O_lambda O_mu=sum c^nu_(lambda,mu) O_nu in K^0(LG(n,2n)). Frozen statement b4906830656cda98aebc, thesis printed p.43, [joint source §1](https://arxiv.org/html/2503.14609v2); local thesis texts/collections-bd8ace3842285c95.txt.gz read. The known ordinary shifted rule and the known OG K-theory rule do not supply this full LG rule.

Primary tools read: [Buch–Ravikumar §5, especially Corollary 5.6](https://sites.math.rutgers.edu/~asbuch/papers/kpieri.pdf), which proves a cancellation-free special-input Pieri rule; [Pechenik–Yong §§7–8](https://ayong.web.illinois.edu/genomictableaux.pdf), which proves the OG genomic rule and only an LG upper-bound conjecture outside its proved Pieri/leading-degree cases. Signed computational reconstruction is explicitly distinguished from the target.

## Exact LG(2,4) geometry and K algebra

LG(2,4) is the smooth three-dimensional quadric. In the Schubert basis 1,a=O_(1),b=O_(2),c=O_(2,1), a is a hyperplane-section structure sheaf, b a line structure sheaf and c a point structure sheaf. Two general hyperplanes intersect in a plane conic, which degenerates flatly into two intersecting lines. The union exact sequence gives its class 2b-c. A general hyperplane intersects a line at a point; two general lines are disjoint; a general hyperplane avoids a fixed point. Consequently

    a²=2b-c, ab=c, ac=b²=bc=c²=0, a³=2c.

The geometric descriptions yield chi(1)=chi(a)=chi(b)=chi(c)=1: these are rational varieties with no higher structure-sheaf cohomology. The full Euler-pairing Gram matrix and its dual basis are

    G = [[1,1,1,1],[1,1,1,0],[1,1,0,0],[1,0,0,0]],
    dual(1)=c, dual(a)=b-c, dual(b)=a-b, dual(c)=1-a.

Literal KLG Pieri enumeration independently reproduces all products with special input (1) or (2). Associativity then supplies those with c=ab. This low-rank algebra is a control and useful exact special case, with no general closure or novelty claim.

<a id="q4592-a1"></a>
## A1: reweight the unchanged ordinary shifted LR objects

Attempt: keep the ordinary skew-tableau content and ordinary rectification objects, adding positive K-theoretic weights to the existing objects to count each signed coefficient. This would directly reuse the new ordinary shifted LR machinery.

For lambda=mu=(1), nu=(2,1), the shape nu/lambda has two boxes and ordinary content mu has one entry, so its ordinary LR set is empty. Yet the actual K coefficient is -1 by a²=2b-c, and its signed-positive value is 1. The adjacent output nu=(2) has the ordinary coefficient 2. The missing excess-codimension contribution is exactly the -c term obtained from the conic's two-line degeneration.

No nonnegative reweighting of an empty ordinary set supplies that contribution. A valid extension must allow different objects such as repeated/set-valued or genomic entries; it cannot merely attach weights to unchanged objects. First full-target failure at this precise contract.

<a id="q4592-a2"></a>
## A2: transfer the proved OG K rule using the cohomological power of two

Attempt: use the cancellation-free OG K rule and rescale each coefficient by the same power 2^(ell(lambda)+ell(mu)-ell(nu)) that transfers OG ordinary cohomology to LG. This would import an already proved full rule.

At n=2, OG(2,5) is P³ and its codimension-one structure sheaf A satisfies A²=B with no codimension-three term. The proposed transfer correctly predicts the leading LG coefficient 2 for output (2), but for output (2,1) the power is 2^(1+1-2)=1 and it predicts zero. The actual LG coefficient is -1. More generally the cohomological transfer controls only |nu|=|lambda|+|mu| and does not identify the full K algebras. The proved source explicitly distinguishes these scopes.

The missing step is a K deformation compatible with the OG-to-LG comparison, including excess codimension. This differs from A1: it starts with a full repeated-entry K rule, but attempts to transport the wrong algebra. Second full-target failure, not a refutation of either the OG rule or the ordinary relation.

<a id="q4592-a3"></a>
## A3: use positive triple intersections with the ordinary complementary class

Attempt: compute the structure coefficient by a positive Euler-characteristic count of a triple intersection with the ordinary complementary Schubert structure sheaf. This replaces the K-dual class by the cohomological complementary class and would avoid alternating basis conversion.

For output nu=(2,1), its ordinary complement is empty, hence the proposed coefficient is chi(a²)=2-1=1. The actual coefficient is -1. The exact Gram matrix shows why: the K-dual of c is 1-a, so

    c^21_(1,1)=chi(a²(1-a))=chi(a²)-chi(a³)=1-2=-1.

Thus the correct pairing already requires a difference of two classes, not a single positive triple intersection. For the other outputs the duals b-c and a-b likewise contain negative summands. The existence of a signed Euler formula is useful computationally, but is not a cancellation-free object count.

The missing step is to account positively for the dual-class subtractions at every input/output, after the required global sign normalization. Third full-target failure. It is a failure of the complementary-class shortcut, not an impossibility claim for a geometric positive formula.

<a id="q4592-a4"></a>
## A4: assemble every input positively from the known special Pieri factors

Attempt: use the proved positive Pieri rule repeatedly. Set e_lambda=(-1)^|lambda| O_lambda, so every product in the e basis has nonnegative structure coefficients. If each e_mu were a nonnegative combination of monomials in the special e_(r), a product with any first input could be counted by concatenated positive Pieri chains, with no subtraction.

This sufficient assembly contract fails already in the associated graded ring for n>=3. In degree three its only special monomials are Q3, Q2 Q1 and Q1³. Leading-degree Pieri gives

    Q2 Q1=Q21+2Q3,   Q1²=2Q2,   Q1³=2Q21+4Q3.

Hence every nonnegative linear combination of these monomials obeys

    coefficient_(Q3) >= 2 coefficient_(Q21).

The input Q21 has coefficients (Q21,Q3)=(1,0), so it is outside that cone. Terms of larger degree do not change the degree-three component. Terms of smaller degree cannot disappear in a nonnegative expression: their positive leading components survive. The signs of e_r multiply to the same overall (-1)^3 in degree three, so that normalization does not alter this obstruction. At n=2 the Q3 class is absent; the full target includes n>=3, where both classes exist.

The exact K Pieri inversion through degree four, freshly counted below, is

    O21 = O1 O2 - 2 O3 + O4 + 2 O31  (mod codimension >=5).

It provides a signed algorithm but begins with the required subtraction. No cancellation-free way of pairing the unwanted Q3 chains or a positive input assembly was obtained. Fourth full-target failure. This is a cone-of-special-factor obstruction, distinct from the Euler-dual obstruction A3; it does not prohibit a direct LR rule with more general objects.

<a id="q4592-a5"></a>
## A5: promote every ballot genomic Q-tableau to an exact positive rule

Attempt: enlarge the ordinary shifted tableaux using genes, with primed/unprimed labels and every genotype ballot, and count all genomic Q-tableaux. This is a genuine candidate object construction: the primary paper proves equality for one-row inputs and at leading cohomological degree. The attempted extension replaces its general upper-bound conjecture by exact equality.

For lambda=(3,1), mu=(2,1), nu=(4,3,1), the four skew positions are

    A=(1,4), B=(2,3), C=(2,4), D=(3,3).

The fresh enumeration uses alphabet 1'<1<2'<2, weak row/column increase, no repeated unprimed entry in a column, no repeated primed entry in a row, and no diagonal prime. Genes are consecutive intervals in the primary order (primes top-to-bottom before unprimes left-to-right), with no same-letter boxes in a gene sharing a row or column. Content (2,1) means two family-one genes and one family-two gene. Every genotype is read top-to-bottom, right-to-left; its doubled sequence is tested with primes treated exactly as in the source. There are 24 semistandard Q fillings, 20 valid gene partitions and six ballot genomic Q objects. The stronger genomic P subset has one object. These match the primary Example 8.5, but were independently enumerated, with the objects recorded.

The actual LG coefficient is reconstructed without assuming the proposed rule. Using the degree-four Pieri inversion in A4, the contribution from codimension>=5 is zero for output of size eight with input lambda of size four. Thus

    c^(431)_(31,21)
      = [O431](O31 O1 O2) - 2 [O431](O31 O3)
        + [O431](O31 O4) + 2 [O431](O31 O31).

Literal proved KLG Pieri counts give the four composite-path contributions -4,-6,-8,-2, totaling -20; the second and third coefficients are -3 and 1. The last is at leading degree and the proved ordinary/leading-Q rule gives 4, independently enumerated. Hence the coefficient is

    -20 - 2(-3) + 1 + 2(4) = -5.

Its sign-normalized value is 5, not 6. The primary source also states -5, so both the true coefficient and the candidate overcount are independently controlled. One must exclude or regroup some Q objects by a general correct positive criterion; accepting all of them fails. This does not refute the source's upper-bound conjecture, the proved Pieri equality, or the catalog target.

Fifth consecutive full-target failure: stop Q4592 unresolved. A1 forbids excess objects; A5 expressly allows them, but its fully specified enlarged candidate overcounts. This overlap in ordinary starting point is disclosed. No additional failed route is claimed for alternative ad hoc subsets of the six objects.

## Checker/source scope

[LG-RANK-TWO-CHECK.json](LG-RANK-TWO-CHECK.json) checks all 64 basis associativity triples and the Euler dual. [LG-PIERI-CHECK.json](LG-PIERI-CHECK.json), from [literal KLG checker](check_lg_pieri.py), records the complete signed coefficient reconstruction. [Q-GENOMIC-CHECK.json](Q-GENOMIC-CHECK.json), from [genomic checker](check_q_genomic.py), records all six candidate objects and the P subset. In its stand-alone receipt, -5 is labelled primary evidence; the separate Pieri receipt supplies the fresh exact reconstruction. The source's proved leading-degree equality is used only at that exact scope. Integer serialization and tool repairs count zero mathematical failures. Main-thread proof/count review remains pending. No full combinatorial LR rule or novelty is claimed.

