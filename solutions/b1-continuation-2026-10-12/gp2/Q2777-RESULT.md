# Q2777: one-dimensional GP² spectra via disjoint-union profiles

2026-10-12. Full-question proof accepted after independent main-thread
syntax and mathematical review, recorded in Q2777-ROOT-REVIEW.md.
Q2777 attempt 1 succeeds, with no failed solve attempts.
No novelty or external-review claim. Q2778 is separately treated in
Q2778-ATTEMPTS.md.

**Claim.** For every GP² sentence φ, its finite-model size spectrum

    Spec(φ) = { |M| : M finite and M ⊨ φ }

is semilinear. More precisely, it is a finite union of additive subsemigroups of the positive integers, each of which is a finite union of arithmetic progressions.

## Exact question and syntax

The catalog question is Q2777 (`672a90c2a14e9a88363f`), “One-dimensional spectra of GP².” It asks whether Spec(φ) is semilinear for every GP² sentence, without requiring an algorithm or a bound for constructing a representation. Its source is Benedikt–Lu–Tan, *Analysis of Logics with Arithmetic*, [CSL 2026, Section 6, paragraph after Theorem 38](https://doi.org/10.4230/LIPIcs.CSL.2026.27). The local source is `../../../texts/papers/collections-2f5eb9092358afd8.txt.gz` relative to this directory.

The proof uses the paper's GP² syntax: unary and binary relation symbols, equality, Boolean connectives, ordinary quantification over unary formulas, and local Presburger quantifiers whose counted sets have positive binary guards R(x,y) or R(y,x). There are no constant or function symbols. The [full version, Sections 3 and 10](https://arxiv.org/html/2508.03574v2) confirms that the arithmetic counts are local and that unguarded unary existential quantification is allowed. The cited predecessor makes the guard restriction explicit: [Lu–Tan, LMCS 2024, Section 3, pages 16:5–16:6](https://lmcs.episciences.org/14106/pdf), where each counting guard is a binary relation atom and no constants are allowed. Ordinary guarded quantification can equivalently be written using a local count and unary existential quantification, and universal quantification using negation.

In particular, arbitrary global counts |U| or unguarded counting quantifiers ∃≥k x U(x) are **not** extra constructors in this argument. The source distinguishes global cardinality constraints from GP². Such an extra constructor would invalidate the preservation lemma, for example by expressing “exactly one P element.”

We use the usual nonempty-domain convention. Allowing an empty structure adds or removes only the possible size 0 and does not affect semilinearity. Self-loops may be retained: disjoint union preserves them, so the argument does not need a loop-free restriction. The proof also works if local modulus tests are admitted.

## 1. Finite closed-subformula profiles are preserved under disjoint union

Let C be the finite set of syntactically closed subformulas of φ, including φ. For any finite structure M, let

    τ_M = ( 1[M ⊨ ψ] : ψ ∈ C ).

If A and B have disjoint domains, their relational disjoint union D=A⊔B interprets every unary relation as its union and every binary relation as the union of its interpretations in the two summands. Thus no binary relation connects the summands.

**Lemma.** If τ_A=τ_B, then for every subformula θ of φ and every assignment of all its free variables to one summand, say A,

    D ⊨ θ[assignment]  ⇔  A ⊨ θ[assignment].

For a closed θ the assignment is empty, and the conclusion holds for both summands. Consequently τ_D=τ_A=τ_B.

**Proof.** Induct over subformula construction.

* Atomic formulas, including equality and diagonal binary atoms, are unchanged on a single summand.
* Boolean connectives follow from the induction hypothesis for their constituent subformulas. Any closed constituent uses the same empty assignment and is covered by the induction.
* Consider a local Presburger formula with retained variable x. Fix x=a in A. Each counted term has the form

      #y [ R(x,y) ∧ θ(x,y) ]

  or its reverse-guard counterpart. If y is in B, its positive binary guard is false. If y is in A, the induction hypothesis gives precisely the same truth value for θ as in A. Hence every counted cardinality is unchanged. Every integer linear comparison, and likewise any local congruence comparison, has unchanged truth value. Equality-guarded local counting, if allowed as a shorthand, has the same property since x=y forces y into A.
* The remaining constructor is unary existential quantification ψ=∃x θ(x), whose result is closed. By induction, θ has exactly its original satisfiers in each summand. Thus

      D ⊨ ψ ⇔ (A ⊨ ψ or B ⊨ ψ).

  Because ψ itself belongs to C and τ_A=τ_B, its two truth values agree. Their disjunction is therefore that common value. A quantified variable absent from θ is covered as well, because the summands and D are nonempty. Unary universal quantification follows either by the same argument or by negation.

These cover the stated syntax. For the usual guarded-fragment presentation, a closed existential binding both variables is also preserved: a positive binary or equality guard forces both witnesses into one summand; a unary guard can cover only a single distinct quantified variable. This agrees with its rewriting into the constructors already treated. ∎

The equal-profile premise is necessary. The sentence

    (∃x P(x) ∧ ¬∃x Q(x)) ∨ (¬∃x P(x) ∧ ∃x Q(x))

holds in a P-only one-element structure and a Q-only one-element structure, but fails in their union. They have different closed-subformula profiles. The proof does not claim that an arbitrary GP² sentence's entire model class is closed under disjoint union.

## 2. Each size set for a fixed profile is an additive semigroup

For a Boolean profile τ with τ(φ)=true, let

    S_τ = { |M| : M finite, τ_M=τ }.

If a,b∈S_τ, choose respective models A and B, rename their elements to make their domains disjoint, and take A⊔B. By the lemma, it has profile τ and size a+b. Thus S_τ is closed under addition. There are at most 2^|C| profiles and

    Spec(φ) = ⋃_{τ : τ(φ)=true} S_τ.

Unrealized profiles contribute the empty set.

## 3. An additive subsemigroup of positive integers is semilinear

Let S be a nonempty subset of N_{>0}, closed under addition. Let m=min S. For each residue r modulo m attained by an element of S, let a_r be the least element of S in that residue class. Then

    S = ⋃_{r attained} { a_r + km : k∈N }.

The right-hand side is contained in S because a_r,m∈S and addition is closed. Conversely, if s∈S has residue r, then s≥a_r and s−a_r is a nonnegative multiple of m, so s belongs to that progression. There are at most m progressions. The empty S is semilinear too. Applying this to each S_τ proves the claim. ∎

## Scope, effectiveness, and the other open question

This is an existence proof of semilinearity for the **total model size**, exactly the stated Q2777. It neither supplies computable bounds for m or the a_r nor explains how to determine which residues are attained. An abstract decidable membership test for a set closed under addition does not by itself provide a termination criterion for learning its eventual period and all residue minima.

No conclusion follows here about multivariate unary spectra or Q2778 (decidability after adding global linear cardinality constraints). Additive submonoids of N^k for k≥2 need not be semilinear. For example, the source's Section 6 realizes the vector set

    { (a,b) : b≤a(a−1) },

up to the two identically zero coordinates. It is closed under addition because a(a−1)+c(c−1)≤(a+c)(a+c−1), but is nonsemilinear. Its total-size projection contains every positive integer by taking b=0. Thus that multivariate counterexample is consistent with this proof and cannot refute Q2777.

## Reproducible finite controls

`check_profiles.py` independently evaluates nested guarded arithmetic formulas on small structures and disjoint unions, grouping summands by the actual truth values of all closed subformulas. It also checks the unequal-profile counterexample, the global-counting exclusion control, the source's quadratic vector set's additive closure, and explicit residue-minimum representations of finitely generated numerical semigroups. The finite tests are regression controls for the structural argument, not substitutes for the all-size proof. Receipt: `PROFILE-CHECK-RESULTS.json`.

Independent main-thread review accepts the local binary-guard syntax and the
all-size argument; see Q2777-ROOT-REVIEW.md. Adding global fixed-threshold
counting would require another argument.
