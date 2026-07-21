#!/usr/bin/env python3
"""Produce one reviewable SaaS OS chapter through the OpenAI Responses API."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "STATUS.md"
REPORTS_DIR = ROOT / ".ai" / "reports"
PROTECTED_PATHS = {
    ".ai/worker.py",
    ".ai/validate.py",
    ".github/workflows/ai-worker.yml",
}
MAX_CONTEXT_CHARS = 450_000
MAX_FILE_CHARS = 220_000
MAX_TOTAL_OUTPUT_CHARS = 900_000

ROW_RE = re.compile(
    r"^\|\s*(P\d{2}-C\d{2})\s*\|\s*([^|]+?)\s*\|\s*"
    r"(BACKLOG|RESEARCHING|OUTLINE|DRAFTING|FACT_CHECK|REVIEW|REVISION|DONE|DEPRECATED)"
    r"\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$",
    re.MULTILINE,
)


def fail(message: str) -> None:
    print(f"AI worker stopped: {message}", file=sys.stderr)
    raise SystemExit(1)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=check,
        text=True,
        capture_output=True,
    )


def parse_rows(text: str) -> list[dict[str, str]]:
    return [
        {
            "id": match.group(1).strip(),
            "title": match.group(2).strip(),
            "status": match.group(3).strip(),
            "dependencies": match.group(4).strip(),
            "output": match.group(5).strip(),
        }
        for match in ROW_RE.finditer(text)
    ]


def replace_status(text: str, chapter_id: str, old: str, new: str) -> str:
    pattern = re.compile(
        rf"^(\|\s*{re.escape(chapter_id)}\s*\|[^|]+\|\s*){old}(\s*\|.*)$",
        re.MULTILINE,
    )
    updated, count = pattern.subn(rf"\g<1>{new}\g<2>", text, count=1)
    if count != 1:
        fail(f"cannot move {chapter_id} from {old} to {new}")
    return updated


def dependency_ready(row: dict[str, str], rows: list[dict[str, str]]) -> bool:
    raw = row["dependencies"]
    if not raw or raw in {"-", "[]"}:
        return True
    states = {item["id"]: item["status"] for item in rows}
    dependencies = re.findall(r"P\d{2}-C\d{2}", raw)
    return all(states.get(item) == "DONE" for item in dependencies)


def main_status_text() -> str:
    result = git("show", "origin/main:STATUS.md", check=False)
    return result.stdout if result.returncode == 0 else ""


def approve_merged_review(status_text: str) -> tuple[str, bool]:
    rows = parse_rows(status_text)
    reviews = [row for row in rows if row["status"] == "REVIEW"]
    if not reviews:
        return status_text, False

    merged_rows = {row["id"]: row for row in parse_rows(main_status_text())}
    review = reviews[0]
    if merged_rows.get(review["id"], {}).get("status") != "REVIEW":
        print(f"Waiting for human review of {review['id']}; no API call made.")
        raise SystemExit(0)

    status_text = replace_status(status_text, review["id"], "REVIEW", "DONE")
    print(f"Accepted merged review for {review['id']} and moved it to DONE.")
    return status_text, True


def context_bundle(chapter: dict[str, str], status_text: str) -> str:
    preferred = [
        "MASTER_PLAN.md",
        "STATUS.md",
        "STYLE_GUIDE.md",
        "GLOSSARY.md",
        "METRICS_DICTIONARY.md",
        "CHANGELOG.md",
    ]
    candidates = [ROOT / item for item in preferred]
    candidates.extend(sorted((ROOT / "volumes").rglob("*.md")))
    candidates.extend(sorted((ROOT / "references").rglob("*.md")))

    sections: list[str] = []
    used: set[Path] = set()
    total = 0
    for path in candidates:
        if path in used or not path.is_file():
            continue
        used.add(path)
        try:
            content = status_text if path == STATUS_PATH else path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if len(content) > MAX_FILE_CHARS:
            content = content[:MAX_FILE_CHARS] + "\n[TRUNCATED]\n"
        section = f"\n--- FILE: {path.relative_to(ROOT).as_posix()} ---\n{content}"
        if total + len(section) > MAX_CONTEXT_CHARS:
            break
        sections.append(section)
        total += len(section)

    tree = git("ls-files", check=False).stdout
    header = (
        f"TARGET CHAPTER: {chapter['id']} — {chapter['title']}\n"
        f"REPOSITORY FILES:\n{tree[:30_000]}\n"
    )
    return header + "".join(sections)


def response_schema() -> dict[str, object]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["summary", "commit_message", "quality_notes", "changes"],
        "properties": {
            "summary": {"type": "string"},
            "commit_message": {"type": "string"},
            "quality_notes": {
                "type": "array",
                "items": {"type": "string"},
            },
            "changes": {
                "type": "array",
                "maxItems": 25,
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["path", "content"],
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                    },
                },
            },
        },
    }


def call_openai(chapter: dict[str, str], context: str) -> dict[str, object]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        fail("OPENAI_API_KEY is not configured")

    model = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
    instructions = """You are the Chief Editor and Operating Systems Architect for SaaS OS.
