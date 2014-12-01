Michelin-Star-TSP
=================

Obtaining data to optimize the cost and time of one's journey around some of the world's best Michelin Star restaurants.

This optimization problem serves as my final project for OPIM 321 Management Science.

The code written for the project is a good example of using Google Places API, Google QPX Express Airfare API, Python Requests library, and Python Urllib2 library. 

Data Needed:

1. Restaurant Information
I started with a file of 24 cities with codes to the airports nearest to them. Google Places API was used to pull Michelin Star resaurants in each city. The results were then concatenated together. The relevent data is stored in all.csv. The columns are: Name of restaurant, price level from $ to $$$$, latitude, longitue, city, rating out of 5 stars.

2. Flight Information
Using the same cities as a starting point, I constructed a list of "airpairs" (list of route possibilities from origin to destination). I next used Google QPX Express Airfare API to obtain flight information for each route. I started with a basic request in request.json, and wrote code to iterate over the airpairs and find 5 flights from the each origin-destination pair. I then concatenated them, converted airport codes to city names, and all prices to USD. I obtained a file allFlights.csv. The columns of this file are: Origin city, destination city, flight number (flight number of first flight in case of one or more stops), duration in minutes, price in currency local to origin city, price in USD.