
from PyPDF2 import PdfFileWriter, PdfFileReader

readFile = '建立品牌.pdf'
pdfFileReader = PdfFileReader(readFile)
outfile='建立品牌_分割檔案.pdf'
pdf_writer=PdfFileWriter()
page_num = pdfFileReader.getNumPages()

if page_num > 4:
    for i in range(4,page_num):
        newpage = pdfFileReader.getPage(i)
        pdf_writer.addPage(newpage)
        pdf_writer.write(open(outfile,'wb'))

print('分割ok')
