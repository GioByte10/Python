import pyautogui
import time
import cv2
from pytesseract import pytesseract
from pynput.keyboard import Controller
import numpy as np
import enchant

abc = "abcdefghijklmnopqrstuvwxyz"

dic = enchant.Dict("en_us")

orange = (255, 126, 0)

word_l_orange = np.array([15, 200, 200])
word_u_orange = np.array([15, 255, 255])

target_l_orange = np.array([12, 50, 50])
target_u_orange = np.array([14, 255, 255])

time.sleep(3)

keybd = Controller()
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

i = 0
x = 0
y = 0


def type(string):

    for character in string:
        keybd.type(character)
        time.sleep(0.04)


def quickType(string):

    for character in string:
        keybd.type(character)


def clear(words_raw):
    words = ""

    for c in words_raw:
        asc = ord(c)
        if 97 <= asc <= 122 or asc == 32:
            words += c

    return words


def crisis(img, x, y):

    for char in abc:
        keybd.type(char)
        print(char)

        if not checkWrong(img, x, y):
            break


def checkWrong(img, width, height):

    for x in range(650):
        for y in range(750):
            if img.getpixel((x, y)) == orange:
                return True

    return False


def replaceIfWrong(img, i, width, height):

    if i == 4:
        quickType("aenilukhostry")

    elif i >= 5:
        crisis(img, width, height)

    for x in range(650):
        for y in range(750):
            # print("x: " + str(x) + "     y: " + str(y))

            if img.getpixel((x, y)) == orange:
                img = pyautogui.screenshot(region=(x + 650, y + 90, 140, 70))
                img.save(r"C:\Users\super\Desktop\Giovanni\Programacion\Lenguajes\Python\Ztype\img.png")

                # pyautogui.moveTo(x + 675, y + 95)

                i += 1

                # img.save(r"C:\Users\super\Desktop\Giovanni\Programacion\Lenguajes\Python\Ztype\img" + str(i) + ".png")
                # quickType("aenilukhostry")

                return [i, x, y]

    if i > 0:
        print("++++++++++++++++++ZERO")
        i = 0

    return [i, 0, 0]


while True:
    img = pyautogui.screenshot(region=(675, 95, 650, 750))
    img.save(r"C:\Users\super\Desktop\Giovanni\Programacion\Lenguajes\Python\Ztype\img.png")

    a = replaceIfWrong(img, i, x, y)

    i = a[0]
    x = a[1]
    y = a[2]

    r_img = cv2.imread("img.png")
    hsv = cv2.cvtColor(r_img, cv2.COLOR_BGR2HSV)

    word_mask = cv2.inRange(hsv, word_l_orange, word_u_orange)
    word_mask = cv2.cvtColor(word_mask, cv2.COLOR_GRAY2BGR)

    r1 = cv2.add(r_img, word_mask)

    # target_mask = cv2.inRange(hsv, target_l_orange, target_u_orange)
    # target_mask = cv2.cvtColor(target_mask, cv2.COLOR_GRAY2BGR)

    # cv2.imshow("r", r1)
    # aenilukhostrycv2.waitKey()

    # r2 = cv2.subtract(r1, target_mask)



    words_raw = pytesseract.image_to_string(r1)

    if "ave" not in words_raw:
        words = clear(words_raw).split()

        for word in words:
            if True:
                print(word)
                type(word)

        time.sleep(0.1)
