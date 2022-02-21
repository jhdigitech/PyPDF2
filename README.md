# PyPDF2
more detail please refer to https://pythonhosted.org/PyPDF2/

how to use PyPDF2 
在此我分享PyPDF的函式，使用經驗
首先要pip install PyPDF2 在Anaconda Promot(Ananconda 3) 將PyPDF導入系統套件

Share_1 ~ 切割檔案 
=========================================================================
from PyPDF2 import PdfFileWriter, PdfFileReader

readFile = '建立品牌.pdf'  #  確認要分割的檔案 readFile
pdfFileReader = PdfFileReader(readFile) # 呼叫PdfFileWriter()去讀取pdf檔案
outfile='建立品牌_分割檔案.pdf'  # 設定新檔案名稱
pdf_writer=PdfFileWriter()    # 設定函式
page_num = pdfFileReader.getNumPages()  # 確認檔案頁數 pdfFileReader.getNumOafes()~ 屬數字的資料型態 <class 'int'>

if page_num > 4:  # 如果頁數大於4
    for i in range(4,page_num):  # 列印第5頁以後的資料在新檔案 
        newpage = pdfFileReader.getPage(i)
        pdf_writer.addPage(newpage)
        pdf_writer.write(open(outfile,'wb'))

print('分割ok') # remind you this action is done
=========================================================================

Share_2 ~ 合併檔案 
=========================================================================
import PyPDF2

files = ['建立品牌.pdf', 'jhdigitech website.pdf']   # 因為我們要做for迴圈所以將檔案做成一個list
pdf_combine = PyPDF2.PdfFileWriter()  # 設計一個變數 pdf_combine 去執行PyPDf2內的PdfFileWriter 的指令，這指令就是pdf寫入的函式
file_output = open('建立品牌與website.pdf','wb')         # 設定一個檔案名稱是合併後的歐...

for file in files:                                          # file做迴圈 
    pdf_reader = PyPDF2.PdfFileReader(open(file, 'rb'))     # 先讀檔案
    for i in range(pdf_reader.numPages):                    # 將讀取的檔案一頁一頁寫入
        pdf_combine.addPage(pdf_reader.getPage(i))

pdf_combine.write(file_output)  
file_output.close()     # 務必記得要close()
print('done')  
=========================================================================




