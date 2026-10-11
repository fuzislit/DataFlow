# DataFlow — Retail Sales Analytics Pipeline

## Overview

DataFlow is an end-to-end data analytics project built to practice data engineering and analytics workflows. It transforms raw retail transaction data into structured analytical models and a Tableau dashboard.

The project uses Python for data cleaning, Snowflake for cloud data warehousing, dbt for SQL transformations and testing, and Tableau for visualization.

## Tech Stack

- **Python & Pandas** — Data exploration and cleaning
- **Snowflake** — Cloud data warehouse
- **SQL** — Data transformations and analysis
- **dbt** — Staging models, analytical models, and data tests
- **Tableau** — Interactive sales dashboard

## Pipeline Architecture

1. **Data Source:** Online Retail II dataset from the UCI Machine Learning Repository.
2. **Data Cleaning:** Python and Pandas remove duplicate records and invalid price entries while preserving return transactions.
3. **Data Warehouse:** The cleaned dataset is loaded into a raw table in Snowflake.
4. **Staging:** A dbt staging view standardizes column names and calculates transaction-line revenue.
5. **Analytics Models:** dbt models aggregate monthly revenue and product-level sales metrics.
6. **Visualization:** Tableau presents key performance indicators, monthly revenue trends, and top products by revenue.

## Data Cleaning

The original worksheet contained 525,461 rows. After cleaning, 514,912 rows remained.

Cleaning steps included:
- Removing exact duplicate records.
- Removing zero-price entries and three negative-price adjustment records.
- Retaining negative quantities to preserve returns and cancellations.
- Retaining records with missing customer IDs for overall sales analysis.

## dbt Models

| Model | Purpose |
|---|---|
| `stg_online_retail` | Standardizes source columns and calculates line revenue |
| `monthly_revenue` | Aggregates net revenue and distinct invoices by month |
| `product_sales` | Aggregates product quantities, net revenue, and invoice counts |

The product sales model excludes `DOT` and `POST` from product rankings.

## Dashboard

The Tableau dashboard includes:
- Total net revenue
- Total distinct invoices
- Total distinct customers
- Monthly revenue trend
- Top 10 products by revenue
- Key business insights

## Project Structure

```text
dataFlow/
├── dataflow_analytics/
│   └── models/
│       ├── staging/
│       └── marts/
├── python/
├── sql/
├── requirements.txt
└── README.md
```

## Purpose

This project was built as a hands-on learning exercise to develop practical skills in data cleaning, cloud data warehousing, SQL-based transformations, data testing, and analytics visualization.