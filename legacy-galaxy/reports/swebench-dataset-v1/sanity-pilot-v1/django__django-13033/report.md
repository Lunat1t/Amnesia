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
| Trajectory tokens | 371596.00 | 388870.00 | 17274.00 | 17274.00 | 17274.00 | 1 |
| Processed input tokens | 370128.00 | 387065.00 | 16937.00 | 16937.00 | 16937.00 | 1 |
| Cached input tokens | NA | NA | NA | NA | NA | 0 |
| Uncached input tokens (not a billing estimate) | NA | NA | NA | NA | NA | 0 |
| Output tokens | 1468.00 | 1805.00 | 337.00 | 337.00 | 337.00 | 1 |
| Tool calls | 12.00 | 12.00 | 0.00 | 0.00 | 0.00 | 1 |
| Duration — all attempts (ms) | 166737.64 | 160867.31 | -5870.34 | -5870.34 | -5870.34 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Galaxy context token estimate | NA | NA | NA | NA | NA | 0 |
| Rendered context characters | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 3.00 | 1.00 | -2.00 | -2.00 | -2.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 166737.64170600133 ms
ON median: 160867.30586200065 ms
Paired Δ median: -5870.335844000685 ms
Paired Δ mean: -5870.335844000685 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context estimate (approx.) | Δ / estimate |
|---|---:|---:|---:|
| django__django-13033 | 17274.00 | NA | NA |

| Processed tokens / verified success (all attempts) | 371596.0 | 388870.0 | 17274.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
