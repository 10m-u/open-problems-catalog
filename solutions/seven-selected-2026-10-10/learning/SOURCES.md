# Q726: source verification and bounded literature check

Checked on **2026-10-10**.

## Primary statement and assumptions

Barna Pásztor, Parnian Kassraie and Andreas Krause,
*Bandits with Preference Feedback: A Stackelberg Game Perspective*.

- [arXiv:2406.16745v3, 18 December 2025](https://arxiv.org/html/2406.16745v3).
- [NeurIPS 2024 proceedings version](https://proceedings.neurips.cc/paper_files/paper/2024/file/1646e34971facbcda3727d1dc28ab635-Paper-Conference.pdf).

The exact question follows Theorem 6 in §5.2. Algorithm 1 and equation (7)
specify the two selection domains. Corollary 5 supplies the uniform confidence
event. Equation (4) supplies the covariance regularizer. The paragraph after
equation (3) states the norm-bounded estimator convention and points to the
Appendix A projection. Proposition 4 and Appendix C.1 identify the dueling
RKHS. Appendix C.2 explains how the restricted-domain proof uses plausible
maximizers; the new proof replaces that step with a metric max-min lemma.

## Later-work check

Both available search systems were used. Queries included:

- `"MaxMinLCB" "unrestricted"`
- `"MaxMinLCB" "without" "regret"`
- `"MaxMinLCB" "triangle"`
- `"MaxMinLCB" "unrestricted" regret proof` (past year)
- `"MaxMinLCB" "conjecture"` (past year; excluding mirrors of the source)

The author's [publication page](https://pasztorb.github.io/publications/)
still links the original result. The later primary paper
[Kayal et al., arXiv:2505.23673](https://arxiv.org/abs/2505.23673),
*Bayesian Optimization from Human Feedback: Near-Optimal Regret Bounds*,
was inspected as related work; it develops a different algorithm and a sharper
regret target. The accessible source version still explicitly leaves the
unrestricted MaxMinLCB question conjectural.

No matching resolution was located in this bounded check. This statement is
not a claim that every publication or unpublished result has been searched.
The proof in this packet is proposed new work, conditional only on the same
theoretical estimator/confidence assumptions as the catalog question.

Only links and original notes are committed; downloaded source text is not.
