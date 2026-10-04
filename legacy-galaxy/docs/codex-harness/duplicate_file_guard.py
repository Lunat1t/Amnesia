#!/usr/bin/env python3
"""Block only duplicate Add File patches; leave edits and other tool calls alone."""

import json
import os
import re
import sys
from pathlib import Path


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    if event.get("tool_name") != "apply_patch":
        return 0

    patch_text = (event.get("tool_input") or {}).get("command", "")
    cwd = Path(event.get("cwd") or os.getcwd()).resolve()
    existing = []
    for match in re.finditer(r"^\*\*\* Add File: (.+?)\s*$", patch_text, re.MULTILINE):
        candidate = Path(match.group(1))
        candidate = (cwd / candidate).resolve() if not candidate.is_absolute() else candidate.resolve()
        try:
            candidate.relative_to(cwd)
        except ValueError:
            continue
        if candidate.exists():
            existing.append(candidate.relative_to(cwd).as_posix())

    if existing:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    "Auto-steering: this Add File target already exists: "
                    + ", ".join(existing)
                    + ". Inspect and edit/reuse the existing file, or choose a justified new path."
                ),
            }
        }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
