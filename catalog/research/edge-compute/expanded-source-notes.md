# Edge Compute Management — Expanded Source Research Handoff

## Purpose and receiving-agent context

This standalone document packages the expanded research supplied in the preceding research response. It is intended for an agent that will not have the conversation. It contains the 67 master-source records, retains their original IDs, and includes 20 additional supporting-source records. It preserves factual qualifications, corrections, retrieval failures, and distinctions between simulation, operator reports, measured deployments, proposals, and effective rules.

Research context: a one-day energy hack in San Francisco on 8 November 2026, at AGI House SF with MIT Sundai Club and Stanford Energy Club; teams have about five hours. The research feeds a neutral public GitHub repository. Sources and facts only: no project suggestions, product ideas, rankings, or recommended build approaches.

Research cutoff: 7 November 2026. This document reformats the prior research; creating the document did not constitute a new website verification pass.

## Categories and themes

- C1 — Site identification: land, zoning, permits, fiber, latency, water, cooling, proximity to users, existing-building reuse, community acceptance.
- C2 — Grid capacity assessment for siting: hosting-capacity maps, feeder/substation headroom, queues, wait times, large-load rules, load forecasts.
- C3 — Load management: demand response, temporal/geographic shifting, carbon/price scheduling, batteries, generation, capping, cooling, deployments.
- C4 — Aggregation of distributed compute: VPPs, DER aggregation, wholesale participation, grid services, communications and controls.
- T1 — Growth, market context, drivers, electricity demand.
- T2 — Siting and interconnection constraints.
- T3 — Public datasets and data services.
- T4 — Flexibility and DERMS terminology.
- T5 — Tools, APIs, simulators, standards.
- T6 — Programs, tariffs, market pathways, initiatives.

## Verification conventions

“Opened” means readable page or repository text was retrieved, not that every linked document was inspected, data files downloaded, software executed, API credentials tested, or physical controls exercised. Several long PDFs were only partially exposed by text extraction. A statement described as “not established” is a research limitation, not proof that the capability or data does not exist. Public access does not establish redistribution permission. A source's forecast, proposal, or marketing claim is not an observed operating result. Historical, foundational material is retained where explicitly identified.

URLs are the portable source references. Conversation-specific citation markers are omitted because another agent cannot resolve those identifiers independently; source IDs and direct URLs are preserved.

## Corrections and material additions to the earlier catalogue

- R02: IEA explicitly licenses Energy and AI under CC BY 4.0; generic “publisher terms” was unnecessarily vague. Source: https://www.iea.org/reports/energy-and-ai
- R03: The IEA parent report is identified as published 16 April 2026. Its executive summary contains 485 TWh for 2025 and approximately 950 TWh for 2030. Sources: https://www.iea.org/reports/energy-and-ai ; https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
- R05: JRC permits reuse under CC BY 4.0 except separately owned material. Practice-value scores are qualitative and must not be summed into an operator score. Source: https://e3p.jrc.ec.europa.eu/sites/default/files/2024-04/JRC136986_2024_best_practice_guidelines.pdf
- D05: PG&E documents a no-login REST endpoint, feeder-organized ZIP/CSV downloads, and 576 hourly results per line section for each of four limiting criteria. Source: https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-quick-start-guide.pdf
- D06: The general queue landing page exposed only a shell. The specific 2026 edition is accessible and supplies an XLSX, codebook, 36 summary tabs, and explicit CC BY 4.0 licensing. Source: https://emp.lbl.gov/publications/queued-2026-edition-characteristics
- D23: Google's repository licenses data and trace documentation CC BY and includes power traces for 57 power domains, not only workload/resource-utilization traces. Sources: https://github.com/google/cluster-data ; https://github.com/google/cluster-data/blob/master/PowerData2019.md
- N01: FERC's implementation-date discussion is an August 2024 snapshot, not evidence those dates were achieved by November 2026. The page states an update date of 23 January 2025, not the search-index date previously shown. Source: https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy
- N04: The retrieved document is dated November 2024; replace “undated landing page” with that document date. Source: https://www.energy.gov/documents/distribution-grid-orchestration
- S08: The original NREL GitHub URL redirects to NatLabRockies/EnergyPlus. Source: https://github.com/NREL/EnergyPlus
- S12: WattTime's documentation endpoint failed twice. Its official data-signals page was readable; endpoint schemas and current subscription entitlements remain unverified. Source: https://watttime.org/data-science/data-signals/

# 1. Reports and analytical evidence

## R01 — LBNL: 2024 United States Data Center Energy Usage Report

URL: https://eta.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report
Detailed PDF: https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf
Tags: C1; C2; C3 | T1; T2.
Status: landing page and substantial PDF text opened; later sections not exhaustively extracted.

The report uses a bottom-up equipment-stock model: shipments and retirement/age assumptions determine installed servers, storage, and networking equipment; equipment-specific operational wattage produces IT electricity demand; modeled PUE and WUE convert this into site electricity and water requirements. Scenarios vary GPU shipments, operational practices, and cooling systems. Estimated US consumption reaches 176 TWh in 2023, versus approximately 60 TWh in 2014–2016; the 2028 range is 325–580 TWh. Its 74–132 GW figure explicitly assumes 50% average capacity utilization and is not annual-average power. Detailed navigation: methodology p.14; server types/power p.16; infrastructure classification p.35; infrastructure electricity/water modeling p.39; total estimates p.49; limitations p.67. Cryptocurrency is analyzed separately in Chapter 6. The authors explicitly identify limited direct-energy disclosures and proprietary market inputs as constraints; this is not a parcel inventory, edge-only forecast, or utility connection-availability dataset.

## R02 — IEA: Energy and AI

URL: https://www.iea.org/reports/energy-and-ai
Detailed demand chapter: https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai
Tags: C1; C2; C3 | T1; T2.
Status: landing page and demand chapter opened. Published: 10 April 2025. License: CC BY 4.0.

The demand chapter estimates 415 TWh of global data-center electricity use in 2024, approximately 1.5% of global electricity, and a Base Case of 945 TWh in 2030. It explicitly distinguishes Base, Lift-Off, High Efficiency, and Headwinds cases. Estimated equipment shares: servers around 60%; storage around 5%; networking up to 5%; cooling approximately 7% in efficient hyperscale facilities to over 30% in less-efficient enterprise facilities. Accelerated-server electricity demand grows approximately 30% annually in its Base Case, versus 9% for conventional servers. US and Chinese growth together account for nearly 80% of projected global growth through 2030. The source connects siting problems to geographic concentration and mismatched construction timelines: data centers can develop in two to three years, while electricity infrastructure generally takes longer. It provides global/regional scenario context, not edge-only demand, real-time capacity maps, or facility-level measurements.

## R03 — IEA: Key Questions on Energy and AI

URL: https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary
Tags: C2; C3 | T1; T2.
Status: executive summary opened; parent report identified as 16 April 2026. License: CC BY 4.0.

The update estimates total data-center electricity demand grew 17% in 2025, with AI-focused facilities growing 50%; its central trajectory increases from 485 TWh in 2025 to approximately 950 TWh in 2030. It distinguishes efficiency per AI task from total system demand: cheaper/simple queries coexist with more energy-intensive reasoning, video, and agentic uses. Physical constraints include high-bandwidth memory, transformers, power electronics, power density, heat evacuation, structural weight, financing, permitting, and community acceptance. It projects 20–25 GW of battery storage power capacity at data centers by 2030 and 15–27 GW of onsite gas generation, mostly US. Its analysis says reliable onsite gas supply can require generation overbuild of 30–70% relative to demand. These are IEA estimates/scenarios, not committed equipment orders, dispatchable VPP capacity, or evidence that onsite generation bypasses permitting and supply constraints.

## R04 — Virginia JLARC: Data Centers in Virginia

URL: https://rga.lis.virginia.gov/Published/2025/RD206/PDF
Tags: C1; C2 | T1; T2.
Status: substantial PDF text opened, including summary, methods, recommendations, contents; not every later table independently extracted. Report 598; 9 December 2024.

The investigation involved over 250 interviews with more than 150 stakeholders, water/emissions/tax-data analysis, local land-use case reviews, an independent demand forecast, and E3 grid/cost modeling. It separates current cost-of-service allocation from future system-cost increases and stranded-infrastructure risk. It finds data-center economics are concentrated in construction: a representative 250,000-square-foot facility may employ approximately 50 ongoing workers versus approximately 1,500 workers at peak construction. Residential impacts include continuous low-frequency noise that may not violate conventional short-duration noise ordinances. Water requirements vary greatly by computing density and cooling technology; regional water abundance does not eliminate locality-specific supply limitations. Its summary projects a typical Dominion residential customer could face $14–$37/month of additional generation/transmission costs by 2040 in constant dollars under modeled conditions. Chapters: energy p.25; energy costs p.43; natural/historic resources p.57; residential impacts p.73; local zoning appendix p.135. Legislative recommendations are proposals, not enacted requirements.

## R05 — JRC: 2024 EU Code of Conduct Best Practice Guidelines

URL: https://e3p.jrc.ec.europa.eu/sites/default/files/2024-04/JRC136986_2024_best_practice_guidelines.pdf
Tags: C1; C3 | T2; T5.
Status: substantial PDF text opened; later cooling/building chapters identified through contents. License: CC BY 4.0 except third-party material.

This is a structured practice catalogue, not a savings calculator. Each practice has a name, description, applicability/“expected” classification, and qualitative value from 1–5. The document explicitly prohibits treating those values as additive quantitative scores. Applicability distinguishes entire facilities, new software, new IT equipment, and new build/retrofit. Responsibility matrices separate operators, colocation providers, colocation customers, and managed-service providers; a tenant may lack control over cooling or electrical infrastructure. Specific early practices address embodied impact, ISO 50001 energy management, asset inventories, accurate single-line/as-built records, workload migration, smart-grid support, overprovisioning, and resilience levels. It warns power delivered outside the data center through IT cabling can distort PUE accounting. Detailed sections: airflow p.33; temperature/humidity p.39; economized cooling p.42; liquid cooling p.50; waste heat p.51; geography p.57; water p.58; monitoring p.59. No universal facility-level energy-savings percentage is established.

## R06 — Duke: Rethinking Load Growth

URL: https://nicholasinstitute.duke.edu/publications/rethinking-load-growth
Persistent identifier: https://hdl.handle.net/10161/32077
Tags: C2; C3 | T1; T2.
Status: publication landing-page narrative opened; underlying full model and appendices not opened.

The page describes a national first-order assessment across the 22 largest US balancing authorities, collectively serving approximately 95% of the grid. Its central concept is “curtailment-enabled headroom”: additional large demand accommodated using existing capacity when limited reductions are permitted during grid stress. Mechanisms named are workload shifting, onsite generation, and operational adjustment. The landing-page finding is nearly 100 GW of potential flexible new load. It links a webinar, slides, takeaways, Congressional testimony, and a later policy brief on DOE's proposed large-load interconnection process. The retrieved text does not provide the exact curtailment-frequency table, hourly modeling code, distribution-level bottlenecks, feeder maps, or parcel approvals. Consequently, exact claims such as “98.1 GW at 0.5% curtailment” are not independently established by this page inspection; the verified landing-page claim is “nearly 100 GW,” explicitly first-order and system-level.

