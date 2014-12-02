f = open("allFlights.csv", "r")
outf = open("minFlights.csv", "w")

flights = []
for line in f:
	flights.append(line[:-1])

i = 0
while i < len(flights):
	line = flights[i]
	pcs = line.split(",")
	print pcs[5]
	minimCost = float(pcs[5])
	minimTime = float(pcs[3])
	k = i + 1
	for j in range(k, k + 4):
		line2 = flights[j]
		pcs2 = line2.split(",")
		if minimCost < float(pcs2[5]):
			minimCost = float(pcs2[5])
		if minimTime < float(pcs2[5]):
			minimTime = float(pcs2[3])
	outf.write(pcs[0] + "," + pcs[1] + "," + str(minimTime) + "," + str(minimCost) + "\n")
	i += 5

f.close()
outf.close()