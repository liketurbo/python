#! python3
# 2048 - automatically playing 2048 game
# 2048.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()

try:
  browser.get('https://play2048.co')
  game_elem = browser.find_element_by_css_selector('html')

  while True:
    game_elem.send_keys(Keys.ARROW_UP)
    game_elem.send_keys(Keys.ARROW_RIGHT)
    game_elem.send_keys(Keys.ARROW_DOWN)
    game_elem.send_keys(Keys.ARROW_LEFT)

    try:
      browser.find_element_by_css_selector(
          '.game-message.game-over')
      break
    except:
      continue
finally:
  sleep(5)
  browser.quit()
