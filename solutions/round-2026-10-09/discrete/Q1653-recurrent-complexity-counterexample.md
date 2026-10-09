# Q1653: a counterexample to factorial-language complexity realization

Date: 2026-10-09. Complete counterexample to the stated conjecture, with a self-contained proof. This result has received an internal mathematical check but has not been peer reviewed. The literature search below does not establish historical priority.

## 1. Statement and primary-source conventions

Catalog Q1653 asks whether every factor-closed language $F\subseteq\{0,1\}^*$ with unbounded complexity $q_F(n)=|F\cap\{0,1\}^n|$ has the same complexity as the recurrent-factor language of some infinite binary sequence.

This is Ben Jarvis's Conjecture 6.36 in *Pin Classes*, printed p. 173. Definition 6.1, printed p. 158, requires closure under contiguous factors and imposes no extension condition. Definition 6.5(3), printed p. 159, specifies equality of the complexity values at every length, not eventual equality or equality of growth rates. Definitions 6.2 and 6.9 identify the relevant language with the factors occurring infinitely often in a one-sided infinite sequence. These distinctions are essential to the counterexample. [J]

**Theorem.** The language

$$
\boxed{F=\{0^i1^j:i,j\ge0\}\ \cup\ \{10\}}
$$

is factor closed and has unbounded complexity, but no infinite binary sequence has recurrent-factor complexity $q_F(n)$ for every $n$. In fact the contradiction already uses lengths 2, 3, and 4.

The empty word may be omitted if the language convention excludes it. Every assertion below concerns positive lengths and is unchanged.

## 2. The explicit language

Every contiguous factor of a word of the form $0^i1^j$ has that form. The only nonempty proper factors of $10$ are $1$ and $0$, which already belong to the first part of $F$. Thus $F$ is factor closed.

At each positive length $n$, the words $0^i1^{n-i}$, for $0\le i\le n$, are distinct and give exactly $n+1$ words in the first part of $F$. The additional word $10$ affects only length 2. Consequently

$$
q_F(n)=
\begin{cases}
2,&n=1,\\
4,&n=2,\\
n+1,&n\ge3.
\end{cases}
$$

In particular, the complexity sequence is

$$
2,\ 4,\ 4,\ 5,\ 6,\ 7,\ldots.
$$

It is unbounded and nondecreasing. Its first relevant levels are:

| Length | Words in $F$ | Count |
| --- | --- | --- |
| 2 | $00,01,10,11$ | 4 |
| 3 | $000,001,011,111$ | 4 |
| 4 | $0000,0001,0011,0111,1111$ | 5 |

There is also a finite forbidden-factor description:

$$
F=\operatorname{Av}(010,100,101,110).
$$

Indeed, the four forbidden words are exactly the three-letter words containing $10$. Every word of length at least 3 that contains $10$ has a three-letter factor containing that occurrence: extend it to the right unless it occurs in the last two positions, in which case extend it to the left. Thus avoiding the four forbidden factors forces a word of length at least 3 to have no $10$, which is precisely the form $0^i1^j$. All words of length at most 2 avoid the four forbidden words. This also shows that the example is a regular factorial language with a finite antidictionary.

## 3. A plateau in recurrent complexity must persist forever

Let $b=b_0b_1b_2\cdots$ be any infinite word over a finite alphabet $\mathcal A$. Write

$$
R_n(b)=\{u\in\mathcal A^n:u\text{ occurs infinitely often in }b\},
\qquad
p_b(n)=|R_n(b)|.
$$

The sequence $b$ itself need not be recurrent.

**Lemma.** If $p_b(n+1)=p_b(n)$ for some $n\ge1$, then $p_b(\ell)=p_b(n)$ for every $\ell\ge n$.

**Proof.** Every $u\in R_n(b)$ has a recurrent right extension. At each of its infinitely many occurrences there is a following letter; since the alphabet is finite, at least one letter $a$ follows infinitely many of those occurrences. Thus $ua\in R_{n+1}(b)$.

Deleting the final letter therefore gives a surjection

$$
\pi_n:R_{n+1}(b)\longrightarrow R_n(b).
$$

If the two finite sets have the same cardinality, this map is a bijection. In that case every recurrent word of length $n$ has exactly one recurrent right extension.

