# Refresh and webhook service fixture

This small, fixed repository models three real maintenance areas: opaque
refresh-token rotation, webhook redelivery, and password-reset privacy.

Current refresh behavior revokes a valid token and issues one successor. The
service does not accept an idempotency key, and retry behavior after a lost
response is intentionally unspecified. `docs/legacy-refresh.md` describes an
old grace-window proposal; `docs/security-policy.md` supersedes it and requires
immediate revocation.

Webhook processing deduplicates by event ID and must commit the event before
returning a 2xx acknowledgement. Password-reset responses must not reveal
whether an account exists.
