import requests, datetime,json,urllib2,math

def publishToFirebase(latDestination,longitDestination,lat,longit):
    currentDate=str(datetime.datetime.now())
    data = {"date":currentDate, "lat":lat, "longit":longit}
    req = urllib2.Request("https://locationtrackingdd.firebaseio.com/"+str(int(latDestination))+"AND"+str(int(longitDestination))+".json")
    req.add_header('Content-Type', 'application/json')
    
    response = urllib2.urlopen(req, json.dumps(data))
    print response
    return response                                                                             
