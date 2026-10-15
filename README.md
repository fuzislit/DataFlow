# DataFlow — Retail Sales Analytics Pipeline

## Overview

DataFlow is an end-to-end data analytics project that transforms retail transaction data into structured analytical models and business insights. The project uses Python and Pandas for data cleaning, Snowflake for cloud data warehousing, dbt for SQL transformations and testing, and Tableau for visualization.

## Tech Stack

**Python · Pandas · SQL · Snowflake · dbt · Tableau**

## Pipeline

1. **Data Cleaning:** Cleaned and validated retail transaction records using Python and Pandas.
2. **Data Warehousing:** Loaded the processed dataset into Snowflake.
3. **Data Transformation:** Built dbt models to standardize data and calculate transaction-level revenue.
4. **Data Analysis:** Developed SQL models to analyze monthly revenue and product sales, with data quality tests.
5. **Visualization:** Created a Tableau dashboard to explore sales trends and product performance.

## Key Results

| Metric | Result |
|---|---:|
| Records processed after cleaning | 514,912 |
| Distinct invoices | 25,543 |
| Distinct customers | 4,381 |
| Distinct products | 4,264 |
| Net revenue | £9.64M |

## Dashboard

_Add a screenshot of your Tableau dashboard here._

## Data Cleaning

The original dataset contained 525,461 rows. After cleaning, 514,912 rows remained.

- Removed duplicate records.
- Removed zero-price entries and three negative-price adjustment records.
- Preserved negative quantities to account for returns and cancellations.
- Retained records with missing customer IDs for overall sales analysis.

## dbt Models

| Model | Purpose |
|---|---|
| `stg_online_retail` | Standardizes columns and calculates transaction-line revenue |
| `monthly_revenue` | Aggregates monthly net revenue and distinct invoices |
| `product_sales` | Aggregates product quantities, revenue, and invoice counts |

The product sales model excludes `DOT` and `POST` from product rankings.

## Data Source

[Online Retail II — UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
