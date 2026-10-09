# Q3569: periodic zero-extension and compatible maximal words

Date: 2026-10-09. Complete proof of the stated equivalence and its shift inequalities. This is a research result for independent review; publication and historical priority are not asserted.

## 1. Statement, conventions, and prior work

Let $U=(U_n)_{n\ge0}$ be a strictly increasing sequence of positive integers, with $U_0=1$ and bounded successive ratios. Let $\operatorname{rep}_U$ denote greedy representation and let

$$
A=\{0,1,\ldots,D\},\qquad
D=\sup_{n\ge0}\left\lceil\frac{U_{n+1}}{U_n}\right\rceil-1,
\qquad
L_U=0^*\operatorname{rep}_U(\mathbb N).
$$

The empty word represents zero. Set

$$
M_n=\operatorname{rep}_U(U_n-1).
$$

Then $M_0=\varepsilon$ and $|M_n|=n$. For a finite or infinite word, $\operatorname{Pref}_k$ denotes its first $k$ letters; for a finite word, $\operatorname{Suff}_k$ denotes its last $k$ letters. Prefixes and suffixes of length zero are empty. The map $\sigma$ deletes the first letter of an infinite word.

Q3569 is Savinien Kreczman's Conjecture 9.1, printed p. 280, in *Linear numeration systems without a dominant root, alternate base numeration systems, and their links* (2026). Its definitions are in §1.2. The conjecture concerns arbitrary positional $U$-systems with the conditions above, not only linear recurrences. The case $p=1$ is already Lemma 1.43 of the thesis, attributed to Charlier–Cisternino–Stipulanti, Lemma 3. The suffix criterion used below is also established prior work, thesis Lemma 1.11. We give elementary proofs of the necessary language facts to make this note self-contained. [K, CCS]

**Theorem.** Fix any integer $p\ge1$. The following conditions are equivalent:

1. For every $w\in A^*$, $w\in L_U$ if and only if $w0^p\in L_U$.
2. For every $m\ge0$, $\operatorname{Pref}_m(M_{m+p})=M_m$.
3. There are infinite words $a_0,\ldots,a_{p-1}\in A^{\mathbb N}$ such that
   $$
   M_{np+i}=\operatorname{Pref}_{np+i}(a_i)
   \quad(n\ge0,\ 0\le i<p).
   $$

When these conditions hold, the infinite words are unique and satisfy

$$
\boxed{\sigma^j(a_i)\le_{\mathrm{lex}}a_{\,i-j\bmod p}
\quad(0\le i<p,\ j\ge0).}
$$

Conditions 1 and 3, together with the displayed inequalities, are exactly the source conjecture. Condition 2 gives a useful intermediate finite-word formulation.

## 2. Two elementary facts about greedy languages

For a word written with the most significant digit first, define

$$
\operatorname{val}_U(d_{m-1}\cdots d_0)
=\sum_{r=0}^{m-1}d_rU_r.
$$

The greedy algorithm gives the following criterion:

$$
w=d_{m-1}\cdots d_0\in L_U
\quad\Longleftrightarrow\quad
\sum_{r=0}^{k-1}d_rU_r<U_k
\quad(1\le k\le m).
\tag{1}
$$

Indeed, in a greedy representation, the remainder after choosing the digit at position $k$ is less than $U_k$. Conversely, these inequalities ensure that at every position the remainder from lower positions is less than the current place value, so the indicated digit is exactly the quotient chosen by the greedy algorithm. Initial zeroes cause no difficulty.

One consequence is **coordinatewise downward closure**: decreasing any digits of a word in $L_U$, while keeping them nonnegative, leaves the word in $L_U$. All sums in (1) can only decrease. In particular,

$$
xy\in L_U\quad\Longrightarrow\quad x0^{|y|}\in L_U.
\tag{2}
$$

The second consequence is the lexicographic suffix criterion:

$$
\boxed{w\in L_U
\quad\Longleftrightarrow\quad
\operatorname{Suff}_k(w)\le_{\mathrm{lex}}M_k
\quad(0\le k\le |w|).}
\tag{3}
$$

Here is a direct proof. Among valid words of a fixed length, numerical order agrees with lexicographic order. At the first differing digit, with place value $U_r$, the difference at that position is at least $U_r$, whereas each lower suffix has value between zero and $U_r-1$, by (1). The lower suffixes cannot reverse that comparison. Since the valid words of length $k$ represent exactly the integers from zero through $U_k-1$, the largest is $M_k$. Every suffix of a valid word is valid by (1), proving the forward implication in (3).

