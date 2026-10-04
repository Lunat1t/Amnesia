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
| Trajectory tokens | 68429.00 | 82878.00 | 14449.00 | 14449.00 | 14449.00 | 1 |
| Input tokens | 68144.00 | 82353.00 | 14209.00 | 14209.00 | 14209.00 | 1 |
| Output tokens | 285.00 | 525.00 | 240.00 | 240.00 | 240.00 | 1 |
| Tool calls | 3.00 | 4.00 | 1.00 | 1.00 | 1.00 | 1 |
| Duration — all attempts (ms) | 17193.15 | 27551.00 | 10357.85 | 10357.85 | 10357.85 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.00 | 3.00 | 2.00 | 2.00 | 2.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 17193.1465749999 ms
ON median: 27550.9990139999 ms
Paired Δ median: 10357.852438999998 ms
Paired Δ mean: 10357.852438999998 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| B-active_tokens | 14449.00 | 1668.00 | 8.66 |

| Token cost / verified success | 68429.0 | 82878.0 | 14449.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
