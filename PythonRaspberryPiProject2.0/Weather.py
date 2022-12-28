import requests
import json
from pprint import pprint
from Location import *

class Weather:
    settings = {
        'api_key' : '040e13ce7de9dadb243f29cde3be44f1',
        'temp_unit' : 'imperial',
        'lat' : 0,
        'long' : 0,
        'url' : 'NULL'
    }

    info = {
        'location' : []
    }

    current = {
        'dt' : 0,
        'sunrise' : 0,
        'sunset' : 0,
        'temp' : 0,
        'feels_like' : 0,
        'pressure' : 0,
        'humidity' : 0,
        'dew_point' : 0,
        'uvi' : 0,
        'clouds' : 0,
        'visibility' : 0,
        'wind_speed' : 0,
        'wind_deg' : 0,
        'weather_conditions' : 'NULL',
        'weather_description' : 'NULL',
        'hourly_rainfall' : 0,
    }

    #TODO: Implement overrided constructor taking zipcode as a parameter and finding location based on that
    def __init__(self, lat, lon):
        self.settings['lat'] = lat
        self.settings['lon'] = lon
        self.info['location'] = find_nearest_city(lat, lon)

        self.settings['url'] = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=%s" % (self.settings['lat'], self.settings['lon'], self.settings['api_key'], self.settings['temp_unit'])

        response = requests.get(self.settings['url'])
        data = json.loads(response.text)
        print(self.settings['url'])

        #read the data from JSON
        self.current['dt'] = data["current"]["dt"]
        self.current['sunrise'] = data["current"]["sunrise"]
        self.current['sunset'] = data["current"]["sunset"]
        self.current['temp'] = data["current"]["temp"]
        self.current['feels_like'] = data["current"]["feels_like"]
        self.current['pressure'] = data["current"]["pressure"]
        self.current['humidity'] = data["current"]["humidity"]
        self.current['dew_point'] = data["current"]["dew_point"]
        self.current['uvi'] = data["current"]["uvi"]
        self.current['clouds'] = data["current"]["clouds"]
        self.current['visibility'] = data["current"]["visibility"]
        self.current['wind_speed'] = data["current"]["wind_speed"]
        self.current['wind_deg'] = data["current"]["wind_deg"]
        self.current['weather_conditions'] = data["current"]["weather"][0]["main"]
        self.current['weather_description'] = data["current"]["weather"][0]["description"]

        self.displayCurrent()

    def displayCurrent(self):
        for entry in self.current.items():
            print(entry)
