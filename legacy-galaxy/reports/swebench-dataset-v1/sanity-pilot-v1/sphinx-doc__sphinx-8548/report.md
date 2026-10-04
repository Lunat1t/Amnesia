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
| Trajectory tokens | 494640.00 | 432801.00 | -61839.00 | -61839.00 | -61839.00 | 1 |
| Processed input tokens | 492773.00 | 431110.00 | -61663.00 | -61663.00 | -61663.00 | 1 |
| Cached input tokens | NA | NA | NA | NA | NA | 0 |
| Uncached input tokens (not a billing estimate) | NA | NA | NA | NA | NA | 0 |
| Output tokens | 1867.00 | 1691.00 | -176.00 | -176.00 | -176.00 | 1 |
| Tool calls | 20.00 | 15.00 | -5.00 | -5.00 | -5.00 | 1 |
| Duration — all attempts (ms) | 109687.87 | 117858.08 | 8170.21 | 8170.21 | 8170.21 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Galaxy context token estimate | NA | NA | NA | NA | NA | 0 |
| Rendered context characters | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 6.00 | 4.00 | -2.00 | -2.00 | -2.00 | 1 |

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

| Task | Trajectory token Δ (ON−OFF) | Galaxy context estimate (approx.) | Δ / estimate |
|---|---:|---:|---:|
| sphinx-doc__sphinx-8548 | -61839.00 | NA | NA |

| Processed tokens / verified success (all attempts) | NA | NA | NA |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
