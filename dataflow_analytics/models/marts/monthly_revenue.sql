SELECT
DATE_TRUNC('MONTH', invoice_date) AS sales_month,
SUM(line_revenue) AS net_revenue,
COUNT(DISTINCT invoice) AS transaction_count
FROM {{ ref('stg_online_retail') }}
GROUP BY DATE_TRUNC('MONTH', invoice_date)