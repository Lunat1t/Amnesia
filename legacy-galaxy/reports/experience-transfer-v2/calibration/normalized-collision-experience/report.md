# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 2 | 0 |
| FAIL | 0 | 0 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 63200.50 | 110312.00 | 47111.50 | 47111.50 | 47111.50 | 2 |
| Input tokens | 62816.50 | 109442.00 | 46625.50 | 46625.50 | 46625.50 | 2 |
| Output tokens | 384.00 | 870.00 | 486.00 | 486.00 | 486.00 | 2 |
| Tool calls | 3.00 | 4.00 | 1.00 | 1.00 | 1.00 | 2 |
| Duration — all attempts (ms) | 21359.12 | 29559.89 | 8200.78 | 8200.78 | 8200.78 | 2 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 0.50 | 1.50 | 1.00 | 1.00 | 1.00 | 2 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 2
OFF median: 21359.11884099983 ms
ON median: 21753.532202499853 ms
Paired Δ median: 394.41336150002826 ms
Paired Δ mean: 394.41336150002826 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| A-normalize_users | 20543.00 | 1655.00 | 12.41 |
| B-normalize_groups | 73680.00 | 1910.00 | 38.58 |

| Token cost / verified success | 63200.5 | 110312.0 | 47111.5 |
| Currency cost / verified success | NA | NA | NA |

Runs: 4. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
