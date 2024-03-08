
# ****** ALMOST OVER ******

# weather.py
# weather module

import requests
import json
from location_raspberry_pi import get_location

def get_weather_data():
    get_loc=get_location()
    latitude=get_loc[0]
    longitude=get_loc[1]
    api_key = '540300516678450432c4b06efd0b07df'
    weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(weather_api_url)
    print(latitude, longitude)
    weather_data = response.json()
    return weather_data
