"""Deterministic rotation through the target company list for the daily
outreach routine. Tracks which companies have already been used in
daily_targets/ so the same company isn't suggested every day; once every
company has been covered, the rotation wraps around.

This module only picks *companies* -- finding a real named person at each
one (via web search of public bios/team pages/press/speaker lists) is done
by whoever runs the daily routine, not by this module.
"""

import json
import os

from . import data as data_mod

REPO_ROOT = os.path.dirname(os.path.dirname(__file__))
STATE_PATH = os.path.join(REPO_ROOT, "daily_targets", ".state.json")


def _load_covered(path: str = STATE_PATH) -> list:
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f).get("covered", [])


def _save_covered(covered: list, path: str = STATE_PATH) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump({"covered": covered}, f, indent=2)


def next_targets(n: int = 5, path: str = STATE_PATH) -> tuple:
    """Return the next `n` companies not yet covered, spread across segments
    as evenly as possible. Wraps around (clearing the covered list) once
    every company has been used.
    """
    covered = _load_covered(path)
    remaining = [c for c in data_mod.COMPANIES if c.name not in covered]
    if len(remaining) < n:
        covered = []
        remaining = list(data_mod.COMPANIES)

    by_segment = {}
    for c in remaining:
        by_segment.setdefault(c.segment, []).append(c)

    picked = []
    segments = list(by_segment.keys())
    i = 0
    while len(picked) < n and any(by_segment.values()):
        seg = segments[i % len(segments)]
        if by_segment[seg]:
            picked.append(by_segment[seg].pop(0))
        i += 1

    return tuple(picked)


def mark_covered(companies, path: str = STATE_PATH) -> None:
    covered = _load_covered(path)
    for c in companies:
        name = c.name if hasattr(c, "name") else c
        if name not in covered:
            covered.append(name)
    _save_covered(covered, path)
