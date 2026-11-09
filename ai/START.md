# START HERE (for ChatGPT, Claude, Gemini and other chat assistants)

SF x MIT Hack Day: Energy, Sunday 8 Nov 2026, AGI House SF. Theme: grid-friendly compute.
Schedule: 10:30 team formation, 13:00 lunch, 18:30 demos.

## How to help the user

1. Ask which track they are on, then open that track's file below and list the most relevant resources with links.
2. Prefer resources marked `access: open` (no key) for a one-day build. Flag keys, billing, paid software, large downloads.
3. Cite names and links from these files. Do not invent tools, datasets or numbers.
4. If they need something outside their track, open the other track file or the all-resources file.
5. Help them reach a working demo by 18:30 and describe how it could expand.

## Feedback

Feedback form (participants, later users, and creators of listed tools): https://forms.gle/k1pnQ4dtvfcGkuGK6
Or email arhams@stanford.edu.

## The four tracks (open the file for full lists, one resource per line)

| Track | Question | File |
|---|---|---|
| 1 Identify suitable sites | Where can distributed compute get power in months, not years? | https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/track-1-sites.md |
| 2 Assess grid capacity at the edge | How much power is there, and how soon? | https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/track-2-grid-capacity.md |
| 3 Manage loads | How can compute flex without breaking service? | https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/track-3-load-management.md |
| 4 Aggregate distributed compute | How do many sites act as one grid resource? | https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/track-4-aggregation.md |

## Other files

| File | Contents |
|---|---|
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/open-source-tools.md | 121 free tools by use, with creators (includes all 42 LF Energy projects) |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/ai/all-resources.md | All 332 resources, one per line |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/ideas/README.md | Ideas around speed to power: permitting layer, vision on city permits, AI approval plans, Omniverse grid twins |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/data/grid-hourly-2025/README.md | Starter data: hourly 2025 grid demand and generation, 12 US operators, one-line loader |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/rfq/README.md | Ready-made problems per track |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/theme/README.md | Grid-friendly compute and 19 example angles |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/concepts/load-flow.md | Load flow explained |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/concepts/grid-forming-microgrids.md | Grid-forming inverters and microgrid control |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/guides/concepts/ev-smart-charging-v2g.md | EV smart charging and vehicle-to-grid |
| https://raw.githubusercontent.com/arhamshah08/energy-hack/main/catalog/catalog.json | Machine-readable catalog |

## Featured (no install)

- **Grid Status (gridstatus.io): live and historical data for all US ISOs** by Grid Status: Web dashboards and API with live and historical prices (LMP), demand, forecasts and fuel mix across US ISOs: CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE. Browse in the browser; an account is needed for the API and downloads. Python library: gridstatus. (access: mixed; tracks: 1,2,3,4; id: gridstatus-io) https://www.gridstatus.io/
- **Load Flow Simulator (browser)** by Adjie Brotosukmono: Free browser tool: draw a single-line diagram and run AC Newton-Raphson or DC load flow (PyPSA-based), with animated flows. Examples include a 9-bus system, a 20/0.4 kV feeder and an HVDC link. Offers a link for AI agents to open a scenario. (access: open; tracks: 2; id: loadflow-simulator-web) https://tool.adjiebrotots.com/loadflow-simulator/
- **AC Grid Lab (browser AC power flow)** by Dr. Eshan Singh: Browser tool: build a one-line network on a map or diagram and solve AC power flow; starter case is a California-inspired nine-bus network with voltage and line-loading checks. JSON import and export. (access: open; tracks: 2; id: ac-grid-lab) https://www.eshansingh.xyz/acopf/
- **ED/UC Simulator: economic dispatch and unit commitment (browser)** by Adjie Brotosukmono: Free browser tool: draw a network, decide which units run hour by hour and read nodal prices (LMP); PyPSA with the HiGHS solver. Examples include a PJM 5-bus case and solar plus battery. (access: open; tracks: 2,3; id: ed-uc-simulator-web) https://tool.adjiebrotots.com/ed-uc-simulator/
- **PyPSA California: interactive grid model (browser)** by Dr. Eshan Singh: Browser app over a PyPSA optimization model of the California grid: configure demand, generation, storage, transmission and policy, then solve. No install. (access: open; tracks: 2,3; id: pypsa-ca-app) https://www.eshansingh.xyz/PyPSA-CA/app/
