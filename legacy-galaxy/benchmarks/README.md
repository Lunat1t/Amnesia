# Galaxy Benchmark Suite v1.0

This suite measures the effect of Galaxy context on writable software-engineering
tasks. Its primary comparison is **the same Codex model, task, repository commit,
CLI tool set, timeout, and run count**, with Galaxy compiled context added only in
the treatment arm. Each repetition/mode gets a clean disposable clone. The source
repository must be a clean Git checkout.

## What it measures

Each task is evaluated by its authored deterministic verifier command. `success`
means the agent command completed; `verified_success` additionally requires a
passing verifier and a persisted verification log whose SHA-256 matches the
evidence ledger. Summary reports include counts, Wilson 95% intervals for
success rates, mean/median/stdev/P25/P75/P95/min/max for observed numeric
telemetry, and paired task/repetition differences. Missing provider telemetry
remains null. Reports include JSON, JSONL, CSV, Markdown, HTML, and SVG/PNG charts.

The current Codex CLI trace supplies token totals and a partial tool/action
inventory. Provider-specific calls, time to first action, human interventions,
semantic memory use/help/harm, and known-error recurrence remain null unless
the trace or authored dataset provides auditable evidence. Do not interpret
null as zero. This release has no controlled cross-project claim: use separate
repository suites and do not aggregate them as transfer evidence without a
pre-registered transfer protocol.

## Configuration

Create a JSON file with an ordered task list. Dataset order is the experience
cutoff order. Sequential tasks can accumulate experience extracted by a
separate same-model pass over the actual agent trajectory, resulting patch hash,
and verifier evidence. Hand-authored `lesson` strings are rejected in the
primary A/B runner. Extraction latency and available token usage are included in
the treatment run totals. Verifiers run on the agent patch applied
to a fresh base clone, not on the agent's potentially contaminated process.
For multiple repositories, set `repositories` to an ID-to-local-path map and
set each task's `repository` to one of those IDs. All source checkouts must be
clean; their HEAD commits are recorded separately. A verifier may declare an
`overlay` map from repository-relative destination paths to external hidden
test files; their hashes are pinned in the manifest and files are copied only
into the verifier clone after the agent patch is applied.

```json
{
  "project": "sample-project",
  "repository": "sample-project",
  "repositories": {"sample-project": "/path/to/clean/sample-project"},
  "context_budget_tokens": 5000,
  "max_files": 16,
  "repetitions": 3,
  "tasks": [
    {
      "id": "bug-001",
      "task": "Fix the regression in the retry handler. Add a regression test.",
      "difficulty": "medium",
      "category": "bug_fix",
      "task_set": "sequential",
      "verification": {
        "type": "command",
        "argv": ["python", "-m", "unittest", "discover", "-s", "tests"],
        "expected_exit": 0,
        "timeout_seconds": 300
      }
    }
  ]
}
```

Supported difficulties: `easy`, `medium`, `hard`, `very hard`. Categories:
`bug_fix`, `feature`, `refactoring`, `cross_file`, `architecture`,
`regression`, `historical_experience`, and `misleading_experience`. Include
historical or misleading memory scenarios in separately labeled suites; the
primary runner excludes hand-authored memory to prevent answer leakage; a
controlled-memory runner is not implemented yet. The
source repository currently must be at
one clean base commit for all configured tasks.

## Run and rebuild a report

Install Galaxy and ensure the configured Codex CLI is authenticated. For
repeatable comparisons, provide a fixed model and reasoning effort, use at
least three repetitions, preserve the config and source commit, and avoid
changing model/provider settings during the run.

```bash
galaxy benchmark run benchmarks/my-suite.json \
  --repo /path/to/clean/repository \
  --out-dir reports/galaxy-benchmark-v1/run-001 \
  --model YOUR_CODEX_MODEL \
  --reasoning-effort medium \
  --repetitions 3
```

Rebuild summaries and charts from the saved records without calling a model:

```bash
galaxy benchmark report reports/galaxy-benchmark-v1/run-001
```

Output layout includes `manifest.json`, per-run prompt/events/answer/patch,
verification logs and hash ledgers under `runs/`, plus `runs.jsonl`, `runs.csv`,
`summary.json`, `report.md`, `report.html`, and `charts/`. Reports never insert
example values in place of unavailable results.

## Fairness and limits

Both arms use the same writable Codex CLI harness and task prompt. The treatment
arm appends the Context Compiler packet. Context assembly latency is recorded
separately; all other task limits should match. Galaxy runtime stores are rooted
under the benchmark run ID. `--temperature` and `--seed` are recorded as
requested metadata, but the Codex CLI may not accept/enforce these controls;
check the manifest and provider support before claiming they were fixed. The
runner currently does not set an API-level token budget and does not support
non-Codex providers. Claims must be scoped to the exact task suite, model,
repository snapshot, and run manifest.

This tool is a measurement harness, not evidence that Galaxy improves outcomes.
Publish failed runs, harm, incomplete telemetry, and the full raw run records.

## SWE-bench Verified import (stage 1)

The importer uses the official `SWE-bench/SWE-bench_Verified` Hugging Face
dataset, `test` split, pinned to revision
`8db12b107a1abfd10808f023ed233890b4d7cbae`. The upstream row fields include
`instance_id`, `repo`, `base_commit`, `problem_statement`, `patch`, `test_patch`,
`FAIL_TO_PASS`, `PASS_TO_PASS`, and `difficulty`.

Install optional Python packages and ensure Docker is running before auditing:

```bash
pip install '.[benchmark]'
galaxy benchmark dataset import swebench-verified \
  --out-dir benchmarks/imports/swebench-verified-v1
galaxy benchmark dataset snapshot \
  benchmarks/imports/swebench-verified-v1 django__django-12345 \
  --out-dir benchmarks/snapshots/django__django-12345
galaxy benchmark dataset audit \
  benchmarks/imports/swebench-verified-v1 django__django-12345
galaxy benchmark swebench-pilot \
  benchmarks/imports/swebench-verified-v1 django__django-12345 \
  --out-dir reports/swebench-pilot/django__django-12345 \
  --galaxy-home /tmp/galaxy-swebench-pilot --model YOUR_CODEX_MODEL
```

The importer writes an agent-visible `tasks/<id>/task.json` and `metadata.json`.
Gold patches, test overlays, and test identifier lists are stored only in the
separate `_hidden/<id>/` tree. The catalog records both hashes and marks tasks
`pending`; import alone is not an audit. Do not put `_hidden/` under a repository
used as the agent's working clone or Galaxy context source. The pilot integration
must apply `test_patch` only in a fresh verifier environment after the agent
patch, then require every `FAIL_TO_PASS` and `PASS_TO_PASS` check to pass. Gold
patch validation must use a separate fresh clone. The official SWE-bench
evaluator uses Docker for reproducible task environments. This checkout has no
Docker executable or SWE-bench runtime, so no task has been audited here yet.
The audit command performs two separate official-harness runs (empty base patch
and gold patch), stores their reports/logs, and accepts only a baseline F2P
failure with P2P preserved plus complete gold F2P/P2P success.
The pilot command accepts only an `accepted` task with a materialized snapshot.
During each agent process, all imported evaluator-only files and previous-arm
patch/trajectory artifacts are temporarily removed from disk; the agent sees
only its checked-out repository, issue statement, and (for ON) compiled Galaxy
context. Evaluator artifacts are restored after both arms finish. The pilot
still requires a separate security review of the Codex sandbox before claiming
host-wide isolation guarantees.
