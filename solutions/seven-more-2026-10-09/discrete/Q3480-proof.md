# Q3480: exact finite-alphabet enumeration and a four-symbol formula

Date: 2026-10-09. Proposed catalog status: **partial**.

## Result and remaining scope

Let \(F_k(n)\) count words of length \(n\) over \([k]\), allowing unused symbols, for which two applications of the hare stack map give a weakly increasing output. Put \(F_k(z)=\sum_{n\geq0}F_k(n)z^n\). Then

\[
\boxed{F_4(z)=\frac{1-9z+30z^2-42z^3+19z^4}{(1-z)(1-3z)^4}.} \tag{1}
\]

If \(A_4(n)\) counts the sortable **Cayley words with maximum exactly four**, then

\[
\boxed{\sum_{n\geq0}A_4(n)z^n
=\frac{z^4(22-119z+162z^2)}{(1-z)(1-2z)(1-3z)^4}.} \tag{2}
\]

In particular,

\[
A_4(n)\sim\frac{n^3 3^n}{324}.
\]

The report also gives an exact finite automaton for each arbitrary fixed alphabet size \(k\), and hence an explicit matrix/inclusion-exclusion formula for every unrestricted length. It does **not** obtain a closed generating function or a useful uniform asymptotic formula for the sum over all possible maximum symbols. Those unrestricted aspects of Cerbai's enumeration question remain unresolved here; the catalog should retain partial status.

## Source alignment

