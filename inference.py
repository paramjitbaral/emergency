#!/usr/bin/env python3
"""Compatibility entrypoint for the refactored journey-based runner."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent
MY_ENV_DIR = ROOT / "my_env"
if str(MY_ENV_DIR) not in sys.path:
    sys.path.insert(0, str(MY_ENV_DIR))

from inference import main


if __name__ == "__main__":
    main()
