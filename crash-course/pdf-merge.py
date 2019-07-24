import PyPDF2

pdf_file1 = open('./data/meetingminutes.pdf', 'rb')
pdf_file2 = open('./data/meetingminutes2.pdf', 'rb')

pdf_reader1 = PyPDF2.PdfFileReader(pdf_file1)
pdf_reader2 = PyPDF2.PdfFileReader(pdf_file2)

pdf_merger = PyPDF2.PdfFileMerger()

pdf_merger.append(pdf_reader1)
pdf_merger.append(pdf_reader2)

pdf_merger.write('./dist/merged.pdf')
