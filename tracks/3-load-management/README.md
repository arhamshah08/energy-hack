[← Front page](../../README.md) &nbsp;·&nbsp; Tracks: [1 Sites](../1-sites/README.md) · [2 Grid capacity](../2-grid-capacity/README.md) · [3 Load management](../3-load-management/README.md) · [4 Aggregation](../4-aggregation/README.md) · [RFQs](../../guides/rfq/README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Track 3: Manage loads

> Manage compute loads so they are grid-friendly.

Theme link: grid-friendly compute reduces, shifts or smooths its load when the grid is stressed. See [theme](../../guides/theme/README.md).

## 1. The problem

When and how can compute change its power draw without breaking service? Options include moving
jobs in time or place, capping power, using batteries or onsite generation, adjusting cooling, and
smoothing fast swings from AI training. Each option has a cost in delay, energy or reliability.

## 2. Facts that shape this track

| # | Fact | Source id |
|---|---|---|
| 1 | Four flexibility mechanisms: compute shifting (time, place), facility infrastructure, storage, onsite generation | `lbnl-integrating-ai-dc` |
| 2 | Google shifts non-urgent work by site and hour when grid events are called; no MW series published | `google-dr-2023`, `google-dc-demand-response-2025` |
| 3 | A 2025 field demo cut an AI cluster's power 25% for 3 hours with software only (preprint) | `emerald-phoenix-2025` |
| 4 | Synchronized ML jobs swing tens of MW within seconds; smoothing cut swings about 50% for under 1% slowdown | `google-power-smoothing-2025` |
| 5 | Demand response was 2.6% of CAISO resource adequacy capacity in summer 2024 | `caiso-dmm-dr-2024` |
| 6 | Average and marginal carbon signals give different answers for load shifting | `watttime`, `electricity-maps` |
| 7 | Public inference traces have timestamps and token counts, not power or deadlines | `azure-llm-inference-traces` |

## 3. Your loop in this track

| Loop part | Options in the catalog |
|---|---|
| Data | `gridstatus-io` (prices and demand across all US ISOs, https://www.gridstatus.io/), `google-cluster-data` (incl. power traces), `azure-llm-inference-traces`, `alibaba-clusterdata`, `eia-930`, `caiso-todays-outlook`, `openei-urdb`, `epri-dcflex-deliverables` |
| Verifier | `flex-pse` (Stanford), `lfe-flexmeasures`, `lfe-openstef` (LF Energy), `sustaindc`, `vessim`, `nrgise-open`, `bess-flexible-dispatch`, `surge-load-forecast`, `timecopilot`, `pvlib-python`, `energyplus`, `carbon-aware-sdk`, `nrel-reopt` |
| Metric | MW reduced and for how long, delayed or dropped jobs, energy cost, emissions, peak demand charge, swing size |
| Proposer | A model, policy or LLM that proposes schedules, caps or setpoints |

**Featured:** [FlexMeasures](https://github.com/FlexMeasures/flexmeasures) by [Seita](https://seita.nl/) (Nicolas Höning), an open-source engine that schedules flexible loads, batteries and generation against prices and grid limits.
[flex-pse](https://github.com/flex-pse/flex-pse), from Stanford, schedules a facility's
energy use against real tariffs and demand response signals. Interested? Join the
[flex-pse Slack](https://join.slack.com/t/flex-pse/shared_invite/zt-4b2va6ztg-K74JiAdHsmqY2CoGjbOmIQ).

## 4. Outputs that demo well

| # | Format |
|---|---|
| 1 | Load curve before and after, with the grid event or price shown |
| 2 | Trade-off chart: MW reduced vs jobs delayed |
| 3 | Policy score across loop iterations (cost, carbon, delay) |

## 5. When you need another track

| You need | Go to |
|---|---|
| How much flexibility the grid needs at a location | [Track 2](../2-grid-capacity/README.md) |
| Running the same policy across many sites | [Track 4](../4-aggregation/README.md) |
| Where the flexible load should be built | [Track 1](../1-sites/README.md) |
| Program rules (who pays for flexibility) | Section F below, [Track 4](../4-aggregation/README.md) |
| Batteries, microgrids, EV charging at the site | [grid-forming microgrids](../../guides/concepts/grid-forming-microgrids.md), [EV smart charging and V2G](../../guides/concepts/ev-smart-charging-v2g.md) |
| Ready-to-load hourly grid data for shifting studies | [starter data](../../data/grid-hourly-2025/README.md) (`starter-us-grid-hourly-2025`) |

## 6. Resources for this track

<!-- BEGIN GENERATED -->

_Generated from the catalog by `scripts/build.py`. 143 resources tagged with this track._

Order inside each table: resources only in this track first, then ones shared with other tracks. Verified sources before preprints.

### A. Data you can use in minute one (no key)

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `comstock` | [NREL (now NLR) ComStock](https://comstock.nlr.gov/) | open |  | Simulated hourly end-use load profiles for the US commercial building stock. |
| `lfe-opensynth` | [OpenSynth](https://lfenergy.org/projects/opensynth/) | open |  | Open data community for synthetic and real energy datasets, starting with demand. LF Energy stage: Sandbox. Code: github.com/OpenSynth-energy. |
| `tamu-activsg2000` | [ACTIVSg2000: 2,000-bus synthetic grid, Texas](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg2000/) | open | 2 | Synthetic grid on the ERCOT footprint. Package includes a MATPOWER case, contingencies and a year of hourly load scenarios. Also bundled with MATPOWER as case_ACTIVSg2000. |
| `afdc-stations` | [AFDC alternative fuel station locator (US DOE)](https://afdc.energy.gov/stations) | open | 1 | US public EV charging stations with location, network, connector types and power level. API through the NREL developer network (free key). |
| `alibaba-clusterdata` | [Alibaba cluster traces](https://github.com/alibaba/clusterdata) | open | 4 | Production traces 2017 to 2026, including GPU traces (2020, 2023, 2025, 2026 up to 155k GPUs), LLM serving and spot GPU. Some downloads need a survey; license per release. |
| `azure-llm-inference-traces` | [Azure LLM inference traces 2023, 2024 and multimodal 2025](https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2024.md) | open | 4 | Production request traces: timestamp, context tokens, generated tokens (plus images in the 2025 multimodal trace). No power, location or deadlines. CC BY. |
| `azure-public-dataset` | [Azure Public Dataset](https://github.com/Azure/AzurePublicDataset) | open | 4 | Azure VM, serverless function and LLM inference request traces. The inference traces show request timing and token counts. |
| `caiso-oasis` | [CAISO OASIS](https://oasis.caiso.com/) | open | 2 | CAISO prices, load, forecasts, transmission and ancillary service data. Queryable by URL API. |
| `caiso-todays-outlook` | [CAISO Today's Outlook](https://www.caiso.com/todays-outlook) | open | 2 | Near-real-time CAISO demand, supply, renewables and emissions dashboards with CSV downloads. |
| `cec-dsgs-docket` | [CEC docket 22-RENEW-01 (DSGS data and guidelines)](https://efiling.energy.ca.gov/Lists/DocketLog.aspx?docketnumber=22-RENEW-01) | open | 4 | Includes anonymized 2024 and 2025 storage VPP performance workbooks (monthly site and hourly discharge), enrolled capacity by county. Measured distributed storage, not compute. |
| `eia-930` | [EIA Hourly Electric Grid Monitor (Form EIA-930)](https://www.eia.gov/electricity/gridmonitor/) | open | 2 | Hourly demand, day-ahead demand forecast, net generation by fuel and interchange for US balancing authorities. Bulk download and API. |
| `eia-861` | [EIA-861 Annual Electric Power Industry Report](https://www.eia.gov/electricity/data/eia861/) | open | 4 | Utility-level sales, customers, revenue, demand response program enrollment and distributed generation by US utility. |
| `epa-egrid` | [EPA eGRID](https://www.epa.gov/egrid) | open | 1 | Emissions and generation mix for US power plants and grid subregions. Annual average emission rates. |
| `ercot-data` | [ERCOT data products](https://www.ercot.com/mp/data-products) | open | 2 | ERCOT load, prices, generation and system reports. ERCOT also publishes large load interconnection status reports. |
| `google-cluster-data` | [Google cluster workload traces](https://github.com/google/cluster-data) | open | 4 | Borg traces: 2019 (eight cells, May 2019) and 2011 (one ~12,500-machine cell), plus power traces for 57 power domains in May 2019. CC BY. |
| `lfe-node-collective` | [NODE Collective](https://lfenergy.org/projects/node-collective/) | open | 1 | National open database of US electrification incentives and rebates. LF Energy stage: Sandbox. Code: github.com/NODE-Collective. |
| `open-meteo` | [Open-Meteo weather API](https://open-meteo.com/) | open | 1 | Weather forecasts and historical reanalysis by coordinate, hourly, JSON. No key for non-commercial use. |
| `openei-urdb` | [OpenEI Utility Rate Database](https://openei.org/wiki/Utility_Rate_Database) | open | 1 | US retail electricity tariffs including energy charges, demand charges and time-of-use periods. API available. |
| `starter-us-grid-hourly-2025` | [Starter data: US grid demand and generation, hourly, 2025 (12 operators)](https://github.com/arhamshah08/energy-hack/tree/main/data/grid-hourly-2025) | open | 2, 4 | Ready-to-load CSV: hourly 2025 demand, day-ahead forecast, net generation, interchange and generation by fuel (coal, gas, nuclear, hydro, solar, wind, battery and more) for CAISO, ERCOT, PJM, MISO, NYISO, ISO-NE, SPP, BPA, Duke, Southern, TVA, FPL. Plus an annual summary file. One-line pandas loader in the README. |

### B. Data that needs a key, account or download

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `acn-data` | [ACN-Data: EV charging sessions (Caltech)](https://ev.caltech.edu/dataset) | registration | 4 | Real EV charging sessions from Caltech, JPL and an office site: arrival, departure, energy requested and delivered. API with a free token. |
| `eia-api-v2` | [EIA Open Data API v2](https://www.eia.gov/opendata/) | api-key | 2 | JSON/CSV API for EIA series including EIA-930 hourly grid data (from 2019). Free key. |
| `electricity-maps` | [Electricity Maps API](https://app.electricitymaps.com/docs) | api-key (browser only) | 4 | Zone-level carbon intensity, mix, flows, load and day-ahead prices: latest, history and forecast; 5 min to hourly. Lifecycle and flow-traced by default, not marginal. 14-day trial. |
| `epri-dcflex-deliverables` | [EPRI DCFlex deliverables (load shape library and reports)](https://dcflex.epri.com/deliverables) | mixed | 2, 4 | Data center load shape library (first edition 2025), storage assessments, flexible design and program mappings. |
| `google-solar-api` | [Google Solar API](https://developers.google.com/maps/documentation/solar/overview) | api-key | 1 | Per-building roof area, panel layouts, sunshine hours and estimated yearly solar output. Needs a Google Cloud project with billing and an API key. |
| `gridstatus-io` | [Grid Status (gridstatus.io): live and historical data for all US ISOs](https://www.gridstatus.io/) | mixed (browser only) | 1, 2, 4 | Web dashboards and API with live and historical prices (LMP), demand, forecasts and fuel mix across US ISOs: CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE. Browse in the browser; an account is needed for the API and downloads. Python library: gridstatus. |
| `nsrdb` | [National Solar Radiation Database (NSRDB)](https://nsrdb.nlr.gov/) | api-key | 1 | Gridded hourly and sub-hourly solar irradiance and weather. Used to model on-site solar output at a location. |
| `noaa-cdo-api` | [NOAA Climate Data Online API v2](https://www.ncei.noaa.gov/cdo-web/webservices/v2) | api-key | 1 | Station observations and climate normals as JSON. Token header; 5 requests/s, 10,000/day; max 1,000 results per call. |
| `pjm-dataminer` | [PJM Data Miner 2](https://dataminer2.pjm.com/) | registration | 2 | PJM load, load forecast, LMP prices, generation and reserve data. API needs a free key. |
| `pjm-historical-forecasts` | [PJM Data Miner, historical load forecasts feed](https://dataminer2.pjm.com/feed/load_frcstd_hist/definition) | registration | 2 | Every forecast vintage since 1 Jan 2011, created every six hours. Pair with actual load to measure forecast error. |
| `pjm-7day-forecast` | [PJM Data Miner, seven-day load forecast feed](https://dataminer2.pjm.com/feed/load_frcstd_7_day) | registration | 2 | Hourly forecast MW by area with evaluation time and target time, so lead time is separable. API needs a PJM account. |
| `watttime` | [WattTime API](https://watttime.org/data-science/data-signals/) | api-key | 4 | Signals: co2_moer (marginal, lb/MWh), co2_aoer (average), health_damage (USD/MWh), with forecasts for load shifting. API docs could not be fetched in research; check access terms. |

### C. Simulators, benchmarks and checks (the verifier in your loop)

| id | Resource | Access | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `kepler` | [Kepler (Kubernetes power exporter)](https://github.com/sustainable-computing-io/kepler) | open | tool |  | Exports estimated power use per Kubernetes pod and container as Prometheus metrics. |
| `nilmtk` | [NILMTK: Non-Intrusive Load Monitoring Toolkit](https://github.com/nilmtk/nilmtk) | open | tool |  | Toolkit to disaggregate a whole-building meter into appliance loads, with loaders for public datasets including the US REDD dataset. Apache-2.0. |
| `nrgise-open` | [NRGISE Open: local energy system simulator](https://github.com/nrgise-open/nrgise-open) | open | simulator |  | Python time-step simulation of local energy systems (PV, storage, loads) with control strategies: peak shaving, self-consumption, controller benchmarking, forecast-error studies, batch sweeps. pip install nrgise. CC BY-NC-SA 4.0 (non-commercial). |
| `powerapi` | [PowerAPI](https://powerapi.org/) | open | tool |  | Python framework for software-defined power meters down to process level. Estimates, not physical metering. BSD-3. |
| `lfe-rtc-tools` | [RTC-Tools](https://lfenergy.org/projects/rtc-tools/) | open | tool |  | Toolbox for control and optimization of time-dependent systems, originally water systems; MESIDO extends it to energy networks. LF Energy stage: Sandbox. Code: github.com/Multi-Energy-Systems-Optimization/mesido. |
| `lfe-rtdip` | [RTDIP: Real Time Data Ingestion Platform](https://lfenergy.org/projects/real-time-data-ingestion-platform-rtdip/) | open | tool |  | Cloud pipelines for ingesting and querying real-time and historical time-series data. LF Energy stage: Sandbox. Code: github.com/rtdip. |
| `scaphandre` | [Scaphandre](https://github.com/hubblo-org/scaphandre) | open | tool |  | Rust agent reporting host and VM power, exporting to Prometheus, JSON and others. Early-stage. Apache-2.0. |
| `lfe-smart-hems-benchmark` | [Smart HEMS Benchmark](https://lfenergy.org/projects/smart-hems-benchmark/) | open | benchmark |  | Manufacturer-neutral benchmark for home energy management systems with solar and batteries. LF Energy stage: Sandbox. Code: github.com/SMART-HEMS-Benchmark/smart-hems-benchmark. |
| `nrel-solar-forecasting` | [Solar-Forecasting: physics-based smart persistence model (NREL, now NLR)](https://github.com/NatLabRockies/Solar-Forecasting) | open | tool |  | NREL software record SWR-18-36: physics-based smart persistence model for intra-hour solar forecasting. BSD-3. Last updated 2022. |
| `sunspec-svp` | [SunSpec System Validation Platform (OpenSVP)](https://github.com/sunspec/svp) | open | tool |  | Open-source Python test platform and scripts for DER conformance testing against IEEE 1547.1, UL 1741 SA and AS/NZS 4777.2 with lab equipment or simulation. |
| `sustaindc` | [SustainDC (HPE dc-rl)](https://github.com/HewlettPackard/dc-rl) | open | simulator |  | Multi-agent RL environments for data center workload shifting, HVAC setpoints and batteries with carbon, weather and Alibaba/Google workload inputs. Metrics: energy, carbon, water, dropped tasks. Mixed MIT / CC BY-NC. |
| `acnportal` | [acnportal / ACN-Sim (Caltech)](https://github.com/zach401/acnportal) | open | simulator | 4 | Simulator for scheduling many EV chargers under site capacity limits, plus a client for ACN-Data. BSD-3. |
| `lfe-arras` | [Arras (formerly HiPAS GridLAB-D)](https://lfenergy.org/projects/arras/) | open | simulator | 2 | Grid and smart-grid simulation for utilities and researchers, the continuation of HiPAS GridLAB-D. LF Energy stage: Sandbox. Code: github.com/arras-energy/gridlabd. |
| `carbon-aware-sdk` | [Carbon Aware SDK (Green Software Foundation)](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | open | tool | 4 | Web API and CLI that wrap carbon intensity providers and return the best time and location to run a workload. |
| `lfe-citrineos` | [CitrineOS](https://lfenergy.org/projects/citrineos/) | open | tool | 4 | Open-source charger network management software for OCPP 2.0.1: monitor, control and manage charging stations. Code: github.com/citrineos/citrineos. |
| `ed-uc-simulator-web` | [ED/UC Simulator: economic dispatch and unit commitment (browser)](https://tool.adjiebrotots.com/ed-uc-simulator/) | open | tool | 2 | Free browser tool: draw a network, decide which units run hour by hour and read nodal prices (LMP); PyPSA with the HiGHS solver. Examples include a PJM 5-bus case and solar plus battery. |
| `energyplus` | [EnergyPlus (now under NatLabRockies)](https://github.com/NatLabRockies/EnergyPlus) | open | simulator | 1 | Whole-building energy and HVAC simulation with Python API. Needs facility inputs; not a calibrated data center model out of the box. |
| `evi-x-toolbox` | [EVI-X toolbox (NREL, now NLR)](https://afdc.energy.gov/evi-x-toolbox) | open | tool | 1 | Models for EV charging demand and infrastructure needs (EVI-Pro family), with web versions. |
| `flex-pse` | [flex-pse: industrial energy flexibility optimization (Stanford)](https://github.com/flex-pse/flex-pse) | open | tool | 4 | Stanford open-source Pyomo/IDAES toolbox: model a facility as a time-discretized optimization, fit it from plant data, and schedule it against real electricity tariffs and demand response signals. pip install flex-pse. Apache-2.0. Community Slack: https://join.slack.com/t/flex-pse/shared_invite/zt-4b2va6ztg-K74JiAdHsmqY2CoGjbOmIQ |
| `bess-flexible-dispatch` | [Flexible BESS dispatch and arbitrage optimizer under grid constraints](https://github.com/Mohammadrezarefaei/bess-flexible-dispatch-optimizer) | open | tool | 2 | Optimizes battery charging and discharging across market prices while respecting hourly non-firm grid export limits and degradation cost. Example data from the German market. No clear license in the repo; ask before reusing code. |
| `lfe-flexmeasures` | [FlexMeasures](https://lfenergy.org/projects/flexmeasures/) | open | tool | 4 | Open-source energy optimization engine that forecasts and schedules flexible loads, batteries and generation against prices and grid limits, for real-time operations. Built by Seita (https://seita.nl/), founded by Nicolas Höning; hosted by LF Energy. LF Energy stage: Incubation. Code: github.com/FlexMeasures/flexmeasures (Apache-2.0). |
| `dc-emt-model` | [Generic EMT Modeling of Data Center Load (Dartmouth)](https://github.com/xingyuz-phd/Generic-EMT-Modeling-of-Data-Center-Load) | mixed | simulator | 2 | Modular electromagnetic transient model of a data center fed by a centralized UPS: rectifier, inverter, battery DC-DC, PFC, buck and VFD modules at three fidelity levels, IT load profiles and voltage ride-through control. Needs PSCAD 5.0.2 (commercial). No license file in the repo; ask the authors before reusing code. |
| `helics` | [HELICS co-simulation framework](https://github.com/GMLC-TDC/HELICS) | open | tool | 2, 4 | Couples separate simulators (grid, buildings, markets, comms) into one time-synchronized federation. Python bindings. Simulates nothing on its own. BSD-3. |
| `lfe-hyphae` | [Hyphae](https://lfenergy.org/projects/hyphae/) | open | tool | 4 | Microgrid software connecting buildings, homes and devices to local generation, storage and EV batteries. LF Energy stage: Incubation. Code: github.com/hyphae. |
| `nixtla-timegpt` | [Nixtla TimeGPT SDK](https://github.com/Nixtla/nixtla) | api-key | api | 2 | Python SDK for TimeGPT, a pre-trained time-series foundation model for forecasting and anomaly detection, including electricity. Needs a Nixtla API key. |
| `nvidia-omniverse-dsx` | [NVIDIA Omniverse DSX Blueprint: digital twins of AI data centers](https://docs.omniverse.nvidia.com/dsx/latest/overview.html) | mixed | tool | 1, 2 | Developer blueprint for OpenUSD digital twins of gigawatt-scale AI data centers: 50-acre reference site geometry, electrical loading and thermal (CFD) simulation, web viewer. DSX Flex matches facility demand to real-time grid conditions. Needs NVIDIA software and GPUs; NVIDIA says it is not turn-key for production. |
| `lfe-opendsm` | [OpenDSM (formerly OpenEEmeter)](https://lfenergy.org/projects/opendsm/) | open | tool | 4 | Measures savings and demand-side impact from meter data, for programs that need verified results. Code: github.com/opendsm/opendsm. |
| `openibr` | [OpenIBR: open-source grid-forming controls](https://www.openibr.org/) | open | simulator | 2 | Universal grid-forming controller for inverter-based resources and large electronic loads such as data centers, aligned with IEEE 2800 and UNIFI. v1.1 builds IEEE/CIGRE TB958 DLLs from the open C code for PSCAD and similar tools, with debug outputs and a COMTRADE-logging test environment. Code: github.com/HeronPower/OpenIBR; DLL guide: github.com/HeronPower/OpenIBR/blob/dev/documentation/9_using_the_ieee_cigre_dll.md |
| `lfe-openstef` | [OpenSTEF](https://lfenergy.org/projects/openstef/) | open | tool | 2 | Python machine learning pipelines for short-term energy forecasts. LF Energy stage: Incubation. Code: github.com/OpenSTEF/openstef. |
| `pvlib-python` | [pvlib-python](https://github.com/pvlib/pvlib-python) | open | simulator | 1 | Python functions for solar position, irradiance, PV cell temperature and DC/AC output. The standard open PV performance model. BSD-3. |
| `pypsa-ca-app` | [PyPSA California: interactive grid model (browser)](https://www.eshansingh.xyz/PyPSA-CA/app/) | open | tool | 2 | Browser app over a PyPSA optimization model of the California grid: configure demand, generation, storage, transmission and policy, then solve. No install. |
| `qualitylogic-2030-5-test-tools` | [QualityLogic IEEE 2030.5 test tools](https://www.qualitylogic.com/industries/smart-energy/smart-energy-test-tool-solutions/ieee-2030-5-test-tools/) | paid | tool | 4 | Commercial IEEE 2030.5 and CSIP test system for clients and servers, used as a certification test harness. Not open source. |
| `nrel-reopt` | [REopt (NREL, now NLR)](https://github.com/NREL/REopt.jl) | open | simulator | 1 | Optimizes the size and dispatch of on-site solar, storage and generators for a site's load and tariff. Julia package and web API. |
| `surge-load-forecast` | [surge: open probabilistic day-ahead US load forecasts](https://github.com/tylergibbs1/surge) | open | tool | 2 | Day-ahead probabilistic load forecasts for all 53 US balancing authorities: Chronos-2 fine-tuned on seven years of EIA-930 data. MIT. |
| `nrel-sam` | [System Advisor Model (SAM, NREL, now NLR)](https://sam.nlr.gov/) | open | simulator | 1 | Performance and financial models for solar, wind, storage and other systems. Python access through PySAM. |
| `timecopilot` | [TimeCopilot: agentic forecasting framework](https://github.com/TimeCopilot/timecopilot) | open | tool | 2 | LLM agent over time-series foundation models: forecast, cross-validate and detect anomalies from natural-language requests through one API. MIT. |
| `vessim` | [Vessim](https://github.com/dos-group/vessim) | open | simulator | 4 | Co-simulation testbed for computing systems with solar, batteries and grid signals. Built for carbon-aware computing experiments. |

### D. Other tools and APIs

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `codibly-2030-5-accelerator` | [Codibly IEEE 2030.5 Accelerator](https://codibly.com/accelerators/ieee-2030-5-accelerator) | paid | 4 | Pre-certified IEEE 2030.5 client and server code sold under a perpetual license with source. Codibly is a SunSpec authorized test lab for IEEE 2030.5 and CSIP. Not open source. |
| `coral-npu` | [Coral NPU (Google)](https://github.com/google-coral/coralnpu) | open | 4 | Open machine learning accelerator core designed for energy-efficient AI at the edge. Hardware design, Apache-2.0. |
| `energyhub-derms` | [EnergyHub edge DERMS utility integrations](https://www.energyhub.com/edge-derms-platform/utility-integrations) | paid | 4 | Commercial DERMS integration gateway, including GE Vernova GridOS. No public API or sandbox. |
| `epri-flex-mosaic` | [EPRI Flex MOSAIC](https://dcflex.epri.com/flex-mosaic) | mixed | 4 | Framework classifying data center flexibility by response characteristics across workloads, generation, storage and cooling. |
| `gridstatus` | [gridstatus (Python library)](https://github.com/gridstatus/gridstatus) | open | 2 | Python API for load, prices, fuel mix and queue data from US ISOs (CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE). |
| `openleadr` | [OpenLEADR (OpenADR 2.0b in Python)](https://github.com/OpenLEADR/openleadr-python) | open | 4 | LF Energy project with open-source OpenADR implementations: openleadr-python (OpenADR 2.0b VEN and VTN, developmental) and openleadr-rs (Rust, OpenADR 3). Code: github.com/openleadr. |
| `pravah` | Pravah: weather forecasting for the grid (India) (access on request) | on-request | 2 | Weather forecasting built for power grid operations in India. Not public: access on request. Email arhams@stanford.edu for a contact. |
| `dersec-py1815` | [py1815: open IEEE 1815 (DNP3) outstation](https://github.com/DERSecurity/py1815) | open | 4 | The DNP3 (IEEE 1815) outstation of Project Satori, for distributed energy resources. Companion to the py20305 IEEE 2030.5 client. |
| `pysunspec2` | [pySunSpec2: SunSpec Modbus library](https://github.com/sunspec/pysunspec2) | open | 4 | Python library for reading and controlling SunSpec Modbus devices such as inverters and batteries. Model definitions at github.com/sunspec/models. Used as the Modbus bridge in Project Satori. |
| `open-satori` | [Satori: open IEEE 2030.5 and SunSpec Modbus reference implementations](https://open-satori.org) | open | 4 | IEEE 2030.5 / CSIP client with a SunSpec Modbus bridge that connects inverters, batteries and EVs to utility programs without firmware changes. pip install py20305; code at github.com/DERSecurity/py20305 (Apache-2.0). Satori Scout, the free iOS/Android reference app, handles device discovery, simulation and VPP connectivity (source under commercial license). |
| `gridappsd-2030-5` | [GRIDAPPS-D IEEE 2030.5 repositories](https://github.com/GRIDAPPSD) | open | 4 | Go components for IEEE 2030.5 server, client and inverter simulator. Repository existence only; conformance not checked. |

### E. Papers and reports

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `google-power-smoothing-2025` | [Google Cloud, Mitigating power and thermal fluctuations in ML infrastructure (2025)](https://cloud.google.com/blog/topics/systems/mitigating-power-and-thermal-fluctuations-in-ml-infrastructure) | verified | report |  | Synchronized ML clusters swing tens of MW every few seconds; compiler-level smoothing cut swings about 50% with under 1% performance loss and slightly higher average power. |
| `google-carbon-aware-2021` | [Radovanovic et al., Carbon-Aware Computing for Datacenters (Google, 2021)](https://arxiv.org/abs/2106.11750) | preprint | paper |  | Google's system that shifts flexible compute in time using day-ahead carbon forecasts and cluster-level virtual capacity curves. |
| `caiso-dmm-dr-2024` | [CAISO DMM, Demand Response Issues and Performance 2024](https://www.caiso.com/documents/demand-response-issues-and-performance-2024-feb-20-2025.pdf) | verified | report | 4 | DR was about 1,400 MW, 2.6% of CAISO RA capacity in summer 2024; only 44% of utility PDR RA capacity was bid on high-load days. |
| `caiso-dmm-dr-2025` | [CAISO DMM, Demand Response Issues and Performance 2025](https://www.caiso.com/notices/department-of-market-monitoring-demand-response-issues-and-performance-2025-report-posted) | verified | report | 4 | 2025 demand response activity and performance across CAISO and WEIM. |
| `doe-i2x-der-roadmap` | [DOE i2X, DER Interconnection Roadmap (2025)](https://www.energy.gov/sites/default/files/2025-01/i2X%20DER%20Interconnection%20Roadmap.pdf) | verified | report | 2, 4 | Distribution DER interconnection under 100 kV / 80 MW. 2030 targets: under 75 days for 50 kW to 5 MW, under 140 days above 5 MW. Aspirational, not legal deadlines. |
| `doe-grid-orchestration` | [DOE, Distribution Grid Orchestration (Nov 2024)](https://www.energy.gov/documents/distribution-grid-orchestration) | verified | report | 2, 4 | Taxonomy of DER orchestration: dispatch-signal, autonomous, behavioral; local feeder constraints vs grid-wide signals; OpenADR and IEEE 2030.5 roles. |
| `doe-large-load-rates` | [DOE, Electricity Rate Designs for Large Loads (2025)](https://www.energy.gov/policy/articles/electricity-rate-designs-large-loads-evolving-practices-and-opportunities) | verified | report | 2 | Utility and regulatory treatment of large new loads: cost allocation and rate design. |
| `doe-microgrids-large-loads` | [DOE, Microgrids, Large Electric Loads and Grid Support](https://www.energy.gov/oe/articles/microgrids-large-electric-loads-grid-support-how-leverage-microgrids-support-utilities) | verified | report | 2, 4 | US data center use rose from 58 TWh (2014) to 176 TWh (2023), 325 to 580 TWh possible by 2028; covers storage, CHP and microgrids for large loads. |
| `doe-sourcing-der` | [DOE, Sourcing DER for Distribution Services (2024)](https://www.energy.gov/sites/default/files/2024-12/Sourcing%20DER%20for%20Dist%20Services%20final%2012.17.24.pdf) | verified | report | 4 | How utilities procure DER for local distribution needs, distinct from wholesale aggregation. |
| `doe-resource-adequacy-2024` | [DOE, The Future of Resource Adequacy (2024)](https://www.energy.gov/sites/default/files/2024-04/2024%20The%20Future%20of%20Resource%20Adequacy%20Report.pdf) | verified | report | 2, 4 | Explains nameplate vs capacity credit: equal MW is not equal reliability. Covers DR, DERMS, ADMS, VPPs. |
| `doe-vpp-announcement-2025` | [DOE, VPP Liftoff update announcement (Jan 2025)](https://www.energy.gov/technologycommercialization/articles/us-department-energy-releases-new-reports-highlighting) | verified | report | 4 | 33 GW of VPPs in North America; 80 to 160 GW by 2030 scenario (10% to 20% of peak). |
| `eia-aeo2026-servers` | [EIA, Data center server energy use grows across the commercial building stock (AEO2026)](https://www.eia.gov/todayinenergy/detail.php?id=67704) | verified | report | 2 | AEO2026 models data center server electricity separately and uses an essentially flat server load shape. |
| `epri-dcflex-programs` | [EPRI DCFlex Workstream 2: Programs](https://dcflex.epri.com/workstream-2) | verified | report | 4 | Maps US and European utility programs and market services to EPRI flexibility classes. |
| `ercot-constraints-2025` | [ERCOT, 2025 Report on Existing and Potential Electric System Constraints and Needs](https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf) | verified | report | 2 | 238.6 GW of large-load requests vs 7,502 MW approved to energize since Jan 2022. Unadjusted 2031 TSP forecast 218 GW vs studied 159 GW. $30.21B transmission planned 2026 to 2031. |
| `ercot-legislative-update-2026` | [ERCOT, Large Load update to Texas legislature (Apr 2026)](https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf) | verified | report | 2 | About 410 GW of large-load requests (about 87% data centers) as of 26 Mar 2026. Explains batch studies about every six months; proposed $50,000/MW security fee. |
| `ferc-energy-primer` | [FERC, Energy Primer (2024 edition)](https://www.ferc.gov/sites/default/files/2024-01/24_Energy-Markets-Primer_0117_DIGITAL_0.pdf) | verified | report | 2, 4 | Staff handbook on electricity and gas markets; RTO/ISO sections for PJM, MISO, CAISO. Vocabulary, not tariff. |
| `google-dr-2023` | [Google Cloud, Using demand response to reduce data center power consumption (2023)](https://cloud.google.com/blog/products/infrastructure/using-demand-response-to-reduce-data-center-power-consumption) | verified | report | 4 | Grid event notices feed Google's compute planner, which sets hourly limits on non-urgent tasks per site (delay or reroute). Europe, Taiwan, US examples. No MW series published. |
| `iea-key-questions-2026` | [IEA, Key Questions on Energy and AI (2026)](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) | verified | report | 2 | Data center demand grew 17% in 2025 (AI-focused 50%); 485 TWh in 2025 to about 950 TWh in 2030. Projects 20 to 25 GW batteries and 15 to 27 GW onsite gas at data centers by 2030. CC BY 4.0. |
| `jrc-eu-coc-2024` | [JRC, 2024 EU Code of Conduct for Data Centres best practice guidelines](https://e3p.jrc.ec.europa.eu/sites/default/files/2024-04/JRC136986_2024_best_practice_guidelines.pdf) | verified | report | 1 | Catalogue of data center practices (cooling, airflow, waste heat, geography, water, monitoring) with 1 to 5 qualitative values that must not be summed. CC BY 4.0. |
| `ca-dr-potential-phase4` | [LBNL / CPUC, California Demand Response Potential Study Phase 4 (2024)](https://eta.lbl.gov/publications/california-demand-response-0) | verified | report | 4 | Shed and shift DR potential in California through 2050 by end use. |
| `lbnl-dc-flex-workshop` | [LBNL / DOE, Data Center Load Flexibility Workshop Summary (2025)](https://eta.lbl.gov/publications/doe-data-center-load-flexibility) | verified | report | 4 | Nov 2024 workshop, 49 participants: workload shifting, storage, onsite generation, demand response, communications and control needs. |
| `lbnl-integrating-ai-dc` | [LBNL, Integrating AI Data Centers with the Power Grid (2026)](https://eta.lbl.gov/publications/integrating-ai-data-centers-power) | verified | paper | 2, 4 | Four flexibility mechanisms: temporal/geographic compute shifting, facility infrastructure flexibility, storage, onsite generation. |
| `lbnl-water-use-workloads` | [LBNL, The water use of data center workloads (2025)](https://datacenters.lbl.gov/publications/water-use-data-center-workloads) | verified | paper | 1 | Workload-level water use varies by more than four orders of magnitude with server efficiency, grid water factors, cooling, climate and utilization. |
| `lbnl-dc-energy-2025-update` | [LBNL, United States Data Center Energy Usage Report: 2025 Update](https://datacenters.lbl.gov/publications/united-states-data-center-energy-2025) | verified | report | 1, 2 | Estimates US data center use at 521 to 843 TWh in 2030, 9.5% to 15.3% of US electricity, central estimate 11.8%. |
| `duke-rethinking-load-growth-2025` | [Norris et al., Rethinking Load Growth (Duke Nicholas Institute, 2025)](https://nicholasinstitute.duke.edu/publications/rethinking-load-growth) | verified | report | 2 | First-order study of the 22 largest balancing authorities: nearly 100 GW of new load could use existing capacity if it accepts limited curtailment during grid stress. |
| `nvidia-dsx-announcement-2025` | [NVIDIA, Omniverse DSX Blueprint for gigawatt-scale AI factories (Oct 2025)](https://blogs.nvidia.com/blog/omniverse-dsx-blueprint/) | verified | report | 2 | Announces DSX Boost (power-optimized operation), DSX Flex (demand matched to real-time grid conditions with AI agents from Emerald AI and Phaidra) and DSX Exchange. NVIDIA claims DSX Flex can help tap some of 100 GW of underused grid capacity (vendor claim). |
| `pge-redwood-microgrid` | [PG&E EPIC 3.11, Redwood Coast Airport Microgrid final report (2024)](https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.11.pdf) | verified | report | 1, 2, 4 | Measured community microgrid: 2.3 MW / 8.8 MWh battery plus 2.2 MW PV; 51+ hours of resilience across 12 events; fixed limited interconnection avoided reconductoring. |
| `pjm-load-transfer-event-2026` | [PJM / Dominion review of large load transfer event (Aug 2026)](https://insidelines.pjm.com/pjm-dominion-review-large-load-transfer-event/) | verified | report | 2 | Nearly 4,000 MW of data center load disconnected unexpectedly in Virginia on 22 Jul 2026; earlier events were about 1,500 MW. |
| `emerald-phoenix-2025` | [Colangelo et al., Turning AI Data Centers into Grid-Interactive Assets (2025)](https://arxiv.org/abs/2507.00909) | preprint | paper | 4 | Field demo in Phoenix: software-only control cut an AI cluster's power by 25% for 3 hours during a grid peak event. |

### F. Programs, rules and standards

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `lfe-battery-data-alliance` | [Battery Data Alliance](https://lfenergy.org/projects/battery-data-alliance/) | verified | standard |  | Common software and data schemas for battery data across companies. LF Energy stage: Sandbox. Code: github.com/battery-data-alliance. |
| `lfe-cds-customer-data` | [CDS Customer Data](https://lfenergy.org/projects/cds-customer-data/) | verified | standard |  | Open specifications for access to utility customer energy data, for carbon accounting, efficiency and flexibility use cases. Code: github.com/lfe-cds/CDS-Customer-Data. |
| `google-dc-demand-response-2025` | [Google, data center demand response agreements with utilities (2025)](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/) | verified | program |  | Aug 2025: agreements with Indiana Michigan Power and TVA to reduce ML workload power during grid events, after three OPPD events in 2024. Google calls it early-stage and location-limited. No MW, payments or event caps disclosed. |
| `pge-business-dr` | [PG&E business demand response programs (incl. Capacity Bidding)](https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/business-programs.html) | verified | program |  | Capacity Bidding Program and other business DR offerings with incentives and performance obligations. |
| `lfe-urpx` | [Utility Rate Plan Exchange (URPX)](https://lfenergy.org/projects/utility-rate-plan-exchange-urpx/) | verified | standard |  | Open, machine-readable standard for utility tariffs and rate plans. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/urpx-org. |
| `caiso-demand-response` | [CAISO Demand Response participation](https://www.caiso.com/generation-transmission/load/demand-response) | verified | program | 4 | Proxy Demand Resource and Reliability DR Resource models. Needs a scheduling coordinator and revenue-quality meters; ancillary services need telemetry. |
| `caiso-der-provider` | [CAISO Distributed Energy Resource Provider model](https://www.caiso.com/generation-transmission/generation/distributed-energy-resources) | verified | program | 4 | DER aggregations in wholesale markets. Utility concurrence review of 30 business days, then onboarding, metering and agreements. |
| `caiso-ddemi-2026` | [CAISO, Demand and Distributed Energy Market Integration straw proposal (Mar 2026)](https://stakeholdercenter.caiso.com/InitiativeDocuments/Straw-Proposal-and-Issue-Paper-Demand-and-Distributed-Energy-Market-Integration-Mar-13-2026.pdf) | verified | filing | 4 | Stakeholder initiative on market pathways for large flexible loads and DER aggregations. |
| `ca-dsgs` | [California Demand Side Grid Support (DSGS) program](https://www.energy.ca.gov/programs-and-topics/programs/demand-side-grid-support-program) | verified | program | 4 | Pays eligible customers for net load reduction and backup generation during extreme events, May to October. Fifth Edition guidelines adopted 27 Apr 2026. |
| `lfe-cds-power-systems-data` | [CDS Power Systems Data](https://lfenergy.org/projects/cds-power-systems-data/) | verified | standard | 2 | Open specification for raw power system data, aimed at more accurate grid emissions reporting. Code: github.com/lfe-cds/CDS-Power-Systems-Data. |
| `cpuc-transportation-electrification` | [CPUC transportation electrification](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/infrastructure/transportation-electrification) | verified | program | 4 | California utility EV programs, rates and rulemakings, including vehicle-grid integration. |
| `doe-demand-growth-hub` | [DOE, Electricity Demand Growth Resource Hub](https://www.energy.gov/policy/electricity-demand-growth-resource-hub) | verified | program | 2, 4 | Federal hub of analyses, programs and resources on rapid load growth, including data centers. |
| `doe-ai-datacenter-hub` | [DOE, Powering America's AI Future: Data Center Resource Hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub) | verified | program | 1, 2, 4 | Federal hub on data center demand, flexibility, efficiency, grid integration, water and DOE programs. |
| `epri-dcflex` | [EPRI DCFlex](https://dcflex.epri.com/) | verified | program | 4 | EPRI initiative with utilities, operators and hyperscalers to demonstrate data center flexibility at field sites. |
| `epri-dcflex-demos` | [EPRI DCFlex demonstrations](https://dcflex.epri.com/demonstrations) | verified | program | 2, 4 | At least ten planned demos (Phoenix, Lenoir, Paris, Chicago named): AI workload modulation, DR, backup integration, ride-through. Page does not give curtailment MW. |
| `ercot-ers` | [ERCOT Emergency Response Service (ERS)](https://www.ercot.com/services/programs/load/eils) | verified | program | 4 | Loads, generators and aggregations paid to reduce consumption within 10 or 30 minutes during energy emergencies. Procured four times a year via QSEs. ERCOT is not under FERC Order 2222. |
| `ercot-ride-through-notice` | [ERCOT market notice, large electronic load ride-through (Jun 2025)](https://www.ercot.com/services/comm/mkt_notices/M-B062325-01) | verified | filing | 2 | ERCOT asked data center and crypto loads of 75 MW+ for voltage ride-through data because simultaneous trips threaten reliability. |
| `ercot-nprr1234` | [ERCOT NPRR1234, large load interconnection requirements](https://www.ercot.com/mktrules/issues/NPRR1234) | verified | standard | 2 | Interconnection and modeling requirements for loads of 25 MW or more. |
| `ferc-2222-fact-sheet` | [FERC Order No. 2222 fact sheet](https://www.ferc.gov/media/ferc-order-no-2222-fact-sheet) | verified | policy | 4 | Minimum aggregation size in RTO/ISO markets may be no greater than 100 kW. |
| `iso-15118-20` | [ISO 15118-20: vehicle to grid communication interface](https://www.iso.org/standard/77845.html) | verified | standard | 4 | Standard for communication between vehicle and charger, adding bidirectional power transfer to plug and charge and scheduling. Paid standard. |
| `miso-firm-service-step-up` | [MISO, Firm Service Step Up for large load interconnections](https://www.misoenergy.org/engage/MISO-Dashboard/firm-service-step-up-for-large-load-interconnections/) | verified | program | 2 | Proposed process letting large loads start with reduced firm service before all upgrades are complete. |
| `miso-large-load-integration` | [MISO, Large Load Additions framework](https://www.misoenergy.org/planning/large-loads---container-page/large-load-additions/) | verified | program | 2, 4 | Requests seek connection in 18 to 36 months. Goal of approval within 120 days. Mechanisms include non-firm service, firm-service step-up, curtailment, telemetry, ride-through. |
| `miso-telemetry-pmu` | [MISO, large load telemetry and PMU requirements](https://www.misoenergy.org/engage/MISO-Dashboard/operational-reliability-requirement---large-load-telemetry-and-phasor-measurement-unit-pmu-requirements/) | verified | standard | 4 | Draft: real-time large load telemetry over ICCP and PMU measurements at the point of interconnection. |
| `miso-lmr-faq` | [MISO, LMR and demand response enrollment FAQ](https://help.misoenergy.org/knowledgebase/article/KA-01560/en-us) | verified | program | 4 | Minimums: LMR 0.1 MW, DRR 1 MW, EDR 0.1 MW. 2 to 6 hour notice, events up to 4 hours, up to 16 dispatches a year. Enrollment tool opens 1 Dec 2026; no API. |
| `ocpp` | [OCPP: Open Charge Point Protocol (Open Charge Alliance)](https://openchargealliance.org/protocols/open-charge-point-protocol/) | verified | standard | 4 | Open protocol between EV chargers and charging management systems, including smart charging profiles that cap or schedule charging power. |
| `openadr` | [OpenADR 3.0](https://www.openadr.org/openadr-3-0) | verified | standard | 4 | REST/OpenAPI standard for DR, price and DER signals; public YAML spec supplements 2.0a/b. Reference implementation is members-only; certification is separate from implementing the API. |
| `lfe-ores` | [ORES: Open Renewable Energy Systems](https://lfenergy.org/projects/ores-open-renewable-energy-systems/) | verified | standard | 4 | Open standards and practice for plug-and-play microgrids and grid-interactive device metadata and APIs. LF Energy stage: Sandbox. Code: github.com/open-renewable-energy-systems. |
| `pge-rule-24` | [PG&E Rule 24 (third-party demand response)](https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/rule-24.html) | verified | program | 4 | Customers enroll with third-party DR providers that bid aggregated reductions into CAISO. |
| `pjm-disconnection-standards-2026` | [PJM, proposed reliability standards for large load disconnection (Sep 2026)](https://insidelines.pjm.com/reliability-standards-to-manage-large-load-disconnection-events-proposed-by-pjm/) | verified | filing | 2 | Proposed requirements for computational loads after the July 2026 event and a June 2026 FERC directive. Proposal, not effective rule. |
| `sce-cbp-elect` | [SCE Capacity Bidding Program Elect](https://www.sce.com/save-money/savings-programs/enroll-in-savings-programs/capacity-bidding-program-elect) | verified | program | 4 | Pays participants for temporary reductions during high demand; overlap restrictions with other DR programs. |
| `sce-elrp` | [SCE Emergency Load Reduction Program](https://www.sce.com/factsheet/emergency-load-reduction-program) | verified | program | 4 | Seven-year DR pilot 2021 to 2027 for qualifying non-residential customers, including CCA and Direct Access. |
| `sunspec-specifications` | [SunSpec specifications and certification](https://sunspec.org/specifications/) | verified | standard | 4 | SunSpec Alliance specifications for DER communication (SunSpec Modbus, IEEE 2030.5/CSIP test specs, security). Certification programs and test labs: https://sunspec.org/certifications/. |
| `open-eac-alliance` | [OpenEAC Alliance M&V methodologies](https://github.com/wattcarbon/open-eac-alliance) |  | standard | 4 | Open, peer-reviewed measurement and verification (M&V) methodologies for issuing Energy Attribute Certificates (EACs) per watt-hour or gram CO2e from battery storage, electrification, demand response and energy efficiency projects. Methods and statuses at methods.openeac.org; drafts go through a 30-day public comment period. |
| `texas-sb6-2025` | [Texas SB 6 (89th Legislature, 2025): large load rules in ERCOT](https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=SB6) | unverified | policy | 2 | Texas law on interconnection standards and grid-emergency curtailment for large loads such as data centers. Read the enrolled text for thresholds. |

<!-- END GENERATED -->