Cerbai, *Sorting Cayley permutations with pattern-avoiding machines*, [Australasian Journal of Combinatorics 80 (2021), 322–341](https://ajc.maths.uq.edu.au/pdf/80/ajc_v80_p322.pdf), Open Problem 1 on printed page 330, asks for this enumeration. The same passage equates 21-sortability with two applications of the hare map. Theorem 3.8 provides a pattern characterization used below. The distinct hare **pop-stack** question appears later in the paper and has a different sorting operation; it is not the subject of this result.

## 1. The general finite automaton

Apply the first stack to the incoming word and feed its output immediately into a second stack. A stack is weakly increasing from top to bottom. On incoming value \(x\), it pops every top value strictly less than \(x\), then pushes \(x\). Equal values may remain together on a stack.

At any time, equal values on one stack occur consecutively. Replace every nonempty run of equal values by one representative. This replaces each weakly monotone stack by a subset of \([k]\), with the order determined by its values. It preserves the decision whether the final output contains an inversion:

1. When a value \(x\) arrives, whether a run is popped depends only on whether its value is less than \(x\), not on its multiplicity.
2. A popped run of value \(v\) feeds a positive number of consecutive copies of \(v\) to the second stack. The first copy pops all lower values and pushes \(v\). Further copies cause no additional pops and merely enlarge its run.
3. A run emitted by the second stack contains no internal inversion. Whether it creates a new inversion depends only on its value and the last previously emitted value.

These observations give an induction over input letters and whole-run pop events: the compressed simulation has the same distinct runs on both stacks and the same last output value as the literal simulation, unless an output inversion has already been detected. At end of input, flush the first stack into the second and then flush the second; the same induction applies.

Thus a state consists of \((S_1,S_2,\ell)\), where \(S_i\subseteq[k]\) and \(\ell\in\{0,1,\ldots,k\}\) records the last output value, with zero as the no-output sentinel. A rejecting sink records an already emitted inversion. There are at most

\[
(k+1)4^k+1
\]

states. The initial state is \((\varnothing,\varnothing,0)\).

### Transition rule

To read \(x\), remove the elements of \(S_1\) less than \(x\), in increasing order, and feed each removed value to \(S_2\). To feed \(v\), remove the elements of \(S_2\) less than \(v\), again in increasing order, comparing each emitted value with \(\ell\). Reject if an emitted value is smaller; otherwise update \(\ell\). Finally insert \(v\) into \(S_2\). After processing the removed first-stack values, insert \(x\) into \(S_1\).

The accepting indicator of a state is found by the analogous two flushes. This makes the automaton completely explicit for every \(k\), including states which would reject only on a final flush.

Let \(T_k\) be its transition-count matrix: an entry counts input symbols leading from one state to another. Let \(e_k\) select the initial state and let \(b_k\) be the accepting indicator column. Then

\[
F_k(n)=e_k^{\mathsf T}T_k^n b_k,
\qquad
F_k(z)=e_k^{\mathsf T}(I-zT_k)^{-1}b_k. \tag{3}
\]

In particular \(F_k(z)\) is rational for each fixed alphabet. All entries of \(T_k\) and \(b_k\) are explicitly computable by the transition rule; this is not a recurrence that calls an unknown sorting count.

Let \(A_k(n)\) count sortable words using every letter in \([k]\). Relabeling an increasing subset of the alphabet preserves all stack comparisons, so ordinary inclusion-exclusion gives

\[
A_k(n)=\sum_{j=0}^{k}(-1)^{k-j}\binom kj F_j(n). \tag{4}
\]

Here \(F_0(0)=1\) and \(F_0(n)=0\) for \(n>0\). The unrestricted Cayley count is consequently

\[
A(n)=\sum_{k=1}^{n}\sum_{j=0}^{k}(-1)^{k-j}\binom kj e_j^{\mathsf T}T_j^n b_j.
\tag{5}
\]

This exact algorithm replaces enumeration of individual Cayley words by state counting, but its state-space bound is exponential in alphabet size. Formula (5) is not presented as a closed-form resolution of the unrestricted enumeration problem.

## 2. A six-state automaton for four letters

Specialize the forbidden-pattern criterion in Cerbai's Theorem 3.8 to the alphabet \(\{1,2,3,4\}\). A word fails precisely when it contains a subsequence 2341, or a subsequence 3241 with **no 4 between the selected 3 and 2**. No pattern on fewer than four distinct symbols causes failure under this criterion.

The following states record the necessary prefix information. Once a higher-numbered persistent state has been reached, the descriptions of earlier states are no longer used.

| State | Information remembered before rejection |
|---|---|
| 0 | No 2 has occurred, and no 3 has occurred since the latest 4. |
| 1 | A 2 has occurred, but neither of the two pairs in state 3 has occurred. |
| 2 | No 2 has occurred, and a 3 has occurred since the latest 4. |
| 3 | A 23 subsequence, or a 32 subsequence with no intervening 4, has occurred; a subsequent 4 is still needed. |
| 4 | One of those pairs has been followed by a 4; a subsequent 1 is forbidden. |
| 5 | A forbidden pattern has occurred. |

Starting at 0, the transitions are

| State | Read 1 | Read 2 | Read 3 | Read 4 | Accept at end? |
|---:|---:|---:|---:|---:|:---:|
| 0 | 0 | 1 | 2 | 0 | Yes |
| 1 | 1 | 1 | 3 | 1 | Yes |
| 2 | 2 | 3 | 2 | 0 | Yes |
| 3 | 3 | 3 | 3 | 4 | Yes |
| 4 | 5 | 4 | 4 | 4 | Yes |
| 5 | 5 | 5 | 5 | 5 | No |

Each transition follows directly from the recorded events. For example, reading 4 in state 2 removes the relevant 3 from the current interval after the latest 4; reading 3 in state 1 permanently creates a 23 pair. Either qualifying pair, followed later by 4 and then 1, is exactly a forbidden pattern.

The independent finite certificate also maps all 174 reachable compressed stack states, plus the rejecting sink, to this six-state automaton. It checks all 700 transitions and every acceptance label. This verifies the six-state presentation directly from the stack mechanics as well as from the source's pattern theorem.

## 3. Derive the generating functions

Let \(g_i(z)\) count acceptable continuations from state \(i\). Every nonrejecting state accepts the empty continuation. From the transition table,

\[
\begin{aligned}
g_4&=1+3zg_4,\\
g_3&=1+3zg_3+zg_4,\\
g_1&=1+3zg_1+zg_3,\\
g_2&=1+2zg_2+zg_3+zg_0,\\
g_0&=1+2zg_0+zg_1+zg_2.
\end{aligned}
\]

Solving the first three gives

\[
g_4=\frac1{1-3z},\quad
g_3=\frac{1-2z}{(1-3z)^2},\quad
g_1=\frac{1-5z+7z^2}{(1-3z)^3}.
\]

Eliminating \(g_2\) from the remaining equations gives

\[
((1-2z)^2-z^2)g_0=(1-2z)(1+zg_1)+z(1+zg_3).
\]

Since \((1-2z)^2-z^2=(1-z)(1-3z)\), substitution gives (1).

Every word over at most three letters succeeds, either by the four-distinct-symbol characterization or by the general stack automaton. Hence \(F_j(z)=1/(1-jz)\) for \(1\leq j\leq3\), while \(F_0(z)=1\). Equation (4) gives

\[
\sum_{n\geq0}A_4(n)z^n
=F_4(z)-\frac4{1-3z}+\frac6{1-2z}-\frac4{1-z}+1,
\]

which simplifies to (2). Its pole at \(z=1/3\) has order four and leading coefficient \(1/54\) when written as a multiple of \((1-3z)^{-4}\). Thus

\[
A_4(n)\sim\frac1{54}\binom{n+3}{3}3^n
\sim\frac{n^3 3^n}{324}.
\]

## 4. Exact checks and limitations

Run from the repository root:

```sh
python solutions/seven-more-2026-10-09/discrete/q3480_enumerate.py
python solutions/seven-more-2026-10-09/discrete/q3480_verify.py
```

Both use only the Python standard library. The generator constructs the general compressed automata for alphabets from zero through eight and evaluates (4) and (5). It recovers the source's unrestricted initial sequence

\[
1,3,13,73,483,3547,27939,231395.
\]

The separate verifier imports no enumeration code. It tests all 87,381 words of lengths zero through eight over four letters using literal stacks that retain every copy of every symbol. It independently reconstructs the 700 quotient transitions using tuples, checks reachability and acceptance, and verifies the rational identities by exact integer polynomial arithmetic. A matrix polynomial identity for the five live states certifies the denominator recurrence for all lengths, not only the checked prefix.

The explicit word 34241 succeeds while 3241 fails; this checks the equality case in the source's additional Cayley-mesh condition. Repeated symbols must not be treated as distinct permutation ranks.

The general automata, the four-symbol rational series, and its asymptotic are proved here. No minimality theorem for general alphabet-size automata, no unrestricted algebraic generating function, and no unrestricted growth constant is claimed. A bounded literature search found the general problem still stated, but does not establish priority for every finite-alphabet observation.

Artifacts: [q3480_certificate.json](q3480_certificate.json), [q3480_enumerate.py](q3480_enumerate.py), [q3480_verify.py](q3480_verify.py), and the dated [source log](SOURCES.md).
