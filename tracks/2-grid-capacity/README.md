[← Front page](../../README.md) &nbsp;·&nbsp; Tracks: [1 Sites](../1-sites/README.md) · [2 Grid capacity](../2-grid-capacity/README.md) · [3 Load management](../3-load-management/README.md) · [4 Aggregation](../4-aggregation/README.md) · [RFQs](../../guides/rfq/README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Track 2: Assess grid capacity at the edge

> Assess grid capacity for edge compute.

Theme link: grid-friendly compute is sized to the headroom the local grid has. See [theme](../../guides/theme/README.md).

## 1. The problem

How much load can a location take, how soon, and under what conditions? Capacity is set by
transmission and distribution limits, by outages (N-1), and by the processes utilities and grid
operators use to approve large loads. Real network models are restricted, so public work uses
utility maps, ISO reports and synthetic grids.

## 2. Facts that shape this track

| # | Fact | Source id |
|---|---|---|
| 1 | Detailed real grid models are restricted (CEII); public studies use synthetic grids | `ferc-ceii`, `tamu-synthetic-grids` |
| 2 | The western US synthetic grid has substation coordinates and an N-1 contingency list, but no hourly load | `tamu-activsg10k` |
| 3 | Utility hosting capacity maps are screening estimates, not commitments; PG&E gives 576 hourly values per line section | `pge-ica`, `pge-grip-guide`, `sce-drpep` |
| 4 | ERCOT: 238.6 GW of large-load requests vs 7.5 GW approved to energize since Jan 2022 | `ercot-constraints-2025` |
| 5 | PJM has no load queue; utilities submit large-load forecast adjustments that PJM vets | `pjm-large-load-vetting` |
| 6 | MISO is designing non-firm and step-up firm service so loads can connect before all upgrades | `miso-firm-service-step-up`, `miso-large-load-integration` |
| 7 | Large loads tripping together is now a planning concern; ride-through data is requested | `pjm-load-transfer-event-2026`, `ercot-ride-through-notice` |
| 8 | Power flow answers whether the network carries a load; production cost and capacity expansion models answer other questions | `pandapower`, `pypsa` |

## 3. Your loop in this track

| Loop part | Options in the catalog |
|---|---|
| Data | `gridstatus-io` (LMP, demand, fuel mix across all US ISOs, https://www.gridstatus.io/), `pge-ica` (PG&E GRIP, https://grip.pge.com/), `tamu-activsg10k`, `tamu-activsg2000`, `pge-grip-guide`, `sce-ica-featureserver`, `eia-930`, `gridstatus`, `pjm-historical-forecasts`, `surge-load-forecast`, `pravah` (grid weather forecasting for India, access on request: arhams@stanford.edu) |
| Verifier | `loadflow-simulator-web`, `ac-grid-lab`, `pypsa-ca-app` (browser, no install), `lfe-powsybl`, `lfe-power-grid-model`, `lfe-dynawo` (LF Energy), `pandapower`, `matpower`, `microsoft-gridsfm` (fast AC-OPF surrogate), `andes` (dynamics), `dc-emt-model` (data center EMT), `openibr` (grid-forming controls), `opendssdirect`, `gridlab-d`, `pypsa`, `pypsa-usa` |
| Metric | MW added before a thermal or voltage violation, violations under N-1, forecast error |
| Proposer | A model or search that suggests where and how much load to add, or how to split it |

## 4. Outputs that demo well

| # | Format |
|---|---|
| 1 | Map of buses or feeders coloured by remaining headroom |
| 2 | Before and after: violations with load at one bus vs spread across several |
| 3 | Headroom by hour of day or season |
| 4 | Chart of headroom found across loop iterations |

## 5. When you need another track

| You need | Go to |
|---|---|
| Which locations are worth testing | [Track 1](../1-sites/README.md) |
| How much flexible load would raise the headroom | [Track 3](../3-load-management/README.md) |
| Counting many small sites together | [Track 4](../4-aggregation/README.md) |
| Terms like hosting capacity, firm service, N-1 | [guides/reference/glossary.md](../../guides/reference/glossary.md) |
| How load flow works, and a browser tool to try it | [guides/concepts/load-flow.md](../../guides/concepts/load-flow.md) |
| Ready-to-load hourly grid data (12 operators, 2025) | [starter data](../../data/grid-hourly-2025/README.md) (`starter-us-grid-hourly-2025`) |

## 6. Resources for this track

<!-- BEGIN GENERATED -->

_Generated from the catalog by `scripts/build.py`. 126 resources tagged with this track._

Order inside each table: resources only in this track first, then ones shared with other tracks. Verified sources before preprints.

### A. Data you can use in minute one (no key)

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `caiso-resource-adequacy` | [CAISO Resource Adequacy](https://www.caiso.com/generation-transmission/resource-adequacy) | open |  | RA program pages and aggregate capacity files for the CAISO balancing area. |
| `eia-411` | [EIA-411 Coordinated Bulk Power Supply and Demand Program](https://www.eia.gov/electricity/data/eia411/) | open |  | Planners' capacity, demand and growth estimates by NERC assessment area. Geography changed in 2011. |
| `lbnl-queued-up` | [LBNL Queued Up: interconnection queue data](https://emp.lbl.gov/publications/queued-2026-edition-characteristics) | open (browser only) |  | 2026 edition: generation and storage requests through end-2025 from 7 ISOs and 50 other areas; XLSX with codebook, CC BY 4.0. Median request-to-operation over 5 years; 13% of 2000 to 2020 requests reached operation. Excludes load requests. |
| `pge-ica` | [PG&E Grid Resource Integration Portal (GRIP)](https://grip.pge.com/) | open |  | PG&E data for California: feeder and line-section load and generation hosting capacity (ICA), forecasts, grid needs, substations and lines, with map exports and a no-login REST service. PG&E says values are directional, not a guarantee. Older DRP page: pge.com distributed-resource-planning-data-and-maps. |
| `sce-ica-featureserver` | [SCE ICA ArcGIS FeatureServer](https://drpep.sce.com/arcgis_server/rest/services/hosted/ICA_Layer/FeatureServer) | open |  | Machine-readable SCE integration capacity layers. Tables at .../hosted/ICA_Tables/FeatureServer. |
| `tamu-synthetic-grids` | [Texas A&M Electric Grid Test Case Repository](https://electricgrids.engr.tamu.edu/) | open |  | Synthetic power system cases from 200 to 70,000 buses (Illinois, South Carolina, Texas, western, northeastern and eastern US) in MATPOWER, PSS/E, PowerWorld and PSLF formats. Free for commercial and non-commercial use. Not real utility networks. |
| `tamu-activsg10k` | [ACTIVSg10k: 10,000-bus synthetic grid, western US](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/) | open | 1 | Synthetic grid on the US WECC footprint, 16 areas. Package includes a MATPOWER case, substation latitude/longitude in the PowerWorld .aux file, and an N-1 branch contingency list. No hourly load time series. Also bundled with MATPOWER as case_ACTIVSg10k. |
| `tamu-activsg2000` | [ACTIVSg2000: 2,000-bus synthetic grid, Texas](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/) | open | 3 | Synthetic grid on the ERCOT footprint. Package includes a MATPOWER case, contingencies and a year of hourly load scenarios. Also bundled with MATPOWER as case_ACTIVSg2000. |
| `caiso-oasis` | [CAISO OASIS](https://oasis.caiso.com/) | open | 3 | CAISO prices, load, forecasts, transmission and ancillary service data. Queryable by URL API. |
| `caiso-todays-outlook` | [CAISO Today's Outlook](https://www.caiso.com/todays-outlook) | open | 3 | Near-real-time CAISO demand, supply, renewables and emissions dashboards with CSV downloads. |
| `eagle-i-outages` | [EAGLE-I recorded electricity outages 2014 to 2022 (ORNL)](https://doi.org/10.6084/m9.figshare.24237376) | open | 1 | Customers without power by US county at 15-minute intervals, 2014 to 2022, from DOE's EAGLE-I system. Live EAGLE-I portal: eagle-i.doe.gov. |
| `eia-930` | [EIA Hourly Electric Grid Monitor (Form EIA-930)](https://www.eia.gov/electricity/gridmonitor/) | open | 3 | Hourly demand, day-ahead demand forecast, net generation by fuel and interchange for US balancing authorities. Bulk download and API. |
| `eia-state-data` | [EIA state electricity data](https://www.eia.gov/electricity/data/state/index.php) | open | 1 | State-level capacity, generation, sales and related historical series. |
| `eia-860` | [EIA-860 Annual Electric Generator Report](https://www.eia.gov/electricity/data/eia860/) | open | 1 | Generator-level data for US plants of 1 MW and above: location, capacity, technology, status, planned additions and retirements. |
| `epoch-data-centers` | [Epoch AI data on AI data centers](https://epoch.ai/data/data-centers) | open | 1 | Tracked large AI data center projects with estimated power, compute and timelines. Focused on large sites, not edge. |
| `ercot-data` | [ERCOT data products](https://www.ercot.com/mp/data-products) | open | 3 | ERCOT load, prices, generation and system reports. ERCOT also publishes large load interconnection status reports. |
| `openinframap` | [Open Infrastructure Map](https://openinframap.org/) | open | 1 | Map of OpenStreetMap power lines, substations, power plants and telecom infrastructure. Underlying data via OSM / Overpass. |
| `overpass-api` | [Overpass API (OpenStreetMap queries)](https://wiki.openstreetmap.org/wiki/Overpass_API) | open | 1 | Query OpenStreetMap features by tag and area, e.g. power=substation, power=line with voltage, building footprints. No key; public endpoints are rate-limited. OSM coverage of grid assets is volunteer-mapped and uneven. |
| `pge-gis-hub` | [PG&E GIS Data Hub](https://pgegishub.pge.com/) | open | 1 | Selected PG&E infrastructure and risk GIS layers as ArcGIS services. |
| `pge-grip-guide` | [PG&E GRIP user guide and quick start (REST endpoint)](https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-quick-start-guide.pdf) | open | 1 | Documents PG&E load ICA: 576 hourly results per line section for four limiting criteria, feeder CSV/ZIP downloads, no-login ArcGIS REST at services2.arcgis.com/mJaJSax0KPHoCNB6/arcgis/rest/services/DRPComplianceRelProd/FeatureServer. Values are directional, not a guarantee. |
| `pudl` | [PUDL (Public Utility Data Liberation), Catalyst Cooperative](https://github.com/catalyst-cooperative/pudl) | open | 1 | Cleaned and linked EIA, FERC and EPA data in SQLite and Parquet. Removes most of the cleanup work of using raw EIA/FERC files. |
| `starter-us-grid-hourly-2025` | [Starter data: US grid demand and generation, hourly, 2025 (12 operators)](https://github.com/arhamshah08/energy-hack/tree/main/data/grid-hourly-2025) | open | 3, 4 | Ready-to-load CSV: hourly 2025 demand, day-ahead forecast, net generation, interchange and generation by fuel (coal, gas, nuclear, hydro, solar, wind, battery and more) for CAISO, ERCOT, PJM, MISO, NYISO, ISO-NE, SPP, BPA, Duke, Southern, TVA, FPL. Plus an annual summary file. One-line pandas loader in the README. |
| `eia-transmission-lines` | [EIA Energy Atlas, Electric Power Transmission Lines](https://atlas.eia.gov/datasets/geoplatform::electric-power-transmission-lines) | open | 1 | Transmission line GIS layer. Research could not retrieve metadata; an older EIA layer is archived. HIFLD legacy portal returned not-found. Check before relying on it. |

### B. Data that needs a key, account or download

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `interconnection-fyi` | [Interconnection.fyi](https://www.interconnection.fyi/) | mixed |  | Searchable aggregation of US interconnection queue projects by ISO, utility, county and point of interconnection. |
| `sce-drpep` | [SCE Distribution Resources Plan External Portal (DRPEP)](https://drpep.sce.com/drpep/) | registration |  | Southern California Edison feeder-level integration (hosting) capacity maps and grid data. Example of a utility hosting capacity portal. |
| `eia-api-v2` | [EIA Open Data API v2](https://www.eia.gov/opendata/) | api-key | 3 | JSON/CSV API for EIA series including EIA-930 hourly grid data (from 2019). Free key. |
| `eia-860m` | [EIA-860M monthly generator inventory (API)](https://www.eia.gov/opendata/browser/electricity/operating-generator-capacity/) | api-key | 1 | Monthly generator-level operating status and capacity via EIA API v2. |
| `epri-dcflex-deliverables` | [EPRI DCFlex deliverables (load shape library and reports)](https://dcflex.epri.com/deliverables) | mixed | 3, 4 | Data center load shape library (first edition 2025), storage assessments, flexible design and program mappings. |
| `gridstatus-io` | [Grid Status (gridstatus.io): live and historical data for all US ISOs](https://www.gridstatus.io/) | mixed (browser only) | 1, 3, 4 | Web dashboards and API with live and historical prices (LMP), demand, forecasts and fuel mix across US ISOs: CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE. Browse in the browser; an account is needed for the API and downloads. Python library: gridstatus. |
| `pjm-dataminer` | [PJM Data Miner 2](https://dataminer2.pjm.com/) | registration | 3 | PJM load, load forecast, LMP prices, generation and reserve data. API needs a free key. |
| `pjm-historical-forecasts` | [PJM Data Miner, historical load forecasts feed](https://dataminer2.pjm.com/feed/load_frcstd_hist/definition) | registration | 3 | Every forecast vintage since 1 Jan 2011, created every six hours. Pair with actual load to measure forecast error. |
| `pjm-7day-forecast` | [PJM Data Miner, seven-day load forecast feed](https://dataminer2.pjm.com/feed/load_frcstd_7_day) | registration | 3 | Hourly forecast MW by area with evaluation time and target time, so lead time is separable. API needs a PJM account. |
| `sdge-ica` | [SDG&E Integration Capacity Analysis](https://marketplace.sdge.com/more-information/customer-generation/enhanced-integration-capacity-analysis-ica) | registration | 1 | Distribution ICA map for SDG&E territory; 2025 update added Limited Generation Profile data. |

### C. Simulators, benchmarks and checks (the verifier in your loop)

| id | Resource | Access | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `ac-grid-lab` | [AC Grid Lab (browser AC power flow)](https://www.eshansingh.xyz/acopf/) | open | tool |  | Browser tool: build a one-line network on a map or diagram and solve AC power flow; starter case is a California-inspired nine-bus network with voltage and line-loading checks. JSON import and export. |
| `lfe-ainetus` | [AINETUS](https://lfenergy.org/projects/ainetus/) | open | tool |  | AI for Safety-Critical Network Infrastructures: human-centric AI components that support grid operators' real-time and planning decisions. LF Energy stage: Sandbox. Code: github.com/ainetus. |
| `lfe-assetlife` | [AssetLife](https://lfenergy.org/projects/assetlife/) | open | tool |  | Python library for asset management: survival analysis, renewal theory and cost calculation for maintenance and replacement decisions. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/AssetLife-project. |
| `lfe-compas` | [CoMPAS](https://lfenergy.org/projects/compas/) | open | tool |  | Shared software blocks for IEC 61850 profile configuration in digital substations. LF Energy stage: Early Adoption. Code: github.com/com-pas. |
| `lfe-dynawo` | [Dynawo](https://lfenergy.org/projects/dyna%CF%89o/) | open | simulator |  | Simulation suite for power system dynamics: voltage, frequency, short circuit and stability with power-electronic resources and HVDC. Code: github.com/dynawo. |
| `lfe-energnn` | [EnerGNN](https://lfenergy.org/projects/energnn/) | open | tool |  | Graph neural network stack (H2MG) for amortized optimization: trained once on many grid cases, it returns near-instant solutions to new ones. LF Energy stage: Sandbox. Code: github.com/energnn/energnn. |
| `lfe-fidopower` | [FIDOpower](https://lfenergy.org/projects/fidopower/) | open | tool |  | Notebook-based tools for reproducible power system analysis. LF Energy stage: Sandbox. Code: github.com/fidopower. |
| `genx` | [GenX capacity expansion model (MIT, Princeton)](https://github.com/GenXProject/GenX.jl) | open | simulator |  | Julia model that chooses which generation, storage and transmission to build and how to operate it, for low-carbon power system studies. GPL-2.0. Needs Julia and a solver. |
| `microsoft-gridsfm` | [GridSFM: small foundation models for the power grid (Microsoft Research)](https://github.com/microsoft/GridSFM) | open | simulator |  | Microsoft Research framework for small foundation models in grid optimization, starting with AC optimal power flow. Learns from graph representations of topology, load, dispatch, flows and voltages across many scenarios. Open checkpoint (GridSFM_Open), datasets on Hugging Face, and an open-data pipeline from OpenStreetMap to solved OPF cases. Suited to fast screening (contingencies, planning scenarios, new data center load) and to giving exact solvers a starting point, not replacing them. MIT. |
| `loadflow-simulator-web` | [Load Flow Simulator (browser)](https://tool.adjiebrotots.com/loadflow-simulator/) | open | tool |  | Free browser tool: draw a single-line diagram and run AC Newton-Raphson or DC load flow (PyPSA-based), with animated flows. Examples include a 9-bus system, a 20/0.4 kV feeder and an HVDC link. Offers a link for AI agents to open a scenario. |
| `manta` | [Manta: open energy system modelling platform](https://manta-plan.org/) | open | tool |  | Open-source application for energy system modelling with graphical no-code workflows and full customization; plug-ins for PyPSA, GenX, Sienna and other frameworks; runs in the cloud, locally or on-premise; AI-assisted setup, debugging and results exploration. Code: github.com/manta-plan/manta (Apache-2.0). Launched 2026; public roadmap and beta program. |
| `opendssdirect` | [OpenDSSDirect.py](https://github.com/dss-extensions/OpenDSSDirect.py) | open | simulator |  | Python bindings for OpenDSS distribution system simulator. Used for feeder-level hosting capacity studies. |
| `lfe-opengridfm` | [OpenGridFM](https://lfenergy.org/projects/opengridfm/) | open | tool |  | Open framework for building and fine-tuning foundation models for power grids. LF Energy stage: Incubation. Code: github.com/gridfm. |
| `lfe-p-swamp` | [p-SWAMP](https://lfenergy.org/projects/p-swamp/) | open | tool |  | Modular research environment for wide-area monitoring and protection with simulation. LF Energy stage: Sandbox. Code: github.com/p-swamp/P-SWAMP. |
| `pandapower` | [pandapower](https://github.com/e2nIEE/pandapower) | open | simulator |  | Python power flow and optimal power flow on pandas tables, with standard test networks. |
| `lfe-power-grid-model` | [Power Grid Model](https://lfenergy.org/projects/power-grid-model/) | open | simulator |  | Fast calculation engine for distribution grids: power flow, state estimation and short circuit. LF Energy stage: Early Adoption. Code: github.com/PowerGridModel. |
| `lfe-powsybl` | [PowSyBl](https://lfenergy.org/projects/powsybl/) | open | simulator |  | Library and tools for power system modelling: load flow, security analysis, dynamic simulation, many grid formats. MPL-2.0. LF Energy stage: Early Adoption. Code: github.com/powsybl. |
| `pypsa` | [PyPSA](https://github.com/PyPSA/PyPSA) | open | simulator |  | Python power system optimization: capacity expansion, unit commitment and power flow. |
| `pypsa-usa` | [PyPSA-USA](https://github.com/PyPSA/pypsa-usa) | open | simulator |  | Open US power system model built on PyPSA with EIA and other public data. |
| `andes` | [ANDES: power system transient dynamics in Python (CURENT)](https://github.com/CURENT/andes) | open | simulator | 4 | Python library for phasor-domain transient stability simulation with symbolic model definitions, including inverter-based resource models. See the repo for license. |
| `lfe-arras` | [Arras (formerly HiPAS GridLAB-D)](https://lfenergy.org/projects/arras/) | open | simulator | 3 | Grid and smart-grid simulation for utilities and researchers, the continuation of HiPAS GridLAB-D. LF Energy stage: Sandbox. Code: github.com/arras-energy/gridlabd. |
| `lfe-covxtreme` | [covXtreme](https://lfenergy.org/projects/covxtreme/) | open | tool | 1 | Statistical modelling of extreme values and how they occur together, for risk from rare severe conditions. LF Energy stage: Sandbox. Code: github.com/covXtreme. |
| `ed-uc-simulator-web` | [ED/UC Simulator: economic dispatch and unit commitment (browser)](https://tool.adjiebrotots.com/ed-uc-simulator/) | open | tool | 3 | Free browser tool: draw a network, decide which units run hour by hour and read nodal prices (LMP); PyPSA with the HiGHS solver. Examples include a PJM 5-bus case and solar plus battery. |
| `bess-flexible-dispatch` | [Flexible BESS dispatch and arbitrage optimizer under grid constraints](https://github.com/Mohammadrezarefaei/bess-flexible-dispatch-optimizer) | open | tool | 3 | Optimizes battery charging and discharging across market prices while respecting hourly non-firm grid export limits and degradation cost. Example data from the German market. No clear license in the repo; ask before reusing code. |
| `dc-emt-model` | [Generic EMT Modeling of Data Center Load (Dartmouth)](https://github.com/xingyuz-phd/Generic-EMT-Modeling-of-Data-Center-Load) | mixed | simulator | 3 | Modular electromagnetic transient model of a data center fed by a centralized UPS: rectifier, inverter, battery DC-DC, PFC, buck and VFD modules at three fidelity levels, IT load profiles and voltage ride-through control. Needs PSCAD 5.0.2 (commercial). No license file in the repo; ask the authors before reusing code. |
| `gridlab-d` | [GridLAB-D](https://github.com/gridlab-d/gridlab-d) | open | simulator | 4 | Distribution system and end-use load simulator from PNNL, including responsive loads and markets. |
| `lfe-grid-vantage` | [GridVantage](https://lfenergy.org/projects/grid-vantage/) | open | tool | 1 | Agent-based grid modelling with resilience metrics to help operators prepare for and recover from extreme weather. LF Energy stage: Sandbox. Code: github.com/grid-vantage. |
| `helics` | [HELICS co-simulation framework](https://github.com/GMLC-TDC/HELICS) | open | tool | 3, 4 | Couples separate simulators (grid, buildings, markets, comms) into one time-synchronized federation. Python bindings. Simulates nothing on its own. BSD-3. |
| `nixtla-timegpt` | [Nixtla TimeGPT SDK](https://github.com/Nixtla/nixtla) | api-key | api | 3 | Python SDK for TimeGPT, a pre-trained time-series foundation model for forecasting and anomaly detection, including electricity. Needs a Nixtla API key. |
| `nvidia-omniverse-dsx` | [NVIDIA Omniverse DSX Blueprint: digital twins of AI data centers](https://docs.omniverse.nvidia.com/dsx/latest/overview.html) | mixed | tool | 1, 3 | Developer blueprint for OpenUSD digital twins of gigawatt-scale AI data centers: 50-acre reference site geometry, electrical loading and thermal (CFD) simulation, web viewer. DSX Flex matches facility demand to real-time grid conditions. Needs NVIDIA software and GPUs; NVIDIA says it is not turn-key for production. |
| `openibr` | [OpenIBR: open-source grid-forming controls](https://www.openibr.org/) | open | simulator | 3 | Universal grid-forming controller for inverter-based resources and large electronic loads such as data centers, aligned with IEEE 2800 and UNIFI. v1.1 builds IEEE/CIGRE TB958 DLLs from the open C code for PSCAD and similar tools, with debug outputs and a COMTRADE-logging test environment. Code: github.com/HeronPower/OpenIBR; DLL guide: github.com/HeronPower/OpenIBR/blob/dev/documentation/9_using_the_ieee_cigre_dll.md |
| `lfe-openstef` | [OpenSTEF](https://lfenergy.org/projects/openstef/) | open | tool | 3 | Python machine learning pipelines for short-term energy forecasts. LF Energy stage: Incubation. Code: github.com/OpenSTEF/openstef. |
| `lfe-operatorfabric` | [OperatorFabric](https://lfenergy.org/projects/operatorfabric/) | open | tool | 4 | Control-room platform that brings alerts, workflows and messages from many systems into one interface. MPL-2.0. LF Energy stage: Early Adoption. Code: github.com/opfab. |
| `pypsa-ca-app` | [PyPSA California: interactive grid model (browser)](https://www.eshansingh.xyz/PyPSA-CA/app/) | open | tool | 3 | Browser app over a PyPSA optimization model of the California grid: configure demand, generation, storage, transmission and policy, then solve. No install. |
| `lfe-seapath` | [SEAPATH](https://lfenergy.org/projects/seapath/) | open | tool | 4 | Real-time platform that runs IEC 61850 substation protection and control as virtual machines or containers on standard servers. LF Energy stage: Graduated. Code: github.com/seapath. |
| `lfe-sogno` | [SOGNO](https://lfenergy.org/projects/sogno/) | open | tool | 4 | Modular, cloud-native automation for distribution utilities: monitoring, state estimation and control. LF Energy stage: Early Adoption. Code: github.com/sogno-platform. |
| `surge-load-forecast` | [surge: open probabilistic day-ahead US load forecasts](https://github.com/tylergibbs1/surge) | open | tool | 3 | Day-ahead probabilistic load forecasts for all 53 US balancing authorities: Chronos-2 fine-tuned on seven years of EIA-930 data. MIT. |
| `timecopilot` | [TimeCopilot: agentic forecasting framework](https://github.com/TimeCopilot/timecopilot) | open | tool | 3 | LLM agent over time-series foundation models: forecast, cross-validate and detect anomalies from natural-language requests through one API. MIT. |
| `lfe-varen` | [VAREN](https://lfenergy.org/projects/varen/) | open | tool | 1 | Python library that automates analysis of mobile LiDAR of overhead distribution lines and nearby vegetation. LF Energy stage: Sandbox. Code: github.com/varen-project. |

### D. Other tools and APIs

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `gridstatus` | [gridstatus (Python library)](https://github.com/gridstatus/gridstatus) | open | 3 | Python API for load, prices, fuel mix and queue data from US ISOs (CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE). |
| `inframation` | [Inframation (inframation.io): map of the energy buildout (FREE BETA)](https://inframation.io/) | open | 1, 4 | Free while in beta, per https://inframation.io/pricing. Searchable map of planned, under-construction, operating and retired power plants, batteries, data centers, large loads, lines and substations in the US and GB, plus energy RFPs and funding, built from interconnection queues, EIA-860M and permit registers with every record linked to its source. Includes a site finder (land near high-voltage lines and substations, out of the floodplain), free RSS/JSON feeds and a keyless public API at https://api.inframation.io. |
| `pravah` | Pravah: weather forecasting for the grid (India) (access on request) | on-request | 3 | Weather forecasting built for power grid operations in India. Not public: access on request. Email arhams@stanford.edu for a contact. |

### E. Papers and reports

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `caiso-lcr-2027` | [CAISO 2027 Local Capacity Requirements](https://stakeholdercenter.prod.caiso.com/RecurringStakeholderProcesses/Local-capacity-requirements-process-2027) | verified | report |  | Local reliability studies and capacity requirements for constrained California transmission areas. |
| `eia-aeo2026` | [EIA, Annual Energy Outlook 2026 narrative](https://www.eia.gov/outlooks/aeo/narrative/) | verified | report |  | High Electricity Demand case with more AI servers; high-case server consumption reaches 818 TWh in 2050. |
| `ercot-large-load-update-2026` | [ERCOT, Interconnection and Grid Analysis Update (Apr 2026)](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf) | verified | report |  | As of 26 Mar 2026, data centers were 87.6% of MW in ERCOT's large-load request portfolio. |
| `pjm-novec-forecast` | [NOVEC data center forecast documentation (PJM 2026 forecast)](https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/novec-documentation.pdf) | verified | report |  | Bottom-up utility method: contract milestones, site control, zoning; moderate-risk projects discounted 50%. July peak 1,387 MW (2025) to 5,032 MW (2030) forecast. |
| `pjm-load-forecast-2025` | [PJM, 2025 Long-Term Load Forecast Report](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.ashx) | verified | report |  | 20-year zonal peak and energy forecast with data center adjustments in 10 zones. Summer peak +3.1%/yr, 209,923 MW by 2035. Tables in Excel. |
| `pjm-2025-review` | [PJM, 2025 Year in Review: Planning](https://insidelines.pjm.com/2025-year-in-review-planning-prepares-for-burgeoning-electricity-demand/) | verified | report |  | Vetted data center load projected to grow about 30 GW from 2025 to 2030. |
| `pjm-load-forecast-2026` | [PJM, 2026 Long-Term Load Forecast](https://insidelines.pjm.com/pjms-updated-20-year-forecast-continues-to-see-significant-long-term-load-growth/) | verified | report |  | 10-year average growth 3.6%/yr summer peak, 4.0%/yr winter peak; data center adjustments a major component. |
| `wecc240-2011` | [Price and Goodin, Reduced Network Modeling of WECC as a Market Design Prototype (IEEE PES 2011)](https://ieeexplore.ieee.org/abstract/document/6039476) | verified | paper |  | Describes a 240-bus reduced Western Interconnection model built by CAISO staff, detailed inside California, with hourly load profiles for CAISO areas. Paywalled; the case file is not bundled with MATPOWER. |
| `doe-i2x-der-roadmap` | [DOE i2X, DER Interconnection Roadmap (2025)](https://www.energy.gov/sites/default/files/2025-01/i2X%20DER%20Interconnection%20Roadmap.pdf) | verified | report | 3, 4 | Distribution DER interconnection under 100 kV / 80 MW. 2030 targets: under 75 days for 50 kW to 5 MW, under 140 days above 5 MW. Aspirational, not legal deadlines. |
| `doe-grid-codes` | [DOE, Distribution Grid Code Adoption Pathways (2024)](https://www.energy.gov/sites/default/files/2024-07/48726_DOE_OE_TDC_Distribution_Grid_Codes_Pathways_RELEASE_508.pdf) | verified | report | 4 | Taxonomy of grid codes; hosting capacity publication choices and five validation stages. |
| `doe-grid-orchestration` | [DOE, Distribution Grid Orchestration (Nov 2024)](https://www.energy.gov/documents/distribution-grid-orchestration) | verified | report | 3, 4 | Taxonomy of DER orchestration: dispatch-signal, autonomous, behavioral; local feeder constraints vs grid-wide signals; OpenADR and IEEE 2030.5 roles. |
| `doe-large-load-rates` | [DOE, Electricity Rate Designs for Large Loads (2025)](https://www.energy.gov/policy/articles/electricity-rate-designs-large-loads-evolving-practices-and-opportunities) | verified | report | 3 | Utility and regulatory treatment of large new loads: cost allocation and rate design. |
| `doe-microgrids-large-loads` | [DOE, Microgrids, Large Electric Loads and Grid Support](https://www.energy.gov/oe/articles/microgrids-large-electric-loads-grid-support-how-leverage-microgrids-support-utilities) | verified | report | 3, 4 | US data center use rose from 58 TWh (2014) to 176 TWh (2023), 325 to 580 TWh possible by 2028; covers storage, CHP and microgrids for large loads. |
| `doe-transmission-needs` | [DOE, National Transmission Needs Study](https://www.energy.gov/oe/national-transmission-needs-study) | verified | report | 1 | Current and future transmission constraints as demand rises; most modeled congestion falls in a small fraction of hours. |
| `doe-resource-adequacy-2024` | [DOE, The Future of Resource Adequacy (2024)](https://www.energy.gov/sites/default/files/2024-04/2024%20The%20Future%20of%20Resource%20Adequacy%20Report.pdf) | verified | report | 3, 4 | Explains nameplate vs capacity credit: equal MW is not equal reliability. Covers DR, DERMS, ADMS, VPPs. |
| `eia-aeo2026-servers` | [EIA, Data center server energy use grows across the commercial building stock (AEO2026)](https://www.eia.gov/todayinenergy/detail.php?id=67704) | verified | report | 3 | AEO2026 models data center server electricity separately and uses an essentially flat server load shape. |
| `eia-wholesale-markets` | [EIA, wholesale electricity markets overview](https://www.eia.gov/electricity/wholesalemarkets/) | verified | report | 4 | Map and links for each US ISO/RTO region. |
| `epri-powering-intelligence-2024` | [EPRI, Powering Intelligence (2024)](https://www.epri.com/research/products/3002028905) | verified | report | 1 | Scenarios of US data center load growth to 2030 with state-level breakdown. |
| `ercot-constraints-2025` | [ERCOT, 2025 Report on Existing and Potential Electric System Constraints and Needs](https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf) | verified | report | 3 | 238.6 GW of large-load requests vs 7,502 MW approved to energize since Jan 2022. Unadjusted 2031 TSP forecast 218 GW vs studied 159 GW. $30.21B transmission planned 2026 to 2031. |
| `ercot-legislative-update-2026` | [ERCOT, Large Load update to Texas legislature (Apr 2026)](https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf) | verified | report | 3 | About 410 GW of large-load requests (about 87% data centers) as of 26 Mar 2026. Explains batch studies about every six months; proposed $50,000/MW security fee. |
| `ferc-energy-primer` | [FERC, Energy Primer (2024 edition)](https://www.ferc.gov/sites/default/files/2024-01/24_Energy-Markets-Primer_0117_DIGITAL_0.pdf) | verified | report | 3, 4 | Staff handbook on electricity and gas markets; RTO/ISO sections for PJM, MISO, CAISO. Vocabulary, not tariff. |
| `iea-energy-ai-2025` | [IEA, Energy and AI (2025)](https://www.iea.org/reports/energy-and-ai) | verified | report | 1 | Global data centers used 415 TWh in 2024 (about 1.5%); 945 TWh in 2030 base case. US and China are nearly 80% of growth. Data centers build in 2 to 3 years, grid infrastructure takes longer. CC BY 4.0. |
| `iea-key-questions-2026` | [IEA, Key Questions on Energy and AI (2026)](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) | verified | report | 3 | Data center demand grew 17% in 2025 (AI-focused 50%); 485 TWh in 2025 to about 950 TWh in 2030. Projects 20 to 25 GW batteries and 15 to 27 GW onsite gas at data centers by 2030. CC BY 4.0. |
| `lbnl-integrating-ai-dc` | [LBNL, Integrating AI Data Centers with the Power Grid (2026)](https://eta.lbl.gov/publications/integrating-ai-data-centers-power) | verified | paper | 3, 4 | Four flexibility mechanisms: temporal/geographic compute shifting, facility infrastructure flexibility, storage, onsite generation. |
| `lbnl-dc-energy-2025-update` | [LBNL, United States Data Center Energy Usage Report: 2025 Update](https://datacenters.lbl.gov/publications/united-states-data-center-energy-2025) | verified | report | 1, 3 | Estimates US data center use at 521 to 843 TWh in 2030, 9.5% to 15.3% of US electricity, central estimate 11.8%. |
| `duke-rethinking-load-growth-2025` | [Norris et al., Rethinking Load Growth (Duke Nicholas Institute, 2025)](https://nicholasinstitute.duke.edu/publications/rethinking-load-growth) | verified | report | 3 | First-order study of the 22 largest balancing authorities: nearly 100 GW of new load could use existing capacity if it accepts limited curtailment during grid stress. |
| `nvidia-dsx-announcement-2025` | [NVIDIA, Omniverse DSX Blueprint for gigawatt-scale AI factories (Oct 2025)](https://blogs.nvidia.com/blog/omniverse-dsx-blueprint/) | verified | report | 3 | Announces DSX Boost (power-optimized operation), DSX Flex (demand matched to real-time grid conditions with AI agents from Emerald AI and Phaidra) and DSX Exchange. NVIDIA claims DSX Flex can help tap some of 100 GW of underused grid capacity (vendor claim). |
| `pge-redwood-microgrid` | [PG&E EPIC 3.11, Redwood Coast Airport Microgrid final report (2024)](https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.11.pdf) | verified | report | 1, 3, 4 | Measured community microgrid: 2.3 MW / 8.8 MWh battery plus 2.2 MW PV; 51+ hours of resilience across 12 events; fixed limited interconnection avoided reconductoring. |
| `pjm-load-transfer-event-2026` | [PJM / Dominion review of large load transfer event (Aug 2026)](https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/) | verified | report | 3 | Nearly 4,000 MW of data center load disconnected unexpectedly in Virginia on 22 Jul 2026; earlier events were about 1,500 MW. |
| `lbnl-dc-energy-2024` | [Shehabi et al., 2024 United States Data Center Energy Usage Report (LBNL)](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report) | verified | report | 1 | US data centers used 176 TWh, about 4.4% of US electricity, in 2023; 325 to 580 TWh (6.7% to 12%) projected for 2028. Bottom-up equipment model. Superseded by lbnl-dc-energy-2025-update for 2030. |
| `va-jlarc-2024` | [Virginia JLARC, Data Centers in Virginia (2024)](https://rga.lis.virginia.gov/Published/2025/RD206/PDF) | verified | report | 1 | State investigation: 250+ interviews, independent demand forecast, E3 grid cost modeling. About 50 ongoing jobs vs 1,500 at construction peak for a 250k sq ft site; low-frequency noise; $14 to $37/month added residential cost by 2040 (modeled). |

### F. Programs, rules and standards

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `ercot-batch-zero` | [ERCOT / PUCT, Batch Zero process for large loads (Jun 2026)](https://www.ercot.com/news/release/06182026-puct-approves-ercots) | verified | program |  | PUCT approved ERCOT's batch study process to decide how much large load ERCOT can reliably connect and where. |
| `ferc-ceii` | [FERC Critical Energy/Electric Infrastructure Information (CEII)](https://www.ferc.gov/ceii) | verified | policy |  | Rules restricting detailed grid data such as real network models; access requires a request and non-disclosure agreement. The reason public studies rely on synthetic grids. |
| `miso-eras` | [MISO, Expedited Resource Addition Study (ERAS)](https://www.misoenergy.org/meet-miso/media-center/2025---news-releases/ferc-approves-misos-expedited-resource-addition-study/) | verified | program |  | FERC-approved temporary fast track for generation interconnection; first requests Aug 2025. A generation pathway, not a load queue. |
| `miso-gen-load-alignment` | [MISO, Generation and Large Load Alignment (LLWG-2026-6)](https://www.misoenergy.org/engage/MISO-Dashboard/generation-and-large-load-alignment/) | verified | program |  | Proposal to study large loads together with the generation serving them. Under development. |
| `pjm-large-load-vetting` | [PJM, annual vetting of large load requests (Sep 2026)](https://insidelines.pjm.com/pjm-kicks-off-annual-process-of-vetting-large-load-requests/) | verified | program |  | PJM has no load interconnection queue; load-serving entities submit large-load adjustments to the forecast, which PJM vets. |
| `lfe-trolie` | [TROLIE](https://lfenergy.org/projects/trolie/) | verified | standard |  | Open specification for exchanging current and forecast transmission line ratings, as required by FERC Order 881. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/trolie/spec. |
| `cec-data-centers` | [California Energy Commission, Data Centers](https://www.energy.ca.gov/programs-and-topics/topics/data-centers) | verified | program | 1 | CEC does not generally permit data centers but forecasts their demand. Early 2026 data centers were about 1,000 MW, roughly 2% of CAISO peak. |
| `lfe-cds-power-systems-data` | [CDS Power Systems Data](https://lfenergy.org/projects/cds-power-systems-data/) | verified | standard | 3 | Open specification for raw power system data, aimed at more accurate grid emissions reporting. Code: github.com/lfe-cds/CDS-Power-Systems-Data. |
| `doe-demand-growth-hub` | [DOE, Electricity Demand Growth Resource Hub](https://www.energy.gov/policy/electricity-demand-growth-resource-hub) | verified | program | 3, 4 | Federal hub of analyses, programs and resources on rapid load growth, including data centers. |
| `doe-ai-datacenter-hub` | [DOE, Powering America's AI Future: Data Center Resource Hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub) | verified | program | 1, 3, 4 | Federal hub on data center demand, flexibility, efficiency, grid integration, water and DOE programs. |
| `epri-dcflex-demos` | [EPRI DCFlex demonstrations](https://dcflex.epri.com/demonstrations) | verified | program | 3, 4 | At least ten planned demos (Phoenix, Lenoir, Paris, Chicago named): AI workload modulation, DR, backup integration, ride-through. Page does not give curtailment MW. |
| `ercot-ride-through-notice` | [ERCOT market notice, large electronic load ride-through (Jun 2025)](https://www.ercot.com/services/comm/mkt_notices/M-B062325-01) | verified | filing | 3 | ERCOT asked data center and crypto loads of 75 MW+ for voltage ride-through data because simultaneous trips threaten reliability. |
| `ercot-nprr1234` | [ERCOT NPRR1234, large load interconnection requirements](https://www.ercot.com/mktrules/issues/NPRR1234) | verified | standard | 3 | Interconnection and modeling requirements for loads of 25 MW or more. |
| `ieee-1547` | [IEEE 1547-2018](https://standards.ieee.org/ieee/1547/5915/) | verified | standard | 4 | Interconnection and interoperability standard for DERs connected to distribution grids. |
| `loudoun-dc-standards` | [Loudoun County, Data Center Standards and Locations](https://www.loudoun.gov/5990/Data-Center-Standards-Locations) | verified | program | 1 | Phase 1 (approved 18 Mar 2025) moved data centers from by-right to Special Exception in affected areas. Phase 2 (plan approved 16 Sep 2025) covers data center and substation standards. Includes existing/proposed data center map. |
| `miso-firm-service-step-up` | [MISO, Firm Service Step Up for large load interconnections](https://www.misoenergy.org/engage/MISO-Dashboard/firm-service-step-up-for-large-load-interconnections/) | verified | program | 3 | Proposed process letting large loads start with reduced firm service before all upgrades are complete. |
| `miso-large-load-integration` | [MISO, Large Load Additions framework](https://www.misoenergy.org/planning/large-loads---container-page/large-load-additions/) | verified | program | 3, 4 | Requests seek connection in 18 to 36 months. Goal of approval within 120 days. Mechanisms include non-firm service, firm-service step-up, curtailment, telemetry, ride-through. |
| `pjm-disconnection-standards-2026` | [PJM, proposed reliability standards for large load disconnection (Sep 2026)](https://insidelines.pjm.com/reliability-standards-to-manage-large-load-disconnection-events-proposed-by-pjm/) | verified | filing | 3 | Proposed requirements for computational loads after the July 2026 event and a June 2026 FERC directive. Proposal, not effective rule. |
| `texas-sb6-2025` | [Texas SB 6 (89th Legislature, 2025): large load rules in ERCOT](https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=SB6) | unverified | policy | 3 | Texas law on interconnection standards and grid-emergency curtailment for large loads such as data centers. Read the enrolled text for thresholds. |

<!-- END GENERATED -->
