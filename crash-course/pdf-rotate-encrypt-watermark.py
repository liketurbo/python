import PyPDF2

pdf_file1 = open('./data/meetingminutes.pdf', 'rb')
pdf_file2 = open('./data/meetingminutes2.pdf', 'rb')
pdf_file3 = open('./data/watermark.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)
pdf_reader3 = PyPDF2.PdfFileReader(pdf_file3)

pdf_writer = PyPDF2.PdfFileWriter()


for page_num in range(pdf_reader1.numPages):
  page_obj = pdf_reader1.getPage(page_num)

  # Adding watermark
  page_obj.mergePage(pdf_reader3.getPage(0))

  pdf_writer.addPage(page_obj)

for page_num in range(pdf_reader2.numPages):
  page_obj = pdf_reader2.getPage(page_num).rotateCounterClockwise(90)
  pdf_writer.addPage(page_obj)

# Encrypting file
pdf_writer.encrypt('swordfish')

file = open('./dist/output.pdf', 'wb')
pdf_writer.write(file)

file.close()
pdf_file1.close()
pdf_file2.close()
