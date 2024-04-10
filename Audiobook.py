import pyttsx3
import PyPDF2
pdf=open("ML.pdf","rb")
reader=PyPDF2.PdfReader(pdf)
pages=len(reader.pages)
massege=pyttsx3.init()
for i in range(4,pages):
    readpage=reader.pages[i]
    apage=readpage.extract_text()
    saying=apage
    massege.say(saying)
    massege.runAndWait()








