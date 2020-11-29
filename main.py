import pyttsx3
import PyPDF2
import os

path = 'your_path'


book = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('This book has', pages, 'pages')

speaker = pyttsx3.init()
#setting up speach rate from 200 to 125
rate = speaker.getProperty('rate')   # getting details of current speaking rate
# print(rate)  // default is 200        
speaker.setProperty('rate', 150)      # setting up new voice rate

voices = speaker.getProperty('voices')       #getting details of current voice
# speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


speaker.say('Now I am going to read a book named: ' + str(book.name[:len(book.name)-4]))
speaker.runAndWait()

#loop for reading all pages from index no. 20
for t in range(19, pages):
    page = pdfReader.getPage(t)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()


   
#closing the pdf file object 
book.close() 
