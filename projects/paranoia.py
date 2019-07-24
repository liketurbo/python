import PyPDF2
import sys
import os
import re

PATH = sys.argv[1]
PASSWORD = sys.argv[2]

for root, folders, filenames in os.walk(PATH):
  for filename in filenames:
    if filename.endswith('.pdf'):
      full_filename = os.path.join(root, filename)

      pdf_write = PyPDF2.PdfFileWriter()
      pdf_read = PyPDF2.PdfFileReader(open(full_filename, 'rb'))

      if pdf_read.isEncrypted:
        continue

      for page_num in range(pdf_read.numPages):
        page_obj = pdf_read.getPage(page_num)
        pdf_write.addPage(page_obj)

      pdf_output = open(re.sub(r'\.pdf$', '_encrypted.pdf',
                               full_filename), 'wb')

      pdf_write.encrypt(PASSWORD)

      print('Creating %s...' % pdf_output.name)
      pdf_write.write(pdf_output)

      pdf_output.close()
