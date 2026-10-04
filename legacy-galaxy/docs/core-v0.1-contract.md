# Archived experiment contract: experience transfer v0.1

> This document predates the narrowed Galaxy direction. It records a prior experiment contract, not an active Core architecture mandate. The current scope is defined by [`architecture/foundation.md`](architecture/foundation.md) and its actual code boundaries by [`architecture/current-state.md`](architecture/current-state.md).

## Purpose

Core v0.1 demonstrates one narrow claim: **evidence-backed experience from an
earlier run can improve the context and verified outcome of a later, independent
run without exceeding its context budget**.

This is a contract over existing Galaxy components, not a replacement architecture.
The repository already has a persistent World Model and change feed, hybrid
Attention, a budgeted Context Compiler, sourced experience episodes, a verification
ledger, and a DAG executor. The v0.1 work connects and evaluates these pieces.

## The vertical slice

```text
observe project snapshot
  → compile bounded ContextPacket (including eligible prior experience)
  → execute task through an external agent or Galaxy DAG runner
  → run deterministic verification
  → record episode with run/node provenance and verified evidence
  → compile context for a later independent task
  → compare against an isolated no-experience baseline
```

The first acceptance scenario is a small, reproducible series of related coding
tasks in one repository. A first run encounters or resolves a labeled failure
pattern. A later task recreates the relevant condition. The enabled run may receive
the earlier episode; the baseline must not. Both arms use the same task, model,
harness, repository snapshot, and execution budget.

## Contracts

### Observation and state

- Every packet identifies its project and stable World Model snapshot.
- A packet must not mix repository states: if the source changes during compilation,
  compilation refreshes/retries or returns an explicit error.
- Incremental observation is an implementation detail; the snapshot and source
  evidence remain authoritative.

### Context packet

- `ContextCompiler` is the single assembly path for task context.
- The packet has a hard caller-supplied token budget. Experience is a bounded,
  lower-priority allocation and may be trimmed to preserve task/code evidence.
- Every included episode identifies its source run and node, outcome, confidence,
  and evidence status. Episodes are advice/observations, not proof of current code.
- Cache identity includes project snapshot and memory/experience state; stale packets
  must not be served after any of these inputs change.

### Verification and learning

- Agent claims such as `DONE`, `PASS`, and free-form evidence strings do not establish
  verification.
- A verified outcome requires a passing deterministic command recorded in the
  Galaxy ledger, with its saved bytes matching the recorded digest.
- An experience episode is marked verified only while its linked verification
  evidence passes that integrity check.
- Consolidated procedures and rules remain candidates until explicit evaluation
  and promotion. Contradictory evidence prevents promotion or triggers review;
  old knowledge remains auditable as historical/superseded rather than silently
  disappearing.

### Isolation

- Baseline and experience-enabled benchmark arms use isolated memory/experience
  stores, so baseline cannot accidentally retrieve the treatment's episodes.
- Project, owner, and team fields are scope selectors in the local prototype, not
  authenticated identities. Do not expose them as a multi-user security boundary.

## First benchmark and acceptance gate

Start with a small labeled suite (at least 12 ordered task pairs across at least 3
failure categories; include tasks where prior advice is irrelevant or misleading).
Freeze task text, repository commits, model/provider, harness, command set, token
and time budgets before running the paired comparison. Reset both arms between
independent series. Report per-task results and aggregate results; do not treat
retrieval alone as evidence of improved agent performance.

Required measures:

| Measure | Definition |
| --- | --- |
| Verified completion | Task succeeds and required deterministic checks pass with intact evidence. |
| Repeated error rate | Labeled prior error category recurs in a later applicable task. |
| Experience reuse rate | Applicable prior episode is retrieved and included in the packet. |
| False-use rate | Irrelevant or contradicted experience is included or causes a worse decision. |
| False blocks | A learned rule prevents a task that reviewers label as allowed. |
| Context cost | Packet tokens and total model input tokens, reported separately. |
| Time to verified completion | Wall time through passing verification, including retries. |
| Human interventions | Reviewer/user interventions per completed task. |

Acceptance is not a single cherry-picked success. Publish the complete paired
results, failures, packet traces, and evidence audit. The initial gate is: no
verification-integrity failures; no baseline contamination; packet budgets obeyed;
and the experience-enabled arm improves verified completion or repeated-error
rate without a material regression in false-use, false-block, total token, or
time measures. If the small suite is underpowered or inconclusive, report that
and expand it instead of claiming the Galaxy Effect.

ContextBench remains a separate retrieval-quality evaluation. ScaleBench is a
later performance evaluation for small/medium/large repositories; neither can
substitute for this end-to-end paired experience experiment.

## Explicitly out of scope for this contract

- Replacing the existing stores with a universal `MemoryObject` schema.
- A general temporal knowledge graph or arbitrary entity graph.
- Automatic promotion of model-written skills/rules.
- Building another agent runtime, IDE, SaaS product, or UI.
- Claiming authentication from CLI owner/team/reviewer strings.
- Claiming better outcomes from packet retrieval, synthetic tasks, or heuristic
  retrieval signals alone.

## Mapping to current implementation

| Contract concern | Existing implementation |
| --- | --- |
| Project observation and temporal snapshot | `galaxy_core/world/`, `galaxy_core/kernel/` |
| Retrieval and bounded packet compilation | `galaxy_core/attention/`, `galaxy_core/context/compiler.py` |
| Experience record/search/retraction | `galaxy_core/context/experience.py` |
| Paired retrieval replay | `galaxy_core/benchmark/continuity.py` and CLI `experience-eval` |
| Deterministic checks and evidence ledger | `galaxy_core/engine/verification.py`, autonomy engine |
| Candidate rule lifecycle | `rule-suggest`, `rule-eval`, `rule-promote`, `rule-disable` |

The key remaining proof is end-to-end paired execution with an external agent or
the DAG runner. The current continuity replay measures retrieval and packet cost;
it does not establish fewer repeated mistakes, faster completion, or higher
verified success. Current local stores also do not provide authenticated
multi-user isolation.
