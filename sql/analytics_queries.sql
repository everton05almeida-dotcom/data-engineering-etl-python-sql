-- Consultas analíticas

-- 1. Cotação média mensal
SELECT
    year_month,
    currency,
    AVG([close]) AS avg_close
FROM fact_exchange_rates
GROUP BY year_month, currency
ORDER BY year_month, currency;

-- 2. Maior e menor cotação por moeda
SELECT
    currency,
    MIN([close]) AS min_close,
    MAX([close]) AS max_close,
    AVG([close]) AS avg_close
FROM fact_exchange_rates
GROUP BY currency;

-- 3. Spread médio
SELECT
    currency,
    AVG(spread) AS avg_spread
FROM fact_exchange_rates
GROUP BY currency
ORDER BY avg_spread DESC;

-- 4. Variação diária
WITH cte AS (
    SELECT
        [date],
        currency,
        [close],
        LAG([close]) OVER (PARTITION BY currency ORDER BY [date]) AS previous_close
    FROM fact_exchange_rates
)
SELECT
    [date],
    currency,
    [close],
    previous_close,
    CASE
        WHEN previous_close IS NULL OR previous_close = 0 THEN NULL
        ELSE ([close] - previous_close) / previous_close
    END AS daily_change_pct
FROM cte
ORDER BY currency, [date];
