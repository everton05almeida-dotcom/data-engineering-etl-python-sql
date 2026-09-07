from pathlib import Path
import json
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW = BASE_DIR / "data" / "raw" / "exchange_rates_api_sample.json"
OUT = BASE_DIR / "data" / "processed" / "exchange_rates_clean.csv"

with RAW.open("r", encoding="utf-8") as f:
    records = json.load(f)

df = pd.DataFrame(records)

for col in ["high", "low", "bid", "ask", "close", "volume"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["date"] = pd.to_datetime(df["create_date"].str[:10], errors="coerce")
df["currency"] = df["code"]
df["spread"] = (df["ask"] - df["bid"]).round(4)
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["year_month"] = df["date"].dt.to_period("M").astype(str)
df["source"] = "AwesomeAPI-compatible sample"

cols = [
    "date","currency","pair","high","low","bid","ask","close","spread",
    "volume","year","month","year_month","source"
]
df = df[cols].dropna(subset=["date","currency","close"])
df = df.drop_duplicates(subset=["date","currency"])
df = df.sort_values(["currency","date"])

df.to_csv(OUT, index=False, encoding="utf-8-sig")
print(f"Transformação concluída: {len(df)} registros")
