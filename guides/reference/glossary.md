[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Glossary: flexibility, DERMS, interconnection, edge

Plain definitions. Terms with a source are from the deep research run
([catalog/research/edge-compute](../../catalog/research/edge-compute/README.md)); others are general usage.

## 1. Edge and data centers

| # | Term | Meaning | Source |
|---|---|---|---|
| 1 | Edge data center | Small facility near users or data sources to cut latency, often kW to a few MW. No standard definition | general |
| 2 | MEC | Multi-access edge computing: cloud capabilities and an IT service environment at the network edge | https://www.etsi.org/technical-groups/mec/ |
| 3 | Hyperscale data center | Very large facility (often 100 MW+) run by a cloud or AI company | general |
| 4 | Power usage effectiveness (PUE) | Total facility energy divided by IT equipment energy | https://datacenters.lbl.gov/publications/avoiding-waste-heat-through-ai |
| 5 | Water usage effectiveness (WUE) | Annual onsite water use divided by IT energy, L/kWh-IT | https://datacenters.lbl.gov/sites/default/files/2023-07/DOE%20AM%20Tool--User%27s%20Manual%20v3.1%20%287-25-2023%29.pdf |
| 6 | Power capping | Limiting IT or facility power to an explicit maximum | https://www.energy.gov/sites/default/files/2024-08/Powering%20AI%20and%20Data%20Center%20Infrastructure%20Recommendations%20July%202024.pdf |
| 7 | Temporal workload shifting | Moving a compute job to a different time with the same result | https://eta.lbl.gov/publications/integrating-ai-data-centers-power |
| 8 | Geographic workload shifting | Moving computation between sites or regions based on grid supply, price or carbon | https://eta.lbl.gov/publications/integrating-ai-data-centers-power |
| 9 | Voltage ride-through | Ability of equipment or load to stay connected through voltage disturbances instead of tripping | https://www.ercot.com/services/comm/mkt_notices/M-B062325-01 |
| 10 | Thermal energy storage | Storing heating or cooling so thermal demand can shift in time | https://www.energy.gov/oe/articles/microgrids-large-electric-loads-grid-support-how-leverage-microgrids-support-utilities |

## 2. Grid capacity and interconnection

| # | Term | Meaning | Source |
|---|---|---|---|
| 11 | Hosting capacity | Generation or load a grid location can take without significant upgrades or violations | https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-user-guide.pdf |
| 12 | Integration Capacity Analysis (ICA) | California term for distribution hosting capacity analysis | same as above |
| 13 | Load ICA | Load a distribution line section can accept without significant upgrades | same as above |
| 14 | Limited generation profile | Time-varying export limit based on available hosting capacity | https://marketplace.sdge.com/more-information/customer-generation/enhanced-integration-capacity-analysis-ica |
| 15 | Flexible interconnection | Connection where injection or withdrawal can be limited dynamically instead of guaranteed firm | https://www.pge.com/assets/pge/docs/about/doing-business-with-pge/pge-grip-user-guide.pdf |
| 16 | Firm service | Service planned to meet a set load without routine curtailment for lack of network capacity | https://www.misoenergy.org/engage/MISO-Dashboard/firm-service-step-up-for-large-load-interconnections/ |
| 17 | Non-firm service | Service whose usable capacity may be restricted under defined grid conditions | same as above |
| 18 | Interconnection queue | List of projects waiting for grid connection studies; PJM has none for loads | https://insidelines.pjm.com/pjm-kicks-off-annual-process-of-vetting-large-load-requests/ |
| 19 | Large load | Load above a threshold that triggers special interconnection rules (ERCOT: 25 MW and up) | https://www.ercot.com/mktrules/issues/NPRR1234 |
| 20 | Load forecast | Estimate of future consumption or peak used for planning and procurement | https://learn.pjm.com/three-priorities/planning-for-the-future/load-forecasting |
| 21 | Local capacity requirement | Minimum capacity needed inside a constrained local transmission area | https://stakeholdercenter.prod.caiso.com/RecurringStakeholderProcesses/Local-capacity-requirements-process-2027 |
| 22 | Resource adequacy | Capacity procured so enough resources serve expected demand | https://www.caiso.com/generation-transmission/resource-adequacy |
| 23 | Capacity credit | Dependable share of nameplate capacity at times of need; equal MW is not equal reliability | https://www.energy.gov/sites/default/files/2024-04/2024%20The%20Future%20of%20Resource%20Adequacy%20Report.pdf |
| 24 | Feeder | Distribution line from a substation to customers | general |
| 25 | Substation | Facility that changes voltage between transmission and distribution | general |
| 26 | ISO / RTO | Operator of the wholesale market and grid in a region (CAISO, ERCOT, PJM, MISO) | https://www.eia.gov/electricity/wholesalemarkets/ |
| 27 | Balancing authority | Entity balancing supply and demand in an area; EIA-930 reports by BA | https://www.eia.gov/electricity/930-content/about.html |
| 28 | LMP | Locational marginal price: wholesale price at a grid node | general |
| 29 | Capacity market | Market for commitments that enough future capacity will be available | https://insidelines.pjm.com/pjm-stakeholders-advance-initiatives-to-reliably-integrate-data-centers/ |
| 30 | Ancillary services | Services keeping the grid stable: regulation, reserves, frequency response | https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy |

## 3. Flexibility and DERMS

| # | Term | Meaning | Source |
|---|---|---|---|
| 31 | DER | Small resource on the distribution system or behind a meter: storage, generation, responsive load | https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy |
| 32 | DER aggregation | Many DERs coordinated to provide a grid or market service together | same as above |
| 33 | DER aggregator | Entity that organizes DERs for participation in an RTO/ISO market | same as above |
| 34 | DERMS | Software that monitors, coordinates and can control DERs across a distribution grid | https://www.energy.gov/nepa/articles/cx-270851-alabama-power-company-distributed-energy-resources-management-system-derms |
| 35 | ADMS | Advanced distribution management system: utility operations, models and control | https://www.energy.gov/nepa/articles/cx-031615-adms-and-derms-initiative |
| 36 | VPP | Coordinated portfolio of distributed resources operated as one grid resource | https://www.energy.gov/technologycommercialization/articles/us-department-energy-releases-new-reports-highlighting |
| 37 | Demand response | Change in consumption in response to grid, price or program signals | https://www.energy.gov/cmei/femp/federal-demand-flexibility |
| 38 | Demand flexibility | Ability to shed, shift or modulate consumption | https://bies.lbl.gov/demand-flexibility |
| 39 | Load shedding | Temporarily reducing demand without moving it to another time | same as above |
| 40 | Load shifting | Moving consumption from one time to another | same as above |
| 41 | Load modulation | Repeatedly adjusting demand up or down rather than one shed event | same as above |
| 42 | Curtailable load | Demand that can be contractually reduced under set conditions | https://www.pge.com/en/save-energy-and-money/energy-saving-programs/demand-response-programs/business-programs.html |
| 43 | Proxy Demand Resource (PDR) | CAISO model letting aggregated demand reductions bid into the market | https://www.caiso.com/generation-transmission/load/demand-response |
| 44 | Reliability Demand Response Resource | CAISO DR resource dispatched for reliability | same as above |
| 45 | DER Provider (DERP) | CAISO participant operating a DER aggregation in wholesale markets | https://www.caiso.com/generation-transmission/generation/distributed-energy-resources |
| 46 | Behind-the-meter | On the customer side of the utility meter | https://stakeholdercenter.caiso.com/InitiativeDocuments/Straw-Proposal-and-Issue-Paper-Demand-and-Distributed-Energy-Market-Integration-Mar-13-2026.pdf |
| 47 | Carbon intensity | Emissions per unit of electricity, average or marginal | general |
| 48 | Marginal emissions (MOER) | Emissions from the generator that responds to the next unit of demand | https://watttime.org/data-science/data-signals/ |

## 4. Standards and rules

| # | Term | Meaning | Source |
|---|---|---|---|
| 49 | FERC Order 2222 | Requires organized US markets to accept DER aggregations (minimum size up to 100 kW). Not ERCOT | https://www.ferc.gov/ferc-order-no-2222-explainer-facilitating-participation-electricity-markets-distributed-energy |
| 50 | OpenADR | Open standard for automated DR, price and grid-event signals | https://www.openadr.org/ |
| 51 | VTN | OpenADR Virtual Top Node: publishes programs and events | https://www.openadr.org/openadr-3-0 |
| 52 | VEN | OpenADR Virtual End Node: receives and responds to signals | same as above |
| 53 | IEEE 2030.5 | RESTful Smart Energy Profile for utility-to-device communication and DER control | https://standards.ieee.org/ieee/2030.5/11216/ |
| 54 | IEEE 1547 | Standard for DER interconnection and interoperability on distribution grids | https://standards.ieee.org/ieee/1547/5915/ |
| 55 | PMU | Phasor measurement unit: synchronized measurement of phasors and frequency | https://www.misoenergy.org/engage/MISO-Dashboard/operational-reliability-requirement---large-load-telemetry-and-phasor-measurement-unit-pmu-requirements/ |
| 56 | ICCP | Inter-Control Center Communications Protocol for real-time telemetry between control centers | same as above |
