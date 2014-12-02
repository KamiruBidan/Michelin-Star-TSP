cities = open("citiesExcluded.csv", "r")
city = {}
for c in cities:
	c = c[:-1]
	city[c] = 1
	print c
cities.close()

inf = open("cities.csv", "r")
outf = open("smallCities.csv", "w")
for line in inf:
	if city.has_key(line.split(",")[0]):
		continue
	outf.write(line)
inf.close()
outf.close()