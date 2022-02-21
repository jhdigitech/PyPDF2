import PyPDF2

files = ['建立品牌.pdf', 'jhdigitech website.pdf']
pdf_combine = PyPDF2.PdfFileWriter()
file_output = open('建立品牌與website.pdf','wb')

for file in files:
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))
    for i in range(pdf_reader.numPages):
        #print(pdf_reader.getPage(i))
        pdf_combine.addPage(pdf_reader.getPage(i))

pdf_combine.write(file_output)   
file_output.close()
print('done')  
