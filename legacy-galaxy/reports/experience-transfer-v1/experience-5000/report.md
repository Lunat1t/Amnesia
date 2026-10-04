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
| Trajectory tokens | 68617.50 | 101129.50 | 32512.00 | 32512.00 | 32512.00 | 2 |
| Input tokens | 68274.50 | 100436.00 | 32161.50 | 32161.50 | 32161.50 | 2 |
| Output tokens | 343.00 | 693.50 | 350.50 | 350.50 | 350.50 | 2 |
| Tool calls | 3.00 | 3.00 | 0.00 | 0.00 | 0.00 | 2 |
| Duration — all attempts (ms) | 18097.25 | 30482.42 | 12385.17 | 12385.17 | 12385.17 | 2 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.00 | 2.00 | 1.00 | 1.00 | 1.00 | 2 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 19566.82323599989 ms
ON median: 22853.342307000275 ms
Paired Δ median: 3286.5190710003844 ms
Paired Δ mean: 3286.5190710003844 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| A-prices | 21328.00 | 1743.00 | 12.24 |
| B-quantities | 43696.00 | 1986.00 | 22.00 |

| Token cost / verified success | 137235.0 | 101129.5 | -36105.5 |
| Currency cost / verified success | NA | NA | NA |

Runs: 4. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
