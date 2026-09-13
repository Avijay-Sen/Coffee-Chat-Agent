"""Simple CSV-backed outreach tracker so nothing falls through the cracks."""

import csv
import os
from datetime import date

FIELDNAMES = [
    "name", "company", "segment", "role", "channel",
    "date_contacted", "status", "followup_date", "notes",
]

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "outreach_log.csv")


def ensure_log(path: str = DEFAULT_PATH) -> None:
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            csv.DictWriter(f, fieldnames=FIELDNAMES).writeheader()


def add_entry(name: str, company: str, segment: str, role: str, channel: str,
              status: str = "sent", followup_date: str = "", notes: str = "",
              path: str = DEFAULT_PATH) -> None:
    ensure_log(path)
    with open(path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "name": name,
            "company": company,
            "segment": segment,
            "role": role,
            "channel": channel,
            "date_contacted": date.today().isoformat(),
            "status": status,
            "followup_date": followup_date,
            "notes": notes,
        })


def list_entries(path: str = DEFAULT_PATH):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
