[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Ideas: speed to power

**Speed to power** is the time from picking a site to having electricity flowing to it. For new
compute it is often the longest step: a data center can be built in 2 to 3 years, while grid
connections and approvals generally take longer (`iea-energy-ai-2025`). Generation projects wait a
median of over five years from request to operation (`lbnl-queued-up`), and towns are adding
moratoria and special permits for data centers (`richmond-dc-moratorium`, `loudoun-dc-standards`).

These are ideas, not assignments. Pick one, combine them, or bring your own.
More problem statements: [RFQs](../rfq/README.md).

## 1. Speed to power: permits and approvals

| # | Idea | What it does | Start with | Track |
|---|---|---|---|---|
| 1.1 | **Grid permitting layer** | A map layer for the grid that joins, per site: zoning and moratoria, permits already issued, utility hosting capacity, and large-load process status. Answers "how fast could this site get power?" | `sf-property-information-map`, `national-zoning-atlas`, filings (`--kind filing`), `pge-ica`, `ercot-batch-zero`, `va-deq-air-permits`, `nepa-mcp` | 1, 2 |
| 1.2 | **Vision to scan city permitting data** | Vision-language models read permit PDFs, council records, site plans and single-line diagrams, and turn them into structured data: requirements, conditions, decisions, dates | `santa-clara-planning-record`, `santa-clara-zoning`, `tulare-dc-moratorium` (CEQAnet records), `va-deq-air-permits`, `loudoun-dc-standards` | 1 |
| 1.3 | **AI plans to accelerate city approvals** | Given a site and the city's rules, an agent drafts the application checklist, pre-checks the plan against code, prepares answers to common conditions (noise, water, backup generators) and flags what usually slows approval | Same records as 1.2, `va-jlarc-2024` (noise, water, local impacts), `jrc-eu-coc-2024` | 1 |
| 1.4 | **Speed-to-power scorecard** | Combine permitting status, hosting capacity, grid process and onsite power options into an estimated time to energize, per site | 1.1 outputs, `pge-ica`, `nrel-reopt`, `miso-firm-service-step-up` | 1, 2 |
| 1.5 | **Connect sooner with flexibility** | Estimate how much earlier a site connects if it accepts limited curtailment or non-firm service | `duke-rethinking-load-growth-2025`, `miso-firm-service-step-up`, `starter-us-grid-hourly-2025`, `pandapower` | 2, 3 |

## 2. Digital twins and grid data

| # | Idea | What it does | Start with | Track |
|---|---|---|---|---|
| 2.1 | **Omniverse for grid data** | Use NVIDIA Omniverse (DSX Blueprint, OpenUSD) to build a digital twin of a data center and its local grid, feed it real hourly grid data, and test how the site responds to grid conditions (the DSX Flex idea) | `nvidia-omniverse-dsx`, `nvidia-dsx-announcement-2025`, `starter-us-grid-hourly-2025`, `tamu-activsg10k` | 2, 3 |
| 2.2 | **Grid twin without special hardware** | The same idea on open tools: synthetic grid plus hourly data plus power flow, viewed on a map | `tamu-activsg10k`, `pandapower`, `starter-us-grid-hourly-2025`, `ac-grid-lab` | 2 |
| 2.3 | **Live grid context for a site** | Show prices, demand and generation mix for the site's grid operator next to its load | `gridstatus-io`, `starter-us-grid-hourly-2025` | 2, 3 |

## 3. Flexible and coordinated compute

| # | Idea | What it does | Start with | Track |
|---|---|---|---|---|
| 3.1 | **Compute that follows the grid** | Shift flexible jobs to hours with spare capacity, low prices or clean power | `starter-us-grid-hourly-2025`, `google-cluster-data`, `flex-pse`, `lfe-flexmeasures` | 3 |
| 3.2 | **EVs and compute on one connection** | Schedule EV charging and compute together so a shared site stays under its limit; add vehicle-to-grid | `acn-data`, `acnportal`, [EV concept](../concepts/ev-smart-charging-v2g.md) | 3, 4 |
| 3.3 | **Ride-through instead of trip-off** | Show how a data center's power electronics could stay connected through faults | `openibr`, `dc-emt-model`, `pjm-load-transfer-event-2026` | 2, 3 |
| 3.4 | **Many small sites as one resource** | Answer a grid request across a fleet of edge sites and prove what was delivered | `lfe-flexmeasures`, `openleadr`, `open-satori`, `citylearn` | 4 |

## 4. Self-improving agents (RSI)

| # | Idea | What it does | Start with | Track |
|---|---|---|---|---|
| 4.1 | **An agent that gets faster at siting** | Proposes sites, checks them against permitting and grid data, scores speed to power, and improves its search each run | [rsi.md](../theme/rsi.md), `openevolve`, `aideml`, ideas 1.1 and 1.4 | 1, 2 |
| 4.2 | **An agent that learns approval patterns** | Reads past permit decisions and learns which plan features lead to faster approval | Ideas 1.2 and 1.3 | 1 |

Have an idea to add? [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6) or arhams@stanford.edu.