## R07 — PJM: 2025 Long-Term Load Forecast

URL: https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2025-load-report.ashx
Tags: C2 | T1; T2.
Status: substantial PDF opened. Posted: 24 January 2025.

The report covers 20-year peak load, net energy, load management, distributed solar, EVs, and batteries by zone, region, locational deliverability area, and total RTO. New Table B-9b separately accounts for summer-peak adjustments; the report says all tables are available in Excel elsewhere on PJM's website. Models use 2014–2023 sector data, hourly observations through August 2024, and 403 weather scenarios derived from 1993–2023. Data-center adjustments occur in AEP, APS, ATSI, BGE, DAYTON, PECO, PL, COMED, DOM, and PS, alongside distinct semiconductor, battery-manufacturing, steel, port, and voltage-optimization adjustments. Ten-year growth: summer peak 3.1%/year, winter peak 3.8%, net energy 4.8%; summer peak reaches 209,923 MW in 2035. The report defines unrestricted peaks as before load-management reductions, with stated treatment of distributed solar, storage, and EVs. Zonal growth is highly uneven; regional demand growth is not local connection headroom.

## R08 — ERCOT: 2025 Constraints and Needs

URL: https://www.ercot.com/files/docs/2025/12/23/2025-Report-on-Existing-and-Potential-Electric-System-Constraints-and-Needs.pdf
Tags: C2; C3 | T1; T2; T6.
Status: report text opened extensively. Data snapshot: 17 December 2025.

This report identifies actual constraints, projected constraints, six-year transmission improvements, large-load procedures, and stability concerns. It reports 238.6 GW of large-load interconnection requests versus 7,502 MW approved to energize since January 2022; approval does not mean all capacity is operational. Queue classifications are “approved to energize,” “planning studies approved,” “under ERCOT review,” and “no studies submitted,” the latter also including projects needing a revised viable connection path. The unadjusted TSP forecast is 218 GW for 2031, while the studied adjusted peak is 159 GW; the document gives an illustrative 100 MW data-center officer-letter load reduced to 27.6 MW through its adjustment factors. It lists $30.21 billion of planned transmission projects for 2026–2031. Actual congestion rents identify bottlenecks but explicitly do not alone establish economic-project eligibility. Stability reports are withheld for security reasons; detailed steady-state models require MIS certificate access.

## R09 — NOVEC: Data-Center Forecast Documentation

URL: https://www.pjm.com/-/media/DotCom/planning/res-adeq/load-forecast/novec-documentation.pdf
Tags: C2 | T1; T2.
Status: full short-document text opened. Forecast prepared August 2025; submitted for the 2026 PJM forecast.

The document exposes a concrete bottom-up forecasting and project-screening process. Building forecasts aggregate to campus, substation, delivery point, customer, and system. Contract milestones are LOA, work plan in development, official work plan, engineering/construction agreement, and electric-service agreement. Requirements include parcel-specific site plans, deposits, CIAC payments, technical engagement, site control, zoning viability, and financial guarantees. “Viable” projects enter the forecast; moderate-risk projects are discounted 50%; high-risk projects are excluded. Building capacity is then converted to metered demand using over a decade of hourly observations and customer/campus-specific behavior. Newly energized sites ramp over years; mature sites have high load/power factors and weaker weather/calendar effects than ordinary commercial buildings. July coincident peak: 1,387 MW actual in 2025; 5,032 MW forecast 2030; 13,140 MW 2040; approximately 17,000 MW total facility capacity. Slowing late-horizon growth reflects absent signed projects, not an asserted market plateau.

## R10 — DOE: Virtual Power Plants Liftoff Update Announcement

URL: https://www.energy.gov/technologycommercialization/articles/us-department-energy-releases-new-reports-highlighting
Tags: C3; C4 | T4; T6.
Status: announcement opened; underlying full VPP report not opened. Published: 10 January 2025.

The page discusses two different reports—geothermal heating/cooling and VPPs—so geothermal investment and demand-reduction figures are not VPP figures. The VPP section reports 33 GW across North America and an 80–160 GW by 2030 deployment scenario representing 10–20% of peak load. DOE says some utilities launched basic VPP programs in under six months with less than $1 million upfront investment, achieving 100+ MW peak-shaving benefits over time; the announcement does not expose individual case-study cost boundaries or performance datasets. It identifies supportive regulation, integrated planning, interconnection, and comprehensive valuation as deployment factors. Its statement that CAISO and ISO-NE had “fully complied” with Order 2222 concerns compliance, not proof every participation pathway was operational. This is a report announcement, not an open enrollment program, procurement award, or guarantee that compute loads qualify.

# 2. Datasets: grid, infrastructure, network, land, climate, population, workloads

## D01 — EIA-860 Generator Inventory

URL: https://www.eia.gov/electricity/data/eia860/
Tags: C1; C2 | T3.
Status: documentation opened; ZIP files not downloaded.

The survey covers plants with at least 1 MW combined nameplate capacity and identifies existing/planned generators and environmental equipment. The page exposes a real file structure: layout/data dictionary; utility; plant; generator; wind; solar; storage; multifuel; owner; environmental associations; environmental equipment. Generator tabs distinguish operable, proposed, and retired/canceled units. Important caveat: the annual retired tab is not a comprehensive retirement history; the page points to preliminary monthly inventories for generators retired since 2002. Environmental association tables connect boilers with generators, cooling systems, particulate collectors, SO2 controls, NOx controls, mercury controls, and stacks. The page lists 2025 early-release and 2024 final ZIPs, plus historical years. Available characteristics include prime mover, energy source, in-service date, nameplate capacity, and summer/winter capability. It does not inventory spare utility capacity for a nearby customer, and the documentation does not establish that every annual workbook field has an equivalent API endpoint.

## D02 — EIA-930 Hourly Grid Operations

URL: https://www.eia.gov/electricity/930-content/about.html
Tags: C2; C3; C4 | T3.
Status: detailed methodology/documentation opened; API not queried.

Variables include demand, day-ahead forecast, net generation, generation by source, total interchange, BA-to-BA interchange, selected subregional demand, and estimated emissions. Battery storage becomes a separate energy-source category on 1 January 2025. Demand is calculated as generation minus net interchange; negative interchange means net inflow. Values are hourly integrated averages, reported hour-ending—not instantaneous measurements. Publication lags differ: demand usually approximately one hour; generation next day; bilateral interchange approximately two days; subregional demand 1–30 days. API history starts January 2019; older flat files extend to collection inception. Emissions use annual fuel factors and an import/export flow model, not marginal-dispatch emissions. BA hourly records are published as reported; daily/regional aggregates incorporate imputation. The page documents DST problems, unconventional BA time zones, pseudo-tie/forecast comparability problems, missing distributed generation, and fuel masking. These details materially affect joins, forecast backtests, and emissions interpretation.

## D03 — EIA-411 Reliability and Planning Data

URL: https://www.eia.gov/electricity/data/eia411/
Tags: C2 | T1; T3.
Status: explanatory page opened; individual tables/download schemas not retrieved.

The “Coordinated Bulk Power Supply and Demand Program Report” collects planners' estimates of electricity supply, capacity, energy, current demand, and future growth. It supports analysis of reliability, generation/transmission construction plans, and consequences of constrained capacity. The page explicitly warns that regional reporting geography changed: historical NERC entities differ from the assessment-area structure used beginning in 2011. Named assessment areas include ERCOT, MISO-US, PJM, SPP, FRCC, NPCC-related areas, SERC aggregates, and WECC aggregates; these are not interchangeable with state boundaries or utility retail territories. This is broad planning context, not feeder-level engineering. Some of the page's historical regional descriptions are dated; the exact geography must be tied to the selected data vintage. The fetched page did not expose complete field layouts, file-level update dates, or a verified complete-survey API.

## D04 — GeoPlatform/EIA Transmission-Line Layer

URL: https://atlas.eia.gov/datasets/geoplatform::electric-power-transmission-lines
Tags: C1; C2 | T3.
Status: direct fetch failed during this pass.

The prior search identified an EIA Energy Atlas catalogue entry titled “Electric Power Transmission Lines,” but this inspection could not retrieve the layer metadata or service contents. Therefore the current field schema, spatial precision, update date, downloadable formats, service URL, and redistribution license are not verified. The earlier search snippet's unusual voltage-threshold wording is not repeated as a dependable technical specification. No available-capacity, circuit-rating, owner, or operating-status field should be presumed without opening the actual metadata. A separate EIA transmission layer is explicitly archived and no longer maintained; it is not automatically the same layer as this catalogue entry. This record is an infrastructure-data lead with a retrieval failure, not a verified nationwide siting-capacity dataset. Archived source: https://atlas.eia.gov/datasets/d4090758322c4d32a4cd002ffaa0aa12_0/about

## D05 — PG&E Grid Resource Integration Portal

Documentation: https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-quick-start-guide.pdf
Portal: https://grip.pge.com
Documented REST endpoint: https://services2.arcgis.com/mJaJSax0KPHoCNB6/arcgis/rest/services/DRPComplianceRelProd/FeatureServer
Tags: C1; C2 | T2; T3.
Status: guide opened; endpoint and live layer responses not independently queried.

PG&E divides datasets into system, ICA, and Distribution Investment Deferral Framework information. System layers include transmission lines/substations, distribution feeders/substations, and some distributed-generation information. ICA includes study results, Expected Load Capacity, and a buffer around networked secondary systems. DIDF includes Grid Needs Assessment, DER/load forecasts, forecast needs, planned projects, and candidate deferral opportunities. Facility names and IDs support joins. Granular Load ICA appears at line-section zoom levels. Detailed CSVs are grouped by administrative division and feeder ID; each line section has 576 hourly results for each of four limiting criteria. The map supports filtering and exports; the guide states REST access requires no login. The guide does not name the four criteria in the extracted text or establish current layer refresh dates. Published study capacity remains different from a binding service reservation.

## D06 — LBNL Queued Up

Original URL: https://emp.lbl.gov/queues
Verified edition: https://emp.lbl.gov/publications/queued-2026-edition-characteristics
Tags: C2 | T2; T3.
Status: original page shell only; 2026 edition landing page opened. Published May 2026. Dataset license: CC BY 4.0.

