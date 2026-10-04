# Sphinx #7590 lean-context diagnostic

## Outcome

One predeclared Galaxy context arm was run against the frozen SWE-bench instance, using `gpt-6-luna`, low reasoning, and the official evaluator.

| Metric | Historical OFF | Historical Galaxy | Lean Galaxy |
|---|---:|---:|---:|
| ContextCompiler source-packet estimate (approx., pre text trim) | 0 | 4,073 | 2,251 |
| Rendered Markdown characters | 0 | 3,891 | 1,673 |
| Processed input tokens | 400,212 | 699,086 | 299,881 |
| Cached input tokens | 364,288 | 656,640 | 278,528 |
| Uncached input tokens | 35,924 | 42,446 | 21,353 |
| Output tokens | 1,855 | 3,130 | 1,499 |
| Input + output tokens | 402,067 | 702,216 | 301,380 |
| Tool calls | 17 | 22 | 11 |
| Duration | 195.9 s | 220.6 s | 165.0 s |
| SWE-bench target | FAIL (0/1 F2P) | FAIL (0/1 F2P) | FAIL (0/1 F2P) |

The ContextCompiler source-packet estimate is 44.8% lower than the historical Galaxy packet. It is calculated before the render-only removal of duplicate task text; final rendered Markdown had 1,673 characters. This run processed 57.1% fewer total tokens than the historical Galaxy arm and 25.0% fewer than historical OFF. The evaluator reported the same failure result and the same report SHA-256 as both historical arms (`491d1ae3164ae60cdf9494857b7fd2f59d197751fa131d20c072622e1007566b`). All arms passed 24/24 pass-to-pass checks; none passed the fail-to-pass target.

This is a promising diagnostic observation, not causal evidence: there is one new run, no randomized repetitions, and no basis to infer a general effect or billing cost. Leave default retrieval unchanged until counterbalanced repeats confirm the signal.

## Integrity checks

- Post-run telemetry correction: the original `context_tokens` field held rendered Markdown characters divided by four (419), not the source-packet compiler estimate (2,251). The saved ContextPackage held that estimate, computed before render-only task-block removal. Code and derived metrics were corrected without changing the prompt, supplied context, model run, or evaluator output. This estimate is approximate, not exact tokenization of the final rendered payload or provider tokenization.

- The run used the plan-frozen base commit, dataset revision, task patches, model, effort, and timeout.
- The context retained `sphinx/domains/cpp.py` and `tests/test_domain_cpp.py`; it excluded the 12 paths listed in the plan and omitted only the duplicate task section from injected context.
- Leakage audit passed; hidden gold/reference material was absent during the agent run.
- Rendered `context.md` SHA-256 matches both the context package's declared rendered-text hash and the run metric: `fb9026b9d6bbab18307b22c912555a4105410b265a5d32d1e621ee5950816b0f`.
- Verification evidence integrity passed. The official evaluator completed without infrastructure failure, but did not resolve the task.

## Provenance

- Frozen protocol: `examples/sphinx-7590-context-ablation-v1/plan.json`
- Raw arm, traces, context, patch, leakage audit and evaluator artifacts are in this report's sibling `runs/`, `evaluator-artifacts/`, and `leakage-audit.json`.
- Main historical comparison: `reports/swebench-pilot/analysis/sphinx-7590-context-harm.md`.
- Internal grounding: `docs/galaxy-v5-roadmap.md`, `docs/sources/galaxy-superapp/00-source-map.md`, `docs/sources/galaxy-superapp/01-current-galaxy.md`, `docs/sources/galaxy-superapp/05-product-validation.md`, `docs/sources/galaxy-superapp/08-operation-amnesia-radar.md`, `docs/architecture/foundation.md`, and `docs/architecture/current-state.md`. These support the five-foundation scope and evidence-based paired measurement, not the outcome of this run.
- No external source was needed; this was a local replay against frozen benchmark data with an official local evaluator.
- A matched follow-up pair is reported at `reports/swebench-pilot/sphinx-7590-lean-context-paired-v2/report.md`; it did not reproduce the first run's token reduction.
