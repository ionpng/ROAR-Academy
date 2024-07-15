import PyPDF2 
import os

path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(path + '/senseandsensabilitypdf.pdf') 
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 
page_object = pdfReader.pages[0]    # We just get page 0 as example 
page_text = page_object.extract_text()   # this is the str type of full page 

print(page_text)