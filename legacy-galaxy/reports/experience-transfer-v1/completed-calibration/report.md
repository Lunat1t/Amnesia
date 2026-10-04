# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 1 | 0 |
| FAIL | 1 | 0 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 63399.50 | 111094.50 | 47695.00 | 47695.00 | 47695.00 | 2 |
| Input tokens | 63044.00 | 110185.00 | 47141.00 | 47141.00 | 47141.00 | 2 |
| Output tokens | 355.50 | 909.50 | 554.00 | 554.00 | 554.00 | 2 |
| Tool calls | 3.00 | 4.00 | 1.00 | 1.00 | 1.00 | 2 |
| Duration — all attempts (ms) | 21908.01 | 33693.81 | 11785.80 | 11785.80 | 11785.80 | 2 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.00 | 2.00 | 1.00 | 1.00 | 1.00 | 2 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 19164.548403000026 ms
ON median: 31477.537287999894 ms
Paired Δ median: 12312.988884999868 ms
Paired Δ mean: 12312.988884999868 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| A-prices | 59906.00 | 1743.00 | 34.37 |
| B-quantities | 35484.00 | 1744.00 | 20.35 |

| Token cost / verified success | 126799.0 | 111094.5 | -15704.5 |
| Currency cost / verified success | NA | NA | NA |

Runs: 4. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
