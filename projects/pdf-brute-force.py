import PyPDF2

dictionary_file = open('./data/dict.txt')
dictionary = dictionary_file.readlines()
dictionary_file.close()

pdf_file = open('./data/encrypted.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

for word in reversed(dictionary):
  print('Checking %s...' % word, end=' ', flush=True)

  result = pdf_reader.decrypt(word.rstrip())

  if (result == 0):
    print('✕')
  else:
    print('✓')
    break
