import requests, datetime,simplejson,urllib2,math

def publishToFirebase(latDestination,longitDestination,lat,longit,distance):
    currentDate=str(datetime.datetime.now())
    myJson = "{\"date\":\""+str(currentDate)+"\", \"lat\":\""+str(lat)+"\", \"longit\":\""+str(longit)+"\",\"distance\":\""+str(distance)+"\"}"
    print myJson
    myJson2=simplejson.dumps(myJson)
    #req = urllib2.Request("https://locationtrackingdd.firebaseio.com/"+str(int(latDestination))+"AND"+str(int(longitDestination))+".json",methods='PUT')
    r=requests.put("https://locationtrackingdd.firebaseio.com/destinations.json",data = myJson)
   
    return r                                                                   

def getFromFirebase():
    res=requests.get("https://locationtrackingdd.firebaseio.com/destinations.json")
    print res.text

    return simplejson.loads(res.text)['distance']