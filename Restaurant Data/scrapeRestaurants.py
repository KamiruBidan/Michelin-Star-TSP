import urllib2
import json

def getCity(city):
	city = city.replace(" ", "+")
	output = "json"
	query = "michelin+star+restaurants+" + city
	key = open("../key","r").readline()
	url = "https://maps.googleapis.com/maps/api/place/textsearch/"
	url += output + "?query=" + query + "&key=" + key
	filename = city + ".json"
	f = open("json/" + filename, "w")
	f.write(urllib2.urlopen(url).read())
	f.close()
	convertToCsv(filename, city)

def convertToCsv(filename, city):
	outfile = "restaurants/" + filename.replace(".json", ".csv")
	city = city.replace("+", " ")
	json_data = open("json/" + filename)
	data = json.load(json_data)
	f = open(outfile, "w")
	for i in range(0, len(data['results'])):
		name = data['results'][i]['name']
		name = name.replace(',','').strip()
		if name == "":
			continue
		if data['results'][i].has_key('price_level'):
			price = data['results'][i]['price_level']
		else:
			continue
		lat = data['results'][i]['geometry']['location']['lat']
		lng = data['results'][i]['geometry']['location']['lng']
		rating = -1
		if data['results'][i].has_key('rating'):
			rating = data['results'][i]['rating']
		line = name + "," + str(price) + "," + str(lat) + "," + str(lng) + "," + city
		if rating != -1:
			line += "," + str(rating)
		f.write(line.encode('ascii', 'ignore') + '\n')
	f.close()
	json_data.close()

cityFile = open("../cities.csv", "r")
for line in cityFile:
	city = line.split(',')[0]
	print line[:-1]
	getCity(line[:-1])
cityFile.close()
