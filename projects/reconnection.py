import requests

res = requests.get('http://google.com')
res.raise_for_status()

if 'http://startwifi.beeline.ru' in res.url:
  res = requests.post('https://startwifi.beeline.ru/status',
                      data={'lang': 'ru', 'screen': 'normal', 'url': '', 'mode': 'partner'})
