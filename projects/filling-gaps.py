import os
from os import path
import re
import shutil

regex = re.compile(r'^(.*?)(\d+)(.+?)$')


def filling_gaps(source):
  matches = []
  for folder_name, _, filenames in os.walk(source):
    for filename in filenames:
      match = regex.search(path.join(folder_name, filename))
      matches.append(match)

  matches.sort(key=lambda match: match.group(2))

  index = int(matches[0].group(2))

  for match in matches:
    orig_name = match.group(0)
    new_name = match.group(1) + str(index).rjust(3, '0') + match.group(3)
    index += 1

    shutil.move(orig_name, new_name)


filling_gaps('./dist')
