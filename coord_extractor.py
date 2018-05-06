import json, wifitest

def getCoords():
	data = wifitest.getIPInfo()
	
	loc = data['loc']
	lat = loc.split(',')[0]
	longit = loc.split(',')[1]
	
	return {"latitude": lat, "longitute": longit}

getCoords()