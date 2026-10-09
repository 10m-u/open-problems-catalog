#!/usr/bin/env python3
"""Validate this round's catalog integration; never edit the catalog.

Run from any directory with Python 3.10+ and Git. The sole output file is
catalog-validation.json beside this script. Its contents are deterministic
for a given set of inputs: there are no timestamps or absolute local paths.

This integration check needs the base Git commit below. Source-archive users
need a clone containing that history only to run this validator; the separate
mathematical checkers do not require Git history. This script checks records
and evidence links, not the truth of the mathematical claims.
"""

from collections import Counter, defaultdict
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROUND = Path(__file__).resolve().parent
REPO = ROUND.parents[1]
BASE = "368ce0d95a90c073be730b27c724133ce31666f0"
EXPECTED = {
    132: "partial",
    256: "proved",
    257: "partial",
    3101: "partial",
    3102: "disproved",
    3286: "proved",
    3287: "proved",
}
COUNTS = {"open": 3449, "partial": 93, "proved": 33, "disproved": 13}
DISPLAY = {
    "open": "Open",
    "partial": "Open, partial results",
    "proved": "Solved here: proved",
    "disproved": "Solved here: disproved",
}
EVIDENCE_FIELDS = ("proof", "review", "checker", "certificate", "source_log")


class ValidationError(Exception):
    """An integration requirement failed."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def canonical(value):
    """Compare JSON values with types and list order preserved."""
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False)


def base_bytes(relative):
    try:
        result = subprocess.run(
            ["git", "show", f"{BASE}:{relative}"], cwd=REPO,
            check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        raise ValidationError("Git is required for the integration validator.") from exc
    require(result.returncode == 0,
            f"Cannot read {relative} at base commit {BASE}. This integration "
            "validator needs a Git clone containing the base commit. The "
            "mathematical checkers remain runnable from a source archive.")
    return result.stdout


def local_link(reference, directory, boundary=REPO):
    """Resolve a required local file link and retain its URL fragment."""
    require(isinstance(reference, str) and reference,
            "A required local evidence reference is empty or not a string.")
    parsed = urlsplit(reference)
    require(not parsed.scheme and not parsed.netloc and not parsed.query,
            f"Expected a local file reference: {reference}")
    require(bool(parsed.path) and not Path(unquote(parsed.path)).is_absolute(),
            f"Expected a relative file reference: {reference}")
    path = (directory / unquote(parsed.path)).resolve()
    require(path.is_relative_to(boundary),
            f"Reference escapes its permitted directory: {reference}")
    require(path.is_file(), f"Linked file is missing: {reference}")
    return path, unquote(parsed.fragment)


def read_csv(contents, label):
    reader = csv.DictReader(io.StringIO(contents.decode("utf-8"), newline=""))
    fields = reader.fieldnames
    require(fields is not None and len(fields) == len(set(fields)),
            f"Invalid or duplicate CSV headers in {label}.")
    require("number" in fields and "status" in fields,
            f"Missing number/status CSV columns in {label}.")
    rows = list(reader)
    require(all(None not in row and all(value is not None for value in row.values())
                for row in rows), f"Malformed CSV row in {label}.")
    require(len({row["number"] for row in rows}) == len(rows),
            f"Duplicate CSV numbers in {label}.")
    return fields, rows


def validate_json(current, previous):
    require(isinstance(current, list) and isinstance(previous, list),
            "Both problem JSON files must contain a list.")
    require(all(isinstance(row, dict) and type(row.get("number")) is int
                for row in current + previous), "Invalid JSON problem number.")
    numbers = [row["number"] for row in current]
    require(numbers == [row["number"] for row in previous],
            "Problem numbers or JSON row order changed.")
    require(len(numbers) == len(set(numbers)) == sum(COUNTS.values()),
            "Duplicate numbers or unexpected catalog size.")
    changes = {}
    for old, new in zip(previous, current):
        number = new["number"]
        require(set(old) == set(new), f"JSON field set changed for Q{number}.")
        changed = sorted(key for key in old if canonical(old[key]) != canonical(new[key]))
        if changed:
            changes[number] = changed
            require(set(changed) <= {"status", "results", "ledger"},
                    f"Unauthorized metadata changes for Q{number}: {changed}")
        if number in EXPECTED:
            require(old["status"] == "open" and old["provisional"] is False,
                    f"Q{number} was not open and nonprovisional at the base.")
            require(not old["results"] and not old["ledger"],
                    f"Q{number} had a preexisting linked result or ledger.")
            require(new["status"] == EXPECTED[number],
                    f"Unexpected new catalog status for Q{number}.")
            require(isinstance(new["results"], list) and new["results"] and
                    isinstance(new["ledger"], list) and new["ledger"],
                    f"Missing new result or ledger for Q{number}.")
    require(sorted(changes) == list(EXPECTED),
            f"Changed problem numbers are {sorted(changes)}, expected {list(EXPECTED)}.")
    require(dict(Counter(row["status"] for row in current)) == COUNTS,
            "Unexpected global catalog status counts.")
    return changes


def validate_csv(current_bytes, previous_bytes, records):
    fields, current = read_csv(current_bytes, "working tree")
    old_fields, previous = read_csv(previous_bytes, "base commit")
    require(fields == old_fields, "CSV headers or column order changed.")
    require([row["number"] for row in current] == [row["number"] for row in previous],
            "CSV problem numbers or row order changed.")
    require([row["number"] for row in current] == [str(row["number"]) for row in records],
            "JSON and CSV problem numbers or row order differ.")
    changed_numbers = []
    for old, new, record in zip(previous, current, records):
        number = record["number"]
        changed = [field for field in fields if old[field] != new[field]]
        require(changed == (["status"] if number in EXPECTED else []),
                f"Unexpected CSV changes for Q{number}: {changed}")
        require(new["status"] == record["status"],
                f"JSON/CSV status disagreement for Q{number}.")
        if changed:
            changed_numbers.append(number)
    require(changed_numbers == list(EXPECTED), "Unexpected set of CSV status changes.")
    return len(fields)


def validate_manifest(manifest, records):
    require(manifest.get("base_commit") == BASE, "RESULTS.json has a different base commit.")
    require(manifest.get("selected_numbers") == list(EXPECTED),
            "RESULTS.json selected_numbers do not match this round.")
    require(manifest.get("catalog_status_counts") == dict(Counter(EXPECTED.values())),
            "RESULTS.json has inconsistent selected status counts.")
    entries = manifest.get("results")
    require(isinstance(entries, list) and len(entries) == len(EXPECTED),
            "RESULTS.json must contain seven result entries.")
    require(all(isinstance(item, dict) and type(item.get("number")) is int for item in entries),
            "Invalid result record or number in RESULTS.json.")
    require(sorted(item["number"] for item in entries) == list(EXPECTED),
            "RESULTS.json entries are missing, duplicated, or outside the selected set.")
    by_number = {row["number"]: row for row in records}
    evidence = set()
    resolved = {}
    for entry in entries:
        number = entry["number"]
        record = by_number[number]
        require(entry.get("catalog_status") == EXPECTED[number],
                f"RESULTS.json catalog status differs for Q{number}.")
        for manifest_key, original in (
                ("statement_ids", record["statement_ids"]),
                ("primary_source", record["source"]["primary_source"]),
                ("source_location", record["location"])):
            require(canonical(entry.get(manifest_key)) == canonical(original),
                    f"RESULTS.json changes original {manifest_key} for Q{number}.")
        paths = {}
        for field in EVIDENCE_FIELDS:
            path, _ = local_link(entry.get(field), ROUND, ROUND)
            paths[field] = path
            evidence.add(path)
        page, anchor = local_link(entry.get("problem_page"), REPO)
        require(anchor == f"q{number}", f"Wrong problem-page anchor for Q{number}.")
        paths["problem_page"] = page
        paths["anchor"] = anchor
        resolved[number] = paths
        result_links = set()
        for result in record["results"]:
            for field in ("proof", "review"):
                path, _ = local_link(result.get(field), REPO)
                require(path == paths[field],
                        f"Catalog result {field} disagrees with RESULTS.json for Q{number}.")
                result_links.add(path)
            require((REPO / "solutions" / result["folder"]).resolve() == ROUND,
                    f"Catalog result folder is inconsistent for Q{number}.")
        require({paths["proof"], paths["review"]} <= result_links,
                f"Missing catalog result proof/review links for Q{number}.")
        ledger_links = set()
        for entry_ledger in record["ledger"]:
            require(entry_ledger.get("status") == EXPECTED[number],
                    f"Catalog ledger status disagrees for Q{number}.")
            sources = entry_ledger.get("sources")
            require(isinstance(sources, list) and sources,
                    f"No ledger sources for Q{number}.")
            for source in sources:
                reference = source.get("url")
                require(isinstance(reference, str) and reference,
                        f"Invalid ledger source for Q{number}.")
                if not urlsplit(reference).scheme:
                    path, _ = local_link(reference, REPO)
                    ledger_links.add(path)
        require({paths["proof"], paths["review"]} <= ledger_links,
                f"Ledger does not link the proof and review for Q{number}.")
    return resolved, evidence


def validate_summaries(records):
    groups = defaultdict(list)
    for row in records:
        groups[row["subject_path"]].append(row)
    text = (REPO / "problems/README.md").read_text(encoding="utf-8")
    summary_rows = re.findall(
        r"^\| [^|]+ \| \[([^\]]+)\]\(([^)]+)\) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$",
        text, re.MULTILINE,
    )
    require(len(summary_rows) == len(groups), "Subject summary table has an unexpected size.")
    seen = set()
    for label, link, total, opened, partial, solved in summary_rows:
        path, _ = local_link(link, REPO / "problems")
        key = path.relative_to(REPO / "problems").with_suffix("").as_posix()
        require(key in groups and key not in seen, f"Unexpected or duplicate subject row: {key}")
        seen.add(key)
        rows = groups[key]
        count = Counter(row["status"] for row in rows)
        require(label == rows[0]["subject"], f"Subject label differs for {key}.")
        require(tuple(map(int, (total, opened, partial, solved))) ==
                (len(rows), count["open"], count["partial"], count["proved"] + count["disproved"]),
                f"Subject summary counts differ for {key}.")
        expected = f"{len(rows)} problems: " + ", ".join(
            f"{count[status]} {display.lower()}" for status, display in DISPLAY.items()
            if count[status]
        ) + "."
        actual = re.findall(r"^\d+ problems:.*\.$", path.read_text(encoding="utf-8"), re.MULTILINE)
        require(actual == [expected], f"Subject-page summary differs for {key}.")
    require(seen == set(groups), "A subject is missing from the summary table.")
    root_readme = (REPO / "README.md").read_text(encoding="utf-8")
    for line in (
            f"| Problems in the catalog | {len(records)} |",
            f"| Open | {COUNTS['open']} |",
            f"| Open, with partial results here | {COUNTS['partial']} |",
            f"| Solved here | {COUNTS['proved'] + COUNTS['disproved']} "
            f"({COUNTS['proved']} proved, {COUNTS['disproved']} disproved) |"):
        require(line in root_readme.splitlines(), f"Root README count differs: {line}")
    return len(groups)


def validate_pages(records, resolved):
    by_number = {row["number"]: row for row in records}
    index_pages = sorted((REPO / "problems/index").glob("*.md"))
    require(index_pages, "No numbered index pages found.")
    index_text = {path: path.read_text(encoding="utf-8") for path in index_pages}
    for number, status in EXPECTED.items():
        paths = resolved[number]
        page = paths["problem_page"]
        text = page.read_text(encoding="utf-8")
        require(text.count(f'<a id="q{number}"></a>') == 1,
                f"Missing or duplicate HTML problem anchor for Q{number}.")
        blocks = re.findall(rf"^## Q{number}\..*?(?=^## Q\d+\.|\Z)", text,
                            re.MULTILINE | re.DOTALL)
        require(len(blocks) == 1, f"Missing or duplicate problem heading for Q{number}.")
        block = blocks[0]
        statuses = re.findall(r"^\*\*Status:\*\*\s*([^·\n]+)", block, re.MULTILINE)
        require([value.strip() for value in statuses] == [DISPLAY[status]],
                f"Problem-page status differs for Q{number}.")
        require("**Result (2026-10-09).**" in block, f"Missing new result text for Q{number}.")
        links = set()
        for reference in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", block):
            parsed = urlsplit(reference)
            if not parsed.scheme and parsed.path:
                path, _ = local_link(reference, page.parent)
                links.add(path)
        require({paths["proof"], paths["review"], paths["certificate"]} <= links,
                f"Problem page does not link the proof, review, and controls for Q{number}.")
        subject = REPO / "problems" / (by_number[number]["subject_path"] + ".md")
        for label, pages in (("subject", {subject: subject.read_text(encoding="utf-8")}),
                             ("numbered index", index_text)):
            matches = []
            pattern = rf"^\| \[Q{number}\]\(([^)]+)\) \|.*\|\s*$"
            for containing_page, contents in pages.items():
                for match in re.finditer(pattern, contents, re.MULTILINE):
                    matches.append((containing_page, match))
            require(len(matches) == 1, f"Q{number} is missing or duplicated in its {label}.")
            containing_page, match = matches[0]
            displayed = match.group(0).rsplit("|", 2)[1].strip()
            require(displayed == DISPLAY[status], f"Wrong {label} status for Q{number}.")
            target, anchor = local_link(match.group(1), containing_page.parent)
            require(target == page and anchor == f"q{number}",
                    f"Wrong {label} problem-page link for Q{number}.")
    return len(index_pages)


def main():
    report = {
        "base_commit": BASE,
        "scope": "Catalog integration and local evidence links; no mathematical proof certification.",
        "passed": False,
        "checks_passed": [],
    }
    try:
        current_json = (REPO / "data/problems.json").read_bytes()
        current_csv = (REPO / "data/problems.csv").read_bytes()
        old_json = base_bytes("data/problems.json")
        old_csv = base_bytes("data/problems.csv")
        records, previous = json.loads(current_json), json.loads(old_json)
        changes = validate_json(records, previous)
        report["checks_passed"].append("Exactly seven JSON records changed; only status/results/ledger changed.")
        report["changed_fields"] = {str(number): fields for number, fields in changes.items()}
        report["csv_columns"] = validate_csv(current_csv, old_csv, records)
        report["checks_passed"].append("All JSON/CSV numbers and statuses match; only seven CSV status cells changed.")
        manifest_path = ROUND / "RESULTS.json"
        manifest = json.loads(manifest_path.read_bytes())
        resolved, evidence = validate_manifest(manifest, records)
        report["checks_passed"].append("Seven manifest records preserve source metadata and resolve all evidence, result, and ledger links.")
        report["subjects_checked"] = validate_summaries(records)
        report["checks_passed"].append("All subject summary tables and root README counts agree with the catalog.")
        report["index_pages_scanned"] = validate_pages(records, resolved)
        report["checks_passed"].append("Selected subject/index rows, problem statuses, anchors, and proof/review/control links agree.")
        report["catalog_size"] = len(records)
        report["catalog_status_counts"] = COUNTS
        report["selected_numbers"] = list(EXPECTED)
        report["selected_statuses"] = {str(number): status for number, status in EXPECTED.items()}
        report["unique_evidence_files"] = len(evidence)
        inputs = evidence | {REPO / "data/problems.json", REPO / "data/problems.csv", manifest_path}
        report["sha256"] = {
            path.relative_to(REPO).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in sorted(inputs)
        }
        report["passed"] = True
    except (ValidationError, OSError, ValueError, KeyError, TypeError) as exc:
        report["error"] = str(exc)
    output = ROUND / "catalog-validation.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
                      encoding="utf-8")
    if report["passed"]:
        print(f"PASS: {len(EXPECTED)} selected records; {report['catalog_size']} catalog entries; "
              f"{report['subjects_checked']} subjects; {report['unique_evidence_files']} evidence files.")
    else:
        print("FAIL: " + report["error"], file=sys.stderr)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
