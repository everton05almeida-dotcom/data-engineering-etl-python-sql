# Arquitetura do Pipeline

```text
        FONTE / API REST
              |
              v
      +----------------+
      |   RAW / JSON   |
      +----------------+
              |
        Python Extract
              |
              v
      +----------------+
      | TRANSFORMAÇÃO  |
      | Pandas / ETL   |
      +----------------+
              |
       Data Quality
              |
              v
      +----------------+
      | PROCESSED CSV  |
      +----------------+
          |         |
          v         v
      SQLite     CURATED
          |         |
          +----+----+
               |
               v
        Power BI / SQL
               |
               v
        Dashboard / KPIs
```

## Conceitos demonstrados

- ingestão de dados
- camadas Raw / Processed / Curated
- ETL
- validação de qualidade
- banco relacional
- SQL analítico
- automação do pipeline
- consumo por ferramenta de BI
