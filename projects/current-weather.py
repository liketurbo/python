import sys
import pprint
import requests
import json

LOCATION = ' '.join(sys.argv[1:])

# Download the JSON data from Yandex.Geocoder API.
url = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s' % (
    'a5d61983-259c-48d2-a409-890470659789&format=json&results=1', LOCATION)
response = requests.get(url)
response.raise_for_status()

lon, lat = json.loads(response.text)['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
    ' ')

# Download the JSON data from Yandex.Weather API.
url = 'https://api.weather.yandex.ru/v1/forecast?lat=%s&lon=%s&limit=1&hours=false' % (
    lat, lon)
response = requests.get(
    url, headers={'X-Yandex-API-Key': '68bd2aaa-2b18-416f-ad83-2f22b5729074'})
response.raise_for_status()

# Today
pprint.pprint(json.loads(response.text)['forecasts'][0])

# Tomorrow
pprint.pprint(json.loads(response.text)['forecasts'][0])
