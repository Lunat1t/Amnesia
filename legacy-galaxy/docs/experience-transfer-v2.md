# Experience transfer v2: independent candidate pairs

Status: single-repetition agent calibration completed; no B success improvement observed. This protocol
is fixed before agent results. Dataset: `examples/experience-transfer-v2/candidates.json`.

Three isolated pairs cover exclusive expiration boundaries (None versus zero),
independent copying of nested data with repeated input aliases, and collision
rejection after Unicode casefolding. A and B operate on different functions in
the same frozen source. The external verifier checks the specified behavior,
input preservation and the unchanged AST of the other function. Reference fixes
are evaluator calibration only and never enter agent repositories or prompts.
These candidates cover more edge cases than v1; difficulty is not established.

Prepare once into a fresh directory:

```bash
PYTHONPATH=. python scripts/prepare_experience_transfer_v2.py /tmp/galaxy-transfer-v2-prepared
```

Each pair directory contains a clean Git fixture, suite config and a B-only
context-only control. Each suite uses three repetitions and 5000 context tokens.
Use separate output/runtime directories for every pair and condition, the same
explicit model and 60-second per-invocation timeout for initial calibration.
Do not reuse another pair's Experience. Run the existing `benchmark run` CLI
with that pair's `suite.json`, then its `context-only.json`. Initial calibration
may override repetitions to one; frozen measurement uses three.

Primary comparison is B verified success with context + Experience versus B
with context only. OFF is an additional baseline. Audit matching source commit,
non-Experience context items, source A verifier-log hashes, delivered episode
IDs, and an uncontaminated empty control store. Missing A extraction or delivery
makes the transfer contrast unavailable, not a treatment failure. A failed run
may produce a failure hypothesis; do not label it verified-success advice.
Infrastructure failures remain separately reported. Preserve all runs and ties.
Do not tune criteria against results. Packet differences beyond Experience
invalidate the intended isolated contrast and must be reported.

Secondary measures: `agent_usage` and `agent_duration_ms` for task execution;
`experience_extraction_usage` and `experience_extraction_ms` for learning cost.
Existing top-level tokens/duration retain legacy combined accounting. Compare
agent costs only at equal verified completion; report learning overhead separately.
Unknown provider prices and semantic usefulness remain unavailable. A small
synthetic suite cannot establish general benefit. Three repetitions support
an initial diagnostic signal, not statistical certainty. Advance only with
intact evidence, independent history, delivered experience and repeatable benefit
without unexplained regressions; otherwise report null effect or harm.

`reports/experience-transfer-v2/preflight.json` contains all twelve baseline /
reference checks: every baseline failed and every reference passed. No agent
outcome was measured in this verifier calibration.


## Agent calibration result (2026-10-03)

All three experience suites and context-only controls completed: 18 agent task runs.
All verifier logs passed SHA-256 audit; every pair delivered linked A experience
to B with matching non-Experience context and identical source commits. All B
conditions passed, giving no success improvement. Agent token differences were
mixed (expiry lower, copying and normalization higher with Experience).
Complete results: `reports/experience-transfer-v2/calibration/results.md` and
`audit.json`, with raw traces and extraction costs. These fixtures are retained
as calibration; the next benefit study should use harder real repository pairs
and irrelevant/stale-memory controls before increasing repetitions.