Now let $v\in R_\ell(b)$, where $\ell>n$. Every contiguous factor of $v$ is recurrent, because each of the infinitely many occurrences of $v$ contains an occurrence of that factor. The first $n$ letters of $v$ therefore determine its next letter by the unique-extension property. The next window of length $n$ determines the following letter, and so on. Induction determines all of $v$ from its length-$n$ prefix. Thus taking the first $n$ letters is an injection from $R_\ell(b)$ into $R_n(b)$.

This prefix map is also surjective: for each recurrent $n$-letter word, among the finitely many length-$\ell$ right extensions at its infinitely many occurrences, one occurs infinitely often. Therefore $|R_\ell(b)|=|R_n(b)|$. This proves the lemma. $\square$

In particular, recurrent complexity is either strictly increasing at every length or eventually constant. The proof uses only finiteness of the alphabet and infinitely many occurrences; no assumption of uniform recurrence or periodicity is needed.

## 4. Contradiction

Suppose an infinite binary sequence $b$ had $p_b(n)=q_F(n)$ at every positive length. Then

$$
p_b(2)=p_b(3)=4.
$$

The lemma forces $p_b(4)=4$. But the required value is

$$
p_b(4)=q_F(4)=5,
$$

a contradiction. Therefore the required sequence does not exist, disproving Q1653 and the stated Conjecture 6.36.

The proof does not assume that the actual recurrent factors of $b$ would equal $F$. Only their cardinalities are compared. This matters because the conjecture asks for complexity equivalence and permits a completely different recurrent language.

## 5. Scope and possible reformulations

The obstruction is a finite increase in complexity at length 2 followed by a plateau and renewed growth. In this example the extra word $10$ has no extension in $F$ to length 3. Factor closure permits such a word, whereas recurrent-factor languages always have recurrent right extensions.

Requiring a factorial language to be right extendible rules out this specific construction. Likewise, comparing complexity only for sufficiently large lengths would remove this particular contradiction, because the example has $q_F(n)=n+1$ for $n\ge3$. This note does not assert that either modified conjecture is true or resolve them. The original source requires neither modification.

The example also does not disprove any separate conjecture about the set of possible growth rates of permutation classes. The implication from a conjecture to a growth-rate statement can fail without the growth-rate statement itself being false.

## 6. Independent finite verification

The companion program verify_recurrent_complexity.py directly enumerates binary words through length 14 and checks:

1. Membership in the explicit union agrees with membership defined by avoiding the four forbidden factors.
2. Every contiguous factor of each accepted word is accepted.
3. The counts agree with the displayed formula.
4. For each possible choice of four recurrent trigrams whose prefixes cover all four bigrams, the number of compatible tetragrams is four.

The last check concerns all 16 possible one-letter right-extension rules on the four binary bigrams. It does not assume those rules can all be realized by an infinite word; it deliberately checks a larger set of candidates. Hence even this finite necessary-condition check is enough to obstruct the requested count of five tetragrams. The general lemma above remains the proof and applies to all lengths without computation.

## 7. Sources and literature boundary

**[J]** Ben Jarvis. *Pin Classes*. PhD thesis, The Open University. The PDF title page is dated August 2025; the repository catalogs it as 2026. Primary PDF: <https://oro.open.ac.uk/108335/1/Pin%20Classes.pdf>. Inspected on 2026-10-09, particularly Definitions 6.1, 6.2, 6.5, 6.9 and Conjecture 6.36. The extracted PDF text explicitly confirms factor closure without extendibility and exact equality of complexity at every length.

Both available search engines were used on 2026-10-09, with queries including Jarvis with Conjecture 6.36, the phrase complexity-equivalence conjecture, factorial language with unbounded and recurrent complexity, and factor-closed with complexity-equivalent. The stronger search also checked recent results. No published resolution of Conjecture 6.36 was located. The related paper *Pin classes II: Small pin classes* was accessible at <https://dmtcs.episciences.org/18082/pdf>; it concerns pin-class growth rates. A direct attempt to open <https://arxiv.org/pdf/2412.04143v3> returned a tool fetch error, so this note does not claim to have inspected that version. These are bounded literature checks, not a guarantee of novelty.
