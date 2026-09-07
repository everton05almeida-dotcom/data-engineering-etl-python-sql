from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "data" / "processed" / "exchange_rates_clean.csv"
OUTPUT = BASE_DIR / "data" / "curated" / "exchange_rates_monthly.csv"

df = pd.read_csv(INPUT)

curated = (
    df.groupby(["year_month","currency"], as_index=False)
      .agg(
          avg_close=("close","mean"),
          min_close=("close","min"),
          max_close=("close","max"),
          avg_spread=("spread","mean"),
          total_volume=("volume","sum"),
          records=("close","size"),
      )
)

for col in ["avg_close","min_close","max_close","avg_spread"]:
    curated[col] = curated[col].round(4)

curated.to_csv(OUTPUT, index=False, encoding="utf-8-sig")
print(f"Camada curated gerada: {len(curated)} registros")
