[← Front page](../../README.md) &nbsp;·&nbsp; [Concepts](README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# EV smart charging and vehicle-to-grid

**Used most in:** [Track 3 Load management](../../tracks/3-load-management/README.md) and
[Track 4 Aggregation](../../tracks/4-aggregation/README.md).

## 1. What it is

| Term | Meaning |
|---|---|
| Smart charging (V1G) | Charging power is shifted or reduced in response to prices, grid events or site limits; energy flows one way |
| Vehicle-to-grid (V2G) | A bidirectional charger lets the vehicle battery export power back to the grid |
| V2B / V2H | Export to a building or home instead of the grid, behind the meter |
| Grid-interactive charging | Charging that receives grid signals and responds, whether one-way or bidirectional |

## 2. Why it fits grid-friendly compute

| # | Point |
|---|---|
| 1 | EV chargers and compute are both large, partly flexible loads that often share a site, a feeder and a connection limit |
| 2 | Charging can be scheduled around compute peaks so the site stays under its contracted or hosting capacity |
| 3 | Parked fleets (depots, workplaces) are batteries on wheels that can be aggregated alongside compute sites |
| 4 | The same coordination stack applies: price or event signals, a controller, measurement of what was delivered |

## 3. How chargers are controlled

| Layer | Standard | Role |
|---|---|---|
| Charger to management system | OCPP (Open Charge Point Protocol) | Start, stop and set charging limits; smart charging profiles (`ocpp`) |
| Vehicle to charger | ISO 15118 (part 20 adds bidirectional power) | Plug and charge, scheduling, power transfer negotiation (`iso-15118-20`) |
| Utility or aggregator to site | OpenADR, IEEE 2030.5 | Price and event signals (`openadr`, `ieee-2030-5`; open-source 2030.5 client: `open-satori`) |
| Bidirectional charger to grid | IEEE 1547 interconnection | Exporting chargers are treated as distributed energy resources (`ieee-1547`) |

## 4. Data and tools

| Resource | What it gives you | Id |
|---|---|---|
| ACN-Data (Caltech) | Real charging sessions: arrival, departure, energy delivered | `acn-data` |
| acnportal / ACN-Sim | Simulator for scheduling many chargers under a site capacity limit | `acnportal` |
| EVerest | Open-source charger software stack (OCPP, ISO 15118) | `everest` |
| CitrineOS | Open-source charger network management for OCPP 2.0.1 (LF Energy) | `lfe-citrineos` |
| AFDC station locator | US public charging stations with an API | `afdc-stations` |
| EVI-X toolbox | Models of charging demand and infrastructure needs | `evi-x-toolbox` |
| CPUC transportation electrification | California EV programs and rules | `cpuc-transportation-electrification` |

## 5. Questions to explore

See [RFQ 3.6 and 4.6](../rfq/README.md).
