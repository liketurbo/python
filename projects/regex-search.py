#! python3
# regex-search - searching in text by regex expression
from glob import glob
import re

txt_paths = glob('./dist/*.txt')

all_text = ''

for txt_path in txt_paths:
  txt_file = open(txt_path)
  all_text += txt_file.read()
  txt_file.close()

regex_pattern = input('Enter regex pattern for search: ')

regex = re.compile(regex_pattern)
res = regex.findall(all_text)

print(res)
