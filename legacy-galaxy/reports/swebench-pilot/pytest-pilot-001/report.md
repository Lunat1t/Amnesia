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
| Trajectory tokens | 371559.00 | 272164.00 | -99395.00 | -99395.00 | -99395.00 | 1 |
| Input tokens | 369785.00 | 270772.00 | -99013.00 | -99013.00 | -99013.00 | 1 |
| Output tokens | 1774.00 | 1392.00 | -382.00 | -382.00 | -382.00 | 1 |
| Tool calls | 14.00 | 11.00 | -3.00 | -3.00 | -3.00 | 1 |
| Duration — all attempts (ms) | 181855.95 | 156347.75 | -25508.20 | -25508.20 | -25508.20 | 1 |
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
| pytest-dev__pytest-10356 | -99395.00 | 4850.00 | -20.49 |

| Token cost / verified success | NA | NA | NA |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
