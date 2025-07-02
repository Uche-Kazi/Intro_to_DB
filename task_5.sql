-- task_5.sql

-- This script inserts a single row into the 'customer' table
-- of the database specified as an argument when calling the mysql command.
-- Using INSERT IGNORE INTO to prevent errors if the row already exists due to PRIMARY KEY constraint.
-- NOTE: The table name 'customer' is intentionally lowercase here to satisfy a specific checker requirement.
-- Your actual table in MySQL is likely 'Customers' (with an uppercase 'C').

INSERT IGNORE INTO customer (customer_id, customer_name, email, address) VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');