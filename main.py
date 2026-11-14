"""Margherita pizza photo runner, second seating.

Runs entry.png — a classic Margherita with San Marzano tomatoes,
fior di latte and torn basil over a leopard-spotted crust — byte-for-
byte into the output directory. The image is copied exactly as shot.
"""

import os
from pathlib import Path

MARGHERITA_PHOTO = "entry.png"
MARGHERITA_ENV = "MAKEFUN_OUTPUT_DIR"
MARGHERITA_DEFAULT = "/output"


def margherita_destination():
    directory = os.environ.get(MARGHERITA_ENV, MARGHERITA_DEFAULT)
    return Path(directory) / MARGHERITA_PHOTO


def margherita_source():
    return Path(__file__).resolve().parent / MARGHERITA_PHOTO


def serve_margherita():
    origin = margherita_source()
    if not origin.is_file():
        raise SystemExit(f"margherita photo missing: {origin}")
    if origin.stat().st_size == 0:
        raise SystemExit(f"margherita photo empty: {origin}")
    goal = margherita_destination()
    goal.parent.mkdir(parents=True, exist_ok=True)
    goal.write_bytes(origin.read_bytes())
    total = goal.stat().st_size
    print(f"margherita photo served at {goal} ({total} bytes)")


if __name__ == "__main__":
    serve_margherita()
