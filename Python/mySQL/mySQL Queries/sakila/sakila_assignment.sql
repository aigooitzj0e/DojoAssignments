#1
-- SELECT customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- LEFT JOIN address ON customer.address_id = address.address_id
-- WHERE address.city_id = 312;

#2
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
-- FROM category
-- LEFT JOIN film_category ON category.category_id = film_category.category_id
-- LEFT JOIN film ON film_category.film_id = film.film_id
-- WHERE category.name = "comedy"

#3
-- SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
-- FROM film
-- LEFT JOIN film_actor ON film.film_id = film_actor.film_id
-- LEFT JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE actor.actor_id = 5

#4
-- SELECT customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- LEFT JOIN address on customer.address_id = address.address_id
-- WHERE customer.store_id = 1
-- AND address.city_id IN (1, 42, 312, 459)

#5
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features
-- FROM film
-- LEFT JOIN film_actor ON film_actor.film_id = film.film_id
-- WHERE film.rating = "G" 
-- AND film.special_features LIKE "%behind the scenes%"
-- AND actor_id = 15

#6
-- SELECT actor.first_name, actor.last_name, film.film_id, actor.actor_id
-- FROM actor
-- LEFT JOIN film_actor ON actor.actor_id = film_actor.actor_id
-- LEFT JOIN film ON film.film_id = film_actor.film_id
-- WHERE film_actor.film_id = 369;

#7
-- SELECT film.title, film.description, film.release_year, film.release_year, film.rating, film.special_features, category.name AS genre
-- FROM category
-- LEFT JOIN film_category ON category.category_id = film_category.category_id
-- LEFT JOIN film ON film_category.film_id = film.film_id
-- WHERE film.rental_rate = 2.99
-- AND category.name = "Drama"

#8
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM film
LEFT JOIN film_actor ON film_actor.film_id = film.film_id #film - film_actor - actor - film_category
LEFT JOIN actor ON actor.actor_id = film_actor.actor_id
LEFT JOIN film_category ON film_category.film_id = film.film_id
LEFT JOIN category ON category.category_id = film_category.category_id
WHERE actor.first_name = "Sandra"
AND actor.last_name = "Kilmer"