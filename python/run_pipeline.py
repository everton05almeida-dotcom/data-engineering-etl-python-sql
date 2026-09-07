import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

steps = [
    "extract.py",
    "transform.py",
    "data_quality.py",
    "load_sqlite.py",
    "curate.py",
]

for step in steps:
    print(f"\n>>> Executando {step}")
    subprocess.run([sys.executable, str(HERE / step)], check=True)

print("\nPipeline ETL executado com sucesso.")
