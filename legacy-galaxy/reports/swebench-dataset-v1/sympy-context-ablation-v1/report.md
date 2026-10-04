# SymPy context ablation — SWE-bench Verified

Five single-run conditions on the same audited issue and model. A/B reuse the already completed frozen sanity-pilot runs; C/D/E are new official SWE-bench evaluator runs.

## Results

| Arm | Context condition | Verified | Trajectory tokens | Context text tokens (chars/4 approx.) | Searches | Unique files opened | Repeat reads | Edit events | Tests | Duration (s) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | off | FAIL | 358733 | — | 5 | 2 | 3 | 1 | 0 | 138.3 |
| B | galaxy_current | FAIL | 1025635 | 1161 | 7 | 2 | 2 | 14 | 0 | 178.9 |
| C | top3 | PASS | 1056719 | 1007 | 11 | 2 | 4 | 6 | 0 | 178.4 |
| D | top1 | FAIL | 376234 | 974 | 4 | 1 | 1 | 3 | 0 | 122.9 |
| E | without_ctx_004 | FAIL | 466626 | 1162 | 5 | 3 | 3 | 3 | 0 | 125.0 |

## Context influence observed by file path

A file marked opened or touched is an observed path match from the trace, not proof that its content helped. Semantic context use and entity use remain unknown.

| Arm | First opened files | Supplied context files later opened | Supplied context files later edited |
|---|---|---|---|
| A | `sympy/stats/crv_types.py`, `sympy/stats/crv.py` | — | — |
| B | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` |
| C | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` |
| D | `sympy/stats/crv_types.py` | — | — |
| E | `sympy/stats/crv_types.py`, `sympy/stats/crv.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv.py`, `sympy/stats/crv_types.py`, `sympy/stats/tests/test_continuous_rv.py` | `sympy/stats/crv_types.py` |

## Interpretation

The outcome difference between A and the Galaxy arms is descriptive: each arm ran once, and the model is stochastic. The A/B traces are legacy JSONL without per-action timestamps; C/D/E use the v1.1 live event clock. Per-action token totals are not emitted by Codex and remain unknown.

rank 4 in the frozen current packet is sympy/core/tests/test_args.py, a downstream test outside the changed component and outside the agent's observed first reads; this is a hypothesis for ablation, not a finding of causal harm.

Every arm has a distinct Codex run ID. Full observable action traces, exact rendered context, structured context inventory, agent patch, and official evaluator artifacts are retained in each arm directory.
