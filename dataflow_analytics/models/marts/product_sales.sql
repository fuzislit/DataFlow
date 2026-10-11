SELECT
stock_code,
SUM(quantity) AS total_quantity_sold,
SUM(line_revenue) AS net_revenue,
COUNT(DISTINCT invoice) AS transaction_count
FROM {{ ref('stg_online_retail') }}
WHERE stock_code NOT IN ('DOT', 'POST')
GROUP BY stock_code