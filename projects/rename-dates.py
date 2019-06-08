#! python3
'''
rename-dates.py - Renames filenames with American MM-DD-YYYY date format
to European DD-MM-YYYY.
'''

import shutil
from os import path
import os
import re

date_formap = re.compile(r'^(.*?)(\d+)-(\d+)-(\d+)(.*?)$')

for file in os.listdir('./dist'):
  res = date_formap.search(file)

  if not res:
    continue

  before, month, day, year, after = res.groups()

  us_style = path.join('.', 'dist', res.group())
  eu_style = path.join('.', 'dist', '%s%s-%s-%s%s' %
                       (before, day, month, year, after))
  print('Renaming %s to %s' % (us_style, eu_style))
  shutil.move(us_style, eu_style)
