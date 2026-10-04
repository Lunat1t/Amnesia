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
| Trajectory tokens | 63307.00 | 82932.00 | 19625.00 | 19625.00 | 19625.00 | 1 |
| Input tokens | 62885.00 | 82292.00 | 19407.00 | 19407.00 | 19407.00 | 1 |
| Output tokens | 422.00 | 640.00 | 218.00 | 218.00 | 218.00 | 1 |
| Tool calls | 3.00 | 4.00 | 1.00 | 1.00 | 1.00 | 1 |
| Duration — all attempts (ms) | 17084.02 | 20225.76 | 3141.74 | 3141.74 | 3141.74 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 2.00 | 2.00 | 0.00 | 0.00 | 0.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 17084.023903999878 ms
ON median: 20225.76372200001 ms
Paired Δ median: 3141.739818000133 ms
Paired Δ mean: 3141.739818000133 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| B-normalize_groups | 19625.00 | 1654.00 | 11.87 |

| Token cost / verified success | 63307.0 | 82932.0 | 19625.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
