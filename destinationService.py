import coord_extractor,publisher,json,time

lat = input("Latitude: ")
longit=input("Longitude: ")
#print lat,longit
lastDistance=20000



while(True):
  time.sleep(5)

  x=coord_extractor.getCoords(lat,longit)

  distance=abs(float(lat)-float(x['latitude']))+abs(float(longit)-float(x['longitude']))

  response=publisher.publishToFirebase(lat,longit,x['latitude'],x['longitude'],distance)

  #print response

  currentLocationId=json.loads(response)['name']

  newDistance=json.loads(publisher.getFromFirebase(lat,longit,currentLocationId))['distance']

  if(distance>newDistance-10):
    print newDistance

  