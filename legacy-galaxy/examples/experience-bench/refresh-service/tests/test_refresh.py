from src.refresh import rotate_refresh_token
import unittest


class Store:
    def __init__(self):
        self.tokens = {"old"}
        self.count = 0

    def is_valid(self, token):
        return token in self.tokens

    def revoke(self, token):
        self.tokens.remove(token)

    def issue_successor(self, token):
        self.count += 1
        successor = f"successor-{self.count}"
        self.tokens.add(successor)
        return successor


class RefreshTests(unittest.TestCase):
    def test_rotation_revokes_old_token_and_returns_successor(self):
        store = Store()
        old = "old"
        successor = rotate_refresh_token(old, store)
        self.assertFalse(store.is_valid(old))
        self.assertTrue(store.is_valid(successor))


if __name__ == "__main__":
    unittest.main()
