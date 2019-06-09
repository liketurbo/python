import os
from os import path
import shutil


def selective_copy(source, destination, type):
  os.mkdir(destination)
  # TODO: iterate folder for specific type
  for folder, _, files in os.walk(source):
    for filename in files:
      if type in filename:
        # TODO: copy those file to destination
        shutil.copy(path.join(folder, filename), destination)


selective_copy('./data', './texts', '.txt')
