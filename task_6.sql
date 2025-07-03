-- task_6.sql

-- This script inserts multiple rows into the 'Customers' table
-- of the database specified as an argument when calling the mysql command.
-- Using INSERT IGNORE INTO to prevent errors if rows with these IDs already exist.

INSERT IGNORE INTO Customers (customer_id, customer_name, email, address) VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');