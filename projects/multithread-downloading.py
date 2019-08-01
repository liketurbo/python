import requests
import os
import bs4
import threading

os.makedirs('./dist/xkcd', exist_ok=True)


def download_xkcd(start_comic, end_comic):
  for url_number in range(start_comic, end_comic):
    print('Downloading page http://xkcd.com/%s' % url_number)

    res = requests.get('http://xkcd.com/%s' % url_number)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comic_elem = soup.select_one('#comic img')
    if not comic_elem:
      print('Could not find comic image')
    else:
      comic_url = comic_elem.get('src')

      print('Dowloading image %s' % ('http:' + comic_url))

      res = requests.get('http:' + comic_url)
      res.raise_for_status()

      img_file = open(os.path.join(
          'dist/xkcd', os.path.basename(comic_url)), 'wb')

      for chunk in res.iter_content(100000):
        img_file.write(chunk)

      img_file.close()


dowload_threads = []

interval = 10
for i in range(0, 1400, interval):
  dowload_thread = threading.Thread(
      target=download_xkcd, args=(i, i + interval - 1))
  dowload_threads.append(dowload_thread)
  dowload_thread.start()

for dowload_thread in dowload_threads:
  dowload_thread.join()

print('Done')