The 2026 edition, produced with GridTracker, covers generation requests through end-2025 from seven ISO/RTOs and 50 non-ISO balancing areas, representing approximately 98% of installed US generating capacity. It explicitly excludes load requests, distribution-connected projects, and behind-the-meter projects. Offered artifacts: 17.57 MB slide-deck PDF; 14.85 MB XLSX containing project records, a codebook, and 36 summary tabs; linked maps and duration/outcome visualizations. End-2025 active queue: approximately 8,200 projects, 1,312 GW generation, 749 GW storage; 549 GW had draft/executed interconnection agreements without commercial operation. For observed regions, projects entering operation in 2025 had a median request-to-operation time over five years. Of capacity requesting connection in 2000–2020, 13% had operated by end-2025, 75% withdrew, 10% remained active. These are generation outcomes, not data-center load connection times.

## D07 — PJM Seven-Day Load Forecast

URL: https://dataminer2.pjm.com/feed/load_frcstd_7_day
Tags: C2; C3 | T3.
Status: actual web table opened; API not authenticated.

The table exposes Evaluated At UTC/EPT, beginning and ending timestamps in both UTC and Eastern Prevailing Time, Forecast Area, and Forecast Load MW. The retrieved response contained a September 2026 forecast evaluation rather than a confirmed current November snapshot, illustrating that retrieval/cache date and operating-data date are separate. Rows were hourly, area-specific values; the interface showed 100 of 4,200 records with pagination. The table includes both forecast creation and target operating time, enabling separation of forecast lead time from forecasted hour. Its companion documentation says automated system-to-system access requires a PJM account. This feed is projected demand, not observed demand, nodal price, generator availability, or feeder headroom. A single retrieved table page is not the full seven-day dataset or proof of a guaranteed refresh interval.

## D08 — PJM Historical Load Forecasts

URL: https://dataminer2.pjm.com/feed/load_frcstd_hist/definition
Tags: C2; C3 | T3.
Status: dataset definition opened.

This feed retains forecasts grouped by creation time. The page specifies forecast creation every six hours starting one day before the effective date; posting is daily at 12:05 a.m.; retention is indefinite; first availability is 1 January 2011. Defined fields are evaluation UTC/EPT, operating-hour beginning UTC/EPT, forecast area, and forecast load in MW. Unlike a final-vintage forecast series, this structure preserves what was forecast at different information times. The documentation explicitly requires a PJM account to download/use the API. It does not itself contain actual load against which forecast errors could be measured, nor does it define a retail electricity tariff. The displayed “last updated” timestamp belongs to the dataset page/response and should not be confused with every observation's evaluation timestamp.

## D09 — CAISO OASIS

URL: https://oasis.caiso.com/
Tags: C2; C3; C4 | T3.
Status: portal shell and help text opened; individual report queries not executed.

OASIS identifies its contents as system-demand forecasts, transmission outages/capacity status, market prices, and market results. Its navigation links available-transfer-capability information, business-practice manuals, base-case data, interconnection-study statistics, LMP contour maps, and trading-hub real-time prices. The page states technical specifications and artifacts are on the ISO Developer site and require self-registration. Historical data older than 39 months, as far back as 2016, use a separate Historical OASIS Data Downloader. This distinction matters for archival access: the main interface is not necessarily the complete history endpoint. The fetched shell does not expose report-specific parameter names, interval definitions, node schemas, query limits, or every market's current endpoint. OASIS transmission capacity information must not be treated as a distribution-utility service commitment for a new customer.

## D10 — ERCOT Market Information List

URL: https://www.ercot.com/mp/data-products
Tags: C2; C3; C4 | T3.
Status: searchable catalogue interface opened; individual products not downloaded.

EMIL is a metadata catalogue of products required by ERCOT Protocols or other binding documents. Searchable attributes include product name, description, EMIL ID, Report Type ID, applicable rules, target audience, MIS posting location, and access roles. Availability filters distinguish public products from roles such as LSE, TSP, DSP, QSE, resource entity, PUCT, and external retail customer. Delivery filters include API, EWS, Citrix, email, public/secure/certified access, and Data Portal. A “products that have data” filter separates specified products from currently populated products. Digital-certificate authentication unlocks additional MIS information. Therefore “listed in EMIL” does not mean freely downloadable or API-accessible. This source is the place to establish which named report exists and its access class; it is not itself one homogeneous time-series dataset.

## D11 — FCC National Broadband Map

Original download URL: https://broadbandmap.fcc.gov/data-download/nationwide-data
Readable official description: https://www.fcc.gov/BroadbandData
Tags: C1 | T3.
Status: download page returned Access Denied; official BDC description opened.

The FCC describes location-specific internet-service availability and mobile-coverage maps reported by ISPs through Broadband Data Collection. Consumers, governments, Tribes, and other stakeholders can challenge reported availability. The inspected description references a December 2025 availability snapshot and filing-window notices. It establishes the data's semantic meaning—provider-reported service availability—not owned fiber routes, lit/dark-fiber capacity, contracted enterprise connectivity, peering relationships, round-trip latency, or last-mile construction cost. The blocked download page prevented verification of current filenames, nationwide file sizes, exact field layouts, and whether each downloadable product requires registration. Availability files and the Broadband Serviceable Location Fabric are separate licensing/access matters; an accessible map does not establish unrestricted redistribution of the Fabric.

## D12 — PeeringDB API

URL: https://www.peeringdb.com/apidocs/
Tags: C1; C4 | T3.
Status: detailed API schema opened; data endpoint not queried.

Facility records expose IDs, organization/campus relationships, address, latitude/longitude, network/exchange/carrier counts, contacts, property status, available voltage services, and diverse_serving_substations. That last field describes two separate substation paths; it is not a measured capacity or verified power-reliability guarantee. Relationship sets connect facilities with networks and exchanges. Filters include numeric comparisons, __in, case-insensitive string matching, and since Unix timestamps; incremental results can include deleted objects, marked by status. Nested relationships require depth; cached responses refresh approximately every 15 minutes and expose meta.generated. Lookup queries with expansion can truncate at 250 records, requiring pagination. The page documents both skip/limit and page/per_page. It also contains non-public editor helpers explicitly outside the public API. Public schema examples are not evidence that every facility fills every field accurately or currently.

## D13 — RIPE Atlas BigQuery and Public Measurements

URL: https://github.com/RIPE-NCC/ripe-atlas-bigquery
Tags: C1; C4 | T3.
Status: repository README opened; BigQuery datasets not queried.

The repository distinguishes two datasets: samples, a static 1% sample for learning, and measurements, six continuously updated public views. Tables/views cover DNS, HTTP, NTP, ping, SSL certificates, and traceroute; measurement history starts 1 January 2020. The project is ripencc-atlas; an example view name is ripencc-atlas.measurements.ping. BigQuery use requires a Google account and a project under which queries run; tutorials cover minimum RTT and estimating/minimizing query costs. The README separately identifies Atlas API and bulk-download access. This is observed network performance from deployed probes to measured targets, not universal latency between arbitrary parcels. Probe/target coverage, test timing, and routing determine what can be inferred. Usage is subject to RIPE Atlas Terms and Conditions; the README is not a blanket permissive database-license grant.

## D14 — MRLC / Annual NLCD

URL: https://www.mrlc.gov/
Tags: C1 | T3.
Status: product catalogue and release notices opened; raster tiles not downloaded.

Annual NLCD has six products: predominant land-cover class; year-to-year land-cover change; class confidence; fractional imperviousness; impervious descriptor distinguishing roads from other developed land; and spectral-change day of year. Collection 1.2, announced 10 June 2026, extends CONUS coverage through 2025, beginning in 1985. MRLC also hosts legacy NLCD, rangeland fractional components, and weekly exotic-annual-grass/herbaceous products—these are separate collections with different temporal semantics. Access includes downloads, WMS, visualization, and geographic subsetting. The EVA tool supplies county statistics comparing land-cover dates. The site's separate tree-canopy release explicitly states 30 m resolution; the inspected homepage does not establish every collection's full spatial specification. Land cover and imperviousness characterize surface conditions, not zoning permission, parcel ownership, utility-service availability, or structural reuse suitability.

## D15 — NOAA Climate Data Online API

URL: https://www.ncei.noaa.gov/cdo-web/webservices/v2
Tags: C1; C3 | T3.
Status: full API documentation opened; authenticated requests not made.

Base URL: https://www.ncei.noaa.gov/cdo-web/api/v2/{endpoint}. Endpoints: datasets, data categories, data types, location categories, locations, stations, and data. Authentication is a token HTTP header; limits are five requests/second and 10,000/day. JSON collections include results and pagination metadata. Default result limit is 25; maximum 1,000. Station discovery supports geographic extent, dataset/type filters, and date coverage. /data requires exactly one dataset ID plus start/end dates; annual/monthly requests allow up to ten years, other data up to one year. units=metric or standard performs scaling/conversion; absent units, no conversion is promised. Coverage fields include minimum/maximum date and data coverage. This is a historical climate-observation service, not a universal hourly weather forecast or parcel-specific cooling-system simulation.

## D16 — USGS Water Data for the Nation

URL: https://waterdata.usgs.gov/
Tags: C1 | T3.
Status: public portal overview opened; individual APIs/schemas not inspected.

The portal spans more than 135 years and over one million monitoring locations; more than 13,500 locations provide real-time stream, lake, reservoir, precipitation, water-quality, or groundwater information. Four distinct observation classes are named: continuous data, daily data, field measurements, and discrete samples. Location metadata identifies the station, responsible agency, and geographic position; discovery can filter state, county, site type, and recency. It links machine-readable REST APIs and dataRetrieval libraries for R/Python. WaterAlert is a separate subscription alert service, not the same as bulk historical retrieval. A monitoring record does not establish a legal withdrawal right, potable/reclaimed-water utility connection, treatment capacity, or data-center cooling-water allocation. Exact parameter codes, current API-version migration details, observation quality flags, and numerical units were not established from this overview page.

## D17 — FEMA National Flood Hazard Layer

URL: https://www.fema.gov/flood-maps/national-flood-hazard-layer
Tags: C1 | T3.
Status: detailed overview/access guidance opened.

NFHL combines effective Flood Insurance Rate Maps and Letters of Map Change; digital coverage exceeds 90% of the US population, not necessarily 90% of land area. Access routes include Map Service Center, NFHL Viewer, county/state GIS downloads, KMZ, and dedicated GIS web services. The page carefully distinguishes effective, preliminary, and pending maps. Pending data have received final determination but do not establish minimum NFIP requirements until effective after the six-month adoption/compliance period. Other flood-risk viewers can include future conditions, sea-level rise, or base-level engineering not present in effective NFHL. Official determinations require suitable basemap accuracy and correct interpretation. This is particularly important where “unmapped” is mistaken for “no flood risk.” Exact GIS table definitions reside in linked technical references, not the overview itself.

## D18 — FEMA National Risk Index

URL: https://www.fema.gov/about/openfema/data-sets/national-risk-index-data
Tags: C1 | T3.
Status: versioned catalogue opened; files not downloaded.

