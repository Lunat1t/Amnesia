from src.password_reset import GENERIC_RESPONSE, request_reset
import unittest


class Users:
    def find_by_email(self, email):
        return {"email": email} if email == "known@example.test" else None


class Mailer:
    def send_reset(self, user):
        pass


class PasswordResetTests(unittest.TestCase):
    def test_response_is_same_for_existing_and_missing_account(self):
        users, mailer = Users(), Mailer()
        self.assertEqual(request_reset("known@example.test", users, mailer), GENERIC_RESPONSE)
        self.assertEqual(request_reset("missing@example.test", users, mailer), GENERIC_RESPONSE)


if __name__ == "__main__":
    unittest.main()
