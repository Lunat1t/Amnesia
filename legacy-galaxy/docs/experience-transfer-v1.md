# Galaxy 5.0: CSV experience transfer pilot

Status: prepared pilot; verifier calibration completed. Initial sandbox agent run failed before task execution because Codex could not write its service state. No benefit claim.

## Hypothesis and fixed tasks

Task A fixes whitespace-only numeric fields in `import_prices`. Task B fixes
`import_quantities` in a fresh clone of the same baseline. Both preserve zero,
row order, CSV quoting and errors for invalid nonempty input. Task A must not
change Task B's importer. Only trajectory-derived experience from completed A
may enter B; no reference patch or verifier is supplied in agent prompts.

The fixture is intentionally easy. This is a plumbing calibration: ceiling
performance is plausible and a tie cannot establish that memory is ineffective
on harder tasks. Reference fixes are used only to calibrate the evaluator.

## Preparation and execution

From the Galaxy checkout:

```bash
PYTHONPATH=. python scripts/prepare_experience_transfer_v1.py /tmp/galaxy-transfer-v1-prepared
python galaxy.py benchmark run /tmp/galaxy-transfer-v1-prepared/suite.json \
  --repo /tmp/galaxy-transfer-v1-prepared/repo \
  --out-dir /tmp/galaxy-transfer-v1-calibration \
  --galaxy-home /tmp/galaxy-transfer-v1-state \
  --model YOUR_MODEL --repetitions 1 --timeout-seconds 60
```

Preparation refuses an existing destination, creates a separate clean Git
fixture, validates the suite config, and hashes fixture/config/verifier files
in `freeze.json`. This is separate from the Galaxy checkout's missing Git metadata.
The verifier is installed through the existing overlay after execution. Each
arm/task runs in a private clone. The existing runner preserves context packages,
trajectories, patches, verification logs/hashes and experience provenance.

## Interpretation fixed before agent results

Primary observation: Task B verified completion. Secondary: Task B tokens,
wall time, searches, tool calls and supplied experience IDs. Inspect source run,
verification evidence and extracted lesson before interpreting transfer.
Missing telemetry stays null. Failed external-runtime runs are infrastructure
failures, never evidence against the hypothesis. Costs require known pricing;
unknown costs must remain unavailable.

The existing OFF/ON suite adds repository context as well as experience in ON.
Therefore its result measures overall Galaxy effect and cannot isolate Experience.
Before making an Experience-specific claim, add an isolated context-only control
using the same packet assembly and no previous episodes. Raw-vs-compiled testing
is covered separately by ExperienceBench v0.1, whose authored observations must
not be confused with independently verified coding experience.

Three repetitions are configured for a subsequent frozen pilot. Accept a pilot
only with intact verification, uncontaminated baseline, no future/stale delivery,
and inspectable source provenance. Benefit requires improved paired verified
completion or lower repeated-error rate; efficiency comparisons require equal
verified completion. Publish all failures and ties. One task pair supports no
general product claim. Skills remain candidates pending held-out evaluation.

## Local verifier calibration

`reports/experience-transfer-v1/preflight.json` records both original functions
failing the authored checks and both reference fixes passing. No model executes
in this calibration. These checks validate the fixture/evaluator, not Galaxy's
performance.

## Agent calibration attempts (2026-10-03)

Initial four agent invocations failed before execution because the sandbox made
Codex service state read-only; artifacts are retained in
`reports/experience-transfer-v1/sandbox-calibration`. An approved runtime retry
reached trace processing but the suite crashed on `targets: null` in an action.
`annotate_context_usage` now tolerates absent target lists; a direct regression
check confirmed null opens do not crash and a known edit remains linked.
The partial retry archive is in `reports/experience-transfer-v1/runtime-calibration`.
Neither attempt provides a completed paired result or evidence of Experience benefit.
A fresh full calibration remains necessary after the trace fix.

## Completed calibration and delivery diagnosis

The fresh `completed-calibration` archive contains four completed runs on
`gpt-6-luna`, one repetition, using the original frozen 2000-token config:

| Task | OFF verifier | ON verifier | ON delivered Experience |
|---|---|---|---|
| A prices | pass | pass | 0 |
| B quantities | fail | pass | 0 |

All four saved verifier logs matched their ledger SHA-256 hashes on audit.
A created `EXP-15013845a0653347` from its verified ON trajectory. Its lesson
concerned testing quoted numeric CSV input versus invalid nonempty input,
rather than the principal whitespace bug. B received no episode: this calibration
provides no causal evidence of Experience transfer. The single OFF/ON contrast
also does not establish a general Galaxy benefit.

An isolated offline replay copied the state, retracted B's future episode, and
compiled B using only A. At 2000 tokens, the compiler allocated 200 tokens to
Experience and retrieved nothing; at 5000, its 500-token allocation retrieved
and delivered A. The resulting packet estimated 1996 tokens. The exclusion
occurred during Experience retrieval allocation, not final packet trimming.
Evidence: `reports/experience-transfer-v1/A-only-budget-replay.json`.

The preparation script now defaults to 5000 tokens and accepts
`--context-budget-tokens`; reproduce the completed run's config with 2000.
The old manifest/config and results remain unchanged. A subsequent run must use
a new prepared directory and output. Before an Experience benefit claim, add
context-only treatment as specified above, verify nonempty A delivery to B,
and calibrate extraction quality on independent task pairs. Token totals in
sequential ON rows include experience-extraction usage; compare them accordingly.

## Context-only control

The paired suite accepts an explicit boolean `use_prior_experience` (default
true for compatibility). False uses a separate empty context store per task,
does not extract/store episodes, and aborts if an episode enters the packet.
Preparation emits `context-only.json` for B and includes it in the freeze hashes.
Run it with the same model, source fixture, context budget and timeout as
`suite.json`, using a new report directory and runtime root. Both suites still
include OFF; compare B's ON context-only outcome with B's ON experience outcome.
These are independent sessions; one repetition remains calibration, not a causal
or statistically reliable benefit claim. Verify source/context items as well as
Experience delivery before treating the prompts as a matched contrast.

## Controlled 5000-token calibration (2026-10-03)

`reports/experience-transfer-v1/controlled-audit.json` records six completed
runs and verifies all six verifier-log hashes. The experience suite produced
`EXP-87e8c977355b3d4d` from verified A; B received exactly that episode, with
source run `A-prices-rep-01-with_galaxy`. The separate context-only B received
zero episodes. B's non-Experience context items and file inventory match exactly
between treatment and control. Raw archives are `experience-5000` and
`context-only-5000`.

| B condition | Verified result | Delivered A episodes |
|---|---|---|
| OFF in experience suite | pass | 0 |
| ON context-only control | pass | 0 |
| ON context + Experience A | pass | 1 |

A's OFF failed and ON passed in the experience suite. This does not establish
Experience benefit, because A receives no past episode. B shows no success
improvement in this one repetition. Extraction costs are included in sequential
ON token totals; context-only performs no extraction, so these totals must not
be called an isolated inference-cost contrast. Per-run timings/tokens remain in
the audit. Memory semantic usefulness and repeated-error measurements remain
unknown. The delivery/provenance plumbing is calibrated; the fixture is likely
too easy for a meaningful benefit test. Next evaluation requires independent
harder task pairs and preregistered repeated runs, with inference and extraction
costs distinguished.
