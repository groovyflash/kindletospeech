#Using selenium in the front so I can see!!!!
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from time import sleep
import pytesseract
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pydub import AudioSegment
from PIL import Image
import pyttsx3

#The scrapKinde function takes the book from kindle and converts it into an audiobook
def createAdudiobook(text):
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    #sets the voice rate to 150
    converter.save_to_file(text, 'fullbook.mp3')
    converter.runAndWait()
    converter.stop()

# This converts the screenshot into text!
def convertToText(IMAGE_PATH):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(Image.open(IMAGE_PATH))
    return text

def cropImage():
    im = Image.open(r"C:\Users\fisch\OneDrive\Desktop\Application\screenshot2.png")
    width, height = im.size
    left = 0
    right = width/2
    bottom = height - height/8
    top = height/8
    im1 = im.crop((left, top, right, bottom))
    im1.save(r"C:\Users\fisch\OneDrive\Desktop\Application\screenshotLEFT.png")
    im2 = im.crop((right, top, width, bottom))
    im2.save(r"C:\Users\fisch\OneDrive\Desktop\Application\screenshotRIGHT.png")

def tester():
    driver = webdriver.Firefox()
    action = webdriver.ActionChains(driver)
    driver.get('https://read.amazon.com/kindle-library')
    sleep(1)
    input("You will be asked to login to the screen via text or email confirmation. Please input somthing if you have finished: ")
    TextRight = ""
    TextRightTest = "1"
    TextLeftTest = "1"
    TextRight = ""
    TextLeft = ""
    text = ""
    hashtest = 0
    count = 0
    while hashtest==0:
        start = time.time()
        sleep(2)
        driver.save_screenshot(r'C:\Users\fisch\OneDrive\Desktop\Application\screenshot2.png')
        cropImage()
        TextLeftTest = TextLeft
        TextLeft = convertToText(r"C:\Users\fisch\OneDrive\Desktop\Application\screenshotLEFT.png")
        TextRightTest = TextRight
        TextRight = convertToText(r"C:\Users\fisch\OneDrive\Desktop\Application\screenshotRIGHT.png")
        if TextRight == TextRightTest and TextLeftTest:
             hashtest = 1
        if hashtest == 0:
              text=text + TextLeft + TextRight
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.ID, 'kr-chevron-right')))
            driver.find_element("xpath", '//*[@id="kr-chevron-right"]').click()
        except NoSuchElementException:
             print("not working :/")
        count= count + 1
        #sleep(4)
    with open('readme.txt', 'w') as f:
        f.write(text)
    end = time.time()
    finaltime = end-start
    print(finaltime)
    end = time.time()
    finaltime = end-start
    print(finaltime)
    converter = pyttsx3.init()
    converter.setProperty('rate', 150)
    converter.save_to_file(text, 'fullbook.mp3')
    converter.runAndWait()
    converter.stop()

tester()
