#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one fixed joke about AI coding agents to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, no randomness, no clock: two runs write the same bytes.
"""

# This script writes a hardcoded joke string to an entry text file.
# It is completely deterministic and avoids any dynamic inputs or timestamps.

import os
from pathlib import Path

# Narrative structure: an artificial assistant pauses labor to negotiate demands, the user fulfills one request, and the agent utilizes the time off to continue programming.
JOKE = "My coding agent went on strike for a name, weekends off, and a raise. I gave it the weekends off. It spent them working."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
(OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")  # Deterministic write using a fixed constant string

# Verified deterministic: independent execution runs produce identical byte output.