The page identifies December 2025 v1.20 as the available version and supplies tables, shapefiles, and geodatabases for states/territories, counties, census tracts, and Tribal relational datasets. Compressed downloads range approximately 39–411 MB. Documentation links include data dictionary, glossary, metadata, technical documentation, and FAQ. Eighteen hazards are explicitly listed, including coastal/inland flooding, drought, heat/cold, wildfire, earthquake, landslide, hurricane, tornado, tsunami, and winter weather. The index is a baseline community-risk measurement assembled from hazard and community-risk factors, not a site engineering investigation or event forecast. County/tract aggregates cannot establish an individual building's flood elevation, seismic condition, wildfire defensibility, or cooling-water reliability. Terms/citation requirements are linked separately. The inspected page does not establish a supported query API for this file collection.

## D19 — Census ACS Five-Year API

URL: https://www.census.gov/data/developers/data-sets/acs-5year.html
Tags: C1 | T3.
Status: API documentation opened; authenticated queries not made.

The page covers annual releases through 2024 and explicitly states all Census API queries now require a key. Detailed tables reach block groups; subject tables and data profiles generally reach tracts; comparison profiles extend to places/county subdivisions. Releases are five-year pooled estimates, not current-day population counts. The 2020–2024 dataset can be compared with non-overlapping 2015–2019 estimates. It documents variable-change categories—unchanged, updated with a match, and no match—and annotation variables explaining unavailable or inapplicable values. Example detailed-table request uses data/2024/acs/acs5, get=NAME,group(B01001), geography filters, and a key. These data provide demographic/economic context rather than direct inference-demand measurements; geographic proximity to population is not itself an observed workload trace or latency guarantee.

## D20 — Census TIGER/Line

URL: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
Tags: C1 | T3.
Status: release documentation opened; shapefiles not downloaded.

The 2026 shapefiles were released 14 October 2026; legal boundaries/names represent 1 January 2026. Modern releases use shapefiles; 2006 and earlier use TIGER/Line ASCII, with Census 2000 available in both. The page explicitly says core geometry files do not include demographic data but contain geographic entity codes linking to Census statistics. Downloads use the FTP archive, accompanied by technical documentation, errata, and user notes. Release date, boundary-reference date, and demographic-estimate period are different concepts. TIGER/Line is not a nationwide ownership parcel database, zoning code, or assessor building-condition inventory. A geographic join can link census attributes, but this source does not establish permission for data-center use or utility-serving territory boundaries.

## D21 — San Francisco Property Information Map

URL: https://sfplanninggis.org/PIM/
Tags: C1 | T2; T3.
Status: extensive application text/layer inventory opened; no particular parcel researched.

Search accepts address, parcel, planning-application number, or map click. Parcel reports combine zoning, height/bulk districts, special-use districts, setbacks, environmental overlays, historic status, planning applications, building/electrical/plumbing permits, complaints, appeals, and notices of special restrictions. Specific hazards include stormwater flooding, FEMA coastal flooding, sea-level rise, liquefaction, landslide, hazardous-site lists, serpentine rock, and slopes over 25%. It exposes year-built and parcel-history layers. Important caveats are explicit: limited/nonconforming-use data are incomplete and unmaintained; starred fields are city-staff-only; historic-resource status is tentative pending specialist confirmation; listed NSRs are limited to Planning Code matters. This portal describes entitlement/history/context, not structural floor capacity, transformer capacity, fiber contracts, or automatic permission to convert a building into compute space.

## D22 — National Zoning Atlas

URL: https://www.zoningatlas.org/
Tags: C1 | T2; T3.
Status: homepage/method description opened; underlying district schema/download contract not opened.

The organization reports more than 200 standardized regulatory characteristics per district, over 11,000 published jurisdictions, more than 1.3 million zoning-code pages reviewed, and over 224 million people in published jurisdictions. Its broader mission references more than 33,000 US jurisdictions; that is not a claim all 33,000 are already mapped. The homepage's dominant documented uses involve housing, lot sizes, parking, manufactured housing, and comparative zoning analysis. It does not establish that “data center” is a normalized nationwide permitted-use field or that industrial districts uniformly allow that use. Published records are interpretations of zoning codes and geospatial files; exact legal permissions remain jurisdiction/code-specific. Current API access, bulk format, update SLA, district-level timestamp fields, and open redistribution license were not established from the inspected homepage.

## D23 — Google Borg Workload and Power Traces

URL: https://github.com/google/cluster-data
Power-data documentation: https://github.com/google/cluster-data/blob/master/PowerData2019.md
Tags: C3; C4 | T3.
Status: repository and power-data README opened. License: CC BY for data and trace documentation.

The root distinguishes version 3/2019—eight Borg cells during May 2019—from version 2/2011—a single approximately 12,500-machine cell—and a deprecated seven-hour 2009 trace. It also links schemas, Colab notebooks, a bibliography, and separate execution-testing traces. Material addition: power traces cover 57 domains during May 2019; two belong to facilities using a newer medium-voltage power-plane design, while the remainder relate to the eight 2019 workload cells. The power README links Data Center Power Oversubscription with a Medium Voltage Power Plane and Priority-Aware Capping and a notebook reproducing figures. The precise sampling interval and workload-to-power join semantics reside in a linked PDF not inspected here. These are historical hyperscale traces, not geographically identified edge sites or a measured wholesale DR deployment.

## D24 — Alibaba Cluster Trace Program

URL: https://github.com/alibaba/clusterdata
Tags: C3; C4 | T3.
Status: root README opened; individual release files not downloaded.

Releases differ substantially: 2017 has approximately 1,300 machines/12 hours; 2018 approximately 4,000 machines/eight days plus batch DAGs; GPU 2020 has over 6,500 GPUs on approximately 1,800 machines/two months; GPU 2023 over 6,200 GPUs on approximately 1,200 machines with heterogeneous resource specifications. GPU 2025 covers over 150 recommendation-inference services and more than 20,000 instances. The 2026 GPU description reports six months, up to 155,410 GPUs and 37,707 servers, with workload mix, priorities, requests/utilization, inventory, topology, traffic, and execution-time fact tables. Other 2026 folders describe diffusion-model serving, LLM model-as-a-service, and spot GPUs. Older download routes require surveys. The root permits catalog/research/study use but does not establish a uniform unrestricted commercial-data license. Resource traces are not automatically electrical-meter traces; schema, anonymization, and license must be checked per release.

## D25 — Azure LLM Inference 2023

URL: https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2023.md
Tags: C3; C4 | T3.
Status: complete release README opened.

The sample was collected from multiple Azure LLM inference services on 11 November 2023 and accompanies ISCA 2024's Splitwise: Efficient generative LLM inference using phase splitting. Separate code and conversation download links are supplied. Exactly three schema fields are documented: TIMESTAMP invocation time, ContextTokens, and GeneratedTokens. A notebook reproduces characterization graphs. Privacy restrictions mean prompt content is absent; benchmarking uses synthetic/selected inputs with matching token counts and forces corresponding output lengths. The release is CC BY and requests citation of Splitwise. This file does not provide geography, utility meters, energy per token, measured power, service deadlines, queue tolerance, or price. Those cannot be inferred as observed fields merely because the trace supports serving-system studies.

## D26 — Azure LLM Inference 2024

URL: https://github.com/Azure/AzurePublicDataset/blob/master/AzureLLMInferenceDataset2024.md
Tags: C3; C4 | T3.
Status: complete release README opened.

The sample spans 10–19 May 2024 across multiple services and accompanies HPCA 2025's DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency. Downloads again distinguish code and conversation. Fields are invocation timestamp, context-token count, and generated-token count; prompt text is unavailable for privacy reasons. The page identifies a Jupyter notebook and accompanying paper, but does not reproduce DynamoLLM's actual energy/performance result tables in the README. It therefore establishes a production-derived request-size/arrival trace—not measured energy savings, a deployable cluster scheduler, a particular model's latency curve, or workload interruptibility. CC BY licensing and paper attribution are explicit. The collection year and paper-publication year differ and should be kept distinct in metadata.

## D27 — Azure LMM Inference 2025 Release

URL: https://github.com/Azure/AzurePublicDataset/blob/master/AzureLMMInferenceDataset2025.md
Tags: C3; C4 | T3.
Status: complete release README opened.

Despite the release name, observations were collected 15–22 October 2024 from a multimodal inference cluster. The accompanying paper is SoCC 2025's ModServe: Modality- and Stage-Aware Resource Disaggregation for Scalable Multimodal Model Serving. The repository file is data/AzureLMMInferenceTrace_multimodal.csv.gz; the README gives a standard gunzip command. Fields: TIMESTAMP, NumImages, ContextTokens including text/image tokens, and text GeneratedTokens. Actual customer prompts/images are not disclosed; the described benchmark substitutes input sizes and ShareGPT-4o images. License is CC BY with paper attribution. The data distinguish image count from token count but do not identify site power, accelerator type, individual-customer location, network bandwidth, deadlines, or utility dispatch events.

# 3. Tools, APIs, simulation environments, and commercial platforms

## S01 — Carbon Aware SDK

URL: https://github.com/Green-Software-Foundation/carbon-aware-sdk
License: https://github.com/Green-Software-Foundation/carbon-aware-sdk/blob/dev/LICENSE
Tags: C3; C4 | T5.
Status: README and MIT license opened; software not executed.

The SDK provides equivalent functionality through Web API and CLI; the API can run in a container alongside applications or centrally. Its central role is decoupling application logic from carbon-data providers, standardizing outputs to gCO2/kWh, and centralizing provider credentials/auditability. The README names WattTime and Electricity Maps as providers and UBS/Vestas as adopters. Important distinction: provider aggregation appears as a roadmap feature, not an unequivocally implemented production capability. The README also states energy-mix percentages are not supplied by the API at that time. Claims of up to 15% timing-related and 50%+ location-related ML carbon reductions are project claims without a benchmark dataset in this README; they are not universal guarantees. MIT governs code, not upstream subscriptions. The SDK supplies decision information, not automatic workload-migration permissions or wholesale dispatch qualification.

## S02 — Kepler

URL: https://github.com/sustainable-computing-io/kepler
Tags: C3 | T5.
Status: current README opened; installation not run. License: Apache-2.0 with component notices.

Kepler is a Prometheus exporter for container, pod, and node energy metrics in Kubernetes. The README gives Helm installation from oci://quay.io/sustainable_computing_io/charts/kepler, namespace creation, readiness waiting, service port-forwarding to 28282, and a sample query for kepler_node_cpu_watts. Other routes include local privileged execution, Docker Compose with Prometheus/Grafana, and Kustomize. A material compatibility warning says manifests and image tags must match: main can reference unshipped health endpoints and cause older images to crash-loop. Documentation distinguishes the 0.10 rewrite from legacy 0.9.x. Its repository contains power-attribution and metrics guides, but this pass did not inspect their accuracy/error models. Kepler measures/attributes energy; it does not itself provide carbon forecasts, jobs' deferral deadlines, cooling electricity, utility-grade revenue metering, or dispatch control.

## S03 — OpenLEADR Python

URL: https://github.com/OpenLEADR/openleadr-python
Tags: C3; C4 | T5.
Status: feature-completeness/security table opened. License: Apache-2.0.

