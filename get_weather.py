#!/usr/local/bin/python


import requests
import json


def get_resource(file):
    """Returns a resource json:
    lat, lon, api_key, attributes to display (wind, clouds, rain, snow)"""

    with open(f'/home/haln/Scripts/OpenWeather/src/{file}') as file:
        data = json.load(file)
    return data

def get_weather_data(lat, lon, api_key):
    """Returns a json from fetched api"""
    fetch_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    raw_json = requests.get(fetch_url)
    return raw_json.json()

def attribute_exists(json_data, attr):
    """Check to see if attribute exists, ie rain/snow
    returns the value if exists, otherwise returns false"""
    try:
        return json_data[attr]
    except KeyError:
        return False

if __name__ == "__main__":

    data = get_resource("resource.json")

    lat = data["lat"]
    lon = data["lon"]
    api = data["api_key"]
    display = data["display"]
    # Get data
    data = get_weather_data(lat, lon, api)

    # Filtering data
    temp = str(data['main']['temp']) + u"\N{DEGREE SIGN}C"
    wind = attribute_exists(data, "wind")
    clouds = attribute_exists(data, "clouds")
    rain = attribute_exists(data, "rain")
    snow = attribute_exists(data, "snow")

    # Output to print
    output = ""
    if not clouds:
        output += f" {temp} "
    else:
        output += f" {temp} "

    if wind:
        wind_speed = " " + str(wind['speed']) + "m/s "
        output += wind_speed

    if rain:
        output += f' {rain["1h"]}mm '

    if snow:
        output += f' {snow["1h"]}mm '

    print(output)
