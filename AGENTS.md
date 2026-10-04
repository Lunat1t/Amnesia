# Amnesia agent instructions

## Project state

Amnesia is the active project name and repository. Its research objective continues the Operation Amnesia question: how to improve coding agents through useful context, memory, and reusable experience. No replacement product architecture or broad implementation scope has been approved yet. The former Galaxy project remains preserved separately; its documentation is historical evidence and source material, not automatically active requirements.

## Before substantive work

1. Read [`docs/amnesia-charter.md`](docs/amnesia-charter.md) and [`docs/sources/amnesia/00-source-map.md`](docs/sources/amnesia/00-source-map.md).
2. Inspect relevant imported source cards and experiment reports under `legacy-galaxy/`; confirm claims against their cited artifacts where available.
3. Separate **internal evidence**, **external source claims**, and **Amnesia hypotheses**. An external article does not prove Amnesia works.
4. Identify the intended outcome, current evidence/gap, next step, sources/constraints, risks, and stopping condition before substantial work.
5. The user is Product Manager and owns product direction. Do technical reconnaissance independently; ask only for an actual product trade-off.

## Evidence and migration constraints

- Preserve provenance, dates, hashes, and limitations. Do not rewrite historical Galaxy source cards to make them appear to describe Amnesia.
- Treat imported Galaxy roadmap items as archived proposals until the PM adopts them for Amnesia.
- This migration includes documentation, source cards, agent definitions, examples, and compact report artifacts. It does not copy the Galaxy runtime/code or large raw SWE-bench repositories and run traces. Those remain in the original Galaxy checkout; see [`MIGRATION.md`](MIGRATION.md).
- Keep agent roles bounded and reviewable. Do not activate skills or policies automatically.
- Do not claim efficacy from retrieval metrics, synthetic tasks, or one-run pilots.

## Completion reports

For substantive work, report result, verification, unknowns, sources, and learning. Keep user-facing work in Russian unless the PM chooses another language.
