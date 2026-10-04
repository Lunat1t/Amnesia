# Galaxy team playbook

Use this playbook when the user asks to work as their Galaxy team. The user is Product Manager; main Codex owns orchestration and synthesis.

1. Follow root `AGENTS.md` and read `docs/codex-agent-workflow.md`.
2. For nontrivial work, create a compact attention map using `attention-map-template.md` in working context. Do not create a per-task file unless requested.
3. Follow workflow routing and product decision gates. For Galaxy work, read roadmap, source map and relevant cards; verify current-state claims against code.
4. Pass bounded task packets to only relevant specialists. Keep at most one writer on overlapping files. Read-only roles stay read-only.
5. When work diverges from the map, steer toward the smallest corrective action. For recurring incidents, follow evidence and promotion steps in the workflow and `incident-register.md`; do not silently convert one failure into a permanent rule.
6. Finish with actual result, verification performed, remaining unknowns, sources used, and any measurable workflow outcome. Never claim that an untrusted/unapproved hook, skill, or rule is active.

The current project-specific hook only detects duplicate file creation through Codex `apply_patch`. Other steering is performed by the orchestrator's workflow until a recurring event has evidence and a safe hook can be justified.
