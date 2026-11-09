[← Front page](../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Open-source tools

Free tools teams can use today, with credit to the people and organisations who built and share
them. Check each tool's license before reusing its code.

**Built one of these tools?** If a description, credit or link is wrong, or you want something added, tell us
through the [feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6) or email arhams@stanford.edu.

<!-- BEGIN GENERATED -->

_121 tools. Generated from the catalog by `scripts/build.py`._

## Try in the browser, no install

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [Load Flow Simulator (browser)](https://tool.adjiebrotots.com/loadflow-simulator/) | Adjie Brotosukmono | Free browser tool: draw a single-line diagram and run AC Newton-Raphson or DC load flow (PyPSA-based), with animated flows. Examples include a 9-bus system, a 20/0.4 kV feeder and an HVDC link. Offers a link for AI agents to open a scenario. | 2 | Free web tool |
| [AC Grid Lab (browser AC power flow)](https://www.eshansingh.xyz/acopf/) | Dr. Eshan Singh | Browser tool: build a one-line network on a map or diagram and solve AC power flow; starter case is a California-inspired nine-bus network with voltage and line-loading checks. JSON import and export. | 2 | Free web tool |
| [ED/UC Simulator: economic dispatch and unit commitment (browser)](https://tool.adjiebrotots.com/ed-uc-simulator/) | Adjie Brotosukmono | Free browser tool: draw a network, decide which units run hour by hour and read nodal prices (LMP); PyPSA with the HiGHS solver. Examples include a PJM 5-bus case and solar plus battery. | 2, 3 | Free web tool |
| [PyPSA California: interactive grid model (browser)](https://www.eshansingh.xyz/PyPSA-CA/app/) | Dr. Eshan Singh | Browser app over a PyPSA optimization model of the California grid: configure demand, generation, storage, transmission and policy, then solve. No install. | 2, 3 | Free web tool |

## Power flow and grid simulation

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
## LF Energy projects (42)

Open-source energy projects hosted by [LF Energy](https://lfenergy.org/projects/), the Linux Foundation's energy foundation. Browse them all at https://lfenergy.org/projects/, for example [AINETUS](https://lfenergy.org/projects/ainetus/) (AI decision support for grid operators).

| Project | Originated by | What it does | Tracks |
|---|---|---|---|
| [AINETUS](https://lfenergy.org/projects/ainetus/) | LF Energy community | AI for Safety-Critical Network Infrastructures: human-centric AI components that support grid operators' real-time and planning decisions. LF Energy stage: Sandbox. Code: github.com/ainetus. | 2 |
| [Arras (formerly HiPAS GridLAB-D)](https://lfenergy.org/projects/arras/) | LF Energy; GridLAB-D originally developed by PNNL for US DOE | Grid and smart-grid simulation for utilities and researchers, the continuation of HiPAS GridLAB-D. LF Energy stage: Sandbox. Code: github.com/arras-energy/gridlabd. | 2, 3 |
| [AssetLife](https://lfenergy.org/projects/assetlife/) | RTE (France) | Python library for asset management: survival analysis, renewal theory and cost calculation for maintenance and replacement decisions. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/AssetLife-project. | 2 |
| [Battery Data Alliance](https://lfenergy.org/projects/battery-data-alliance/) | LF Energy community | Common software and data schemas for battery data across companies. LF Energy stage: Sandbox. Code: github.com/battery-data-alliance. | 3 |
| [CDS Customer Data](https://lfenergy.org/projects/cds-customer-data/) | LF Energy community | Open specifications for access to utility customer energy data, for carbon accounting, efficiency and flexibility use cases. Code: github.com/lfe-cds/CDS-Customer-Data. | 3 |
| [CDS Power Systems Data](https://lfenergy.org/projects/cds-power-systems-data/) | LF Energy community | Open specification for raw power system data, aimed at more accurate grid emissions reporting. Code: github.com/lfe-cds/CDS-Power-Systems-Data. | 2, 3 |
| [CDS Registration](https://lfenergy.org/projects/cds-registration/) | LF Energy community | Open specifications for how third-party systems securely discover, register with and connect to utility platforms. Code: github.com/lfe-cds/CDS-Registration. | 4 |
| [CitrineOS](https://lfenergy.org/projects/citrineos/) | S44 Energy | Open-source charger network management software for OCPP 2.0.1: monitor, control and manage charging stations. Code: github.com/citrineos/citrineos. | 3, 4 |
| [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) | Intelligent Environments Lab (UT Austin), hosted by LF Energy | Gym environment for coordinated demand response of many buildings with storage and solar. | 4 |
| [CoMPAS](https://lfenergy.org/projects/compas/) | LF Energy community | Shared software blocks for IEC 61850 profile configuration in digital substations. LF Energy stage: Early Adoption. Code: github.com/com-pas. | 2 |
| [covXtreme](https://lfenergy.org/projects/covxtreme/) | Shell | Statistical modelling of extreme values and how they occur together, for risk from rare severe conditions. LF Energy stage: Sandbox. Code: github.com/covXtreme. | 1, 2 |
| [CUPID](https://lfenergy.org/projects/cupid/) | LF Energy; from the Horizon Europe InterSTORE project | Interoperability toolkit that extends IEEE 2030.5 for distributed energy resources and energy management systems. LF Energy stage: Sandbox. Code: github.com/cupid-project. | 4 |
| [Dynawo](https://lfenergy.org/projects/dyna%CF%89o/) | LF Energy community | Simulation suite for power system dynamics: voltage, frequency, short circuit and stability with power-electronic resources and HVDC. Code: github.com/dynawo. | 2 |
| [EnerGNN](https://lfenergy.org/projects/energnn/) | RTE with University of Liège and partners | Graph neural network stack (H2MG) for amortized optimization: trained once on many grid cases, it returns near-instant solutions to new ones. LF Energy stage: Sandbox. Code: github.com/energnn/energnn. | 2 |
| [EVerest: open-source EV charging software stack (LF Energy)](https://github.com/EVerest/EVerest) | PIONIX GmbH, hosted by LF Energy | Charger firmware and software stack implementing OCPP and ISO 15118 for EV charging stations. Apache-2.0. | 4 |
| [FIDOpower](https://lfenergy.org/projects/fidopower/) | SLAC National Accelerator Laboratory | Notebook-based tools for reproducible power system analysis. LF Energy stage: Sandbox. Code: github.com/fidopower. | 2 |
| [FlexMeasures](https://lfenergy.org/projects/flexmeasures/) | Seita Energy Flexibility (Nicolas Höning) | Open-source energy optimization engine that forecasts and schedules flexible loads, batteries and generation against prices and grid limits, for real-time operations. Built by Seita (https://seita.nl/), founded by Nicolas Höning; hosted by LF Energy. LF Energy stage: Incubation. Code: github.com/FlexMeasures/flexmeasures (Apache-2.0). | 3, 4 |
| [GEISA (Grid Edge Interoperability & Security Alliance)](https://lfenergy.org/projects/geisa/) | LF Energy community | Secure, interoperable ecosystem for deploying and operating grid edge computing and applications. LF Energy stage: Sandbox. Code: github.com/geisa. | 4 |
| [Grid2Op (RTE France)](https://github.com/Grid2op/grid2op) | RTE France, hosted by LF Energy | Power grid operation environment for RL and agents, used in the L2RPN competitions. Agents act on topology and redispatch. | - |
| [GridVantage](https://lfenergy.org/projects/grid-vantage/) | LF Energy community | Agent-based grid modelling with resilience metrics to help operators prepare for and recover from extreme weather. LF Energy stage: Sandbox. Code: github.com/grid-vantage. | 1, 2 |
| [Hyphae](https://lfenergy.org/projects/hyphae/) | LF Energy community | Microgrid software connecting buildings, homes and devices to local generation, storage and EV batteries. LF Energy stage: Incubation. Code: github.com/hyphae. | 3, 4 |
| [NODE Collective](https://lfenergy.org/projects/node-collective/) | Building Decarbonization Coalition, Rewiring America, Eli Technologies | National open database of US electrification incentives and rebates. LF Energy stage: Sandbox. Code: github.com/NODE-Collective. | 1, 3 |
| [OpenDSM (formerly OpenEEmeter)](https://lfenergy.org/projects/opendsm/) | Recurve | Measures savings and demand-side impact from meter data, for programs that need verified results. Code: github.com/opendsm/opendsm. | 3, 4 |
| [OpenGridFM](https://lfenergy.org/projects/opengridfm/) | LF Energy community | Open framework for building and fine-tuning foundation models for power grids. LF Energy stage: Incubation. Code: github.com/gridfm. | 2 |
| [OpenLEADR (OpenADR 2.0b in Python)](https://github.com/OpenLEADR/openleadr-python) | LF Energy (OpenLEADR) | LF Energy project with open-source OpenADR implementations: openleadr-python (OpenADR 2.0b VEN and VTN, developmental) and openleadr-rs (Rust, OpenADR 3). Code: github.com/openleadr. | 3, 4 |
| [OpenSTEF](https://lfenergy.org/projects/openstef/) | LF Energy community (grid operators, vendors, researchers) | Python machine learning pipelines for short-term energy forecasts. LF Energy stage: Incubation. Code: github.com/OpenSTEF/openstef. | 2, 3 |
| [OpenSynth](https://lfenergy.org/projects/opensynth/) | Centre for Net Zero | Open data community for synthetic and real energy datasets, starting with demand. LF Energy stage: Sandbox. Code: github.com/OpenSynth-energy. | 3 |
| [OperatorFabric](https://lfenergy.org/projects/operatorfabric/) | RTE (France) | Control-room platform that brings alerts, workflows and messages from many systems into one interface. MPL-2.0. LF Energy stage: Early Adoption. Code: github.com/opfab. | 2, 4 |
| [ORES: Open Renewable Energy Systems](https://lfenergy.org/projects/ores-open-renewable-energy-systems/) | LF Energy community | Open standards and practice for plug-and-play microgrids and grid-interactive device metadata and APIs. LF Energy stage: Sandbox. Code: github.com/open-renewable-energy-systems. | 3, 4 |
| [p-SWAMP](https://lfenergy.org/projects/p-swamp/) | LF Energy community | Modular research environment for wide-area monitoring and protection with simulation. LF Energy stage: Sandbox. Code: github.com/p-swamp/P-SWAMP. | 2 |
| [Power Grid Model](https://lfenergy.org/projects/power-grid-model/) | LF Energy community | Fast calculation engine for distribution grids: power flow, state estimation and short circuit. LF Energy stage: Early Adoption. Code: github.com/PowerGridModel. | 2 |
| [PowSyBl](https://lfenergy.org/projects/powsybl/) | RTE (France) | Library and tools for power system modelling: load flow, security analysis, dynamic simulation, many grid formats. MPL-2.0. LF Energy stage: Early Adoption. Code: github.com/powsybl. | 2 |
| [RTC-Tools](https://lfenergy.org/projects/rtc-tools/) | Deltares | Toolbox for control and optimization of time-dependent systems, originally water systems; MESIDO extends it to energy networks. LF Energy stage: Sandbox. Code: github.com/Multi-Energy-Systems-Optimization/mesido. | 3 |
| [RTDIP: Real Time Data Ingestion Platform](https://lfenergy.org/projects/real-time-data-ingestion-platform-rtdip/) | LF Energy community | Cloud pipelines for ingesting and querying real-time and historical time-series data. LF Energy stage: Sandbox. Code: github.com/rtdip. | 3 |
| [SEAPATH](https://lfenergy.org/projects/seapath/) | LF Energy community | Real-time platform that runs IEC 61850 substation protection and control as virtual machines or containers on standard servers. LF Energy stage: Graduated. Code: github.com/seapath. | 2, 4 |
| [Semantic Energy Framework (SEF)](https://lfenergy.org/projects/semantic-energy-framework-sef/) | LF Energy; from the EU InterConnect project | Semantic interoperability so energy apps and devices interpret shared data the same way. LF Energy stage: Sandbox. Code: github.com/lfe-sef. | 4 |
| [Shapeshifter](https://lfenergy.org/projects/shapeshifter/) | LF Energy community | Implements the USEF Flexibility Trading Protocol for coordinating flexibility between grid operators and aggregators. LF Energy stage: Incubation. Code: github.com/shapeshifter. | 4 |
| [Smart HEMS Benchmark](https://lfenergy.org/projects/smart-hems-benchmark/) | LF Energy community | Manufacturer-neutral benchmark for home energy management systems with solar and batteries. LF Energy stage: Sandbox. Code: github.com/SMART-HEMS-Benchmark/smart-hems-benchmark. | 3 |
| [SOGNO](https://lfenergy.org/projects/sogno/) | LF Energy community | Modular, cloud-native automation for distribution utilities: monitoring, state estimation and control. LF Energy stage: Early Adoption. Code: github.com/sogno-platform. | 2, 4 |
| [TROLIE](https://lfenergy.org/projects/trolie/) | LF Energy community | Open specification for exchanging current and forecast transmission line ratings, as required by FERC Order 881. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/trolie/spec. | 2 |
| [Utility Rate Plan Exchange (URPX)](https://lfenergy.org/projects/utility-rate-plan-exchange-urpx/) | Flux Tailor with the National Laboratory of the Rockies | Open, machine-readable standard for utility tariffs and rate plans. Apache-2.0. LF Energy stage: Sandbox. Code: github.com/urpx-org. | 3 |
| [VAREN](https://lfenergy.org/projects/varen/) | LF Energy community | Python library that automates analysis of mobile LiDAR of overhead distribution lines and nearby vegetation. LF Energy stage: Sandbox. Code: github.com/varen-project. | 1, 2 |

| [pandapower](https://github.com/e2nIEE/pandapower) | Fraunhofer IEE and University of Kassel | Python power flow and optimal power flow on pandas tables, with standard test networks. | 2 | See repo |
| [MATPOWER](https://github.com/MATPOWER/matpower) | MATPOWER team (Ray Zimmerman) | MATLAB/Octave power flow and OPF package. Its case format is used by most grid benchmarks. | - | See repo |
| [PowerModels.jl](https://github.com/lanl-ansi/PowerModels.jl) | Los Alamos National Laboratory | Julia package for steady-state power network optimization with many formulations. | - | See repo |
| [OpenDSSDirect.py](https://github.com/dss-extensions/OpenDSSDirect.py) | DSS-Extensions (OpenDSS by EPRI) | Python bindings for OpenDSS distribution system simulator. Used for feeder-level hosting capacity studies. | 2 | See repo |
| [GridLAB-D](https://github.com/gridlab-d/gridlab-d) | PNNL | Distribution system and end-use load simulator from PNNL, including responsive loads and markets. | 2, 4 | See repo |
| [PyPSA](https://github.com/PyPSA/PyPSA) | PyPSA team | Python power system optimization: capacity expansion, unit commitment and power flow. | 2 | MIT |
| [PyPSA-USA](https://github.com/PyPSA/pypsa-usa) | PyPSA-USA contributors | Open US power system model built on PyPSA with EIA and other public data. | 2 | MIT |
| [GridSFM: small foundation models for the power grid (Microsoft Research)](https://github.com/microsoft/GridSFM) | Microsoft Research | Microsoft Research framework for small foundation models in grid optimization, starting with AC optimal power flow. Learns from graph representations of topology, load, dispatch, flows and voltages across many scenarios. Open checkpoint (GridSFM_Open), datasets on Hugging Face, and an open-data pipeline from OpenStreetMap to solved OPF cases. Suited to fast screening (contingencies, planning scenarios, new data center load) and to giving exact solvers a starting point, not replacing them. MIT. | 2 | MIT |
| [ANDES: power system transient dynamics in Python (CURENT)](https://github.com/CURENT/andes) | CURENT (Hantao Cui et al.) | Python library for phasor-domain transient stability simulation with symbolic model definitions, including inverter-based resource models. See the repo for license. | 2, 4 | See repo |
| [Generic EMT Modeling of Data Center Load (Dartmouth)](https://github.com/xingyuz-phd/Generic-EMT-Modeling-of-Data-Center-Load) | Xingyu Zhao, Yingyi Tang, Junbo Zhao (Dartmouth) | Modular electromagnetic transient model of a data center fed by a centralized UPS: rectifier, inverter, battery DC-DC, PFC, buck and VFD modules at three fidelity levels, IT load profiles and voltage ride-through control. Needs PSCAD 5.0.2 (commercial). No license file in the repo; ask the authors before reusing code. | 2, 3 | None stated |
| [OpenIBR: open-source grid-forming controls](https://www.openibr.org/) | Heron Power | Universal grid-forming controller for inverter-based resources and large electronic loads such as data centers, aligned with IEEE 2800 and UNIFI. v1.1 builds IEEE/CIGRE TB958 DLLs from the open C code for PSCAD and similar tools, with debug outputs and a COMTRADE-logging test environment. Code: github.com/HeronPower/OpenIBR; DLL guide: github.com/HeronPower/OpenIBR/blob/dev/documentation/9_using_the_ieee_cigre_dll.md | 2, 3 | Apache-2.0 |
| [HELICS co-simulation framework](https://github.com/GMLC-TDC/HELICS) | US DOE Grid Modernization Lab Consortium (PNNL, LLNL, NREL) | Couples separate simulators (grid, buildings, markets, comms) into one time-synchronized federation. Python bindings. Simulates nothing on its own. BSD-3. | 2, 3, 4 | BSD-3-Clause |
| [Grid2Op (RTE France)](https://github.com/Grid2op/grid2op) | RTE France, hosted by LF Energy | Power grid operation environment for RL and agents, used in the L2RPN competitions. Agents act on topology and redispatch. | - | MPL-2.0 |
| [PGLib-OPF](https://github.com/power-grid-lib/pglib-opf) | IEEE PES Task Force on OPF benchmarks | Standard benchmark library of optimal power flow test cases from 3 to 30,000 buses. | - | See repo |

## Planning, siting and capacity expansion

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [GenX capacity expansion model (MIT, Princeton)](https://github.com/GenXProject/GenX.jl) | MIT and Princeton (GenX team) | Julia model that chooses which generation, storage and transmission to build and how to operate it, for low-carbon power system studies. GPL-2.0. Needs Julia and a solver. | 2 | GPL-2.0 |
| [Manta: open energy system modelling platform](https://manta-plan.org/) | Open Energy Transition | Open-source application for energy system modelling with graphical no-code workflows and full customization; plug-ins for PyPSA, GenX, Sienna and other frameworks; runs in the cloud, locally or on-premise; AI-assisted setup, debugging and results exploration. Code: github.com/manta-plan/manta (Apache-2.0). Launched 2026; public roadmap and beta program. | 2 | Apache-2.0 |
| [REopt (NREL, now NLR)](https://github.com/NREL/REopt.jl) | NREL (now NLR) | Optimizes the size and dispatch of on-site solar, storage and generators for a site's load and tariff. Julia package and web API. | 1, 3 | Apache-2.0 |
| [System Advisor Model (SAM, NREL, now NLR)](https://sam.nlr.gov/) | NREL (now NLR) | Performance and financial models for solar, wind, storage and other systems. Python access through PySAM. | 1, 3 | BSD-3-Clause |
| [reV (Renewable Energy Potential model, NREL, now NLR)](https://github.com/NREL/reV) | NREL (now NLR) | Geospatial model of renewable generation potential, supply curves and siting exclusions. | 1 | BSD-3-Clause |
| [EVI-X toolbox (NREL, now NLR)](https://afdc.energy.gov/evi-x-toolbox) | NREL (now NLR) | Models for EV charging demand and infrastructure needs (EVI-Pro family), with web versions. | 1, 3 | Free web tools |
| [NEPA MCP Toolkit (PermitAI, PNNL)](https://pnnl.github.io/nepa-mcp/) | Pacific Northwest National Laboratory (PNNL) | 23 Model Context Protocol servers that give AI agents federal environmental data for siting, NEPA review and permitting: permitting schedules, protected areas, species and critical habitat, wetlands, flood hazards, soils, air quality, cultural resources, Tribal lands, demographics, brownfields and federal regulations. pip install nepa-mcp; code at github.com/pnnl/nepa-mcp. Census and EPA AQS servers need free API keys. | 1 | BSD-3-Clause |

## Data center and compute energy

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [SustainDC (HPE dc-rl)](https://github.com/HewlettPackard/dc-rl) | Hewlett Packard Enterprise | Multi-agent RL environments for data center workload shifting, HVAC setpoints and batteries with carbon, weather and Alibaba/Google workload inputs. Metrics: energy, carbon, water, dropped tasks. Mixed MIT / CC BY-NC. | 3 | MIT |
| [Vessim](https://github.com/dos-group/vessim) | TU Berlin (DOS group) | Co-simulation testbed for computing systems with solar, batteries and grid signals. Built for carbon-aware computing experiments. | 3, 4 | MIT |
| [Kepler (Kubernetes power exporter)](https://github.com/sustainable-computing-io/kepler) | Sustainable Computing community (CNCF) | Exports estimated power use per Kubernetes pod and container as Prometheus metrics. | 3 | Apache-2.0 |
| [Scaphandre](https://github.com/hubblo-org/scaphandre) | Hubblo | Rust agent reporting host and VM power, exporting to Prometheus, JSON and others. Early-stage. Apache-2.0. | 3 | Apache-2.0 |
| [PowerAPI](https://powerapi.org/) | Inria and University of Lille | Python framework for software-defined power meters down to process level. Estimates, not physical metering. BSD-3. | 3 | BSD-3-Clause |
| [Carbon Aware SDK (Green Software Foundation)](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | Green Software Foundation | Web API and CLI that wrap carbon intensity providers and return the best time and location to run a workload. | 3, 4 | MIT |
| [EnergyPlus (now under NatLabRockies)](https://github.com/NatLabRockies/EnergyPlus) | US DOE, NREL (now NLR) | Whole-building energy and HVAC simulation with Python API. Needs facility inputs; not a calibrated data center model out of the box. | 1, 3 | See repo |
| [Coral NPU (Google)](https://github.com/google-coral/coralnpu) | Google | Open machine learning accelerator core designed for energy-efficient AI at the edge. Hardware design, Apache-2.0. | 3, 4 | Apache-2.0 |

## Load management, storage and flexibility

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [flex-pse: industrial energy flexibility optimization (Stanford)](https://github.com/flex-pse/flex-pse) | Stanford | Stanford open-source Pyomo/IDAES toolbox: model a facility as a time-discretized optimization, fit it from plant data, and schedule it against real electricity tariffs and demand response signals. pip install flex-pse. Apache-2.0. Community Slack: https://join.slack.com/t/flex-pse/shared_invite/zt-4b2va6ztg-K74JiAdHsmqY2CoGjbOmIQ | 3, 4 | Apache-2.0 |
| [NRGISE Open: local energy system simulator](https://github.com/nrgise-open/nrgise-open) | Fraunhofer ISE (Tobias Rohrer, Nils Reiners, Ricarda Hogl) | Python time-step simulation of local energy systems (PV, storage, loads) with control strategies: peak shaving, self-consumption, controller benchmarking, forecast-error studies, batch sweeps. pip install nrgise. CC BY-NC-SA 4.0 (non-commercial). | 3 | CC BY-NC-SA 4.0 |
| [Flexible BESS dispatch and arbitrage optimizer under grid constraints](https://github.com/Mohammadrezarefaei/bess-flexible-dispatch-optimizer) | Mohammadreza Refaei | Optimizes battery charging and discharging across market prices while respecting hourly non-firm grid export limits and degradation cost. Example data from the German market. No clear license in the repo; ask before reusing code. | 3, 2 | None stated |
| [CityLearn](https://github.com/intelligent-environments-lab/CityLearn) | Intelligent Environments Lab (UT Austin), hosted by LF Energy | Gym environment for coordinated demand response of many buildings with storage and solar. | 4 | MIT |
| [NILMTK: Non-Intrusive Load Monitoring Toolkit](https://github.com/nilmtk/nilmtk) | NILMTK community | Toolkit to disaggregate a whole-building meter into appliance loads, with loaders for public datasets including the US REDD dataset. Apache-2.0. | 3 | Apache-2.0 |
| [OpenEAC Alliance M&V methodologies](https://github.com/wattcarbon/open-eac-alliance) | OpenEAC Alliance (repo maintained by WattCarbon) | Open, peer-reviewed measurement and verification (M&V) methodologies for issuing Energy Attribute Certificates (EACs) per watt-hour or gram CO2e from battery storage, electrification, demand response and energy efficiency projects. Methods and statuses at methods.openeac.org; drafts go through a 30-day public comment period. | 3, 4 | Apache-2.0 |

## EV charging and vehicle-to-grid

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [acnportal / ACN-Sim (Caltech)](https://github.com/zach401/acnportal) | Caltech (Zach Lee, Steven Low group) | Simulator for scheduling many EV chargers under site capacity limits, plus a client for ACN-Data. BSD-3. | 3, 4 | BSD-3-Clause |
| [EVerest: open-source EV charging software stack (LF Energy)](https://github.com/EVerest/EVerest) | PIONIX GmbH, hosted by LF Energy | Charger firmware and software stack implementing OCPP and ISO 15118 for EV charging stations. Apache-2.0. | 4 | Apache-2.0 |
| [EVSE Test System (QualityLogic)](https://github.com/QualityLogic/evse-test-system) | QualityLogic | Modified EVerest stack for testing EV interoperability over DIN 70121 and ISO 15118-2, AC and DC: 20 conformance scenarios from CharIN and ChargeX specs, web dashboard, REST API, PCAP capture and software-in-the-loop mode without hardware. | 4 | Apache-2.0 |

## Coordination and grid protocols

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [Satori: open IEEE 2030.5 and SunSpec Modbus reference implementations](https://open-satori.org) | DER Security Corp (DERSec) | IEEE 2030.5 / CSIP client with a SunSpec Modbus bridge that connects inverters, batteries and EVs to utility programs without firmware changes. pip install py20305; code at github.com/DERSecurity/py20305 (Apache-2.0). Satori Scout, the free iOS/Android reference app, handles device discovery, simulation and VPP connectivity (source under commercial license). | 3, 4 | Apache-2.0 |
| [py1815: open IEEE 1815 (DNP3) outstation](https://github.com/DERSecurity/py1815) | DER Security Corp (DERSec), Project Satori | The DNP3 (IEEE 1815) outstation of Project Satori, for distributed energy resources. Companion to the py20305 IEEE 2030.5 client. | 3, 4 | Apache-2.0 |
| [pySunSpec2: SunSpec Modbus library](https://github.com/sunspec/pysunspec2) | SunSpec Alliance | Python library for reading and controlling SunSpec Modbus devices such as inverters and batteries. Model definitions at github.com/sunspec/models. Used as the Modbus bridge in Project Satori. | 3, 4 | Apache-2.0 |
| [SunSpec System Validation Platform (OpenSVP)](https://github.com/sunspec/svp) | SunSpec Alliance with CanmetENERGY-Varennes | Open-source Python test platform and scripts for DER conformance testing against IEEE 1547.1, UL 1741 SA and AS/NZS 4777.2 with lab equipment or simulation. | 3 | Apache-2.0 |
| [OpenLEADR (OpenADR 2.0b in Python)](https://github.com/OpenLEADR/openleadr-python) | LF Energy (OpenLEADR) | LF Energy project with open-source OpenADR implementations: openleadr-python (OpenADR 2.0b VEN and VTN, developmental) and openleadr-rs (Rust, OpenADR 3). Code: github.com/openleadr. | 3, 4 | Apache-2.0 |
| [GRIDAPPS-D IEEE 2030.5 repositories](https://github.com/GRIDAPPSD) | PNNL (GridAPPS-D) | Go components for IEEE 2030.5 server, client and inverter simulator. Repository existence only; conformance not checked. | 3, 4 | See repos |

## Forecasting

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [surge: open probabilistic day-ahead US load forecasts](https://github.com/tylergibbs1/surge) | Tyler Gibbs | Day-ahead probabilistic load forecasts for all 53 US balancing authorities: Chronos-2 fine-tuned on seven years of EIA-930 data. MIT. | 2, 3 | MIT |
| [TimeCopilot: agentic forecasting framework](https://github.com/TimeCopilot/timecopilot) | TimeCopilot | LLM agent over time-series foundation models: forecast, cross-validate and detect anomalies from natural-language requests through one API. MIT. | 2, 3 | MIT |
| [pvlib-python](https://github.com/pvlib/pvlib-python) | pvlib community (Sandia origin) | Python functions for solar position, irradiance, PV cell temperature and DC/AC output. The standard open PV performance model. BSD-3. | 1, 3 | BSD-3-Clause |
| [Solar-Forecasting: physics-based smart persistence model (NREL, now NLR)](https://github.com/NatLabRockies/Solar-Forecasting) | NREL (now NLR) | NREL software record SWR-18-36: physics-based smart persistence model for intra-hour solar forecasting. BSD-3. Last updated 2022. | 3 | BSD-3-Clause |
| [BuildingsBench (NREL, now NLR)](https://github.com/NREL/BuildingsBench) | NREL (now NLR) | Benchmark and 900k simulated buildings for short-term load forecasting, including zero-shot tests on real buildings. | - | BSD-3-Clause |

## Data access

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [gridstatus (Python library)](https://github.com/gridstatus/gridstatus) | Grid Status | Python API for load, prices, fuel mix and queue data from US ISOs (CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE). | 2, 3 | BSD-3-Clause |
| [Inframation (inframation.io): map of the energy buildout (FREE BETA)](https://inframation.io/) | Compass International | Free while in beta, per https://inframation.io/pricing. Searchable map of planned, under-construction, operating and retired power plants, batteries, data centers, large loads, lines and substations in the US and GB, plus energy RFPs and funding, built from interconnection queues, EIA-860M and permit registers with every record linked to its source. Includes a site finder (land near high-voltage lines and substations, out of the floodplain), free RSS/JSON feeds and a keyless public API at https://api.inframation.io. | 1, 2, 4 | Free beta, not open source; no site license yet, each record carries its source's license |
| [Overpass API (OpenStreetMap queries)](https://wiki.openstreetmap.org/wiki/Overpass_API) | OpenStreetMap community (Roland Olbricht) | Query OpenStreetMap features by tag and area, e.g. power=substation, power=line with voltage, building footprints. No key; public endpoints are rate-limited. OSM coverage of grid assets is volunteer-mapped and uneven. | 1, 2 | AGPL-3.0 |
| [Census Reporter API](https://censusreporter.org/) | Census Reporter | Simplified access to ACS tables by geography through api.censusreporter.org. No key, unlike the official Census API. | 1 | Free API |
| [Open-Meteo weather API](https://open-meteo.com/) | Open-Meteo (Patrick Zippenfenig) | Weather forecasts and historical reanalysis by coordinate, hourly, JSON. No key for non-commercial use. | 1, 3 | AGPL-3.0 |

## RSI and agent loops

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [AIDE (Weco AI)](https://github.com/WecoAI/aideml) | Weco AI | Agent that iterates on ML code with a tree search over solutions, scored by a user-defined metric. | - | MIT |
| [autoresearch (Andrej Karpathy)](https://github.com/karpathy/autoresearch) | Andrej Karpathy | Minimal loop where an agent edits a training script, runs a short experiment, and keeps changes that improve a validation metric. | - | See repo |
| [OpenEvolve](https://github.com/codelion/openevolve) | Asankhaya Sharma | Open-source implementation of the AlphaEvolve pattern: an LLM mutates programs and an evaluator scores them across generations. | - | Apache-2.0 |
| [ShinkaEvolve (Sakana AI)](https://github.com/SakanaAI/ShinkaEvolve) | Sakana AI | Sample-efficient LLM-driven program evolution framework with novelty filtering and an archive of solutions. | - | Apache-2.0 |
| [Darwin Godel Machine](https://github.com/jennyzzt/dgm) | Jenny Zhang et al. (UBC, Sakana AI) | Coding agent that edits its own code and keeps an archive of agent variants, scored on coding benchmarks. | - | Apache-2.0 |
| [FunSearch (Google DeepMind)](https://github.com/google-deepmind/funsearch) | Google DeepMind | LLM proposes programs, an automated evaluator scores them, best programs are fed back. Released code for the Nature 2023 paper. | - | Apache-2.0 |
| [DSPy](https://github.com/stanfordnlp/dspy) | Stanford NLP | Framework that optimizes LLM prompts and pipelines against a metric instead of hand-written prompts. | - | MIT |
| [GEPA](https://github.com/gepa-ai/gepa) | Lakshya A. Agrawal et al. | Reflective prompt evolution: an LLM reads execution traces and rewrites prompts, keeping a Pareto set of candidates. | - | MIT |
| [The AI Scientist (Sakana AI)](https://github.com/SakanaAI/AI-Scientist) | Sakana AI | End-to-end loop that generates research ideas, runs experiments from templates and writes papers. | - | See repo |
| [MLE-bench (OpenAI)](https://github.com/openai/mle-bench) | OpenAI | 75 Kaggle competitions used to measure how well agents do ML engineering. | - | See repo |

## Materials (reference)

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [pymatgen](https://github.com/materialsproject/pymatgen) | Materials Project (LBNL) | Python library for crystal structures, phase diagrams, electrochemistry analysis and Materials Project access. | - | See repo |
| [Atomic Simulation Environment (ASE)](https://gitlab.com/ase/ase) | ASE community (DTU) | Python toolkit to set up, run and analyze atomistic simulations with many calculators, including ML potentials. | - | LGPL-2.1 |
| [MACE](https://github.com/ACEsuit/mace) | ACEsuit (University of Cambridge and others) | Machine-learned interatomic potentials, including foundation models (MACE-MP) that run near-DFT checks in seconds. | - | See repo |
| [CHGNet](https://github.com/CederGroupHub/chgnet) | Ceder Group (UC Berkeley) | Universal ML potential trained on Materials Project trajectories, includes magnetic moments. Runs on CPU or GPU. | - | See repo |
| [MatterSim (Microsoft)](https://github.com/microsoft/mattersim) | Microsoft Research | Universal ML potential for materials across elements, temperatures and pressures. | - | MIT |
| [Orb models (Orbital Materials)](https://github.com/orbital-materials/orb-models) | Orbital Materials | Pretrained universal ML interatomic potentials with ASE calculator interface. | - | Apache-2.0 |
| [fairchem (Meta FAIR Chemistry)](https://github.com/facebookresearch/fairchem) | Meta FAIR Chemistry | Models and tooling for Open Catalyst and OMat datasets, including pretrained potentials for catalysts and materials. | - | See repo |
| [MatterGen (Microsoft)](https://github.com/microsoft/mattergen) | Microsoft Research | Diffusion model that generates crystal structures conditioned on target properties. | - | MIT |
| [Matbench Discovery](https://matbench-discovery.materialsproject.org/) | Materials Project (LBNL) | Leaderboard ranking ML models on predicting stability of new crystals. | - | MIT |
| [PyBaMM](https://github.com/pybamm-team/PyBaMM) | PyBaMM team (University of Oxford and others) | Python battery models (SPM, SPMe, DFN) with degradation submodels and parameter sets. Simulates a cycling protocol in seconds. | - | BSD-3-Clause |

## Fusion (reference)

| Tool | Built by | What it does | Tracks | License |
|---|---|---|---|---|
| [TORAX (Google DeepMind)](https://github.com/google-deepmind/torax) | Google DeepMind | Differentiable tokamak core transport simulator in JAX. Fast enough to run inside optimization loops. | - | See repo |
| [FreeGS](https://github.com/freegs-plasma/freegs) | FreeGS contributors (Ben Dudson) | Free-boundary Grad-Shafranov plasma equilibrium solver in Python. | - | LGPL-3.0 |
| [FreeGSNKE](https://github.com/FusionComputingLab/freegsnke) | FusionComputingLab (UKAEA, STFC Hartree Centre) | Evolutive free-boundary equilibrium solver built on FreeGS, for time-dependent tokamak simulation. | - | LGPL-3.0 |
| [Open FUSION Toolkit](https://github.com/OpenFUSIONToolkit/OpenFUSIONToolkit) | Open FUSION Toolkit team | Finite element codes for plasma equilibrium (TokaMaker), MHD and 3D wall eddy currents. | - | LGPL-3.0 |
| [PlasmaPy](https://github.com/PlasmaPy/PlasmaPy) | PlasmaPy community | Community Python package for plasma physics formulary and analysis. | - | BSD-3-Clause |


<!-- END GENERATED -->
