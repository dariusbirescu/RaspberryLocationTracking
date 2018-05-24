import requests, datetime,json,urllib2,math

def publishToFirebase(latDestination,longitDestination,lat,longit,distance):
    currentDate=str(datetime.datetime.now())
    data = {"date":currentDate, "lat":lat, "longit":longit,"distance":distance}
    req = urllib2.Request("https://locationtrackingdd.firebaseio.com/"+str(int(latDestination))+"AND"+str(int(longitDestination))+".json")
    req.add_header('Content-Type', 'application/json')
    
    response = urllib2.urlopen(req, json.dumps(data))
    #print response.read()
    return response.read()                                                                      

def getFromFirebase(lat,longit,locationId):
    res=urllib2.urlopen("https://locationtrackingdd.firebaseio.com/"+str(int(lat))+"AND"+str(int(longit))+"/"+locationId+".json")
    return res.read()