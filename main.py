#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one fixed joke about AI coding agents to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: two runs write the same bytes.
"""

# This script writes a hardcoded programming joke to a designated output directory.
# Its output remains perfectly deterministic across executions due to the absence of dynamic inputs or timestamps.

import os
from pathlib import Path

# This humor highlights disproportionate automated effort where simple asks spawn sprawling extra features while ignoring the initial objective.
# Because no external state, random numbers, or dynamic timestamps are used, output is completely reproducible.
JOKE = "I asked my coding agent to add a login button. It shipped a dashboard, dark mode, and a billing page. The login button is still a TODO."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")

# Verification: Verified output byte count is 135 bytes, and two independent runs matched byte-for-byte.
