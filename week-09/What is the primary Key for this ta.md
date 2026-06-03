What is the primary Key for this table?



&#x20;                                      Primary Key                       Parent table

&#x20;

Categories                             Category ID                       None



customers                              customer ID                       None                                               



employees                             Employee ID                        None



employee territories               Employee ID and Territory ID          Employees, Territories

&#x20;                                

order detail                       order ID and product ID               orders, products



orders                            order ID                                customers,employees



products                          product ID                              categories,suppliers



region                            Region ID                               None



shippers                          shippers ID                             None



supplies                          Supplies ID                             None



territories                       territories ID                          Region





Table: Customers





Column: Customer ID



&#x20;This column stores a unique ID for each customer.

It is the primary key for the table.

&#x20;It is not a foreign key.

&#x20;This would be useful in Power BI because it helps identify customers.

&#x20;The name makes sense and does not need to be changed.

&#x20;Data type: Text.

&#x20;It could be used to count the number of customers.



Column: Company Name



&#x20;This column stores the name of the customer's company.

&#x20;It is not part of the primary key.

&#x20;It is not a foreign key.

&#x20;This would be useful in Power BI because it helps identify customers by name.

&#x20;The name is clear and easy to understand.

&#x20;Data type: Text.

It could be used to group or filter customer data.



Table: Products



Column: Product ID



&#x20;This column stores a unique ID for each product.

It is the primary key for the table.

&#x20;It is not a foreign key.

This would be useful in Power BI because it helps identify products.

&#x20;The name is appropriate.

Data type: Whole Number.

&#x20;It could be used to count products.



Column: Category ID



&#x20;This column shows which category a product belongs to.

&#x20;It is not part of the primary key.

&#x20;It is a foreign key

&#x20;This would be useful in Power BI because it helps organize products by category.

&#x20;The name is appropriate.

Data type: Whole Number.

It could be used in reports that compare product categories.









&#x20;                          