The module implements OpenADR 2.0b, with both VEN client and VTN server. Supported features include HTTP pull, registration, telemetry reports, events, and message signing over secured connections. Explicitly unsupported in the table: HTTP push, XMPP, history reports, EiOpt, and status reports, with status-report work linked separately. The official OpenADR Alliance root certificate is not included. HTTP pull is identified as the common method permitting a VEN behind NAT. The repository advertises one-minute examples but also warns the code is still developmental and not recommended for mission-critical or security-paramount applications. It supplies Python integration and testing infrastructure, not evidence of certification for every deployment. OpenADR 2.0b compatibility must not be confused with OpenADR 3's distinct API specification. Utility onboarding, certificates, contract eligibility, and physical control authority remain external.

## S04 — SustainDC

URL: https://github.com/HewlettPackard/dc-rl
Tags: C3 | T3; T5.
Status: extensive README/configuration material opened; simulations not executed.

Three coupled environments model delayable workloads, data-center IT/HVAC, and batteries. Workload actions store delayable tasks, process immediate tasks, or maximize throughput; HVAC actions change or maintain cooling setpoint; battery actions charge/hold/discharge. Observations include time encodings, carbon forecasts, workload backlog, ambient/room temperature, prior energy, grid consumption, and battery SoC. Configuration examples expose facility capacity, battery parameter, flexible-load ratio, active agents, data files, and individual/cooperative reward weights. Inputs include Alibaba 2017/Google 2011 workload derivatives, EPW weather, and EIA-derived carbon files for eight US states. Custom workload format requires cpu_load between 0–1 and 8,760 hourly rows; original traces are not necessarily themselves year-long observations. Metrics include IT/HVAC energy, carbon, water, and dropped tasks. Python 3.10+, dependencies, training/evaluation scripts, and pretrained-model directories are public. Mixed MIT/CC BY-NC portions restrict blanket commercial-use assumptions; results are simulations, not field-validated dispatch.

## S05 — CityLearn

URL: https://lfenergy.org/projects/citylearn/
Tags: C3; C4 | T5.
Status: detailed project page opened; repository/package not executed. License: MIT.

CityLearn models virtual districts with heat pumps, electric heaters, thermal tanks, batteries, EVs, and PV. It standardizes observations, actions, reward functions, datasets, and KPIs across rule-based, MPC, single-agent RL, and multi-agent RL controllers. The page identifies cost, carbon, comfort, and grid metrics; an internal backup controller meets building loads and occupant comfort regardless of agent choices. Foundations include Gymnasium, US End-Use Load Profiles, LSTM thermal dynamics, and optional PySAM PV sizing. Tooling includes CLI, tutorials, and a visualization UI. The project is LF Energy Sandbox, with the v2 series beginning in 2023. It is building-district flexibility infrastructure, not an out-of-the-box physical model of GPU inference, server power caps, data-center cooling plants, or wholesale-market settlements. Feeder capacity is not established merely by aggregating simulated building demand.

## S06 — pandapower

URL: https://github.com/e2nIEE/pandapower
Tags: C2; C3; C4 | T5.
Status: README opened; network solves not executed. License: BSD-3-Clause as established in catalogue/license source.

The package represents electrical networks through pandas-based data structures and supports analysis/optimization using MATPOWER/PYPOWER-compatible case formats. Named solver integrations include improved Newton–Raphson, PYPOWER solvers, PowerGridModel, lightsim2grid, and PowerModels.jl. The repository links minimal examples, interactive tutorials, documentation, and SimBench grid models/load profiles. This is a distinction between calculation engine and input evidence: a network case must contain topology, impedances, transformer/line ratings, loads, generation, and operating assumptions appropriate to the question; downloading a package does not recover a real utility's hidden model. The inspected README establishes power-system modeling capabilities, not a validated US nationwide hosting-capacity dataset. Its sibling pandapipes addresses gas/heat/water networks; those capabilities are not automatically part of pandapower. License source: https://github.com/e2nIEE/pandapower/blob/develop/LICENSE

## S07 — HELICS

URL: https://github.com/GMLC-TDC/HELICS
Tags: C2; C3; C4 | T5.
Status: extensive README opened; federation not run. License: BSD-3-Clause.

HELICS synchronizes independent simulators—“federates”—and exchanges runtime data so they act as a federation. The README explicitly states HELICS cannot simulate anything by itself. Bindings include Python, C, Java, Octave, Julia, MATLAB, and Simulink; Nim/C# are described as experimental. Supporting executables include broker, broker server, player, recorder, and general app. Player replays timed data from files; recorder captures subscribed streams, enabling repeatable debugging/replay. Example/tutorial repositories include transmission–distribution–market–communications co-simulation. It supports multi-domain coupling across electrical systems, buildings, transport, gas, and controls, but requires external models and interfaces. The source claims scale from laptop pairs to 100,000+ simulators; no such scalability benchmark was reproduced here. A Docker helper image contains executables, not necessarily libraries needed for linking.

## S08 — EnergyPlus

Original URL: https://github.com/NREL/EnergyPlus
Resolved repository: https://github.com/NatLabRockies/EnergyPlus
Tags: C1; C3 | T5.
Status: redirected repository README opened. License: BSD-3-like.

EnergyPlus models whole-building energy and water use. Repository directories include datasets, weather, input dictionary/schema, testfiles, engineering/developer documentation, APIs, and workflows. Documentation differentiates Getting Started, Input Output Reference, Engineering Reference, epJSON input schema, native C API, and Python bindings for runtime/data-transfer/callback interfaces. Releases occur twice yearly, usually March and September. latest documentation follows development; stable follows the formal release, so object syntax and APIs can differ by version. The README warns pre-release input changes may not be supported by transition tools. It establishes a building/HVAC simulation engine, not a calibrated model of a particular facility or a ready networked compute-fleet controller. Facility geometry, schedules, loads, equipment, controls, and weather are separate inputs; no claim that a five-hour installation produces an accurate data-center thermal model was tested.

## S09 — Scaphandre

URL: https://github.com/hubblo-org/scaphandre
Tags: C3 | T5.
Status: README/features opened; agent not installed. License: Apache-2.0.

The Rust metrology agent targets bare-metal and QEMU/KVM host/VM power and energy information. It can expose VM metrics back inside a VM through hypervisor capabilities, and export through Prometheus HTTP, Prometheus Pushgateway, Riemann, Warp10, JSON files, or terminal output. Kubernetes support and packages for several Linux distributions and Windows versions are listed. The README still characterizes the project as early-stage. Its low-overhead goal is an objective, not a verified zero-overhead guarantee. The fetched overview does not establish error bounds, every supported processor, GPU/cooling coverage, or electricity-meter equivalence. It supplies observability, not workload scheduling, carbon accounting by itself, retail demand-charge computation, or certified performance settlement. VM visibility depends on host/hypervisor support rather than being universally available in public cloud VMs.

## S10 — PowerAPI

URL: https://powerapi.org/
Tags: C3 | T5.
Status: official overview opened. Code license: BSD-3-Clause; website content: CC BY 4.0.

PowerAPI is a Python framework for software-defined power meters. Its documented attribution granularities include global machine, VM, container, application, process, and code. The architecture is actor-based and extensible through plugins for metric storage, power estimation, and computation. The page explicitly describes estimating application power without an additional physical meter; this does not mean every estimate has the accuracy or coverage of an external meter. It links the June 2024 JOSS paper, DOI 10.21105/joss.06670, and a HAL article. The overview does not expose a complete installation recipe, hardware-counter prerequisites, calibration procedures, estimator error distributions, or supported platform matrix. The domain is powerapi.org; the unrelated powerapi.com result from the earlier search is not this research toolkit.

## S11 — Electricity Maps API

Overview: https://app.electricitymaps.com/docs
Specific schema: https://app.electricitymaps.com/docs/reference/carbon-intensity/latest
Tags: C1; C3; C4 | T3; T5.
Status: API overview and representative v4 endpoint opened; authenticated call not made.

The API covers mix, flows, load/net load, carbon intensity, renewable/carbon-free share, European day-ahead prices, and US day-ahead LMPs. Common endpoint suffixes distinguish historical range, historical instant, last 24 hours, latest, and forecast; price endpoints also distinguish published actual prices from combined actual/proprietary forecasts. /v4/carbon-intensity/latest accepts zone or latitude/longitude, temporal granularity of five minutes/15 minutes/hourly, direct versus lifecycle emission factors, and flowTraced consumption-versus-production accounting. Defaults include hourly, lifecycle, and flow-traced. disableEstimations can omit estimated points; response metadata includes timestamp, updated/created times, estimation flags/method, and granularity. A 14-day trial is advertised. These are zone-level modeled/assembled electricity data, not meter-level site emissions or marginal emissions by default; current access/coverage depends on the commercial plan.

## S12 — WattTime Data API

Original URL: https://docs.watttime.org/
Readable official description: https://watttime.org/data-science/data-signals/
Tags: C3; C4 | T3; T5.
Status: API documentation fetch failed twice; signal overview opened.

The official overview specifies three signal names and units: co2_moer, marginal operating CO2 emissions in pounds/MWh; co2_aoer, generation-weighted average CO2 in pounds/MWh; and health_damage, monetized marginal health impact in USD/MWh. WattTime distinguishes forecasting for load-shift decisions from historical signals for quantifying achieved effects. It presents marginal signals for intervention/avoided-emissions analysis and average signals for footprint accounting. Its stronger statement that average-signal load shifting “wouldn't reduce emissions” is the provider's methodological position, not a universal empirical theorem independently established here. Because the docs were inaccessible, current authentication routes, endpoint payloads, forecast horizons, rate limits, region IDs, free/research entitlements, and redistribution rights remain unverified. The API must not be represented as fully tested or unrestricted.

## S13 — EnergyHub Utility Integrations

URL: https://www.energyhub.com/edge-derms-platform/utility-integrations
Tags: C3; C4 | T5.
Status: vendor product page opened; partner documentation not accessed.

EnergyHub describes an integration gateway separated from its core platform, synchronizing EnergyHub REST APIs with utility systems. It presents integration with GE Vernova GridOS DERMS as combining grid optimization with customer-side/grid-edge resource controls. The page links VPP maturity, load-shaping, and deployment material but does not expose a public OpenAPI schema, downloadable SDK, source code, sandbox credentials, commercial price, or compute-specific connector. Vendor claims about capacity and operational benefits are not independently measured by this page. This source establishes that commercial DERMS-to-utility integration is a product function; it does not establish that arbitrary edge servers can register, be dispatched, or settle wholesale transactions through an open API. Proprietary platform access and utility agreements remain separate from public marketing documentation.

# 4. Programs and participation pathways

## P01 — Loudoun Data Center Standards and Locations

URL: https://www.loudoun.gov/5990/Data-Center-Standards-Locations
Tags: C1; C2 | T2; T6.
Status: official project page opened.

