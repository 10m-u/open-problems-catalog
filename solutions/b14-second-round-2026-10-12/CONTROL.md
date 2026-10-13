# B14 continuation control

The user authorized continuation on **every B14 target**, retaining the same subagent. The same agent, /root/b14_local_optima, worked on Q3817/P3 and independent audits; the main thread coordinated the other targets. No additional agent was created.

**Clarified stopping rule:** five consecutive unsuccessful solve attempts **on one problem** stop that problem; the overall goal stops only when **every problem** is solved or has reached its own limit. A total of five failures across different problems does not stop B14. This supersedes the earlier provisional aggregate interpretation.

The stopping count concerns substantive attempts to establish the stated target. Software errors and finite-check corrections do not count. Restricted theorems and baselines are retained without closing broader statements. Each attempt states its route, what was actually tried, evidence and remaining gap. An unsuccessful bounded exploration may count without asserting its route is impossible. Obstructing a proposed lemma does not disprove the catalog conjecture.

## Target register

Eight catalog statements and six programme investigations are tracked separately. The user explicitly selected **broader research ambitions**, not only first deliverables. The register is now terminal under the clarified rule.

| Target | Current result/scope | Failure streak | State |
|---|---|---:|---|
| Q3817 | Paths/stars proved; arbitrary sparse graphs unresolved | 5 | Stopped for this problem only |
| Q3818 | Exact statement proved and reviewed in round 1 | 0 | Solved locally |
| Q549 | General-disjunction certificate discovery | 5 | Stopped, unresolved |
| Q550 | Matching variable-branch discovery | 5 | Stopped, unresolved |
| Q1852 | Path-power degree condition | 5 | Stopped after independent review |
| Q1853 | Cycle-power degree condition | 5 | Stopped after independent review |
| Q1953 | Full bicirculant Hamiltonicity | 5 | Stopped, unresolved |
| Q3819 | Existence of short improving clustering path | 5 | Stopped, unresolved |
| P1 | Certified baseline, obstructions and controlled comparison | 5 | Broader ambition stopped, unresolved |
| P2 | Exact universal endpoint equivalence plus exponential realizable quotient after elimination | 0 | Broader existential reduction ambition solved locally |
| P3 | Expected O_c(n^8 log n) strict 2-opt moves on the full sparse Exp model | 0 | Broader move-count ambition solved locally; polynomial convergence is prior art |
| P4 | All-size subdivision gap theorem and scoped rounding | 5 | General 4/3 ambition stopped, unresolved |
| P5 | Stronger all-size count bound proved | 0 | Solved locally |
| P6 | Five trained policies inside the same certified solver | 5 | Broader speed-improvement ambition stopped, unresolved |

## Reviewed unsuccessful routes

| Attempt | Problem | Route and outcome | Evidence |
|---|---|---|---|
| P1-A1 | P1 | Unique-optimum forced-1-tree bounds guarantee sparse residuals. A strict metric with a unique optimum prevents deletion of every edge. | [Proof](generating-graph/RESULT.md), [review](initialization/UNIQUENESS-REVIEW.md) |
| Q3817-A1 | Q3817 | Packing integration yields a linear expected NN ceiling. On exponential paths the ceiling is Omega(n log n). | [Attempt](initialization/ATTEMPT-Q3817-PACKING.md) |
| Q3817-A2 | Q3817 | Uniform expected traversal charge per generating edge. An exponential double-star bridge has charge Theta(log n), while the total ratio tends to one. | [Attempt](initialization/ATTEMPT-Q3817-EDGE-CHARGE.md), [receipt](initialization/DOUBLE-STAR-CHECK-RESULTS.json) |

All ten unresolved targets have reached their own five-route limits: seven catalog questions and P1/P4/P6. The fifty route failures are not fifty independent impossibility results; shared ingredients and stronger intermediate claims are explicitly identified in the reviews. No software error, timing correction or subagent connection failure is counted.

[Q3817 review](INITIALIZATION-REVIEW.md), [power review](initialization/POWER-REVIEW.md), [certificate review](initialization/CERTIFICATE-REVIEW.md), [Haar review](initialization/HAAR-REVIEW.md), [clustering review](Q3819-REVIEW.md) and [broader programme count review](BROADER-ROUTE-REVIEW.md) record the stopping evidence. The final programme count review was completed by the main thread after the retained agent's connection failures; underlying result audits retain their independent provenance.

[P2 review](initialization/P2-EXPONENTIAL-REVIEW.md) and [P3 proof/review](P3-REVIEW.md) justify those positive terminal scopes. [STATUS.json](STATUS.json) records all fourteen targets. The overall research run is complete under the user's rule, without claiming that its stopped mathematical questions have been solved.
