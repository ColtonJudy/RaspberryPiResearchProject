from tkinter.constants import BOTTOM, TOP
from Weather import Weather
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from Location import *

lat, lon = getLocation()

root = tk.Tk()
root.geometry('800x600')
root.title('Colton\'s Weather Program')

#TKinter labels
header_label = tk.Label(root)
header_label.pack(side=TOP)

lat_label = tk.Label(root)
lat_label.pack(side=TOP)

lon_label = tk.Label(root)
lon_label.pack(side=TOP)

weather_conditons_label = tk.Label(root)
weather_conditons_label.pack(side=TOP)

temp_label = tk.Label(root)
temp_label.pack(side=TOP)

feels_like_label = tk.Label(root)
feels_like_label.pack(side=TOP)

pressure_label = tk.Label(root)
pressure_label.pack(side=TOP)

humidity_label = tk.Label(root)
humidity_label.pack(side=TOP)

wind_speed_label = tk.Label(root)
wind_speed_label.pack(side=TOP)

hourly_rainfall_label = tk.Label(root)
hourly_rainfall_label.pack(side=TOP)

update_label = tk.Label(root)
update_label.pack(side=BOTTOM)

#method that loads the weather data to the labels
def loadWeatherData(lat, lon):
    #update weather variable
    weather = Weather(lat, lon)
    timeLastUpdated = datetime.now().strftime("%H:%M")

    header_label['text'] = "Weather conditions in " + str(weather.info['location'][0]) + ", " + str(weather.info['location'][2]) + " as of " + timeLastUpdated
    lat_label['text'] = "Latitude: " + str(weather.settings['lat'])
    lon_label['text'] = "Longitutde: " + str(weather.settings['lon'])

    temp_label['text'] = "Current Temperature: " + str(round(weather.current['temp'], 1)) + "°F"
    weather_conditons_label['text'] = "Current Weather: " + weather.current['weather_conditions']
    feels_like_label['text'] = "Feels like: " + str(round(weather.current['feels_like'], 1)) + "°F"
    pressure_label['text'] = "Barometric Pressure: " + str(weather.current['pressure']) + " MB"
    humidity_label['text'] = "Humidity: " + str(weather.current['humidity']) + "%"
    wind_speed_label['text'] = "Wind speed: " + str(weather.current['wind_speed']) + " MPH"
    hourly_rainfall_label['text'] = "Hourly Rainfall: " + str(weather.current['hourly_rainfall']) + " IN"

    update_label['text'] = "Last updated: " + timeLastUpdated

loadWeatherData(lat, lon)

#Update Button
#TODO: API HAS A LIMITED NUMBER OF CALLS PER DAY, SO A LIMIT SHOULD BE ADDED OR THE PROGRAM SHOULD BE MADE TO ONLY AUTOMATICALLY UPDATE ~ EVERY MINUTE
update_button = tk.Button(root, text="Update",command=lambda: loadWeatherData(lat, lon))
update_button.pack(side=BOTTOM)

root.mainloop()