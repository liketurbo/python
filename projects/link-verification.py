#! python3
# link-verification - verifies every link in given url for working
# link-verification.py <link>
import requests
from requests.exceptions import MissingSchema
import sys
import bs4

res = requests.get(sys.argv[1])
res.raise_for_status()

page_soup = bs4.BeautifulSoup(res.text, 'html.parser')

link_elements = page_soup.select('a')
link_elements_href = map(lambda x: x.get('href'), link_elements)

link_length = 45
status_length = 6
print('link'.ljust(link_length), 'status', sep=' | ')
print(''.ljust(link_length, '-'), ''.ljust(status_length, '-'), sep='-|-')
for link in link_elements_href:
  try:
    res = requests.get(link)

    print_link = link[:link_length - 3] + \
        '...' if len(link) > link_length else link.ljust(link_length)
    print(print_link, res.status_code, sep=' | ')
  except MissingSchema:
    print_link = link[:link_length - 3] + \
        '...' if len(link) > link_length else link.ljust(link_length)
    print(print_link, '404', sep=' | ')
