-- a script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your MySQL server.
-- The database name will be passed as an argument of the mysql command
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table';
