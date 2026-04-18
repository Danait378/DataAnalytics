Adding a Database from a Script
1. Add the Northwind database using the following steps:
a) Use the Notepad application on your computer to open Northwind_MySQL.sql from
the Week 2 student material.
b) Copy the full text of the script, and paste into a blank query in MySQL Workbench.
c) Run the query to create the Northwind database.
2. Refresh the Schemas panel to confirm that you have a new schema for northwind.
3. Create a script named Ex4C_northwind_extract.sql and save it to your week-02
folder.
4. Answer the following questions by studying the northwind schema. At the top of your
script, include comments with your answers (written as a complete sentence):
a) What is the name of the table that holds the items Northwind sells?
b) What is the name of the table that holds the types/categories of the items
Northwind sells?
5. Create a SELECT statement to retrieve all columns from the employees table.
a) Who is the Northwind employee whose name makes it look like she’s a bird?
Include the answer as a comment underneath the SELECT statement.
6. Create a SELECT statement to retrieve all columns from the products table.
a) How many records does your query return? Using the toolbar options at the top of
the query pane, how can you change your query to retrieve only 10 rows? Include
the answer as a comment underneath the SELECT statement.
b) BONUS: How could you write the query to limit the number of rows returned? This
isn’t covered in the Week 2 Student Guide, so if you tackle this bonus question,
you’ll need to do a little independent research. Add the answer as a comment in
your script with a note on what source you used to find the answer.
Year Up United Data Analyst Training Academy Week 2 Lab Workbook
Page 27 of 28
7. Create another SELECT statement to retrieve all columns from the categories table.
c) What is the category id of seafood? Include a comment in your script to answer
this.
8. Create a final SELECT statement to retrieve the top 50 records from orders, including
only the OrderID, OrderDate, ShipName, and ShipCountry columns.
a) Export the resulting record set to .csv format as Ex4C_order_sample.csv and save it
to week-02.
9. Save changes to Ex4C_northwind_extract.sql
10. Using Git Bash, commit and push your changes to week-02 to GitHub.
