#! python3
# email-sender.py - sends email message to specified address
# email-sender.py <email> <message>

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('https://mail.yandex.com')

login_elem = None
while not login_elem:
  try:
    login_elem = browser.find_element_by_link_text('Log in')
    break
  except:
    continue
login_elem.click()

email_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'passp-field-login'))
)
email_elem.send_keys('bo8.saget')
email_elem.submit()

passw_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'passp-field-passwd'))
)
passw_elem.send_keys('pFvXg5PbJW9rTUF')
passw_elem.submit()

compose_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Compose'))
)
compose_elem.click()

to_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[name="to"]'))
)
to_elem.send_keys(sys.argv[1])

text_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]'))
)
text_elem.send_keys(' '.join(sys.argv[2:]))

send_elem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'nb-13'))
)
send_elem.click()
