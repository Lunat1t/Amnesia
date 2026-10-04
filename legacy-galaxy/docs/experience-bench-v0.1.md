# ExperienceBench v0.1 protocol

This is a **calibration protocol**, not a claim that Galaxy beats baseline.
The CLI compares the same ordered task suite and read-only repository snapshot
in three independent arms:

| Arm | Agent input | Question answered |
|---|---|---|
| `baseline` | Task + repository access | How does Codex do without Galaxy memory/context? |
| `raw` | Baseline + retrieved episode records | Does retrieved prior experience help or harm? |
| `compiled` | Baseline + bounded Galaxy Context Packet | Does compilation preserve useful experience more efficiently? |

The primary contrasts are baseline-vs-raw (experience utility) and raw-vs-
compiled (compression/selection loss). Retrieval recall is reported separately;
retrieving a memory never counts as task success by itself.

## Evaluators

1. **Deterministic criteria/checks:** `must_include`, `must_include_any`,
   `must_not_include`, structured `json_subset`, repository `file_exists` /
   `file_contains`, and optional authored commands. Phrase matching is a
   lexical check, not semantic understanding. Commands run only with
   `--run-checks`, in a disposable copy of the repository, without a shell.
2. **Semantic rubric:** per-task `semantic_rubric` with a prose criterion,
   pass/fail conditions, and evidence. `--semantic-judge` invokes Codex as a
   separate blinded evaluator. It saves the criterion, answer, full judge
   prompt, raw result, reason and model. This is an auditable model judgment,
   not ground truth; use a different judge model when feasible.
3. **Memory/provenance:** the same optional judge labels episode IDs used,
   helpful, or presented as fact while `verified=false`. These are explicitly
   heuristic labels. Exact source verification and future/stale-memory gates
   remain deterministic.

If a semantic rubric is present but no semantic judge is enabled, semantic and
overall task success are `null`, not silently inferred from string criteria.
Metrics the runner cannot observe (for example provider tool-call events) are
`null`, not guessed.

## Temporal and arm isolation

- Every task gets an ISO UTC `memory_cutoff` before any arm is executed.
- Only observations from earlier completed task entries can be eligible.
- Dataset references to future/missing memories fail validation before model
  calls. At runtime, eligible/retrieved/delivered IDs are checked against the
  prior-observation set; any leak aborts the run.
- `stale_prior` must also appear in `retire_prior`; those IDs are retracted
  before the cutoff and recorded as stale candidates. A corrected observation
  is not available until after its own source task finishes.
- Each repetition and arm has a distinct ExperienceStore/cache directory.
  Codex uses independent ephemeral, read-only sessions on the same unchanged
  repository snapshot. Repository content is hashed before and after each
  repetition; a change aborts the run.

Each arm/task artifact records `eligible_memory_ids`, `retrieved_memory_ids`,
`delivered_memory_ids`, stale candidates and the cutoff. The funnel reports
eligible → retrieved → delivered → used → helpful. `used/helpful` are null
without the semantic judge. Benefit, harm and no-effect are paired task-level
comparisons against baseline, never proxies for Recall@K.

## Dataset schema and controlled candidate

Dataset tasks are ordered. An `observation` attached to a task becomes
available only after that task; it may include outcome, lesson, evidence,
confidence and `verified`. Synthetic annotations must stay unverified. Later
tasks name applicable memories with `gold_prior`; stale entries use
`stale_prior` and `retire_prior`.

`examples/experience-bench/experiencebench-v0.1-candidate.json` contains 12
controlled scenarios covering useful transfer, unrelated work, partial
transfer across webhook/token domains, a repeated failure hypothesis,
superseded advice, correction, and unverified provenance. Its paired fixture
repository is `examples/experience-bench/refresh-service/`. This is a
candidate dataset and must be calibrated before freezing; do not tune its
criteria after inspecting a frozen result.

## Calibration and frozen run

Calibration (small prefix, not a result claim):

```bash
galaxy experience-bench examples/experience-bench/experiencebench-v0.1-candidate.json \
  --repo examples/experience-bench/refresh-service \
  --out-dir /tmp/experiencebench-calibration \
  --limit 2 --repetitions 1 --semantic-judge
```

After auditing prompts, rubrics, evaluator disagreements, token counters and
all failures, freeze the dataset and launch the planned experiment:

```bash
galaxy experience-bench examples/experience-bench/experiencebench-v0.1-candidate.json \
  --repo examples/experience-bench/refresh-service \
  --out-dir benchmarks/experiencebench-v0.1-frozen \
  --repetitions 3 --semantic-judge --model YOUR_CODEX_MODEL --freeze-manifest
```

Every new output directory receives an immutable `manifest.json` with dataset
SHA-256, repository commit/tree hash and dirty status, Galaxy commit/tree hash,
Codex version/config hash, model, evaluator configuration, repetitions and
timestamp. A frozen run requires an explicit model and identifiable snapshots.
The manifest is written before calls; an existing manifest is never
overwritten. `summary.json` and `summary.md` aggregate mean/median/min/max and
standard deviation across repetitions. Per-task/per-arm/per-run folders keep
the prompt, answer, Codex JSONL events, metrics, evaluation and memory
eligible/retrieved/delivered artifacts.

## Metrics and limits

The report includes task/criterion/semantic pass rates, input/cached-input/
output/total tokens, wall time, tool-call counts, memory funnel counts and
transition rates, experience hit/precision, false-memory injections, stale
memory delivery, future leakage, unverified-as-fact rate, and baseline-paired
Memory Benefit/Harm/No Effect rates. Unsupported counters and unrun judges are
null. Judge token usage is kept separate from agent token usage.

This v0.1 runner is read-only: it does not evaluate successful code edits or
claim deterministic test-pass rates for agent changes. Tool-call telemetry
depends on Codex JSONL event coverage. A 12-task candidate and one calibration
run are not statistically powered evidence of a general Galaxy Effect. Keep
the complete manifest, outputs, and failures; do not claim Galaxy is better
from a positive-looking calibration.
