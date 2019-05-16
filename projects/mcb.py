#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys

mcb_shelve = shelve.open('./dist/mcb')
print(len(sys.argv))

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  mcb_shelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
  if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(mcb_shelve.keys()))
  elif sys.argv[1] in mcb_shelve:
    pyperclip.copy(mcb_shelve[sys.argv[1]])
