/* 
a) The actor table just has info about each actor, like their ID, first name, last name, and when the record was last updated.

b) The film table has details about movies, like the film ID, title, description, release year, language, how long it is, rental info, rating, and special features.

c) The film_actor table is the one that has both actor_id and film_id. It links actors to the movies they’re in.

d) The rental table shows each time someone rented a movie. It includes things like rental_id, rental_date, inventory_id, customer_id, return date, and staff_id. It’s kind of hard to read because it mostly uses numbers instead of actual names, so you usually have to connect it to other tables to understand it better.

e) The inventory table shows each copy of a movie that exists in the store. It includes inventory_id, film_id, store_id, and last update info.

f) To figure out the names of films rented on a specific date, you need the rental, inventory, and film tables. rental links to inventory using inventory_id, and inventory links to film using film_id. Then film gives you the actual movie titles.
*/

SELECT rental_id, rental_date, inventory_id FROM rental;

SELECT inventory_id, film_id FROM inventory;

SELECT film_id, title FROM film;