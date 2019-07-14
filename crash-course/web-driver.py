from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://student.sechenov.ru/auth.php')
try:
  email_elem = browser.find_element_by_css_selector('input[name="USER_LOGIN"]')
  email_elem.send_keys('vippayne@mail.ru')

  password_elem = browser.find_element_by_css_selector(
      'input[name="USER_PASSWORD"]')
  password_elem.send_keys('r9jahi')

  checkbox_elem = browser.find_element_by_css_selector(
      '#activated-auth-form input[type="checkbox"]')
  checkbox_elem.click()

  submit_elem = browser.find_element_by_id('activated-auth-form-submit')
  submit_elem.click()
except:
  print('Was not able to find an element with that name.')
