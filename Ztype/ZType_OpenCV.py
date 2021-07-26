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

    # Grayscale, Gaussian blur, Otsu's threshold
    r_img = cv2.imread("img.png")
    gray = cv2.cvtColor(r_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Morph open to remove noise and invert image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    invert = 255 - opening

    words_raw = pytesseract.image_to_string(invert)
    words = clear(words_raw)
    print(words)

    type(words)
    type('\b')


    i = 1
