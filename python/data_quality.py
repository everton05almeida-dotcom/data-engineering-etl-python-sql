from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT = BASE_DIR / "data" / "processed" / "exchange_rates_clean.csv"

df = pd.read_csv(INPUT)

checks = {
    "linhas": len(df),
    "nulos_criticos": int(df[["date","currency","close"]].isna().sum().sum()),
    "duplicados_data_moeda": int(df.duplicated(["date","currency"]).sum()),
    "moedas": int(df["currency"].nunique()),
}

print("DATA QUALITY CHECKS")
for key, value in checks.items():
    print(f"- {key}: {value}")

if checks["nulos_criticos"] > 0 or checks["duplicados_data_moeda"] > 0:
    raise SystemExit("Falha nos testes de qualidade.")

print("Qualidade aprovada.")
