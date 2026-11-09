[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# RFQs: Requests for Questions

Problems people in the grid and compute world have today, sized for one day. Pick one, change
one, or bring your own. Each lists who has the problem, why it matters (with a source), where to
start, what checks your answer, and what to show at 18:30.

**Questions about any RFQ:** [feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6) or arhams@stanford.edu.

All ids are in the catalog: `python3 scripts/find.py <id>`.

## Track 1: Identify suitable sites

| # | Question | Who has it | Why it matters | Start with | Checked by | Show at 18:30 |
|---|---|---|---|---|---|---|
| 1.1 | Where in a chosen county could a 1 to 5 MW edge site go: near a substation and fiber, outside flood and fire zones? | Edge developer | Land use rules and hazards differ site by site (`richmond-dc-moratorium`, `fema-nfhl`) | `overpass-api`, `fema-nfhl`, `cpuc-fire-threat-map`, `fcc-broadband-map` | Scoring rules + `nrel-reopt` for onsite energy | Map of ranked sites with the evidence per site |
| 1.2 | Which existing buildings could be reused for edge compute instead of building new? | Property owner, city | Reuse avoids new construction; footprints and zoning are public | `microsoft-us-building-footprints`, `sf-property-information-map`, `national-zoning-atlas`, `mrlc-nlcd` | Filters for size, zoning, hazards | Shortlist map with reasons |
| 1.3 | What do local data center rules now require, county by county? | Developer, policy team | Moratoria, Conditional Use Permits and Special Exceptions are spreading (`loudoun-dc-standards`, `santa-clara-zoning`) | The filings in `python3 scripts/find.py --kind filing` | Agent extraction checked against the source text | Rules tracker table with citations |
| 1.4 | Where would a new edge site cut user latency the most? | Edge network operator | Latency is the reason edge exists; measured latency is public (`ripe-atlas`) | `ripe-atlas`, `peeringdb`, `census-reporter-api` | Measured RTT vs population served | Latency improvement map |
| 1.5 | What is the water and cooling risk of a candidate site? | Developer, community | Water use varies by more than 10,000x (`lbnl-water-use-workloads`) | `wri-aqueduct`, `usgs-water-data`, `noaa-cdo-api`, `open-meteo` | Climate and water stress scoring | Risk card per site |

## Track 2: Assess grid capacity at the edge

| # | Question | Who has it | Why it matters | Start with | Checked by | Show at 18:30 |
|---|---|---|---|---|---|---|
| 2.1 | How much load can each substation in a region take before a thermal or voltage violation? | Developer, utility planner | Real models are restricted (`ferc-ceii`); synthetic grids are public | `tamu-activsg10k` | `pandapower` or `matpower` power flow | Headroom map by substation |
| 2.2 | Does splitting one large load across several substations connect more of it? | Developer | Large requests far exceed approvals (`ercot-constraints-2025`) | `tamu-activsg10k` | Power flow, before vs after | Violations: one site vs split |
| 2.3 | How often do single outages (N-1) turn new load into violations? | Utility planner | Reliability is judged under outages, not only the intact network | `tamu-activsg10k` contingency list | Power flow per contingency | Share of outages causing violations, by site |
| 2.4 | When in the day and year is load headroom lowest on a feeder? | Developer, utility | PG&E publishes 576 hourly values per line section (`pge-grip-guide`) | `pge-ica` (https://grip.pge.com/), `pge-grip-guide`, `sce-ica-featureserver` | Read from the published values | Hour-by-season heatmap |
| 2.5 | How large are day-ahead load forecast errors, and are they growing where data centers connect? | Grid operator | Forecast misses drive reliability risk; PJM keeps every forecast vintage (`pjm-historical-forecasts`) | `pjm-historical-forecasts`, `eia-930`, `surge-load-forecast` | Error against actual load | Forecast error chart over time |

## Track 3: Manage loads

| # | Question | Who has it | Why it matters | Start with | Checked by | Show at 18:30 |
|---|---|---|---|---|---|---|
| 3.1 | How much can an inference cluster shift without breaking latency targets? | Cloud operator | Field demos show software-only reductions (`emerald-phoenix-2025`) | `azure-llm-inference-traces` | `sustaindc` or `vessim` | MW reduced vs requests delayed |
| 3.2 | Which batch schedule minimizes cost and carbon given tomorrow's prices and grid mix? | Data center operator | Average and marginal signals give different answers (`watttime`) | `google-cluster-data`, `caiso-todays-outlook`, `electricity-maps` | `carbon-aware-sdk`, simulator | Schedule chart with cost and carbon saved |
| 3.3 | Can batteries plus power caps smooth AI training swings? | Operator, utility | Training swings tens of MW in seconds (`google-power-smoothing-2025`) | `google-cluster-data` power traces | `sustaindc` battery model | Swing size before vs after |
| 3.4 | Which demand response programs would a 5 MW edge site qualify for, and what could it earn? | Site owner | Programs differ by region and minimum size (`miso-lmr-faq`, `ercot-ers`) | `pge-business-dr`, `sce-cbp-elect`, `ca-dsgs`, `ercot-ers`, `miso-lmr-faq` | Agent extraction checked against program text; `flex-pse` (Stanford) to schedule against the tariff | Eligibility and earnings table |
| 3.5 | Can a learned cooling policy save energy without overheating? | Facility operator | Cooling is 7% to 30%+ of data center energy (`iea-energy-ai-2025`) | `sustaindc`, `energyplus` | Simulator temperature and energy | Energy saved with temperature kept in range |
| 3.6 | Can EV charging at a compute site be scheduled around compute peaks so the site stays under its connection limit? | Site owner, fleet operator | EV charging and compute often share one connection; charging can shift | `acn-data`, workload traces, `openei-urdb` | `acnportal` (ACN-Sim) | Combined load curve vs the site limit, before and after |

## Track 4: Aggregate distributed compute

| # | Question | Who has it | Why it matters | Start with | Checked by | Show at 18:30 |
|---|---|---|---|---|---|---|
| 4.1 | Can 50 edge sites answer one grid event and deliver the requested MW? | Aggregator | VPPs are about 33 GW today (`doe-vpp-announcement-2025`) | `openleadr`, workload traces | `vessim` or `citylearn` | Dashboard: requested vs delivered MW |
| 4.2 | Which sites should respond to a request, given each site's flexibility and service limits? | Aggregator, operator | Equal MW is not equal reliability (`doe-resource-adequacy-2024`) | Track 3 outputs, `eia-930` | Assignment scored in simulation | Site assignment map and delivery score |
| 4.3 | Does a group of small sites meet a market's size, metering and telemetry rules? | Aggregator | Rules differ: 100 kW cap on minimums (`ferc-2222`), CAISO metering (`caiso-der-provider`), MISO minimums (`miso-lmr-faq`) | Those three ids, `miso-telemetry-pmu` | Rules checker against source text | Pass/fail per market with reasons |
| 4.4 | How does a compute aggregate compare with a battery VPP on delivery? | Utility, regulator | Real storage VPP performance data is public (`cec-dsgs-docket`) | `cec-dsgs-docket`, Track 3 simulations | Side by side delivery metrics | Comparison chart |
| 4.5 | Can inference move between edge sites when one site's grid is stressed, without breaking latency? | Edge operator | Edge apps need mobility across sites (`etsi-edge-native-2023`) | `ripe-atlas`, `eia-930`, inference traces | Simulated latency and grid stress | Live map of work moving between sites |
| 4.6 | Can parked EV fleets with bidirectional chargers and compute sites answer a grid event together? | Aggregator, fleet depot | Vehicle-to-grid adds storage that is already parked at many sites ([concept](../concepts/ev-smart-charging-v2g.md)) | `acn-data`, `afdc-stations`, `ocpp` | `acnportal`, `citylearn` | Requested vs delivered MW, split by vehicles and compute |

## Across tracks

| # | Question | Tracks |
|---|---|---|
| X.1 | From site to plan: choose sites, check their capacity, add the flexibility needed to connect sooner | 1, 2, 3 |
| X.2 | An agent that gets better each run at finding grid-friendly sites or schedules, with the improvement shown | Any + [guides/theme/rsi.md](../theme/rsi.md) |
| X.3 | One page per site: hazards, capacity, flexibility options, programs, all sourced | 1, 2, 3, 4 |

**Want to check whether your question is a good fit?** Email arhams@stanford.edu.
