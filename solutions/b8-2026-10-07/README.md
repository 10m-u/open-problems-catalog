# B8: unseen vocabulary, missing mass and support estimation

Research report from an AI research agent working on this catalog, filed as received. The proofs are written arguments by that agent; they have not been independently re-derived or peer reviewed. Statuses below are the report's own, at its stated scope.

| Problem | Title | Status | Result |
|---|---|---|---|
| [Q851](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q851) | The remaining accuracy cost of support-size diagnosis | investigated | No new result at this scope. Remaining/limits: Close the epsilon-dependent logarithmic gap in the non-tolerant sample complexity. |
| [Q852](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q852) | Tolerant support diagnosis without a support-size promise | proved | Yes. With δ=ε−ε′, C·n·log²(e/δ)/(δ²·log(en)) samples estimate d_n(p) within δ/4 with probability at least 3/4 for every countable distribution, with no support promise; thresholding gives the tolerant test. Scope: Full retained… |
| [Q853](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q853) | Removing the log cost of dependent missing-mass estimation | investigated | No new result at this scope. Remaining/limits: A general O(T/n) estimator or a lower bound ruling it out remains absent. |
| [Q854](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q854) | Linear mixing-time variance of unseen stationary mass | partial | Var(M0) ≤ min{1/4, 1/(an)} ≤ min{1/4, 2T/n} for every stationary refresh chain (1−a)I+a·1π^T; uniform examples show the linear dependence on T is needed. Scope: Arbitrary kernels remain open. Not independently re-derived. |
| [Q855](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q855) | The rare-count mass estimation frontier | partial | iid cumulative Good–Turing has MSE ≤ min{1, 22√(ζ+1)/n}, so the iid (ζ+1)/n order is not sharp for growing ζ (that sharpness subclaim is disproved); complementary plug-in envelopes 1/(ζ+1) iid and 4T/(ζ+1) Markov. Scope: Matching lower… |
| [Q856](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q856) | The exact minimax constant for unseen probability mass | partial | Among unclipped linear estimators Σ\_{r≤R} β\_{r,n}Φ\_r with fixed R and deterministic coefficients the best asymptotic worst-case constant is c_GT=0.6080367865…; Painsky's Eq. G73 estimator has the same leading constant. Scope: The… |
| [Q858](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q858) | Gaussian uncertainty for distinct entities observed in pairs | proved | Yes. For every fixed law on unordered pairs of distinct naturals, Var\|V_n\|→∞ implies (\|V_n\|−E\|V_n\|)/√Var\|V_n\| ⇒ N(0,1), with no connectedness assumption (zero-free region, cumulant bounds, de-Poissonization). Scope: Full retained… |
| [Q859](../../problems/computer_science_ai/classical-statistical-machine-learning.md#q859) | Linear rarity cost for next-event exposure estimation | partial | In the iid submodel with ζ\_n→∞ and ζ\_n=o(n), minimax MSE for unconditional next-token rare exposure is Θ(ζ\_n/n); explicit finite-sample Markov bound with its bias terms; worst-case bounded differences cannot remove the quadratic rarity… |

## Files

- [B8_Prose_Diagnostics_2026-10-07.png](B8_Prose_Diagnostics_2026-10-07.png)
- [B8_Research_Report_2026-10-07.md](B8_Research_Report_2026-10-07.md)
- [B8_Statement_Ledger_2026-10-07.json](B8_Statement_Ledger_2026-10-07.json)

