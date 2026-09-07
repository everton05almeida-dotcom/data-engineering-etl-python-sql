from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = BASE_DIR / "data" / "processed" / "exchange_rates_clean.csv"
DB_PATH = BASE_DIR / "database" / "exchange_rates.db"

df = pd.read_csv(CSV_PATH)

with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("fact_exchange_rates", conn, if_exists="replace", index=False)

print(f"Carga concluída em: {DB_PATH}")
print(f"Linhas carregadas: {len(df)}")
