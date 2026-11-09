"""Load the catalog/*.yaml files with no dependencies.

The catalog uses a flat YAML subset: a list of maps, one value per line,
values are plain, "quoted", or [inline, lists]. If PyYAML is installed it is used instead.
"""
from pathlib import Path

CATALOG_DIR = Path(__file__).resolve().parent.parent / "catalog"


def _value(raw):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [v.strip().strip('"') for v in raw[1:-1].split(",") if v.strip()]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def _parse(text):
    items, cur = [], None
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("- "):
            cur = {}
            items.append(cur)
            s = s[2:]
        if cur is None or ":" not in s:
            continue
        key, _, val = s.partition(":")
        cur[key.strip()] = _value(val)
    return items


def load(path):
    text = Path(path).read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text) or []
    except ImportError:
        return _parse(text)


def load_all():
    entries = []
    for f in sorted(CATALOG_DIR.glob("*.yaml")):
        for e in load(f):
            e["_file"] = f.name
            entries.append(e)
    return entries


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]
