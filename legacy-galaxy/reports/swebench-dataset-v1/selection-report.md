# SWE-bench Verified Dataset v1 audit and selection report

Candidate pool: 72 tasks; frozen neutral pool hash `c09a2aae35baf0a5c7923332e8399251f4eb79c9f8b0833ded13127b80df1ebe`.
Official base/gold audit: 55 accepted, 0 rejected, 17 infrastructure pending.
The 17 pending tasks have no official base/gold per-instance reports because SWE-bench could not pull task-specific Matplotlib images from Docker Hub (404). They were not counted as test failures.

## Audit by repository

| Repository | Candidates | Accepted | Rejected | Infra pending |
|---|---:|---:|---:|---:|
| django/django | 18 | 18 | 0 | 0 |
| matplotlib/matplotlib | 18 | 1 | 0 | 17 |
| sphinx-doc/sphinx | 18 | 18 | 0 | 0 |
| sympy/sympy | 18 | 18 | 0 | 0 |

## Frozen 30-task selection

Selection used accepted audits only, the preregistered repository balancing and deterministic difficulty/patch-size rotation, and no Galaxy performance or retrieval outcomes.
Repository targets after redistribution: `{"django/django": 10, "matplotlib/matplotlib": 1, "sphinx-doc/sphinx": 10, "sympy/sympy": 9}`.
Difficulty counts: <15 min fix: 11, 15 min - 1 hour: 9, 1-4 hours: 8, >4 hours: 2.

| Repository | Selected |
|---|---:|
| django/django | 10 |
| matplotlib/matplotlib | 1 |
| sphinx-doc/sphinx | 10 |
| sympy/sympy | 9 |

## Pending infrastructure candidates

- `matplotlib__matplotlib-23476` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-26113` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-26208` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-24177` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-24570` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-25332` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-20676` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-25287` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-23314` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-26291` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-24627` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-23299` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-23412` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-26342` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-22871` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-24637` — missing task-specific SWE-bench Docker image (registry 404).
- `matplotlib__matplotlib-25775` — missing task-specific SWE-bench Docker image (registry 404).

## Integrity evidence

Dataset SHA-256: `9f0dd9bc9644e2b1ca6ee4965291487e884d873c2f291a06aa773d936f0ae278`.
Leakage audit: 30/30 passed.
Manifest: `benchmarks/datasets/dataset-v1-manifest.json`.
Incomplete/infra attempts are preserved under `reports/swebench-dataset-v1/infra-attempts/`.
