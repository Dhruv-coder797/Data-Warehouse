-- CREATE SCHEMAS
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS warehouse;
CREATE SCHEMA IF NOT EXISTS analytics;

-- STAGING TABLE
CREATE TABLE IF NOT EXISTS staging.orders_raw (
    order_id INT,
    order_date DATE,
    customer_name TEXT,
    product_name TEXT,
    quantity INT,
    price NUMERIC
);

-- DIMENSIONS
CREATE TABLE IF NOT EXISTS warehouse.customer_dim (
    customer_id SERIAL PRIMARY KEY,
    customer_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS warehouse.product_dim (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS warehouse.date_dim (
    date_id DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- FACT TABLE
CREATE TABLE IF NOT EXISTS warehouse.sales_fact (
    order_id INT PRIMARY KEY,
    date_id DATE,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount NUMERIC
);

-- ANALYTICS
CREATE TABLE IF NOT EXISTS analytics.monthly_sales (
    year INT,
    month INT,
    revenue NUMERIC
);
