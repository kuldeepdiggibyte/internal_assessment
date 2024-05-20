SELECT customer_id
FROM customers_sales
GROUP BY customer_id
HAVING COUNT(customer_id)>1  