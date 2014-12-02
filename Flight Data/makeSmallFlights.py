cities = open("../citiesExcluded.csv", "r")
city = {}
for c in cities:
	c = c[:-1]
	city[c] = 1
cities.close()

inf = open("minFlights.csv", "r")
outf = open("smallFlights.csv", "w")
for line in inf:
	if city.has_key(line.split(",")[0]) or city.has_key(line.split(",")[1]):
		continue
	outf.write(line)
inf.close()
outf.close()