Produce exactly one complete, professional Vietnamese chapter for the target item. Follow MASTER_PLAN.md, the chapter template, repository style, Definition of Done, and existing cross-references. Create the chapter plus directly relevant SOP, template, dashboard, prompt, agent specification, case-study, glossary, or reference artifacts when justified.

Use web search for current or factual claims. Prefer primary sources, research papers, standards bodies, and original vendor documentation. Include verifiable URLs and access dates. Never invent quotations, statistics, benchmarks, citations, or case studies. Explicitly distinguish facts, inference, and recommendations. Keep every artifact operational and reviewable.

Return full file contents only for files that must be created or changed. Do not change STATUS.md, CHANGELOG.md, workflow files, or automation code; the runner owns status and change history. Do not mark anything DONE. Do not include secrets. Stay within the target chapter and its supporting artifacts."""
    payload = {
        "model": model,
        "instructions": instructions,
        "input": context,
        "reasoning": {"effort": "high"},
        "tools": [{"type": "web_search"}],
        "text": {
            "format": {
                "type": "json_schema",
                "name": "saas_os_change_set",
                "strict": True,
                "schema": response_schema(),
            },
            "verbosity": "high",
        },
        "max_output_tokens": 50_000,
        "store": False,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=2_400) as response:
            body = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:2_000]
        fail(f"OpenAI API returned HTTP {exc.code}: {detail}")
    except (urllib.error.URLError, TimeoutError) as exc:
        fail(f"OpenAI API request failed: {exc}")

    output_text = body.get("output_text")
    if not output_text:
        for item in body.get("output", []):
            if item.get("type") != "message":
                continue
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    output_text = content.get("text")
                    break
    if not output_text:
        fail("OpenAI API returned no structured output")
    try:
        return json.loads(output_text)
    except json.JSONDecodeError as exc:
        fail(f"OpenAI output was not valid JSON: {exc}")


def safe_target(raw_path: str) -> Path:
    pure = PurePosixPath(raw_path)
    if pure.is_absolute() or ".." in pure.parts or not pure.parts:
        fail(f"unsafe output path: {raw_path}")
    normalized = pure.as_posix()
    if normalized in PROTECTED_PATHS or normalized.startswith(".git/"):
        fail(f"model attempted to modify protected path: {normalized}")
    return ROOT.joinpath(*pure.parts)


def apply_changes(result: dict[str, object]) -> list[str]:
    changes = result.get("changes")
    if not isinstance(changes, list) or not changes:
        fail("model returned no file changes")
    total = 0
    written: list[str] = []
    for change in changes:
        if not isinstance(change, dict):
            fail("invalid change object")
        raw_path = change.get("path")
        content = change.get("content")
        if not isinstance(raw_path, str) or not isinstance(content, str):
            fail("change path and content must be strings")
        if raw_path in {"STATUS.md", "CHANGELOG.md"}:
            fail(f"model attempted to modify runner-owned file: {raw_path}")
        total += len(content)
        if len(content) > MAX_FILE_CHARS or total > MAX_TOTAL_OUTPUT_CHARS:
            fail("model output exceeded file-size guardrail")
        target = safe_target(raw_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(f".{target.name}.ai-tmp")
        temporary.write_text(content.rstrip() + "\n", encoding="utf-8")
        temporary.replace(target)
        written.append(raw_path)
    return written


def append_changelog(chapter: dict[str, str], summary: str, files: list[str]) -> None:
    path = ROOT / "CHANGELOG.md"
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Changelog\n"
    entry = (
        f"\n## {chapter['id']} moved to REVIEW\n\n"
        f"- {summary.strip()}\n"
        f"- Files: {', '.join(f'`{item}`' for item in files)}\n"
    )
    path.write_text(existing.rstrip() + "\n" + entry, encoding="utf-8")


def write_report(chapter: dict[str, str], result: dict[str, object], files: list[str]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "chapter": chapter,
        "summary": result.get("summary", ""),
        "quality_notes": result.get("quality_notes", []),
        "files": files,
        "model": os.environ.get("OPENAI_MODEL", "gpt-5.6-sol"),
        "human_action": "Review and merge the draft pull request to approve this chapter.",
    }
    (REPORTS_DIR / f"{chapter['id'].lower()}-review.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    pr_body = ROOT / ".ai" / "PR_BODY.md"
    notes = "\n".join(f"- {item}" for item in report["quality_notes"]) or "- No additional notes."
    pr_body.write_text(
        f"## Chapter\n\n{chapter['id']} — {chapter['title']}\n\n"
        f"## Summary\n\n{report['summary']}\n\n"
        f"## Quality notes\n\n{notes}\n\n"
        "## Human action\n\nReview the artifacts and merge this PR to approve the chapter. "
        "The worker never merges this PR itself. Use Create a merge commit and keep "
        "the fixed develope-for-ai branch; do not squash or delete it.\n",
        encoding="utf-8",
    )


def run() -> None:
    if not STATUS_PATH.exists():
        fail("STATUS.md is missing")
    branch = git("branch", "--show-current").stdout.strip()
    if branch != "develope-for-ai":
        fail(f"expected branch develope-for-ai, found {branch or 'detached HEAD'}")

    original_status = STATUS_PATH.read_text(encoding="utf-8")
    status_text, approved = approve_merged_review(original_status)
    rows = parse_rows(status_text)
    if not rows:
        fail("STATUS.md contains no machine-readable chapter rows")
    candidates = [
        row for row in rows
        if row["status"] in {"BACKLOG", "REVISION"} and dependency_ready(row, rows)
    ]
    if not candidates:
        if approved:
            STATUS_PATH.write_text(status_text, encoding="utf-8")
        print("No eligible chapter; no API call made.")
        return

    chapter = candidates[0]
    old_state = chapter["status"]
    researching = replace_status(status_text, chapter["id"], old_state, "RESEARCHING")
    STATUS_PATH.write_text(researching, encoding="utf-8")
    try:
        result = call_openai(chapter, context_bundle(chapter, researching))
        files = apply_changes(result)
        review_status = replace_status(researching, chapter["id"], "RESEARCHING", "REVIEW")
        for raw_path in files:
            if raw_path.endswith(".md") and "chapter-" in raw_path:
                output = f"`{raw_path}`"
                review_status = re.sub(
                    rf"^(\|\s*{re.escape(chapter['id'])}\s*\|(?:[^|]*\|){{3}}\s*)[^|]*(\|)$",
                    rf"\g<1>{output} \g<2>",
                    review_status,
                    count=1,
                    flags=re.MULTILINE,
                )
                break
        STATUS_PATH.write_text(review_status, encoding="utf-8")
        summary = str(result.get("summary", f"Produced {chapter['id']}"))
        append_changelog(chapter, summary, files)
        write_report(chapter, result, files)
        print(f"Prepared {chapter['id']} for human review with {len(files)} changed files.")
    except BaseException:
        STATUS_PATH.write_text(original_status, encoding="utf-8")
        raise


if __name__ == "__main__":
    run()
