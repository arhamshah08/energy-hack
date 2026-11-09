[← Front page](../../README.md) &nbsp;·&nbsp; Tracks: [1 Sites](../1-sites/README.md) · [2 Grid capacity](../2-grid-capacity/README.md) · [3 Load management](../3-load-management/README.md) · [4 Aggregation](../4-aggregation/README.md) · [RFQs](../../guides/rfq/README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Track 1: Identify suitable sites

> Identify suitable sites for edge compute.

Theme link: grid-friendly compute starts with location. See [theme](../../guides/theme/README.md).

## 1. The problem

Hyperscale data centers (1 GW and up) can wait years for power. Large-load requests far outrun
approvals: ERCOT counted 238.6 GW of requests against 7.5 GW approved to energize since 2022
(`ercot-constraints-2025`), and new generation waits a median of more than five years from request
to operation (`lbnl-queued-up`).

**How can we bring power to GPUs in months or weeks instead of years?**

One path is the capacity that already exists across the distribution grid. Many feeders and
substations have spare room for **distributed compute** (`pge-ica`, `sce-drpep`), sized below where
large-load rules begin (25 MW in ERCOT, `ercot-nprr1234`).

Track 1 asks where those sites are. A good site has spare grid capacity nearby, clears land use and
permits, reaches fiber, avoids hazards, has cooling and water options, and sits near the users it
serves. Public data covers each layer separately. Joining them into a list of sites that can get
power fast is the work. More on speed to power: [ideas](../../guides/ideas/README.md).

## 2. Facts that shape this track

| # | Fact | Source id |
|---|---|---|
| 1 | Local land use is changing fast: moratoria (Richmond to 2028, Tulare), Conditional Use Permits (Santa Clara), Special Exception (Loudoun) | `richmond-dc-moratorium`, `santa-clara-zoning`, `loudoun-dc-standards` |
| 2 | Zoning data is fragmented; no national field says "data center allowed" | `national-zoning-atlas` |
| 3 | Broadband maps show provider-reported service, not fiber routes, capacity or latency | `fcc-broadband-map` |
| 4 | Measured latency exists only between probes and targets | `ripe-atlas` |
| 5 | Workload water use varies by more than four orders of magnitude with cooling, climate and grid | `lbnl-water-use-workloads` |
| 6 | Backup generators need air permits; Virginia publishes them | `va-deq-air-permits` |
| 7 | A data center can take 2 to 3 years to build; grid connection often takes longer | `iea-energy-ai-2025` |

## 3. Your loop in this track

| Loop part | Options in the catalog |
|---|---|
| Data layers | `pge-ica` (PG&E GRIP for California, https://grip.pge.com/), `overpass-api`, `openinframap`, `eia-860`, `peeringdb`, `census-reporter-api`, `fema-nri`, `fema-nfhl`, `usgs-water-data`, `open-meteo`, `microsoft-us-building-footprints`, `national-zoning-atlas` |
| Verifier (check a site) | `nrel-reopt` (onsite energy), `pvlib-python` (onsite solar), `nrel-rev` (resource and exclusions), power flow at the nearest substation (Track 2) |
| Metric | Distance to substation and fiber, latency to users, hazard exposure, land and power cost, permit status |
| Proposer | A model or search that suggests candidate locations |

## 4. Outputs that demo well

| # | Format |
|---|---|
| 1 | Map with candidate sites coloured by score, click for the evidence behind the score |
| 2 | Ranked table of sites with each layer's contribution |
| 3 | Chart of score improvement across loop iterations |

## 5. When you need another track

| You need | Go to |
|---|---|
| How much power is actually available at the site | [Track 2](../2-grid-capacity/README.md) |
| Whether the site's load could flex to connect sooner | [Track 3](../3-load-management/README.md) |
| Splitting one large site into several small ones | [Track 4](../4-aggregation/README.md), [Track 2](../2-grid-capacity/README.md) |
| Setup cost of each data source | [guides/reference/data-setup.md](../../guides/reference/data-setup.md) |
| Grid ideas explained | [guides/concepts/](../../guides/concepts/README.md): load flow, grid-forming microgrids, EV charging and V2G |
| Speed to power ideas (permitting layer, vision on permits, AI approval plans) | [ideas](../../guides/ideas/README.md) |

## 6. Resources for this track

<!-- BEGIN GENERATED -->

_Generated from the catalog by `scripts/build.py`. 78 resources tagged with this track._

Order inside each table: resources only in this track first, then ones shared with other tracks. Verified sources before preprints.

### A. Data you can use in minute one (no key)

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `census-reporter-api` | [Census Reporter API](https://censusreporter.org/) | open |  | Simplified access to ACS tables by geography through api.censusreporter.org. No key, unlike the official Census API. |
| `census-tiger` | [Census TIGER/Line shapefiles (2026)](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) | open |  | National boundaries, roads, rails, hydrography; 2026 release 14 Oct 2026. Not parcels or zoning. |
| `cpuc-fire-threat-map` | [CPUC High Fire Threat District map](https://www.cpuc.ca.gov/industries-and-topics/wildfires/fire-threat-maps-and-fire-safety-rulemaking) | open |  | California fire threat tiers (Tier 2 elevated, Tier 3 extreme) used for utility fire safety rules, published as a map and ArcGIS feature service. |
| `esa-worldcover` | [ESA WorldCover](https://esa-worldcover.org/en) | open |  | Global 10 m land cover maps for 2020 and 2021 from Sentinel-1 and Sentinel-2. |
| `fcc-broadband-map` | [FCC National Broadband Map](https://broadbandmap.fcc.gov/) | open (browser only) |  | Provider-reported fixed and mobile broadband availability by location (CSV and GIS). Not fiber routes, capacity or latency. Download page blocks scripts. |
| `fema-nfhl` | [FEMA National Flood Hazard Layer](https://www.fema.gov/flood-maps/national-flood-hazard-layer) | open (browser only) |  | Effective flood maps covering 90%+ of US population, via viewer, downloads and GIS services. Unmapped does not mean no flood risk. |
| `fema-nri` | [FEMA National Risk Index (OpenFEMA)](https://www.fema.gov/about/openfema/data-sets/national-risk-index-data) | open (browser only) |  | v1.20 (Dec 2025): risk for 18 hazards by state, county, tract. Tables, shapefiles, geodatabases, 39 to 411 MB. Old hazards.fema.gov/nri URL redirects. |
| `microsoft-us-building-footprints` | [Microsoft US Building Footprints](https://github.com/microsoft/USBuildingFootprints) | open |  | Building footprint polygons for the US derived from imagery, by state, GeoJSON. ODbL license. |
| `mrlc-nlcd` | [MRLC Annual National Land Cover Database](https://www.mrlc.gov/) | open |  | Annual US land cover, change and imperviousness 1985 to 2025 (Collection 1.2, June 2026). Downloads and WMS. |
| `im3-datacenter-atlas` | [PNNL IM3 Open Source Data Center Atlas](https://im3.pnnl.gov/datacenter-atlas) | open |  | Open geospatial inventory of existing US data center locations compiled by Pacific Northwest National Laboratory. |
| `sf-property-information-map` | [San Francisco Property Information Map](https://sfplanninggis.org/PIM/) | open |  | Parcel reports: zoning, height/bulk, overlays, permits, hazards (flooding, sea-level rise, liquefaction), year built. Not structural or electrical capacity. |
| `usgs-water-data` | [USGS Water Data APIs](https://api.waterdata.usgs.gov/) | open |  | REST/OGC APIs for streamflow, groundwater, daily and continuous values at 1M+ monitoring sites. Not a water right or utility allocation. |
| `va-deq-air-permits` | [Virginia DEQ, issued air permits for data centers](https://www.deq.virginia.gov/news-info/shortcuts/permits/air/issued-air-permits-for-data-centers) | open (browser only) |  | List of air permits for data center backup generation: facility, locality, permit ID, dates. |
| `wri-aqueduct` | [WRI Aqueduct water risk atlas](https://www.wri.org/aqueduct) | open |  | Global water stress and water risk indicators by watershed. Relevant to cooling water availability. |
| `tamu-activsg10k` | [ACTIVSg10k: 10,000-bus synthetic grid, western US](https://electricgrids.engr.tamu.edu/electric-grid-test-cases/activsg10k/) | open | 2 | Synthetic grid on the US WECC footprint, 16 areas. Package includes a MATPOWER case, substation latitude/longitude in the PowerWorld .aux file, and an N-1 branch contingency list. No hourly load time series. Also bundled with MATPOWER as case_ACTIVSg10k. |
| `afdc-stations` | [AFDC alternative fuel station locator (US DOE)](https://afdc.energy.gov/stations) | open | 3 | US public EV charging stations with location, network, connector types and power level. API through the NREL developer network (free key). |
| `eagle-i-outages` | [EAGLE-I recorded electricity outages 2014 to 2022 (ORNL)](https://doi.org/10.6084/m9.figshare.24237376) | open | 2 | Customers without power by US county at 15-minute intervals, 2014 to 2022, from DOE's EAGLE-I system. Live EAGLE-I portal: eagle-i.doe.gov. |
| `eia-state-data` | [EIA state electricity data](https://www.eia.gov/electricity/data/state/index.php) | open | 2 | State-level capacity, generation, sales and related historical series. |
| `eia-860` | [EIA-860 Annual Electric Generator Report](https://www.eia.gov/electricity/data/eia860/) | open | 2 | Generator-level data for US plants of 1 MW and above: location, capacity, technology, status, planned additions and retirements. |
| `epa-egrid` | [EPA eGRID](https://www.epa.gov/egrid) | open | 3 | Emissions and generation mix for US power plants and grid subregions. Annual average emission rates. |
| `epoch-data-centers` | [Epoch AI data on AI data centers](https://epoch.ai/data/data-centers) | open | 2 | Tracked large AI data center projects with estimated power, compute and timelines. Focused on large sites, not edge. |
| `lfe-node-collective` | [NODE Collective](https://lfenergy.org/projects/node-collective/) | open | 3 | National open database of US electrification incentives and rebates. LF Energy stage: Sandbox. Code: github.com/NODE-Collective. |
| `openinframap` | [Open Infrastructure Map](https://openinframap.org/) | open | 2 | Map of OpenStreetMap power lines, substations, power plants and telecom infrastructure. Underlying data via OSM / Overpass. |
| `open-meteo` | [Open-Meteo weather API](https://open-meteo.com/) | open | 3 | Weather forecasts and historical reanalysis by coordinate, hourly, JSON. No key for non-commercial use. |
| `openei-urdb` | [OpenEI Utility Rate Database](https://openei.org/wiki/Utility_Rate_Database) | open | 3 | US retail electricity tariffs including energy charges, demand charges and time-of-use periods. API available. |
| `overpass-api` | [Overpass API (OpenStreetMap queries)](https://wiki.openstreetmap.org/wiki/Overpass_API) | open | 2 | Query OpenStreetMap features by tag and area, e.g. power=substation, power=line with voltage, building footprints. No key; public endpoints are rate-limited. OSM coverage of grid assets is volunteer-mapped and uneven. |
| `peeringdb` | [PeeringDB](https://www.peeringdb.com/) | open | 4 | Database of colocation facilities, exchanges and networks with coordinates and a public API (peeringdb.com/apidocs). Facility records include diverse_serving_substations, a declared field, not measured capacity. |
| `pge-gis-hub` | [PG&E GIS Data Hub](https://pgegishub.pge.com/) | open | 2 | Selected PG&E infrastructure and risk GIS layers as ArcGIS services. |
| `pge-grip-guide` | [PG&E GRIP user guide and quick start (REST endpoint)](https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-quick-start-guide.pdf) | open | 2 | Documents PG&E load ICA: 576 hourly results per line section for four limiting criteria, feeder CSV/ZIP downloads, no-login ArcGIS REST at services2.arcgis.com/mJaJSax0KPHoCNB6/arcgis/rest/services/DRPComplianceRelProd/FeatureServer. Values are directional, not a guarantee. |
| `pudl` | [PUDL (Public Utility Data Liberation), Catalyst Cooperative](https://github.com/catalyst-cooperative/pudl) | open | 2 | Cleaned and linked EIA, FERC and EPA data in SQLite and Parquet. Removes most of the cleanup work of using raw EIA/FERC files. |
| `eia-transmission-lines` | [EIA Energy Atlas, Electric Power Transmission Lines](https://atlas.eia.gov/datasets/geoplatform::electric-power-transmission-lines) | open | 2 | Transmission line GIS layer. Research could not retrieve metadata; an older EIA layer is archived. HIFLD legacy portal returned not-found. Check before relying on it. |

### B. Data that needs a key, account or download

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `era5` | [ERA5 reanalysis (Copernicus)](https://cds.climate.copernicus.eu/) | registration |  | Global hourly weather reanalysis from 1940. Common input for load, wind and solar forecasting. |
| `national-zoning-atlas` | [National Zoning Atlas](https://www.zoningatlas.org/) | mixed |  | Standardized zoning for 11,000+ jurisdictions, 200+ characteristics per district. Data center is not a normalized permitted-use field. |
| `census-acs` | [US Census American Community Survey](https://www.census.gov/data/developers/data-sets/acs-5year.html) | api-key |  | ACS 5-year estimates via API down to block group. All Census API queries now need a free key. |
| `eia-860m` | [EIA-860M monthly generator inventory (API)](https://www.eia.gov/opendata/browser/electricity/operating-generator-capacity/) | api-key | 2 | Monthly generator-level operating status and capacity via EIA API v2. |
| `google-solar-api` | [Google Solar API](https://developers.google.com/maps/documentation/solar/overview) | api-key | 3 | Per-building roof area, panel layouts, sunshine hours and estimated yearly solar output. Needs a Google Cloud project with billing and an API key. |
| `gridstatus-io` | [Grid Status (gridstatus.io): live and historical data for all US ISOs](https://www.gridstatus.io/) | mixed (browser only) | 2, 3, 4 | Web dashboards and API with live and historical prices (LMP), demand, forecasts and fuel mix across US ISOs: CAISO, ERCOT, PJM, MISO, SPP, NYISO, ISO-NE. Browse in the browser; an account is needed for the API and downloads. Python library: gridstatus. |
| `nsrdb` | [National Solar Radiation Database (NSRDB)](https://nsrdb.nlr.gov/) | api-key | 3 | Gridded hourly and sub-hourly solar irradiance and weather. Used to model on-site solar output at a location. |
| `noaa-cdo-api` | [NOAA Climate Data Online API v2](https://www.ncei.noaa.gov/cdo-web/webservices/v2) | api-key | 3 | Station observations and climate normals as JSON. Token header; 5 requests/s, 10,000/day; max 1,000 results per call. |
| `ripe-atlas` | [RIPE Atlas public measurements (BigQuery)](https://github.com/RIPE-NCC/ripe-atlas-bigquery) | registration | 4 | Ping, traceroute, DNS, HTTP measurements from deployed probes since 2020, queryable in BigQuery (Google account). Measured latency between probes and targets, not arbitrary sites. |
| `sdge-ica` | [SDG&E Integration Capacity Analysis](https://marketplace.sdge.com/more-information/customer-generation/enhanced-integration-capacity-analysis-ica) | registration | 2 | Distribution ICA map for SDG&E territory; 2025 update added Limited Generation Profile data. |

### C. Simulators, benchmarks and checks (the verifier in your loop)

| id | Resource | Access | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `nrel-rev` | [reV (Renewable Energy Potential model, NREL, now NLR)](https://github.com/NREL/reV) | open | simulator |  | Geospatial model of renewable generation potential, supply curves and siting exclusions. |
| `lfe-covxtreme` | [covXtreme](https://lfenergy.org/projects/covxtreme/) | open | tool | 2 | Statistical modelling of extreme values and how they occur together, for risk from rare severe conditions. LF Energy stage: Sandbox. Code: github.com/covXtreme. |
| `energyplus` | [EnergyPlus (now under NatLabRockies)](https://github.com/NatLabRockies/EnergyPlus) | open | simulator | 3 | Whole-building energy and HVAC simulation with Python API. Needs facility inputs; not a calibrated data center model out of the box. |
| `evi-x-toolbox` | [EVI-X toolbox (NREL, now NLR)](https://afdc.energy.gov/evi-x-toolbox) | open | tool | 3 | Models for EV charging demand and infrastructure needs (EVI-Pro family), with web versions. |
| `lfe-grid-vantage` | [GridVantage](https://lfenergy.org/projects/grid-vantage/) | open | tool | 2 | Agent-based grid modelling with resilience metrics to help operators prepare for and recover from extreme weather. LF Energy stage: Sandbox. Code: github.com/grid-vantage. |
| `nvidia-omniverse-dsx` | [NVIDIA Omniverse DSX Blueprint: digital twins of AI data centers](https://docs.omniverse.nvidia.com/dsx/latest/overview.html) | mixed | tool | 2, 3 | Developer blueprint for OpenUSD digital twins of gigawatt-scale AI data centers: 50-acre reference site geometry, electrical loading and thermal (CFD) simulation, web viewer. DSX Flex matches facility demand to real-time grid conditions. Needs NVIDIA software and GPUs; NVIDIA says it is not turn-key for production. |
| `pvlib-python` | [pvlib-python](https://github.com/pvlib/pvlib-python) | open | simulator | 3 | Python functions for solar position, irradiance, PV cell temperature and DC/AC output. The standard open PV performance model. BSD-3. |
| `nrel-reopt` | [REopt (NREL, now NLR)](https://github.com/NREL/REopt.jl) | open | simulator | 3 | Optimizes the size and dispatch of on-site solar, storage and generators for a site's load and tariff. Julia package and web API. |
| `nrel-sam` | [System Advisor Model (SAM, NREL, now NLR)](https://sam.nlr.gov/) | open | simulator | 3 | Performance and financial models for solar, wind, storage and other systems. Python access through PySAM. |
| `lfe-varen` | [VAREN](https://lfenergy.org/projects/varen/) | open | tool | 2 | Python library that automates analysis of mobile LiDAR of overhead distribution lines and nearby vegetation. LF Energy stage: Sandbox. Code: github.com/varen-project. |

### D. Other tools and APIs

| id | Resource | Access | Also in track | What it is |
|---|---|---|---|---|
| `google-earth-engine` | [Google Earth Engine](https://earthengine.google.com/) | registration |  | Cloud catalogue and compute for satellite imagery and geospatial datasets (Landsat, Sentinel, NAIP, land cover, ERA5). Free for non-commercial use after registering a Cloud project; Python and JavaScript APIs. |
| `nepa-mcp` | [NEPA MCP Toolkit (PermitAI, PNNL)](https://pnnl.github.io/nepa-mcp/) | mixed |  | 23 Model Context Protocol servers that give AI agents federal environmental data for siting, NEPA review and permitting: permitting schedules, protected areas, species and critical habitat, wetlands, flood hazards, soils, air quality, cultural resources, Tribal lands, demographics, brownfields and federal regulations. pip install nepa-mcp; code at github.com/pnnl/nepa-mcp. Census and EPA AQS servers need free API keys. |
| `inframation` | [Inframation (inframation.io): map of the energy buildout (FREE BETA)](https://inframation.io/) | open | 2, 4 | Free while in beta, per https://inframation.io/pricing. Searchable map of planned, under-construction, operating and retired power plants, batteries, data centers, large loads, lines and substations in the US and GB, plus energy RFPs and funding, built from interconnection queues, EIA-860M and permit registers with every record linked to its source. Includes a site finder (land near high-voltage lines and substations, out of the floodplain), free RSS/JSON feeds and a keyless public API at https://api.inframation.io. |

### E. Papers and reports

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `mobile-edge-market-forecast-2026` | [Commercial mobile edge computing market forecast (press release, 2026)](https://www.globenewswire.com/news-release/2026/11/04/3395444/0/en/Mobile-Edge-Computing-Market-Size-Share-Industry-Trends-and-Growth-Forecasts-2026-2031-5G-Edge-AI-and-Asia-Pacific-Demand-Fuel-30-1-CAGR-to-3-88-Billion.html) | unverified | report |  | Vendor forecast: USD 0.80B (2025) to 3.88B (2031), 30.1% CAGR. Methodology not inspected; measures mobile edge computing, not edge data center buildings or MW. |
| `doe-transmission-needs` | [DOE, National Transmission Needs Study](https://www.energy.gov/oe/national-transmission-needs-study) | verified | report | 2 | Current and future transmission constraints as demand rises; most modeled congestion falls in a small fraction of hours. |
| `epri-powering-intelligence-2024` | [EPRI, Powering Intelligence (2024)](https://www.epri.com/research/products/3002028905) | verified | report | 2 | Scenarios of US data center load growth to 2030 with state-level breakdown. |
| `etsi-edge-native-2023` | [ETSI White Paper 55, MEC support towards edge-native design (2023)](https://www.etsi.org/images/files/ETSIWhitePapers/ETSI-WP55-MEC_support_towards_Edge_native.pdf) | verified | report | 4 | Edge constraints: limited single-rack resources, heterogeneity, intermittent upstream links, user mobility, latency. Covers MEC 021 application mobility and MEC 011 discovery APIs. |
| `etsi-mec-security-2022` | [ETSI, Multi-access Edge Computing security white paper (2022)](https://www.etsi.org/newsroom/press-releases/2123-2022-09-etsi-publishes-a-new-white-paper-on-multi-access-edge-computing-security/) | verified | report | 4 | Scope of edge security across federation, physical, data, network and application layers in multi-vendor edge ecosystems. Announcement only; full paper linked. |
| `iea-energy-ai-2025` | [IEA, Energy and AI (2025)](https://www.iea.org/reports/energy-and-ai) | verified | report | 2 | Global data centers used 415 TWh in 2024 (about 1.5%); 945 TWh in 2030 base case. US and China are nearly 80% of growth. Data centers build in 2 to 3 years, grid infrastructure takes longer. CC BY 4.0. |
| `jrc-eu-coc-2024` | [JRC, 2024 EU Code of Conduct for Data Centres best practice guidelines](https://e3p.jrc.ec.europa.eu/sites/default/files/2024-04/JRC136986_2024_best_practice_guidelines.pdf) | verified | report | 3 | Catalogue of data center practices (cooling, airflow, waste heat, geography, water, monitoring) with 1 to 5 qualitative values that must not be summed. CC BY 4.0. |
| `lbnl-water-use-workloads` | [LBNL, The water use of data center workloads (2025)](https://datacenters.lbl.gov/publications/water-use-data-center-workloads) | verified | paper | 3 | Workload-level water use varies by more than four orders of magnitude with server efficiency, grid water factors, cooling, climate and utilization. |
| `lbnl-dc-energy-2025-update` | [LBNL, United States Data Center Energy Usage Report: 2025 Update](https://datacenters.lbl.gov/publications/united-states-data-center-energy-2025) | verified | report | 2, 3 | Estimates US data center use at 521 to 843 TWh in 2030, 9.5% to 15.3% of US electricity, central estimate 11.8%. |
| `pge-redwood-microgrid` | [PG&E EPIC 3.11, Redwood Coast Airport Microgrid final report (2024)](https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.11.pdf) | verified | report | 2, 3, 4 | Measured community microgrid: 2.3 MW / 8.8 MWh battery plus 2.2 MW PV; 51+ hours of resilience across 12 events; fixed limited interconnection avoided reconductoring. |
| `lbnl-dc-energy-2024` | [Shehabi et al., 2024 United States Data Center Energy Usage Report (LBNL)](https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report) | verified | report | 2 | US data centers used 176 TWh, about 4.4% of US electricity, in 2023; 325 to 580 TWh (6.7% to 12%) projected for 2028. Bottom-up equipment model. Superseded by lbnl-dc-energy-2025-update for 2030. |
| `va-jlarc-2024` | [Virginia JLARC, Data Centers in Virginia (2024)](https://rga.lis.virginia.gov/Published/2025/RD206/PDF) | verified | report | 2 | State investigation: 250+ interviews, independent demand forecast, E3 grid cost modeling. About 50 ongoing jobs vs 1,500 at construction peak for a 250k sq ft site; low-frequency noise; $14 to $37/month added residential cost by 2040 (modeled). |

### F. Programs, rules and standards

| id | Resource | Status | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `richmond-dc-moratorium` | [City of Richmond CA, temporary moratorium on new data centers (CEQAnet)](https://ceqanet.lci.ca.gov/2026101044) | verified | filing |  | Citywide moratorium extended through 15 Sep 2028 while permanent rules are evaluated. |
| `santa-clara-zoning` | [City of Santa Clara, data center zoning framework](https://santaclara.legistar.com/LegislationDetail.aspx?FullText=1&GUID=2791DE9D-56B5-49B5-9998-BC1264149D06&ID=8260886) | verified | filing |  | 2024 zoning code requires standalone data centers to obtain a Conditional Use Permit and architectural review. |
| `santa-clara-planning-record` | [City of Santa Clara, Planning Commission data center record](https://santaclara.legistar.com/LegislationDetail.aspx?FullText=1&GUID=25408312-6834-469E-B545-48CCFFBD1814&ID=7404898) | verified | filing |  | Review of noise, fiscal benefits, power use and concentration of data centers; CUP required in Office/R&D and industrial districts. |
| `loudoun-land-use` | [Loudoun County, Data Centers: Land Use Considerations](https://www.loudoun.gov/6410/Land-Use-Considerations) | verified | filing |  | Rural policy area zoning, about two-thirds of county land, does not allow data centers. |
| `prince-william-dc-review` | [Prince William County, data center overlay district review](https://www.pwcva.gov/department/planning-office/data-center-overlay-district-comprehensive-review) | verified | filing |  | Specified new data center proposals now go through special-use-permit review instead of by-right zoning. |
| `sf-planning-interim-controls` | [San Francisco Planning, code change summaries and interim controls](https://sfplanning.org/fil/planning-code-change-summaries) | verified | filing |  | Index of adopted and interim controls, including an interim zoning moratorium for data centers in San Francisco. |
| `tulare-dc-moratorium` | [Tulare County, temporary moratorium on new data centers (CEQAnet)](https://ceqanet.lci.ca.gov/2026100006) | verified | filing |  | Moratorium extension while the county develops zoning, infrastructure, water, energy, noise and safety standards. |
| `cec-data-centers` | [California Energy Commission, Data Centers](https://www.energy.ca.gov/programs-and-topics/topics/data-centers) | verified | program | 2 | CEC does not generally permit data centers but forecasts their demand. Early 2026 data centers were about 1,000 MW, roughly 2% of CAISO peak. |
| `doe-ai-datacenter-hub` | [DOE, Powering America's AI Future: Data Center Resource Hub](https://www.energy.gov/powering-americas-ai-future-data-center-resource-hub) | verified | program | 2, 3, 4 | Federal hub on data center demand, flexibility, efficiency, grid integration, water and DOE programs. |
| `etsi-mec-overview` | [ETSI MEC technical group](https://www.etsi.org/technical-groups/mec/) | verified | standard | 4 | Defines multi-access edge computing as cloud capabilities and an IT service environment at the network edge. |
| `loudoun-dc-standards` | [Loudoun County, Data Center Standards and Locations](https://www.loudoun.gov/5990/Data-Center-Standards-Locations) | verified | program | 2 | Phase 1 (approved 18 Mar 2025) moved data centers from by-right to Special Exception in affected areas. Phase 2 (plan approved 16 Sep 2025) covers data center and substation standards. Includes existing/proposed data center map. |

<!-- END GENERATED -->
