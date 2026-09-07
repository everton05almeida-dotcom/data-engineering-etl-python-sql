# Power BI — roteiro

Use preferencialmente `data/curated/exchange_rates_monthly.csv` para uma visão executiva e
`data/processed/exchange_rates_clean.csv` para detalhamento diário.

## Página 1 — Visão Executiva
- Cotação atual / última observação
- Cotação média
- Máxima e mínima
- Spread médio
- Série temporal por moeda

## Página 2 — Comparação de Moedas
- USD x EUR x GBP
- média mensal
- variação percentual
- volume

## Página 3 — Qualidade / Pipeline
- número de registros
- período processado
- moedas disponíveis
- status dos testes de qualidade

## DAX sugerido

```DAX
Cotação Média = AVERAGE(exchange_rates_clean[close])

Cotação Máxima = MAX(exchange_rates_clean[close])

Cotação Mínima = MIN(exchange_rates_clean[close])

Spread Médio = AVERAGE(exchange_rates_clean[spread])

Variação % =
VAR Atual = [Cotação Média]
VAR Anterior =
    CALCULATE(
        [Cotação Média],
        DATEADD(Calendario[Data], -1, MONTH)
    )
RETURN DIVIDE(Atual - Anterior, Anterior, 0)
```
