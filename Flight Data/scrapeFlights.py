import json
import ast
import requests

def getDetails(data, o, d):
	if not data["trips"].has_key("tripOption"):
		f = open("00noFlights.csv", "a")
		f.write(o + "," + d + "\n")
		return
	origin = data["trips"]["tripOption"][0]["slice"][0]["segment"][0]["leg"][0]["origin"]
	destin = data["trips"]["tripOption"][0]["slice"][0]["segment"][len(data["trips"]["tripOption"][0]["slice"][0]["segment"]) - 1]["leg"][0]["destination"]
	outfile = "flights/" + origin + "-" + destin + ".csv"
	f = open(outfile, "w+")
	for i in range(0, len(data["trips"]["tripOption"])):
		duration = data["trips"]["tripOption"][i]["slice"][0]["duration"]
		fnum = data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["flight"]["carrier"]
		fnum += data["trips"]["tripOption"][i]["slice"][0]["segment"][0]["flight"]["number"]
		price = data["trips"]["tripOption"][i]["pricing"][0]["saleTotal"]
		line = origin + "," + destin + "," + fnum + "," + str(duration) + "," + price
		f.write(line.encode('ascii', 'ignore') + '\n')
	f.close()

def buildJson(origin, destin):
	json_data = open("request.json")
	data = json.load(json_data)
	key = open("../key","r").readline()
	url = "https://www.googleapis.com/qpxExpress/v1/trips/search"
	url += "?key=" + key
	data = ast.literal_eval(json.dumps(data))
	data["request"]["slice"][0]["origin"] = origin
	data["request"]["slice"][0]["destination"] = destin
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(data), headers=headers)
	data = r.json()
	getDetails(data, origin, destin)

start = 0
end = -1
k = 0
cityFile = open("airpairs.csv", "r")
for line in cityFile:
	if k >= end && end != -1:
		break
	if k < start:
		k += 1
		continue
	origin = line.split(',')[0]
	destin = line.split(',')[1][:-1]
	if origin == destin:
		continue
	print origin + "-" + destin 
	buildJson(origin, destin)
	k += 1
cityFile.close()
