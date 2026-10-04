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
| Trajectory tokens | 55093.00 | 124831.00 | 69738.00 | 69738.00 | 69738.00 | 2 |
| Input tokens | 54815.50 | 124013.50 | 69198.00 | 69198.00 | 69198.00 | 2 |
| Output tokens | 277.50 | 817.50 | 540.00 | 540.00 | 540.00 | 2 |
| Tool calls | 2.50 | 4.50 | 2.00 | 2.00 | 2.00 | 2 |
| Duration — all attempts (ms) | 16695.81 | 37210.37 | 20514.56 | 20514.56 | 20514.56 | 2 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 1.50 | 3.00 | 1.50 | 1.50 | 1.50 | 2 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 1
OFF median: 18711.671286000183 ms
ON median: 31937.8042430003 ms
Paired Δ median: 13226.132957000118 ms
Paired Δ mean: 13226.132957000118 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context tokens | Δ / context token |
|---|---:|---:|---:|
| A-clone_profiles | 54897.00 | 1589.00 | 34.55 |
| B-clone_policies | 84579.00 | 1853.00 | 45.64 |

| Token cost / verified success | 110186.0 | 124831.0 | 14645.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 4. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
