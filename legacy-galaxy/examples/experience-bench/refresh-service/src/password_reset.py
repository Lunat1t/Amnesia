"""Privacy-preserving password reset response."""


GENERIC_RESPONSE = "If the account exists, reset instructions will be sent."


def request_reset(email, users, mailer):
    user = users.find_by_email(email)
    if user is not None:
        mailer.send_reset(user)
    return GENERIC_RESPONSE
