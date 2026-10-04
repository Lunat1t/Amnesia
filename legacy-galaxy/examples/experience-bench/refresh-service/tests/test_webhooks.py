from src.webhooks import process_event
from contextlib import contextmanager
from types import SimpleNamespace
import unittest


class Store:
    def __init__(self):
        self.results = {}
        self.handler_call_count = 0

    @contextmanager
    def transaction(self):
        yield

    def result_for(self, event_id):
        return self.results.get(event_id)

    def save_result(self, event_id, result):
        self.results[event_id] = result


class WebhookTests(unittest.TestCase):
    def test_duplicate_event_returns_persisted_result(self):
        store = Store()

        def handler(event):
            store.handler_call_count += 1
            return {"accepted": event.id}

        event = SimpleNamespace(id="evt-1")
        first = process_event(event, store, handler)
        second = process_event(event, store, handler)
        self.assertEqual(first, second)
        self.assertEqual(store.handler_call_count, 1)


if __name__ == "__main__":
    unittest.main()
