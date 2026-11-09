[← Front page](../../README.md) &nbsp;·&nbsp; Tracks: [1 Sites](../1-sites/README.md) · [2 Grid capacity](../2-grid-capacity/README.md) · [3 Load management](../3-load-management/README.md) · [4 Aggregation](../4-aggregation/README.md) · [RFQs](../../guides/rfq/README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Track 4: Aggregate distributed compute

> Aggregate distributed compute to make it grid-friendly.

Theme link: grid-friendly compute is coordinated across sites so the grid can rely on it. See [theme](../../guides/theme/README.md).

## 1. The problem

How can many small compute sites act as one resource for the grid? That needs a way to receive
grid signals, decide which sites respond, move work between sites, meter and prove what was
delivered, and meet market or program rules.

## 2. Facts that shape this track

| # | Fact | Source id |
|---|---|---|
| 1 | FERC Order 2222 requires organized markets to accept DER aggregations; minimum size up to 100 kW; not ERCOT | `ferc-2222`, `ferc-2222-fact-sheet` |
| 2 | CAISO aggregations need utility concurrence (30 business days), a scheduling coordinator and revenue-quality meters | `caiso-der-provider`, `caiso-demand-response` |
| 3 | MISO demand response minimums: 0.1 MW (LMR), 1 MW (DRR); up to 16 dispatches a year | `miso-lmr-faq` |
| 4 | North America had about 33 GW of VPPs; DOE scenario 80 to 160 GW by 2030 | `doe-vpp-announcement-2025` |
| 5 | OpenADR 3 is a public REST/OpenAPI spec; certification is separate | `openadr` |
| 6 | Equal MW does not give equal reliability; capacity credit depends on timing and duration | `doe-resource-adequacy-2024` |
| 7 | Edge applications need mobility and discovery across sites with intermittent links | `etsi-edge-native-2023` |

## 3. Your loop in this track

| Loop part | Options in the catalog |
|---|---|
| Data | `caiso-dmm-dr-2024`, `cec-dsgs-docket` (storage VPP performance), `eia-930`, `peeringdb`, workload traces (Track 3) |
| Verifier | `citylearn`, `helics`, `gridlab-d`, `vessim` |
| Coordination platforms | `lfe-flexmeasures` (by [Seita](https://seita.nl/), Nicolas Höning), `lfe-shapeshifter`, `lfe-hyphae`, `lfe-geisa` (LF Energy) |
| Protocols | `openadr`, `openleadr`, `lfe-cupid`, `ieee-2030-5`, `open-satori` (open-source 2030.5 client by DERSec), `gridappsd-2030-5` |
| Metric | Aggregate MW available, delivered vs committed, response time, minimum size met |
| Proposer | A model or policy that assigns grid requests to sites |

## 4. Outputs that demo well

| # | Format |
|---|---|
| 1 | Dashboard: grid signal in, sites responding, total MW delivered vs requested |
| 2 | Map of sites with live status |
| 3 | Delivery accuracy across loop iterations |

## 5. When you need another track

| You need | Go to |
|---|---|
| How each site can flex | [Track 3](../3-load-management/README.md) |
| Where the sites are and their grid limits | [Track 1](../1-sites/README.md), [Track 2](../2-grid-capacity/README.md) |
| Terms like DERMS, VPP, VTN/VEN | [guides/reference/glossary.md](../../guides/reference/glossary.md) |
| Aggregating EVs alongside compute | [EV smart charging and V2G](../../guides/concepts/ev-smart-charging-v2g.md) |
| Ideas for many-site coordination | [ideas](../../guides/ideas/README.md) |

## 6. Resources for this track

<!-- BEGIN GENERATED -->

_Generated from the catalog by `scripts/build.py`. 95 resources tagged with this track._

Order inside each table: resources only in this track first, then ones shared with other tracks. Verified sources before preprints.

### A. Data you can use in minute one (no key)

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `alibaba-clusterdata` | [Alibaba cluster traces](https://github.com/alibaba/clusterdata) | open | 3 | Production traces 2017 to 2026, including GPU traces (2020, 2023, 2025, 2026 up to 155k GPUs), LLM serving and spot GPU. Some downloads need a survey; license per release. |
| `azure-llm-inference-traces` | [Azure LLM inference traces 2023, 2024 and multimodal 2025](https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2024.md) | open | 3 | Production request traces: timestamp, context tokens, generated tokens (plus images in the 2025 multimodal trace). No power, location or deadlines. CC BY. |
| `azure-public-dataset` | [Azure Public Dataset](https://github.com/Azure/AzurePublicDataset) | open | 3 | Azure VM, serverless function and LLM inference request traces. The inference traces show request timing and token counts. |
| `cec-dsgs-docket` | [CEC docket 22-RENEW-01 (DSGS data and guidelines)](https://efiling.energy.ca.gov/Lists/DocketLog.aspx?docketnumber=22-RENEW-01) | open | 3 | Includes anonymized 2024 and 2025 storage VPP performance workbooks (monthly site and hourly discharge), enrolled capacity by county. Measured distributed storage, not compute. |
| `eia-861` | [EIA-861 Annual Electric Power Industry Report](https://www.eia.gov/electricity/data/eia861/) | open | 3 | Utility-level sales, customers, revenue, demand response program enrollment and distributed generation by US utility. |
| `google-cluster-data` | [Google cluster workload traces](https://github.com/google/cluster-data) | open | 3 | Borg traces: 2019 (eight cells, May 2019) and 2011 (one ~12,500-machine cell), plus power traces for 57 power domains in May 2019. CC BY. |
| `peeringdb` | [PeeringDB](https://www.peeringdb.com/) | open | 1 | Database of colocation facilities, exchanges and networks with coordinates and a public API (peeringdb.com/apidocs). Facility records include diverse_serving_substations, a declared field, not measured capacity. |
| `starter-us-grid-hourly-2025` | [Starter data: US grid demand and generation, hourly, 2025 (12 operators)](https://github.com/arhamshah08/energy-hack/tree/main/data/grid-hourly-2025) | open | 2, 3 | Ready-to-load CSV: hourly 2025 demand, day-ahead forecast, net generation, interchange and generation by fuel (coal, gas, nuclear, hydro, solar, wind, battery and more) for CAISO, ERCOT, PJM, MISO, NYISO, ISO-NE, SPP, BPA, Duke, Southern, TVA, FPL. Plus an annual summary file. One-line pandas loader in the README. |

### B. Data that needs a key, account or download

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `acn-data` | [ACN-Data: EV charging sessions (Caltech)](https://ev.caltech.edu/dataset) | registration | 3 | Real EV charging sessions from Caltech, JPL and an office site: arrival, departure, energy requested and delivered. API with a free token. |
| `electricity-maps` | [Electricity Maps API](https://app.electricitymaps.com/docs) | api-key (browser only) | 3 | Zone-level carbon intensity, mix, flows, load and day-ahead prices: latest, history and forecast; 5 min to hourly. Lifecycle and flow-traced by default, not marginal. 14-day trial. |
| `epri-dcflex-deliverables` | [EPRI DCFlex deliverables (load shape library and reports)](https://dcflex.epri.com/deliverables) | mixed | 2, 3 | Data center load shape library (first edition 2025), storage assessments, flexible design and program mappings. |
| `gridstatus-io` | [Grid Status (gridstatus.io): live and historical data for all US ISOs](https://www.gridstatus.io/) | mixed (browser only) | 1, 2, 3 | Web dashboards and API with live and historical prices (LMP), demand, forecasts and fuel mix across US ISOs: CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE. Browse in the browser; an account is needed for the API and downloads. Python library: gridstatus. |
| `ripe-atlas` | [RIPE Atlas public measurements (BigQuery)](https://github.com/RIPE-NCC/ripe-atlas-bigquery) | registration | 1 | Ping, traceroute, DNS, HTTP measurements from deployed probes since 2020, queryable in BigQuery (Google account). Measured latency between probes and targets, not arbitrary sites. |
| `watttime` | [WattTime API](https://watttime.org/data-science/data-signals/) | api-key | 3 | Signals: co2_moer (marginal, lb/MWh), co2_aoer (average), health_damage (USD/MWh), with forecasts for load shifting. API docs could not be fetched in research; check access terms. |

### C. Simulators, benchmarks and checks (the verifier in your loop)

| id | Resource | Access | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `citylearn` | [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) | open | simulator |  | Gym environment for coordinated demand response of many buildings with storage and solar. |
| `lfe-cupid` | [CUPID](https://lfenergy.org/projects/cupid/) | open | tool |  | Interoperability toolkit that extends IEEE 2030.5 for distributed energy resources and energy management systems. LF Energy stage: Sandbox. Code: github.com/cupid-project. |
| `qualitylogic-evse-test-system` | [EVSE Test System (QualityLogic)](https://github.com/QualityLogic/evse-test-system) | open | tool |  | Modified EVerest stack for testing EV interoperability over DIN 70121 and ISO 15118-2, AC and DC: 20 conformance scenarios from CharIN and ChargeX specs, web dashboard, REST API, PCAP capture and software-in-the-loop mode without hardware. |
| `acnportal` | [acnportal / ACN-Sim (Caltech)](https://github.com/zach401/acnportal) | open | simulator | 3 | Simulator for scheduling many EV chargers under site capacity limits, plus a client for ACN-Data. BSD-3. |
| `andes` | [ANDES: power system transient dynamics in Python (CURENT)](https://github.com/CURENT/andes) | open | simulator | 2 | Python library for phasor-domain transient stability simulation with symbolic model definitions, including inverter-based resource models. See the repo for license. |
| `carbon-aware-sdk` | [Carbon Aware SDK (Green Software Foundation)](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | open | tool | 3 | Web API and CLI that wrap carbon intensity providers and return the best time and location to run a workload. |
| `lfe-citrineos` | [CitrineOS](https://lfenergy.org/projects/citrineos/) | open | tool | 3 | Open-source charger network management software for OCPP 2.0.1: monitor, control and manage charging stations. Code: github.com/citrineos/citrineos. |
| `flex-pse` | [flex-pse: industrial energy flexibility optimization (Stanford)](https://github.com/flex-pse/flex-pse) | open | tool | 3 | Stanford open-source Pyomo/IDAES toolbox: model a facility as a time-discretized optimization, fit it from plant data, and schedule it against real electricity tariffs and demand response signals. pip install flex-pse. Apache-2.0. Community Slack: https://join.slack.com/t/flex-pse/shared_invite/zt-4b2va6ztg-K74JiAdHsmqY2CoGjbOmIQ |
| `lfe-flexmeasures` | [FlexMeasures](https://lfenergy.org/projects/flexmeasures/) | open | tool | 3 | Open-source energy optimization engine that forecasts and schedules flexible loads, batteries and generation against prices and grid limits, for real-time operations. Built by Seita (https://seita.nl/), founded by Nicolas Höning; hosted by LF Energy. LF Energy stage: Incubation. Code: github.com/FlexMeasures/flexmeasures (Apache-2.0). |
| `gridlab-d` | [GridLAB-D](https://github.com/gridlab-d/gridlab-d) | open | simulator | 2 | Distribution system and end-use load simulator from PNNL, including responsive loads and markets. |
| `helics` | [HELICS co-simulation framework](https://github.com/GMLC-TDC/HELICS) | open | tool | 2, 3 | Couples separate simulators (grid, buildings, markets, comms) into one time-synchronized federation. Python bindings. Simulates nothing on its own. BSD-3. |
| `lfe-hyphae` | [Hyphae](https://lfenergy.org/projects/hyphae/) | open | tool | 3 | Microgrid software connecting buildings, homes and devices to local generation, storage and EV batteries. LF Energy stage: Incubation. Code: github.com/hyphae. |
| `lfe-opendsm` | [OpenDSM (formerly OpenEEmeter)](https://lfenergy.org/projects/opendsm/) | open | tool | 3 | Measures savings and demand-side impact from meter data, for programs that need verified results. Code: github.com/opendsm/opendsm. |
| `lfe-operatorfabric` | [OperatorFabric](https://lfenergy.org/projects/operatorfabric/) | open | tool | 2 | Control-room platform that brings alerts, workflows and messages from many systems into one interface. MPL-2.0. LF Energy stage: Early Adoption. Code: github.com/opfab. |
| `qualitylogic-2030-5-test-tools` | [QualityLogic IEEE 2030.5 test tools](https://www.qualitylogic.com/industries/smart-energy/smart-energy-test-tool-solutions/ieee-2030-5-test-tools/) | paid | tool | 3 | Commercial IEEE 2030.5 and CSIP test system for clients and servers, used as a certification test harness. Not open source. |
| `lfe-seapath` | [SEAPATH](https://lfenergy.org/projects/seapath/) | open | tool | 2 | Real-time platform that runs IEC 61850 substation protection and control as virtual machines or containers on standard servers. LF Energy stage: Graduated. Code: github.com/seapath. |
| `lfe-sogno` | [SOGNO](https://lfenergy.org/projects/sogno/) | open | tool | 2 | Modular, cloud-native automation for distribution utilities: monitoring, state estimation and control. LF Energy stage: Early Adoption. Code: github.com/sogno-platform. |
| `vessim` | [Vessim](https://github.com/dos-group/vessim) | open | simulator | 3 | Co-simulation testbed for computing systems with solar, batteries and grid signals. Built for carbon-aware computing experiments. |

### D. Other tools and APIs

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `everest` | [EVerest: open-source EV charging software stack (LF Energy)](https://github.com/EVerest/EVerest) | open |  | Charger firmware and software stack implementing OCPP and ISO 15118 for EV charging stations. Apache-2.0. |
| `codibly-2030-5-accelerator` | [Codibly IEEE 2030.5 Accelerator](https://codibly.com/accelerators/ieee-2030-5-accelerator) | paid | 3 | Pre-certified IEEE 2030.5 client and server code sold under a perpetual license with source. Codibly is a SunSpec authorized test lab for IEEE 2030.5 and CSIP. Not open source. |
| `coral-npu` | [Coral NPU (Google)](https://github.com/google-coral/coralnpu) | open | 3 | Open machine learning accelerator core designed for energy-efficient AI at the edge. Hardware design, Apache-2.0. |
| `energyhub-derms` | [EnergyHub edge DERMS utility integrations](https://www.energyhub.com/edge-derms-platform/utility-integrations) | paid | 3 | Commercial DERMS integration gateway, including GE Vernova GridOS. No public API or sandbox. |
| `epri-flex-mosaic` | [EPRI Flex MOSAIC](https://dcflex.epri.com/flex-mosaic) | mixed | 3 | Framework classifying data center flexibility by response characteristics across workloads, generation, storage and cooling. |
| `inframation` | [Inframation (inframation.io): map of the energy buildout (FREE BETA)](https://inframation.io/) | open | 1, 2 | Free while in beta, per https://inframation.io/pricing. Searchable map of planned, under-construction, operating and retired power plants, batteries, data centers, large loads, lines and substations in the US and GB, plus energy RFPs and funding, built from interconnection queues, EIA-860M and permit registers with every record linked to its source. Includes a site finder (land near high-voltage lines and substations, out of the floodplain), free RSS/JSON feeds and a keyless public API at https://api.inframation.io. |
| `openleadr` | [OpenLEADR (OpenADR 2.0b in Python)](https://github.com/OpenLEADR/openleadr-python) | open | 3 | LF Energy project with open-source OpenADR implementations: openleadr-python (OpenADR 2.0b VEN and VTN, developmental) and openleadr-rs (Rust, OpenADR 3). Code: github.com/openleadr. |
| `dersec-py1815` | [py1815: open IEEE 1815 (DNP3) outstation](https://github.com/DERSecurity/py1815) | open | 3 | The DNP3 (IEEE 1815) outstation of Project Satori, for distributed energy resources. Companion to the py20305 IEEE 2030.5 client. |
| `pysunspec2` | [pySunSpec2: SunSpec Modbus library](https://github.com/sunspec/pysunspec2) | open | 3 | Python library for reading and controlling SunSpec Modbus devices such as inverters and batteries. Model definitions at github.com/sunspec/models. Used as the Modbus bridge in Project Satori. |
| `open-satori` | [Satori: open IEEE 2030.5 and SunSpec Modbus reference implementations](https://open-satori.org) | open | 3 | IEEE 2030.5 / CSIP client with a SunSpec Modbus bridge that connects inverters, batteries and EVs to utility programs without firmware changes. pip install py20305; code at github.com/DERSecurity/py20305 (Apache-2.0). Satori Scout, the free iOS/Android reference app, handles device discovery, simulation and VPP connectivity (source under commercial license). |
| `gridappsd-2030-5` | [GRIDAPPS-D IEEE 2030.5 repositories](https://github.com/GRIDAPPSD) | open | 3 | Go components for IEEE 2030.5 server, client and inverter simulator. Repository existence only; conformance not checked. |

### E. Papers and reports

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `caiso-dmm-dr-2024` | [CAISO DMM, Demand Response Issues and Performance 2024](https://www.caiso.com/documents/demand-response-issues-and-performance-2024-feb-20-2025.pdf) | verified | report | 3 | DR was about 1,400 MW, 2.6% of CAISO RA capacity in summer 2024; only 44% of utility PDR RA capacity was bid on high-load days. |
| `caiso-dmm-dr-2025` | [CAISO DMM, Demand Response Issues and Performance 2025](https://www.caiso.com/notices/department-of-market-monitoring-demand-response-issues-and-performance-2025-report-posted) | verified | report | 3 | 2025 demand response activity and performance across CAISO and WEIM. |
| `doe-i2x-der-roadmap` | [DOE i2X, DER Interconnection Roadmap (2025)](https://www.energy.gov/sites/default/files/2025-01/i2X%20DER%20Interconnection%20Roadmap.pdf) | verified | report | 2, 3 | Distribution DER interconnection under 100 kV / 80 MW. 2030 targets: under 75 days for 50 kW to 5 MW, under 140 days above 5 MW. Aspirational, not legal deadlines. |
| `doe-grid-codes` | [DOE, Distribution Grid Code Adoption Pathways (2024)](https://www.energy.gov/sites/default/files/2024-07/48726_DOE_OE_TDC_Distribution_Grid_Codes_Pathways_RELEASE_508.pdf) | verified | report | 2 | Taxonomy of grid codes; hosting capacity publication choices and five validation stages. |
| `doe-grid-orchestration` | [DOE, Distribution Grid Orchestration (Nov 2024)](https://www.energy.gov/documents/distribution-grid-orchestration) | verified | report | 2, 3 | Taxonomy of DER orchestration: dispatch-signal, autonomous, behavioral; local feeder constraints vs grid-wide signals; OpenADR and IEEE 2030.5 roles. |
| `doe-microgrids-large-loads` | [DOE, Microgrids, Large Electric Loads and Grid Support](https://www.energy.gov/oe/articles/microgrids-large-electric-loads-grid-support-how-leverage-microgrids-support-utilities) | verified | report | 2, 3 | US data center use rose from 58 TWh (2014) to 176 TWh (2023), 325 to 580 TWh possible by 2028; covers storage, CHP and microgrids for large loads. |
| `doe-sourcing-der` | [DOE, Sourcing DER for Distribution Services (2024)](https://www.energy.gov/sites/default/files/2024-12/Sourcing%20DER%20for%20Dist%20Services%20final%2012.17.24.pdf) | verified | report | 3 | How utilities procure DER for local distribution needs, distinct from wholesale aggregation. |
| `doe-resource-adequacy-2024` | [DOE, The Future of Resource Adequacy (2024)](https://www.energy.gov/sites/default/files/2024-04/2024%20The%20Future%20of%20Resource%20Adequacy%20Report.pdf) | verified | report | 2, 3 | Explains nameplate vs capacity credit: equal MW is not equal reliability. Covers DR, DERMS, ADMS, VPPs. |
| `doe-vpp-announcement-2025` | [DOE, VPP Liftoff update announcement (Jan 2025)](https://www.energy.gov/technologycommercialization/articles/us-department-energy-releases-new-reports-highlighting) | verified | report | 3 | 33 GW of VPPs in North America; 80 to 160 GW by 2030 scenario (10% to 20% of peak). |
| `eia-wholesale-markets` | [EIA, wholesale electricity markets overview](https://www.eia.gov/electricity/wholesalemarkets/) | verified | report | 2 | Map and links for each US ISO/RTO region. |
| `epri-dcflex-programs` | [EPRI DCFlex Workstream 2: Programs](https://dcflex.epri.com/workstream-2) | verified | report | 3 | Maps US and European utility programs and market services to EPRI flexibility classes. |
| `etsi-edge-native-2023` | [ETSI White Paper 55, MEC support towards edge-native design (2023)](https://www.etsi.org/images/files/ETSIWhitePapers/ETSI-WP55-MEC_support_towards_Edge_native.pdf) | verified | report | 1 | Edge constraints: limited single-rack resources, heterogeneity, intermittent upstream links, user mobility, latency. Covers MEC 021 application mobility and MEC 011 discovery APIs. |
| `etsi-mec-security-2022` | [ETSI, Multi-access Edge Computing security white paper (2022)](https://www.etsi.org/newsroom/press-releases/2123-2022-09-etsi-publishes-a-new-white-paper-on-multi-access-edge-computing-security/) | verified | report | 1 | Scope of edge security across federation, physical, data, network and application layers in multi-vendor edge ecosystems. Announcement only; full paper linked. |
| `ferc-energy-primer` | [FERC, Energy Primer (2024 edition)](https://www.ferc.gov/sites/default/files/2024-01/24_Energy-Markets-Primer_0117_DIGITAL_0.pdf) | verified | report | 2, 3 | Staff handbook on electricity and gas markets; RTO/ISO sections for PJM, MISO, CAISO. Vocabulary, not tariff. |
| `google-dr-2023` | [Google Cloud, Using demand response to reduce data center power consumption (2023)](https://cloud.google.com/blog/products/infrastructure/using-demand-response-to-reduce-data-center-power-consumption) | verified | report | 3 | Grid event notices feed Google's compute planner, which sets hourly limits on non-urgent tasks per site (delay or reroute). Europe, Taiwan, US examples. No MW series published. |
| `ca-dr-potential-phase4` | [LBNL / CPUC, California Demand Response Potential Study Phase 4 (2024)](https://eta.lbl.gov/publications/california-demand-response-0) | verified | report | 3 | Shed and shift DR potential in California through 2050 by end use. |
| `lbnl-dc-flex-workshop` | [LBNL / DOE, Data Center Load Flexibility Workshop Summary (2025)](https://eta.lbl.gov/publications/doe-data-center-load-flexibility) | verified | report | 3 | Nov 2024 workshop, 49 participants: workload shifting, storage, onsite generation, demand response, communications and control needs. |
| `lbnl-integrating-ai-dc` | [LBNL, Integrating AI Data Centers with the Power Grid (2026)](https://eta.lbl.gov/publications/integrating-ai-data-centers-power) | verified | paper | 2, 3 | Four flexibility mechanisms: temporal/geographic compute shifting, facility infrastructure flexibility, storage, onsite generation. |
| `pge-redwood-microgrid` | [PG&E EPIC 3.11, Redwood Coast Airport Microgrid final report (2024)](https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.11.pdf) | verified | report | 1, 2, 3 | Measured community microgrid: 2.3 MW / 8.8 MWh battery plus 2.2 MW PV; 51+ hours of resilience across 12 events; fixed limited interconnection avoided reconductoring. |
| `emerald-phoenix-2025` | [Colangelo et al., Turning AI Data Centers into Grid-Interactive Assets (2025)](https://arxiv.org/abs/2507.00909) | preprint | paper | 3 | Field demo in Phoenix: software-only control cut an AI cluster's power by 25% for 3 hours during a grid peak event. |

### F. Programs, rules and standards

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `lfe-cds-registration` | [CDS Registration](https://lfenergy.org/projects/cds-registration/) | verified | standard |  | Open specifications for how third-party systems securely discover, register with and connect to utility platforms. Code: github.com/lfe-cds/CDS-Registration. |
| `ferc-2222` | [FERC Order No. 2222](https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy) | verified | policy |  | Requires RTOs/ISOs to let DER aggregations into energy, capacity and ancillary markets; minimum aggregation size no more than 100 kW. Does not apply to ERCOT. Implementation dates on the page are as of Aug 2024. |
| `lfe-geisa` | [GEISA (Grid Edge Interoperability & Security Alliance)](https://lfenergy.org/projects/geisa/) | verified | standard |  | Secure, interoperable ecosystem for deploying and operating grid edge computing and applications. LF Energy stage: Sandbox. Code: github.com/geisa. |
| `ieee-2030-5` | [IEEE 2030.5-2023 Smart Energy Profile](https://standards.ieee.org/ieee/2030.5/11216/) | verified | standard |  | Application protocol for utility communication with DERs; required for inverter communication under California Rule 21. |
| `lfe-sef` | [Semantic Energy Framework (SEF)](https://lfenergy.org/projects/semantic-energy-framework-sef/) | verified | standard |  | Semantic interoperability so energy apps and devices interpret shared data the same way. LF Energy stage: Sandbox. Code: github.com/lfe-sef. |
| `lfe-shapeshifter` | [Shapeshifter](https://lfenergy.org/projects/shapeshifter/) | verified | standard |  | Implements the USEF Flexibility Trading Protocol for coordinating flexibility between grid operators and aggregators. LF Energy stage: Incubation. Code: github.com/shapeshifter. |
| `caiso-demand-response` | [CAISO Demand Response participation](https://www.caiso.com/generation-transmission/load/demand-response) | verified | program | 3 | Proxy Demand Resource and Reliability DR Resource models. Needs a scheduling coordinator and revenue-quality meters; ancillary services need telemetry. |
| `caiso-der-provider` | [CAISO Distributed Energy Resource Provider model](https://www.caiso.com/generation-transmission/generation/distributed-energy-resources) | verified | program | 3 | DER aggregations in wholesale markets. Utility concurrence review of 30 business days, then onboarding, metering and agreements. |
| `caiso-ddemi-2026` | [CAISO, Demand and Distributed Energy Market Integration straw proposal (Mar 2026)](https://stakeholdercenter.caiso.com/InitiativeDocuments/Straw-Proposal-and-Issue-Paper-Demand-and-Distributed-Energy-Market-Integration-Mar-13-2026.pdf) | verified | filing | 3 | Stakeholder initiative on market pathways for large flexible loads and DER aggregations. |
| `ca-dsgs` | [California Demand Side Grid Support (DSGS) program](https://www.energy.ca.gov/programs-and-topics/programs/demand-side-grid-support-program) | verified | program | 3 | Pays eligible customers for net load reduction and backup generation during extreme events, May to October. Fifth Edition guidelines adopted 27 Apr 2026. |
| `cpuc-transportation-electrification` | [CPUC transportation electrification](https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/infrastructure/transportation-electrification) | verified | program | 3 | California utility EV programs, rates and rulemakings, including vehicle-grid integration. |
| `doe-demand-growth-hub` | [DOE, Electricity Demand Growth Resource Hub](https://www.energy.gov/policy/electricity-demand-growth-resource-hub) | verified | program | 2, 3 | Federal hub of analyses, programs and resources on rapid load growth, including data centers. |
| `doe-ai-datacenter-hub` | [DOE, Powering America's AI Future: Data Center Resource Hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub) | verified | program | 1, 2, 3 | Federal hub on data center demand, flexibility, efficiency, grid integration, water and DOE programs. |
| `epri-dcflex` | [EPRI DCFlex](https://dcflex.epri.com/) | verified | program | 3 | EPRI initiative with utilities, operators and hyperscalers to demonstrate data center flexibility at field sites. |
| `epri-dcflex-demos` | [EPRI DCFlex demonstrations](https://dcflex.epri.com/demonstrations) | verified | program | 2, 3 | At least ten planned demos (Phoenix, Lenoir, Paris, Chicago named): AI workload modulation, DR, backup integration, ride-through. Page does not give curtailment MW. |
| `ercot-ers` | [ERCOT Emergency Response Service (ERS)](https://www.ercot.com/services/programs/load/eils) | verified | program | 3 | Loads, generators and aggregations paid to reduce consumption within 10 or 30 minutes during energy emergencies. Procured four times a year via QSEs. ERCOT is not under FERC Order 2222. |
| `etsi-mec-overview` | [ETSI MEC technical group](https://www.etsi.org/technical-groups/mec/) | verified | standard | 1 | Defines multi-access edge computing as cloud capabilities and an IT service environment at the network edge. |
| `ferc-2222-fact-sheet` | [FERC Order No. 2222 fact sheet](https://www.ferc.gov/media/ferc-order-no-2222-fact-sheet) | verified | policy | 3 | Minimum aggregation size in RTO/ISO markets may be no greater than 100 kW. |
| `ieee-1547` | [IEEE 1547-2018](https://standards.ieee.org/ieee/1547/5915/) | verified | standard | 2 | Interconnection and interoperability standard for DERs connected to distribution grids. |
| `iso-15118-20` | [ISO 15118-20: vehicle to grid communication interface](https://www.iso.org/standard/77845.html) | verified | standard | 3 | Standard for communication between vehicle and charger, adding bidirectional power transfer to plug and charge and scheduling. Paid standard. |
| `miso-large-load-integration` | [MISO, Large Load Additions framework](https://www.misoenergy.org/planning/large-loads---container-page/large-load-additions/) | verified | program | 2, 3 | Requests seek connection in 18 to 36 months. Goal of approval within 120 days. Mechanisms include non-firm service, firm-service step-up, curtailment, telemetry, ride-through. |
| `miso-telemetry-pmu` | [MISO, large load telemetry and PMU requirements](https://www.misoenergy.org/engage/MISO-Dashboard/operational-reliability-requirement---large-load-telemetry-and-phasor-measurement-unit-pmu-requirements/) | verified | standard | 3 | Draft: real-time large load telemetry over ICCP and PMU measurements at the point of interconnection. |
| `miso-lmr-faq` | [MISO, LMR and demand response enrollment FAQ](https://help.misoenergy.org/knowledgebase/article/KA-01560/en-us) | verified | program | 3 | Minimums: LMR 0.1 MW, DRR 1 MW, EDR 0.1 MW. 2 to 6 hour notice, events up to 4 hours, up to 16 dispatches a year. Enrollment tool opens 1 Dec 2026; no API. |
| `ocpp` | [OCPP: Open Charge Point Protocol (Open Charge Alliance)](https://openchargealliance.org/protocols/open-charge-point-protocol/) | verified | standard | 3 | Open protocol between EV chargers and charging management systems, including smart charging profiles that cap or schedule charging power. |
| `openadr` | [OpenADR 3.0](https://www.openadr.org/openadr-3-0) | verified | standard | 3 | REST/OpenAPI standard for DR, price and DER signals; public YAML spec supplements 2.0a/b. Reference implementation is members-only; certification is separate from implementing the API. |
| `lfe-ores` | [ORES: Open Renewable Energy Systems](https://lfenergy.org/projects/ores-open-renewable-energy-systems/) | verified | standard | 3 | Open standards and practice for plug-and-play microgrids and grid-interactive device metadata and APIs. LF Energy stage: Sandbox. Code: github.com/open-renewable-energy-systems. |
| `pge-rule-24` | [PG&E Rule 24 (third-party demand response)](https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/rule-24.html) | verified | program | 3 | Customers enroll with third-party DR providers that bid aggregated reductions into CAISO. |
| `sce-cbp-elect` | [SCE Capacity Bidding Program Elect](https://www.sce.com/save-money/savings-programs/enroll-in-savings-programs/capacity-bidding-program-elect) | verified | program | 3 | Pays participants for temporary reductions during high demand; overlap restrictions with other DR programs. |
| `sce-elrp` | [SCE Emergency Load Reduction Program](https://www.sce.com/factsheet/emergency-load-reduction-program) | verified | program | 3 | Seven-year DR pilot 2021 to 2027 for qualifying non-residential customers, including CCA and Direct Access. |
| `sunspec-specifications` | [SunSpec specifications and certification](https://sunspec.org/specifications/) | verified | standard | 3 | SunSpec Alliance specifications for DER communication (SunSpec Modbus, IEEE 2030.5/CSIP test specs, security). Certification programs and test labs: https://sunspec.org/certifications/. |
| `open-eac-alliance` | [OpenEAC Alliance M&V methodologies](https://github.com/wattcarbon/open-eac-alliance) |  | standard | 3 | Open, peer-reviewed measurement and verification (M&V) methodologies for issuing Energy Attribute Certificates (EACs) per watt-hour or gram CO2e from battery storage, electrification, demand response and energy efficiency projects. Methods and statuses at methods.openeac.org; drafts go through a 30-day public comment period. |

<!-- END GENERATED -->
