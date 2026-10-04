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
| Trajectory tokens | 90165.50 | 67405.00 | -22760.50 | -22760.50 | -22760.50 | 2 |
| Input tokens | 89722.50 | 66735.00 | -22987.50 | -22987.50 | -22987.50 | 2 |
| Output tokens | 443.00 | 670.00 | 227.00 | 227.00 | 227.00 | 2 |
| Tool calls | 4.00 | 3.00 | -1.00 | -1.00 | -1.00 | 2 |
| Duration — all attempts (ms) | 19749.39 | 32709.91 | 12960.52 | 12960.52 | 12960.52 | 2 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.50 | 2.50 | 1.00 | 1.00 | 1.00 | 2 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 2
OFF median: 19749.38930450003 ms
ON median: 18736.022766999668 ms
Paired Δ median: -1013.3665375003602 ms
Paired Δ mean: -1013.3665375003602 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| A-active_sessions | -49747.00 | 1668.00 | -29.82 |
| B-active_tokens | 4226.00 | 1906.00 | 2.22 |

| Token cost / verified success | 90165.5 | 67405.0 | -22760.5 |
| Currency cost / verified success | NA | NA | NA |

Runs: 4. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
