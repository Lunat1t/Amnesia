# Experience transfer v2 calibration

Completed agent task runs: 18; verifier passes: 17. Model: gpt-6-luna. One repetition per condition.

| Pair | B context only | B with Experience | Agent tokens: context only | Agent tokens: Experience |
|---|---|---|---:|---:|
| expiry | True | True | 82878 | 50430 |
| copy-isolation | True | True | 66358 | 128568 |
| normalized-collision | True | True | 82932 | 119101 |

All 18 verifier logs matched their evidence hashes. For every pair, the source commit and non-Experience context items match; B receives only the linked A episode and controls contain no Experience.

No B success improvement observed. Agent token differences are mixed. These include all input tokens, not estimated billed costs; cached-input pricing is not modeled. Extraction usage and duration are separate in audit.json. One repetition cannot establish an efficiency or general benefit claim.

The synthetic functions remain too easy to distinguish success consistently. The next useful study should use real repository maintenance pairs with independent hidden checks and irrelevant/obsolete advice controls. Keep these runs as delivery/evaluator calibration; do not expand repetitions merely to seek a positive result.
