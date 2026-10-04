# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 0 | 0 |
| FAIL | 0 | 1 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 402067.00 | 702216.00 | 300149.00 | 300149.00 | 300149.00 | 1 |
| Input tokens | 400212.00 | 699086.00 | 298874.00 | 298874.00 | 298874.00 | 1 |
| Output tokens | 1855.00 | 3130.00 | 1275.00 | 1275.00 | 1275.00 | 1 |
| Tool calls | 17.00 | 22.00 | 5.00 | 5.00 | 5.00 | 1 |
| Duration — all attempts (ms) | 195941.76 | 220620.38 | 24678.62 | 24678.62 | 24678.62 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | NA | NA | NA | NA | NA | 0 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 0
OFF median: NA ms
ON median: NA ms
Paired Δ median: NA ms
Paired Δ mean: NA ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| sphinx-doc__sphinx-7590 | 300149.00 | 4073.00 | 73.69 |

| Token cost / verified success | NA | NA | NA |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
