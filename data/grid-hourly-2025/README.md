[← Front page](../../README.md) &nbsp;·&nbsp; [Feedback form](https://forms.gle/k1pnQ4dtvfcGkuGK6)

# US grid demand and generation, hourly, 2025

Hourly demand and generation by fuel for the 12 largest US grid operators (balancing authorities),
for all of 2025. Cleaned from US EIA Form 930, ready to load in one line. Public domain (US government data).

| File | Size | Contents |
|---|---|---|
| [us_grid_hourly_2025.csv](us_grid_hourly_2025.csv) | 13.8 MB, 105,120 rows | One row per operator per hour |
| [us_grid_summary_2025.csv](us_grid_summary_2025.csv) | 2 KB | One row per operator: annual demand, peak, generation mix |

## Load it

```python
import pandas as pd
url = "https://raw.githubusercontent.com/arhamshah08/energy-hack/main/data/grid-hourly-2025/us_grid_hourly_2025.csv"
df = pd.read_csv(url, parse_dates=["utc_time_end"])
ercot = df[df.ba == "ERCO"]                       # one operator
ercot.plot(x="utc_time_end", y=["demand_mw", "solar_mw", "wind_mw"])
```

## Operators included

| Code | Operator | Region |
|---|---|---|
| CISO | California ISO (CAISO) | California |
| ERCO | ERCOT | Texas |
| PJM | PJM Interconnection | Mid-Atlantic and Midwest |
| MISO | Midcontinent ISO | Midwest |
| NYIS | New York ISO | New York |
| ISNE | ISO New England | New England |
| SWPP | Southwest Power Pool | Central |
| BPAT | Bonneville Power Administration | Northwest |
| DUK | Duke Energy Carolinas | Carolinas |
| SOCO | Southern Company | Southeast |
| TVA | Tennessee Valley Authority | Tennessee |
| FPL | Florida Power & Light | Florida |

## Columns (hourly file)

| Column | Meaning |
|---|---|
| `ba`, `ba_name`, `region` | Operator code, name, EIA region |
| `utc_time_end`, `local_time_end` | End of the hour, UTC and local (values are hourly averages, hour-ending) |
| `demand_forecast_mw` | Operator's day-ahead demand forecast |
| `demand_mw` | Demand (EIA adjusted series) |
| `net_generation_mw` | Total net generation (adjusted) |
| `interchange_mw` | Net flow out of the area; negative means importing |
| `coal_mw` ... `unknown_mw` | Net generation by source (adjusted). `solar_mw` and `wind_mw` include units with integrated batteries; `battery_mw` is stand-alone storage (negative when charging) |

## 2025 at a glance (from the summary file)

| Operator | Demand (TWh) | Peak (MW) | Largest sources |
|---|---|---|---|
| PJM | 843 | 160,560 | Gas 42%, nuclear 31%, coal 17% |
| MISO | 664 | 120,343 | Gas 35%, coal 29%, wind 15% |
| ERCOT | 487 | 83,597 | Gas 41%, wind 23%, solar 14% |
| SPP | 300 | 54,411 | Wind 37%, coal 29%, gas 25% |
| CAISO | 224 | 43,860 | Gas 40%, solar 25%, hydro 11% |

## Things to know

| # | Note |
|---|---|
| 1 | Operator areas are balancing authorities, not states; some utilities inside a state run their own area |
| 2 | "Adjusted" values are EIA's cleaned series, with some gaps filled by imputation |
| 3 | Battery storage is reported as its own source from 2025 |
| 4 | No prices or emissions in this file; prices: `gridstatus-io`, emissions: `epa-egrid` |
| 5 | Other operators and years: EIA bulk files at https://www.eia.gov/electricity/gridmonitor/ (`eia-930`) |

Rebuild: `scripts/data/make_grid_dataset.py`. Source: U.S. Energy Information Administration, Form EIA-930.
