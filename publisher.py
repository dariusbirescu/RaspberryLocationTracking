import requests, datetime,json,urllib2

def publishToFirebase(lat,longit):
    currentDate=str(datetime.datetime.now())
    print currentDate
    
    data = {"date":currentDate, "lat":lat, "longit":longit}
    req = urllib2.Request("https://locationtracking-b3f3f.firebaseio.com/.json")
    req.add_header('Content-Type', 'application/json')
    
    response = urllib2.urlopen(req, json.dumps(data))
    print response
    return response

publishToFirebase(3,4)
                                                                             
