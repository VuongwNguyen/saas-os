# Repository agent rules

- Treat `MASTER_PLAN.md` and `STATUS.md` as sources of truth.
- Work only on `develope-for-ai`; never push directly to `main`.
- Process at most one chapter per run.
- Stop when any chapter is awaiting human review.
- Never mark a chapter `DONE` before its review changes appear in `main`.
- Do not invent sources, quotations, statistics, benchmarks, or case studies.
- Preserve Vietnamese as the primary content language.
- Run `python3 .ai/validate.py` and `git diff --check` before publishing changes.
- Never reveal, log, or commit secrets.
- Never merge, force-push, rewrite remote history, or delete branches.
