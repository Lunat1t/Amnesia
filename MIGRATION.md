# Migration from Galaxy to Amnesia

- **Source checkout:** `/home/bah/Documents/Codex/galaxy-3.2.1-alpha.19-evidence-integrity`
- **Migrated on:** 2026-10-04
- **Destination:** Amnesia standalone repository
- **Source checkout changed or deleted:** no

## Included

- All files under `docs/`, copied without editing to `legacy-galaxy/docs/` (all source cards, architecture notes, roadmaps, and team harness documents).
- Original `README.md` and `AGENTS.md`, all seven Galaxy Codex role definitions, and examples, preserved under `legacy-galaxy/`.
- Active Amnesia README, agent instructions, charter, source map, and seven Amnesia-named Codex roles.
- Benchmark README/dataset manifest and 126 compact protocol/report/evidence files and three source-code citation snapshots copied with their paths under `legacy-galaxy/`.
- `migration-manifest.json` contains SHA-256 for every migrated file.

## Kept in the Galaxy checkout

Galaxy source code/runtime, hidden benchmark patches, repository snapshots, databases, event traces, evaluator logs, and other bulk run state were not copied. The original checkout remains intact and is the provenance location for these artifacts. Compact reports and manifests were included where available. This is a complete transfer of documentation/source cards/agent definitions, not a code or raw-data fork.

Historical Galaxy references remain verbatim to preserve citations and provenance. The old absolute-path Codex hook config was not copied or enabled; active Amnesia `.codex/config.toml` only enables agent definitions.
