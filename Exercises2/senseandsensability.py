import PyPDF2
import os

# Get the directory of the current script
path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(path + '/senseandsensabilitypdf.pdf', "rb")
pdfReader = PyPDF2.PdfReader(file_handle)
page_number = len(pdfReader.pages)  # Get the total number of pages

frequency_table = dict()

def is_not_chapter(word):
    if "CHAPTER" in word:
        return False
    else:
        return True
    
def is_not_link(word):
    if "www" in word:
        return False
    else:
        return True
    
def remove_non_alpha(word):
    return ''.join([char for char in word if char.isalpha()])

for i in range(page_number):
    lines = pdfReader.pages[i].extract_text().split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            word = remove_non_alpha(word)
            if word and is_not_chapter(word) and is_not_link(word):
                word = word.lower()
                if word in frequency_table:
                    frequency_table[word] += 1
                else:
                    frequency_table[word] = 1

for word in frequency_table:
    print(f"{word} : {frequency_table[word]}")

print(frequency_table)