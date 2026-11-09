[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# Materials for energy

> Search for battery, catalyst and solar materials with simulation in the loop. (event statement)

| Sub-area | Query |
|---|---|
| All | `python3 scripts/find.py --domain materials` |
| Verifiers (simulators) | `python3 scripts/find.py --domain materials --role verifier` |
| Batteries | `python3 scripts/find.py --domain materials battery` |

## Loop components

| Loop part | Batteries | Catalysts | Solar | General crystals |
|---|---|---|---|---|
| Data | `matr-battery`, `battery-archive`, `nasa-pcoe`, `materials-project` (electrodes) | `open-catalyst`, `catalysis-hub` | `perovskite-database`, `jarvis` | `materials-project`, `oqmd`, `aflow`, `alexandria`, `omat24`, `gnome` |
| Verifier | `pybamm` (cell-level), ML potentials | `fairchem` | `jarvis` tools | `mace`, `chgnet`, `mattersim`, `orb-models` via `ase` |
| Metric | Cycle life, capacity fade | Adsorption energy error | `nrel-cell-efficiency` (records) | `matbench-discovery`, energy above hull |
| Proposer | | | | `mattergen` |
| Analysis | `pymatgen` | `pymatgen` | `pymatgen` | `pymatgen` |

## Facts

| # | Fact | Source id |
|---|---|---|
| 1 | Cycle life can be predicted from the first 100 cycles on the Severson dataset | `severson-2019` |
| 2 | Closed-loop Bayesian optimization with early prediction cut fast-charge protocol search from an estimated 500 days to 16 | `attia-2020` |
| 3 | GNoME reported 2.2M new crystals, 381k on the convex hull, via an ML plus DFT active-learning loop | `gnome-2023` |
| 4 | Autonomous lab A-Lab reported 41 of 58 targets in 17 days; the claims were later disputed | `a-lab-2023` |
| 5 | Universal ML potentials give near-DFT energies in seconds on a laptop for small cells | `mace`, `chgnet` |

## Setup notes

| # | Item | Note |
|---|---|---|
| 1 | Materials Project | Free API key, sign in at the site |
| 2 | ML potentials | `pip install mace-torch` / `chgnet`; CPU works for small systems |
| 3 | PyBaMM | `pip install pybamm`; no GPU needed |
| 4 | DFT | Too slow for a 5-hour loop at scale; most loops use ML potentials as the verifier |
