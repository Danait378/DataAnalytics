USE northwind;

-- 1. List product id, product name, unit price, and category name of all products.
-- Order by category name, then product name.
SELECT 

    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName
FROM Products p
JOIN Categories c 
    ON p.CategoryID = c.CategoryID
ORDER BY 
    c.CategoryName,
    p.ProductName;

-- 2. List product id, product name, unit price, and supplier name for products costing more than $75.
-- Order by product name.
SELECT 

    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Suppliers s 
    ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice > 75
ORDER BY p.ProductName;
-- 3. List product id, product name, unit price, category name, and supplier name of every product.
-- Order by product name.
SELECT 

    p.ProductID,
    p.ProductName,
    p.UnitPrice,
    c.CategoryName,
    s.CompanyName AS SupplierName
FROM Products p
JOIN Categories c 
    ON p.CategoryID = c.CategoryID
JOIN Suppliers s 
    ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

-- 4. List order id, ship name, ship address, and shipping company name for orders shipped to Germany.
-- Alias shipping company name as 'Shipper'. Order by shipper then ship name.
SELECT 
    o.OrderID,
    o.ShipName,
    o.ShipAddress,
    sh.CompanyName AS Shipper
FROM Orders o
JOIN Shippers sh 
    ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY 
    sh.CompanyName,
    o.ShipName;

-- 5. Same as #4, but remove OrderID and group by ship name with count of orders per ship name.
SELECT 
    o.ShipName,
    o.ShipAddress,
    sh.CompanyName AS Shipper,
    COUNT(o.OrderID) AS OrderCount
FROM Orders o
JOIN Shippers sh 
    ON o.ShipVia = sh.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY 
    o.ShipName,
    o.ShipAddress,
    sh.CompanyName
ORDER BY 
    sh.CompanyName,
    o.ShipName;
    
    -- 6. List order id, order date, ship name, and ship address for all orders that included Sasquatch Ale.
-- (Requires 3 tables, including Order Details table with backticks due to space)
SELECT 
    o.OrderID,
    o.OrderDate,
    o.ShipName,
    o.ShipAddress
FROM Orders o
JOIN `Order Details` od 
    ON o.OrderID = od.OrderID
JOIN Products p 
    ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';

