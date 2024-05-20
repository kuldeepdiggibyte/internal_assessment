SELECT MONTH(order_date) AS month, YEAR(order_date) AS year, SUM(order_total) AS total_revenue
FROM orders_tbl
GROUP BY MONTH(order_date), YEAR(order_date) ORDER BY year, month;