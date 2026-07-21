#!/usr/bin/env python3
"""Fast deterministic validation for the SaaS OS automation contract."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "MASTER_PLAN.md",
    "STATUS.md",
    "STYLE_GUIDE.md",
    "CHANGELOG.md",
    ".ai/worker.py",
    ".github/workflows/ai-worker.yml",
]
VALID_STATES = {
    "BACKLOG", "RESEARCHING", "OUTLINE", "DRAFTING", "FACT_CHECK",
    "REVIEW", "REVISION", "DONE", "DEPRECATED",
}


def error(message: str) -> None:
    print(f"validation error: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative in REQUIRED:
    path = ROOT / relative
    if not path.is_file() or path.stat().st_size == 0:
        error(f"missing or empty required file: {relative}")

status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
rows = re.findall(
    r"^\|\s*(P\d{2}-C\d{2})\s*\|[^|]+\|\s*([A-Z_]+)\s*\|",
    status,
    flags=re.MULTILINE,
)
if not rows:
    error("STATUS.md has no chapter rows")
if len({chapter_id for chapter_id, _ in rows}) != len(rows):
    error("STATUS.md contains duplicate chapter IDs")
for chapter_id, state in rows:
    if state not in VALID_STATES:
        error(f"invalid state for {chapter_id}: {state}")
if sum(state == "REVIEW" for _, state in rows) > 1:
    error("only one chapter may be in REVIEW")

diff = subprocess.run(
    ["git", "-C", str(ROOT), "diff", "--numstat"],
    check=True,
    text=True,
    capture_output=True,
).stdout
for line in diff.splitlines():
    parts = line.split("\t", 2)
    if len(parts) == 3 and parts[0].isdigit() and int(parts[0]) > 8_000:
        error(f"unexpectedly large generated change: {parts[2]}")

print(f"Validation passed for {len(rows)} queued chapters.")
