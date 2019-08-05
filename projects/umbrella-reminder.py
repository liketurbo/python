import requests
from twilio.rest import Client

# Download the JSON data from Yandex.Geocoder API.
url = 'https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s' % (
    'a5d61983-259c-48d2-a409-890470659789&format=json&results=1', 'Moscow')
res = requests.get(url)
res.raise_for_status()

lon, lat = res.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(
    ' ')

# Download the JSON data from Yandex.Weather API.
res = requests.get(
    'https://api.weather.yandex.ru/v1/forecast?lat=%s&lon=%s' % (
        lat, lon), headers={'X-Yandex-API-Key': '68bd2aaa-2b18-416f-ad83-2f22b5729074'})
res.raise_for_status()

conditions = map(lambda x: x['condition'], res.json()['forecasts'][0]['hours'])
is_rain = any('rain' in x for x in conditions)

if is_rain:
  account_SID = 'AC691ab11264f4b2d6d3309ba8b811d205'
  auth_token = '5dddd0020a17adcd7953d1ee436c3924'
  twilio_number = '+14253812300'

  twilio_cli = Client(account_SID, auth_token)
  msg = 'Rain promised for today. Don\'t forget to take your umbrella.'

  twilio_cli.messages.create(
      body=msg, from_=twilio_number, to='+79773571157')
  twilio_cli.messages.create(
      body=msg, from_=twilio_number, to='+79612619617')
