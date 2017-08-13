USE world;

#1
SELECT * FROM languages
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC

/*
#2
SELECT countries.name, COUNT(cities.id) AS cities_num
FROM countries
LEFT JOIN cities on countries.id = cities.country_id
GROUP BY countries.id
ORDER BY cities_num DESC;


#3
SELECT cities.name, cities.population
FROM countries
LEFT JOIN cities on countries.id = cities.country_id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population DESC


#4
SELECT countries.name, languages.language, languages.percentage
FROM countries
LEFT JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89.00
ORDER BY languages.percentage DESC;


#5
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000


#6
SELECT countries.name, countries.government_form, countries.life_expectancy, countries.capital
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75


#7
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
LEFT JOIN cities on countries.id = cities.country_id
WHERE countries.name = "Argentina" 
AND cities.district = "Buenos Aires" 
AND cities.population > 500000


#8
SELECT countries.region, COUNT(countries.id) as country_num
FROM countries
GROUP BY countries.region
ORDER BY country_num DESC
*/