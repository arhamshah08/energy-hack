[← Front page](../../README.md) &nbsp;·&nbsp; [Concepts](README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Load flow (power flow)

**Used most in:** [Track 2 Grid capacity](../../tracks/2-grid-capacity/README.md), also Tracks 1 and 3.

## 1. What it is

Load flow calculates the voltage at every node (bus) and the active power, reactive power and
current on every line and transformer of a network, for one steady-state operating condition.
It answers the basic grid question: **can this network carry this generation and demand within
its physical and regulatory limits?** Every grid connection offer for a large load, battery or
generator rests on load flow studies.

## 2. Inputs and outputs

| In | Out |
|---|---|
| Network topology: which buses connect to which | Voltage magnitude and angle at every bus |
| Impedance of every line and transformer | Active power (MW) on every branch |
| Transformer tap positions | Reactive power (MVAr) on every branch |
| Generation and demand at every bus | Losses (I²R heat in conductors and transformers) |
| Voltage set points of generators | Loading of each branch as % of its rating |

Each bus is one of three types:

| Bus type | Fixed | Solved for | Typical |
|---|---|---|---|
| Slack (reference) | Voltage magnitude and angle | P and Q | One large generator or the grid connection point; balances losses |
| PV | Active power P and voltage magnitude | Q and angle | Generators and inverters controlling voltage |
| PQ | Active power P and reactive power Q | Voltage magnitude and angle | Loads, including a data center |

## 3. How it is solved

| Method | What it does | When to use |
|---|---|---|
| AC power flow (Newton-Raphson) | Solves the full nonlinear equations iteratively | Voltage and reactive power matter; final checks |
| Fast decoupled | Approximation of Newton-Raphson that separates P-angle from Q-voltage | Large networks, faster iterations |
| DC power flow | Linear approximation: flat voltages, no reactive power, no losses | Fast screening of thermal limits across many cases; inside optimization loops |
| Optimal power flow (OPF) | Adds an objective, usually lowest cost, subject to network limits | Dispatch and pricing questions |
| Economic dispatch and unit commitment | Which units run and how much, hour by hour, and the resulting nodal prices | Market and operations questions (`ed-uc-simulator-web`) |
| Capacity expansion | What to build over years, then how to run it | Planning questions (`genx`, `pypsa`, `manta`; California in the browser: `pypsa-ca-app`) |
| Learned surrogate | Neural network trained to approximate AC power flow or OPF | Thousands of fast evaluations; check final answers with a real solver (`microsoft-gridsfm`) |

## 4. Limits it checks

| Limit | Typical value | Note |
|---|---|---|
| Voltage at customer service (US) | ANSI C84.1 Range A: ±5% of nominal | Range B (wider) is allowed briefly |
| Transmission planning voltage | Often 0.95 to 1.05 per unit normal, about 0.90 to 1.10 after an outage | Criteria vary by utility and region |
| Thermal rating | Normal and short-term emergency ratings per line and transformer | Ratings can vary with season and weather |
| N-1 | All limits must hold with any single element out of service | Run one load flow per contingency |

Other countries use different limits; for example, some European distribution codes allow ±10%
at medium voltage.

## 5. What load flow does not capture

Load flow is steady state. Questions about what happens in the milliseconds and seconds after a
change need other studies:

| Study | Question | Open resource |
|---|---|---|
| Short circuit / fault level | How much current flows in a fault, can breakers clear it | `pandapower` (short circuit module) |
| Transient stability | Do generators and inverters stay in step after a disturbance | `andes` |
| Electromagnetic transients (EMT) | Fast power electronics behaviour: converters, UPS, ride-through | `dc-emt-model` (data center UPS load in PSCAD) |
| Harmonics | Distortion from power electronics | Specialist tools |
| Time series (quasi-static) | Load flow repeated for every hour of a year | `pandapower` timeseries, `opendssdirect` |

The July 2026 Virginia event (`pjm-load-transfer-event-2026`), where nearly 4,000 MW of data
center load disconnected together, is a dynamic problem: load flow alone would not show it.

## 6. Why it matters for grid-friendly compute

| # | Use |
|---|---|
| 1 | **Hosting capacity:** add MW at a bus until the first voltage or thermal violation |
| 2 | **Siting:** compare one large connection with the same load split across several buses |
| 3 | **Flexibility value:** see how many violations disappear if load drops in the binding hours |
| 4 | **Connection cost and curtailment:** violations drive network upgrades (cost) or limits on operation (curtailment), both of which flow into a project's finances |

## 7. Try it

In the browser, no install: draw a one-line diagram and run AC or DC load flow with the
[Load Flow Simulator](https://tool.adjiebrotots.com/loadflow-simulator/) by Adjie Brotosukmono (`loadflow-simulator-web`).
Or [AC Grid Lab](https://www.eshansingh.xyz/acopf/) by Dr. Eshan Singh (`ac-grid-lab`), which starts from a California-inspired nine-bus network.
For dispatch and prices: [ED/UC Simulator](https://tool.adjiebrotots.com/ed-uc-simulator/) by Adjie Brotosukmono (`ed-uc-simulator-web`).
For California-wide planning: [PyPSA California](https://www.eshansingh.xyz/PyPSA-CA/app/) by Dr. Eshan Singh (`pypsa-ca-app`).
All free tools, with credits: [open-source-tools](../../tools/README.md).

In Python, five lines:

```python
import pandapower as pp, pandapower.networks as pn
net = pn.case118()                                     # IEEE 118-bus test system
pp.create_load(net, bus=50, p_mw=100, q_mvar=20)        # add a 100 MW data center
pp.runpp(net)                                          # AC power flow
print(net.res_bus.vm_pu.min(), net.res_line.loading_percent.max())
```

Larger, map-based networks: `tamu-activsg10k`. Distribution feeders: `opendssdirect`.
Other solvers: `matpower`, `pypsa`, `powermodels`, and from LF Energy `lfe-powsybl` and `lfe-power-grid-model`.
