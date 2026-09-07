-- SQL Server schema (versão de referência)

CREATE TABLE fact_exchange_rates (
    [date] DATE NOT NULL,
    currency VARCHAR(10) NOT NULL,
    pair VARCHAR(20) NOT NULL,
    high DECIMAL(12,4),
    low DECIMAL(12,4),
    bid DECIMAL(12,4),
    ask DECIMAL(12,4),
    [close] DECIMAL(12,4),
    spread DECIMAL(12,4),
    volume BIGINT,
    [year] INT,
    [month] INT,
    year_month CHAR(7),
    source VARCHAR(100),
    CONSTRAINT UQ_exchange_date_currency UNIQUE ([date], currency)
);
