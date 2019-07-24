import os
import PyPDF2

pdf_files = []

for filename in os.listdir('./data'):
  if filename.endswith('.pdf'):
    pdf_files.append(os.path.join('./data', filename))

pdf_files.sort(reverse=True)

pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
  pdf_file = open(filename, 'rb')
  pdf_reader = PyPDF2.PdfFileReader(pdf_file)

  for page_num in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

pdf_output = open('./dist/output.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
