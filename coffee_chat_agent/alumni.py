"""Track alumni contacts found through legitimate, ToS-compliant channels --
LinkedIn's own "School Alumni" page (a manual search feature LinkedIn
provides, not scraping), a university mentorship platform (e.g. Cal Alumni
Association's CalConnect), a department alumni directory, or a career center
tool (e.g. Handshake). These are warm leads: shared school beats a cold
C-suite outreach every time.

This module only stores what you've already found by hand -- it does not
search LinkedIn itself.
"""

import csv
import os

FIELDNAMES = ["name", "company", "role", "segment", "function", "source", "contacted", "notes"]

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "alumni.csv")


def ensure_file(path: str = DEFAULT_PATH) -> None:
    if not os.path.exists(path):
        with open(path, "w", newline="") as f:
            csv.DictWriter(f, fieldnames=FIELDNAMES).writeheader()


def add(name: str, company: str, role: str = "", segment: str = "", function: str = "",
        source: str = "", notes: str = "", path: str = DEFAULT_PATH) -> None:
    ensure_file(path)
    with open(path, "a", newline="") as f:
        csv.DictWriter(f, fieldnames=FIELDNAMES).writerow({
            "name": name, "company": company, "role": role, "segment": segment,
            "function": function, "source": source, "contacted": "no", "notes": notes,
        })


def list_all(path: str = DEFAULT_PATH) -> list:
    if not os.path.exists(path):
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def find(name: str, path: str = DEFAULT_PATH):
    for row in list_all(path):
        if row["name"].strip().lower() == name.strip().lower():
            return row
    return None


def next_uncontacted(n: int = 5, path: str = DEFAULT_PATH) -> list:
    return [r for r in list_all(path) if r.get("contacted", "no").lower() != "yes"][:n]


def mark_contacted(names: list, path: str = DEFAULT_PATH) -> None:
    rows = list_all(path)
    wanted = {n.strip().lower() for n in names}
    for r in rows:
        if r["name"].strip().lower() in wanted:
            r["contacted"] = "yes"
    ensure_file(path)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
