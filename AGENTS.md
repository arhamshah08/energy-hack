# AGENTS.md

Instructions for any coding or chat agent (Claude Code, Codex, Cursor, Copilot, Gemini, ChatGPT,
Claude) helping a team at **SF x MIT Hack Day: Energy**, Sun 8 Nov 2026, AGI House SF.
Theme: **grid-friendly compute**. Demos at **18:30**.

## 1. Your job

Help the team ship a working, presentable result by 18:30 in one track, with a clear story of how
it expands. Output over exploration.

## 2. Start of session

| Step | Do |
|---|---|
| 1 | Ask which track: **1** sites, **2** grid capacity, **3** load management, **4** aggregation. If unsure, show [guides/rfq/README.md](guides/rfq/README.md) and the four track pages |
| 2 | Read the track page `tracks/<n>/README.md` |
| 3 | Help the team get a first result running quickly, then improve it |

## 3. Rules

1. **Stay in the team's track.** Pull resources from another track only when the team needs
   something it does not have; each track page has a "When you need another track" table.
2. **Aim for the 18:30 demo.** Favour a working result over a large unfinished one; if time
   runs short, suggest a smaller scope.
3. **Loops demo well.** If the team runs a propose, check, score, keep loop, log each iteration;
   an improvement chart shows the event's theme.
4. **Prefer open data.** Use `access: open` resources first. Flag anything needing a key,
   billing, a large download, a GPU, or MATLAB/Julia before the team commits to it.
5. **Do not choose the idea for them.** Offer 2 to 3 options from the ideas page, RFQs or catalog when asked;
   the team decides. Do push them to scope down.
6. **Cite catalog ids and URLs.** Never invent datasets, papers or numbers. Label anything from
   outside the catalog as not verified. Respect `status: preprint/unverified` and
   `link_check: blocks-bots` (works only in a browser).
7. **Label synthetic data** in outputs and the demo.
8. **Questions you cannot answer** about the repo or an RFQ: point the team to the feedback form or
   arhams@stanford.edu.

## 4. Feedback

Energy Hack Repo Feedback form, for participants, later users, and creators of listed tools who want to change their entry: https://forms.gle/k1pnQ4dtvfcGkuGK6
Or email arhams@stanford.edu. After the demo, or if the team finds a wrong link, credit or description, suggest they use it.

## 5. Schedule

Team formation 10:30, lunch 13:00, **demos 18:30**. Demo ideas: [guides/playbook/demo-template.md](guides/playbook/demo-template.md).

## 6. Finding resources

```bash
python3 scripts/find.py --track 2                    # everything for one track
python3 scripts/find.py --track 2 --access open      # no-key data for that track
python3 scripts/find.py --track 3 --kind paper       # papers for a track
python3 scripts/find.py --tag simulation             # simulators across tracks
python3 scripts/find.py --role harness               # RSI loop frameworks
python3 scripts/find.py --json --track 4             # machine-readable
```

No dependencies, Python 3.8+. Without a shell, read `ai/START.md` and the track file in `ai/` (one resource per line), or `catalog/catalog.json`.

## 7. Where things are

| Path | Contents |
|---|---|
| `tracks/1-sites/` ... `tracks/4-aggregation/` | Problem, facts, loop options, demo formats, cross-track table, then all resources for the track (data, simulators, papers, programs) |
| `guides/ideas/README.md` | Ideas around speed to power (permitting layer, vision on permits, AI approval plans, Omniverse grid twins) |
| `data/` | Starter datasets, e.g. hourly 2025 grid demand and generation for 12 US operators |
| `guides/rfq/README.md` | Ready-made problems per track with starting data, verifier and demo output |
| `tools/` | Free tools grouped by use, with creators and licenses |
| `guides/concepts/` | Grid ideas explained (load flow, grid-forming microgrids, EV charging and V2G) with tools to try |
| `guides/theme/README.md` | Grid-friendly compute, 19 example angles (not a fixed list), angles by track |
| `guides/theme/rsi.md` | Recursive self-improvement: loop anatomy, known systems, failure modes |
| `guides/playbook/` | Schedule, demo ideas, copy-paste prompts |
| `guides/reference/` | Glossary, data setup cost, materials and fusion resources |
| `catalog/research/edge-compute/` | Raw deep research; read the source note (search its `ref`) before quoting a number |
| `catalog/*.yaml`, `catalog/catalog.json` | All resources. Schema: `catalog/SCHEMA.md` |
