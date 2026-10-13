#!/usr/bin/env python3
"""Merge reviewed per-target outcomes; refuse to call unfinished work complete."""
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
FOUNDATIONS = {"Q1375", "Q1376", "Q1377", "Q1378", "Q1481", "Q1979"}
PACKETS = {
    **{q: "arithmetic/ATTEMPTS.md" for q in (
        "Q2978", "Q2979", "Q2980", "Q2981", "Q2982",
        "Q2990", "Q2991", "Q2992", "Q2993")},
    **{q: "model-theory/ATTEMPTS.md" for q in (
        "Q246", "Q2169", "Q2170", "Q3268", "Q3482")},
    **{q: "graphs/ATTEMPTS.md" for q in ("Q3075", "Q3076", "Q3077", "Q3079")},
    "Q3206": "anti-recurrence/ATTEMPTS.md",
    "Q3668": "proof-complexity/ATTEMPTS.md",
    "Q3824": "proof-complexity/ATTEMPTS.md",
    "Q2778": "gp2/Q2778-ATTEMPTS.md",
    "A-TAIL": "fourier/DISTRIBUTION.md",
    "A-ENTROPY": "fourier/ENTROPY.md",
}
SOLUTIONS = {
    "Q2168": ("retained_solution", "model-theory/ATTEMPTS.md"),
    "Q2777": ("solved_locally", "gp2/Q2777-RESULT.md"),
    "A-ONES": ("solved_locally", "fourier/ALL-ONES.md"),
    "A-PROOF-LANE": ("solved_locally", "automatic-proofs/RESULT.md"),
}


def routes(q, path):
    text = (HERE / path).read_text()
    if q.startswith("Q") and q not in {"Q2778", "Q3206"}:
        text = re.split(r"(?m)^## " + q + r"(?:\s|:| —)", text, maxsplit=1)[1]
        text = re.split(r"(?m)^## ", text, maxsplit=1)[0]
    if q == "Q2778":
        names = re.findall(r"(?m)^## A([1-5])\. (.*)$", text)
    else:
        names = re.findall(r"(?m)^([1-5])\. \*\*([^*]+)\*\*", text)
    assert len(names) == 5, (q, names)
    return [{"attempt": int(n), "route": title.rstrip("."),
             "outcome": "full_target_failure", "evidence": path,
             "section": q, "review": "ROOT-REVIEW.md"} for n, title in names]


def main():
    status = json.loads((HERE / "STATUS.json").read_text())
    for t in status["targets"]:
        q = t["target"]
        if q in SOLUTIONS:
            state, proof = SOLUTIONS[q]
            t.update(status=state, consecutive_failures=0, evidence=[proof],
                     attempts=[{"attempt": 1, "outcome": "retained_proof_audited"
                                if q == "Q2168" else "solution",
                                "evidence": proof}])
        elif q in PACKETS:
            t.update(status="failure_limit", consecutive_failures=5,
                     attempts=routes(q, PACKETS[q]), evidence=[PACKETS[q]])
    paths = [HERE / "foundations/STATUS.json", HERE / "foundations/ROOT-STATUS.json"]
    review_path = HERE / "foundations/ROOT-REVIEW.json"
    reviewed = json.loads(review_path.read_text()).get("accepted_targets", []) if review_path.exists() else []
    if all(p.exists() for p in paths):
        entries = []
        for foundation_path in paths:
            supplied = json.loads(foundation_path.read_text())
            part = supplied.get("targets", supplied)
            if isinstance(part, dict):
                part = [dict(v, target=k) for k, v in part.items()]
            entries += part
        by_id = {t["target"]: t for t in entries}
        assert set(by_id) == FOUNDATIONS and len(entries) == len(FOUNDATIONS)
        for t in status["targets"]:
            if t["target"] in FOUNDATIONS:
                entry = by_id[t["target"]]
                if entry.get("root_review_accepted") or t["target"] in reviewed:
                    t.update({k: v for k, v in entry.items()
                              if k not in ("statement_id", "text", "source")})
                    t["root_review_accepted"] = True
                    if t["status"] == "failure_limit_pending_review":
                        t["status"] = "failure_limit"
    terminal = {"solved_locally", "retained_solution", "failure_limit"}
    done = all(t["status"] in terminal for t in status["targets"])
    status["overall_state"] = ("complete_under_stopping_rule" if done
                               else "foundations_in_progress")
    status["counts"] = {k: sum(t["status"] == k for t in status["targets"])
                        for k in sorted(terminal | {"active"})}
    status["partial_results_do_not_reset_counters"] = True
    (HERE / "STATUS.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(status["counts"]))


if __name__ == "__main__":
    main()
