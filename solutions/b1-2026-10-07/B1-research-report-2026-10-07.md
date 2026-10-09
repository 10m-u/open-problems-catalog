# B1 Research Report

7 October 2026

## Main conclusion

**Q2168 has an affirmative solution.** If t is any positive transcendental real number, set

\[
W=\mathbb Q[t]+\operatorname{span}_{\mathbb Q}\{(t+n)^{-1}:n\ge1\},
\qquad P=W\times\mathbb Z,
\]

with coordinatewise addition, lexicographic order in which W is more significant, and distinguished 1=(0,1). Then

\[
\operatorname{SC}(P)=\Sigma_4.
\]

The proof constructs a Σ₄ Scott sentence and excludes every Π₄ Scott sentence. It uses only elementary facts about rational functions, Presburger quantifier elimination, and Montalbán's orbit theorem. The exact hierarchy and original Question 6.1 are those in [Block, version 3](https://arxiv.org/html/2601.21118v3); the orbit theorem is also checked against [Montalbán's author-hosted paper, Theorem 1.1](https://math.berkeley.edu/~antonio/papers/scottRank.pdf). The construction is proved in Part I. It is a result of this research session, not a theorem attributed to those sources.

Of the ten retained catalogue questions, **one is proved, eight have partial results, and one remains unresolved**. “Partial” never means that the original statement has been closed. The precise wordings and stable IDs are retained below and in the machine-readable ledger.

The main additional conclusions for the two-arithmetic programme are:

1. There is a sound uniform automatic encoding of modular addition, XOR, AND, fixed rotations, and fixed finite circuits. Ten counterexample languages are proved empty by complete finite-state certificates. Two deliberately false assertions have explicit counterexamples. These graph arguments cover every word width after the primitive semantics are proved; they are distinct from finite-width controls.
2. The original numeric Fourier nonzero-support relation is not automatic. Its restriction to a=b=2ⁿ forces P=2a² and has synchronized language {ZⁿAZⁿB:n≥0}. A reversed Walsh-mask coordinate repairs the support predicate, but uniform reversal itself is nonautomatic.
3. Common translations, common endomorphisms, common automorphisms, and common affine permutations of cyclic addition and XOR are classified with exact width exceptions. These are precise statements about specified map classes; they do not identify the missing original top-toggle specification by guesswork.
4. In paired Fourier block m, exact coherence is Cₘ=1/(2ᵐ sin(π/2ᵐ⁺¹)), decreasing to 2/π. The minimum Walsh entropy among cyclic-character rows is the explicit sum of binary entropies in Part III and is always below 1151/576<2 bits. Therefore a positive width-linear uncertainty bound fails even after restricting to the largest block.
5. Deterministic fixed-width correlations cannot decay exponentially to zero for all lengths: every permutation obeys c(T)≥1/√(2ʷ−1), and pure rotations have c=1 at every length.
6. Automatic predicates cannot witness Q246. Q2169 has a positive answer when the quotient has a least nonzero Archimedean class. The foundational questions have sound restricted decision procedures, an axiomatization obstruction, a restricted QE obstruction, and exact interval-family shatter formulas.

## Status and evidence conventions

The supplied handoff records a historical catalogue state with zero exact closures. That provenance is preserved in the copied input. The dispositions here record what is proved or left open by the present arguments; they are not edits to the external catalogue. Inspected primary versions are listed in the bibliography. A retained question in one inspected version is not a claim that every later publication has been exhaustively excluded.

Evidence is distinguished as written argument, primary-source comparison, finite computation, and compiled formal theorem. **No compiled formal theorem was obtained. No Walnut executable was run.** The automatic verification consists of explicit Python automata, mathematical semantic invariants, full transition graphs, independently checked graph certificates, and separate semantic controls. The model-theoretic results are written proofs with separate reviews within this session; no external peer-review status is claimed.

The Fourier sign conventions in the handoff differ between excerpts. They conjugate the overlap matrix and leave support, magnitudes, entropy, and every result used here unchanged. Width zero is excluded throughout the word arithmetic. The relational valuation at zero is false; the alternative total unary valuation has value zero at zero. Each use states its convention.

## Exact catalogue register

| Question | Stable statement ID | Exact retained statement | Report status and contribution |
|---|---|---|---|
| Q246 | b4cba42238e08ad101bc | Does some predicate R⊆ℕ make (ℤ,<,+,R) NIP but non-distal? NIP means every formula has finite VC-dimension; distal has its standard model-theoretic meaning. | **partial**. Every automatic unary predicate is excluded as a NIP but non-distal witness. |
| Q1375 | 3c545d79b70573f46278 | For each fixed k≥1, what is the exact decision complexity of BA_p sentences with k quantifier alternations? | **partial**. Conservative fixed-block automata bound; no elementary-time normalization of arbitrary sentences to equivalent Σ₂ sentences. |
| Q1376 | 7017180285bacc39c17f | Given regular L⊆Σ*, is it decidable whether [L] is definable by an existential BA_p formula? | **partial**. Affirmative semidecision; sound YES/NO/UNKNOWN automaton triage by growth; exact full-growth counterexample to completeness of that triage. |
| Q1377 | f8506c29d8d1507a5f50 | Is BA_k finitely axiomatizable? | **partial**. No axiomatization solely by universally quantified quantifier-free sentences, even an infinite one. |
| Q1378 | d1962d78132eb0c2aaac | Does BA_k have an expansion by finitely many definable functions or predicates whose theory eliminates quantifiers? | **partial**. No QE expansion whose added predicates and complements are existential and whose added total functions have existential graphs. |
| Q1481 | 8d48b234d27dbcb91ed7 | Is it decidable, given finite automata for regular L₁,L₂⊆Σ*, whether [L₁] is existentially definable in (N,0,1,+,[L₂],≤)? | **partial**. Affirmative semidecision; complete decision when the second predicate is ultimately periodic. |
| Q1979 | 11f085365348dc8d4680 | For every definable S in every model of Presburger arithmetic, is π_S(t) asymptotic to a polynomial? | **partial**. Exact shatter functions and leading constants for interval families and independent residue-class interval families in every Presburger model. |
| Q2168 | 70b5ed041cc98b2932f1 | Does a Presburger group P with SC(P)=Σ4 exist? | **proved**. Explicit countable Presburger group with a Σ₄ Scott sentence and no Π₄ Scott sentence; hence optimal complexity Σ₄. |
| Q2169 | c2fc98c1e0a3bc2fd1d8 | For every nonzero countable divisible ordered abelian group V, is DgSp(V)=DgSp(V×Z), with lexicographic order and distinguished 1=(0,1)? | **partial**. Degree-spectrum equality when the quotient has a least nonzero Archimedean class; includes finite Archimedean rank and finite dimension. |
| Q2170 | 86f031cac9140549efc3 | Does every countable non-automorphically-trivial structure have the same degree spectrum as some Presburger group? | **unresolved**. No universality theorem or forbidden degree spectrum obtained. |

## Structure of the complete argument

Part I proves Q2168 at the exact retained scope, including both Scott-complexity bounds. Part II gives the number encoding, all-width verification semantics, and the Fourier nonautomaticity boundary. Part III proves the algebraic classifications and Fourier estimates. Part IV contains the foundational partial results. Part V proves the Q246 obstruction and the Q2169 least-class theorem, and records the unchanged Q2170 gap. Part VI records executed checks and reproduction commands. Part VII identifies the remaining mathematical bottlenecks.

The verification archive contains this report, the ledger, complete individual proof notes, two written audit notes, the original supplied handoff, the source-version registry, every verification script and generated input, the complete graph certificates, all cited outputs, and a SHA-256 manifest. The superseded Laurent-space construction is retained only as a marked development draft; the final Q2168 proof is the rational-function construction in Part I.


## Part I A Presburger group of optimal Scott complexity Σ₄

Stable statement ID: `70b5ed041cc98b2932f1`.

Retained question: Does a Presburger group P with SC(P)=Σ₄ exist?

Answer: **Yes.** The construction below gives such a countable group. Evidence: written mathematical proof, checked separately by the root agent and the foundations agent. These checks are completed within this research session; no external peer review or proof-assistant compilation is claimed.

### Conventions and standard dependency

The language is L={+,<,0,1}; additive inverses and integer linear combinations in formulas are abbreviations obtained by moving negative terms across an equation or inequality. No additional function symbols or quantifiers are required for those abbreviations.

Use the infinitary hierarchy in Block, *Measuring the Complexity of Countable Presburger Models*, arXiv:2601.21118v3 (16 June 2026), §1.1, pp.2–3. Σ₀=Π₀ consists of finitary quantifier-free formulas. For α>0, a Σα formula is a countable disjunction of formulas ∃ȳ ψ, with ψ in Πβ for β<α. Πα is the dual class. The empty existential tuple is permitted, and the standard inclusions between adjacent levels are understood.

**Orbit theorem.** For a countable structure A and α>0, A has a Πα+1 Scott sentence if and only if every finite-tuple automorphism orbit in A is definable without parameters by a Σα infinitary formula. This is Montalbán's theorem, cited as Theorem 1.1 by Block; original reference: Antonio Montalbán, *A robuster Scott rank*, Proceedings of the American Mathematical Society 143 (2015), 5427–5436. We use α=2 for an expansion by one named constant, and α=3 for the unexpanded structure.

Primary comparison: Block's exact Question 6.1 is printed on p.29 in v3. The hierarchy and orbit theorem are at https://arxiv.org/html/2601.21118v3 (Theorem 1.1). Montalbán's author-hosted primary draft, https://math.berkeley.edu/~antonio/papers/scottRank.pdf , saved/compiled 23 March 2014, states this same theorem as Theorem 1.1 on p.1. The construction and proof below are new work in this session, not a claimed theorem from either paper.

### 1. The ordered vector space

Choose one positive transcendental real number t. Define

W = ℚ[t] + span_ℚ { 1/(t+n) : n≥1 } ⊂ ℝ.

Every member is a finite sum of a polynomial in t and rational multiples of the displayed reciprocals. Evaluation at t embeds the rational function field ℚ(T) into ℝ: a nonzero rational function over ℚ cannot vanish at a transcendental argument. Consequently we can reason about elements of W as rational functions. Such functions have at most simple poles, all belonging to the negative integers −1,−2,… . Their expression as a polynomial plus these simple-pole terms is unique, by partial fractions. In particular, (t+n)⁻¹ belongs to W and (t+n)⁻² does not.

W is a countable nonzero divisible ordered abelian group under real addition and order. Define

P = W × ℤ,

with coordinatewise addition, lexicographic order in which the W coordinate is more significant, 0=(0,0), and distinguished 1=(0,1). This is a Presburger group: it is a discretely ordered abelian group with least positive element 1, and for every positive integer m each (w,z) has a unique residue r∈{0,…,m−1} modulo m, because w/m∈W and z=mq+r in ℤ.

Write a=(1,0), where the first 1 is the real unit, distinct from P's distinguished group element (0,1).

### 2. Proper elementary substructures containing arbitrary finite sets

For each n≥1, set

Wₙ=(t+n)W,       Pₙ=Wₙ×ℤ ⊂ P.

Multiplication by t+n takes W into W, since it preserves polynomials and

(t+n)/(t+m) = 1 + (n−m)/(t+m).

Wₙ consists exactly of the members of W with zero coefficient on the pole term 1/(t+n). Multiplication by T+n removes that pole and creates no new one. Conversely, dividing a rational function in W with no pole at −n by T+n creates only a simple pole at −n and preserves simplicity of all other poles, so the quotient is again in W. Equivalently, this follows by polynomial division and partial fractions. Thus Wₙ is a proper divisible ordered subgroup of W, because (t+n)⁻¹∉Wₙ. The map

fₙ:Pₙ→P,       fₙ(w,z)=(w/(t+n),z)

is an ordered-group isomorphism preserving the distinguished 0 and 1.

Both Pₙ and P are models of Presburger arithmetic. Their inclusion preserves congruences modulo every positive integer: the residue of (w,z) in either structure is z modulo m. Presburger quantifier elimination in the expansion by all congruence predicates therefore implies

Pₙ ≺ P.

This appeal to quantifier elimination does not change the language in the statement: it establishes elementarity of the original L-structures.

Every finite subset F⊂P is contained in Pₙ for all sufficiently large n. Indeed, the W-coordinates of its elements have only finitely many poles in total. Outside that finite set of pole indices, those coordinates belong to Wₙ. In particular a∈Pₙ for every n and

fₙ(a)=aₙ=((t+n)⁻¹,0).

### 3. The elements a and aₙ are not automorphic

The set of elements divisible by every positive standard integer is characteristic in P and is exactly

D = ⋂_{m≥1}mP = W×{0}.

Any automorphism of P therefore restricts to a strictly order-preserving additive automorphism of W. Every strictly order-preserving additive homomorphism h:W→W is multiplication by h(1)>0: for every w∈W and rational q=m/r (r>0), the comparison rw<m is equivalent to rh(w)<mh(1). Consequently w and h(w)/h(1) have the same rational cut in ℝ and are equal.

If an automorphism sent a to aₙ, its restriction to D would have to be multiplication by (t+n)⁻¹. But that map sends (t+n)⁻¹∈W to (t+n)⁻²∉W, a rational function with a double pole. Hence it is not an automorphism, and aₙ is outside the orbit of a.

### 4. Downward preservation at Π₂

**Lemma.** If B≺A are finitary elementary structures, every infinitary Σ₁ formula is absolute between B and A for tuples from B. Every infinitary Π₂ formula true in A of a tuple from B is true in B of that tuple.

**Proof.** A Σ₁ formula is a countable disjunction of finitary existential quantifier-free formulas. Each disjunct is absolute by finitary elementarity; hence the disjunction is absolute. A Π₂ formula is a countable conjunction of universal closures of Σ₀ or Σ₁ formulas. If it holds in A, each of its universal instances with values in B holds in A and hence in B by the preceding absoluteness. ∎

### 5. The orbit of a has no Σ₃ definition

Let φ(x) be any parameter-free Σ₃ formula true of a in P. Select a true disjunct ∃ȳ ψ(x,ȳ), with ψ in Πβ for some β<3, and select finite witnesses b̄∈P. Regard ψ as Π₂ using the hierarchy inclusions.

Choose n outside the finite set of pole indices of the W-coordinates of b̄, so a,b̄∈Pₙ. The preservation lemma gives

Pₙ ⊨ ψ(a,b̄).

Applying fₙ yields

P ⊨ ψ(aₙ,fₙ(b̄)),

and hence P⊨φ(aₙ). Since aₙ is not automorphic to a, no such φ defines the orbit of a.

By the orbit theorem with α=3, P has no Π₄ Scott sentence.

### 6. A Σ₄ upper bound

Work in the expansion (P,a) naming a. Its automorphism group is trivial, by the scalar characterization in §3. We show that every element is definable by a Π₁ infinitary formula in this expansion.

Fix p=(w,z)∈P. First require the residue sequence of x to equal that of the integer z:

ρ_z(x) := ⋀_{m≥2} ∀y ⋀_{0≤r<m, r≠z mod m} x≠my+r·1.

This is Π₁. Within P it says that the integer coordinate of x is z, since an integer divisible by every positive integer is zero.

Next require x−z·1 to have real cut w relative to a. For each rational q=u/v with v>0, use the atomic comparison

v(x−z·1) < u a  if w<q,
v(x−z·1) = u a  if w=q,
v(x−z·1) > u a  if w>q.

Let θ_{w,z}(x,a) be the conjunction of all these comparisons. The displayed notation uses only integer coefficients, and negative terms can be moved to the opposite side. It is a Π₁ formula. In P, ρ_z(x)∧θ_{w,z}(x,a) holds exactly when x=(w,z), because distinct real numbers have distinct rational cuts.

For a finite tuple, take the finite conjunction of its coordinate formulas. Every automorphism orbit in (P,a) is therefore Π₁-definable, hence Σ₂-definable. By the orbit theorem with α=2, (P,a) has a Π₃ Scott sentence σ(a). Replacing the named constant by a variable and existentially quantifying it gives a Σ₄ Scott sentence ∃a σ(a) for P.

#### 6.1. An explicit schematic Scott sentence

The upper bound can also be obtained directly, without applying the orbit theorem. Enumerate P without repetitions as p₀,p₁,…, with p₀=0, p₁=1 and p₂=a. For pᵢ=(wᵢ,zᵢ), let Fᵢ(x,c)=ρ_{zᵢ}(x)∧θ_{wᵢ,zᵢ}(x,c). These are the Π₁ formulas just constructed. Let σ(c) consist of the following countable conjunction:

1. Every label is realized: ⋀ᵢ ∃x Fᵢ(x,c).
2. Every element receives a label: ∀x ⋁ᵢ Fᵢ(x,c).
3. Each label is unique: for every i, ∀x∀y[(Fᵢ(x,c)∧Fᵢ(y,c))→x=y].
4. Distinct labels denote distinct elements: the corresponding universal implication to x≠y for each i≠j.
5. The labelled elements have exactly the atomic diagram of P, with c labelled by p₂. For example, if pᵢ+pⱼ=pₖ, include ∀x∀y∀z[(Fᵢ(x,c)∧Fⱼ(y,c)∧Fₖ(z,c))→x+y=z]. For each i,j prescribe either x<y or its negation according to pᵢ<pⱼ. Prescribe x=0 for F₀, x=1 for F₁, and x=c for F₂.

Clauses 1 and 2 are Π₃. Clauses 3–5 are Π₂, since negating Fᵢ gives a Σ₁ formula and a finite disjunction of Σ₁ formulas with an atomic or negated-atomic conclusion remains Σ₁. Thus σ(c) is Π₃. Any model of it has exactly one element with each label, and its functions, relations and constants agree with those of (P,a). The label map is an isomorphism. Hence ∃c σ(c) is the claimed Σ₄ Scott sentence. This construction also shows directly why uniqueness of rational cuts in arbitrary nonstandard models does not need to be assumed: the Scott sentence explicitly imposes singleton and diagram conditions.

### 7. Optimality

P has a Σ₄ Scott sentence and no Π₄ Scott sentence. Every lower class Σα, Πα or d-Σα for α<4 is contained in Π₄ after the usual padding of quantifier blocks. In particular, a d-Σ₃ sentence is Π₄, so the missing possibility d-Σ₃ is excluded as well. Consequently

SC(P)=Σ₄.

This proves the exact retained existence statement, under its stated countable-structure and infinitary-complexity conventions.

### 8. Optional effective strengthening

The number t may be chosen to be a computable transcendental in (1,2). For completeness, enumerate the nonzero integer polynomials f₀,f₁,… . Starting from (1,2), choose successively nested closed rational intervals I_s with nonempty interior and diameter at most 2⁻ˢ, requiring I_s to be contained in the interior of I_{s−1} and f_j to be bounded away from zero on I_s for j≤s. Such an interval can be found effectively: rational points avoiding the finitely many zero sets are dense, and a sufficiently small rational interval around such a point has all required polynomial signs fixed, as verified by rational interval arithmetic. The unique point in the nested intervals is a computable positive transcendental.

The unique polynomial-plus-partial-fractions expressions form an effective presentation of W. Equality is decided symbolically; the sign of a nonzero difference is obtained by approximating t until interval evaluation excludes zero, which must eventually occur by transcendence. Addition and rational scaling are symbolic. Thus W and P admit computable presentations. This strengthening is not needed for the retained question; no such presentation was executed or formally compiled in this draft.


## Part II Uniform encoding and the Fourier automaticity boundary

Date: 7 October 2026. These results belong to B1's proposed automatic-proof lane. They have **no assigned catalog Q number or canonical stable statement ID**. They do not by themselves resolve Q1375–Q1378 or Q1481. Local result labels below are not replacements for catalog IDs.

### 1. Domain and notation

All arithmetic variables range over the standard naturals, including zero. The word bound is the **value** \(P=2^w\), with \(w\geq1\); the formula quantifies over \(P\), not over an exponent variable linked by an assumed exponential function. Let \(X_P=[0,P)\). Write \(x+_P y\) for cyclic addition and \(x\oplus y\) for XOR.

The primitive valuation relation is \(V_2(d,x)\): \(x>0\) and \(d\) is the largest power of two dividing \(x\). Thus \(V_2(d,0)\) is false for every \(d\). In the alternative unary convention, \(V_2(0)=0\), and the relational graph is obtained by additionally requiring \(x>0\). These two conventions are never silently interchanged.

Define

\[
\operatorname{Pow}(p):=p>0\land V_2(p,p),\qquad
D(P,x_1,\ldots,x_r):=\operatorname{Pow}(P)\land P\geq2\land\bigwedge_i x_i<P.
\]

For positive powers \(p\), the bit at place \(p\) is definable by

\[
\operatorname{Bit}(x,p):=\operatorname{Pow}(p)\land
\exists u,r\;(x=u+r\land r<p\land V_2(p,u)).
\]

Indeed, \(u\) has zero bits below \(p\) and a one at \(p\), while adding \(r<p\) changes only the lower bits. Conversely take \(u=x-(x\bmod p)\). The displayed subtraction and remainder are only in the correctness argument; they are not extra symbols in the formula.

Consequently

\[
\operatorname{Xor}(x,y,z):=\forall p\;\bigl(\operatorname{Pow}(p)\to
[\operatorname{Bit}(z,p)\leftrightarrow
(\operatorname{Bit}(x,p)\mathbin{\mathrm{xor}}\operatorname{Bit}(y,p))]\bigr)
\]

defines ordinary XOR. All powers are quantified, so no extra high bit of \(z\) can survive. Replacing Boolean xor by conjunction defines bitwise AND. An explicit two-state digit automaton is much smaller than naively compiling these definitions.

The modular adder is already Presburger-definable apart from the power guard:

\[
\operatorname{ModAdd}(P,x,y,z):=D(P,x,y,z)\land(x+y=z\lor x+y=z+P).
\]

No variable multiplication occurs. Exactly one of the two alternatives holds because \(x+y<2P\).

### 2. Inventory of permitted operations

| Operation or relation | Uniform encoding | Qualification |
|---|---|---|
| Word bound and membership | \(\operatorname{Pow}(P),x<P\) | Width is supplied by the value \(P\). |
| Modular addition | The displayed two-branch formula | Includes discarded overflow. |
| XOR and AND | Bit formula or two-state column checker | No fixed-width expansion is required. |
| Multiplication or division by a fixed integer | Linear equations and inequalities | The coefficient must be a numeral. |
| Fixed one-bit cyclic rotation | Linear case split below | A fixed composition remains automatic. |
| Fixed-size circuits built from these operations | Existentially bind intermediate values | Number of gates is fixed in the formula. |
| First-order properties of such circuits | Boolean operations and number quantification | Resource cost can grow sharply with quantifier blocks. |
| \(P=2^n\) with numerical variable \(n\) | Not automatic | Proof below; a power predicate does not supply its exponent. |
| Arbitrary multiplication, even \(P=2a^2\) on powers | Not automatic | Required by a slice of the original Fourier support relation. |
| Exact uniform popcount or numerical word length | Not automatic | Each would define the exponential graph. |
| Original Fourier nonzero support \((P,a,b)\) | Not automatic | Theorem B1-BOUNDARY-01 below. |
| Support with reversed Walsh mask \((P,a,r)\) | Existential BA₂ | Conversion between \(b\) and \(r\) is itself nonautomatic. |
| Exact Fourier amplitudes and entropy | No direct BA₂ encoding supplied | Analytic proofs apply; the nonzero-support obstruction is already enough to exclude a uniform automatic amplitude encoding whose zero test recovers support. |

For a one-bit left rotation let \(2h=P\). Its graph on \(X_P\) is the disjunction

\[
\exists u\;[x=u<h\land y=2u]
\quad\lor\quad
\exists u\;[x=u+h\land u<h\land y=2u+1].
\]

For a one-bit right rotation, use \(x=2u,y=u\), or \(x=2u+1,y=u+h\), with the same bounds. Here \(x=u<h\) abbreviates \(x=u\land u<h\). Variable rotation count, variable circuit length, and quantification over arbitrary maps are not supplied by this inventory.

### 3. Executed all-width verification

#### Representation and primitive automata

Every tuple is read synchronously, least significant binary digit first. A symbol is a vector in \(\{0,1\}^r\). In JSON it is the integer whose bit \(i\) is the digit of track \(i\). Any number of final all-zero columns is permitted. Acceptance is by final state of a finite word. The empty representation denotes an all-zero tuple for unbounded primitives; the word-domain guard rejects it because it requires \(P\geq2\).

The modular adder has five states before minimization: START, carry 0, carry 1, AFTER, DEAD. Before the unique one on the \(P\) track, each column checks

\[
x_i+y_i+c_i=z_i+2c_{i+1},\qquad c_0=0.
\]

At the \(P\)-marker all word tracks must be zero; either outgoing carry is discarded, and the machine enters AFTER. Only all-zero columns are allowed thereafter. A marker at START is rejected, excluding \(P=1\). Missing or repeated markers and words outside \([0,P)\) are rejected.

The loop invariant after \(j\) data columns is

\[
\sum_{i<j}x_i2^i+\sum_{i<j}y_i2^i
=\sum_{i<j}z_i2^i+2^jc_j.
\]

At the marker \(j=w\), this is precisely equality modulo \(P\). This proves the primitive semantics for every width. The independent linear-equation construction also checks that this graph agrees with the Presburger formula in §1.

The XOR and AND automata have one accepting live state and one rejecting dead state, checking their Boolean relation in every column. The valuation machine waits for the first one on the number track, requires the only one on the power track to occur in the same column, then requires that power track to stay zero. Its zero convention is therefore explicit.

For the generic equality \(\sum_i a_i x_i=c\), the machine starts with carry \(-c\). It requires \(q+\sum_i a_i b_i\) to be even in each column and replaces \(q\) by half that value. It accepts with final carry zero. The invariant is

\[
q_j=\frac{\sum_i a_i(x_i\bmod2^j)-c}{2^j}.
\]

The reachable carry set is finite because the recurrence contracts the carry outside a fixed interval determined by the coefficients. This proves correctness for positive and negative coefficients.

#### Quantification and the padding issue

Existential quantification erases tracks, yielding nondeterministic transitions. The implementation also takes the right quotient by all-zero columns on the retained tracks: a projected state is accepting when the original automaton can reach a final state after further columns whose visible digits are all zero. Witness digits on erased tracks are unrestricted. This step is necessary because a quantified witness can have more digits than the free variables. Subset construction then gives a deterministic automaton. The explicit control \(\exists y(x=0\land y=8)\leftrightarrow x=0\) checks this issue, including the empty and arbitrarily padded representations of zero.

Boolean products, complements of complete deterministic machines, and projection preserve the stated semantics. Universal number quantification uses complement–projection–complement. No claim about arbitrary second-order or function quantification is made.

#### Why the certificates are uniform

For every counterexample automaton, the certificate lists a set of states containing the initial state and closed under every alphabet transition. If it contains no final state, induction on word length proves there is no accepted word of **any length**. Every numerical tuple has such a finite representation. Thus emptiness proves the quantified statement for every word width, not merely for the bounded semantic controls.

`verification/check_certificates.py` does not import the builder. It independently checks graph dimensions, transition destinations, certificate closure, the exact reachable set, file hashes, and the claimed absence or presence of accepting states. Its trust boundary does not include a proof that the compiler implements the displayed formulas; that connection is supplied by the primitive invariants and construction arguments above, the archived builder, and mathematical review. No Lean/Coq kernel theorem or Walnut execution is claimed.

The suite proves:

1. The direct adder equals its Presburger definition.
2. Addition and XOR both have the expected lowest bit.
3. Adding \(P/2\) equals XOR by \(P/2\).
4. \(x+_Py=x\oplus y\) iff \(x\mathbin{\&}y\in\{0,P/2\}\).
5. \(\forall x<P\;(x+_Pa=x\oplus b)\) iff \(a=b\in\{0,P/2\}\).
6. The existential padding control.
7. For \(w\geq2\), toggling the top bit exactly when the bottom bit is one preserves both addition and XOR and is an involution.

Two deliberately false universal assertions produce witnesses. The raw transcript and separate checker output are preserved. The recorded run takes approximately 0.505 seconds under Python 3.12.14, with peak RSS 17,152 KiB. The largest intermediate construction has 88 states and 45,056 transitions; its alphabet has 512 columns. Declared limits are 100,000 states and 5,000,000 transitions per construction, plus a 60-second process timeout. There are no randomized steps.

The separate finite controls cover all 4,680 input triples for each of addition and XOR across widths 1–4, 1,024 valuation pairs, and 340 translation-parameter pairs. These controls check encoding agreement; the reachability certificates carry the all-width conclusions.

#### Tool comparison

The official Walnut repository and command/file-format documentation were inspected on 7 October 2026 before implementation. The repository describes version 8.0-alpha; the changelog dates 7.1 to 2 December 2025. No Walnut executable was run. This archive instead supplies a standard-library Python verifier and complete automata in JSON plus Walnut text format. The text exports follow the documented `lsd_2` alphabet/state/transition convention; they have not been imported by Walnut in this environment.

Primary references:

- [Walnut repository](https://github.com/Walnut-Theorem-Prover/Walnut), README and changelog.
- [Walnut file format](https://github.com/Walnut-Theorem-Prover/Walnut/wiki/Walnut-file-format), version edited 2 November 2025.
- [Walnut def/eval](https://github.com/Walnut-Theorem-Prover/Walnut/wiki/Command:def-or-eval), version edited 7 September 2026.
- Khodier–Schaeffer–Shallit, [Self-Verifying Predicates in Büchi Arithmetic](https://arxiv.org/html/2507.19717v1), 25 July 2025, Theorem 2 and §4.2: primary description of the formula-to-automaton and counterexample-emptiness method. The present implementation is independent code, not a run of their program.

### 4. The Fourier support obstruction

**Local result B1-BOUNDARY-01.** Let \(P=2^w\), \(w\geq1\), \(0\leq a,b<P\), and

\[
M_P(a,b)=P^{-1}\sum_{x=0}^{P-1}e^{2\pi i ax/P}(-1)^{\langle b,x\rangle}.
\]

The ternary relation

\[
S(P,a,b)\iff D(P,a,b)\land M_P(a,b)\ne0
\]

is **not** first-order definable in BA₂ in the original numeric coordinates. Evidence: written argument using the standard equivalence of Büchi definability and synchronized binary recognizability; no inference from a failed software run.

#### Dependency lemma: exact support

Writing \(x=\sum_{i=0}^{w-1}x_i2^i\) gives the finite product

\[
M_P(a,b)=P^{-1}\prod_{i=0}^{w-1}\left(1+(-1)^{b_i}e^{2\pi i a2^i/P}\right).
\]

If \(a=0\), every factor forces \(b_i=0\), so only \(b=0\) survives. If \(a>0\), put \(v=v_2(a)\). At \(i=w-v-1\), the exponential is \(-1\), so \(b_i=1\) is necessary. At larger \(i\), the exponential is \(1\), forcing \(b_i=0\). At smaller \(i\), the exponential is neither \(1\) nor \(-1\), so either digit is allowed. Hence

\[
S(P,a,b)\iff
(a=b=0)\quad\text{or}\quad
\bigl(a,b>0\land v_2(a)+\operatorname{msb}(b)=w-1\bigr),
\]

within the domain. The opposite sign in the exponential conjugates the product and has the same support and magnitudes. The source handoff uses both signs in different excerpts; this distinction does not affect this theorem.

#### Nonregular diagonal slice

Restrict to \(a=b=2^n\), \(n\geq0\). The support condition becomes

\[
w=2n+1,\qquad P=2^{2n+1}=2a^2.
\]

Suppose \(S\) were automatic. Intersect its recognizer with the automatic conditions \(a=b\), \(a>0\), \(\operatorname{Pow}(a)\), and canonical tuple termination. In track order \((a,b,P)\), define symbols

\[
Z=(0,0,0),\quad A=(1,1,0),\quad B=(0,0,1).
\]

The resulting least-significant-first language is exactly

\[
\{Z^n A Z^n B:n\geq0\}.
\]

This is not regular. If a pumping length were \(N\), pumping a nonempty segment inside the initial \(Z^N\) of \(Z^N A Z^N B\) would change only the first zero block. Equality of the two block lengths would fail. This contradicts closure of regular languages under the stated restrictions, proving the theorem.

For a deterministic automaton agreeing with the support relation on all widths at most \(W\), the prefixes \(Z^0,\ldots,Z^{\lfloor(W-1)/2\rfloor}\) have pairwise distinguishable continuation languages within that width cap: append \(AZ^iB\) to distinguish \(Z^i\) from \(Z^j\). Thus even such bounded agreement requires at least \(\lfloor(W-1)/2\rfloor+1\) states. The main theorem is stronger than this linear lower bound.

#### Automatic restricted fragments

For any **fixed** valuation \(v_2(a)=c\), support is the automatic condition

\[
2^{c+1}b\geq P\quad\land\quad2^c b<P,
\]

together with the domain and the fixed valuation condition. The powers \(2^c\) are constants, not variables. Finite unions of such fixed bands are also automatic. Thus the obstruction is the simultaneous unbounded variation of the two bit positions.

### 5. An explicit change of coordinates recovers automatic support

**Local result B1-BOUNDARY-02.** Let

\[
r=\operatorname{Rev}_w(b)=\sum_{i=0}^{w-1}b_i2^{w-1-i}.
\]

For \(b>0\), \(v_2(r)=w-1-\operatorname{msb}(b)\). Therefore support in the coordinates \((P,a,r)\) is

\[
D(P,a,r)\land\left[(a=r=0)\lor\exists d\;(V_2(d,a)\land V_2(d,r))\right].
\]

This is existential BA₂. It gives a useful automatic representation of the support blocks when the reversed Walsh index is the native input. It does not define support in the original coordinates: the conversion graph \((P,b,r)\) for \(r=\operatorname{Rev}_w(b)\) is nonautomatic. Restrict that graph to \(b=r=2^n\); the same nonregular language from §4 results.

The encoding choice therefore depends on the relations that must coexist. Computing \(r\) externally is possible at each finite width, but is not a first-order definable conversion within BA₂. No conclusion about arbitrary representations or richer logics follows from nondefinability in the specified numeric coordinates.

### 6. Additional exact boundaries: exponential, multiplication, counting

**Finite-output length lemma.** Let a binary synchronized automaton with \(N\) states recognize the graph of a partial function \(f:\mathbb N^r\to\mathbb N\). For every input in its domain, the output's binary length is at most the maximum input length plus \(N\) (an inessential one-column convention can change the bound by one).

**Proof.** Use a canonical least-significant-first representation. If the output extends more than \(N\) columns beyond every input, some state repeats strictly before the output's final one and after all input digits end. Pump that loop. All input tracks receive only padding zeros, so the input tuple is unchanged. The output's final one shifts to a new position, giving a different output for the same input. This contradicts functionality. ∎

Consequences:

- The graph \(P=2^n\) is not automatic, because its output length is \(n+1\), whereas the input length is \(O(\log n)\).
- The graph \(y=x^2\), even restricted to powers of two, is not automatic. Hence unrestricted multiplication cannot be supplied as a BA₂ function.
- If numerical bit length \(\ell(x)\) were automatic, its graph restricted to positive powers, with variables exchanged, would define \(x=2^{\ell-1}\), contradicting the exponential case.
- If exact popcount \(H(x,n)\) were automatic, then \(\operatorname{Pow}(P)\land\exists x(x+1=P\land H(x,n))\) would define \(P=2^n\). Thus exact unbounded popcount is not automatic either.

This does not forbid all counting information. For example, popcount modulo any fixed modulus is automatic, and counts of some specially chosen fibers have automatic graphs. The forbidden claim is an unrestricted exact count operator.

For the automaticity equivalence used here, see Bell–Block Gorman–Schulz, [A Dichotomy for k-automatic expansions of Presburger Arithmetic](https://arxiv.org/html/2508.04851v2), 13 May 2026, introduction and §2.3, with its primary Büchi/Bruyère references. The boundary arguments in §§4–6 are supplied in full above.


## Part III Algebraic classifications and exact Fourier estimates

Date: 7 October 2026. Input: `B1 Automatic Proofs - Agent Handoff 2026-10-07.md`, especially the programme context and the excerpts from inverse inquiries 04 and 25. These are written mathematical proofs, supplemented by bounded computation. No proof assistant was run. No claim of literature novelty is made. None of the ten retained catalogue questions is closed by these results.

### 1. Domain, notation, and the missing original map specification

Throughout, let `w` be an integer with `w >= 1`, let `P = 2^w`, and let `X_w = {0,...,P-1}`. Write `x +_P y` for cyclic addition modulo `P`, and `x xor y` for the XOR of their `w` binary digits. Put `h=P/2`. A word is identified with its ordinary unsigned integer value, with digit zero the least significant digit.

The handoff does not give the original statement defining the “shared top-bit-toggle map.” Consequently, that original statement cannot be recovered or certified here. A precise and natural statement can nevertheless be proved uniformly: the intersection of the two translation groups consists of the identity and the top-bit toggle. The latter is the unique nonidentity common translation. This assertion is different from a claim about common group automorphisms or common affine permutations; those classes are also classified below.

| Class of maps on `X_w` | Exact answer |
|---|---|
| Maps that are translations for both operations | `x`, and `x xor h = x +_P h` |
| Maps commuting with every translation for both operations | The same two maps |
| Common group automorphisms, `w>=2` | `x`, and `(1+h)x mod P = x xor (h x_0)` |
| Common group endomorphisms | Multipliers `0`, `2^r` for `0<=r<w`, and `h+2^r` for `0<=r<w-1` |
| Cyclic affine permutations that are also XOR affine, `w>=3` | The 16 maps classified in Section 5 |

The symbol `h x_0` in this table denotes either zero or `h` according to the single bit `x_0`; it does not presuppose definability of unrestricted multiplication. Width one and two exceptions are stated explicitly below. Width zero is excluded.

### 2. Carry identities and lowest-bit compatibility

**Lemma 2.1 (one-bit carry).** For every `a,b,c` in `{0,1}`, there are unique `s,d` in `{0,1}` such that

`a+b+c = s+2d`.

They are `s=a xor b xor c` and `d=1` exactly when at least two of `a,b,c` equal one.

| a | b | c | s | d |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

**Proof.** The four possible integer totals are `0,1,2,3`, whose binary representations give the stated outputs. This also proves uniqueness. The displayed table is the complete enumeration of inputs. ∎

For addition of two words, set `c_0=0` and use the lemma successively at digits `i=0,...,w-1`. Then

`x+y = sum_{i<w} s_i 2^i + c_w P`.

This follows by multiplying `x_i+y_i+c_i=s_i+2c_{i+1}` by `2^i` and summing; all intermediate carry terms cancel. Therefore the low `w` output digits are exactly `x+_P y`, and

`(x+_P y)_0 = x_0 xor y_0 = (x xor y)_0`.

This proof is uniform in `w`; the eight-row table is a dependency lemma, not a finite-width substitute for the proof.

**Lemma 2.2 (the exact carry mask).** For all `x,y in X_w`, the natural-number identity

`x+y = (x xor y) + 2(x AND y)`

holds. Consequently,

`x+_P y = x xor y` if and only if `x AND y` belongs to `{0,h}`.

**Proof.** At each bit, `x_i+y_i=(x_i xor y_i)+2x_i y_i`; sum these identities with weights `2^i`. The equality modulo `P` is equivalent to `P` dividing `2(x AND y)`. Since `0<=x AND y<P`, its only possible values with this property are `0` and `h`. ∎

The ordinary nonmodular condition would require `x AND y=0`. Allowing an overlap at the highest bit is essential for modular addition.

### 3. Common translations and the strongest justified toggle uniqueness

**Theorem 3.1.** For every `w>=1` and every `a,b in X_w`,

`for all x in X_w, x+_P a = x xor b`

if and only if `a=b` and `a in {0,h}`.

**Proof.** At `x=0`, the displayed identity gives `a=b`. At `x=a`, it then gives `2a=0 mod P`, so `a=0` or `a=h`. Conversely, translation by zero is the identity. Write any word as `x=r+epsilon h` with `0<=r<h` and `epsilon in {0,1}`. Adding `h` modulo `P` switches `epsilon` and preserves `r`, precisely as XOR by `h` does. ∎

**Corollary 3.2 (centralizer version).** The only permutations commuting with every cyclic translation and every XOR translation are the identity and the top-bit toggle.

**Proof.** Suppose `F` commutes with all cyclic translations, and let `a=F(0)`. Commutation with translation by `x` gives `F(x)=x+_P a`. Commutation with XOR translation by `x` similarly gives `F(x)=x xor a`. Apply Theorem 3.1. Both displayed maps do commute with all translations in both abelian groups. ∎

The toggle is not a group automorphism, because it sends zero to `h`. Confusing translations with automorphisms would produce an incorrect uniqueness claim.

### 4. All common endomorphisms and automorphisms

**Theorem 4.1.** For `w>=2`, multiplication by an odd residue `u` modulo `P` is XOR linear if and only if `u=1` or `u=1+h`.

**Proof of necessity.** Suppose multiplication by `u` is XOR linear. For each `1<=j<=w-2`, the identity `1+2^j=1 xor 2^j` implies

`u +_P (2^j u mod P) = u xor (2^j u mod P)`.

By Lemma 2.2, the bitwise intersection of the two words on the right can have no nonzero digit below `w-1`. Since `u` is odd, digit `j` of `2^j u mod P` equals one. Thus digit `j` of `u` must equal zero. The only possible digits of `u` are therefore its required digit zero and its optional top digit: `u=1` or `1+h`.

**Proof of sufficiency.** Multiplication by one is the identity. Since `h x mod P` depends only on the parity of `x`,

`(1+h)x mod P = x +_P (h x_0) = x xor (h x_0)`.

This is the XOR linear shear which adds digit zero to digit `w-1` and leaves all other digits unchanged. Because these are distinct digits for `w>=2`, applying it twice is the identity. ∎

**Theorem 4.2.** The common endomorphisms of the two groups on `X_w` are precisely the maps `x -> m x mod P` with

`m in {0} union {2^r: 0<=r<w} union {h+2^r: 0<=r<w-1}`.

There are exactly `2w` such maps. For `w>=2`, exactly two are automorphisms: the maps in Theorem 4.1. For `w=1`, the common endomorphisms are zero and identity, and identity is the only automorphism.

**Proof.** Every endomorphism of the cyclic group is multiplication by its value at one. The zero multiplier is admissible. If `m!=0`, write `m=2^r u` with `u` odd and `n=w-r`. Multiplication by `m` factors as reduction to the lowest `n` input digits, multiplication by `u` modulo `2^n`, and an embedding shifting all output digits upward by `r`. The first and last maps are XOR linear. The middle map is XOR linear if and only if the original map is: the reverse implication follows by restricting inputs to `0<=x<2^n` and reading the shifted output. For `n>=2`, Theorem 4.1 gives `u=1` or `u=1+2^{n-1}`. These become `m=2^r` or `2^r+h`. For `n=1`, only `u=1` is possible. The displayed residues are distinct, and their count is `1+w+(w-1)=2w`. A cyclic multiplier is invertible if and only if it is odd, yielding the automorphism assertion. ∎

This classification of admissible multipliers does not, by itself, supply a uniform automatic graph for every corresponding action when the multiplier is a variable. Variable shifts need separate scrutiny.

### 5. Common affine permutations: a complete classification

A map is XOR affine when it has the form `L(x) xor c`, where `L` is a linear transformation over the two-element field. Such a map is a permutation exactly when `L` is invertible. A cyclic affine permutation is `f(x)=a x+b mod P`, where `a` is odd.

**Lemma 5.1.** For `w>=2`, translation `T_b(x)=x+_P b` is XOR affine if and only if `P/4` divides `b`. For `w=1`, both translations are XOR affine.

**Proof of necessity.** The case `b=0` is immediate. Otherwise write `b=2^r c`, with `c` odd. If `w-r>=3`, restrict inputs to `x=2^r t` for `t=0,1,2,3`, and read the output after division by `2^r`. XOR affinity would imply

`c xor (c+1) xor (c+2) xor (c+3) = 0 mod 2^{w-r}`.

In the lowest three bits this XOR is four for every odd `c`. Indeed the possible initial residues `c mod 8` are `1,3,5,7`, and the four respective XORs of consecutive residues are all four. This contradicts affinity. Thus `r>=w-2`, which is the required divisibility.

**Proof of sufficiency.** Write `q=P/4`, `b=dq`, and `x=s+qt` with `0<=s<q` and `d,t in {0,1,2,3}`. The low digits represented by `s` do not change, and the top two digits undergo addition by `d` modulo four. In binary, with `t=t_0+2t_1` and `d=d_0+2d_1`, their outputs are

`t'_0=t_0 xor d_0`,

`t'_1=t_1 xor d_1 xor (d_0 t_0)`.

Since `d_0` is fixed, these are affine Boolean functions. ∎

**Theorem 5.2.** For every `w>=3`, put `q=P/4` and `h=P/2`. A cyclic affine permutation `a x+b mod P` is XOR affine if and only if one of the following disjoint alternatives holds:

1. `a in {1,1+h}` and `b in {0,q,2q,3q}`.
2. `a in {P-1,h-1}` and `b in {q-1,2q-1,3q-1,4q-1}`.

Thus there are exactly 16 maps. At width two, all eight cyclic affine permutations are XOR affine. At width one, both permutations are XOR affine.

**Proof: restrict the slope.** Write `a=2k+1`, and let `beta=b mod 2`. XOR affinity requires that `f(2y) xor f(2y+1)` be independent of `y`. The values `z=f(2y)` run through all words with parity `beta`, because multiplication by the odd number `a` permutes residues modulo `h`. Write `z=2t+beta`. Then

`z+_P a = 2(t+k+beta mod h)+(1-beta)`.

Consequently, constancy of the Boolean difference is equivalent to constancy of

`t xor (t+k+beta mod h)`

over all `t in {0,...,h-1}`. Theorem 3.1 at width `w-1` says this holds exactly when `k+beta` is zero or `h/2` modulo `h`. If `beta=0`, this forces `a in {1,1+h}`. If `beta=1`, it forces `a in {P-1,h-1}`.

**Proof: restrict the intercept and prove sufficiency.** Both multipliers in `{1,1+h}` are invertible XOR linear maps by Theorem 4.1. Composition with either does not affect whether the translation `T_b` is XOR affine. Therefore the positive-slope cases are exactly those with `q|b`, by Lemma 5.1.

For negative slopes, write `a=-u mod P` with `u in {1,1+h}`. The complement `C(x)=P-1-x` is XOR by the all-ones word and is therefore XOR affine. The identity

`a x+b mod P = T_{b+1}(C(u x mod P))`

shows that the negative-slope cases are exactly those with `q|(b+1)`. This also proves sufficiency for every displayed map. The two slope sets are disjoint when `w>=3`. At width two, the multiplier sets coincide and `q=1`, so all eight cases are admitted. At width one both arithmetic operations are the same two-element operation. ∎

**Extension 5.3 (noninvertible affine maps).** For an arbitrary multiplier `a`, all constant maps (`a=0`) are XOR affine. Otherwise write `a=2^r u`, `n=w-r`, and `b=b_low+2^r d` with `0<=b_low<2^r`. Then `a x+b mod P` is XOR affine if and only if the odd-slope affine map `u x+d mod 2^n` is XOR affine. The above classification, including its width-one and width-two cases, gives a complete decision rule. This follows from exactly the reduction-and-embedding argument in Theorem 4.2; the low `r` output bits are constant.

### 6. Shared characters and rotation

Let `omega=exp(2 pi i/P)`, `chi_a(x)=omega^{a x}`, and `psi_b(x)=(-1)^{sum_i b_i x_i}`. Exponents in `psi_b` are taken modulo two.

**Theorem 6.1.** The characters shared by cyclic addition and XOR are exactly the trivial character and the parity character: `(a,b)=(0,0)` and `(a,b)=(h,1)`.

**Proof.** A common character has value at one satisfying `chi(1)^2=chi(1 xor 1)=chi(0)=1`. As a cyclic character it is completely determined by its value at one, which is therefore either `1` or `-1`. The two resulting characters are the constant character and `(-1)^x`, respectively. Both are XOR characters, with masks zero and one. ∎

Define the normalized overlap using the negative sign convention

`M_w[a,b] = P^{-1} sum_{x in X_w} omega^{-a x} psi_b(x)`.

The inquiry 04 excerpt uses the positive sign, whereas inquiry 25 displays the negative sign in its product formula. The two versions are complex conjugates and have the same magnitudes and support. No support or magnitude result below depends on that choice.

The triangle inequality gives `|M_w[a,b]|<=1`. Equality holds only when all summands have the same phase. The `x=0` summand is one, so equality means `omega^{-a x}psi_b(x)=1` for every `x`. Theorem 6.1 therefore proves that the two displayed pairs are the complete equality set, at every width.

If `rho` is the cyclic permutation of all `w` digit positions, an XOR character is `rho` invariant exactly when all digits of its mask are equal. Its masks are consequently zero and the all-ones word. For `w>=2`, their intersection with the nonzero shared-character mask `{1}` is empty. At width one, rotation is identity, so the exception must be retained.

### 7. Fourier blocks, exact coherence, and bounded row entropy

#### 7.1 Product and support audit

Summing independently over binary digits gives

`M_w[a,b] = product_{i=0}^{w-1} (1+(-1)^{b_i} exp(-2 pi i a 2^i/P))/2`.

For `a=0`, this equals one at `b=0` and zero elsewhere. For `a!=0`, write `a=2^v d`, where `d` is odd, and put `m=w-1-v`. At digits `i>m`, the exponential equals one, forcing `b_i=0` for nonzero overlap. At digit `m`, it equals minus one, forcing `b_m=1`. At smaller digits neither choice vanishes. Thus

`M_w[a,b]!=0` if and only if `msb(b)=w-1-v_2(a)`

for nonzero `a,b`. Each paired block indexed by `m` has `2^m` rows and `2^m` columns. The exceptional trivial cell `(0,0)` is separate.

The factors in the squared magnitude are independent Bernoulli probabilities. For a row in block `m`, the free-digit parameters, in reverse order, are

`p_j(d)=sin^2(pi d/2^j), j=2,...,m+1`.

The forced digits contribute no entropy.

#### 7.2 Exact maximum magnitude in every block

**Theorem 7.1.** The maximum overlap magnitude in block `m` is

`C_m = product_{j=2}^{m+1} cos(pi/2^j) = 1/(2^m sin(pi/2^{m+1}))`.

This includes `C_0=1`. An attaining pair is

`a=2^{w-m-1}, b=2^m`.

The sequence `C_m` strictly decreases and converges to `2/pi`.

**Proof.** For odd `d`, the angle `pi d/2^j` is at distance at least `pi/2^j` from the nearest multiple of `pi/2`. Therefore

`max(|sin(pi d/2^j)|,|cos(pi d/2^j)|) <= cos(pi/2^j)`.

Every free-digit factor satisfies this bound. Setting `d=1` and all lower mask digits to zero attains every factor simultaneously; the forced digit contributes one. Iterating the identity `sin(2t)=2 sin(t)cos(t)` yields the product formula. Each additional cosine factor is strictly below one and positive, proving strict decrease. Finally `sin(t)/t -> 1` at zero, so the displayed closed expression tends to `2/pi`. ∎

For w>=2, removing the two common-character cells leaves exact coherence `1/sqrt(2)`, attained in block `m=1`. More strongly, the largest block, of size `2^{w-1}`, has coherence tending to `2/pi`, not zero. Merely discarding small paired blocks cannot create a coherence that vanishes with width.

#### 7.3 Exact minimum Shannon entropy among rows of a block

For a probability `p`, let `h_2(p)=-p log_2 p-(1-p)log_2(1-p)`, with endpoint values zero. The Walsh coefficient probabilities of a unit cyclic character are `|M_w[a,b]|^2`.

**Theorem 7.2.** The minimum Walsh Shannon entropy among the cyclic-character rows in block `m` is

`E_m = sum_{j=2}^{m+1} h_2(sin^2(pi/2^j))`.

The row `a=2^{w-m-1}` attains it. For every `m`,

`E_m < 1151/576 < 2`.

The sequence increases to a finite limit. A floating calculation of that limit gives approximately `1.9470770706125926` bits; the exact theorem is the series expression and the rational bound, not the decimal.

**Proof of the minimum formula.** The entropy of a product of independent Bernoulli variables is the sum of their individual entropies. For odd `d`, each `p_j(d)` lies between `sin^2(pi/2^j)` and `cos^2(pi/2^j)`. The entropy function is symmetric around `1/2` and strictly increasing on `(0,1/2)`, since its derivative there is `log_2((1-p)/p)>0`. Its minimum on that interval of probabilities is attained at an endpoint. The odd part `d=1` attains the endpoint simultaneously for every `j`. Summing proves the formula.

**Proof of the rational bound.** The case `E_0=0` is immediate. For `m>=1`, the first summand (`j=2`) is one. For `j>=3`, put `p_j=sin^2(pi/2^j)` and `q_j=10/4^j`. The inequalities `sin t<t` for positive `t` and `pi^2<10` give `p_j<q_j<1`. For `0<p<1`,

`h_2(p) <= p log_2(e/p)`.

Indeed `-(1-p)ln(1-p)<=p`; the difference has derivative `-ln(1-p)>=0` and vanishes at zero. The function `p log_2(e/p)` is increasing for `p<1`. Hence

`sum_{j=3}^infty h_2(p_j) < 10 sum_{j=3}^infty 4^{-j}(log_2(e/10)+2j)`.

The two geometric sums are `sum_{j>=3}4^{-j}=1/48` and `sum_{j>=3}j4^{-j}=5/72`. Therefore

`E_m < 43/18+(5/24)log_2(e/10)`.

For an entirely rational comparison, the exponential series through degree six and a geometric upper bound on its tail give

`e < 1957/720+1/4410 = 31967/11760 < 68/25`.

Furthermore,

`125^8 = 59604644775390625 > 58516894675632128 = 2^15 * 34^8`.

It follows that `e/10 < 34/125 < 2^{-15/8}`. Substitution yields

`E_m < 43/18 - 25/64 = 1151/576 < 2`.

For completeness, the bound on `pi` used above follows from the positive integral

`0 < integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7-pi`.

Polynomial division gives the stated integral directly; `(22/7)^2<10`. Every summand of `E_m` is positive, and the convergent dominating series just used proves convergence. ∎

**Corollary 7.3 (a strong obstruction to width-linear uncertainty).** Even when the vector is restricted to the largest paired Fourier block, no lower bound `H_cyclic(f)+H_XOR(f) >= c w` with fixed `c>0` can hold for all widths and all unit vectors in that block.

**Proof.** Choose `f(x)=P^{-1/2}exp(2 pi i x/P)`, the cyclic character of frequency one. Its cyclic coefficient entropy is zero; its Walsh coefficient entropy is `E_{w-1}<2`. It belongs to the largest paired block because frequency one has valuation zero. For `w>2/c`, the proposed inequality fails. ∎

This is an exact family of counterexamples within the largest block. It is stronger than retaining a fixed two-bit quotient state, and it does not rely on a conjectured uncertainty inequality or on numerical evidence.

### 8. Deterministic correlation cannot decay indefinitely

For any permutation `T` of `X_w`, define

`c(T) = max_{a!=0,b!=0} |P^{-1} sum_x omega^{a T(x)} psi_b(x)|`.

**Theorem 8.1.** For every `w>=1` and every permutation `T`,

`c(T) >= 1/sqrt(P-1)`.

**Proof.** The functions `P^{-1/2}omega^{aT(x)}` form an orthonormal basis because `T` permutes the summation points. The normalized Walsh functions form another orthonormal basis. Their overlap matrix is unitary. Its constant row and column have entry one at their intersection and zero elsewhere. Thus, for each nonzero row index `a`, the sum of squared magnitudes in the `P-1` nonzero columns is one. At least one entry has squared magnitude at least `1/(P-1)`. ∎

Consequently, at fixed width there cannot be constants `C<infinity` and `gamma>0` satisfying `c(T_L)<=C exp(-gamma L)` for all `L`, regardless of the deterministic schedule of additions and rotations. The bound is an obstruction to indefinite decay; it does not exclude decay toward a nonzero floor over a finite range.

**Theorem 8.2 (explicit recurrence and zero-addition counterexamples).** If all addition constants are zero, so `T_L=rho^L`, then `c(T_L)=1` for every `L`. If a fixed permutation step `F` is repeated, then `c(F^L)=1` at every positive multiple of the finite order of `F`.

**Proof.** For a digit permutation, the least significant output digit is one of the input digits. Taking `a=h` and taking `b` to be that input digit's mask makes `omega^{aT_L(x)}` equal the corresponding Walsh character pointwise. Hence the absolute overlap is one. For the second assertion, every finite permutation has finite order, equal to the least common multiple of its cycle lengths. At multiples of this order the permutation is identity, whose parity character has overlap one. ∎

These results disprove the literal indefinite-decay reading of inquiry 04's Q4.4. They do not answer an alternative question about random additions, averages of transition operators, ranges of `L` growing with `w`, or decay only down to a width-dependent floor. Any such target needs its random model, averaging convention, and quantifiers stated separately. No probabilistic conclusion is imported from the deterministic argument.

### 9. The support relation is not uniformly automatic in the original coordinates

This section independently audits the root agent's proposed sharp definability boundary.

Let `S(P,a,b)` mean: `P=2^w` with `w>=1`, `0<=a,b<P`, and `M_w[a,b]!=0`. Represent all number tracks by synchronized binary digits in least-significant-digit-first order; arbitrary high zero padding is permitted, and a canonical word has no final all-zero column.

**Theorem 9.1.** The ternary relation `S` is not definable in first-order Büchi arithmetic in the original integer coordinates `(P,a,b)`.

**Proof.** Every relation definable in this arithmetic has a regular synchronized representation. For the required direction, one can use the finite carry automata for addition, finite comparison automata, and the finite patterns for the valuation relation; Boolean operations and projection preserve regularity, with high-zero padding handling witnesses of different lengths. Restrict a hypothetical recognizer for `S` to the regular condition `a=b=t`, where `t` is a positive power of two. Write `t=2^n`. The support theorem gives

`n = w-1-n`,

so the restricted relation is exactly `P=2^{2n+1}=2t^2`.

Order the tracks as `(t,t,P)` and put `Z=(0,0,0)`, `A=(1,1,0)`, `B=(0,0,1)`. Its canonical language would be

`{Z^n A Z^n B : n>=0}`.

This is not regular. If a finite automaton had pumping length `p`, apply the pumping lemma to `Z^p A Z^p B`. Every permitted nonempty pumped segment within the first `p` letters consists only of initial `Z`s. Removing it changes the initial block length but preserves the middle block length, producing a word outside the language. This is a contradiction. ∎

The argument excludes the zero Fourier row and zero Walsh mask by using positive powers throughout. It is unaffected by the sign in the Fourier exponent. At `n=0`, the word is `AB`, corresponding to `(t,t,P)=(1,1,2)`, so there is no endpoint exception. This is a uniform nondefinability result; each fixed-width relation is finite and definable.

#### A reversed-coordinate repair, and its exact limitation

For `0<=b<P`, let `r=Rev_w(b)` be the number obtained by reversing exactly `w` binary digits, including zeros within that fixed word. For `b!=0`,

`v_2(r)=w-1-msb(b)`.

Hence the support condition in coordinates `(P,a,r)` is exactly

`Pow2(P) and P>=2 and a<P and r<P and`

`[(a=0 and r=0) or (a>0 and r>0 and V2(a)=V2(r))]`.

This uses the unary convention `V2(0)=0`, but the positive branch deliberately excludes zero. In the binary-relation convention of the handoff, replace the equality of valuations by

`exists d (V2(d,a) and V2(d,r))`.

Both positive inputs make the formula independent of any unspecified valuation-at-zero convention. The resulting support relation in the new coordinates is existential Büchi definable.

The coordinate conversion is not an automatic operation uniformly in `P`: if its graph were regular, restricting to `b=r=2^n` would again impose `w=2n+1` and would produce the same nonregular language `Z^n A Z^n B`. Thus this formula is useful when reversed masks are the chosen native coordinates. It does not express the original support predicate in the original integer encoding, and it cannot be composed with an automatic reversal that does not exist.

### 10. Uniform encodings supported by the algebra

The natural word-bound parameter is `P`, a positive power of two, not an exponent variable `w` with an assumed definable function `2^w`.

For example, the uniform top-toggle relation is expressed using only addition, order, and the power-of-two condition:

`Pow2(P) and P>=2 and exists h (`

`P=h+h and x<P and y<P and`

`[(x<h and y=x+h) or (h<=x and x=y+h)])`.

Parity is definable by `x=q+q` or `x=q+q+1`. The uniform common automorphism `U` is identity on even words and top-toggle on odd words, with `P>=4`. The 16 affine maps can be represented as compositions of the following constant-size list of primitives: the identity or `U`; optional bitwise complement; and a translation by one of `0,P/4,P/2,3P/4`. Complement is described by `x+y+1=P`, and the divisions by two and four use addition equations. Therefore these selected families do not require variable multiplication or variable digit shifts.

By contrast, Section 9 shows that even the Boolean assertion “this Fourier coefficient is nonzero” is outside the uniform original-coordinate Büchi fragment. The failure is more specific than merely observing that complex amplitudes or entropy are not native arithmetic terms.

### 11. Computation record and audit boundaries

`verification/algebra/algebra_check.py` is a standard-library Python program with a 45-second wall-clock alarm and deterministic exhaustive generators. It ran successfully and wrote the full machine-readable output `verification/algebra/algebra_check_output.json`. The script records its source SHA-256, Python version, platform, resource bound, observed runtime, ranges, all accepted affine parameter pairs, and per-width results. Its observed runtime was below one second in this environment. All assertions passed.

| Check | Exhaustive range | Kind of observation |
|---|---|---|
| Carry truth table | All 8 Boolean triples | Exact integers |
| Common translations and endomorphisms | Widths 1 through 8 | Exact maps tested on all words |
| Common affine permutations | Widths 1 through 7; 10,922 `(w,a,b)` candidates | Exact maps tested against affine reconstruction |
| Shared characters | Widths 1 through 7 | Exact congruence of exponents |
| Fourier support | Widths 1 through 6 | Exact cyclotomic polynomial reduction |
| Block maxima and minimum row entropy | Widths 1 through 6 | Direct numerical Fourier sums, separately labeled floating evidence |
| Entropy rational bound | Displayed exact rational and integer comparisons | Exact integers and fractions |
| Repeated addition-rotation step orders | Widths 1 through 7; every constant | Exact permutation cycle decompositions |

The exact support test reduces the Fourier polynomial modulo `X^{P/2}+1`. This polynomial is irreducible: after substituting `X+1`, every nonleading coefficient is divisible by two, and the constant coefficient is two and not divisible by four. The coefficient parity follows from `(X+1)^{2^k}=X^{2^k}+1` over the field with two elements. Eisenstein's criterion therefore applies. Consequently, a reduced polynomial of degree less than `P/2` vanishes at a primitive `P`th root exactly when every coefficient is zero.

The numerical Fourier checks use tolerances `1e-11` for coefficients and normalization and `1e-10` for entropy. They neither establish nor replace the exact theorems. The entropy decimal is a floating sum of terms `j=2,...,99`; the rigorous bound in Theorem 7.2 does not depend on it.

The proof dependencies are explicit above. The source packet's finite-width uniqueness evidence has been replaced by a uniform proof only for the precisely stated map classes in Sections 3 through 5. The missing original map specification remains missing. The ten catalogue targets remain outside the exact scope of this algebraic work.


## Part IV Restricted results for the foundations questions

Date: 2026-10-07. Assigned questions: Q1375–Q1378, Q1481, Q1979.

No assigned question is closed at its complete retained scope. The results below are **partial** for those questions. They consist of independent written arguments, explicit deductions from identified published results, and the finite computations recorded in `verification/foundations/check_output.json`. There is no compiled formal theorem. Elementary observations are not claimed as new literature discoveries.

### Source comparison and exact ledger map

| Q | Stable statement ID | Exact retained statement | Disposition and evidence |
|---|---|---|---|
| Q1375 | `3c545d79b70573f46278` | For each fixed k≥1, what is the exact decision complexity of BA_p sentences with k quantifier alternations? | **partial**: conservative automata bound and normalization obstruction below; original complexity gap remains. Primary-source comparison + written argument. |
| Q1376 | `7017180285bacc39c17f` | Given regular L⊆Σ*, is it decidable whether [L] is definable by an existential BA_p formula? | **partial**: affirmative semidecision, complete decisions on two growth classes, explicit limitation. Written argument + published dependency + finite computation. |
| Q1377 | `f8506c29d8d1507a5f50` | Is BA_k finitely axiomatizable? | **partial**: no axiomatization solely by universal sentences, even allowing infinitely many; finite axiomatization with unrestricted quantifiers remains unresolved. Written argument + primary-source comparison. |
| Q1378 | `d1962d78132eb0c2aaac` | Does BA_k have an expansion by finitely many definable functions or predicates whose theory eliminates quantifiers? | **partial**: impossible when predicates have existential definitions for both signs and functions have existential graphs. Unrestricted definable expansion remains unresolved. Written argument + published dependency. |
| Q1481 | `8d48b234d27dbcb91ed7` | Is it decidable, given finite automata for regular L₁,L₂⊆Σ*, whether [L₁] is existentially definable in (N,0,1,+,[L₂],≤)? | **partial**: affirmative semidecision; complete decision when [L₂] is ultimately periodic; positive answer whenever [L₁] is ultimately periodic. Written argument. |
| Q1979 | `11f085365348dc8d4680` | For every definable S in every model of Presburger arithmetic, is π_S(t) asymptotic to a polynomial? | **partial**: exact interval formulas, residue-class product formulas with leading constants, and computability of individual shatter values. Arbitrary definable families remain unresolved. Written argument + finite computation. |

#### Primary sources actually inspected

The following summaries are deliberately short; theorem pointers identify the dependencies without reproducing papers.

1. **Haase–Starčak, DLT 2025 survey**, pp. 5, 7, 9, DOI `10.1007/978-3-032-01475-7_1`. [Oxford source](https://ora.ox.ac.uk/objects/uuid%3A3b864e1a-847b-4275-b173-fe33960e3571/files/scn69m6569). Direct retrieval failed with 403, but search-indexed text of pp. 5 and 7 and indexed evidence from p. 9 were obtained. Open Problems 3 and 5 are retained. The survey states overall TOWER completeness, existential NP completeness, and the bounded-alternation gap. Its Theorem 3 records Starchak's unary characterization; the existence of finite expression parameters does not provide a decision bound on those parameters. Open Problem 6 appears on p. 9; its exact wording is supplied by the handoff rather than reverified from a full page.
2. **Haase–Różycki, On the Expressiveness of Büchi Arithmetic**, FoSSaCS 2021, pp. 310–323; [author PDF](https://www.cs.ox.ac.uk/people/christoph.haase/home/publication/hr-21/hr-21.pdf), 14 pages, successfully read. Theorem 1 (PDF p. 5) gives strict existential inexpressiveness. Corollary 1 (PDF p. 9) supplies the growth gap: a unary existentially definable set has either polynomial digit-length counts or counts at least c pⁿ infinitely often. Theorem 2 (PDF pp. 9–10) gives Σ₂ expressive completeness. Theorem 3 (PDF p. 10) covers regular polynomial growth. The specific nonexistential example is [{01,10}*].
3. **Guépin–Haase–Worrell, On the Existential Theories of Büchi Arithmetic and Linear p-adic Fields**, LICS 2019, [author PDF](https://www.cs.ox.ac.uk/people/christoph.haase/home/publication/ghw-19/ghw-19.pdf), Theorem 1, PDF p. 2. Existential satisfiability is NP-complete, including a binary-encoded base. Their valuation is formally a binary relation with no value at zero. Their introduction explains why NP does not imply polynomial binary-length numerical witnesses.
4. **Starchak, Existential Definability of Unary Predicates in Büchi Arithmetic**, CiE 2024, pp. 218–232, [publisher page](https://link.springer.com/chapter/10.1007/978-3-031-64309-5_18). Abstract and appendices visible; the complete chapter was not obtained. The abstract characterizes existential sets by finite unions and concatenations of word singletons, word stars, and fixed length/congruence languages. No recognition algorithm follows merely from this statement.
5. **Kovalyov, A natural axiomatization of Büchi Arithmetic**, [arXiv:2605.28408v1](https://arxiv.org/html/2605.28408v1), dated 27 May 2026, full HTML inspected. Theorem 3.1 proves completeness of its bounded-comprehension axiomatization; Question 1(1) and (4), corresponding to printed p. 13 in the handoff, retain finite axiomatizability and finite definitional QE. Its “Π₁” convention permits bounded quantifiers in the matrix; it does not mean a universal sentence with quantifier-free matrix. Its valuation is a total unary function with V_k(0)=0.
6. **Nieuwveld, On existential Büchi arithmetic in two coprime bases**, [arXiv:2608.24410v1](https://arxiv.org/html/2608.24410v1), dated 25 August 2026, Theorem 2. The stated result is decidability of the existential theory over Z with two coprime-base valuations. This is a **scope-nonmatch** for exact Q1375, Q1376 and Q1481.
7. **Eleftheriou–Papadopoulos, On the global linear Zarankiewicz problem**, [unversioned primary PDF](https://arxiv.org/pdf/2510.03546), 71 pages, successfully read. Question 9.3 is still present at printed p. 60/PDF p. 60. Explicit v2 URLs failed; the retrieved unversioned PDF's version/date was not independently established. Thus this confirms the retained wording in the retrieved document, not a complete latest-version search.
8. **Basit–Tran, On the shatter function of semilinear set systems**, [arXiv:2501.10032v1](https://arxiv.org/html/2501.10032v1), Theorem 1.1. The real semilinear result explicitly says π(t)=Θ(tˢ) for integer s. This is **scope-nonmatch** for all Presburger models. It also warns about terminology: “asymptotic to a polynomial” here denotes Θ behavior, not necessarily π(t)/P(t)→1. Q1979's wording must not silently be strengthened. The special cases proved below satisfy the stronger ratio conclusion.

Relevant web reference IDs for the parent to reopen if needed: `turn19search12` (survey p. 5), `turn25search17` (survey p. 7), `turn23search28` (survey p. 9), `turn5view3` (Haase–Różycki), `turn23view0` (Guépin–Haase–Worrell), `turn19view0` (Starchak), `turn5view0` (Kovalyov), `turn5view2` (Nieuwveld), `turn17view2` (Zarankiewicz PDF), `turn25view1` (Basit–Tran). Failed links are not evidence of nonexistent papers or of open status.

### 1. Q1376 and Q1481: uniform affirmative semidecision

Fix a base p≥2, canonical most-significant-digit-first representations, and finite automata A₁,A₂. Write R_i=[L(A_i)]. Arbitrary source languages can first be normalized: take the left quotient by 0*, intersect with nonzero canonical words, and add the word 0 precisely when any all-zero word, including the empty word if admitted, represents an accepted zero. This is an effective regular-language operation.

**Proposition 1.** The positive instances of Q1481 form a recursively enumerable set, uniformly in A₁,A₂. The same holds for Q1376.

**Proof.** Enumerate all existential formulas φ(x) in the finite language (0,1,+,≤,R₂). A synchronous automaton for every atomic formula is effectively available; R₂ atoms use the supplied automaton, with linear terms handled by addition relations and projection. Boolean operations and projection compile the complete candidate into an automaton B_φ. Compare its canonical language with A₁ by symmetric difference and emptiness. If they agree, output YES and φ. Every check terminates, and every existential definition eventually appears. There is no specified termination on negative instances. Replace R₂ by the fixed base-p valuation relation for Q1376. ∎

This is a genuinely uniform mathematical semialgorithm, not a claim that an unbounded formula enumeration was executed. It separates “no definition found within a budget” from a negative certificate.

#### Ultimately periodic relative predicates

A unary set R is ultimately periodic if there exist T≥0 and d>0 with R(n)↔R(n+d) for all n≥T. The standard unary Presburger characterization follows from Presburger elimination into linear inequalities and fixed-modulus congruences: beyond all finitely many endpoints, only finitely many periodic congruence conditions remain. Conversely, a finite initial segment plus periodic tails is a finite union of singletons and arithmetic progressions and therefore has an existential Presburger definition.

**Proposition 2.** If R₂ is ultimately periodic, then R₁ has an existential definition in (N,0,1,+,≤,R₂) if and only if R₁ is ultimately periodic. This restricted case of Q1481 is decidable from automata. If R₁ is ultimately periodic, the answer is YES for every R₂.

**Proof.** Expand every R₂ atom using its Presburger definition. Every set first-order definable in that expansion is Presburger definable, so a unary one is ultimately periodic. The converse uses the existential definition just described. To decide ultimate periodicity of a supplied automatic R, decide the Büchi sentence

    ∃T ∃d (d>0 ∧ ∀n (n≥T → (R(n) ↔ R(n+d)))).

This sentence is legal because d multiplies no variable. On YES, enumerate T,d and verify the tail condition to obtain a concrete periodic presentation. For a residue represented by c≥T, a progression uses ∃z(x=c+dz), where the selected d is now a numeral, so dz is repeated addition by a fixed coefficient. ∎

No execution of a general BA or Presburger solver is claimed for this proposition.

### 2. Q1376: an exact SCC triage algorithm

Use a complete deterministic automaton for canonical base-p words. Delete unreachable and non-coaccessible states. A useful strongly connected component (SCC) is **cyclic** if it contains a directed cycle. Count outgoing edges with label multiplicity; two labels going to the same state count twice.

**Proposition 3.** The following procedure is sound.

* If every cyclic useful SCC is a directed simple cycle with exactly one internal outgoing edge at each vertex, answer YES.
* If some cyclic useful SCC is not such a cycle, and no useful SCC has all p outgoing edges of every vertex internal, answer NO.
* Otherwise return UNKNOWN.

**Polynomial case.** Every successful run follows one of finitely many paths through the SCC condensation DAG. Within a simple-cycle component the only unbounded choice is the number of complete repetitions. Splitting according to entry/exit vertices gives a finite union of expressions u₀v₁*u₁⋯v_r*u_r. The number of words of length n is polynomially bounded.

There is also a direct existential construction for each expression, so this positive result need not be treated solely as an imported theorem. Let P_p(h) say h is a positive p-power. For a nonempty fixed word v of length ℓ and numerical value a, put

    Step_ℓ(h,H) := P_p(h) ∧ P_p(H) ∧ ∃d(H=h+(p^ℓ−1)d).

For powers H≥h, this holds exactly when H/h=p^(ℓj) for j≥0. Indeed gcd(p,p^ℓ−1)=1, and the multiplicative order of p modulo p^ℓ−1 is ℓ; the exceptional modulus 1 when p=2,ℓ=1 gives the same statement directly. The positioned block vʲ, with h the power below its least significant digit, contributes z characterized by

    (p^ℓ−1)z + a h = a H.

All coefficients are constants. A fixed word u of length e and value b instead imposes H=pᵉh and z=b h. Chain these equations from right to left with final lower boundary h=1, and require x to equal the sum of the block contributions. Existentially quantify all boundaries and contributions. This defines exactly the numerical values of the expression, including leading zeros and empty repetitions. Finite union preserves existential definability.

**Intermediate-growth case.** In a nonsimple cyclic SCC some state has two distinct internal outgoing labels. Complete each edge to a return word u,v at that state. If their lengths are a,b, the two return words uᵇ,vᵃ have equal length ab and different initial labels. Their free concatenations give 2ʲ accepted extensions at a linearly spaced sequence of lengths. Thus growth is not polynomial.

Let N be the number of useful states. In any SCC that is not closed under all p letters, every state has a path of length at most N−1 to a vertex with an outgoing letter leaving that SCC. Consequently at most pᴺ−1 words of length N remain wholly inside that SCC. The number of internal words of length n is at most Cγⁿ, where γ=(pᴺ−1)^(1/N)<p. An accepting run visits at most N SCCs, so partitioning its length among them introduces only a polynomial factor: d(n)≤C'nᴺγⁿ=o(pⁿ). Haase–Różycki's growth gap now excludes an existential definition. ∎

#### The UNKNOWN branch cannot be relabeled YES

Let K be the numbers represented by {01,10}*, with the empty word representing 0. Its canonical binary language is

    {0} ∪ (1|10)(01|10)*.

For n≥2 its count at length n is 2^floor((n−1)/2), and at length 1 the count is 2. Hence K has intermediate exponential growth and is not existentially BA₂ definable.

Define M={2n:n≥0} ∪ {2n+1:n∈K}. This is regular and has full binary growth because it contains every even number. Nevertheless,

    n∈K ⇔ 2n+1∈M.

If M were existentially definable, substituting the arithmetic term 2n+1 would give an existential definition of K. Thus M is not existentially definable. Its DFA reaches the UNKNOWN branch. This supplies an exact negative example hidden by a full-growth component and motivates applying the growth test also to affine preimages; it does not make that stronger heuristic complete.

**Executed artifact.** `verification/foundations/foundations_check.py` built complete unminimized DFAs with 3, 9, and 12 states for powers of two, K, and M. All use alphabet {0,1}, MSDF canonical finite words, zero represented by 0, terminal-state acceptance. `verification/foundations/automata.json` contains all states and transitions; `verification/foundations/check_output.json` records useful SCCs, internal degrees, counts for lengths 1–24, the three decisions, and the affine identity for n=0,…,4095. These finite checks sanity-check the constructions; the written arguments above prove their uniform properties.

### 3. Q1378: a restriction every QE proposal must escape

**Proposition 4.** No definitional expansion of BA_p has quantifier elimination if every added predicate and its complement have existential BA_p definitions and every added total function has an existential BA_p graph. This includes finite expansions satisfying these restrictions; it actually holds without a finiteness restriction on the vocabulary.

**Proof.** Take a quantifier-free formula in the expanded language, push negations to atoms, and introduce existential variables for every value of every function subterm. Conjoin the existential graph definitions. Because the graphs describe total functions with unique outputs, this replacement is correct even when the final atomic assertion is negative. Replace each positive predicate literal by its existential definition and each negative one by the existential definition of its complement. Original base-language literals remain quantifier-free. Conjunction and disjunction of existential formulas are existential after fresh variables are chosen. Thus every expanded quantifier-free formula translates to an existential formula in the original language.

If the expanded theory eliminated quantifiers, apply it to each original formula and then perform this translation. Every BA_p-definable set would be existentially definable, contradicting K above (or the general-base strictness theorem of Haase–Różycki). The zero convention is preserved by explicitly including (x=0∧y=0) in the graph when passing from a partial valuation relation to a total unary valuation. ∎

This does not rule out predicates with nonexistential complements or total functions whose graphs are not existentially definable. Those possibilities are permitted by exact Q1378. A “finite collection of convenient existential macros” is therefore insufficient when its negative literals remain existential too.

### 4. Q1377: universal axioms cannot suffice

Here the language is exactly (0,S,+,V_k,≤), with V_k total and V_k(0)=0.

**Proposition 5.** BA_k has no axiomatization consisting solely of universally quantified quantifier-free sentences, even an infinite one.

**Proof.** By compactness choose an elementary extension M of standard BA_k with a positive k-power α exceeding every standard natural number. Let

    H={nα+m : n,m∈N standard} ⊆ M.

It contains 0, is closed under successor and addition, and has the induced order. It is also closed under V_k. If n>0,m=0, then V_k(nα)=V_k(n)α. If m>0, choose the standard r with V_k(m)=kʳ. Since α is an arbitrarily large k-power, nα is divisible by k^(r+1), so V_k(nα+m)=kʳ. The n=0 and zero cases are immediate. These identities are elementary transfers of true fixed-n,m assertions in the standard structure.

Thus H is a substructure of M. But H fails the Presburger division sentence

    ∀x ∃y (x=y+y ∨ x=y+y+1)

at x=α. For y=nα+m, n=0 gives a finite right side, while n≥1 gives a right side at least 2α. Hence H is not a BA_k model. Every universal sentence true in M is inherited by H, proving the claim. ∎

Kovalyov's complete Π₁ axiomatization does not contradict this proposition: its matrix allows bounded existential quantifiers. This result does not answer finite axiomatizability by sentences of arbitrary quantifier form.

### 5. Q1375: sound bounds and the cost of normalization

“k alternations” can mean k switches or k blocks; these differ by one. The retained question should preserve that ambiguity until a chosen convention is fixed. The existential fragment has one block and zero switches.

For an explicit conservative bound, use the relational valuation language, fixed p, and formula length n including coefficient encodings. A quantifier-free matrix has a deterministic synchronous automaton with at most 2^poly(n) states: constant-arity primitive machines combine by products, and carries for linear expressions range over exponentially bounded intervals. Consecutive quantifiers of the same type can be projected as a whole block. If N states are available before a block, projection followed by determinization uses at most 2^N states; universal projection uses complement, projection, determinization, and complement, with the same bound. Thus r prenex blocks admit a direct deterministic upper bound exp_(r+1)(poly(n)), where exp₀(x)=x and exp_(j+1)(x)=2^exp_j(x). Padding closure and witness extension must be included in the projection semantics. This bound is deliberately loose and is not an improved exact complexity theorem. The published NP existential bound is far better.

**Normalization obstruction.** There cannot be an elementary-time algorithm mapping every BA_p sentence to an equivalent Σ₂ BA_p sentence. Such an algorithm followed by the preceding fixed-block elementary decision procedure would make full BA_p elementary, contradicting its known nonelementary lower bound. This is a lower bound on an effective conversion procedure; it is not a lower bound on the shortest equivalent sentence (every true sentence is equivalent to 0=0). Expressive completeness of Σ₂ therefore supplies no cheap automatic normalization route.

### 6. Q1979: exact special cases in every Presburger model

Let M be any model of Th(Z,0,1,+,<). For r≥0 let S_r be all unions of at most r bounded closed intervals of M, with the empty union allowed. A family with exactly r endpoint pairs gives the same system because an empty interval is encoded by its left endpoint exceeding its right endpoint.

**Proposition 6.** For every t≥0,

    π_{S_r}(t)=f_r(t):=Σ_{j=0}^r binom(t+1,2j),

where binomial coefficients with lower argument greater than t+1 are zero. For r≥1, f_r(t)~t^(2r)/(2r)!.

**Proof.** Sort any t-element A as a₁<⋯<a_t. Traces of r intervals are precisely binary strings with at most r runs of 1s: an interval gives a consecutive block, and any chosen consecutive block is realized by [a_i,a_j]. A string with j runs corresponds bijectively to 2j distinct boundaries among the t+1 gaps before, between, and after its positions. Sum over j. This works for every A and every model; no saturation or Archimedean assumption is used. The highest binomial term has the asserted leading coefficient. ∎

Now fix a standard integer q≥1 and r_c≥1 for c=0,…,q−1. Let S_{q,r} consist of sets formed by independently choosing at most r_c intervals in residue class c modulo q, then taking the union over classes.

**Proposition 7.** Set d_c=2r_c and D=Σ_c d_c. Then

    π_{S_{q,r}}(t)=max_{t₀+⋯+t_{q−1}=t} ∏_c f_{r_c}(t_c)

and

    π_{S_{q,r}}(t) ~ C t^D,
    C=∏_c ((d_c/D)^d_c / d_c!).

If every r_c=r, C=q^(−2rq)/((2r)!)^q.

**Proof.** For A with t_c points in each residue class, independence of the endpoints makes the number of traces the product. Every allocation is realizable because each standard residue class is infinite in every Presburger model. Each factor is t_c^d_c/d_c!+O((t_c+1)^(d_c−1)); multiplying gives a uniform O((t+1)^(D−1)) remainder. The maximum of ∏α_c^d_c on the simplex α_c≥0,Σα_c=1 occurs at α_c=d_c/D, by weighted AM–GM or logarithmic differentiation. Choose integer allocations within a bounded distance of these proportions for the lower bound. The uniform upper remainder gives the matching upper bound. ∎

The endpoint choices must be independent. General Presburger formulas can couple different intervals, residues, coordinates and parameters, so Presburger cell decomposition by itself does not turn this proposition into an answer to Q1979.

**Proposition 8.** For a parameter-free Presburger formula φ(x;y), each individual value π_φ(t) is effectively computable and is the same in every Presburger model. The same holds for explicitly specified standard integer parameters.

**Proof.** For each s≤2ᵗ, express the existence of t distinct tuples a_i and s parameter tuples b_j giving pairwise distinct traces:

    ∃a₁…a_t ∃b₁…b_s [ distinct(a_i) ∧
      ∧_{j<k} ∨_{i≤t} (φ(a_i;b_j) XOR φ(a_i;b_k)) ].

Include any parameter-domain restriction in this formula. It is a Presburger sentence, so its truth is decidable and model independent by completeness. The largest successful s is π_φ(t). This is pointwise computability, not a finite criterion proving the entire asymptotic sequence. For nonstandard parameters the assertion depends on their complete type and no unconditional effective presentation is asserted. ∎

### Computation contract and reproducibility

Command actually run:

    python3 verification/foundations/foundations_check.py

Python 3.12.14; standard library only; no randomized steps; no seed; no external solver or proof assistant. The recorded runtime is about 0.134 seconds, measured internally and environment dependent. The bounded resource contract is: three small explicit automata; word counts through length 24; the affine pullback for 4096 inputs; all binary strings of lengths 0–12 for r=0,…,4 (65 interval-count cases); all allocations of t≤24 across two residue classes with r=1. Every assertion passed. `verification/foundations/automata.json` and `verification/foundations/check_output.json` are complete outputs, and the script supplies the generators and all inputs. No finite computation is used as a proof of an unbounded Q statement.


## Part V Other model-theoretic results

Date: 7 October 2026.

### Q246 — automatic predicates cannot be witnesses

Stable statement ID: `b4cba42238e08ad101bc`.

Retained question: Does some unary R⊆ℕ make (ℤ,<,+,R) NIP but non-distal?

**Status of exact question: unresolved here. Partial theorem:** for every integer k≥2 and every k-automatic unary predicate R⊆ℕ, if (ℤ,<,+,R) is NIP, then it is distal. Consequently an affirmative witness to Q246 cannot be automatic in any integer base.

#### Dependencies and source comparison

Tong's *Distality to and from Combinatorics* (September 2025 thesis), Problem 3.1.2, printed p.38 / PDF page 50, states the retained question. Theorem 3.4.8, printed p.80 / PDF page 92, proves distality for congruence-periodic sparse predicates; the introduction explicitly lists k^ℕ, k≥2, among its examples (printed p.2 / PDF page 14).

Bell, Block Gorman and Schulz, *A Dichotomy for k-automatic expansions of Presburger Arithmetic*, arXiv:2508.04851v2, 13 May 2026, Theorem 1.1 (p.2), proves that a nonperiodic unary k-automatic R either defines full Büchi arithmetic or is definable from the powers predicate. Their Fact 2.17 (p.7, citing Bès, Theorem 3.1) supplies the reverse definability of k^ℕ from every nonperiodic k-automatic R. Thus the second alternative is interdefinability, which is essential: arbitrary reducts of distal structures need not be distal.

Okura, *Distal Expansions of the Integers and the p-adic Fields*, arXiv:2603.19786v1, 20 March 2026, Definition 3.2 and Theorem 3.24, proves the larger almost-sparse case. Its introduction identifies the question settled as Tong's sparse-predicate question concerning removal of congruence periodicity. That result does not resolve Q246.

#### Explicit independence-property witness in Büchi arithmetic

Fix k≥2. Work on ℕ with addition, order and unary Vₖ, where Vₖ(0)=0 and Vₖ(x) is the largest power of k dividing positive x. Define Powₖ(p) by p>0∧Vₖ(p)=p. Define

δₖ(x;p) := Powₖ(p) ∧ ∃u∃v [x=u+v ∧ p≤v<2p ∧ (u=0 ∨ Vₖ(u)≥kp)].

Multiplication by the fixed constants 2 and k is repeated addition; the formula uses no multiplication of variables. If p=kⁱ, then u=0 or Vₖ(u)≥kp means that u is a multiple of k^{i+1}. The constraint p≤v<2p says exactly that the base-k digit of x at place i is 1. For any m≥1, take parameters pᵢ=kⁱ for 0≤i<m. For every S⊆{0,…,m−1}, the integer x_S=∑_{i∈S}kⁱ satisfies

δₖ(x_S;pᵢ) ⇔ i∈S.

This is one fixed formula with patterns of arbitrarily large size, proving IP. Equivalently the dual formula δₖ(y;x) has infinite VC dimension. The exponent notation occurs only in the external choice of parameters and witnesses, not as an arithmetic function in the formula.

For a binary valuation relation, define Powₖ(p):=p>0∧Vₖ(p,p), and replace Vₖ(u)≥kp by ∃q(Vₖ(q,u)∧q≥kp), with the separate u=0 clause retained. Thus the proof respects either source convention without assigning a positive valuation to zero.

#### Proof of the automatic obstruction

If R is eventually periodic, it is Presburger-definable, and the expansion is a definitional expansion of distal Presburger arithmetic. Otherwise apply the dichotomy and reverse definability above. If R defines Vₖ on ℕ, δₖ witnesses IP in the expansion and rules out NIP. In the remaining case (ℕ,+,R) is interdefinable with (ℕ,+,k^ℕ). Translating the definitions to ℤ by restricting quantified variables to the definable nonnegative part shows that (ℤ,<,+,R) and (ℤ,<,+,k^ℕ) are interdefinable. The latter is distal by Tong's theorem, hence so is the former.

The conclusion is an obstruction to an automatic search for Q246 witnesses. It is not an obstruction to using Büchi arithmetic as a decision procedure for unrelated arithmetic statements.

### Q2169 — removing the discrete factor when the quotient has a least Archimedean class

Stable statement ID: `c2fc98c1e0a3bc2fd1d8`.

Retained question: For every nonzero countable divisible ordered abelian group V, is DgSp(V)=DgSp(V×ℤ), with lexicographic order and distinguished 1=(0,1)?

**Status of exact question: unresolved here. Partial theorem:** the equality holds whenever the positive Archimedean classes of V have a least member. This includes every nonzero Archimedean V, every V of finite Archimedean rank, and every finite-dimensional ordered ℚ-vector space V. It also applies to the Archimedean W used in the Q2168 construction.

#### Degree and presentation conventions

The degree spectrum uses exact Turing degrees of atomic diagrams of copies on ℕ. During constructions it is convenient first to obtain a copy computable from an oracle X. For any infinite linearly ordered structure, such a copy can be relabelled to have degree exactly deg(X): for each pair of existing labels {2n,2n+1}, map the new pair to the old elements in increasing or decreasing order according to X(n). The transported atomic diagram is X-computable, and comparison of each new pair recovers X. This supplies exact degree, without silently replacing spectra by the set of degrees that merely compute copies.

#### Forward inclusion

A copy A of V with degree d gives the explicit product A×ℤ with lexicographic order, of degree exactly d. Its product diagram is d-computable, and the known slice A×{0} recovers the diagram of A. Therefore DgSp(V)⊆DgSp(V×ℤ), without additional assumptions.

#### The usual quotient and its effective obstacle

Let P≈V×ℤ be an arbitrary presentation. Let C=ℤ·1. The quotient P/C is V. The relation x∈C is c.e. in the atomic diagram of P, because its positive instances are found by enumerating x=m·1 for standard m∈ℤ. This alone does not decide whether x lies in C. Likewise x≡y modulo C is only c.e. by this argument. Enumerating one representative per equivalence class therefore need not be computable in that oracle. Using one Turing jump does decide the relation and yields a quotient copy.

Block v3, Propositions 5.1–5.2 (p.20) record the forward inclusion and the one-jump reverse inclusion; Question 6.4 (p.29) asks whether the jump can always be removed. The proof below removes it under a structural hypothesis.

#### Least-class proof

Assume that V has a positive element v_* such that every nonzero v∈V satisfies n|v|>v_* for some standard positive integer n. This is exactly existence of a least positive Archimedean class. In the given copy P choose a positive element a whose image under some isomorphism P≈V×ℤ has first coordinate v_*. The natural-number label of a is one finite parameter in the oracle program; finding a uniformly from all presentations is not asserted or needed for degree-spectrum inclusion.

For input x∈P, dovetail the following searches using the atomic diagram:

1. Search m∈ℤ for x=m·1.
2. Search n≥1 for n|x|>a.

If x∈C, search 1 succeeds and search 2 never succeeds, since a is larger than every standard integer. If x∉C, its V-coordinate is nonzero; by the least-class hypothesis some n makes the first coordinate of n|x| strictly greater than v_*, and search 2 succeeds. Search 1 cannot succeed. Therefore exactly one search halts, deciding C in the same oracle.

The equivalence relation E(x,y)⇔x−y∈C is now decidable. Select least natural-number representatives of its equivalence classes. This set of representatives is decidable, because a given label has only finitely many smaller labels to test. It is infinite because V≠0 is divisible. Addition and order on the representatives are computed from P, replacing sums by their representatives. For distinct cosets, order is independent of representatives because C is convex. The quotient is consequently computable from the atomic diagram of P and is isomorphic to V. The exact-degree relabelling above gives deg(P)∈DgSp(V), proving the reverse inclusion.

#### Why finite dimension is covered

Representatives of distinct positive Archimedean classes in an ordered ℚ-vector space are linearly independent: in any finite dependence the term in the greatest class dominates the sum of all smaller classes. A finite-dimensional space therefore has finitely many positive Archimedean classes, hence a least one.

#### Presentation-level criterion

The same argument works whenever the given copy P computes a sequence of positive elements a_j∉C such that, for every x∉C, some j,n satisfy n|x|>a_j. Such a sequence makes C decidable. Conversely, if C is decidable, the positive elements outside C can be effectively enumerated and provide such a sequence. This characterizes the extra information needed to compute this particular quotient presentation. It does not characterize degree-spectrum equality, since another computable presentation of V may exist even when this quotient is not computable.

### Q2170 — source status and scope

Stable statement ID: `86f031cac9140549efc3`.

Retained question: Does every countable non-automorphically-trivial structure have the same degree spectrum as some Presburger group?

**Status: unresolved.** Block v3 retains Question 6.5 on p.29. No universality proof or spectrum obstruction was obtained here. The Q2168 example and the Q2169 least-class theorem do not settle universality. In particular, Scott-sentence complexity and degree spectra are different invariants: realizing Σ₄ Scott complexity does not realize an arbitrary degree spectrum.

### Primary-source URLs and version record

- Tong thesis: https://etheses.whiterose.ac.uk/id/eprint/37811/1/Tong_HWM_Mathematics_PhD_2025.pdf . Title page: September 2025. Q246 at printed p.38 / PDF page 50; Theorem 3.4.8 at printed p.80 / PDF page 92.
- Bell–Block Gorman–Schulz: https://arxiv.org/abs/2508.04851 ; https://arxiv.org/html/2508.04851v2 ; https://arxiv.org/pdf/2508.04851 . Latest version displayed: v2, 13 May 2026. Theorem 1.1 at printed p.2; Fact 2.17 at p.7 gives reverse definability.
- Okura: https://arxiv.org/abs/2603.19786 ; https://arxiv.org/html/2603.19786v1 . Version v1, 20 March 2026; Definition 3.2 and Theorem 3.24.
- Block: https://arxiv.org/abs/2601.21118 ; https://arxiv.org/html/2601.21118v3 ; https://arxiv.org/pdf/2601.21118 . Latest version displayed: v3, 16 June 2026; Questions 6.1, 6.4, 6.5 on p.29. Initial direct versioned URLs returned fetch errors, but following the unversioned abstract's PDF/HTML links retrieved the full v3 source. Source presence and version were verified; failed initial retrieval was not interpreted as research status.
- Montalbán: https://math.berkeley.edu/~antonio/papers/scottRank.pdf . Author-hosted submitted draft saved/compiled 23 March 2014, Theorem 1.1, p.1; journal publication: *Proceedings of the American Mathematical Society* 143 (2015), 5427–5436, DOI 10.1090/proc/12669. The exact orbit theorem used in the Q2168 proof is present in both this primary draft and Block's Theorem 1.1.

### Evidence limits

These are written arguments and primary-source comparisons. No Lean/Coq kernel theorem was compiled, no atomic-diagram construction was run, and no finite computation is used as evidence for the infinite model-theoretic claims. The broad unresolved statuses distinguish failure to obtain a proof from a claim that a complete current literature survey has ruled out all later work.


## Part VI Executed verification and reproduction

### Certificate inventory

Each empty language below is a counterexample language. Its certificate supplies every state, every transition, the initial and accepting states, an inductive closed reachable-state set, and a SHA-256 identity recorded by the independent checker. “Empty” proves the corresponding assertion for all finite encodings; the written primitive invariants connect those encodings to the intended numerical statements. State counts describe these particular constructions, not minimum-state lower bounds.

| Counterexample or comparison | States | Transitions | Result |
|---|---:|---:|---|
| modadd_matches_presburger | 13 | 208 | Empty |
| addition_lowest_bit | 6 | 96 | Empty |
| xor_lowest_bit | 4 | 32 | Empty |
| top_bit_translation | 24 | 384 | Empty |
| addition_equals_xor_criterion | 64 | 2048 | Empty |
| common_translation_classification | 21 | 168 | Empty |
| existential_padding_control | 9 | 18 | Empty |
| odd_top_toggle_additive | 88 | 45056 | Empty |
| odd_top_toggle_xor_linear | 51 | 26112 | Empty |
| odd_top_toggle_involution | 15 | 480 | Empty |
| negative_all_addition_is_xor | 9 | 144 | Nonempty; P=4, x=3, y=1, z=0 |
| negative_all_translations_are_xor | 26 | 832 | Nonempty; P=4, a=3, b=3, x=1, z=0 |

The main run used Python 3.12.14 and took 0.504771 seconds, with peak resident memory 17,152 KiB. The largest intermediate construction had 88 states and 45,056 transitions. Limits were 100,000 states and 5,000,000 transitions per construction and a 60-second process timeout. The algebra and independent audit scripts each declare a 45-second alarm. No randomness or seed is involved. Runtime and memory are environment-dependent observations.

The first false universal assertion fails at P=4, x=3, y=1: modular addition gives zero, whereas XOR gives two. The second fails even with the two translation constants equal: P=4, a=b=3, x=1, z=0. Thus the negative controls test substantive false claims rather than only malformed inputs.

### Separate numerical controls

The main suite checks 4,680 input triples for addition and another 4,680 for XOR over widths 1–4, 1,024 valuation pairs, and 340 translation-parameter pairs. The independent audit checks 123,462 word-domain tuples, 123,462 modular-adder tuples, 4,096 valuation pairs, 6,809 odd-top-toggle tuples, and 606 projection observations. It also performs two further complete graph comparisons: existence of y=64x+17 is universal, and existence of an odd y=3x+5 is equivalent to x being even. The independent audit completed in 1.288805 seconds.

The algebra controls enumerate common translations and endomorphisms through width eight, all 10,922 cyclic-affine candidates through width seven, and shared characters through width seven. Exact cyclotomic support and separately labeled floating Fourier diagnostics run through width six. The entropy bound uses exact integer and rational arithmetic. The foundations controls construct the three explicit 3-, 9-, and 12-state DFAs, count words through length 24, check the affine pullback on 4,096 integers, verify 65 interval-count cases through t=12, and check residue allocations through t=24. These are bounded controls; the uniform conclusions depend on the written arguments.

The preserved raw outputs are verification/transcript.jsonl, verification/certificate_check.txt, verification/generated/run_summary.json, verification/algebra/algebra_check_output.json, verification/foundations/check_output.json, and verification/audit/audit_automata_output.json. Primitive graphs are exported both as JSON and in Walnut text format. The Walnut exports were not imported or executed by Walnut.

### Reproduction commands

From the extracted B1-research-2026-10-07 directory, Python 3.12 and the standard library suffice. These commands overwrite the generated outputs in that extracted directory, so use a working copy if preserving the recorded timing metadata matters.

~~~bash
python3 verification/check_certificates.py
timeout 60s python3 verification/run_verification.py > verification/transcript.jsonl
python3 verification/check_certificates.py > verification/certificate_check.txt
python3 verification/algebra/algebra_check.py
python3 verification/foundations/foundations_check.py
python3 verification/audit/audit_automata.py
~~~

The initial command validates the supplied certificates before regeneration. The script paths are portable. The timeout and resource facilities used by the scripts target the recorded Linux environment. The manifest covers the delivered files before a reproduction changes runtime metadata.

### Trust boundary

The independent graph checker does not import the automaton builder. It checks graph dimensions, total transition tables, target indices, hashes, exact reachability, and the empty/nonempty claims. This establishes finite-state closure using a much smaller program. It does not turn the Python implementation into a proof-assistant kernel. Correct mathematical interpretation still uses the written primitive semantics and formula-construction review. The two written audits are in notes/Q2168-independent-audit.md and notes/automata-audit.md.

## Part VII Remaining mathematical bottlenecks

- **Q246:** Existence or nonexistence of a nonautomatic unary R making the expansion NIP and non-distal.
- **Q1375:** Matching upper and lower bounds for each exact fixed-alternation fragment, under a fixed alternation convention and input language.
- **Q1376:** A terminating recognition algorithm or an undecidability proof for all regular unary predicates; full-growth cases remain outside the triage.
- **Q1377:** Finite axiomatizability with unrestricted quantifier form.
- **Q1378:** Finite definitional QE using arbitrary definable predicates or functions beyond the excluded existential restrictions.
- **Q1481:** General negative-instance termination or an undecidability theorem for arbitrary regular [L₂].
- **Q1979:** Polynomial asymptotics for arbitrary definable families in every Presburger model, with coupled parameters, residues, and coordinates.
- **Q2169:** Removing the jump for all quotient groups with no least nonzero Archimedean class, without additional presentation information.
- **Q2170:** The full degree-spectrum universality assertion.


The auxiliary inquiry about a complete Fourier tail distribution remains partial. The exact all-ones Walsh-column maximum in inverse Q4.3 remains unresolved; a maximum over the entire paired block does not answer a fixed-column maximum. For inverse Q4.4, the deterministic all-length decay-to-zero interpretation is disproved. A random model, a finite-length regime, or decay toward a nonzero floor would be a different statement with different quantifiers.

For automatic proof development, fixed circuits and the reversed-mask support predicate are legal targets. A uniform recognizer for the original Fourier support coordinates is ruled out by a mathematical nonregularity proof. Increasing automaton resources cannot repair that original representation. The exact bit-length, exponential, and popcount obstructions likewise rule out those specific uniform graphs; fixed-width instances and fixed-modulus statistics remain available.

The new Q2168 proof is the strongest candidate for direct formalization: its independent lemmas are partial-fraction uniqueness, the elementary-substructure family, scalar rigidity, infinitary Π₂ downward preservation, and the explicit Scott-sentence complexity calculation. Formalization would strengthen verification of this established written argument; no such compiled artifact is included in the present results.

## Source registry

The input handoff is preserved byte-for-byte in sources/B1-handoff-2026-10-07.md. Its SHA-256 is 3e5471ea384dfcfd8f84a3a3bfb7b51350cb1bae5984483acddaa23174916d8e. The machine-readable registry in sources/primary_sources.json records source versions, theorem locations, access limits that affect status claims, and scope exclusions. The short list below identifies the mathematical and software dependencies used above.

- **[Jason Block, Measuring the Complexity of Countable Presburger Models](https://arxiv.org/html/2601.21118v3)**. v3, 16 June 2026. Theorem 1.1, p.3; Propositions 5.1-5.2, p.20; Questions 6.1, 6.4, 6.5, p.29.
- **[Antonio Montalbán, A robuster Scott rank](https://math.berkeley.edu/~antonio/papers/scottRank.pdf)**. Author-hosted submitted draft saved/compiled 23 March 2014; journal publication 2015. Theorem 1.1, p.1.
- **[Ho Wang Mervyn Tong, Distality to and from Combinatorics](https://etheses.whiterose.ac.uk/id/eprint/37811/1/Tong_HWM_Mathematics_PhD_2025.pdf)**. September 2025 thesis. Problem 3.1.2, printed p.38 / PDF page 50; Theorem 3.4.8, printed p.80 / PDF page 92; Powers examples, printed p.2 / PDF page 14.
- **[Bell, Block Gorman and Schulz, A Dichotomy for k-automatic expansions of Presburger Arithmetic](https://arxiv.org/html/2508.04851v2)**. v2, 13 May 2026. Theorem 1.1, p.2; Fact 2.17, p.7.
- **[Okura, Distal Expansions of the Integers and the p-adic Fields](https://arxiv.org/html/2603.19786v1)**. v1, 20 March 2026. Definition 3.2; Theorem 3.24; Introduction: identification of Tong's separate sparse-predicate question.
- **[On the Expressiveness of Büchi Arithmetic](https://www.cs.ox.ac.uk/people/christoph.haase/home/publication/hr-21/hr-21.pdf)**. FoSSaCS 2021, author-hosted paper. Theorem 1, PDF p.5; Corollary 1, PDF p.9; Theorem 2, PDF pp.9–10; Theorem 3, PDF p.10.
- **[On the Existential Theories of Büchi Arithmetic and Linear p-adic Fields](https://www.cs.ox.ac.uk/people/christoph.haase/home/publication/ghw-19/ghw-19.pdf)**. LICS 2019, author-hosted paper. Theorem 1, PDF p.2.
- **[Formal languages and arithmetic theories: recent results and open problems](https://ora.ox.ac.uk/objects/uuid%3A3b864e1a-847b-4275-b173-fe33960e3571/files/scn69m6569)**. DLT 2025 survey. Open Problem 3, p.5; Open Problem 5, p.7; Open Problem 6, p.9, exact wording from supplied handoff.
- **[Existential Definability of Unary Predicates in Büchi Arithmetic](https://link.springer.com/chapter/10.1007/978-3-031-64309-5_18)**. CiE 2024, pp.218–232.
- **[A natural axiomatization of Büchi Arithmetic](https://arxiv.org/html/2605.28408v1)**. v1, 27 May 2026. Theorem 3.1; Question 1(1) and 1(4).
- **[On existential Büchi arithmetic in two coprime bases](https://arxiv.org/html/2608.24410v1)**. v1, 25 August 2026. Theorem 2.
- **[On the global linear Zarankiewicz problem](https://arxiv.org/pdf/2510.03546)**. Retrieved unversioned 71-page PDF; exact version/date not independently established. Question 9.3, p.60.
- **[On the shatter function of semilinear set systems](https://arxiv.org/html/2501.10032v1)**. v1, January 2025. Theorem 1.1.
- **[Walnut official repository and documentation](https://github.com/Walnut-Theorem-Prover/Walnut)**. README describes 8.0-alpha; changelog dates 7.1 to 2 December 2025. README; Changelog; https://github.com/Walnut-Theorem-Prover/Walnut/wiki/Walnut-file-format; https://github.com/Walnut-Theorem-Prover/Walnut/wiki/Command:def-or-eval.
- **[Self-Verifying Predicates in Büchi Arithmetic](https://arxiv.org/html/2507.19717v1)**. v1, 25 July 2025. Theorem 2; Section 4.2.
