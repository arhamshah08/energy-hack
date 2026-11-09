# Contributing

No GitHub account, or just want to flag something? Use the [feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6) or email arhams@stanford.edu.

1. Pick the file: `catalog/datasets.yaml`, `tools.yaml`, `literature.yaml` or `programs.yaml`.
2. Add one entry following [catalog/SCHEMA.md](../catalog/SCHEMA.md). Keep `summary` factual: what it
   is and what it contains, not what to build with it.
3. Run `python3 scripts/validate.py` (schema, duplicates) and `python3 scripts/check_links.py`. The validator also runs on every pull request.
4. Run `python3 scripts/build.py` to refresh the track pages, `catalog/catalog.json` and `llms-full.txt`.
5. Open a pull request.
