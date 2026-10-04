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
| Trajectory tokens | 78819.00 | 66358.00 | -12461.00 | -12461.00 | -12461.00 | 1 |
| Input tokens | 78485.00 | 65753.00 | -12732.00 | -12732.00 | -12732.00 | 1 |
| Output tokens | 334.00 | 605.00 | 271.00 | 271.00 | 271.00 | 1 |
| Tool calls | 4.00 | 3.00 | -1.00 | -1.00 | -1.00 | 1 |
| Duration — all attempts (ms) | 16611.14 | 20727.41 | 4116.27 | 4116.27 | 4116.27 | 1 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.00 | 2.00 | 1.00 | 1.00 | 1.00 | 1 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 16611.138610000125 ms
ON median: 20727.410108000186 ms
Paired Δ median: 4116.27149800006 ms
Paired Δ mean: 4116.27149800006 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| B-clone_policies | -12461.00 | 1589.00 | -7.84 |

| Token cost / verified success | 78819.0 | 66358.0 | -12461.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 2. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
