# Independent review of the Q3819 routes

12 October 2026. Main thread review of the retained agent's four further routes,
together with the previously checked inversion route.

The exact transfer formula agrees with independently recomputed SSE. The
fixed-size swap example defeats both two-transfer orderings, although one first
transfer already reaches a better local optimum. The displayed swap gain needs
a plus sign between its two positive terms; that transcription has been fixed.
The arbitrarily small gain family has objective one and exactly two improving
transfers; neither precision nor a long path is inferred from it. Enumeration of
all 90 unlabeled partitions certifies the global optimum in the target-assignment
example, whose only improving move increases disagreement with that optimum.
The eight-point smoothing example satisfies the published dimensional size
condition and survives normalization into the unit interval. Continuity and
the positive density of Gaussian noise justify the stated open-box failure
event; this alone says nothing about the shortest original improving path.

These count as five distinct rejected sufficient arguments: inversion descent,
simulation of swaps, a coordinate-independent progress scale, descent toward
a global assignment, and uniform smoothing with sign-preserving pullback.
The last and third share sensitivity to small margins, which is recorded
explicitly. They assert different necessary lemmas for different proposed
algorithms, rather than repeat the same test on new sizes. No sixth failure is
counted for the smoothed bound's dependence on k.

**Disposition: stop Q3819 at five consecutive failed full-target routes.**
The catalog statement remains unresolved. Every exhibited partition has a
short improving path. This review does not establish a shortest-path lower
bound, external novelty, or a disproof of Q3819.

Evidence: [agent's route packet](initialization/Q3819-ATTEMPTS.md),
[exact checker](initialization/check_q3819_routes.py), and
[receipt](initialization/Q3819-ROUTE-CHECK-RESULTS.json).
