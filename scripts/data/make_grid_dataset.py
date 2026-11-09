"""Build a cleaned hourly US grid dataset from EIA-930 balance files.

Usage:
  1. Download EIA930_BALANCE_2025_Jan_Jun.csv and EIA930_BALANCE_2025_Jul_Dec.csv from
     https://www.eia.gov/electricity/gridmonitor/sixMonthFiles/ into <raw_dir>, renamed to
     bal_2025_Jan_Jun.csv and bal_2025_Jul_Dec.csv
  2. python3 scripts/data/make_grid_dataset.py <raw_dir> data/grid-hourly-2025
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

raw, out = Path(sys.argv[1]), Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

BAS = {
    "CISO": "California ISO (CAISO)", "ERCO": "ERCOT (Texas)", "PJM": "PJM Interconnection",
    "MISO": "Midcontinent ISO (MISO)", "NYIS": "New York ISO (NYISO)", "ISNE": "ISO New England",
    "SWPP": "Southwest Power Pool (SPP)", "BPAT": "Bonneville Power Administration",
    "DUK": "Duke Energy Carolinas", "SOCO": "Southern Company", "TVA": "Tennessee Valley Authority",
    "FPL": "Florida Power & Light",
}

def num(v):
    v = (v or "").replace(",", "").strip()
    return float(v) if v else None

FUELS = [  # output name, source column indices (Adjusted), summed
    ("coal_mw", [48]), ("natural_gas_mw", [49]), ("nuclear_mw", [50]), ("petroleum_mw", [51]),
    ("hydro_mw", [52]), ("pumped_storage_mw", [53]), ("solar_mw", [54, 55]), ("wind_mw", [56, 57]),
    ("battery_mw", [58]), ("other_storage_mw", [59, 60]), ("geothermal_mw", [61]),
    ("other_mw", [62]), ("unknown_mw", [63]),
]
HEAD = ["ba", "ba_name", "region", "utc_time_end", "local_time_end", "demand_forecast_mw", "demand_mw",
        "net_generation_mw", "interchange_mw"] + [f for f, _ in FUELS]

rows = []
for f in sorted(raw.glob("bal_2025_*.csv")):
    with f.open(newline="") as fh:
        r = csv.reader(fh)
        next(r)
        for c in r:
            if c[0] not in BAS:
                continue
            utc = datetime.strptime(c[4], "%m/%d/%Y %I:%M:%S %p").strftime("%Y-%m-%dT%H:00:00Z")
            loc = datetime.strptime(c[3], "%m/%d/%Y %I:%M:%S %p").strftime("%Y-%m-%d %H:00")
            vals = {"demand_forecast_mw": num(c[5]), "demand_mw": num(c[13]),
                    "net_generation_mw": num(c[14]), "interchange_mw": num(c[15])}
            for name, idx in FUELS:
                parts = [num(c[i]) for i in idx if i < len(c)]
                parts = [p for p in parts if p is not None]
                vals[name] = sum(parts) if parts else None
            rows.append([c[0], BAS[c[0]], c[64] if len(c) > 64 else "", utc, loc] +
                        [("" if vals[h] is None else round(vals[h])) for h in HEAD[5:]])

rows.sort(key=lambda x: (x[0], x[3]))
with (out / "us_grid_hourly_2025.csv").open("w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(HEAD)
    w.writerows(rows)

# annual summary
summ = []
for ba, name in BAS.items():
    rr = [r for r in rows if r[0] == ba]
    dem = [r[6] for r in rr if r[6] != ""]
    gen = {f: sum(r[HEAD.index(f)] for r in rr if r[HEAD.index(f)] != "" and r[HEAD.index(f)] > 0) for f, _ in FUELS}
    tot = sum(gen.values()) or 1
    peak = max(rr, key=lambda r: r[6] if r[6] != "" else -1)
    summ.append([ba, name, rr[0][2], len(rr), round(sum(dem) / 1e6, 1), max(dem), peak[3], round(sum(dem) / len(dem))] +
                [round(100 * gen[f] / tot, 1) for f, _ in FUELS])
with (out / "us_grid_summary_2025.csv").open("w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["ba", "ba_name", "region", "hours", "demand_twh", "peak_demand_mw", "peak_hour_utc", "mean_demand_mw"] +
               [f.replace("_mw", "_share_pct") for f, _ in FUELS])
    w.writerows(summ)
print(len(rows), "hourly rows;", len(summ), "BAs")
