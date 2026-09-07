"""Extração de cotações para o pipeline ETL.

Por padrão, gera uma amostra sintética reproduzível no formato de uma API de câmbio.
Com --api, consulta a AwesomeAPI e grava a resposta na camada Raw.
"""
from pathlib import Path
from datetime import datetime, timedelta
import argparse
import json
import math
import random
import requests

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_FILE = RAW_DIR / "exchange_rates_api_sample.json"


def generate_sample(days=90):
    random.seed(207)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    config = {"USD-BRL": (5.15, .22), "EUR-BRL": (5.62, .25), "GBP-BRL": (6.58, .30)}
    start = datetime(2025, 1, 1)
    records = []
    for pair, (base, amp) in config.items():
        for i in range(days):
            dt = start + timedelta(days=i)
            close = round(base * (1 + i * .00012) + math.sin(i/28)*amp*.18 + random.uniform(-amp*.10, amp*.10), 4)
            spread = random.uniform(.005, .035)
            bid = round(close - random.uniform(.001, .009), 4)
            ask = round(close + random.uniform(.001, .009), 4)
            records.append({
                "code": pair.split("-")[0], "codein": "BRL", "pair": pair,
                "name": f"{pair.split('-')[0]} / Real Brasileiro",
                "high": str(round(close + spread, 4)), "low": str(round(close - spread, 4)),
                "bid": str(bid), "ask": str(ask), "close": str(close),
                "volume": str(random.randint(1200, 9200)), "timestamp": str(int(dt.timestamp())),
                "create_date": dt.strftime("%Y-%m-%d 18:00:00")
            })
    with RAW_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return records


def extract_api(pairs=("USD-BRL", "EUR-BRL", "GBP-BRL")):
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    records = []
    for pair in pairs:
        url = f"https://economia.awesomeapi.com.br/json/daily/{pair}/30"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        for item in response.json():
            item["pair"] = pair
            records.append(item)
    with RAW_FILE.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", action="store_true", help="Consulta a API pública em vez da amostra sintética")
    args = parser.parse_args()
    data = extract_api() if args.api else generate_sample()
    print(f"Extração concluída: {len(data)} registros gravados em {RAW_FILE}")
