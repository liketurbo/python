import pyperclip
import re

phone_regex = re.compile(r'''
  (\+?\d)? # country code
  \s?
  \(?(\d{3})\)? #operator code
  \s?
  (\d{3}[-\s]?\d{2}[-\s]?\d{2}) # subscriber code
''', re.VERBOSE)

email_regex = re.compile(r'''
  [a-zA-Z0-9_.-]+ # username
  @
  [a-zA-Z0-9_.-]+ # domain name
  \.[a-z]{2,4} # dot something
''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
  phone_num = '+7' + groups[1] + groups[2].replace('-', '')
  matches.append(phone_num)
for groups in email_regex.findall(text):
  matches.append(groups[0])

if len(matches) > 0:
  pyperclip.copy('\n'.join(matches))
  print('Copied to clipboard:')
  print('\n'.join(matches))
else:
  print("No phone numbers or email addresses found.")
