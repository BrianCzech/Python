import PyPDF2
import pyttsx3
import win32api
from tkinter.filedialog import *

book=askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages

for num in range(0,pages):
    page=pdfReader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()

