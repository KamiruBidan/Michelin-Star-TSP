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
	mcLine = line
	minimTime = float(pcs[3])
	mtLine = line
	k = i + 1
	for j in range(k, k + 4):
		line2 = flights[j]
		pcs2 = line2.split(",")
		if minimCost > float(pcs2[5]):
			minimCost = float(pcs2[5])
			mcLine = line2
		if minimTime > float(pcs2[3]):
			minimTime = float(pcs2[3])
			mtLine = line2
	outf.write(mcLine + "\n")
	if mcLine == mtLine:
		i += 5
		continue
	outf.write(mtLine + "\n")
	i += 5

f.close()
outf.close()