For the converse, use induction on $m=|w|$. The empty word is valid. If all suffix comparisons in (3) hold for a nonempty $w$, its proper suffix of length $m-1$ is valid by induction. Write $w=cv$ and $M_m=dt$, where $|v|=|t|=m-1$. The words $v,t$ are valid. If $c<d$, then

$$
\operatorname{val}_U(w)
\le(c+1)U_{m-1}-1
\le dU_{m-1}-1
\le \operatorname{val}_U(M_m).
$$

If $c=d$, the comparison $w\le_{\mathrm{lex}}M_m$ gives $v\le_{\mathrm{lex}}t$, and the established numerical-order property gives the same value inequality. The case $c>d$ is excluded by $w\le_{\mathrm{lex}}M_m$. Thus the full word has value at most $U_m-1$, and its proper suffixes already meet (1); hence $w$ is valid. This proves (3).

## 3. Zero-extension implies compatibility of maximal words

Assume condition 1, and fix $m\ge1$. Appending $p$ zeroes to $M_m$ gives a valid length-$m+p$ word, so maximality gives

$$
M_m0^p\le_{\mathrm{lex}}M_{m+p}.
\tag{4}
$$

Let $P=\operatorname{Pref}_m(M_{m+p})$. Taking length-$m$ prefixes in (4) yields $M_m\le_{\mathrm{lex}}P$.

On the other hand, $M_{m+p}$ is valid. By downward closure (2), replacing its last $p$ digits by zeroes gives $P0^p\in L_U$. Applying condition 1 in the removal direction gives $P\in L_U$. Since $P$ has length $m$, its maximality bound is $P\le_{\mathrm{lex}}M_m$. Therefore $P=M_m$, proving condition 2 for $m\ge1$. For $m=0$, both sides are empty, so it holds as well.

This is the only place where one must be careful about deleting $p$ digits: the assumption directly permits deletion of $p$ trailing zeroes. Formula (2) first turns the arbitrary final $p$ digits of a maximal word into zeroes.

## 4. Compatibility implies zero-extension

Assume condition 2. For each $k\ge0$, there is a word $t_k$ of length $p$ such that

$$
M_{k+p}=M_kt_k.
$$

For every word $v$ of length $k$,

$$
v0^p\le_{\mathrm{lex}}M_{k+p}
\quad\Longleftrightarrow\quad
v\le_{\mathrm{lex}}M_k.
\tag{5}
$$

If $v\ne M_k$, the comparison is decided within the first $k$ positions. If $v=M_k$, the left side is true because $0^p\le_{\mathrm{lex}}t_k$. This also handles $k=0$.

Now fix an arbitrary $w\in A^*$. Every suffix of $w0^p$ of length at most $p$ consists entirely of zeroes and satisfies (3). Each longer suffix has the form

$$
\operatorname{Suff}_k(w)\,0^p,\qquad 1\le k\le|w|.
$$

By (5), its comparison with $M_{k+p}$ is equivalent to the comparison of $\operatorname{Suff}_k(w)$ with $M_k$. Using (3) for both words proves

$$
w0^p\in L_U\quad\Longleftrightarrow\quad w\in L_U,
$$

which is condition 1. In particular, the empty word and all short suffixes are included.

## 5. Infinite limits along residue classes

Assume condition 2. For each fixed $i\in\{0,\ldots,p-1\}$, the words

$$
M_i,\ M_{p+i},\ M_{2p+i},\ldots
$$

are nested prefixes whose lengths tend to infinity. Their union therefore determines a unique infinite word $a_i$ over $A$, satisfying condition 3.

Conversely, in condition 3, the words $M_m$ and $M_{m+p}$ are prefixes of the same $a_i$, with $i\equiv m\pmod p$. Thus the former is the length-$m$ prefix of the latter, which is condition 2.

## 6. The cross-residue shift inequalities

Assume the equivalent conditions and fix $i\in\{0,\ldots,p-1\}$ and $j\ge0$. Let

$$
r=i-j\bmod p\in\{0,\ldots,p-1\}.
$$

Choose arbitrarily large $N\equiv i\pmod p$ with $N\ge j$. Since $M_N$ is a valid word, its suffix of length $N-j$ is valid and hence bounded by the maximal word of that length:

