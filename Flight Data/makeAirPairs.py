k = 0
f = open("airpairs.csv", "w")
cityFile = open("../cities.csv", "r")
cities = []
for line in cityFile:
	cities.append(line)
for line in cities:
	origin = line.split(',')[1][:-1]
	for line2 in cities:
		destin = line2.split(',')[1][:-1]
		if origin == destin:
			continue
		print origin + "-" + destin 
		f.write(origin + "," + destin + "\n")
		k += 1
cityFile.close()
f.close()
