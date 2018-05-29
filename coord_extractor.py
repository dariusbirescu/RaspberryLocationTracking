import json, wifitest, publisher

index=-1
def getCoords(destinationLat,destinationLong):
        global index
        coordinates=[{"latitude":120, "longitude":120},{"latitude":125,"longitude":130},{"latitude":120, "longitude":120},{"latitude":110, "longitude":110},{"latitude":110, "longitude":110}]
        index=index+1

        return coordinates[index]