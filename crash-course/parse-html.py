import requests
import bs4

try:
  res = requests.get(
      'https://www.google.com/search?q=weather&rlz=1C1SQJL_ruRU856RU856&oq=weather+&aqs=chrome..69i57j35i39j0l4.8047j1j1&sourceid=chrome&ie=UTF-8')
  res.raise_for_status()

  file = open('./dist/google-weather.html', 'wb')
  for chunk in res.iter_content(100000):
    file.write(chunk)
  file.close()
  google_soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elem = google_soup.select_one('.BNeawe.iBp4i.AP7Wnd')
  print(elem.attrs)
  print(elem.getText())

except Exception as err:
  print(err)
