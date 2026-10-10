#!/usr/bin/env python3
"""Focused integrity gate for the seven-selected-2026-10-10 catalog update.

Read-only apart from an explicitly requested JSON report. No research checker,
network request, repository mutation, or historic test suite is run.
"""
from collections import Counter, defaultdict
import argparse
import csv
from functools import lru_cache
import io
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

BASE = '322939ded7f14279544590a46e7917abbcc96942'
ROUND = 'seven-selected-2026-10-10'
ROOT = Path(__file__).resolve().parents[2]
ROUND_DIR = ROOT / 'solutions' / ROUND
EXPECTED = {212: 'disproved', 726: 'proved', 3840: 'partial', 3841: 'partial',
            3893: 'proved', 3982: 'proved', 3983: 'proved'}
LABELS = {'open': 'Open', 'partial': 'Open, partial results',
          'proved': 'Solved here: proved', 'disproved': 'Solved here: disproved'}
ALLOWED_FIELDS = {'status', 'results', 'ledger', 'status_notes'}
PENDING_REPORT = None


class ValidationError(Exception):
    pass


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def read(path):
    return path.read_text(encoding='utf-8')


@lru_cache(maxsize=None)
def base_text(path):
    result = subprocess.run(['git', 'show', BASE + ':' + path], cwd=ROOT,
                            text=True, encoding='utf-8', capture_output=True)
    require(result.returncode == 0, 'cannot read frozen base file: ' + path)
    return result.stdout


def unique_entries(entries, source):
    require(isinstance(entries, list), source + ' must be an array')
    numbers = [entry['number'] for entry in entries]
    require(all(type(n) is int for n in numbers), source + ' has a noninteger number')
    require(len(set(numbers)) == len(numbers), source + ' has duplicate numbers')
    return {entry['number']: entry for entry in entries}


def csv_entries(text):
    reader = csv.DictReader(io.StringIO(text))
    rows = list(reader)
    numbers = [int(row['number']) for row in rows]
    require(len(set(numbers)) == len(numbers), 'CSV has duplicate numbers')
    return reader.fieldnames, rows, {int(row['number']): row for row in rows}


def blocks(text):
    starts = list(re.finditer(r'^## Q(\d+)\. (.*)$', text, re.M))
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        yield int(match.group(1)), text[match.start():end]


def block_status(block):
    match = re.search(r'^\*\*Status:\*\* (.*?) · \*\*Kind:', block, re.M)
    require(match is not None, 'missing detail-page status')
    return match.group(1)


def statement_paragraph(block):
    match = re.search(r'^\*\*Status:\*\*[^\n]*\n\s*\n', block, re.M)
    require(match is not None, 'missing detail-page statement boundary')
    return block[match.end():].split('\n\n', 1)[0]


def numbered_table(text):
    for line in text.splitlines():
        if not line.startswith('|'):
            continue
        match = re.search(r'\[Q(\d+)\]\(([^)]+)\)', line)
        if match:
            yield int(match.group(1)), match.group(2), line.rsplit('|', 2)[-2].strip()


def file_path(target, owner=ROOT / 'README.md'):
    target = re.sub(r'\\([\\`*_{}\[\]()#+.!<> -])', r'\1', target)
    parsed = urlsplit(target)
    require(not parsed.scheme and not parsed.netloc, 'expected local artifact: ' + target)
    if parsed.path.startswith('/'):
        path = ROOT / unquote(parsed.path).lstrip('/')
    else:
        path = owner.parent / unquote(parsed.path) if parsed.path else owner
    path = path.resolve()
    require(path.is_relative_to(ROOT), 'local target escapes repository: ' + target)
    require(path.exists() or path == PENDING_REPORT,
            'missing local target: ' + str(path.relative_to(ROOT)))
    return path, unquote(parsed.fragment)


def artifact_paths(value, key, number):
    paths = [value] if isinstance(value, str) else value
    require(isinstance(paths, list) and paths and all(isinstance(p, str) and p for p in paths),
            f'Q{number} manifest {key} must be a path or nonempty path list')
    for target in paths:
        path, _ = file_path(target)
        require(path.is_file(), f'Q{number} {key} is not a file: {target}')
        yield path


