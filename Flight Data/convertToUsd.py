k = 0
f = open("allFlights.csv", "w")
flights = open("allFlightsCity.csv", "r")
currency = open("currency.csv", "r")
curr = {}
for line in currency:
	curr[line.split(",")[0]] = float(line.split(",")[1][:-1])
print curr
for line in flights:
	arr = line.split(",")
	last = arr[4][:-1]
	print last[:3] + "   " + last[3:]
	cost = float(last[3:])
	cu = last[:3]
	newcost = cost * curr[cu]
	newline = line[:-1] + "," + str(newcost) + "\n"
	f.write(newline)
f.close()
flights.close()
currency.close()
