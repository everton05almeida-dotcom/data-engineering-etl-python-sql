"""
Extração de cotações.

Modo padrão:
- lê um JSON local compatível com a estrutura de uma API de câmbio.

Modo opcional:
- se --api for usado, tenta consultar a AwesomeAPI.
"""

from pathlib import Path
import argparse
import json
import requests

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"

def extract_local():
    path = RAW_DIR / "exchange_rates_api_sample.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def extract_api(pairs=("USD-BRL", "EUR-BRL", "GBP-BRL")):
    records = []
    for pair in pairs:
        url = f"https://economia.awesomeapi.com.br/json/daily/{pair}/30"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        payload = response.json()
        for item in payload:
            item["pair"] = pair
            records.append(item)
    output = RAW_DIR / "exchange_rates_api_live.json"
    with output.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return records

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api", action="store_true", help="Tenta consultar a API pública")
    args = parser.parse_args()
    data = extract_api() if args.api else extract_local()
    print(f"Extração concluída: {len(data)} registros")
