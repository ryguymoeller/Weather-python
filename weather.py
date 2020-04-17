APPID = '90d7ac23cbc3400bb6e4078ab50e3057'

import json
import requests
import sys
import pprint
import datetime

def dayOfWeek(dayWeek):
    day = datetime.datetime.strptime(dayWeek, '%Y-%m-%d')
    day = day.strftime('%A')
    return day

# Compute location from command line arguments.

zipcode = input('Enter Zip Code: ')
country_code = 'us'
state = 'CA'
days = 5

# Download the JSON data from OpenWeatherMap.org's APPID
url = f'https://api.weatherbit.io/v2.0/forecast/daily?postal_code={zipcode}&units=I&days={days}&key={APPID}'
currenturl = f'https://api.weatherbit.io/v2.0/current?postal_code={zipcode}&units=I&key={APPID}'

response = requests.get(url)
response.raise_for_status()

responseCurrent = requests.get(currenturl)
responseCurrent.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(response.text)
weatherCurrentData = json.loads(responseCurrent.text)

# Print weather descriptions.
w = weatherData
wc = weatherCurrentData
# pprint.pprint(w)

currentTemp = wc['data'][0]['temp']
currentDesc = wc['data'][0]['weather']['description']

tomorrowTemp = w['data'][1]['high_temp']
tomorrowDesc = w['data'][1]['weather']['description']
tomorrowDate = w['data'][1]['datetime']

dayAfterTemp = w['data'][2]['high_temp']
dayAfterDesc = w['data'][2]['weather']['description']
dayAfterDate = w['data'][2]['datetime']

print('\n')
print('Today:')
print(f'Currently {currentTemp} and {currentDesc}' + '\n')

print(f'Tomorrow  ({dayOfWeek(tomorrowDate)}):')
print(f'Forecast of a high of {tomorrowTemp} and {tomorrowDesc}\n')

print(f'{dayOfWeek(dayAfterDate)}:')
print(f'Forecast of a high of {dayAfterTemp} and {dayAfterDesc}')
print('\n\n\n')
