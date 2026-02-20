-- CUSTOMER DIMENSION
INSERT INTO warehouse.customer_dim (customer_name)
SELECT DISTINCT customer_name
FROM staging.orders_raw
ON CONFLICT DO NOTHING;

-- PRODUCT DIMENSION
INSERT INTO warehouse.product_dim (product_name)
SELECT DISTINCT product_name
FROM staging.orders_raw
ON CONFLICT DO NOTHING;

-- DATE DIMENSION
INSERT INTO warehouse.date_dim
SELECT DISTINCT
order_date,
EXTRACT(YEAR FROM order_date),
EXTRACT(MONTH FROM order_date),
EXTRACT(DAY FROM order_date)
FROM staging.orders_raw
ON CONFLICT DO NOTHING;

-- FACT TABLE
INSERT INTO warehouse.sales_fact
SELECT
s.order_id,
s.order_date,
c.customer_id,
p.product_id,
s.quantity,
s.quantity * s.price
FROM staging.orders_raw s
JOIN warehouse.customer_dim c
ON s.customer_name = c.customer_name
JOIN warehouse.product_dim p
ON s.product_name = p.product_name
ON CONFLICT DO NOTHING;

-- REFRESH ANALYTICS TABLE
TRUNCATE analytics.monthly_sales;

INSERT INTO analytics.monthly_sales
SELECT
d.year,
d.month,
SUM(f.total_amount) AS revenue
FROM warehouse.sales_fact f
JOIN warehouse.date_dim d
ON f.date_id = d.date_id
GROUP BY d.year, d.month;
