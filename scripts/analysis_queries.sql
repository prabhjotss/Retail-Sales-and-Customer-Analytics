-- Monthly revenue
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Customer Lifetime Value (CLV)
SELECT c.customer_id,
       c.customer_name,
       SUM(s.quantity * s.price) AS lifetime_value
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
GROUP BY c.customer_id
ORDER BY lifetime_value DESC;
