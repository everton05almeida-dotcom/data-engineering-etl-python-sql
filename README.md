# ⚙️ Data Engineering — Pipeline ETL com Python + API + SQL

Projeto de portfólio voltado para **Engenharia de Dados**, demonstrando um pipeline ETL
com arquitetura em camadas, validação de qualidade, armazenamento SQL e preparação para BI.

> Os dados históricos incluídos no repositório são **sintéticos** e seguem uma estrutura
> compatível com uma API pública de cotações. O projeto também inclui um modo opcional para
> consulta de API em tempo de execução.

## 🎯 Objetivo

Construir um fluxo automatizado capaz de:

1. extrair dados de uma fonte JSON/API;
2. preservar a camada **Raw**;
3. limpar e padronizar os dados com **Python + Pandas**;
4. executar testes de **qualidade de dados**;
5. carregar os dados em um banco **SQLite**;
6. gerar uma camada **Curated** para consumo analítico;
7. disponibilizar consultas **SQL** e estrutura para **Power BI**.

## 🛠️ Tecnologias

- Python
- Pandas
- Requests
- REST API
- JSON
- SQL
- SQLite
- SQL Server (schema de referência)
- ETL
- Data Quality
- Power BI
- Git / GitHub

## 🏗️ Arquitetura

`API/JSON → Raw → Python/Pandas → Data Quality → Processed → SQL → Curated → Power BI`

Veja o desenho completo em `docs/arquitetura.md`.

## 📁 Estrutura

```text
data/
├── raw/
├── processed/
└── curated/

python/
├── extract.py
├── transform.py
├── data_quality.py
├── load_sqlite.py
├── curate.py
└── run_pipeline.py

sql/
├── schema_sql_server.sql
└── analytics_queries.sql

docs/
└── arquitetura.md

powerbi/
└── COMO_MONTAR_POWER_BI.md

database/
outputs/
Pipeline_ETL_Monitor.xlsx
```

## ▶️ Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o pipeline completo:

```bash
python python/run_pipeline.py
```

Para testar a extração opcional via API pública:

```bash
python python/extract.py --api
```

## ✅ Qualidade de Dados

O pipeline verifica:

- campos críticos nulos;
- duplicidades por data + moeda;
- quantidade de moedas;
- quantidade de registros processados.

Em caso de falha nos testes críticos, a execução é interrompida.

## 🗃️ Camadas

### Raw
Mantém a resposta original em JSON.

### Processed
Dados tratados, tipados, deduplicados e padronizados.

### Curated
Agregações mensais preparadas para dashboards e análises.

## 📊 Monitoramento

`Pipeline_ETL_Monitor.xlsx` apresenta:

- volume processado;
- quantidade de moedas;
- meses processados;
- resultado dos testes de qualidade;
- evolução mensal das cotações;
- resumo das camadas do pipeline.

## 💡 Competências demonstradas

Este projeto foi criado para demonstrar conhecimentos introdutórios/práticos em:

- Engenharia de Dados
- construção de pipelines
- ETL
- ingestão via API/JSON
- modelagem de camadas
- qualidade de dados
- Python para dados
- banco de dados e SQL
- preparação de dados para Business Intelligence

## 🚀 Evoluções futuras

- Docker
- PostgreSQL
- Apache Airflow
- Azure Data Factory
- Databricks / Spark
- armazenamento em cloud
- CI/CD para pipelines
