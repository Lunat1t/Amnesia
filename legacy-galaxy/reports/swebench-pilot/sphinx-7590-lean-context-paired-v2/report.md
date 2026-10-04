# Sphinx #7590 paired lean-context repeat

## Paired result

Frozen protocol: `examples/sphinx-7590-context-ablation-v2/plan.json` (SHA-256 `7d2b4ab7efda35226070c1d3a516edbc843a98d44c2b36cad288adf381fbaa2b`). Arm order was lean Galaxy ON, then OFF; each used a fresh worktree from the same accepted base commit, model, and evaluator.

| Metric | OFF | Lean Galaxy ON | ON − OFF |
|---|---:|---:|---:|
| ContextCompiler source-packet estimate (approx., pre text trim) | 0 | 2,247 | +2,247 |
| Rendered Markdown characters | 0 | 1,673 | +1,673 |
| Processed input tokens | 368,620 | 479,186 | +110,566 |
| Cached input tokens | 342,528 | 444,160 | +101,632 |
| Uncached input tokens | 26,092 | 35,026 | +8,934 |
| Output tokens | 1,720 | 2,550 | +830 |
| Input + output tokens | 370,340 | 481,736 | +111,396 (+30.1%) |
| Tool calls | 13 | 16 | +3 |
| Duration | 177.9 s | 182.8 s | +4.9 s |
| Official target | FAIL (0/1 F2P) | FAIL (0/1 F2P) | no outcome change |

The lean packet reduced the ContextCompiler source-packet estimate from 4,073 in the historical
Galaxy run to 2,247 (−44.8%), before render-only removal of duplicate task text; final output had 1,673 rendered Markdown characters. The estimate is approximate, not exact tokenization of the final payload or provider tokenization. The matched repeat did **not** reduce trajectory
usage: Galaxy ON used 30.1% more total processed tokens than OFF. The earlier
single lean arm had gone the other way (301,380 ON versus historical OFF
402,067). Across the two lean ON observations, total processed usage differs
by about 60%. That spread shows why the first apparent reduction could not
support a retrieval change.

Both new arms passed the same 24/24 pass-to-pass checks and failed the single
fail-to-pass target. The official evaluator report hash is identical for both
and both historical arms. Both agent patches applied, but neither resolved the
task. Therefore this pair provides **no verified quality benefit**, and its
resource signal is mixed. Keep default retrieval unchanged; this does not
justify an Sphinx-specific rule or a broad conclusion about Galaxy.

Cached input is reported separately. The +111,396 total-token delta is not a
billing delta; there is no configured dated price schedule. Uncached input was
+8,934 tokens in this pair.

## Integrity and artifacts

- Frozen base commit, dataset revision, gold-patch hash, test-patch hash, model,
  and effort match the plan.
- The lean ON packet retains `sphinx/domains/cpp.py` and
  `tests/test_domain_cpp.py`, omits the duplicate task block and the 12
  predeclared off-task paths, and has a ContextCompiler source-packet estimate of 2,247 (approximate, pre text trim), with 1,673 rendered Markdown characters.
- Leakage audit passed for both arms. Both evaluator reports completed without
  infrastructure failure, and both saved evidence ledgers validate.
- ON rendered context hash matches the saved context package metadata:
  `472240f06e75b3f315c427cda56ec96060c674520d21c17492d2648b5fd9f2e7`.
- Raw metrics, traces, patches, evaluator artifacts, and leakage audit are in
  this directory's `runs/`, `evaluator-artifacts/`, and
  `leakage-audit.json`; machine-readable comparison is `outcome.json`.

## Learning and next step

The duplicate task and off-task file entries can be removed without hiding the
parser and target test, but this experiment does not show that context removal
improves the task outcome or reliably lowers total usage. The observed trajectory-token
variation is larger than the initial one-run signal. The first lean-context row
was also corrected post-run: `419` was a Markdown-character-divided-by-four
proxy, not the ContextCompiler estimate of `2,251`; no run input changed. Next, evaluate an already
completed multi-task paired dataset with the corrected cumulative/cache-aware
telemetry; only preregister fresh runs if that audit identifies a reproducible
failure mode. Do not spend more on this single task to decide default retrieval.

Internal grounding: `docs/galaxy-v5-roadmap.md`,
`docs/sources/galaxy-superapp/00-source-map.md`,
`docs/sources/galaxy-superapp/01-current-galaxy.md`,
`docs/sources/galaxy-superapp/05-product-validation.md`,
`docs/sources/galaxy-superapp/08-operation-amnesia-radar.md`,
`docs/architecture/foundation.md`, and
`docs/architecture/current-state.md`. They support the narrow 5.0 scope and
verified paired measurement; the outcome above comes from saved local traces
and the official evaluator, not from those design sources. No external source
was required.
