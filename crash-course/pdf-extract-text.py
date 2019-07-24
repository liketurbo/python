import PyPDF2

pdf_obj = open('./data/meetingminutes.pdf', 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_obj)

print(pdf_read.numPages)
print(pdf_read.getPage(0).extractText())

pdf_obj.close()
