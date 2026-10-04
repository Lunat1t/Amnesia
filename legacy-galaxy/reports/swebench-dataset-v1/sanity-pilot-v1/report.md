# Galaxy Benchmark v1.0

Pilot analysis: paired Galaxy OFF/ON outcomes

Verified paired outcome differences: 0/5. Infrastructure and evidence artifacts were recorded.
Context efficiency: heterogeneous. Experience effect: not tested.

## Paired outcomes

| OFF \ ON | PASS | FAIL |
|---|---:|---:|
| PASS | 3 | 0 |
| FAIL | 0 | 2 |

## Numerical metrics: marginal summaries and paired treatment effects

Positive paired Δ means ON used more / took longer; negative means less / faster.

| Metric | OFF median | ON median | Marginal difference (ON−OFF) | Median paired Δ | Mean paired Δ | Complete pairs |
|---|---:|---:|---:|---:|---:|---:|
| Trajectory tokens | 358733.00 | 388870.00 | 30137.00 | 84179.00 | 168015.60 | 5 |
| Processed input tokens | 355923.00 | 387065.00 | 31142.00 | 83977.00 | 167286.20 | 5 |
| Cached input tokens | NA | NA | NA | NA | NA | 0 |
| Uncached input tokens (not a billing estimate) | NA | NA | NA | NA | NA | 0 |
| Output tokens | 1468.00 | 1721.00 | 253.00 | 337.00 | 729.40 | 5 |
| Tool calls | 10.00 | 15.00 | 5.00 | 2.00 | 4.80 | 5 |
| Duration — all attempts (ms) | 138306.68 | 160867.31 | 22560.63 | 18804.33 | 22573.49 | 5 |
| Context assembly (ms) | NA | NA | NA | NA | NA | 0 |
| Galaxy context token estimate | NA | NA | NA | NA | NA | 0 |
| Rendered context characters | NA | NA | NA | NA | NA | 0 |
| Unique files opened | 2.00 | 2.00 | 0.00 | 0.00 | -0.20 | 5 |

## Verified completion time

Only runs that passed SWE-bench are included; this is not an all-task completion-time result.

Successful complete pairs: 3
OFF median: 166737.64170600133 ms
ON median: 160867.30586200065 ms
Paired Δ median: 18804.33121399983 ms
Paired Δ mean: 21367.754744332768 ms

## Interpretation

One repetition per task and arm is descriptive only. The pilot does not establish a Galaxy benefit.
Usage is read from the latest cumulative Codex trace snapshot; traces and extraction are retained for audit.
Context amplification is a debugging signal, not a quality KPI.

## Context amplification diagnostic

| Task | Trajectory token Δ (ON−OFF) | Galaxy context estimate (approx.) | Δ / estimate |
|---|---:|---:|---:|
| matplotlib__matplotlib-13989 | 84179.00 | NA | NA |
| django__django-13033 | 17274.00 | NA | NA |
| sphinx-doc__sphinx-8548 | -61839.00 | NA | NA |
| sympy__sympy-13878 | 666902.00 | NA | NA |
| django__django-13406 | 133562.00 | NA | NA |

| Processed tokens / verified success (all attempts) | 543030.3333333334 | 823056.3333333334 | 280026.0 |
| Currency cost / verified success | NA | NA | NA |

Runs: 10. Raw records and evidence logs are in `runs/`, `runs.jsonl`, and `runs.csv`.
Unavailable telemetry and unrun comparisons are shown as NA; no values are imputed.
