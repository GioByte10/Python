import numpy as np
import pyautogui
import time
import cv2
from pytesseract import pytesseract
from pynput.keyboard import Controller

time.sleep(3)

keybd = Controller()
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

i = 0


def type(string):
    for character in string:
        keybd.type(character)
        time.sleep(0.05)


def clear(words_raw):
    words = ""

    for c in words_raw:
        asc = ord(c)
        if 97 <= asc <= 122:
            words += c

    return words


while True:
    img = pyautogui.screenshot(region=(675, 95, 650, 750))
    img.save(r"C:\Users\super\Desktop\Giovanni\Programacion\Lenguajes\Python\Ztype\img.png")

    img = cv2.imread('img.png')

    img = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.adaptiveThreshold(cv2.bilateralFilter(img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                          31, 2)



    words_raw = pytesseract.image_to_string(img)

    words = clear(words_raw)
    print(words)

    type(words)
    type('\b')

    i = 1
