-- Check the top 10 stock codes by net revenue.
-- This helps validate the dbt product_sales model.


SELECT *
FROM DATAFLOW_DB.DBT_DEV.PRODUCT_SALES
ORDER BY NET_REVENUE DESC
LIMIT 10;
