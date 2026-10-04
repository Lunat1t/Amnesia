# Real-repository Experience transfer: calibration v2

Status: frozen before the first agent run. This is a one-repetition pipeline and
relevance calibration, not the primary Experience benefit study.

## Frozen tasks and hypothesis

Dataset: local imported SWE-bench Verified SymPy snapshots.

- Source A: `sympy__sympy-13091`, rich comparisons with unknown Python types.
- Intervening task: `sympy__sympy-22914`, PythonCodePrinter support for `Min`/`Max`.
- Target B: `sympy__sympy-17139`, a complex exponent triggers an invalid ordering comparison during trigonometric simplification.

The candidate transfer is a general caution about forcing an unsupported
comparison decision. The source and target are in different subsystems, so
relevance is uncertain. The extracted lesson must be supported by A's actual
trajectory, patch, and passing evaluator evidence; if it does not match the
preregistered hypothesis, the relevant arm is unavailable. Do not author a
lesson to fit the hypothesis.

Independent review found the earlier candidate target
`sympy__sympy-15875` too easy and too explicit for a primary benefit study. Its
separate frozen preflight remains at
`reports/real-experience-transfer-v2/preflight.json`; it has no agent runs and
is superseded before execution. The reviewer recommended treating the present
pair only as calibration. See the contained design note in this document;
there is no new product-scope decision.

## Integrity and conditions

The companion preflight is `reports/real-experience-transfer-v2-calibration/preflight.json`.
It records the frozen plan hash, source snapshot commits and hashes, exact
public-task hashes, accepted base/gold audits, hashes of gold/evaluator
artifacts, dataset revision, SWE-bench version, and successful Podman API ping.
Hidden evaluator files stay unavailable to the coding agent.

Target arms, in fixed order:

1. **control** — ordinary Galaxy context, empty Experience store.
2. **relevant** — verified extracted A episode, only if its actual lesson
   supports the transfer hypothesis.
3. **irrelevant** — verified extracted episode from the intervening task.

No obsolete arm is included: no target-specific supersession evidence exists.
This experiment forces audited exposure and does not measure native retrieval.
Delivery, file opens, or the agent's self-report do not prove semantic use or
benefit.

## Frozen execution settings

The manifest records model `gpt-6-luna`, reasoning effort `medium`, 900-second
timeout, 5,000-token Galaxy context budget, 16-file cap, and one calibration
repetition. Reasoning effort is raised from the previous `low` runs after two
distinct incomplete fixes; this steering is exploratory, not a validated
permanent team rule. There is no currency-cost claim because no applicable
dated price schedule is configured.

Source A and the intervening task each run through the existing SWE-bench
agent/evaluator path. Preserve every failure. Extract only from a passing run
with intact metrics, evidence log, patch, trace, and official evaluator report.
Run B arms only after both verified source episodes exist and the relevant
lesson passes the preregistered semantic gate. Compare packet inventories and
hashes; invalidate the contrast if non-Experience context differs.

One repetition is descriptive calibration only. A tie or token difference is
not evidence of product benefit. If the source or intervening task fails, stop
the corresponding arm rather than repairing its patch by hand or relabeling a
failure as Experience.

## Evidence classes

- **Internal evidence:** current-state/foundation maps and the frozen local
  dataset audits support runtime boundaries, task commits, and evaluator
  integrity. Prior v1 calibration records no verified real-task episodes.
- **External evidence:** none is used here to claim Galaxy benefit. SWE-bench
  issue reports are task inputs, not independent evidence that Experience
  helps.
- **Galaxy hypothesis:** comparison handling may transfer between these tasks;
  only the controlled run can test whether the actual lesson helps, is neutral,
  or causes harm.

The accepted scope remains Context, Memory, Experience, Skills/Learning, and
Evidence. This benchmark does not justify a new retrieval, runtime, or
orchestration component.

## Outcome (2026-10-04)

The calibration stopped before target B, as required by the frozen source gates:

- Source A (`sympy__sympy-13091`) did **not** resolve. Official SWE-bench reported
  `test_equality` passing but `test_comparisons_with_unknown_type` failing;
  all 89 pass-to-pass tests passed. The agent changed `Basic.__eq__` to return
  `NotImplemented` for an unknown type and updated `__ne__` to propagate it.
  Its answer reports that it could not run local tests because `pytest` was
  unavailable. The official test failure is the decisive evidence; this run
  is not eligible for Experience extraction. Evaluator report SHA-256:
  `8b0a166b06489a4f0503e47dc165dfd2177241feda0993b65b6e974e833722ac`.
- The intervening task (`sympy__sympy-22914`) resolved: 1/1 fail-to-pass and
  17/17 pass-to-pass tests passed. Its leakage audit also passed. Evaluator
  report SHA-256:
  `959d8ff63ff1e67afe6ffe2ee301475a210e6e8693568cbbac1032d9b309bcf9`.
- Hidden gold/evaluator artifacts were absent during both agent runs, and both
  leakage audits passed. The A failure means no relevant Episode can be
  extracted; therefore neither B condition order nor any B result exists.
  The passing intervening task alone is not a transferable control Episode.

This establishes a pipeline result, not a Galaxy effect: the official
evaluator and leakage checks can distinguish one incomplete patch from one
verified fix, while the source-task run had no local pytest feedback. The
comparison-transfer hypothesis remains untested. Preserve both runs as-is; do
not hand-repair A and call it an Experience episode. A future calibration
requires a newly frozen source episode that passes its evaluator gate before
target B starts.
