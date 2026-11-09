#!/usr/bin/env python3
"""Search the catalog. No dependencies.

Examples
  python3 scripts/find.py --track 2                     # everything for Track 2, grid capacity
  python3 scripts/find.py --track 3 --kind paper        # papers for Track 3
  python3 scripts/find.py --track 1 --access open       # no-key data for Track 1
  python3 scripts/find.py --tag simulation              # simulators across all tracks
  python3 scripts/find.py --role harness                # RSI loop frameworks
  python3 scripts/find.py --json --track 4              # machine-readable
"""
import argparse
import json
import sys

from catalog_lib import as_list, load_all

TRACKS = {"1": "1-sites", "2": "2-grid-capacity", "3": "3-load-management", "4": "4-aggregation",
          "sites": "1-sites", "grid-capacity": "2-grid-capacity",
          "load-management": "3-load-management", "aggregation": "4-aggregation"}

p = argparse.ArgumentParser(description="Filter catalog entries. All filters combine with AND.")
p.add_argument("query", nargs="*", help="free text matched against id, name, summary")
p.add_argument("--track", help="1 sites | 2 grid-capacity | 3 load-management | 4 aggregation")
p.add_argument("--tag", help="rsi | simulation | coordination | edge-ai")
p.add_argument("--domain", help="edge-compute | materials | grid-fusion | rsi")
p.add_argument("--topic", help="T1 growth | T2 siting difficulty | T3 datasets | T4 vocabulary | T5 tools | T6 programs")
p.add_argument("--role", help="data | verifier | metric | proposer | harness | background")
p.add_argument("--kind", help="dataset | tool | simulator | api | benchmark | paper | report | program | policy | standard | filing")
p.add_argument("--access", help="open | api-key | registration | mixed | paid | on-request")
p.add_argument("--json", action="store_true", help="print JSON (for agents)")
a = p.parse_args()

track = TRACKS.get(str(a.track).lower(), a.track) if a.track else None
out = []
for e in load_all():
    if track and track not in as_list(e.get("track")):
        continue
    for field, val in (("tag", a.tag), ("domain", a.domain), ("role", a.role)):
        if val and val not in as_list(e.get(field)):
            break
    else:
        if a.topic and a.topic.upper() not in as_list(e.get("topic")):
            continue
        if a.kind and a.kind != e.get("kind"):
            continue
        if a.access and a.access != e.get("access"):
            continue
        hay = " ".join(str(e.get(k, "")) for k in ("id", "name", "summary")).lower()
        if any(q.lower() not in hay for q in a.query):
            continue
        out.append(e)

if a.json:
    json.dump([{k: v for k, v in e.items() if not k.startswith("_")} for e in out], sys.stdout, indent=2)
    print()
else:
    for e in out:
        tr = ",".join(t.split("-")[0] for t in as_list(e.get("track")))
        print(f"{e['id']}  [{e.get('kind')}{'  track ' + tr if tr else ''}]")
        print(f"  {e.get('name')}")
        print(f"  {e.get('url') or 'no public link: access on request'}")
        print(f"  {e.get('summary')}\n")
    print(f"{len(out)} match(es)", file=sys.stderr)
