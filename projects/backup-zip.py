#! python3
'''
backup-zip.py - Copies an entire folder and its contents into
a ZIP file whose filename increments.
'''

from zipfile import ZipFile as zip
import os
import sys


def backup_zip(folder):
  if not os.path.isdir(folder):
    raise Exception('Cannot find folder')

  for version in range(sys.maxsize):
    zip_filename = '%s-%s.zip' % (os.path.basename(folder), version)

    if not os.path.exists(zip_filename):
      break

  print('Creating %s...' % zip_filename)
  zip_file = zip(zip_filename, 'w')

  for folder_name, _, filenames in os.walk(folder):
    for filename in filenames:
      print('Adding %s...' % os.path.join(folder_name, filename))
      zip_file.write(os.path.join(folder_name, filename))

  zip_file.close()


backup_zip('./dist')
