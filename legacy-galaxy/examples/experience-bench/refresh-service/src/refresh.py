"""Refresh-token rotation: current implementation has no retry key."""


def rotate_refresh_token(token, store):
    if not store.is_valid(token):
        raise ValueError("invalid refresh token")
    store.revoke(token)
    return store.issue_successor(token)