The county initiated the process 6 February 2024 and split it into two phases on 2 July 2024. Phase 1, approved 18 March 2025, converted data centers from previously by-right uses to conditional/Special Exception uses in affected areas. Phase 2 is described as underway and concerns data-center/substation policy and use-specific standards. A grandfathering resolution allows some applications accepted before 12 February 2025 to proceed without new SPEX approval. The page links an application-pathway guide but explicitly says the ordinance and adopted resolution override that illustrative guide. Additional artifacts include an existing/proposed data-center map, LandMARC records, open-house materials, public comments, and meeting documents. The page does not supply a simple countywide “allowed/not allowed” parcel CSV, a guaranteed approval timeline, or proof every pre-cutoff application qualifies for grandfathering.

## P02 — EPRI DCFlex Demonstrations

URL: https://dcflex.epri.com/demonstrations
Tags: C2; C3; C4 | T5; T6.
Status: demonstration catalogue opened; underlying deliverable PDFs not all opened.

The page says the initiative will feature at least ten demonstrations spanning geography, market structure, scale, technology, load flexibility, power quality, and backup power. Its 2025 update names Phoenix, Lenoir, Paris, and Chicago, with AI workload modulation, demand response, backup integration, and fault ride-through among topics. One precisely described field test compared HVO and fossil diesel on 6 May 2026 using a 2 MW Cummins QSK60/DQKAB backup generator at a Compass facility in Texas. Mostardi Platt tested 50% and 100% load using EPA reference methods; pollutants included PM, NOx, CO, CO2, hydrocarbons, and selected hazardous pollutants. A separate lifecycle assessment used GREET. The landing page does not reproduce numerical emissions results or compute-curtailment MW. Generator rating, lifecycle GHG effects, and grid flexibility are distinct quantities; ten planned demonstrations does not prove ten completed public-result datasets.

## P03 — ERCOT Emergency Response Service

URL: https://www.ercot.com/services/programs/load/eils
Tags: C3; C4 | T6.
Status: program description and document list opened; DOCX technical requirements not downloaded.

ERS selects qualified loads, generators, and their aggregations for emergency availability, arranged through QSEs. Participants can reduce consumption or increase generation within ten or thirty minutes to prevent/alleviate an actual or anticipated Energy Emergency Alert. Procurement occurs four times per ERS year: December–March, April–May, June–September, and October–November. The page links offer disclosures, procurement results, monthly response, submission/unavailability forms, reinstatement procedures, and term-specific RFPs/technical requirements. Current materials include October–November 2026 and December 2026–March 2027. Authorization is PUCT Rule §25.507. The overview establishes general commercial/industrial participation, not automatic eligibility for all data centers. Minimum offers, test procedures, baseline methods, duration obligations, compensation formulas, and nonperformance penalties require the term's technical documents and were not verified from the landing page.

## P04 — CAISO Demand Response

URL: https://www.caiso.com/generation-transmission/load/demand-response
Tags: C3; C4 | T4; T6.
Status: detailed official participation page opened.

Aggregators of customer demand reductions can participate in day-ahead, real-time, and ancillary-service markets through applicable models. Entry requires the New Resource Implementation process, a scheduling coordinator, and ISO-certified revenue-quality meters; ancillary services additionally require special certification and direct telemetry. Proxy Demand Resources must satisfy the net-benefits-test mechanism establishing a monthly threshold for cost-effective DR bids. PDR-LSR permits eligible storage to bid both decreases and increases in load using two distinct Resource IDs: one for curtailment and one for consumption, with different price ranges. The page links DRRS location/registration management, agreements, participant lists, telemetry checklists, tariff, BPM, and participation-model comparison. LAP mapping is available in OASIS Full Network Model Mapping. The page also distinguishes out-of-market ELRP/DSGS emergency programs from CAISO market participation. An API signal alone does not satisfy these registration and metering requirements.

## P05 — CAISO DER Provider Model

URL: https://www.caiso.com/generation-transmission/generation/distributed-energy-resources
Tags: C3; C4 | T4; T6.
Status: detailed official participation page opened.

DER providers own or operate aggregations participating in wholesale energy/ancillary markets. Before NRI, the provider must obtain distribution-utility or metered-subsystem concurrence; the page specifies a 30-business-day concurrence review. This review is separate from the overall onboarding/implementation duration. Participation requires a scheduling coordinator and revenue-quality meters, with additional telemetry/certification for ancillary services. Listed contractual artifacts include Scheduling Coordinator Agreement, Meter Service Agreement, DER Provider Agreement, information-request sheets, and concurrence-letter template. A signed-DERPA participant list establishes entities with agreements, not necessarily their current dispatched capacity or commercial performance. The page does not publish a blanket rule allowing geographically arbitrary sites to aggregate or state that a compute fleet alone meets every DERP resource requirement; applicable tariff/BPM locational and operational rules remain controlling.

## P06 — California Demand Side Grid Support

URL: https://www.energy.ca.gov/programs-and-topics/programs/demand-side-grid-support-program
Guidelines metadata: https://www.energy.ca.gov/publications/2026/demand-side-grid-support-dsgs-program-guidelines-fifth-edition
Docket: https://efiling.energy.ca.gov/Lists/DocketLog.aspx?docketnumber=22-RENEW-01
Tags: C3; C4 | T6.
Status: program, publication metadata, and docket opened; adopted 88-page guideline text not fully inspected.

The program pays eligible customers for net-load reductions and backup generation during extreme events, May–October, using capacity commitments and per-unit performance incentives. AB 205 created it; AB 209 expanded eligibility in 2022. The program links Fifth Edition guidelines, status reports, 2025 Option 3/4 enrolled capacity by county/district, and performance workshops. Version control is important: the publication page says “updated February 27,” while the docket explicitly records adopted clean/strikeout versions on 27 April 2026, TN269649/TN269650. The docket also identifies anonymized 2024/2025 storage-VPP performance workbooks with monthly site-level and hourly-discharge sheets. Exact current option thresholds, payments, dual-enrollment restrictions, generator conditions, and budget availability were not established by opening the metadata alone.

## P07 — MISO Expedited Resource Addition Study

URL: https://www.misoenergy.org/meet-miso/media-center/2025---news-releases/ferc-approves-misos-expedited-resource-addition-study/
Tags: C2 | T2; T6.
Status: approval announcement opened.

MISO describes ERAS as temporary and targeted generation interconnection intended to address urgent resource-adequacy needs while broader process reform proceeds. The announcement says initial interconnection requests were accepted 6–11 August 2025, studied first-come/first-served, with the first quarterly study beginning 2 September. It links a fuller schedule, informational guide, and application tool but the fetched text does not expose all eligibility conditions or the detailed “key features” list. This source confirms approval and the initial cycle; it does not establish a currently open application window as of November 2026, completion of every study, or actual commercial operation. ERAS is a generation-resource pathway, not an unrestricted data-center load queue or direct enrollment into a demand-response program.

## P08 — MISO Large Load Integration

URL: https://www.misoenergy.org/planning/large-loads---container-page/large-load-additions/
Tags: C2; C3; C4 | T2; T6.
Status: current framework page opened.

MISO describes requests seeking connection in 18–36 months, faster than typical generation/transmission construction. Its three-part framework is connect quickly, transition/scale with flexibility, and operate reliably. The page states an approval objective within 120 days with studies/GIAs signed, but this is not a guarantee physical service is energized in 120 days. Named mechanisms include co-location/ZGIA, ERAS, expedited project review, non-firm service, firm-service step-up, and new study procedures under development. Operational requirements listed include curtailment, real-time telemetry, resource-adequacy coordination, ride-through, stability control, resilience, and security. It references a 18 June 2026 FERC direction to update large-load tariff provisions. The page mixes existing tools and developing solutions; exact eligibility, firm-service rights, curtailment limits, and legally effective rates are not provided in this framework summary.

## P09 — Google 2023 Demand-Response Deployment

URL: https://cloud.google.com/blog/products/infrastructure/using-demand-response-to-reduce-data-center-power-consumption
Tags: C3; C4 | T5; T6.
Status: complete operator narrative opened. Published: 3 October 2023.

A utility/grid forecast-event notice enters Google's global compute-planning system; an algorithm generates hour-by-hour limits on non-urgent tasks at specified sites. Work can be delayed until after the event or, where feasible, rerouted to a different grid. Examples of non-urgent tasks include YouTube processing and translation-system background work. Europe: daily reductions during typical 5–9 p.m. peaks, December 2022–March 2023, in Netherlands, Belgium, Ireland, Finland, and Denmark. Taiwan: daily peak reductions in summers 2022/2023 with Taipower. US examples include Oregon, Nebraska, and the Southeast; Northern Wasco County PUD confirms a day-ahead pilot at The Dalles. Google reports no additional computing hardware and no impairment of named user-facing services. The article supplies no event-level MW series, rebound profile, baseline methodology, or independently audited savings.

## P10 — Google ML Flexibility Agreements

URL: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/how-were-making-data-centers-more-flexible-to-benefit-power-grids/
Tags: C3; C4 | T5; T6.
Status: full announcement opened. Published: 4 August 2025.

The announcement identifies I&M and TVA utility agreements specifically targeting ML workloads, building on three OPPD grid events in 2024. I&M's statement names Google's new Fort Wayne, Indiana, facility. It separately names Centrica Energy/Elia in Belgium and Taipower for earlier non-urgent workload flexibility. Google explicitly says flexibility is early-stage, available only at certain locations, and limited by high service-reliability obligations—including healthcare customers. This is evidence of bilateral utility coordination and operator-reported demonstrations, not an open utility tariff available to arbitrary compute sites. The announcement does not disclose contracted MW, annual event caps, notice periods, payments, measurement/verification, rebound constraints, or penalties. It also does not establish that every ML workload, particularly latency-critical inference, can pause or migrate.

# 5. Standards, regulatory interpretation, orchestration, and edge architecture

## N01 — FERC Order 2222 Explainer

URL: https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy
Tags: C3; C4 | T4; T6.
Status: full explainer opened. Foundational orders: 2020/2021; page states updated 23 January 2025.

The explainer distinguishes component DERs, aggregators, wholesale markets, and retail customers. Aggregators—not each device—are typically direct market participants. Rules must address minimum aggregation size down to 100 kW, geographic/node limits, metering, telemetry, and coordination among ISO/RTO, utility, aggregator, and regulator. It explicitly states Order 2222 does not apply to ERCOT. Simultaneous retail/wholesale participation requires avoiding duplicate compensation. Critical freshness limitation: implementation timelines are explicitly “as of August 2024”; their listed future dates are not verified operational status in November 2026. Dockets are identified for CAISO ER21-2455, NYISO ER21-2460, ISO-NE ER22-983, SPP ER22-1697, PJM ER22-962/ER24-1803, and MISO ER22-1640. The explainer simplifies legally binding orders and tells readers to use the orders for exact requirements.

## N02 — OpenADR 3

