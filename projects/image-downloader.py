#! python3
# image-downloader - downloads first 5 images from flickr.com
# image-downloader.py <image_name>
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import requests
import os

browser = webdriver.Firefox()

try:
  print('Starting up...')

  browser.get('https://www.flickr.com/search/?text=' + ' '.join(sys.argv[1:]))
  os.makedirs('./dist/flickr', exist_ok=True)

  img_elements = browser.find_elements_by_css_selector(
      'a[role="heading"][tabindex="0"]')[:5]
  img_elements_links = list(
      map(lambda x: x.get_attribute('href'), img_elements))

  for img_elem_link in img_elements_links:
    browser.get(img_elem_link)

    print('Loading page %s...' % img_elem_link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[title="Download this photo"]'))
    ).click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[data-track="viewAllSizesClick"]'))
    ).click()

    download_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#allsizes-photo > img'))
    ).get_attribute('src')

    res = requests.get(download_link)
    res.raise_for_status()

    print('Loading image %s...' % download_link)

    img_file = open(
        os.path.join('./dist/flickr', os.path.basename(download_link)), 'wb')
    for chunk in res.iter_content(100000):
      img_file.write(chunk)
    img_file.close()
finally:
  browser.quit()
