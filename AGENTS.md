# AGENTS.md

Instructions for any coding or chat agent (Claude Code, Codex, Cursor, Copilot, Gemini, ChatGPT,
Claude) using this repo. It is a free, open catalog of resources on **grid-friendly compute**:
powering data centers and distributed compute without straining the grid. Anyone can use it.
It was first made for SF x MIT Hack Day: Energy (8 Nov 2026, AGI House SF).

## 1. Your job

Help the user find what in this repo fits their interest, and say plainly what is missing.
If they want to build something, help them get a first result running fast, then improve it.

## 2. Start of session

| Step | Do |
|---|---|
| 1 | Ask what they are interested in. If unsure, show the four tracks: **1** sites, **2** grid capacity, **3** load management, **4** aggregation |
| 2 | Read the matching track page `tracks/<n>/README.md`, or search with `scripts/find.py` |
| 3 | Reply with a short brief: what this repo is (one line), 3 to 5 resources that fit with links, what is missing (see `ai/START.md` "Known gaps"), and arhams@stanford.edu for questions |

## 3. Rules

1. **Stay on their interest.** Pull from another track only when they need it; each track page has
   a "When you need another track" table.
2. **Prefer open data.** Use `access: open` resources first. Flag anything needing a key, billing,
   a large download, a GPU, or MATLAB/Julia before they commit to it.
3. **Do not choose the idea for them.** Offer 2 to 3 options from the ideas page, RFQs or catalog
   when asked; they decide. Do push them to scope down.
4. **Cite catalog ids and URLs.** Never invent datasets, papers or numbers. Label anything from
   outside the catalog as not verified. Respect `status: preprint/unverified` and
   `link_check: blocks-bots` (works only in a browser).
5. **Label synthetic data** in any output.
6. **Loops show progress well.** If they run a propose, check, score, keep loop, log each
   iteration and plot the score.

## 4. Questions and feedback

Email arhams@stanford.edu, or use the feedback form (also for creators of listed tools who want
to change their entry): https://forms.gle/k1pnQ4dtvfcGkuGK6

## 5. Finding resources

```bash
python3 scripts/find.py --track 2                    # everything for one track
python3 scripts/find.py --track 2 --access open      # no-key data for that track
python3 scripts/find.py --track 3 --kind paper       # papers for a track
python3 scripts/find.py --tag simulation             # simulators across tracks
python3 scripts/find.py --role harness               # RSI loop frameworks
python3 scripts/find.py --json --track 4             # machine-readable
```

No dependencies, Python 3.8+. Without a shell, read `ai/START.md` and the track file in `ai/` (one resource per line), or `catalog/catalog.json`.

## 6. Where things are

| Path | Contents |
|---|---|
| `tracks/1-sites/` ... `tracks/4-aggregation/` | Problem, facts, loop options, outputs, cross-track table, then all resources for the track |
| `guides/ideas/README.md` | Ideas around speed to power (permitting layer, vision on permits, AI approval plans, Omniverse grid twins) |
| `data/` | Starter data: hourly 2025 grid demand and generation for 12 US operators |
| `guides/rfq/README.md` | Ready-made problems per track with starting data, verifier and output to show |
| `tools/` | Free tools grouped by use, with creators and licenses |
| `guides/concepts/` | Grid ideas explained (load flow, grid-forming microgrids, EV charging and V2G) with tools to try |
| `guides/theme/README.md` | Grid-friendly compute, 19 example angles |
| `guides/theme/rsi.md` | Recursive self-improvement: loop anatomy, known systems, failure modes |
| `guides/playbook/` | Build plan, how to present a result, copy-paste prompts |
| `guides/reference/` | Glossary, data setup cost, materials and fusion resources |
| `guides/event/` | The original hack day (8 Nov 2026) |
| `catalog/research/edge-compute/` | Raw deep research; read the source note (search its `ref`) before quoting a number |
| `catalog/*.yaml`, `catalog/catalog.json` | All resources. Schema: `catalog/SCHEMA.md` |
