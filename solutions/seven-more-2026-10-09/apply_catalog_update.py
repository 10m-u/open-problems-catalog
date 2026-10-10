#!/usr/bin/env python3
"""Apply the exact catalog patch after checking every affected file's hash.

Use --check for a dry run. No files are staged or committed. Already-applied
updates are accepted; mixed or edited target files are rejected without writes.
"""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROUND_DIR = Path(__file__).resolve().parent


def checked_patch(repo):
    repo = repo.resolve()
    manifest = json.loads((ROUND_DIR / "CATALOG_PATCH.json").read_text())
    patch_path = ROUND_DIR / "catalog-update.patch"
    patch = patch_path.read_bytes()
    if manifest["format_version"] != 1 or manifest["patch"] != patch_path.name:
        raise ValueError("Unsupported catalog patch manifest")
    if hashlib.sha256(patch).hexdigest() != manifest["patch_sha256"]:
        raise ValueError("Catalog patch checksum mismatch")
    paths = []
    states = []
    for entry in manifest["files"]:
        relative = Path(entry["path"])
        target = (repo / relative).resolve()
        if relative.is_absolute() or ".." in relative.parts or ".git" in relative.parts:
            raise ValueError("Unsafe patch path")
        if not target.is_relative_to(repo) or (repo / relative).is_symlink():
            raise ValueError("Patch path escapes the repository")
        paths.append(entry["path"])
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        if digest == entry["before_sha256"]:
            states.append("before")
        elif digest == entry["after_sha256"]:
            states.append("after")
        else:
            raise ValueError(f"Edited or incompatible target file: {entry['path']}")
    if len(paths) != 16 or len(set(paths)) != 16:
        raise ValueError("Expected exactly 16 distinct catalog paths")
    stats = subprocess.run(["git", "apply", "--numstat"], cwd=repo,
                           input=patch, capture_output=True, check=True).stdout.decode()
    patch_paths = [line.split("\t", 2)[2] for line in stats.splitlines()]
    if sorted(patch_paths) != sorted(paths):
        raise ValueError("Patch paths disagree with the manifest")
    if len(set(states)) != 1:
        raise ValueError("Catalog is partly updated; refusing to overwrite it")
    return manifest, patch, states[0]


def apply_update(repo, check_only=False):
    repo = Path(repo).resolve()
    manifest, patch, state = checked_patch(repo)
    if state == "after":
        return {"state": "already_applied", "files": len(manifest["files"])}
    command = ["git", "-c", "core.whitespace=cr-at-eol", "apply", "--unidiff-zero", "--whitespace=nowarn"]
    subprocess.run(command + ["--check"], cwd=repo, input=patch, check=True)
    if check_only:
        return {"state": "ready", "files": len(manifest["files"])}
    subprocess.run(command, cwd=repo, input=patch, check=True)
    _, _, after = checked_patch(repo)
    if after != "after":
        raise ValueError("Applied catalog does not match the verified target hashes")
    return {"state": "applied", "files": len(manifest["files"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without changing catalog files")
    args = parser.parse_args()
    try:
        result = apply_update(ROUND_DIR.parents[1], check_only=args.check)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(f"Catalog update refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
