
"""import easyocr
import cv2
import numpy
reader = easyocr.Reader(['en'] , gpu= False)
imageloc= 'C:\\Users\\Administrator\\Desktop\\SCAN'+string+'.jpg'
query = reader.read(imageloc)
print(query)"""
from googletrans import Translator
tran=Translator()

import pytesseract as ts
import pywhatkit as pwt
from PIL import Image
#AUDIO
from gtts import gTTS
import os

#TO CLEAN
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
ts.pytesseract.tesseract_cmd=r'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
s='IMG'
#CREATING THE FILE
myFile="texttrans.txt"
file = open('text.txt' ,"w+")
def scanner(s):
    string='/' + s
    try:
        #IMAGE TO TEXT
        imageloc= 'C:\\Users\\Administrator\\Desktop\\SCAN'+string+'.jpg'
        queryimg=Image.open(imageloc)
        query=ts.image_to_string(queryimg)
        print(query)
        #CLEAN FOR SUB/TB DETECTOR
        new_review=query
        new_review = re.sub('[^a-zA-Z]', ' ', new_review)
        new_review = new_review.lower()
        new_review = new_review.split()
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
        new_review = ' '.join(new_review)
        new_corpus = [new_review]
        print(new_corpus)

        #TRANSLATE
        translated = tran.translate(query , dest="hi")
        out=translated.text
        #INSERT TO THE FILE
        file.write(query)
        file.write("TRANSLATED VERION \n")
        os.system("start text.txt")
        file.close()
        with open(myFile, 'w', encoding='utf-8') as f:
            f.write(out)
            os.system("start texttrans.txt")
            f.close()
        #SPEACH  GTTA
        audio= gTTS(text=query , lang='en' ,slow=False )
        audio.save("a1.mp3")
        os.system("start a1.mp3")
        #GOOGLE SEARCH
        pwt.search(query)
    except:
            print("GIVEN IMAGE IS'NT SCANNABLE")
scanner(s)
