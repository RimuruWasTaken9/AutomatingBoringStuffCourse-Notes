import PyPDF2
import os


os.chdir('c:\\users\\rimuru\\documents')
pdfFile = open('test.pdf', 'rb')
'''
reader = PyPDF2.PdfReader(pdfFile)
print(len(reader.pages))
page = reader.pages[1]
print(page.extract_text(),'test')
for pageNum in range(len(reader.pages)):
    print(reader.pages[pageNum].extract_text())
#the pdf I used didn't give me text, but the program seemed to run fine.
'''
"""
pdf1File = open('test.pdf','rb')
pdf2File = open('test.pdf','rb')
reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)
writer = PyPDF2.PdfWriter()
for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)
outputFile = open('combinedtest.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
#the pdf I used still didn't work so no actual result shown, need a new pdf
"""
#so many of the functions in the video are outdated
#PdfFileReader() = PdfReader()
#getPage() = .pages
#.numPages = len('name'.pages)
#.getPage(pageNumber) = .pages[page_number]
#extractText = extract_text
#PdfFileWriter() = PdfWriter()
#addPage() = .add_page

