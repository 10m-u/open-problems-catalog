# Q3454: a quantitative result for commuting support projections

Date: 2026-10-09. Status: proved partial result; the unrestricted conjecture remains open in this report.

## Target and comparison with the primary source

Let $A$ be a complex unital Banach algebra with $\|1\|=1$. An element $e$ is hermitian if $\|\exp(ite)\|=1$ for all real $t$. A Moore–Penrose inverse $a^\dagger$ satisfies

$$
aa^\dagger a=a,\qquad a^\dagger aa^\dagger=a^\dagger,
$$

with both products $aa^\dagger$ and $a^\dagger a$ hermitian.

The question is whether $a_n\to a$, with all elements Moore–Penrose invertible and $\sup_n\|a_n^\dagger\|<\infty$, forces $a_n^\dagger\to a^\dagger$.

Primary source: Gardella–Palmstrøm–Thiel, [Rigidity of pseudofunction algebras of ample groupoids](https://arxiv.org/html/2506.09563v1), Conjecture 2.22. Their Theorem 2.23 assumes commuting ultrahermitian idempotents; Remark 2.24 discusses closure under multiplication. Their Theorem 2.25 covers unital $L^p$-operator algebras. The [arXiv record](https://arxiv.org/abs/2506.09563) listed only v1 when checked on 9 October 2026.

The proof here only requires two pairwise commutation relations for the given pair of elements. It does not assume ultrahermitian idempotents or that a product of hermitian idempotents is hermitian.

No prior exact-Q3454 solution was found under `solutions/` at commit `8967f4f70776856b3dfc0b2494ed73167b15ee0c`. A targeted literature search did not locate the quantitative statement below; no claim of priority follows from that search.

## Quantitative theorem

For a Moore–Penrose invertible element $x$, write

$$
p_x=x^\dagger x,\qquad q_x=xx^\dagger.
$$

Let $a,b\in A$ be Moore–Penrose invertible, and suppose

$$
p_ap_b=p_bp_a,\qquad q_aq_b=q_bq_a.
\tag{1}
$$

Put $M=\max(\|a^\dagger\|,\|b^\dagger\|)$. If

$$
M\|a-b\|<1,
\tag{2}
$$

then

$$
p_a=p_b,\qquad q_a=q_b,
\tag{3}
$$

and

$$
\|b^\dagger-a^\dagger\|
\leq\|b^\dagger\|\,\|a^\dagger\|\,\|a-b\|.
\tag{4}
$$

The case $M=0$ means $a=b=0$ and is immediate.

## Proof

If $e$ is a hermitian idempotent, then

$$
\exp(i\pi e)=1-2e,\qquad \|1-2e\|=1.
$$

Therefore

$$
\|e\|\leq1,\qquad\|1-e\|\leq1,
\tag{5}
$$

by writing each as half the sum or difference of $1$ and $1-2e$. Every nonzero idempotent $d$ in a normed algebra has $\|d\|\geq1$: the inequality $\|d\|=\|d^2\|\leq\|d\|^2$ proves it. The latter fact does not require hermitianness.

Since $a(1-p_a)=0$,

$$
p_b(1-p_a)=b^\dagger b(1-p_a)
=b^\dagger(b-a)(1-p_a).
$$

Equations (2) and (5) imply $\|p_b(1-p_a)\|<1$. Commutation in (1) makes $p_b(1-p_a)$ an idempotent. It must therefore be zero. Reversing $a,b$ shows $p_a(1-p_b)=0$. Thus

$$
p_b=p_bp_a=p_ap_b=p_a.
$$

For the other support projections, $(1-q_a)a=0$, so

$$
(1-q_a)q_b=(1-q_a)bb^\dagger
=(1-q_a)(b-a)b^\dagger.
$$

This also has norm less than 1 and is an idempotent by (1), hence is zero. Swapping $a,b$ again gives $q_a=q_b$, proving (3).

Use the common supports to calculate

$$
\begin{aligned}
b^\dagger(a-b)a^\dagger
&=b^\dagger aa^\dagger-b^\dagger ba^\dagger\\
&=b^\dagger q_a-p_ba^\dagger\\
&=b^\dagger q_b-p_aa^\dagger\\
&=b^\dagger-a^\dagger.
\end{aligned}
$$

Submultiplicativity proves (4). QED.

## Consequences

1. If all hermitian idempotents in $A$ commute, the answer to Q3454 is affirmative. For $a_n\to a$ and $M=\max(\|a^\dagger\|,\sup_n\|a_n^\dagger\|)<\infty$, equation (2) holds eventually. Formula (4) then gives convergence with an explicit bound.
2. Global commutativity is unnecessary. It is enough that, for all sufficiently large $n$, $a_n^\dagger a_n$ commutes with $a^\dagger a$, and $a_na_n^\dagger$ commutes with $aa^\dagger$. No cross-commutation or commutation between different indices is used.
3. On this locus, changing either support projection requires $\|a-b\|\geq1/M$. The threshold is sharp in the elementary algebra $\mathbb C$: take $a=0,b=c>0$, so $M=1/c$ and $M\|a-b\|=1$, while the supports differ.
4. If $a,b$ are MP partial isometries, their inverse norms are at most 1. Under (1), $\|a-b\|<1$ gives $\|a^\dagger-b^\dagger\|\leq\|a-b\|$.

## Scope and remaining gap

This removes an explicit hypothesis from the primary source's theorem and isolates a pairwise condition sufficient for a quantitative conclusion. It does not prove Q3454 in an arbitrary Banach algebra: when the two support projections do not commute, $p_b(1-p_a)$ need not be an idempotent, so its small norm does not force it to vanish.

The report does not establish a concrete Banach algebra separating the global class “all hermitian idempotents commute” from the source's commuting-ultrahermitian class. Thus the proven statement is a weaker-hypothesis theorem and proof simplification; strict enlargement of the known class of examples is not claimed. The local pairwise formulation is valid independently of that distinction.

The script `verify_results.py` includes exact rational matrix checks of the algebraic identities and a support-changing equality case. These checks are supplementary; the Banach-algebra argument is the proof.
