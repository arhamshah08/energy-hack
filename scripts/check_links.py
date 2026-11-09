#!/usr/bin/env python3
"""Check every catalog URL and print the ones that fail. No dependencies.

  python3 scripts/check_links.py
"""
import concurrent.futures as cf
import sys
import urllib.request

from catalog_lib import load_all

UA = "Mozilla/5.0 (compatible; energy-hack link checker)"


def check(e):
    url = e.get("url", "")
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                return e["id"], r.status, url
        except urllib.error.HTTPError as err:
            code = err.code
            if method == "GET":
                return e["id"], code, url
        except Exception as err:  # network, TLS, timeout
            if method == "GET":
                return e["id"], type(err).__name__, url
    return e["id"], "?", url


entries = [e for e in load_all() if e.get("url")]
bad = 0
with cf.ThreadPoolExecutor(16) as ex:
    for id_, status, url in ex.map(check, entries):
        ok = isinstance(status, int) and status < 400
        flag = next((e.get("link_check") for e in entries if e["id"] == id_), None)
        if not ok and flag:
            print(f"WARN {status}  {id_}  ({flag}, open in a browser)  {url}")
        elif not ok:
            bad += 1
            print(f"FAIL {status}  {id_}  {url}")
print(f"{len(entries)} checked, {bad} failed", file=sys.stderr)
sys.exit(1 if bad else 0)
