import requests
import os
import bs4

url = 'http://xkcd.com'
os.makedirs('./dist/xkcd', exist_ok=True)

while not url.endswith('#'):
  print('Downloading page %s...' % url)
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  img_elem = soup.select_one('#comic img')
  if img_elem == None:
    print('Could not find comic image.')
  else:
    img_url = img_elem.get('src')
    print('Downloading image %s%s...' % ('http:', img_url))
    res = requests.get('http:' + img_url)
    res.raise_for_status()

    img_file = open(os.path.join(
        './dist/xkcd', os.path.basename(img_url)), 'wb')
    for chunk in res.iter_content(100000):
      img_file.write(chunk)
    img_file.close()

  prev_link = soup.select_one('a[rel="prev"]')
  url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
