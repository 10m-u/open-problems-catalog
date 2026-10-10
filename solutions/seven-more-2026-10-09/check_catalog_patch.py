#!/usr/bin/env python3
"""Verify the catalog patch in a disposable worktree, without editing this checkout."""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from apply_catalog_update import ROUND_DIR, apply_update
from validate_catalog import BASE_COMMIT, ROUND, Validator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true", help="Refresh validation-summary.json")
    args = parser.parse_args()
    repo = ROUND_DIR.parents[1]
    with tempfile.TemporaryDirectory(prefix="seven-more-patch-", dir=repo.parent) as parent:
        checkout = Path(parent) / "repo"
        subprocess.run(["git", "worktree", "add", "--quiet", "--detach", str(checkout), BASE_COMMIT],
                       cwd=repo, check=True)
        try:
            shutil.copytree(ROUND_DIR, checkout / ROUND, ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copyfile(repo / "solutions/README.md", checkout / "solutions/README.md")
            dry_run = apply_update(checkout, check_only=True)
            applied = apply_update(checkout)
            repeated = apply_update(checkout)
            assert dry_run["state"] == "ready"
            assert applied["state"] == "applied"
            assert repeated["state"] == "already_applied"
            report = Validator(checkout, BASE_COMMIT).run()
            report["publication_layout"] = "Catalog patch validated in a disposable worktree; the published catalog is unchanged until the patch is applied."
            report["patch_application"] = {"dry_run": dry_run, "application": applied,
                                           "idempotence": repeated, "target_hashes_verified": True}
            # A later unrelated edit must be rejected without overwriting it.
            target = checkout / "README.md"
            modified = target.read_bytes() + b"\nPatch rejection control.\n"
            target.write_bytes(modified)
            try:
                apply_update(checkout)
            except ValueError:
                pass
            else:
                raise AssertionError("An edited catalog target was accepted")
            assert target.read_bytes() == modified
            report["patch_application"]["edited_target_rejected_without_writes"] = True
        finally:
            subprocess.run(["git", "worktree", "remove", "--force", str(checkout)], cwd=repo, check=True)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        (ROUND_DIR / "validation-summary.json").write_text(rendered)
    print(json.dumps({"all_passed": report["all_passed"], "checks_completed": report["checks_completed"],
                      "patch_application": report["patch_application"]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
