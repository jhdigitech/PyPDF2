# PyPDF2
how to use PyPDF2 
在此我分享PyPDF的函式，使用經驗
首先要pip install PyPDF2 在Anaconda Promot(Ananconda 3) 將PyPDF導入系統套件

第一招 ~ 分割檔案 
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






