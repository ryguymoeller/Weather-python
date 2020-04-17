APPID = '90d7ac23cbc3400bb6e4078ab50e3057'

import json
import requests
import sys
import pprint
import datetime

def forecastWeather(zipcode):
    # Download the JSON data from https://www.weatherbit.io/api/weather-forecast-16-day API
    url = f'https://api.weatherbit.io/v2.0/forecast/daily?postal_code={zipcode}&units=I&days={days}&key={APPID}'
    response = requests.get(url)
    response.raise_for_status()
    # Load JSON data into a Python variable
    weatherData = json.loads(response.text)
    w = weatherData

    # Loop to go through the days to forecast
    for day in range(1, days):
        forecastTemp = w['data'][day]['high_temp']
        forecastDesc = w['data'][day]['weather']['description']
        forecastDate = w['data'][day]['datetime']

        # Print data
        print(f'{dayOfWeek(forecastDate)}:')
        print(f'Forecast of a high of {forecastTemp} and {forecastDesc}\n\n')


def dayOfWeek(dayWeek):
    day = datetime.datetime.strptime(dayWeek, '%Y-%m-%d')
    day = day.strftime('%A')
    return day

# Have the user input a zipcode
zipcode = input('Enter Zip Code: ')
country_code = 'us'
days = 5    # days to foreceast

# Download the JSON data from https://www.weatherbit.io/api/weather-current APPID
currenturl = f'https://api.weatherbit.io/v2.0/current?postal_code={zipcode}&units=I&key={APPID}'

responseCurrent = requests.get(currenturl)
responseCurrent.raise_for_status()

# Load JSON data into a Python variable
weatherCurrentData = json.loads(responseCurrent.text)

# Print weather descriptions.
wc = weatherCurrentData
currentTemp = wc['data'][0]['temp']
currentDesc = wc['data'][0]['weather']['description']
currentFeelsLike = wc['data'][0]['app_temp']

# print the current weather data
print('\n')
print('Today:')
print(f'Currently {currentTemp} and {currentDesc}')
print(f'Feels like {currentFeelsLike}' + '\n')

# Call the forecast Weather function
forecastWeather(zipcode)


# pprint.pprint(w)
