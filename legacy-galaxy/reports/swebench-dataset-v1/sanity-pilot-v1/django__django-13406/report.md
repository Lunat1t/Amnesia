# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 1 | 0 |
| FAIL | 0 | 0 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 235481.00 | 369043.00 | 133562.00 | 133562.00 | 133562.00 | 1 |
| Processed input tokens | 234162.00 | 367322.00 | 133160.00 | 133160.00 | 133160.00 | 1 |
| Cached input tokens | NA | NA | NA | NA | NA | 0 |
| Uncached input tokens (not a billing estimate) | NA | NA | NA | NA | NA | 0 |
| Output tokens | 1319.00 | 1721.00 | 402.00 | 402.00 | 402.00 | 1 |
| Tool calls | 8.00 | 15.00 | 7.00 | 7.00 | 7.00 | 1 |
| Duration — all attempts (ms) | 92092.51 | 143261.77 | 51169.27 | 51169.27 | 51169.27 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Galaxy context token estimate | NA | NA | NA | NA | NA | 0 |
| Rendered context characters | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 0.00 | 3.00 | 3.00 | 3.00 | 3.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 92092.50567800063 ms
ON median: 143261.7745409998 ms
Paired Δ median: 51169.26886299916 ms
Paired Δ mean: 51169.26886299916 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context estimate (approx.) | Δ / estimate |
|---|---:|---:|---:|
| django__django-13406 | 133562.00 | NA | NA |

| Processed tokens / verified success (all attempts) | 235481.0 | 369043.0 | 133562.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
