# SaaS OS

The complete operating system for building, operating, and scaling SaaS and AI-native companies.

SaaS OS is a Vietnamese, modular knowledge base containing handbooks, SOPs, templates, dashboards, metrics, prompts, agent specifications, playbooks, case studies, and maturity assessments.

## Governance

- `MASTER_PLAN.md` defines architecture and quality standards.
- `STATUS.md` is the execution queue and progress source of truth.
- AI work is published only on `develope-for-ai`.
- Every generated chapter stops at `REVIEW`.
- Merging its draft pull request is the human approval signal.
- The automation never merges into `main`.
- Merge with **Create a merge commit** and keep `develope-for-ai`; do not squash or delete the fixed AI branch.

## Automation

The scheduled workflow checks for work every 15 minutes but calls the OpenAI API only when an eligible chapter exists and no unmerged chapter is awaiting review.

Required repository secret:

- `OPENAI_API_KEY`

Optional repository variable:

- `OPENAI_MODEL` — defaults to `gpt-5.6-sol`.

The scheduled workflow becomes active only after `.github/workflows/ai-worker.yml` is merged into the default branch.
