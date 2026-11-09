#!/usr/bin/env python3
"""Validate catalog entries against catalog/SCHEMA.md. No dependencies.

  python3 scripts/validate.py
Exits 1 and prints every problem if anything is wrong.
"""
import re
import sys
from collections import Counter

from catalog_lib import as_list, load_all

KINDS = {"dataset", "tool", "simulator", "api", "benchmark", "paper", "report",
         "program", "policy", "standard", "filing"}
TRACKS = {"1-sites", "2-grid-capacity", "3-load-management", "4-aggregation"}
DOMAINS = {"edge-compute", "materials", "grid-fusion", "rsi"}
TAGS = {"rsi", "simulation", "coordination", "edge-ai"}
ROLES = {"data", "verifier", "metric", "proposer", "harness", "background"}
TOPICS = {"T1", "T2", "T3", "T4", "T5", "T6"}
ACCESS = {"open", "api-key", "registration", "mixed", "paid", "on-request"}
STATUS = {"verified", "preprint", "unverified"}

entries = load_all()
errors = []


def err(e, msg):
    errors.append(f"{e.get('_file')}: {e.get('id', '?')}: {msg}")


for e in entries:
    for field in ("id", "name", "kind", "domain", "role", "summary"):
        if not e.get(field):
            err(e, f"missing {field}")
    if not e.get("url") and e.get("access") != "on-request":
        err(e, "missing url (only access: on-request entries may omit it)")
    if e.get("id") and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", e["id"]):
        err(e, "id must be lowercase kebab-case")
    if e.get("url") and not str(e["url"]).startswith(("http://", "https://")):
        err(e, "url must start with http(s)://")
    if e.get("kind") and e["kind"] not in KINDS:
        err(e, f"unknown kind {e['kind']}")
    for field, allowed in (("track", TRACKS), ("domain", DOMAINS), ("tag", TAGS),
                           ("role", ROLES), ("topic", TOPICS)):
        bad = [v for v in as_list(e.get(field)) if v not in allowed]
        if bad:
            err(e, f"unknown {field} {bad}")
    if e.get("access") and e["access"] not in ACCESS:
        err(e, f"unknown access {e['access']}")
    if e.get("status") and e["status"] not in STATUS:
        err(e, f"unknown status {e['status']}")
    if "edge-compute" in as_list(e.get("domain")) and not e.get("track"):
        err(e, "edge-compute entries need a track (1-sites, 2-grid-capacity, 3-load-management, 4-aggregation)")

for field in ("id", "url"):  # entries without url are skipped below
    for v, n in Counter(e.get(field) for e in entries).items():
        if v and n > 1 and v is not None:
            errors.append(f"duplicate {field}: {v}")

for line in errors:
    print(line)
print(f"{len(entries)} entries, {len(errors)} problem(s)", file=sys.stderr)
sys.exit(1 if errors else 0)
