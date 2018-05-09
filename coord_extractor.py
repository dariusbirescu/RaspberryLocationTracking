import json, wifitest, publisher

def getCoords():
	data = wifitest.getIPInfo()
	
	loc = data['loc']
	lat = loc.split(',')[0]
	longit = loc.split(',')[1]

        print lat
        print longit

        publisher.publishToFirebase(lat,longit)
	
	return {"latitude": lat, "longitute": longit}

getCoords()
