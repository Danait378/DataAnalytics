-- a) The name of the table that holds the items Northwind sells is Products.
-- b) The name of the table that holds the types/categories of the items Northwind sells is Categories.
SELECT * FROM employees;
 SELECT * FROM employees;
-- The Northwind employee whose name makes it look like she’s a bird is Nancy Davolio.
SELECT * FROM products;
-- This query returns 77 records.
-- To retrieve only 10 rows, change the Limit setting in the toolbar at the top of the query editor to 10.

-- You can limit rows using:
-- SELECT * FROM products LIMIT 10;
-- Source: MySQL documentation (SELECT LIMIT clause)
SELECT * FROM categories;
-- The category ID of Seafood is 8.
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
