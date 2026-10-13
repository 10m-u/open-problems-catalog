# Primary-source context and novelty boundary

Checked 2026-10-12. These sources provide context, not external verification of the new proofs. Targeted searches for the combination of 2-opt, blocks/biconnected components, sign-preserving integer weights, and module/necklace completion did not establish priority for the precise results in this packet. This is a bounded literature check, not evidence that no prior equivalent result exists.

## Established local elimination

William Cook, Keld Helsgaun, Stefan Hougardy and Rasmus T. Schroeder, “Local elimination in the traveling salesman problem,” arXiv:2307.07054 (2023), later Mathematical Programming Computation, DOI 10.1007/s12532-024-00262-y.

Primary pages checked: https://arxiv.org/abs/2307.07054 and https://link.springer.com/article/10.1007/s12532-024-00262-y.

The paper combines LP reduced-cost elimination with a combinatorial method using exact k-opt searches. Thus local or combinatorial elimination itself is not new here. The present claim is the explicit primary-face characterization, completion formulas, contracted exact DP, and separation from a specified rooted-1-tree family. There is no computational comparison against that published implementation.

## Established integer weight compression

András Frank and Éva Tardos, “An application of simultaneous diophantine approximation in combinatorial optimization,” Combinatorica 7 (1987), 49-65, DOI 10.1007/BF02579200.

Primary page checked: https://link.springer.com/article/10.1007/BF02579200.

Its abstract describes replacing objective weights by bounded integral weights preserving optimal solutions. Integer weight compression is therefore established background. The block-descent proof supplies its own elementary vertex/determinant argument for a specific finite collection of four-label signs. The block noncancellation lemma and the resulting global quadratic descent bound are the research claims in this continuation; the packet does not claim to originate the general compression method.

## Probabilistic shortest-path analysis

Stefan Klootwijk, Bodo Manthey and Sander K. Visser, “Probabilistic Analysis of Optimization Problems on Generalized Random Shortest Path Metrics,” arXiv:1810.11232, revised 2020.

Primary page checked: https://arxiv.org/abs/1810.11232.

The abstract reports a polynomial bound on the expected number of 2-opt iterations in the random shortest-path models it studies. The new statement is deterministic under a fixed maximum biconnected-block size and permits arbitrary positive lengths. The broad abstract is not used to assert that the older expected-time theorem covers every sparse generating graph.

Stefan Klootwijk and Bodo Manthey, “Probabilistic Analysis of Optimization Problems on Sparse Random Shortest Path Metrics,” Algorithmica (2023), DOI 10.1007/s00453-023-01167-3.

Primary page checked: https://link.springer.com/article/10.1007/s00453-023-01167-3.

This is the programme's source for sparse-metric nearest-neighbor and local-optimum quality questions. The new deterministic block theorem is a descent-length result, not a nearest-neighbor approximation-ratio theorem or a new bound on the final optimum's quality.

## Handoff-derived ingredients

The original programme is the task basis. The prior negative Petersen necklace, its subtour point, and its all-root/all-potential forced-1-tree dominance argument are copied in PREDECESSOR-1TREE-OBSTRUCTION.md and attributed explicitly in the new proof. PREDECESSOR-TREE-DESCENT.md supplies the earlier tree-cut result. PREDECESSOR-STATE-COMPRESSION.md supplies the earlier endpoint-pairing state representation. Relative links within these byte-preserved excerpts point into the original archive and may not resolve in this smaller packet; PROVENANCE.json supplies the exact archive members.