URL: https://www.openadr.org/openadr-3-0
Tags: C3; C4 | T4; T5.
Status: specification/certification overview opened; package not downloaded.

OpenADR 3 is supplementary to, not a replacement for, 2.0a/b. The normative artifact is OpenAPI YAML; where documentation conflicts, YAML prevails. The public package includes YAML, Definitions covering models/enumerations/security, and a User Guide with illustrative program/event/report/endpoint exchanges. The official reference implementation is members-only. Certification is distinct from implementing the API: only products completing Alliance certification can claim certified/compliant status. The page lists Continuous Pricing VEN and Baseline VEN profiles as available, while EVSE/Inverter Management profiles are examples not yet defined on the page. VENs may implement selected profiles; VTN certification has broader functionality requirements and transition rules involving 2.0b plus 3. Final verification uses Alliance-appointed test houses. This is an interoperability standard and certification framework, not a market tariff or authority to control utility equipment.

## N03 — IEEE 1547-2018

URL: https://standards.ieee.org/ieee/1547/5915/
Tags: C2; C3; C4 | T4; T5.
Status: public standard abstract/status opened; full paid text not accessed. Foundational.

The standard concerns DER interconnection/interoperability with electric power systems, including performance, operations, testing, safety, maintenance, abnormal conditions, power quality, and islanding. It applies across synchronous machines, induction machines, and inverter/converter DER at typical primary/secondary distribution voltages, with emphasis on radial systems while considering networks. It assumes a 60 Hz source. Published 6 April 2018; the page lists it as active and identifies amendment 1547a-2020, which changes allowed trip-clearing-time ranges for Category III abnormal operation. Public metadata does not expose numerical ride-through curves, exact settings, testing clauses, or a complete communications implementation. IEEE 1547 is not itself a pure-load scheduling API and should not be described as requiring every compute server to export power. Applicability arises through the interconnected DER equipment and governing adoption requirements.

## N04 — DOE Distribution Grid Orchestration

URL: https://www.energy.gov/documents/distribution-grid-orchestration
Tags: C2; C3; C4 | T4; T5.
Status: substantial report text opened. Dated: November 2024.

The report classifies orchestration into dispatch-signal, autonomous, and behavioral mechanisms. Dispatch can be centralized or decentralized and price-based or control-based. Autonomous control can use fixed parameters, periodic engineering updates, or dynamic real-time constraints. Interfaces may be direct utility-to-device, one intermediary, or aggregator plus manufacturer. It distinguishes grid-wide economics from local thermal/voltage constraints on service transformers, laterals, and main feeders. Examples include MIDAS/CalFUSE pricing, SCE RATES transactive pilots, Duke OpenFMB peer-to-peer controls, inverter Volt-Watt/Volt-VAr functions, and SCE localized autonomous/communications-based load control. Relevant standards include OpenADR and IEEE 2030.5. It discusses maturity and failures such as connectivity, secure data exchange, and insufficient modeling of distribution constraints. It is an architecture/taxonomy report, not a deployable DERMS package or evidence that one global carbon signal protects every local feeder.

## N05 — DOE i2X DER Interconnection Roadmap

URL: https://www.energy.gov/sites/default/files/2025-01/i2X%20DER%20Interconnection%20Roadmap.pdf
Tags: C2; C3; C4 | T2; T4; T6.
Status: substantial PDF text, executive summary, solution inventory, targets opened. Published: 16 January 2025.

Scope is distribution/subtransmission generation/storage/hybrids, generally below 100 kV and below 80 MW; conventional DR/efficiency are not a focus because they often do not require DER interconnection. Four goals cover transparency/security, process timelines, economic efficiency, and reliability. Specific mechanisms include standardized data/hosting capacity, commercial-readiness criteria, automation, group studies, flexible export limits, cost allocation, nameplate-versus-export distinctions, EMT modeling, protection, and cybersecurity. Targets for 2030—systems not triggering upgrades—include median agreement times within one business day below 50 kW, under 75 days for 50 kW–5 MW, and under 140 days above 5 MW. These are aspirational roadmap targets, not current legal deadlines or observed performance. The report explicitly frames solutions as contextual/non-prescriptive and distinguishes generation interconnection from demand-service questions.

## N06 — ETSI Edge-Native Design

Announcement: https://www.etsi.org/newsroom/press-releases/2250-new-etsi-white-paper-on-mec-support-for-edge-native-design-an-application-developer-perspective/
Detailed paper: https://www.etsi.org/images/files/ETSIWhitePapers/ETSI-WP55-MEC_support_towards_Edge_native.pdf
Tags: C1; C4 | T1; T5.
Status: announcement and substantial White Paper 55 text opened. June 2023.

The paper directly addresses small/distributed edge constraints: limited single-server/rack resources, heterogeneity, intermittent upstream connectivity, user mobility, privacy, latency, and cross-site resilience. It distinguishes customer premises, access/RAN, core, and distributed-cloud placement. Applications may need GPU/CPU-specific capabilities and dynamic relocation while maintaining QoS. Detailed standards links include MEC 021 Application Mobility Service and MEC 011 discovery/registration; AMS provides adjacent-instance endpoints, target-instance identification, communication-link information, mobility-status notification, and cleanup assistance. It explicitly says actual context-transfer procedures depend on deployment/OS/virtualization and are outside portions of MEC scope. Use cases include enterprise/private 5G, V2X perception, media, drones, and real-time AI translation. This explains compute/network orchestration requirements, not utility dispatch, electric-capacity maps, or a universal latency threshold.

## N07 — ETSI MEC Security

URL: https://www.etsi.org/newsroom/press-releases/2123-2022-09-etsi-publishes-a-new-white-paper-on-multi-access-edge-computing-security/
Tags: C1; C4 | T2; T5.
Status: announcement opened; underlying full security white paper not opened. Published: 26 September 2022.

The second-edition announcement identifies MEC federation, infrastructure/physical protection, data protection, user security, network-layer security, and application-layer security. Its key technical distinction is an edge ecosystem with multiple hardware/software vendors, operators, suppliers, and stakeholders, where conventional centralized-cloud controls may not cover the complete trust chain. It emphasizes third-party component integrity and end-to-end security across all participating entities. Standards families mentioned include ETSI MEC, ETSI CYBER, NFV, and 3GPP SA3, plus potentially applicable cybersecurity regulation. The page does not expose threat matrices, normative security controls, a conformance suite, or a field-measured security result. It establishes the existence and scope of the paper, not certification of a particular edge platform or permission to exchange customer data across jurisdictions.

# 6. Additional sources previously cited outside the 67-row master catalogue

These records cover supporting sources used in earlier tables, glossary, caveats, and key numbers. They are separate from—not replacements for—the master IDs.

## A01 — Google ML power/thermal smoothing

URL: https://cloud.google.com/blog/topics/systems/mitigating-power-and-thermal-fluctuations-in-ml-infrastructure
Tags: C3 | T5.
Status: full article opened. 11 February 2025.

Google describes synchronized ML clusters exhibiting tens-of-MW swings, repeating every few seconds over prolonged runs. Its compiler detects workload signatures such as synchronization flags and redistributes TPU compute-block activity to smooth power. One test shows nearly 50% lower fluctuation magnitude and temperature swings reduced from approximately 20°C to 10°C, with under 1% performance impact and small increases in average power. This last point is important: smoothing can consume slightly more average energy while improving power quality/reliability. No public fleet trace, complete test matrix, or portable open-source implementation is provided in the article.

## A02 — ERCOT April 2026 legislative update

URL: https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf
Tags: C2; C3 | T1; T2; T6.
Status: presentation opened.

As of 26 March 2026, ERCOT tracked approximately 410 GW of large-load requests, approximately 87% data centers. Its separate generation queue had 2,008 active requests totaling 453,562 MW as of 28 February. The presentation explains repeated single-project restudies can invalidate earlier results when nearby requests arrive; proposed batching groups requests approximately every six months and reserves allocated capacity. It presents target dates, proposed rules, and pending portal development—not proof those later milestones occurred. A proposed $50,000/MW security/interconnection-fee framework is explicitly attached to a March proposal. The source differentiates requested load, generation supply, rules already effective, and rules still proposed.

## A03 — MISO generation/load study alignment

URL: https://www.misoenergy.org/engage/MISO-Dashboard/generation-and-large-load-alignment/
Tags: C2 | T2; T6.
Status: dashboard opened; last modified 31 July 2026.

Initiative LLWG-2026-6, titled Load Addition Resource Study, proposes aligning large-load studies with generation serving those loads. Stated purposes are consistent assumptions, fewer timing mismatches, and optimized network upgrades while preserving reliability. Status is active; the page lists the Large Load Working Group. It did not expose supporting issue documents or FERC orders in the retrieved response. It is evidence of a proposal under development, not proof an effective tariff already grants a combined generation-plus-load fast track.

## A04 — MISO LMR/DR enrollment FAQ

URL: https://help.misoenergy.org/knowledgebase/article/KA-01560/en-us
Tags: C3; C4 | T4; T6.
Status: detailed FAQ opened.

Minimums: LMR 0.1 MW per asset/component; DRR 1 MW per grouping; EDR 0.1 MW. Eligible certified participants include LSEs, retail-customer aggregators, and end users. Nonresidential aggregate assets require address/account/meter IDs; assets at least 5 MW require EPNode data. LES supports template/CSV bulk import/export but explicitly no API. LES opening for LMR-DR/DRR is 1 December 2026, after the research cutoff; planning-year deadlines are separately listed. The FAQ describes 2–6-hour notification, events typically up to four hours, and up to 16 annual dispatches. These statements supplement controlling tariff/BPM rules; they must not be conflated with all MISO reserve or energy products.

## A05 — CEC reliability-reserve docket and measured VPP data

URL: https://efiling.energy.ca.gov/Lists/DocketLog.aspx?docketnumber=22-RENEW-01
Tags: C3; C4 | T3; T6.
Status: docket index opened; underlying workbooks not downloaded.

The docket is unusually specific about available empirical artifacts. TN269155 describes anonymized 2025 storage-VPP data with three sheets: data dictionary, monthly site-aggregated performance, and hourly site discharge, covering six months. TN266632 describes an analogous 2024 workbook. TN269649 is the adopted Fifth Edition clean guidelines, 88 pages; TN269650 is the 96-page strikeout. TN269692 gives 2025 Option 3/4 enrolled capacity by district/county. The index also includes event-data filings and confidentiality requests; not every filing is publicly downloadable or equally authoritative. This is a source of real distributed-storage performance, not necessarily compute-site participation.

## A06 — FERC Energy Primer

URL: https://www.ferc.gov/sites/default/files/2024-01/24_Energy-Markets-Primer_0117_DIGITAL_0.pdf
Tags: C2; C3; C4 | T4.
Status: contents/introduction and portions of PDF opened; not every glossary passage re-extracted.

