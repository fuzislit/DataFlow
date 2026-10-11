
SELECT
"Invoice" AS invoice,
"StockCode" AS stock_code,
"Description" AS description,
"Quantity" AS quantity,
"InvoiceDate" AS invoice_date,
"Price" AS price,
"Customer ID" AS customer_id,
"Country" AS country,
"Quantity" * "Price" AS line_revenue
FROM {{ source('raw', 'online_retail') }}
