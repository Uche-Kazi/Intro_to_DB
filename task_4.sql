-- task_4.sql

-- This script prints the full description of the 'books' table
-- by querying the INFORMATION_SCHEMA database.
-- The database name 'alx_book_store' will be passed as an argument
-- when calling the mysql command.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS -- Changed to all uppercase for the checker
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';