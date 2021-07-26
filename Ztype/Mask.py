import pyautogui
import time
import cv2
from pytesseract import pytesseract
from pynput.keyboard import Controller
import numpy as np

lower_orange = np.array([15, 50, 50])
upper_orange = np.array([45, 255, 255])

time.sleep(3)

keybd = Controller()
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

i = 0


def type(string):

    if "avelear" not in string:

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
    hsv = cv2.cvtColor(r_img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    orange_c = cv2.bitwise_and(r_img, r_img, mask= mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    r = cv2.add(r_img, mask)

    words_raw = pytesseract.image_to_string(r)

    words = clear(words_raw)
    print(words)

    type(words)

    i = 1