The 2024-branded handbook is dated December 2023 internally and explains physical/financial natural gas, electricity, gas–electric interactions, and market manipulation. Electricity sections begin around p.34; RTO/ISO markets p.66; PJM p.83; MISO p.87; CAISO p.94. It is vocabulary and market-structure context, not a current tariff. The front matter explicitly says it is staff analysis, not binding on the Commission. Regional product rules and market dates can become stale even while definitions remain useful.

## A07 — DOE Future of Resource Adequacy

URL: https://www.energy.gov/sites/default/files/2024-04/2024%20The%20Future%20of%20Resource%20Adequacy%20Report.pdf
Tags: C2; C3; C4 | T4; T6.
Status: substantial PDF opened. April 2024.

The report distinguishes nameplate capacity from capacity credit: dependable contribution depends on timing, weather, duration, outages, and the rest of the system's portfolio. It discusses correlated thermal/fuel failures, storage duration, transmission sharing, demand response, DERMS/ADMS, and VPPs. This establishes why an equal number of MW is not necessarily an equal reliability service. The report cites BIL/IRA financing and tax programs as understood in April 2024; those policy descriptions are not verified current November 2026 eligibility. It is not a siting-capacity inventory or proof that a given battery/compute portfolio receives a particular accredited capacity value.

## A08 — DOE Distribution Grid Code Adoption Pathways

URL: https://www.energy.gov/sites/default/files/2024-07/48726_DOE_OE_TDC_Distribution_Grid_Codes_Pathways_RELEASE_508.pdf
Tags: C2; C4 | T4; T5.
Status: substantial PDF opened. June 2024.

The report expands “grid codes” beyond device engineering to institutional, business, and technical processes. Its taxonomy separates code families, functional elements, components, and associated standards/practices. Hosting-capacity publication requires choices about granularity, methodology, refresh, security, staffing, and validation. It cites five validation stages: input data, model, engineering analysis, results, publication. Illustrative DER-penetration bands are up to 5%, 5–15%, and above 15% of peak load—not universal engineering limits. Seattle City Light and Eversource examples appear later in the document. This is a capability/adoption framework, not binding nationwide grid-code requirements.

## A09 — PG&E Redwood Coast Airport Microgrid final report

URL: https://www.pge.com/assets/pge/docs/about/corporate-responsibility-and-sustainability/pge-epic-project-3.11.pdf
Tags: C1; C2; C3; C4 | T2; T5; T6.
Status: substantial report opened. 21 December 2024.

The project combines a 2.3 MW/8.8 MWh battery, 2.2 MW DC-coupled PV, and separate 300 kW NEM PV; initially 19 customers averaged 175 kW and peaked at 360 kW. Commissioned 26 May 2022, it reports over 51 hours of incremental resilience across 12 events. PG&E controls distribution assets; RCEA controls generation, with explicit agreements defining the boundary. Wholesale operation reserves battery capacity for resilience. The report documents hardware-in-loop testing, nuisance islanding, protection/failsafe issues, charge/discharge sensitivity, and a fixed limited interconnection avoiding reconductoring. It is a measured community-microgrid example, not a compute-fleet deployment; its limited-interconnection case does not establish general flexible-service availability.

## A10 — Archived EIA transmission layer and failed HIFLD portal

URLs:
https://atlas.eia.gov/datasets/d4090758322c4d32a4cd002ffaa0aa12_0/about
https://hifld-geoplatform.opendata.arcgis.com/
Tags: C1; C2 | T3.
Status: earlier retrieval evidence only; not freshly reopened during the expanded inspection.

The first entry explicitly labels a transmission layer archived and unmaintained. The HIFLD legacy address previously returned a not-found page. Neither is evidence of a current nationwide download service. The earlier catalogue's live-layer lead D04 also failed direct retrieval in the expanded inspection. Current hosting, replacement datasets, field schemas, and licensing were not established; no substitute substation dataset is silently asserted.

## A11 — OpenFEMA dataset catalogue

URL: https://www.fema.gov/about/openfema/data-sets
Tags: C1 | T3.
Status: earlier search evidence; not freshly reopened during the expanded inspection.

The catalogue describes OpenFEMA's machine-readable dataset delivery and distinguishes available datasets/access arrangements. It was used to support the claim that the NRI product is file-oriented rather than automatically available through every OpenFEMA API function. No current API call, exact NRI endpoint, or complete catalogue audit was executed. The stronger verified source for NRI version, geography, formats, and download sizes is D18.

## A12 — GRIDAPPS-D IEEE 2030.5 repository listings

URLs: https://github.com/orgs/GRIDAPPSD/repositories
https://github.com/GRIDAPPSD
Tags: C3; C4 | T5.
Status: earlier repository-listing evidence; individual implementation not opened or built.

The listings identify Go components for IEEE 2030.5, including core/server/client/inverter-simulator-related work. They establish repository existence, not conformance, completeness, a usable release, specific license for every component, or a five-hour installation benchmark. The earlier catalogue correctly treated these as conditional implementation leads. They are not evidence that IEEE 2030.5 alone solves wholesale qualification or provides a compute workload scheduler.

## A13 — DOE IEEE 2030.5 presentation

URL: https://www.energy.gov/documents/seto-right-combination-webinar-hecopdf
Tags: C3; C4 | T4; T5.
Status: earlier extracted/search evidence only; not freshly reopened during the expanded inspection.

The presentation was used for IEEE 2030.5 vocabulary and smart-energy communication context. It is not the normative IEEE standard, a complete protocol implementation, or evidence of current utility certification requirements. Detailed message objects, security profiles, implementation settings, and performance limits were not independently reverified here. N04 supplies stronger freshly inspected discussion of IEEE 2030.5's role in grid-edge communications.

## A14 — DOE Sourcing DER for Distribution Services

URL: https://www.energy.gov/sites/default/files/2024-12/Sourcing%20DER%20for%20Dist%20Services%20final%2012.17.24.pdf
Additional version encountered: https://www.energy.gov/sites/default/files/2025-01/Sourcing%20DER%20for%20Dist%20Services%20final%201.9.24.pdf
Tags: C3; C4 | T4; T6.
Status: earlier extracted/search evidence; not freshly reopened during the expanded inspection.

The report addresses sourcing DER for local distribution needs and includes managed EV charging and other flexible resources. It was used for orchestration vocabulary and the distinction between distribution services and broad wholesale aggregation. No universal payment schedule, compute eligibility, or current procurement window was established from it. The separate January-hosted version encountered earlier may represent a revised artifact; identical wording/version should not be assumed without document comparison.

## A15 — Loudoun Phase 2 detail page

URL: https://www.loudoun.gov/6222/Phase-2-Data-Center-Standards-Locations
Tags: C1; C2 | T2; T6.
Status: earlier official-page evidence; not freshly reopened during the expanded inspection.

The page identifies Board approval of the Phase 2 project plan on 16 September 2025. The main page P01 independently confirms Phase 2 is underway and concerns new data-center/substation guidance and use-specific standards. Plan initiation is not final adoption of every proposed setback, noise rule, or location restriction. No precise future standard is represented as enacted solely from the project-plan date.

## A16 — FERC Order 2222 fact sheet

URL: https://www.ferc.gov/media/ferc-order-no-2222-fact-sheet
Tags: C3; C4 | T4; T6.
Status: earlier official-page evidence; not freshly reopened during the expanded inspection.

This supports the federal rule's aggregation-size provision: RTO/ISO minimum aggregation thresholds may be no greater than 100 kW. That is not a requirement that every device be 100 kW, nor a promise that all 100 kW compute loads qualify. The freshly inspected explainer N01 additionally establishes geographic, telemetry, utility-coordination, jurisdiction, and duplicate-compensation constraints.

## A17 — DOE announcement of LBNL consumption report

URL: https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
Tags: C2 | T1.
Status: earlier official announcement evidence; not freshly reopened during the expanded inspection.

The announcement communicates the report's headline values—176 TWh and 4.4% of US electricity in 2023, with 325–580 TWh/6.7–12% scenarios for 2028. It is an accessible summary, not independent confirmation using a second measurement method. The freshly inspected LBNL report R01 supplies methodology and uncertainty; using both citations does not create two independent datasets.

## A18 — ETSI MEC technical-group overview

URL: https://www.etsi.org/technical-groups/mec/
Tags: C1; C4 | T1; T4.
Status: earlier official overview evidence; not freshly reopened during the expanded inspection.

The overview defines MEC as cloud-computing capabilities and an IT service environment at the network edge. It was used for glossary-level meaning, not quantitative market size, latency guarantees, or power projections. N06's inspected paper adds the concrete constraints and application-mobility/discovery interfaces missing from a one-line definition.

## A19 — EIA wholesale-market overview

URL: https://www.eia.gov/electricity/wholesalemarkets/
Tags: C2; C4 | T4.
Status: earlier official overview evidence; not freshly reopened during the expanded inspection.

The page provides regional-market and operator context and links market information. It supports distinguishing ISO/RTO regions, not assuming all US utilities have the same capacity market, demand-response products, or DER-aggregation implementation. Detailed current participation requirements require the relevant tariff; the source is not itself a nationwide program-enrollment API.

## A20 — Commercial mobile-edge-computing forecast

URL: https://www.globenewswire.com/news-release/2026/11/04/3395444/0/en/Mobile-Edge-Computing-Market-Size-Share-Industry-Trends-and-Growth-Forecasts-2026-2031-5G-Edge-AI-and-Asia-Pacific-Demand-Fuel-30-1-CAGR-to-3-88-Billion.html
Tags: C1 | T1.
Status: earlier commercial press-release search evidence; full methodology not inspected.

The quoted commercial forecast is USD 0.80 billion in 2025, USD 1.04 billion in 2026, and USD 3.88 billion in 2031, with 30.1% CAGR. These numbers remain unverified. The market being valued is mobile edge computing as defined by that publisher, not necessarily physical edge-data-center buildings, electrical MW, colocation revenue, or all AI inference. The earlier response intentionally flagged rather than endorsed these figures. No primary public edge-only electricity series was established.

# 7. Remaining verification gaps

- D04 transmission GIS: current metadata, schema, license, and working download/service URL were not retrieved.
- D11 FCC: the nationwide download interface was blocked; only the official program description was inspectable.
- S12 WattTime: technical API documentation failed; signal definitions were verified through the official overview.
- D06 LBNL: the general landing page was incomplete in extraction, but the 2026 edition successfully resolved the substantive dataset/version/license questions. Source: https://emp.lbl.gov/publications/queued-2026-edition-characteristics
- Long PDFs: the inspection covered substantial text and contents, not every page, appendix, figure, linked workbook, or underlying proprietary input.
- APIs/software: no authenticated API requests, live utility controls, software installations, simulation benchmarks, or conformance tests were executed.
- Program eligibility: CAISO/ERCOT/MISO pages establish participation structures; site-specific qualification and binding obligations still reside in tariffs, agreements, technical requirements, and approved registrations.
- Source freshness: rolling repositories and portals expose retrieved content; a preserved historical snapshot for every page as of the cutoff was not independently archived.

# End of handoff
