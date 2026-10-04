# Agent steering incidents

This is an evidence log, not an automatic memory. Add an entry only when an observable failure or repeated human correction occurred. Remove sensitive data and avoid storing chat transcripts.

No user-observed recurring incidents have been recorded yet. The duplicate-file guard is a **pilot hypothesis inspired by the lecture example**, not an incident validated in this project. Measure whether it catches a real mistake and whether it causes false blocks; remove it if it duplicates Codex's native behavior or adds friction without benefit.

## Entry format

### [date] Short incident name

- **Trigger:** What action/state was observable?
- **Expected / actual:** What should happen and what happened?
- **Evidence:** Task/session reference or sanitized concrete example.
- **Repeat count:** Independent occurrences; mark unknown when unknown.
- **Likely cause:** Hypothesis, not established fact.
- **Steering:** Smallest correction (context, standard, skill, hook, or none).
- **False-positive / cost risk:** How could the correction misfire or slow work?
- **Check:** Comparable follow-up and observed outcome.
- **Status:** observed / candidate / validated / rejected / retired.

### 2026-10-04 Context token estimate conflated with rendered length

- **Trigger:** A lean-context run stored `len(rendered_markdown) / 4` in the benchmark field `context_tokens`.
- **Expected / actual:** The field should carry the comparable `ContextPackage.token_estimate`; rendered character count and its rough `/4` proxy should have distinct names. Two independent lean ON runs each saved `419` as `context_tokens`, while their saved ContextPackages declared `2,251` and `2,247`.
- **Evidence:** `reports/swebench-pilot/sphinx-7590-lean-context-v1/outcome.json`, `reports/swebench-pilot/sphinx-7590-lean-context-paired-v2/outcome.json`, their saved `context-package.json` and `context.md` files, and the Codex traces. Both package/render hashes reconcile. The source packet estimate is approximate and is recorded before the render-only task-block removal.
- **Repeat count:** 2 independent lean ON runs in the same benchmark path; no post-fix model run yet.
- **Likely cause:** The trajectory inventory exposed a rendered-character `/4` proxy beside the native packet estimate, and the runner assigned the proxy to a token-named field.
- **Steering:** Set `context_tokens` from `ContextPackage.token_estimate`; record `context_rendered_characters` and `rendered_context_chars_div4_proxy` separately; repair derived rows/reports from saved packages and traces; state the estimator's approximation and pre-transform timing. Preserve the legacy summary alias while labeling it as processed tokens, not billed cost.
- **False-positive / cost risk:** The compiler estimate is not provider tokenization and can overstate the final payload after render-only transforms. Treating the estimate as exact would create a new error; codepoint counts are a separate diagnostic only.
- **Check:** Both saved lean runs now reconcile `context_tokens` with the package estimate and rendered character count with `context.md`; hashes and leakage checks pass. The three-task pilot's six cumulative usage rows also reconcile. A separate post-fix model run has not been made.
- **Status:** candidate.

### 2026-10-04 Duplicate report creation blocked

- **Trigger:** An `apply_patch` call tried to add `reports/swebench-pilot/sphinx-7590-lean-context-v1/report.md` after the benchmark runner had already generated it.
- **Expected / actual:** Add-file was blocked because the target existed. The file was inspected and then reused/edited to hold the diagnostic report.
- **Evidence:** Auto-steering hook output in the current Codex task; existing file was the runner-generated benchmark report.
- **Repeat count:** 1 occurrence; this does not establish a recurring user workflow failure.
- **Likely cause:** The generated report's existence was not checked before drafting an Add File patch.
- **Steering:** Inspect an existing artifact and update it when the user-requested result belongs at that path. No hook expansion proposed.
- **False-positive / cost risk:** A legitimate intentional replacement may require an extra inspect/edit step.
- **Check:** The existing path was preserved and edited; there was no parallel duplicate report.
- **Status:** observed.

### 2026-10-04 Usage snapshot and context report regeneration defects

- **Trigger:** Independent review of the telemetry and trajectory-report corrections.
- **Expected / actual:** A cumulative usage row must reflect one complete latest snapshot; regenerated context diagnostics must preserve the native ContextCompiler estimate and keep rendered-character proxies separate. The parser retained older fields omitted by a later snapshot, while the report script replaced `context_tokens` with rendered Markdown characters divided by four. The v1 diagnostic report also contained a mistyped context SHA-256.
- **Evidence:** Reviewer findings in the current Codex task; parser and report-builder paths; saved Sphinx v1 `context.md`, metrics, and hashes.
- **Repeat count:** One independent review pass found three issues; no follow-up recurrence measurement yet.
- **Likely cause:** Per-field accumulation treated snapshots as patches, and the analysis script reused one field for unlike measurements; report digest was manually transcribed.
- **Steering:** Replace all usage fields from each valid snapshot (missing means unknown); retain the native estimate and write the `/4` value to a separate proxy field; correct the digest from the saved bytes.
- **False-positive / cost risk:** A partial but intentionally sparse provider snapshot will now surface missing data as null rather than borrowing the last known value. This is preferable for integrity but may reduce apparent telemetry coverage.
- **Check:** Changed parser and report derivation; modules compile; v1 rendered-context digest now matches `context.md` and saved metrics. A full trajectory-report regeneration and independent post-fix usage fixture have not been run.
- **Status:** candidate.
