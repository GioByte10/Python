import pyautogui
import time
import cv2
from pytesseract import pytesseract
from pynput.keyboard import Controller
import numpy as np
import enchant

dic = enchant.Dict("en_us")

lower_orange = np.array([15, 50, 50])
upper_orange = np.array([45, 255, 255])

time.sleep(3)

keybd = Controller()
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

i = 0


def type(string):

    for character in string:
        keybd.type(character)
        time.sleep(0.03)


def clear(words_raw):
    words = ""

    for c in words_raw:
        asc = ord(c)
        if 97 <= asc <= 122 or asc == 32:
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

    gray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    cv2.imshow("r", invert)
    cv2.waitKey()

    words_raw = pytesseract.image_to_string(invert)

    if "avelear" not in words_raw:
        words = clear(words_raw).split()

        for word in words:

            if True:
                print(word)
                type(word)

    i = 0