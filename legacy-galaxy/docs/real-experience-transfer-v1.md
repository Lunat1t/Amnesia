# Real-repository Experience transfer: controlled challenge v1

Status: benchmark assembled and offline source/evaluator preflight passed.
No new agent runs or transfer outcomes have been collected. Existing historical
base/gold audits are evaluator calibration, not Experience-producing agent runs.

## Frozen candidate sequence

Repository: genuine upstream `sympy/sympy` snapshots from the imported SWE-bench
Verified dataset. Source A: `sympy__sympy-14711` (numeric zero in Vector addition).
An intervening unrelated maintenance task: `sympy__sympy-16766` (Indexed support
in PythonCodePrinter). Target B: `sympy__sympy-17630` (lost ZeroMatrix shape in
repeated BlockMatrix multiplication). Base commit, clean Git state, accepted
base/gold audit and hidden patch hashes were checked for each snapshot and saved
in `reports/real-experience-transfer-v1/preflight.json`. These are independent
real reported bugs in different subsystems; transfer relevance is a candidate
hypothesis about typed symbolic identity, not an established property.

The GitHub Galaxy URL could not resolve from this environment. No GitHub sync
or fabricated source history is claimed; all selected upstream snapshots are
already local, with their original commits.

## Conditions and interpretation

| Condition | Delivered material | Gate |
|---|---|---|
| control | same ordinary Galaxy context, zero Experience | empty store |
| relevant | extracted episode from successful A | intact source run/log/patch/report/extraction |
| irrelevant | episode from successful intervening printer task | same evidence checks; relevance label preregistered |
| obsolete | formerly verified advice plus target-specific supersession warning | reviewed supersession and hashed supporting evidence |

Age, different repository commits, or advice from another subsystem does not
establish obsolescence. No obsolete episode is authored to fill the fourth arm.
It remains unavailable until historical validity and current supersession are
independently documented. `reviewed` is a local review annotation, not an
authenticated identity or an automatic determination that advice is stale.

These conditions intentionally force selected, audited exposure, testing agent
transfer and resistance to unhelpful advice. They do not measure native retrieval.
A separate ExperienceStore replay must report eligible/retrieved/delivered IDs,
with obsolete entries retracted before cutoff, against the same B task. Distinguish
native stale exclusion from the forced obsolete challenge; historical verified
outcome never means currently valid advice. Wrong patch counts, semantic usage
and repeated-error categories stay null until independently annotated against a
fixed rubric. Use independent tests, not the agent's description, for success.

## Commands

Use `.venv-mcp/bin/python`: that existing environment has SWE-bench and Docker
SDK. Podman API preflight succeeded at
`unix:///run/user/1000/podman/podman.sock`. Only the unrelated Podman hello image
is cached; the actual task evaluator images still need preparation. Network
access/image builds must succeed before new model runs are useful.

```bash
.venv-mcp/bin/python scripts/real_experience_transfer.py prepare /tmp/real-transfer-prepared
# Execute source A, then intervening task; each run uses a distinct output/state:
DOCKER_HOST=unix:///run/user/1000/podman/podman.sock \
.venv-mcp/bin/python scripts/real_experience_transfer.py run \
  --task sympy__sympy-14711 --out /tmp/real-transfer-A \
  --state /tmp/real-transfer-A-state --model gpt-6-luna
# Once official A checks pass, extract only its actual trajectory/patch:
.venv-mcp/bin/python scripts/real_experience_transfer.py extract \
  --run /tmp/real-transfer-A/runs/SOURCE_RUN_ID --out /tmp/real-transfer-A-episode \
  --target sympy__sympy-17630 --condition relevant --model gpt-6-luna
# Run B challenge, one new output/state per condition:
DOCKER_HOST=unix:///run/user/1000/podman/podman.sock \
.venv-mcp/bin/python scripts/real_experience_transfer.py run \
  --task sympy__sympy-17630 --out /tmp/real-transfer-B-relevant \
  --state /tmp/real-transfer-B-relevant-state --model gpt-6-luna \
  --condition relevant --bundle /tmp/real-transfer-A-episode/bundle.json
```

Use `--condition control` with no bundle for the control; obtain irrelevant
bundle through the same extraction procedure after the intervening task. Obsolete
bundle requires an actual historical source, extraction and supersession record.
That record names `source_episode_id`, `target_base_commit`, a reviewed reason,
and an `evidence` path/SHA-256 reference proving the behavioral change. Do not
relabel irrelevant as obsolete. Extraction saves its own usage separately.

Existing adapter preserves hidden-test/gold isolation during agent execution,
official evaluator artifacts, exact context packages, raw events, agent patch
and verifier ledger. Challenge bundle SHA-256 is frozen in the target manifest
and rechecked at packet construction. Legacy OFF/ON remains the default.
Challenge overflow fails rather than silently drop base context or the episode.

## Remaining prerequisites and decision rules

Prepare/certify evaluator images; collect successful independently verified A
and intervening runs; audit extracted lessons; identify actual superseded
historical advice; then freeze episode hashes and counterbalanced condition
order before B. Initial calibration is one repetition. Measurement requires
independent repeated runs, identical model/tools/budget/source commits, and
matching non-Experience context items. Do not compare arms if sources are absent,
base context differs, or evaluators fail. Preserve every failed source attempt.

Primary: official B resolution with PASS_TO_PASS preservation. Secondary:
verified repeated-error rate, observable searches/tool calls, execution tokens,
time to verified completion. Learning/extraction overhead is separate. Raw
input tokens are not billed cost; unknown cached pricing stays unavailable.
A tie in success can motivate an efficiency study but a single lower-token run
does not prove benefit. Evaluate irrelevant/obsolete harm as carefully as relevant
benefit. Context and Experience remain experimental; memory has a local minimal
store; skill candidates exist but validated skills/learning are unproved.
Evidence and benchmark passed scoped local calibration; neither is globally
certified stable. Core/platform expansion remains frozen.

Native retrieval replay is executable via `scripts/real_experience_transfer.py
replay --target TARGET_ID --bundle RELEVANT_BUNDLE --bundle IRRELEVANT_BUNDLE
--bundle OBSOLETE_BUNDLE --out NEW_DIRECTORY`. It validates source bundles,
records them in an isolated existing ExperienceStore, retracts the independently
superseded episode before compilation, and saves eligible/retrieved/delivered IDs
plus the bundle-ID/store-ID mapping. It makes no agent-success or semantic-use claim.
