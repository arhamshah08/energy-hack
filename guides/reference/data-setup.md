[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Data facts and setup cost (all tracks)

Facts about public siting data that affect what can be built in a day. Each row cites a catalog id.

## 1. Facts about the data

| # | Fact | Source id |
|---|---|---|
| 1 | Detailed real grid models are restricted as Critical Energy/Electric Infrastructure Information; access needs a request and NDA | `ferc-ceii` |
| 2 | Public studies therefore use synthetic grids: realistic structure and similar load and generation, but no relation to the actual network at that location | `tamu-synthetic-grids` |
| 3 | The western US synthetic grid ships with substation coordinates, so a region can be cut out by a latitude/longitude box | `tamu-activsg10k` |
| 4 | The same package includes an N-1 branch contingency list but no hourly load series | `tamu-activsg10k` |
| 5 | The Texas synthetic grid includes a year of hourly load scenarios | `tamu-activsg2000` |
| 6 | Hourly load shapes for real regions come from balancing authority and ISO data | `eia-930`, `caiso-oasis`, `pjm-dataminer`, `gridstatus` |
| 7 | Utility hosting capacity maps are screening estimates under stated assumptions, not commitments | `pge-ica`, `pge-grip-guide`, `sce-drpep` |
| 8 | Hosting capacity maps cover distribution feeders; transmission constraints sit in ISO studies | `caiso-lcr-2027`, `ercot-constraints-2025` |
| 9 | Power flow answers whether the network physically carries a load (thermal and voltage limits); production cost models optimize dispatch and assume deliverability; capacity expansion models choose what to build | `pandapower`, `matpower`, `pypsa` |
| 10 | Reliability is usually measured across a full year (for example loss of load expectation), and equal MW does not give equal reliability | `doe-resource-adequacy-2024` |
| 11 | Measured data center load data is scarce in public; available proxies are load shape libraries, cluster power traces and simulated building loads | `epri-dcflex-deliverables`, `google-cluster-data`, `comstock` |
| 12 | OpenStreetMap power infrastructure is volunteer-mapped and uneven by region | `overpass-api`, `openinframap` |
| 13 | Large loads can trip offline together during grid faults; operators now ask for ride-through data | `pjm-load-transfer-event-2026`, `ercot-ride-through-notice` |

## 2. No key needed

| # | Resource | Gives you | Id |
|---|---|---|---|
| 1 | Synthetic grids + MATPOWER / pandapower | Network to run power flow on | `tamu-activsg10k`, `matpower`, `pandapower` |
| 2 | Overpass API | Substations, lines, buildings from OSM | `overpass-api` |
| 3 | Census Reporter API | Population, income, housing by geography | `census-reporter-api` |
| 4 | Open-Meteo | Hourly weather by coordinate | `open-meteo` |
| 5 | EIA-930 bulk files | Hourly demand and generation by balancing authority | `eia-930` |
| 6 | CAISO OASIS / Today's Outlook | California prices, load, supply | `caiso-oasis`, `caiso-todays-outlook` |
| 6b | Grid Status website (browsing) | Prices, demand, fuel mix for every US ISO; API needs an account | `gridstatus-io` |
| 7 | PG&E GRIP (https://grip.pge.com/), SCE ICA FeatureServer | Feeder hosting capacity (California) | `pge-ica`, `pge-grip-guide`, `sce-ica-featureserver` |
| 8 | FEMA flood and risk data | Hazard exposure | `fema-nfhl`, `fema-nri` |
| 9 | Building footprints | Footprint polygons | `microsoft-us-building-footprints` |
| 10 | EAGLE-I outage history | County outages at 15-minute resolution | `eagle-i-outages` |
| 11 | Workload traces | Compute demand patterns | `google-cluster-data`, `azure-llm-inference-traces` |
| 12 | CPUC fire threat districts | Wildfire tiers (California) | `cpuc-fire-threat-map` |

`python3 scripts/find.py --track 1 --access open` lists all open resources for a track.

## 3. Needs a key, account or billing

| # | Resource | Setup | Id |
|---|---|---|---|
| 1 | EIA API v2 | Free key by email | `eia-api-v2` |
| 2 | Official Census API | Free key | `census-acs` |
| 3 | NOAA CDO | Free token, 10,000 requests/day | `noaa-cdo-api` |
| 4 | PJM Data Miner API | Free account | `pjm-dataminer` |
| 5 | Materials Project, NSRDB | Free key | `materials-project`, `nsrdb` |
| 6 | Electricity Maps, WattTime | Account; free tiers or trials with limits | `electricity-maps`, `watttime` |
| 7 | Google Earth Engine | Register a Cloud project (free non-commercial) | `google-earth-engine` |
| 8 | Google Solar API | Cloud project with billing and API key | `google-solar-api` |
| 9 | ERA5 | Copernicus account; download queue | `era5` |
| 10 | RIPE Atlas on BigQuery | Google account and project | `ripe-atlas` |
