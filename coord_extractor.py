import json, wifitest, publisher

def getCoords(destinationLat,destinationLong):
	data = wifitest.getIPInfo()
	
	loc = data['loc']
	lat = loc.split(',')[0]
	longit = loc.split(',')[1]

        #print lat
        #print longit

	return {"latitude": lat, "longitude": longit}