def remove_fences(text):
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return '\n'.join(lines)


def markdown_targets(text):
    """Inline links/images with balanced URL parentheses, plus references/HTML."""
    text = remove_fences(text)
    text = re.sub(r'(`+).*?\1', '', text)
    for match in re.finditer(r'!?\[[^\]\n]*\]\(\s*', text):
        start = match.end()
        if start < len(text) and text[start] == '<':
            end = text.find('>', start + 1)
            if end >= 0:
                yield text[start + 1:end]
            continue
        depth, cursor = 1, start
        while cursor < len(text):
            character = text[cursor]
            if character == '\\':
                cursor += 2
                continue
            if character == '(':
                depth += 1
            elif character == ')':
                depth -= 1
                if not depth:
                    yield text[start:cursor].split()[0] if text[start:cursor].split() else ''
                    break
            elif character.isspace() and depth == 1:
                yield text[start:cursor]
                break
            cursor += 1
    for match in re.finditer(r'^\s{0,3}\[[^\]\n]+\]:\s*(?:<([^>]+)>|(\S+))', text, re.M):
        yield match.group(1) or match.group(2)
    for match in re.finditer(r'\b(?:href|src)=[\"\']([^\"\']+)[\"\']', text):
        yield match.group(1)


@lru_cache(maxsize=None)
def markdown_anchors(path):
    text = read(path)
    anchors = set(re.findall(r'\bid=[\"\']([^\"\']+)[\"\']', text))
    seen = Counter()
    for match in re.finditer(r'^#{1,6}\s+(.+?)\s*#*$', remove_fences(text), re.M):
        heading = re.sub(r'<[^>]*>', '', match.group(1))
        heading = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading)
        slug = ''.join(c for c in heading.lower() if c.isalnum() or c in '_- ')
        slug = slug.replace(' ', '-')
        suffix = '' if seen[slug] == 0 else '-' + str(seen[slug])
        anchors.add(slug + suffix)
        seen[slug] += 1
    return anchors


def check_link(target, owner):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return False
    path, fragment = file_path(target, owner)
    if fragment:
        if re.fullmatch(r'L\d+(?:-L\d+)?', fragment):
            numbers = list(map(int, re.findall(r'\d+', fragment)))
            require(path.is_file() and min(numbers) >= 1 and max(numbers) <= len(read(path).splitlines()),
                    'invalid local line anchor: ' + target)
        elif path.suffix.lower() == '.md':
            require(fragment in markdown_anchors(path), 'missing Markdown anchor: ' + target)
        else:
            require(path.is_file() and fragment in set(re.findall(r'\bid=[\"\']([^\"\']+)[\"\']', read(path))),
                    'unresolved local anchor: ' + target)
    return True


