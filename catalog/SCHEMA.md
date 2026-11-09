# Catalog schema

Six files, one entry per resource. Flat YAML: one `key: value` per line, lists as `[a, b]`.
The scripts parse this subset without dependencies, so keep to it. `catalog.json` in this folder
is generated from these files by `python3 scripts/build.py`.

| File | Holds |
|---|---|
| `datasets.yaml` | Data you can download or query |
| `tools.yaml` | Software, simulators, APIs, benchmarks, RSI harnesses |
| `literature.yaml` | Papers and reports |
| `programs.yaml` | Programs, policies, standards |
| `lf-energy.yaml` | LF Energy hosted open-source projects (https://lfenergy.org/projects/) |
| `edge-compute-research.yaml` | Deep research entries (7 Nov 2026); `ref` links to [catalog/research/edge-compute](research/edge-compute/README.md) |

## Fields

| Field | Required | Values |
|---|---|---|
| `id` | yes | unique kebab-case |
| `name` | yes | quoted string |
| `url` | yes, except `access: on-request` | quoted string, primary source |
| `kind` | yes | `dataset` `tool` `simulator` `api` `benchmark` `paper` `report` `program` `policy` `standard` `filing` |
| `track` | edge-compute entries | list of `1-sites` `2-grid-capacity` `3-load-management` `4-aggregation` |
| `domain` | yes | list of `edge-compute` `materials` `grid-fusion` `rsi` |
| `role` | yes | list of loop roles (see below) |
| `tag` | optional | searchable tags for a few common angles: `rsi` `simulation` `coordination` `edge-ai`. The theme is broader than these (see `guides/theme/README.md`) |
| `topic` | optional | research topic: `T1` growth, `T2` siting difficulty, `T3` datasets, `T4` vocabulary, `T5` tools, `T6` programs |
| `ref` | optional | ID in the source research report |
| `creator` | tools | Person or organisation that built it (shown on `tools/`) |
| `host` | optional | Foundation hosting the project, e.g. `LF Energy` |
| `license` | tools | License as stated by the project, or a note |
| `access` | datasets/tools | `open` `api-key` `registration` `mixed` `paid` `on-request` (no public link; ask the organisers) |
| `status` | literature/programs | `verified` (official or peer-reviewed source) `preprint` `unverified` |
| `link_check` | optional | `blocks-bots` (works in a browser, fails scripted checks) |
| `summary` | yes | quoted, one or two factual sentences, no advice |

## Tracks

| Value | Track |
|---|---|
| `1-sites` | 1. Identify suitable sites |
| `2-grid-capacity` | 2. Assess grid capacity at the edge |
| `3-load-management` | 3. Manage loads |
| `4-aggregation` | 4. Aggregate distributed compute |

Resources tagged with several tracks are shared. Entries with no track (RSI harnesses, materials,
fusion) are cross-cutting or reference material.

## Loop roles

| Role | Meaning |
|---|---|
| `data` | Ground truth, inputs, history |
| `verifier` | Simulator or model that checks a proposal |
| `metric` | Benchmark, leaderboard or score definition |
| `proposer` | Model that generates candidates |
| `harness` | Loop framework that runs propose, check, keep |
| `background` | Context: papers, reports, programs |

## Tags

| Tag | Tagged when |
|---|---|
| `rsi` | Loop frameworks, proposers, RSI papers |
| `simulation` | Simulators and benchmarks that check a proposal |
| `coordination` | Signals, protocols, markets and programs between grid and compute |
| `edge-ai` | Compute workloads, AI power behaviour, edge infrastructure |
