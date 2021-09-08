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

    r_img = cv2.imread("img.png")
    gray = cv2.cvtColor(r_img, cv2.COLOR_BGR2GRAY)

    words_raw = pytesseract.image_to_string(gray)

    words = clear(words_raw)
    print(words)

    type(words)
    type('\b')

    i = 1