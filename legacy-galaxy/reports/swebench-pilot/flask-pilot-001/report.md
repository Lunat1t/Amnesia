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
| Trajectory tokens | 141272.00 | 147036.00 | 5764.00 | 5764.00 | 5764.00 | 1 |
| Input tokens | 140516.00 | 146319.00 | 5803.00 | 5803.00 | 5803.00 | 1 |
| Output tokens | 756.00 | 717.00 | -39.00 | -39.00 | -39.00 | 1 |
| Tool calls | 8.00 | 6.00 | -2.00 | -2.00 | -2.00 | 1 |
| Duration — all attempts (ms) | 152896.99 | 155351.14 | 2454.15 | 2454.15 | 2454.15 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
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

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| pallets__flask-5014 | 5764.00 | 3896.00 | 1.48 |

| Token cost / verified success | 141272.0 | 147036.0 | 5764.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
