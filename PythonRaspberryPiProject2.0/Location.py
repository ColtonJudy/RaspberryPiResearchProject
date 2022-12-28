from geopy.geocoders import Nominatim
import gpsd
from time import sleep
import os
import string

defaultCoordinates = (36.535170, -87.35481)

#Find the nearest city to the given coordinates using Nominatim API
def find_nearest_city(lat, lon):
    geolocator = Nominatim(user_agent="Colton's Weather Raspberry Pi Project")

    coords = (lat, lon)
    locationRaw = geolocator.reverse(coords, zoom=10)
    location = str(locationRaw).split(", ")

    return location

#TODO implement receiving GPS data via PI dongle
def getLocation():

    #LAUNCH GPSD
    os.system("gpsd -D 5 -N -n /dev/cu.usbmodem1101")

    try:
        gpsd.connect()
    except:
        print("GPSD failed to connect")

    while True:
        try:
            packet = gpsd.get_current()
        except:
            print("GPS Device not detected, using default coordinates")
            return defaultCoordinates

        try:
            print(packet.position())
            return packet.position()
        except:
            print("Position could not be determined, press [Y] to use default coordinates")
            return defaultCoordinates