import requests
import sys
import webbrowser
import bs4

try:
  print('Googling...')
  res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
  res.raise_for_status()

  google_soup = bs4.BeautifulSoup(res.text, 'html.parser')
  file = open('./dist/google-search.html', 'wb')
  for chunk in res.iter_content(100000):
    file.write(chunk)
  file.close()
  link_elements = google_soup.select(
      '#main > div > div > div > a')
  for i, link in enumerate(link_elements):
    if i == 5:
      break
    webbrowser.open('http://google.com' + link.get('href'))

except Exception as err:
  print(err)
