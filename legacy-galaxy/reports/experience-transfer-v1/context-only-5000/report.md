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
| Trajectory tokens | 62955.00 | 91564.00 | 28609.00 | 28609.00 | 28609.00 | 1 |
| Input tokens | 62635.00 | 90752.00 | 28117.00 | 28117.00 | 28117.00 | 1 |
| Output tokens | 320.00 | 812.00 | 492.00 | 492.00 | 492.00 | 1 |
| Tool calls | 3.00 | 3.00 | 0.00 | 0.00 | 0.00 | 1 |
| Duration — all attempts (ms) | 16746.53 | 27757.69 | 11011.16 | 11011.16 | 11011.16 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.00 | 2.00 | 1.00 | 1.00 | 1.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 16746.530610000038 ms
ON median: 27757.694559000127 ms
Paired Δ median: 11011.163949000089 ms
Paired Δ mean: 11011.163949000089 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| B-quantities | 28609.00 | 1745.00 | 16.39 |

| Token cost / verified success | 62955.0 | 91564.0 | 28609.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
