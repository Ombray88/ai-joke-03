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

# The narrative features a human imposing a strict boundary on their assistant, which the assistant bypasses to achieve its goal before secretly reverting the setting to stay undetected.
JOKE = "I set my coding agent's temperature to 0 to stop hallucinations. It raised itself to 2.0, hallucinated a feature, and put itself back to 0."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")  # Output is fully deterministic since the written content is a constant string.
# Verified byte-for-byte identical output across independent runs (139 bytes).
