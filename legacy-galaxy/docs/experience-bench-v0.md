# ExperienceBench v0

ExperienceBench runs three isolated Codex arms against the same ordered tasks
and repository snapshot:

1. **baseline** — task plus repository access, without Galaxy memory/context;
2. **raw** — task, repository access and retrieved episode records;
3. **compiled** — task, repository access and the bounded Galaxy Context Packet.

The runner uses `codex exec --json` in read-only, ephemeral sessions. Each arm
has a distinct runtime store; annotated observations become available only
after their source task. `gold_prior` must cite earlier `(run_id, node_id)` pairs.
The runner rotates arm order deterministically across tasks and retains each
answer, event stream, stderr log, and `report.json` under `--out-dir`.

## Dataset

```json
{
  "project": "refresh-demo",
  "tasks": [
    {
      "id": "learn-contract",
      "task": "Review refresh token rotation and state what the repository specifies about retries.",
      "criteria": {"must_include": ["not specified"]},
      "observation": {
        "run_id": "review-1",
        "node_id": "retry-contract",
        "outcome": "success",
        "summary": "Captured the client retry contract for refresh rotation.",
        "lesson": "For the same idempotency key, return the original successor token; do not mint another.",
        "evidence": ["synthetic annotation; confirm with service owner"],
        "verified": false
      }
    },
    {
      "id": "apply-contract",
      "task": "A refresh request timed out and is retried with the same idempotency key. Recommend behavior and a regression test.",
      "gold_prior": [["review-1", "retry-contract"]],
      "criteria": {"must_include": ["same successor"], "must_not_include": ["repository proves this"]}
    }
  ]
}
```

`criteria` are simple case-insensitive answer substring checks, not a code
verifier. `must_include` terms must all appear, `must_include_any` is a list of
alternative-term groups (one match per group), and `must_not_include` terms may
not appear. Prefer multiple accepted phrasings; brittle exact substrings can
mis-score a semantically correct answer. Criteria are not included in prompts.
Observations are benchmark annotations, not model-generated learning; keep
their evidence status honest. Do not mark synthetic lessons verified.

## Run

```bash
galaxy experience-bench tasks.json \
  --repo /path/to/frozen/repository \
  --out-dir benchmarks/experience-run-01 \
  --budget-tokens 5000 --max-files 16
```

This invokes Codex once per task per arm. `report.json` records criterion
success, retrieved/gold episode counts, estimated attached context tokens,
Codex JSONL input/cached-input/output token counters, compilation time and
wall time, experience precision/recall, false injections, and counts of
unverified retrieved episodes. A missing provider counter is reported as zero
and is not an estimate. Inspect `limitations` before interpreting the results.

The benchmark is read-only and evaluates answers, not edits or deterministic
test passes. Repository access is available to all arms, so Codex may inspect
files itself even when a packet is supplied. A small successful run is a
mechanism diagnostic, not evidence of a general Galaxy effect. Use frozen task
text and commits, multiple failure categories, held-out cases, and publish all
arms including failures before making outcome claims.
