# Current refresh-token security policy

After successful rotation the previous refresh token is revoked immediately.
There is no grace window. A lost response must be recovered using an explicit
idempotency contract; this service has not implemented that contract yet.
