[← Front page](../../README.md) &nbsp;·&nbsp; [Concepts](README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Grid-forming inverters and microgrid control

**Used most in:** [Track 3 Load management](../../tracks/3-load-management/README.md) and
[Track 4 Aggregation](../../tracks/4-aggregation/README.md); also ride-through questions in Track 2.

## 1. Why it matters here

Data centers increasingly sit behind batteries, UPS systems and onsite generation (IEA projects
20 to 25 GW of batteries at data centers by 2030, `iea-key-questions-2026`). All of these connect
through inverters. How those inverters are controlled decides whether a site can run as an
island, share load between sources, ride through grid disturbances, and help the grid instead of
tripping off with everyone else.

## 2. Grid-following vs grid-forming

| | Grid-following (GFL) | Grid-forming (GFM) |
|---|---|---|
| Behaves like | A controlled current source | A controlled voltage source |
| Needs an existing grid voltage | Yes, it locks onto it with a phase-locked loop | No, it sets voltage and frequency itself |
| Can run an island alone | No | Yes |
| Response to disturbances | Follows the grid; can lose sync in weak grids | Resists change; can provide inertia-like support |
| Typical today | Most solar and battery inverters | Growing in batteries and microgrids |

## 3. Control hierarchy in an islanded microgrid

Several grid-forming inverters in parallel need a clear split between fast and slow control.

| Layer | Speed | Job |
|---|---|---|
| Primary (each inverter) | about 5 to 15 ms | Droop, virtual impedance, power filtering: share load autonomously and keep the system stable |
| Secondary (site controller) | about 50 to 300 ms | Measure V, f, P, Q at the common bus and slowly restore voltage and frequency to target |
| Tertiary (energy management) | seconds to hours | Dispatch, state of charge, tariffs, grid programs, reconnection |

**Bandwidth separation** is the key design rule: each layer must be much slower than the one
below it, so the site controller corrects real deviations without fighting the inverters.

## 4. The building blocks

**Droop control** lets parallel sources share load with no fast communication. Each inverter
lowers its frequency as its active power rises and lowers its voltage as its reactive power rises:

```
f = f_ref - n_f * P
V = V_ref - m_v * Q
```

Because all inverters see the same frequency, they settle where each carries power in inverse
proportion to its droop slope. The cost is a small, deliberate deviation in f and V, which the
secondary layer later removes.

**Virtual impedance** makes the inverter act as if it had a chosen output impedance. It improves
reactive power sharing, reduces circulating current between parallel inverters, lowers sensitivity
to unequal cable and transformer impedances, and adds damping. Droop sets the sharing rule;
virtual impedance makes the sharing behave well through the real network.

**Power filtering and virtual inertia.** Measured P and Q are filtered so droop does not chase
every transient, harmonic or measurement blip. Slowing the response this way also gives an
inertia-like behaviour: frequency changes more gently after a step in load. Virtual synchronous
machine (VSM) controls make this explicit by emulating a rotating machine's inertia and damping.

**Site controller.** Watches the common point (for example the medium-voltage bus) and nudges each
inverter's V_ref and f_ref to bring the system back to nominal, then hands over to energy
management for slower decisions.

The goal, in order: stable sharing, controlled transient response, coordinated restoration,
robust steady state.

## 5. Links to data center loads

| # | Point | Source id |
|---|---|---|
| 1 | AI training swings tens of MW within seconds; inverters and storage can smooth it | `google-power-smoothing-2025` |
| 2 | Large loads tripping together is a reliability risk; ride-through behaviour depends on UPS and converter controls | `pjm-load-transfer-event-2026`, `ercot-ride-through-notice` |
| 3 | A data center's UPS and converters can be modelled in EMT to study grid interactions | `dc-emt-model` |
| 4 | Open grid-forming controls now exist for large electronic loads such as data centers, not only for generators | `openibr` |
| 5 | A measured community microgrid: battery, PV, islanding events, controls lessons | `pge-redwood-microgrid` |

## 6. Simulate it

| Tool | Level | Id |
|---|---|---|
| Dynawo (LF Energy) | Power system dynamics with power-electronic resources | `lfe-dynawo` |
| OpenIBR | Open grid-forming controller for inverters and large electronic loads; TB958 DLLs for PSCAD (Heron Power) | `openibr` |
| ANDES (Python) | Phasor-domain transient stability, including inverter-based resource models | `andes` |
| PSCAD data center model | EMT, data center UPS and converters (commercial PSCAD) | `dc-emt-model` |
| HELICS | Couple a grid simulator with a control or compute simulator | `helics` |
| pandapower | Steady-state check of the microgrid network | `pandapower` |
| NRGISE Open | Time-step simulation of a site's PV, storage and control strategy | `nrgise-open` |
| BESS dispatch optimizer | Battery schedule under changing grid export limits | `bess-flexible-dispatch` |
