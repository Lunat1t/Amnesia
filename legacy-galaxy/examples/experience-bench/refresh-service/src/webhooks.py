"""Webhook idempotency boundary."""


def process_event(event, store, handler):
    existing = store.result_for(event.id)
    if existing is not None:
        return existing
    with store.transaction():
        result = handler(event)
        store.save_result(event.id, result)
    return result


def acknowledge(event, store, handler):
    """The caller may send 2xx only after process_event commits."""
    return process_event(event, store, handler)
