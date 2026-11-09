[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Grid and fusion

> Forecasting, control and plasma simulation, wherever an agent can propose something and a model
> can check it. (event statement)

| Sub-area | Query |
|---|---|
| All | `python3 scripts/find.py --domain grid-fusion` |
| Verifiers | `python3 scripts/find.py --domain grid-fusion --role verifier` |
| Benchmarks | `python3 scripts/find.py --domain grid-fusion --role metric` |

## Loop components

| Loop part | Grid forecasting | Grid control and planning | Fusion |
|---|---|---|---|
| Data | `eia-930`, `gridstatus`, `opsd`, `bdg2`, `comstock`, `resstock`, `era5`, `wind-toolkit`, `nsrdb` | `pudl`, `eia-860`, ISO portals | `fair-mast`, `the-well` (MHD sims) |
| Verifier | Held-out data | `pandapower`, `pypsa`, `grid2op`, `matpower`, `powermodels`, `opendssdirect`, `gridlab-d`, `citylearn` | `torax`, `freegs`, `freegsnke`, `openfusiontoolkit`, `plasmapy` |
| Metric | `buildingsbench` | `pglib-opf`, Grid2Op scores | Simulator outputs (confinement, stability) |

## Facts

| # | Fact | Source id |
|---|---|---|
| 1 | An RL controller trained in simulation shaped plasmas on the real TCV tokamak | `degrave-2022` |
| 2 | An RL controller on DIII-D avoided tearing instabilities in real time | `seo-2024` |
| 3 | TORAX is differentiable and written in JAX, built for use inside optimization loops | `torax-2024` |
| 4 | Grid2Op ran the L2RPN competitions where agents operate a grid through topology changes | `grid2op` |
| 5 | PGLib-OPF holds 3 to 30,000-bus OPF test cases used as a common benchmark | `pglib-2019` |

## Setup notes

| # | Item | Note |
|---|---|---|
| 1 | pandapower, pypsa, grid2op, torax, freegs | `pip install`; Python only |
| 2 | MATPOWER, PowerModels.jl | Need MATLAB/Octave or Julia |
| 3 | ERA5 | Free registration; downloads queue and can be slow |
| 4 | FAIR-MAST | Portal may be slow; see the GitHub repo for access paths |