def validate():
    manifest = json.loads(read(ROUND_DIR / 'RESULTS.json'))
    require(manifest.get('base_commit') == BASE, 'manifest base_commit is not the frozen base')
    require(manifest.get('round') == ROUND, 'manifest round differs')
    results = unique_entries(manifest.get('results'), 'manifest results')
    require(set(results) == set(EXPECTED), 'manifest must contain exactly the seven selected IDs')
    for number, entry in results.items():
        require(entry.get('status') == EXPECTED[number], f'wrong manifest status for Q{number}')
        for field in ('title', 'scope', 'limits'):
            require(isinstance(entry.get(field), str) and entry[field].strip(), f'Q{number} lacks {field}')

    base = json.loads(base_text('data/problems.json'))
    current = json.loads(read(ROOT / 'data/problems.json'))
    old, new = unique_entries(base, 'base JSON'), unique_entries(current, 'current JSON')
    require([p['number'] for p in base] == [p['number'] for p in current], 'catalog ID order or membership changed')
    changed = {number for number in old if old[number] != new[number]}
    require(changed == set(EXPECTED), 'JSON changed IDs differ: ' + str(sorted(changed)))
    changed_fields = {}
    missing = object()
    for number in EXPECTED:
        fields = {key for key in old[number].keys() | new[number].keys()
                  if old[number].get(key, missing) != new[number].get(key, missing)}
        require(fields <= ALLOWED_FIELDS, f'Q{number} changed forbidden fields: {sorted(fields - ALLOWED_FIELDS)}')
        require(new[number]['status'] == EXPECTED[number], f'wrong JSON status for Q{number}')
        require(old[number]['text'] == new[number]['text'], f'Q{number} statement changed')
        require(new[number].get('results') or new[number].get('ledger'), f'Q{number} has no recorded result')
        changed_fields[str(number)] = sorted(fields)

    old_headers, old_rows, old_csv = csv_entries(base_text('data/problems.csv'))
    headers, rows, current_csv = csv_entries(read(ROOT / 'data/problems.csv'))
    require(headers == old_headers, 'CSV header changed')
    require([row['number'] for row in rows] == [row['number'] for row in old_rows], 'CSV row order or membership changed')
    require(set(current_csv) == set(new), 'CSV and JSON ID sets differ')
    for number, row in current_csv.items():
        require(row['status'] == new[number]['status'], f'CSV/JSON status mismatch at Q{number}')
        for key in headers:
            if key != 'status' or number not in EXPECTED:
                require(row[key] == old_csv[number][key], f'CSV changed Q{number} field {key}')

    # Every detail status, overview status, and numeric-index status is checked.
    full, indexes, overviews = {}, {}, {}
    for path in sorted((ROOT / 'problems').glob('*/*.md')):
        if path.parent.name == 'index':
            for number, target, status in numbered_table(read(path)):
                require(number not in indexes, f'duplicate numeric index Q{number}')
                indexes[number] = (path, target, status)
        else:
            for number, block in blocks(read(path)):
                require(number not in full, f'duplicate full detail Q{number}')
                full[number] = (path, block)
    require(set(full) == set(new), 'detail-page IDs differ from JSON')
    require(set(indexes) == set(new), 'numeric-index IDs differ from JSON')
    by_subject = defaultdict(list)
    for entry in current:
        by_subject[entry['subject_path']].append(entry)
    subject_counts = {}
    subject_table = read(ROOT / 'problems/README.md')
    for subject, entries in sorted(by_subject.items()):
        path = ROOT / 'problems' / (subject + '.md')
        text = read(path)
        counts = Counter(entry['status'] for entry in entries)
        subject_counts[subject] = dict(counts)
        match = re.search(r'^(\d+) problems: (.*)\.$', text, re.M)
        require(match is not None and int(match.group(1)) == len(entries), 'wrong subject total: ' + subject)
        phrases = re.findall(r'(\d+) (open, partial results|solved here: proved|solved here: disproved|open)', match.group(2))
        parsed_counts = {next(key for key, label in LABELS.items() if label.lower() == phrase): int(count)
                         for count, phrase in phrases}
        require(parsed_counts == {key: value for key, value in counts.items() if value}, 'wrong subject status counts: ' + subject)
        pattern = r'^\|[^\n]*\]\(' + re.escape(subject + '.md') + r'\) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|$'
        summary = re.search(pattern, subject_table, re.M)
        expected_summary = (len(entries), counts['open'], counts['partial'], counts['proved'] + counts['disproved'])
        require(summary is not None and tuple(map(int, summary.groups())) == expected_summary,
                'wrong all-subject summary row: ' + subject)
        seen = set()
        for number, target, status in numbered_table(text):
            require(number not in seen, f'duplicate subject overview Q{number}')
            seen.add(number)
            require(number not in overviews, f'Q{number} occurs in two subject overviews')
            overviews[number] = (path, target, status)
        require(seen == {entry['number'] for entry in entries}, 'wrong subject overview membership: ' + subject)
    for number, entry in new.items():
        expected_label = LABELS[entry['status']]
        require(block_status(full[number][1]) == expected_label, f'wrong detail status at Q{number}')
        require(indexes[number][2] == expected_label, f'wrong index status at Q{number}')
        require(overviews[number][2] == expected_label, f'wrong subject overview status at Q{number}')

    counts = Counter(entry['status'] for entry in current)
    root_text = read(ROOT / 'README.md')
    totals = {'Problems in the catalog': str(len(current)), 'Open': str(counts['open']),
              'Open, with partial results here': str(counts['partial']),
              'Solved here': f"{counts['proved'] + counts['disproved']} ({counts['proved']} proved, {counts['disproved']} disproved)"}
    for label, value in totals.items():
        match = re.search(r'^\| ' + re.escape(label) + r' \| (.*?) \|$', root_text, re.M)
        require(match is not None and match.group(1) == value, 'wrong global count: ' + label)

    referenced = set()
    for number, entry in results.items():
        for field in ('proof', 'review', 'checks', 'sources', 'page', 'index'):
            require(field in entry, f'Q{number} lacks manifest {field}')
            referenced.update(artifact_paths(entry[field], field, number))
        page = next(artifact_paths(entry['page'], 'page', number))
        index = next(artifact_paths(entry['index'], 'index', number))
        require(page == full[number][0], f'Q{number} manifest page is not its actual full-detail page')
        require(index == indexes[number][0], f'Q{number} manifest index is not its actual index file')
        old_blocks = dict(blocks(base_text(str(page.relative_to(ROOT)))))
        require(number in old_blocks, f'Q{number} absent from base detail page')
        require(old_blocks[number].splitlines()[0] == full[number][1].splitlines()[0], f'Q{number} detail heading changed')
        require(statement_paragraph(old_blocks[number]) == statement_paragraph(full[number][1]), f'Q{number} rendered statement changed')
        for owner, target, _ in (indexes[number], overviews[number]):
            actual, fragment = file_path(target, owner)
            require(actual == page and fragment == 'q' + str(number), f'Q{number} catalog link points to wrong detail')
            check_link(target, owner)
        # Result references on the updated detail block must all resolve locally.
        for target in markdown_targets(full[number][1]):
            check_link(target, page)

    local_links, markdown_files = 0, 0
    for path in sorted(ROUND_DIR.rglob('*.md')):
        markdown_files += 1
        for target in markdown_targets(read(path)):
            local_links += check_link(target, path)
    return {'status': 'pass', 'base_commit': BASE, 'round': ROUND,
            'catalog_entries': len(current), 'changed_ids': sorted(changed),
            'changed_fields': changed_fields, 'global_status_counts': dict(sorted(counts.items())),
            'subject_counts_checked': len(subject_counts), 'detail_statuses_checked': len(full),
            'overview_statuses_checked': len(overviews), 'index_statuses_checked': len(indexes),
            'manifest_artifacts_checked': len(referenced), 'round_markdown_files_checked': markdown_files,
            'local_markdown_links_checked': local_links,
            'checks': ['exact seven-ID JSON change boundary', 'immutable problem statements and metadata',
                       'CSV statuses and unchanged other fields', 'all rendered catalog statuses',
                       'global and subject count recomputation', 'exact full-page and index routing',
                       'manifest artifact existence', 'local Markdown files and fragment targets']}


def main():
    global PENDING_REPORT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', help='Optional JSON report path inside this research-round directory')
    args = parser.parse_args()
    destination = None
    if args.output:
        destination = Path(args.output).resolve()
        require(destination.is_relative_to(ROUND_DIR) and destination.suffix == '.json'
                and destination.name != 'RESULTS.json',
                'report must be a separate JSON file inside the research round')
        # A README may link to the report this invocation is about to create.
        PENDING_REPORT = destination
    try:
        report = validate()
        exit_code = 0
    except (ValidationError, OSError, ValueError, KeyError, TypeError) as error:
        report = {'status': 'fail', 'base_commit': BASE, 'round': ROUND, 'error': str(error)}
        exit_code = 1
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    if destination is not None:
        destination.write_text(encoded, encoding='utf-8')
    print(encoded, end='')
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
