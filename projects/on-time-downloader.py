import os
import shelve
import requests
import sys
import bs4
import threading
import re
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

comics = [
    ('http://lefthandedtoons.com', 'img.comicimage'),
    ('http://buttersafe.com', '#comic > img'),
    ('http://savagechickens.com', '[id^=post-] img'),
    ('http://lunarbaboon.com', '[id^=item] .body img'),
    ('http://completelyseriouscomics.com', '#comic img'),
    ('http://exocomics.com', '[id^=comic-] img'),
    ('http://nonadventures.com', '#comic img'),
    ('http://moonbeard.com', '#comic img'),
    ('http://happletea.com', '#comic img')
]

last_comics = []


def download_last_img(url):
  print('Downloading image %s...' % url)

  res = requests.get(url, headers=headers)
  res.raise_for_status()

  current_date = datetime.datetime.now().strftime('%d-%m-%y')
  os.makedirs(os.path.join('dist/daily-comics', current_date), exist_ok=True)

  img_file = open(os.path.join(
      'dist/daily-comics', current_date, os.path.basename(url)), 'wb')
  for chunk in res.iter_content(100000):
    img_file.write(chunk)
  img_file.close()


def get_last_img(url, selector):
  print('Fetching from %s...' % url)

  res = requests.get(url, headers=headers)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  img = soup.select_one(selector)

  image_url = img.get('src')

  if not re.match(r'https?://', image_url):
    image_url = url + image_url

  last_comics.append(image_url)


os.makedirs('dist/daily-comics', exist_ok=True)

download_threads = []

for comic in comics:
  thread = threading.Thread(target=get_last_img, args=comic)
  download_threads.append(thread)
  thread.start()

for thread in download_threads:
  thread.join()

shelve_file = shelve.open('dist/daily-comics/comics-data')

comics_to_download = None

if shelve_file.get('last_comics'):
  comics_to_download = set(last_comics).difference(shelve_file['last_comics'])
else:
  comics_to_download = last_comics

download_threads = []
for comic in comics_to_download:
  thread = threading.Thread(target=download_last_img, args=[comic])
  download_threads.append(thread)
  thread.start()

shelve_file['last_comics'] = last_comics
shelve_file.close()
