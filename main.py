import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()

pdfreader = PdfReader(book)
pages = len(pdfreader.pages)

player = pyttsx3.init()

for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()

    if text:
        player.say(text)

player.runAndWait()