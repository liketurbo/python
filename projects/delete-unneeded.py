from os import path
from hurry.filesize import size
import os


def delete_unneeded(source):
  for foldername, _, filenames in os.walk(source):
    for filename in filenames:
      filepath = path.join(foldername, filename)
      filesize = path.getsize(filepath) / 1000000

      if filesize > 100:
        print(path.basename(filepath), filesize)
        # os.unlink(filepath)


delete_unneeded('/c/Users/Ramzan/Downloads/Movies')
