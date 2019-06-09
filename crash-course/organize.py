from send2trash import send2trash
from zipfile import ZipFile as zip
import shutil
import os

shutil.copy('./data/message-from-netflix.txt', './dist')
shutil.copy('./data/message-from-netflix.txt', './dist/msg.txt')

if not os.path.isdir('./dist/folder'):
  shutil.copytree('./data/', './dist/folder')

if not os.path.isdir('./dist/another-folder'):
  shutil.move('./dist/folder', './dist/another-folder')

shutil.move('./dist/msg.txt', './dist/folder/msg')

if os.path.isdir('./dist/folder/subfolder'):
  shutil.move('./dist/msg.txt', './dist/folder/subfolder/msg')

os.unlink('./dist/folder/msg')

os.mkdir('./dist/test-folder')
os.rmdir('./dist/test-folder')

for filename in os.listdir():
  if filename.endswith('.rxt'):
    # os.unlink(filename)
    print(filename)

random_guy = open('./dist/random-guy.txt', 'w')
random_guy.write('Random Guy called you.')
random_guy.close()

send2trash('./dist/random-guy.txt')

for folder_name, subfolders, filenames in os.walk('./dist'):
  print('Current:', folder_name)

  if subfolders:
    print('Subfolders:')
  for subfolder in subfolders:
    print('|-', subfolder)

  if filenames:
    print('Filenames:')
  for filename in filenames:
    print('|-', filename)

# Extracting
zip_file = zip('./data/example.zip')

spam_info = zip_file.getinfo('spam.txt')
print(spam_info)

zip_file.extractall('./dist/from-zip/files')
zip_file.extract('spam.txt', './dist')

# Creating
zip_file = zip('./dist/new.zip', 'w')
zip_file.write('./dist/spam.txt')
zip_file.close()
