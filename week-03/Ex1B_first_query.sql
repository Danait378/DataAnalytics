

USE Northwind;

SELECT * FROM actor; -- Retrieved 200 records

SELECT * FROM film; -- Retrieved 1000 records
-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM Products;
-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT 
    ProductID,
    ProductName,
    UnitPrice
FROM Products
WHERE UnitPrice <= 7.50;
-- 3. Products with no units in stock but 1 or more units on backorder
SELECT 
    ProductID,
    ProductName,
    UnitsInStock,
    UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0
  AND UnitsOnOrder >= 1;

-- 4. Category identification and seafood items

-- 4a. View categories table to see all product categories
SELECT * 
FROM Categories;

-- 4b. Products are linked to categories using CategoryID
-- List all seafood products
SELECT 
    p.ProductID,
    p.ProductName,
    c.CategoryName
FROM Products p
JOIN Categories c
    ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';

-- 5. Supplier identification and Tokyo Traders products

-- 5a. Find supplier ID for Tokyo Traders
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- 5b. Find all products supplied by Tokyo Traders
SELECT 
    ProductID,
    ProductName,
    UnitPrice,
    SupplierID
FROM Products
WHERE SupplierID = (
    SELECT SupplierID
    FROM Suppliers
    WHERE CompanyName = 'Tokyo Traders'
);
-- 6. Employee questions

-- 6a. Count total employees
SELECT COUNT(*) AS TotalEmployees
FROM Employees;

-- 6b. Employees with "Manager" in job title
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Title
FROM Employees
WHERE Title LIKE '%Manager%';
