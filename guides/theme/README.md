[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Theme: grid-friendly compute

**Grid-friendly compute** connects and runs without pushing the grid past its limits, and helps
the grid when it can. In the sources in this repo that means five properties:

| # | Property | Track where it is worked on |
|---|---|---|
| 1 | Located where power and network capacity exist | [Track 1 Sites](../../tracks/1-sites/README.md) |
| 2 | Sized to the headroom the local grid actually has | [Track 2 Grid capacity](../../tracks/2-grid-capacity/README.md) |
| 3 | Able to reduce, shift or smooth its load when the grid is stressed | [Track 3 Load management](../../tracks/3-load-management/README.md) |
| 4 | Coordinated across many sites so it acts as one resource the grid can rely on | [Track 4 Aggregation](../../tracks/4-aggregation/README.md) |
| 5 | Stays connected through grid faults instead of tripping together | Tracks 2 and 3 (`pjm-load-transfer-event-2026`, `ercot-ride-through-notice`) |

## 1. Why it matters now

| # | Fact | Source id |
|---|---|---|
| 1 | US data centers used about 4.4% of US electricity in 2023; 9.5% to 15.3% projected for 2030 | `lbnl-dc-energy-2024`, `lbnl-dc-energy-2025-update` |
| 2 | ERCOT tracked about 410 GW of large-load requests in March 2026, about 87% data centers | `ercot-legislative-update-2026` |
| 3 | Data centers build in 2 to 3 years; grid infrastructure generally takes longer | `iea-energy-ai-2025` |
| 4 | Nearly 100 GW of new load could use existing US capacity if it accepts limited curtailment (first-order estimate) | `duke-rethinking-load-growth-2025` |
| 5 | Nearly 4,000 MW of data center load tripped offline together in Virginia on 22 Jul 2026 | `pjm-load-transfer-event-2026` |
| 6 | Synchronized AI training swings power by tens of MW within seconds | `google-power-smoothing-2025` |
| 7 | Public hosting capacity maps are screening estimates, not commitments | `pge-ica`, `sce-drpep` |
| 8 | No single percentage of data center load is flexible; it depends on workload deadlines, design and program rules | `lbnl-integrating-ai-dc` |

More numbers and contested claims: [catalog/research/edge-compute](../../catalog/research/edge-compute/README.md).

## 2. Angles on the theme

Examples, not a fixed list. Any approach that makes compute easier on the grid fits. Bring your own angle.

| # | Angle | What it covers | Starting resources |
|---|---|---|---|
| 1 | **Simulation and digital twins** | Check an idea in a model before touching hardware, including Omniverse twins of a data center and its grid | `nvidia-omniverse-dsx`, `pandapower`, `sustaindc`, `energyplus`, `tamu-activsg10k` |
| 2 | **RSI and self-improving agents** | Loops that propose, check, score, keep, and get better each run ([rsi.md](rsi.md)) | `aideml`, `openevolve`, `dspy` |
| 3 | **Coordination and signals** | Prices, carbon, grid events, protocols between grid and compute | `openadr`, `openleadr`, `electricity-maps` |
| 4 | **Edge AI workloads** | Inference at small sites: latency, deadlines, power behaviour | `azure-llm-inference-traces`, `etsi-edge-native-2023`, `coral-npu` |
| 5 | **Forecasting** | Load, renewables, weather, prices, failures ahead of time | `surge-load-forecast`, `timecopilot`, `pravah` (India, on request), `pjm-historical-forecasts`, `eia-930`, `buildingsbench` |
| 6 | **Storage and batteries** | Batteries at or near compute to shave peaks or ride through events | `nrgise-open`, `bess-flexible-dispatch`, `pybamm`, `cec-dsgs-docket` |
| 7 | **Onsite generation and microgrids** | Solar, gas, microgrids serving compute | `nrel-reopt`, `nrel-sam`, `pge-redwood-microgrid` |
| 8 | **Cooling, heat and water** | Cooling energy, waste heat, water use | `energyplus`, `lbnl-water-use-workloads`, `jrc-eu-coc-2024` |
| 9 | **Reliability and ride-through** | Staying connected through faults; avoiding mass trips | `pjm-load-transfer-event-2026`, `ercot-ride-through-notice` |
| 10 | **Markets, prices and programs** | Who pays for flexibility and how to qualify | `gridstatus-io` (LMPs across US ISOs), `flex-pse` (Stanford), `caiso-demand-response`, `ercot-ers`, `openei-urdb` |
| 11 | **Carbon awareness** | Running work when and where the grid is cleaner | `watttime`, `carbon-aware-sdk`, `epa-egrid` |
| 12 | **Speed to power: interconnection and permitting** | Getting connected and approved sooner: a permitting layer for the grid, vision models reading city permits, AI plans for faster approval ([ideas](../ideas/README.md)) | `ercot-batch-zero`, `miso-firm-service-step-up`, `loudoun-dc-standards`, `sf-property-information-map` |
| 13 | **Community, cost and equity** | Bills, noise, jobs, local acceptance | `va-jlarc-2024`, `census-reporter-api` |
| 14 | **Measurement and verification** | Proving what was delivered: telemetry, metering | `kepler`, `miso-telemetry-pmu`, `caiso-dmm-dr-2024` |
| 15 | **Resilience and hazards** | Outages, wildfire, flood exposure | `eagle-i-outages`, `fema-nri`, `cpuc-fire-threat-map` |
| 16 | **Security and trust at the edge** | Multi-vendor edge sites and data between grid and compute | `etsi-mec-security-2022` |
| 17 | **EV smart charging and vehicle-to-grid** | Charging that follows grid signals; parked vehicles exporting power ([concept](../concepts/ev-smart-charging-v2g.md)) | `acn-data`, `acnportal`, `everest`, `ocpp` |
| 18 | **Grid-forming control and microgrids** | Batteries and onsite sources that island, share load and ride through ([concept](../concepts/grid-forming-microgrids.md)) | `openibr`, `andes`, `dc-emt-model`, `pge-redwood-microgrid` |
| 19 | **Grid physics** | Load flow, dispatch, stability ([concept](../concepts/load-flow.md)) | `loadflow-simulator-web`, `ac-grid-lab`, `ed-uc-simulator-web`, `pypsa-ca-app`, `pandapower` |

Four of these have searchable tags: `python3 scripts/find.py --tag simulation` (also `rsi`, `coordination`, `edge-ai`).

## 3. Some angles by track

Examples of how a few angles show up in each track. Explanations of grid ideas: [concepts](../concepts/README.md).

| | Simulation | RSI loop shape | Coordination | Edge AI |
|---|---|---|---|---|
| **1 Sites** | Site energy and onsite generation: `nrel-reopt`, `nrel-sam`, `nrel-rev` | Propose candidate locations; score them against data layers | Zoning, permits, utility process: `loudoun-dc-standards`, `santa-clara-zoning` | Latency and network reach: `peeringdb`, `ripe-atlas`, `fcc-broadband-map` |
| **2 Grid capacity** | Power flow and N-1 on synthetic grids: `tamu-activsg10k`, `pandapower`, `matpower` | Propose placements or splits of load; power flow scores violations | Large-load processes: `ercot-batch-zero`, `miso-firm-service-step-up`, `pjm-large-load-vetting` | AI load shape assumptions: `eia-aeo2026-servers` (flat) vs `google-power-smoothing-2025` (swings) |
| **3 Load management** | Data center workload, cooling and battery sims: `sustaindc`, `vessim`, `energyplus` | Propose schedules or control policies; simulator scores cost, carbon, delayed jobs | Price, carbon and DR signals: `electricity-maps`, `watttime`, `pge-business-dr` | Inference traces and power telemetry: `azure-llm-inference-traces`, `kepler` |
| **4 Aggregation** | Multi-site coordination sims: `citylearn`, `helics`, `gridlab-d` | Propose dispatch across sites; simulator scores delivered vs committed MW | Protocols and markets: `openadr`, `ieee-2030-5`, `ferc-2222`, `caiso-der-provider` | Workload mobility across edge sites: `etsi-edge-native-2023` |

## 4. Tools for every track

<!-- BEGIN GENERATED -->

_Generated by `scripts/build.py`._

### Loop frameworks and benchmarks

| id | Resource | Access | Kind | Also in track | What it is |
|---|---|---|---|---|---|
| `aideml` | [AIDE (Weco AI)](https://github.com/WecoAI/aideml) | open | tool |  | Agent that iterates on ML code with a tree search over solutions, scored by a user-defined metric. |
| `lfe-ainetus` | [AINETUS](https://lfenergy.org/projects/ainetus/) | open | tool | 2 | AI for Safety-Critical Network Infrastructures: human-centric AI components that support grid operators' real-time and planning decisions. LF Energy stage: Sandbox. Code: github.com/ainetus. |
| `autoresearch` | [autoresearch (Andrej Karpathy)](https://github.com/karpathy/autoresearch) | open | tool |  | Minimal loop where an agent edits a training script, runs a short experiment, and keeps changes that improve a validation metric. |
| `dgm` | [Darwin Godel Machine](https://github.com/jennyzzt/dgm) | open | tool |  | Coding agent that edits its own code and keeps an archive of agent variants, scored on coding benchmarks. |
| `dspy` | [DSPy](https://github.com/stanfordnlp/dspy) | open | tool |  | Framework that optimizes LLM prompts and pipelines against a metric instead of hand-written prompts. |
| `lfe-energnn` | [EnerGNN](https://lfenergy.org/projects/energnn/) | open | tool | 2 | Graph neural network stack (H2MG) for amortized optimization: trained once on many grid cases, it returns near-instant solutions to new ones. LF Energy stage: Sandbox. Code: github.com/energnn/energnn. |
| `funsearch` | [FunSearch (Google DeepMind)](https://github.com/google-deepmind/funsearch) | open | tool |  | LLM proposes programs, an automated evaluator scores them, best programs are fed back. Released code for the Nature 2023 paper. |
| `gepa` | [GEPA](https://github.com/gepa-ai/gepa) | open | tool |  | Reflective prompt evolution: an LLM reads execution traces and rewrites prompts, keeping a Pareto set of candidates. |
| `helics` | [HELICS co-simulation framework](https://github.com/GMLC-TDC/HELICS) | open | tool | 2, 3, 4 | Couples separate simulators (grid, buildings, markets, comms) into one time-synchronized federation. Python bindings. Simulates nothing on its own. BSD-3. |
| `mattergen` | [MatterGen (Microsoft)](https://github.com/microsoft/mattergen) | open | tool |  | Diffusion model that generates crystal structures conditioned on target properties. |
| `mle-bench` | [MLE-bench (OpenAI)](https://github.com/openai/mle-bench) | open | benchmark |  | 75 Kaggle competitions used to measure how well agents do ML engineering. |
| `openevolve` | [OpenEvolve](https://github.com/codelion/openevolve) | open | tool |  | Open-source implementation of the AlphaEvolve pattern: an LLM mutates programs and an evaluator scores them across generations. |
| `lfe-opengridfm` | [OpenGridFM](https://lfenergy.org/projects/opengridfm/) | open | tool | 2 | Open framework for building and fine-tuning foundation models for power grids. LF Energy stage: Incubation. Code: github.com/gridfm. |
| `shinkaevolve` | [ShinkaEvolve (Sakana AI)](https://github.com/SakanaAI/ShinkaEvolve) | open | tool |  | Sample-efficient LLM-driven program evolution framework with novelty filtering and an archive of solutions. |
| `ai-scientist` | [The AI Scientist (Sakana AI)](https://github.com/SakanaAI/AI-Scientist) | open | tool |  | End-to-end loop that generates research ideas, runs experiments from templates and writes papers. |
| `timecopilot` | [TimeCopilot: agentic forecasting framework](https://github.com/TimeCopilot/timecopilot) | open | tool | 2, 3 | LLM agent over time-series foundation models: forecast, cross-validate and detect anomalies from natural-language requests through one API. MIT. |

### RSI papers

| id | Resource | Status | Also in track | What it is |
|---|---|---|---|---|
| `attia-2020` | [Attia et al., Closed-loop optimization of fast-charging protocols (Nature 2020)](https://www.nature.com/articles/s41586-020-1994-5) | verified |  | Bayesian optimization plus early cycle-life prediction found long-life fast-charge protocols in 16 days instead of an estimated 500. |
| `funsearch-2023` | [Romera-Paredes et al., Mathematical discoveries from program search with LLMs (Nature 2023)](https://www.nature.com/articles/s41586-023-06924-6) | verified |  | FunSearch: LLM proposes programs, evaluator scores them, best are recycled into prompts. New cap set constructions. |
| `a-lab-2023` | [Szymanski et al., An autonomous laboratory for the accelerated synthesis of novel materials (Nature 2023)](https://www.nature.com/articles/s41586-023-06734-w) | verified |  | Robotic lab with computational targets and active learning; 41 of 58 targets synthesized in 17 days. Claims later disputed in the literature. |
| `gepa-2025` | [Agrawal et al., GEPA: Reflective Prompt Evolution (2025)](https://arxiv.org/abs/2507.19457) | preprint |  | Prompt optimization by reflecting on traces; reports outperforming RL fine-tuning (GRPO) with fewer rollouts. |
| `autolab-2026` | [AutoLab: long-horizon closed-loop optimization benchmark (2026)](https://huggingface.co/papers/2606.05080) | preprint |  | 36 expert tasks across system optimization, model development and CUDA kernels. Finds sustained iteration matters more than first attempt. |
| `hyperagents-2026` | [Hyperagents (DGM-H), 2026](https://arxiv.org/abs/2603.19461) | preprint |  | Self-referential agents that can also edit their improvement procedure; reports gains outside coding. |
| `ai-scientist-2024` | [Lu et al., The AI Scientist (2024)](https://arxiv.org/abs/2408.06292) | preprint |  | Automated pipeline for idea generation, experiments, paper writing and automated review. |
| `alphaevolve-2025` | [Novikov et al., AlphaEvolve (Google DeepMind, 2025)](https://arxiv.org/abs/2506.13131) | preprint |  | LLM-driven evolutionary coding agent with automated evaluators; reported results in math, scheduling and kernel optimization. |
| `self-improving-coding-agent-2025` | [Robeyns et al., A Self-Improving Coding Agent (2025)](https://arxiv.org/abs/2504.15228) | preprint |  | Agent edits its own codebase between benchmark runs and keeps edits that raise scores. |
| `self-improvement-survey-2026` | [Self-Improvements in Modern Agentic Systems: A Survey (2026)](https://huggingface.co/papers/2607.13104) | preprint |  | Survey organizing self-improvement by which component changes (prompt, memory, tools, code, weights). |
| `reflexion-2023` | [Shinn et al., Reflexion (2023)](https://arxiv.org/abs/2303.11366) | preprint |  | Agents store verbal feedback from failed attempts in memory and use it on the next try, without weight updates. |
| `voyager-2023` | [Wang et al., Voyager (2023)](https://arxiv.org/abs/2305.16291) | preprint |  | LLM agent builds a growing library of verified code skills through self-verification. |
| `aide2-2026` | [Weco AI, AIDE2: outer-loop agent rewrites an inner-loop research agent (2026)](https://www.alphaxiv.org/abs/2609.26457) | preprint |  | Reports an outer agent improving the code of an inner research agent, with gains carrying to unseen domains. Preprint, Sept 2026. |
| `stop-2023` | [Zelikman et al., Self-Taught Optimizer (STOP) (2023)](https://arxiv.org/abs/2310.02304) | preprint |  | A scaffolding program that improves code is applied to improving itself. Early recursive scaffolding result. |
| `dgm-2025` | [Zhang et al., Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (2025)](https://arxiv.org/abs/2505.22954) | preprint |  | Coding agent rewrites its own code; archive-based open-ended search raised SWE-bench and Polyglot scores. |

<!-- END GENERATED -->
