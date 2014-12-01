k = 0
f = open("allFlightsCity.csv", "w")
flights = open("allFlights.csv", "r")
cityCodes = open("../cities.csv", "r")
cities = {"TRF":"oslo"}
for line in cityCodes:
	cities[line.split(",")[1][:-1]] = line.split(",")[0]
for line in flights:
	arr = line.split(",", 2)
	print arr[0] + "--->" + arr[1]
	origin = cities[arr[0]]
	destin = cities[arr[1]]
	f.write(origin + "," + destin + "," + arr[2])
f.close()
flights.close()
cityCodes.close()
