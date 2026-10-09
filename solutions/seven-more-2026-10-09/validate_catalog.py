#!/usr/bin/env python3
"""Read-only integration gate for the seven-problem research round.

Compare the working tree with the fixed local Git base. All comparisons use the
Python standard library; this program never contacts a remote or edits catalog
files. The optional --output writes only a validation summary.
"""

from collections import Counter, defaultdict
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlsplit


BASE_COMMIT = "b75acbb7671a16ac38e8f41656b92f211dce5f4a"
EXPECTED = {276: "partial", 277: "partial", 964: "proved", 1715: "disproved",
            2305: "proved", 3480: "partial", 3499: "disproved"}
LABELS = {"open": "Open", "partial": "Open, partial results",
          "proved": "Solved here: proved", "disproved": "Solved here: disproved"}
ROUND = "solutions/seven-more-2026-10-09"
RESULT_MARKER = "**Result (2026-10-09).**"
ANCHOR = re.compile(r'^<a id="q(\d+)"></a>\s*$', re.MULTILINE)
TABLE_Q = re.compile(r'^\|\s*\[Q(\d+)\]\(([^)]+)\)\s*\|')
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')


class ValidationError(Exception):
    pass


class Validator:
    def __init__(self, repo, base):
        self.repo = repo.resolve()
        self.base = base
        self.checks = 0
        self._base_blobs = {}
        self.evidence_paths = set()

    def require(self, condition, message):
        self.checks += 1
        if not condition:
            raise ValidationError(message)

    def base_bytes(self, path):
        if path not in self._base_blobs:
            process = subprocess.run(["git", "show", f"{self.base}:{path}"],
                                     cwd=self.repo, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            self.require(process.returncode == 0,
                         f"Cannot read {path} from local base {self.base}: "
                         + process.stderr.decode("utf-8", "replace").strip())
            self._base_blobs[path] = process.stdout
        return self._base_blobs[path]

    def base_text(self, path):
        return self.base_bytes(path).decode("utf-8")

    def text(self, path):
        target = self.repo / path
        self.require(target.is_file(), f"Missing file: {path}")
        return target.read_text(encoding="utf-8")

    def local_reference(self, value, relative_to, label):
        self.require(isinstance(value, str) and bool(value), f"Empty path: {label}")
        parsed = urlsplit(value)
        self.require(not parsed.scheme and not parsed.netloc,
                     f"Expected local evidence path for {label}, got {value!r}")
        target = (relative_to / parsed.path).resolve()
        self.require(target.is_relative_to(self.repo),
                     f"Path escapes repository: {label}: {value}")
        self.require(target.is_file() and target.stat().st_size > 0,
                     f"Missing or empty evidence file: {label}: {value}")
        if parsed.fragment:
            self.require(f'<a id="{parsed.fragment}"></a>' in target.read_text(encoding="utf-8"),
                         f"Missing explicit anchor in {label}: {value}")
        self.evidence_paths.add(target.relative_to(self.repo).as_posix())
        return target

    def json_and_csv(self):
        old = json.loads(self.base_text("data/problems.json"))
        new = json.loads(self.text("data/problems.json"))
        self.require(isinstance(old, list) and isinstance(new, list), "Catalog must be a JSON array")
        old_ids = [x["number"] for x in old]
        new_ids = [x["number"] for x in new]
        self.require(len(set(old_ids)) == len(old_ids), "Duplicate problem ID in base JSON")
        self.require(new_ids == old_ids, "Problem IDs or their ordering changed")
        old_by_id, new_by_id = {x["number"]: x for x in old}, {x["number"]: x for x in new}
        changed = []
        for previous, current in zip(old, new):
            number = previous["number"]
            if previous != current:
                changed.append(number)
            if number not in EXPECTED:
                self.require(current == previous, f"Unselected JSON entry changed: Q{number}")
                continue
            self.require(previous["status"] == "open", f"Selected Q{number} was not open at the base")
            self.require(current["status"] == EXPECTED[number],
                         f"Wrong JSON status for Q{number}: {current['status']!r}")
            self.require(set(current) == set(previous), f"JSON keys added/removed for Q{number}")
            protected = set(previous) - {"status", "results", "ledger"}
            for key in protected:
                self.require(current[key] == previous[key],
                             f"Protected JSON field changed: Q{number}.{key}")
            for key in ("results", "ledger"):
                self.require(isinstance(current[key], list), f"Q{number}.{key} is not a list")
                self.require(current[key][:len(previous[key])] == previous[key],
                             f"Existing {key} history changed for Q{number}")
                self.require(len(current[key]) > len(previous[key]),
                             f"Missing appended {key} evidence for Q{number}")
        self.require(set(changed) == set(EXPECTED), f"Changed JSON IDs are {changed}; expected exactly seven")

        old_reader = csv.DictReader(io.StringIO(self.base_text("data/problems.csv"), newline=""))
        new_reader = csv.DictReader(io.StringIO(self.text("data/problems.csv"), newline=""))
        old_rows, new_rows = list(old_reader), list(new_reader)
        self.require(old_reader.fieldnames == new_reader.fieldnames, "CSV columns changed")
        self.require([x["number"] for x in old_rows] == [x["number"] for x in new_rows],
                     "CSV IDs or ordering changed")
        self.require([int(x["number"]) for x in new_rows] == new_ids, "CSV and JSON IDs/order differ")
        csv_changed = []
        for previous, current in zip(old_rows, new_rows):
            number = int(previous["number"])
            if previous != current:
                csv_changed.append(number)
            self.require(current["status"] == new_by_id[number]["status"],
                         f"CSV/JSON status mismatch for Q{number}")
            allowed = {"status"} if number in EXPECTED else set()
            for key in previous:
                if key not in allowed:
                    self.require(current[key] == previous[key],
                                 f"Protected CSV cell changed: Q{number}.{key}")
        self.require(set(csv_changed) == set(EXPECTED),
                     f"Changed CSV IDs are {csv_changed}; expected exactly seven")
        return old_by_id, new_by_id

    def manifest(self, old, current):
        manifest = json.loads(self.text(f"{ROUND}/RESULTS.json"))
        self.require(manifest.get("date") == "2026-10-09", "Manifest date mismatch")
        self.require(manifest.get("base_commit") == self.base, "Manifest base_commit mismatch")
        records = manifest.get("results")
        self.require(isinstance(records, list) and len(records) == 7, "Manifest must contain exactly seven results")
        self.require({r["number"] for r in records} == set(EXPECTED), "Manifest IDs differ from selected IDs")
        counts = Counter(r["conclusion"] for r in records)
        self.require(dict(counts) == {"partial": 3, "affirmative": 2, "counterexample": 2},
                     f"Unexpected conclusion counts: {dict(counts)}")
        self.require(manifest.get("classification_counts") == dict(counts),
                     "Manifest classification_counts disagree with its results")
        paths = {}
        for record in records:
            number = record["number"]
            self.require(record.get("catalog_status") == EXPECTED[number] == current[number]["status"],
                         f"Manifest/catalog status mismatch for Q{number}")
            conclusion_status = {"partial": "partial", "affirmative": "proved", "counterexample": "disproved"}
            self.require(conclusion_status.get(record["conclusion"]) == EXPECTED[number],
                         f"Conclusion/status mismatch for Q{number}")
            for key in ("title", "result", "boundary", "primary_source", "primary_location", "internal_review"):
                self.require(isinstance(record.get(key), str) and record[key].strip(),
                             f"Missing manifest {key} for Q{number}")
            paths[number] = {}
            for key in ("proof", "review", "checker", "certificate", "source_log"):
                paths[number][key] = self.local_reference(record.get(key), self.repo / ROUND, f"Q{number}.{key}")
            page = record.get("catalog_page")
            self.require(isinstance(page, str) and page.endswith(f"#q{number}"),
                         f"Manifest catalog anchor incorrect for Q{number}")
            paths[number]["catalog_page"] = self.local_reference(page, self.repo, f"Q{number}.catalog_page")

            # Every appended repository result links to real local evidence.
            for result in current[number]["results"][len(old[number]["results"]):]:
                self.require(isinstance(result, dict), f"Malformed result for Q{number}")
                for key in ("proof", "review", "checker", "certificate", "source_log"):
                    if key in result:
                        target = self.local_reference(result[key], self.repo, f"Q{number}.results.{key}")
                        self.require(target == paths[number][key],
                                     f"Manifest/result path mismatch: Q{number}.{key}")
            for ledger in current[number]["ledger"][len(old[number]["ledger"]):]:
                self.require(isinstance(ledger, dict) and ledger.get("status") == EXPECTED[number],
                             f"Appended ledger status mismatch for Q{number}")
                for source in ledger.get("sources", []):
                    url = source.get("url", "")
                    if url and not urlsplit(url).scheme:
                        self.local_reference(url, self.repo, f"Q{number}.ledger.sources")
        return manifest, paths

    @staticmethod
    def blocks(text):
        matches = list(ANCHOR.finditer(text))
        prefix = text[:matches[0].start()] if matches else text
        out = {}
        for i, match in enumerate(matches):
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            number = int(match.group(1))
            if number in out:
                raise ValidationError(f"Repeated detailed anchor Q{number}")
            out[number] = text[match.start():end]
        return prefix, out

    @staticmethod
    def normalize_table_line(line):
        match = TABLE_Q.match(line)
        if not match or int(match.group(1)) not in EXPECTED:
            return line
        cells = line.rsplit("|", 2)
        return cells[0] + "| <STATUS> |" + cells[2]

    @classmethod
    def normalized_prefix(cls, text, counts=False):
        lines = text.splitlines(keepends=True)
        normalized = "".join(cls.normalize_table_line(line) for line in lines)
        if counts:
            normalized = re.sub(r'^\d+ problems?: .*\.$', '<COUNTS>', normalized, flags=re.MULTILINE)
        return normalized

    @staticmethod
    def original_block(block):
        if RESULT_MARKER in block:
            block = block.split(RESULT_MARKER, 1)[0]
        block = re.sub(r'(\*\*Status:\*\* )[^\n·]+', r'\1<STATUS> ', block, count=1)
        return block.rstrip()

    def table_rows(self, text, path, current):
        rows = {}
        for line in text.splitlines():
            match = TABLE_Q.match(line)
            if not match:
                continue
            number = int(match.group(1))
            self.require(number not in rows, f"Duplicate table row Q{number} in {path}")
            self.require(number in current, f"Unknown table ID Q{number} in {path}")
            label = line.rsplit("|", 2)[1].strip()
            self.require(label == LABELS[current[number]["status"]],
                         f"Wrong table status for Q{number} in {path}: {label!r}")
            rows[number] = (match.group(2), line)
        return rows

    def subject_summary(self, text, path, entries):
        match = re.search(r'^(\d+) problems?: (.+)\.$', text, re.MULTILINE)
        self.require(match is not None, f"Missing subject count line: {path}")
        self.require(int(match.group(1)) == len(entries), f"Wrong total in {path}")
        parts = re.findall(r'(\d+) (open, partial results|solved here: proved|solved here: disproved|open)', match.group(2))
        inverse = {"open": "open", "open, partial results": "partial",
                   "solved here: proved": "proved", "solved here: disproved": "disproved"}
        found = Counter()
        for count, label in parts:
            self.require(inverse[label] not in found, f"Repeated count category in {path}")
            found[inverse[label]] = int(count)
        expected = Counter(x["status"] for x in entries)
        self.require(found == expected, f"Wrong subject counts in {path}: {dict(found)} vs {dict(expected)}")

    def markdown(self, old, current, evidence):
        subjects = defaultdict(list)
        for entry in current.values():
            subjects[entry["subject_path"]].append(entry)
        process = subprocess.run(["git", "ls-tree", "-r", "--name-only", self.base, "problems"],
                                 cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.require(process.returncode == 0, "Cannot enumerate local base problem files")
        baseline_paths = process.stdout.splitlines()
        detailed = {}
        subject_rows = {}
        index_rows = {}
        selected_detail_paths = set()
        for path in baseline_paths:
            if not path.endswith(".md") or path in {"problems/README.md", "problems/INDEX.md", "problems/EXCLUDED.md"}:
                continue
            previous, now = self.base_text(path), self.text(path)
            if path.startswith("problems/index/"):
                self.require(self.normalized_prefix(previous) == self.normalized_prefix(now),
                             f"Numeric-index content changed beyond selected statuses: {path}")
                rows = self.table_rows(now, path, current)
                for number, row in rows.items():
                    self.require(number not in index_rows, f"Duplicate numeric-index entry Q{number}")
                    index_rows[number] = (path, row)
                continue

            old_prefix, old_blocks = self.blocks(previous)
            new_prefix, new_blocks = self.blocks(now)
            self.require(list(old_blocks) == list(new_blocks), f"Detailed IDs/order changed in {path}")
            overview_key = path[len("problems/"):-len(".md")]
            is_overview = overview_key in subjects
            self.require(self.normalized_prefix(old_prefix, is_overview) == self.normalized_prefix(new_prefix, is_overview),
                         f"Subject prefix/table changed beyond statuses/counts: {path}")
            if is_overview:
                self.subject_summary(now, path, subjects[overview_key])
                rows = self.table_rows(new_prefix, path, current)
                self.require(set(rows) == {x["number"] for x in subjects[overview_key]},
                             f"Subject overview IDs disagree with JSON: {path}")
                for number, row in rows.items():
                    self.require(number not in subject_rows, f"Duplicate subject-table entry Q{number}")
                    subject_rows[number] = (path, row)

            for number, block in new_blocks.items():
                self.require(number in current, f"Unknown detailed ID Q{number}")
                self.require(number not in detailed, f"Duplicate detailed entry Q{number}")
                detailed[number] = path
                status = re.search(r'^\*\*Status:\*\* ([^\n·]+)', block, re.MULTILINE)
                self.require(status is not None and status.group(1).strip() == LABELS[current[number]["status"]],
                             f"Wrong detailed status for Q{number} in {path}")
                if number not in EXPECTED:
                    self.require(block == old_blocks[number], f"Unselected detailed block changed: Q{number} in {path}")
                    continue
                selected_detail_paths.add(path)
                self.require(RESULT_MARKER not in old_blocks[number], f"Unexpected old result marker for Q{number}")
                self.require(block.count(RESULT_MARKER) == 1, f"Missing/repeated added result block for Q{number}")
                self.require(self.original_block(block) == self.original_block(old_blocks[number]),
                             f"Original statement/context/source/notes changed in Markdown: Q{number}")
                self.require((self.repo / path).resolve() == evidence[number]["catalog_page"],
                             f"Manifest points to wrong detailed page for Q{number}")
                added = block.split(RESULT_MARKER, 1)[1]
                links = set()
                for link in LINK.findall(added):
                    if not urlsplit(link).scheme:
                        links.add(self.local_reference(link, (self.repo / path).parent, f"Q{number} added Markdown link"))
                for key in ("proof", "review", "source_log"):
                    self.require(evidence[number][key] in links, f"Added Q{number} block does not link its {key}")
                self.require(bool({evidence[number]["checker"], evidence[number]["certificate"]} & links),
                             f"Added Q{number} block lacks computational-control link")

        for name, entries in (("detailed entries", detailed), ("subject overview rows", subject_rows), ("numeric-index rows", index_rows)):
            self.require(set(entries) == set(current), f"{name} do not cover the exact catalog IDs")
        for number in EXPECTED:
            for kind, entries in (("subject", subject_rows), ("numeric index", index_rows)):
                path, (target, _) = entries[number]
                expected_target = (self.repo / detailed[number]).resolve()
                actual = self.local_reference(target, (self.repo / path).parent, f"Q{number} {kind} link")
                self.require(actual == expected_target and target.endswith(f"#q{number}"),
                             f"Wrong Q{number} target in {path}")

        # The numeric range counts and exclusions are unaffected by this round.
        for path in ("problems/INDEX.md", "problems/EXCLUDED.md"):
            self.require(self.text(path) == self.base_text(path), f"Unrelated catalog index/exclusion file changed: {path}")
        self.subject_index(subjects)
        return {"detailed_entries": len(detailed), "subject_table_rows": len(subject_rows),
                "numeric_index_rows": len(index_rows), "subject_overviews": len(subjects),
                "selected_detail_pages": sorted(selected_detail_paths)}

    def subject_index(self, subjects):
        path = "problems/README.md"
        previous, now = self.base_text(path), self.text(path)
        pattern = re.compile(r'^\|\s*([^|]+?)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*$')
        found = set()
        for line in now.splitlines():
            match = pattern.match(line)
            if not match:
                continue
            subject = match.group(3).removesuffix(".md")
            self.require(subject in subjects and subject not in found, f"Unknown/duplicate subject summary {subject}")
            found.add(subject)
            statuses = Counter(x["status"] for x in subjects[subject])
            expected = (len(subjects[subject]), statuses["open"], statuses["partial"], statuses["proved"] + statuses["disproved"])
            actual = tuple(map(int, match.groups()[3:]))
            self.require(actual == expected, f"Subject-index counts wrong for {subject}: {actual} vs {expected}")
        self.require(found == set(subjects), "Subject index has missing categories")
        affected = {x["subject_path"] for group in subjects.values() for x in group if x["number"] in EXPECTED}
        def normalized(text):
            lines = []
            for line in text.splitlines(keepends=True):
                match = pattern.match(line)
                if match and match.group(3).removesuffix(".md") in affected:
                    prefix = line.rsplit("|", 5)[0]
                    line = prefix + "| <COUNTS> |\n"
                lines.append(line)
            return "".join(lines)
        self.require(normalized(previous) == normalized(now), "Subject index changed beyond the four affected count rows")

    def top_counts(self, current):
        text = self.text("README.md")
        counts = Counter(x["status"] for x in current.values())
        self.require(counts == Counter({"open": 3442, "partial": 96, "proved": 35, "disproved": 15}),
                     f"Unexpected overall catalog status counts: {dict(counts)}")
        cells = {}
        for line in text.splitlines():
            match = re.fullmatch(r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', line)
            if match:
                cells[match.group(1)] = match.group(2)
        expected = {"Problems in the catalog": str(len(current)), "Open": str(counts["open"]),
                    "Open, with partial results here": str(counts["partial"]),
                    "Solved here": f"{counts['proved'] + counts['disproved']} ({counts['proved']} proved, {counts['disproved']} disproved)"}
        for name, count in expected.items():
            self.require(cells.get(name) == count, f"README total {name!r} is {cells.get(name)!r}, expected {count!r}")
        lead = re.search(r'A catalog of \*\*(\d+) open mathematical problems\*\*', text)
        self.require(lead is not None and int(lead.group(1)) == len(current), "README leading catalog total mismatch")
        return dict(counts)

    def protected_data(self):
        process = subprocess.run(["git", "ls-tree", "-r", "--name-only", self.base, "data"],
                                 cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.require(process.returncode == 0, "Cannot enumerate base data files")
        protected = []
        for path in process.stdout.splitlines():
            if path in {"data/problems.json", "data/problems.csv"}:
                continue
            self.require((self.repo / path).read_bytes() == self.base_bytes(path), f"Protected data file changed: {path}")
            protected.append(path)
        return protected

    def run(self):
        self.require(self.base == BASE_COMMIT, "This round's validation base must not be changed")
        old, current = self.json_and_csv()
        manifest, evidence = self.manifest(old, current)
        markdown = self.markdown(old, current, evidence)
        counts = self.top_counts(current)
        protected = self.protected_data()
        evidence_hashes = {path: hashlib.sha256((self.repo / path).read_bytes()).hexdigest()
                           for path in sorted(self.evidence_paths)}
        return {"date": "2026-10-09", "base_commit": self.base, "all_passed": True,
                "validation_scope": "Catalog integration and evidence linkage; does not establish mathematical correctness or novelty",
                "changed_problem_statuses": {str(k): v for k, v in EXPECTED.items()},
                "catalog_entries": len(current), "catalog_counts": counts,
                "manifest_entries": len(manifest["results"]), "markdown": markdown,
                "protected_data_files": protected, "evidence_sha256": evidence_hashes,
                "checks_completed": self.checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write this validation summary JSON (optional)")
    args = parser.parse_args()
    validator = Validator(Path(__file__).resolve().parents[2], BASE_COMMIT)
    try:
        report = validator.run()
    except (ValidationError, KeyError, ValueError, OSError, TypeError) as error:
        report = {"date": "2026-10-09", "base_commit": BASE_COMMIT, "all_passed": False,
                  "error": str(error), "checks_completed": validator.checks}
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.output is not None:
        # Explicitly prevent the optional output from replacing a catalog file.
        output = args.output.resolve()
        round_dir = (validator.repo / ROUND).resolve()
        if not output.is_relative_to(round_dir) or output.name != "validation-summary.json":
            parser.error("--output must name validation-summary.json inside this research round")
        output.write_text(rendered, encoding="utf-8")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
