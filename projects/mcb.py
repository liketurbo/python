#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe
# mcb.py save <keyword> - Saves clipboard to keyword.
# mcb.py <keyword> - Loads keyword to clipboard.
# mcb.py list - Loads all keywords to clipboard.
# mcb.py delete - Delete all keyword
# mcb.py delete <keyword> - Delete keyword

import shelve
import pyperclip
import sys

mcb_shelve = shelve.open('./dist/mcb.db')

if len(sys.argv) == 3:
  if sys.argv[1].lower() == 'save':
    print('Clipboard saved under key %s' % sys.argv[2])
    mcb_shelve[sys.argv[2]] = pyperclip.paste()
  elif sys.argv[1].lower() == 'delete':
    print('Key %s has been deleted' % sys.argv[2])
    del mcb_shelve[sys.argv[2]]
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    keys = str(list(mcb_shelve.keys()))
    print('You have values with keys %s' % keys)
    pyperclip.copy(keys)
  elif sys.argv[1] in mcb_shelve:
    print('Value of %s copied to the clipboard' % sys.argv[1])
    pyperclip.copy(mcb_shelve[sys.argv[1]])
  elif sys.argv[1].lower() == 'delete':
    print('Removed all keys')
    mcb_shelve.clear()
