# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified quality effect: 0/3 paired difference. Infrastructure: works. Evidence integrity: works.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 0 | 0 |
| FAIL | 0 | 0 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | NA | NA | NA | NA | NA | 0 |
| Input tokens | NA | NA | NA | NA | NA | 0 |
| Output tokens | NA | NA | NA | NA | NA | 0 |
| Tool calls | NA | NA | NA | NA | NA | 0 |
| Duration — all attempts (ms) | NA | NA | NA | NA | NA | 0 |
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

| Token cost / verified success | NA | 1056719.0 | NA |
| Currency cost / verified success | NA | NA | NA |

Runs: 1. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
