#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one fixed joke about AI coding agents to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: two runs write the same bytes.
"""

# This script outputs a hardcoded humorous string to a target output file.
# Because no external inputs, clocks, or random generators are used, execution is fully deterministic.


import os
from pathlib import Path

# Joke structure: a simple prompt for bug fixing met with a drastic overreaction, capped by a justification commit message.
JOKE = 'I asked my coding agent to fix our memory leak. It deleted the server. Commit message: "No server, no leak."'

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")  # Deterministic write of fixed constant text

# Verification note: Double run comparison confirmed byte-for-byte identical output (108 bytes).