$$
\operatorname{Suff}_{N-j}(M_N)
\le_{\mathrm{lex}}M_{N-j}.
$$

The prefix descriptions of the $a_i$'s rewrite this as

$$
\operatorname{Pref}_{N-j}\bigl(\sigma^j(a_i)\bigr)
\le_{\mathrm{lex}}
\operatorname{Pref}_{N-j}(a_r).
\tag{6}
$$

These compared lengths tend to infinity. If $\sigma^j(a_i)>_{\mathrm{lex}}a_r$, their first differing position would violate (6) for all sufficiently large such $N$. Therefore $\sigma^j(a_i)\le_{\mathrm{lex}}a_r$, as required. The case $j=0$ simply gives equality with $a_i$.

This completes the proof of Q3569. No existence or value of a dominant root was used.

## 7. A period-two example

Set

$$
U_{2k}=6^k,\qquad U_{2k+1}=2\cdot6^k.
$$

These place values have successive ratios alternating between 2 and 3. The maximal words are

$$
M_{2k}=(21)^k,\qquad M_{2k+1}=1(21)^k.
$$

Consequently condition 3 holds with $p=2$, $a_0=(21)^\infty$, and $a_1=(12)^\infty$. The theorem shows that validity is preserved and reflected by adding two zeroes.

Adding just one zero does not have the same property: $2\notin L_U$, whereas $20\in L_U$, since its value is $2U_1=4<U_2=6$ and its final digit is zero. Thus the result covers systems beyond the already known $p=1$ condition. Direct greedy evaluation verifies the displayed maximal words.

## 8. Reproducible controls and scope

The companion program verify_periodic_zero.py constructs greedy representations from integer place values and tests membership independently using the remainder inequalities (1). It compares this membership calculation with the suffix criterion and tests the finite version of conditions 1 and 2 across many strictly increasing finite prefixes of $U$, including failure cases, the empty word, and $p$ larger than the tested word length. It also checks the alternating-ratio example explicitly. Its JSON output records the bounds and counts.

The completed run checked 729 place-value prefixes, 995,085 comparisons between numeric membership and the suffix criterion, and 2,916 finite equivalence profiles for $p=1,2,3,4$. Of the latter, 120 satisfy both finite conditions and 2,796 fail both. It also checked two-zero extension for all 9,841 words over $\{0,1,2\}$ of length at most 8 in the alternating-ratio example, along with 62 periodic shift comparisons. Every check passed.

These controls test indexing and representation conventions. The infinite equivalence and infinite-word comparisons are proved above, independently of finite verification.

This note does not resolve the source's separate conjectures about alternate-base intermediate representations or noncanonical shifts. Those are stronger further steps in the source's proposed research program.

## 9. Source access and literature boundary

**[K]** Savinien Kreczman. *Linear numeration systems without a dominant root, alternate base numeration systems, and their links*. PhD thesis, Université de Liège, 2026. Institutional record: <https://orbi.uliege.be/handle/2268/345086>. Full text: <https://orbi.uliege.be/bitstream/2268/345086/1/Kreczman_PhD_Thesis_JuryRemarks.pdf>. The full 340-page PDF was inspected on 2026-10-09 via the record's download link, after a direct PDF fetch initially failed. Relevant locations: definitions and greedy inequalities, printed pp. 12–13; Lemmas 1.10–1.11, p. 16; Lemma 1.43, p. 33; Conjecture 9.1, p. 280.

**[CCS]** Émilie Charlier, Célia Cisternino, Manon Stipulanti. *A full characterization of Bertrand numeration systems*. Developments in Language Theory, 2022. Primary author PDF: <https://orbi.uliege.be/bitstream/2268/289032/1/Charlier-Cisternino-Stipulanti-DLT2022.pdf>. Inspected on 2026-10-09. Lemma 1 gives the suffix criterion, and Lemma 3 proves the $p=1$ case. The argument here extends that finite-word mechanism to arbitrary $p$, explicitly supplying the downward-closure step and the cross-residue limiting argument.

Bounded searches on 2026-10-09 used both search engines with Kreczman and Conjecture 9.1, periodic Bertrand numeration, p-Bertrand, maximal words and prefixes, and zero-extension terminology. They returned the thesis and related numeration papers, including the known $p=1$ characterization. No later resolution of the exact $p$-periodic statement was located. This does not establish historical novelty.
