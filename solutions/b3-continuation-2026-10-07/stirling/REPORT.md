# Stirling continuation: checkpoint, 7 October 2026

This continuation reconstructs the stalled agent's progress from the external agent's intermediate messages. Its updated files were not supplied. The previous packet remains at `solutions/b3-2026-10-06/`; the exact questions are Q1158–Q1161, with statement IDs `9956ab4a985ffbd2fdb0`, `046b83f433f0f897bebf`, `0aded4f0c2d209554604`, and `abb14a59ea452c80cc77`.

## Recovered theorem: first principal cycle Hankel minor

For every **integer r≥2**, the determinant

\[
H_r(x)=\det(c_{r,i+j}(x))_{i,j=0}^{2}
\]

has strictly positive coefficients in exactly degrees **2,3,4,5,6**, and zero coefficients elsewhere. This is one principal 3×3 minor; it says nothing about arbitrary order-three minors. The proof below is reconstructed independently and has no publication-priority claim. Q1160 remains open.

### Definitions and normalization

Set p=r−1. The shifted cycle triangle satisfies C(0,0)=1, with all entries outside 0≤k≤n zero, and

\[
C(n,k)=(n+pk-1)_{\underline p} C(n-1,k-1)+(n+pk-1)C(n-1,k).
\]

Let c_{r,n}(x)=Σ_k C(n,k)x^k, including **c_{r,0}(x)=1**. This is the column-shifted triangle, not the unshifted associated Stirling triangle. The normalization and recurrence agree with [Deb–Sokal, Lemma 1.1](https://arxiv.org/html/2507.18959v1#S1.SS1).

Put a=(r−1)!, y=ax, and

\[
B=\frac{(2r)!}{2(r!)^2},\qquad T=\frac{(3r)!}{6(r!)^3},\qquad U=\frac{(4r)!}{24(r!)^4}.
\]

The first five normalized rows f_n(y)=c_{r,n}(y/a) are

\[
\begin{aligned}
f_0&=1,\\
f_1&=y,\\
f_2&=ry+By^2,\\
f_3&=r(r+1)y+\frac{2r(2r+1)}{r+1}By^2+Ty^3,\\
f_4&=r(r+1)(r+2)y+
\frac{2r(2r+1)(3r^2+6r+2)}{(r+1)(r+2)}By^2+
\frac{3r(3r+1)}{r+1}Ty^3+Uy^4.
\end{aligned}
\]

These formulas follow either by the recurrence or by counting cycles of sizes at least r. In the two-cycle term of f_4, the possible unordered size pairs are (r,r+2) and (r+1,r+1); the latter carries its factor 1/2.

### Exact determinant coefficients

Write det(f_{i+j}(y))=Σ_{j=2}^6 h_j y^j. Expansion gives

\[
\begin{aligned}
h_2&=r^2(r+1),\\
h_3&=\frac{r}{(r+1)(r+2)}
\left[B(5r^4+8r^3+5r^2+8r+4)-(r^3+5r^2+8r+4)\right],\\
h_4&=\frac{r}{(r+1)^2(r+2)}(AT-DB^2-EB),\\
h_5&=\frac{r}{r+1}\left[B^2(5r+1)+BT(r-1)-T(7r+1)+U(r+1)\right],\\
h_6&=BU-T^2-B^3+2BT-U,
\end{aligned}
\]

where

\[
\begin{aligned}
A&=7r^4+20r^3+9r^2-8r-4,\\
D&=4r^4+6r^3-14r^2-16r-4,\\
E&=5r^4+16r^3+19r^2+8r.
\end{aligned}
\]

The original coefficients are a^j h_j, so their signs agree.

### All-parameter positivity proof

We have B≥3. Also

\[
\frac{T}{B^2}=\frac23\frac{(3r)!r!}{((2r)!)^2},\qquad
\frac{(T/B^2)_{r+1}}{(T/B^2)_r}
=\frac{3(3r+1)(3r+2)}{4(2r+1)^2}>1.
\]

The numerator minus denominator of the last ratio is **11r²+11r+2**. At r=2, T/B²=5/3. Thus T≥(5/3)B² for every integer r≥2. Finally U/T=binom(4r,r)/4≥7: the binomial coefficient is 28 at r=2 and increases, for example by injecting r-subsets of [4r] into (r+1)-subsets of [4r+4] by adjoining the fixed new element 4r+1.

h_2 is positive. In h_3, B≥1 leaves the strictly positive lower bound 5r⁴+7r³ within the brackets.

For h_4, A>0 for r≥2. With K=(5/3)A−D, we have K>0 and

\[
3K-E=5A-3D-E=18r^4+66r^3+68r^2-8>0.
\]

For completeness 3K=23r⁴+82r³+87r²+8r−8>0. Therefore

\[
AT-DB^2-EB\ge B^2K-BE
=B(BK-E)\ge B(3K-E)>0.
\]

For h_5, substitute U≥7T. Its bracket is at least

\[
B^2(5r+1)+BT(r-1)+6T>0.
\]

h_6 is the moment determinant det(d_{i+j})_{i,j=0}^2, where d_n=(rn)!/(n!(r!)^n). These are moments of X=(r^(r−1)/a)∏_{q=1}^{r−1}G_q, with independent shape-q/r, scale-one gamma variables. The moments agree by their consecutive ratios. X has a positive density on (0,∞), so the Andréief/Vandermonde integral for this determinant is strictly positive. Alternatively, it is the Gram determinant of 1,t,t² for a positive density; no nonzero quadratic vanishes almost everywhere. This establishes h_6>0 and completes the theorem.

## Corollary: the whole leading 3×3 cycle block

For every integer r≥2, **every nonempty minor of (c_{r,i+j}(x))_{i,j=0}² is coefficientwise nonnegative**, and each coefficient within each minor's nonzero support is strictly positive. Thus the proof supplies the first entire block, not only its determinant. It does not cover an arbitrary 3×3 Hankel block.

There are six distinct 2×2 minors up to transposition. In the table, I,J denote index sets; each bracket is the ascending list of nonzero coefficients of det(f_{i+j}(y)) for its stated degrees. All omitted coefficients are zero.

| I; J | Degrees | Coefficients |
|---|---|---|
| 01; 01 | 1–2 | r; B−1 |
| 01; 02 | 1–3 | r(r+1); r((4r+2)B−r−1)/(r+1); T−B |
| 01; 12 | 2–4 | r; 2Br²/(r+1); T−B² |
| 02; 02 | 1–4 | r(r+1)(r+2); r(B(12r³+30r²+20r+4)−r³−3r²−2r)/((r+1)(r+2)); r((9r+3)T−(2r+2)B)/(r+1); U−B² |
| 02; 12 | 2–5 | 2r(r+1); Br(r+1)(7r+2)/(r+2); 2r((4r+1)T−(2r+1)B²)/(r+1); U−BT |
| 12; 12 | 2–6 | r²(r+1); Br(5r⁴+8r³+5r²+8r+4)/((r+1)(r+2)); r(AT−DB²)/((r+1)²(r+2)); r(BT(r−1)+U(r+1))/(r+1); BU−T² |

The previous inequalities B≥3 and T≥(5/3)B² make all interior coefficients positive. In particular, AT−DB²=(AT−DB²−EB)+EB>0. For the middle term of the fourth row, B≥1 leaves 11r³+27r²+18r+4>0. Its next term is positive since T>B. The highest coefficients U−B², U−BT and BU−T² are positive generalized 2×2 gamma-product moment determinants; the remaining highest coefficients are positive for the same reason or from T>B². The 1×1 minors are the positive-coefficient rows already displayed; the 3×3 case is proved above.

## Recovery status and remaining work

The universal coefficientwise positivity of **every 2×2 Hankel minor for both families** in the external agent's intermediate message remains an unverified lead at this checkpoint. It is stronger than the original triangle TN2 theorem: those concern different matrices. A proof of the first principal 3×3 cycle minor does not recover that universal assertion.

Q1158/Q1159 still require arbitrary-order total nonnegativity of the triangles. Q1160 still requires all cycle Hankel minors. Q1161 still requires an all-n half-plane proof at r=3. No catalog resolution or original submitted ledger is altered here.

The standard-library checker [checks.py](checks.py) regenerates both triangles by their recurrence and independently compares them to the labelled-assembly coefficient formula. [checks.json](checks.json) records 880 matching entries for r=1..8 and n=0..9, the first principal determinant formula at 33 parameter values (r=2..32,64,100), and 23,328 passing **finite-only** 2×2 Hankel controls for both families at r∈{1,2,3,4,5,6,8,11,16}, I,J⊂{0,...,8}. The negative subset coefficient at r=3 is also regenerated as a scope control. These ranges are controls on transcription and recovery; the all-r theorem rests on the displayed proof. The existing packet's n≤80 stability certificates have not been recreated.

Run from the repository root:

```sh
python3 solutions/b3-continuation-2026-10-07/stirling/checks.py
```

The exact conjecture and evidence register is [conjectures.json](conjectures.json). Priority directions are to recover the universal 2×2 proof, then control a shifted order-three cycle minor rather than enlarge an already passing block. A positive ordinary production matrix cannot be obtained merely by scaling the original triangle's columns: the initial report already gives negative production entries. A successful path model must change or enlarge its state space.
