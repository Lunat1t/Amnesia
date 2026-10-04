# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 1 | 0 |
| FAIL | 0 | 2 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 371559.00 | 272164.00 | -99395.00 | 5764.00 | 68839.33 | 3 |
| Processed input tokens | 369785.00 | 270772.00 | -99013.00 | 5803.00 | 68554.67 | 3 |
| Cached input tokens | 339456.00 | 249856.00 | -89600.00 | -768.00 | 67328.00 | 3 |
| Uncached input tokens (not a billing estimate) | 30329.00 | 22159.00 | -8170.00 | 6522.00 | 1226.67 | 3 |
| Output tokens | 1774.00 | 1392.00 | -382.00 | -39.00 | 284.67 | 3 |
| Tool calls | 14.00 | 11.00 | -3.00 | -2.00 | 0.00 | 3 |
| Duration — all attempts (ms) | 181855.95 | 156347.75 | -25508.20 | 2454.15 | 541.52 | 3 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Galaxy context token estimate | NA | NA | NA | NA | NA | 0 |
| Rendered context characters | NA | NA | NA | NA | NA | 0 |
| Unique files opened | NA | NA | NA | NA | NA | 0 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 152896.99056599964 ms
ON median: 155351.13993499998 ms
Paired Δ median: 2454.149369000341 ms
Paired Δ mean: 2454.149369000341 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context estimate (approx.) | Δ / estimate |
|---|---:|---:|---:|
| pallets__flask-5014 | 5764.00 | 3896.00 | 1.48 |
| pytest-dev__pytest-10356 | -99395.00 | 4850.00 | -20.49 |
| sphinx-doc__sphinx-7590 | 300149.00 | 4073.00 | 73.69 |

| Processed tokens / verified success (all attempts) | 914898.0 | 1121416.0 | 206518.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 6. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
