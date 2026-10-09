# Independent review of the Q3569 proof

**Verdict: accepted as a complete proof of the exact stated conjecture.** The proposed equivalence holds for every positional numeration system in the source's scope and every integer $p\geq1$. The cross-residue shift inequalities are also proved. No additional recurrence or dominant-root assumption is needed.

Reviewed on 9 October 2026: `../discrete/Q3569-periodic-zero-extension.md`. This is an independent mathematical review within this research round, not external peer review or a certification of historical priority.

## Exact source and hypotheses

I opened the [institutional thesis record](https://orbi.uliege.be/handle/2268/345086) and followed its Download link to the [primary thesis PDF](https://orbi.uliege.be/bitstream/2268/345086/1/Kreczman_PhD_Thesis_JuryRemarks.pdf). I read Definition 1.4, Definition 1.6 and equation (1.1), Lemmas 1.10–1.11, Lemma 1.43, and Conjecture 9.1.

Conjecture 9.1, printed page 280, asks precisely for equivalence between invariance of $L_U$ under appending/removing $p$ terminal zeroes and existence of the specified infinite words along lengths modulo $p$. It includes the stated shift inequalities. The report uses the source's positional setting: strictly increasing positive integer place values, $U_0=1$, bounded successive ratios, the resulting finite digit alphabet, greedy representations, and permitted initial zeroes. The known $p=1$ result is identified as prior work. The later conjectures concerning alternate bases and noncanonical shifts are separate questions.

## Greedy membership and the suffix criterion

Let $M_m=\operatorname{rep}_U(U_m-1)$. Then $|M_m|=m$ and $M_0=\varepsilon$. For $w=d_{m-1}\cdots d_0$, the numeric criterion

$$
w\in L_U\iff
\sum_{r=0}^{k-1}d_rU_r<U_k\quad(1\leq k\leq m)
$$

is valid, including words with initial zeroes. The report's proof is consistent with the source's equation (1.1). In particular, decreasing digits coordinatewise preserves every inequality and therefore preserves membership. This downward closure is sufficient to replace an arbitrary terminal block by zeroes without changing its length.

The report also correctly proves, rather than merely assuming, the lexicographic suffix criterion

$$
w\in L_U\iff
\operatorname{Suff}_k(w)\leq_{\rm lex}M_k
\quad(0\leq k\leq |w|).
$$

The numerical-order argument is only used for **valid** equal-length words, where each lower-position remainder lies in $[0,U_r-1]$. This restriction is essential and is respected. In the converse induction, the proper suffix is already valid before that order argument is applied. The case of a strictly smaller first digit supplies the remaining full-word bound. There is no circular use of the criterion being proved.

## The equivalence

The report's intermediate condition is

$$
M_m=\operatorname{Pref}_m(M_{m+p})\qquad(m\geq0).
$$

Under zero-extension invariance, $M_m0^p$ is valid, so its length-$m$ prefix is at most the corresponding prefix $P$ of $M_{m+p}$. Conversely, downward closure gives $P0^p\in L_U$. The assumed removal of $p$ terminal zeroes gives $P\in L_U$, and maximality then gives $P\leq_{\rm lex}M_m$. These two inequalities force equality. The argument does not wrongly assume that arbitrary terminal digits may be deleted.

For the converse, write $M_{k+p}=M_kt_k$ with $|t_k|=p$. For every length-$k$ word $v$,

$$
v0^p\leq_{\rm lex}M_{k+p}
\iff v\leq_{\rm lex}M_k.
$$

A strict comparison is decided among the first $k$ positions. In the equality case, the appended zero block is at most $t_k$ because all digits are nonnegative. Applying this equivalence to each suffix proves both directions of zero-extension invariance by the suffix criterion.

Prefix consistency along each sequence of lengths $i,p+i,2p+i,\ldots$ gives a unique infinite word $a_i$. Its prefixes have unbounded lengths, so neither existence nor uniqueness requires a compactness assumption beyond this explicit nesting. Conversely, the asserted infinite words immediately imply prefix consistency.

## Boundary lengths and shift indices

All boundary cases in the written proof are correct:

- $M_0=\varepsilon$, and its prefix consistency is automatic.
- For the empty word, the appended word $0^p$ is valid.
- Every suffix of an appended word of length at most $p$ consists entirely of zeroes, so it meets its own maximal-word bound.
- Every longer suffix is exactly $\operatorname{Suff}_k(w)0^p$ for some $1\leq k\leq |w|$. This covers all remaining lengths, even when $p>|w|$.
- The residue $i=0$ starts with an empty prefix, but its later prescribed lengths tend to infinity and still determine $a_0$ uniquely.

For a fixed $i$ and arbitrary shift $j\geq0$, choose unbounded lengths $N\equiv i\pmod p$ with $N\geq j$. The suffix of $M_N$ of length $N-j$ is valid and at most $M_{N-j}$. These two finite words are respectively the length-$N-j$ prefixes of $\sigma^j(a_i)$ and $a_{i-j\bmod p}$. Thus their prefix comparisons hold at unbounded lengths. Any reversed infinite lexicographic comparison would have a first differing position, contradicting one of those comparisons. This proves exactly the source's inequality, with the correct residue sign. The cases $j=0$ and $j>i$ are covered.

## Example and scope of the verdict

For $U_{2k}=6^k$ and $U_{2k+1}=2\cdot6^k$, the place-value ratios are alternately $2$ and $3$. Greedy evaluation gives $M_{2k}=(21)^k$ and $M_{2k+1}=1(21)^k$, as claimed. The resulting infinite words are $a_0=(21)^\infty$ and $a_1=(12)^\infty$. Also $2\notin L_U$ while $20\in L_U$: the latter has value $4<U_2=6$ and zero final remainder. The example therefore satisfies the $p=2$ condition while failing the $p=1$ condition.

I also inspected and independently ran `../discrete/verify_periodic_zero.py` from the repository root. Its exact integer controls passed: 729 place-value prefixes, 995,085 comparisons of numeric membership with the suffix criterion, 2,916 finite equivalence profiles for $p=1,2,3,4$ (120 true and 2,796 false), 9,841 checks of the alternating example's two-zero extension, and 62 periodic shift checks. The enumeration includes the empty word and periods larger than the tested word length. The resulting `../discrete/periodic-zero-checks.json` agrees with those counts.

No gap was found in the general proof or the example. The verdict rests on the proof for arbitrary lengths and does not infer an infinite-language assertion from finite experiments. The computations check implementation and indexing conventions. This review does not establish whether the same generalization has previously appeared elsewhere.
