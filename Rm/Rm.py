import pyautogui
import time

time.sleep(10)

while True:

    if int(time.strftime("%H")) == 13 or int(time.strftime("%H")) == 17 or int(time.strftime("%H")) == 22 or int(time.strftime("%H")) == 0:
        cords = pyautogui.locateCenterOnScreen('C:\\Users\\super\\Desktop\\Giovanni\\Programacion\\Lenguajes\\Python\\Rm\\Sh.png')

        if cords is not None:
            pyautogui.click(cords)

        else:
            cords = pyautogui.locateCenterOnScreen('C:\\Users\\super\\Desktop\\Giovanni\\Programacion\\Lenguajes\\Python\\Rm\\Nn.png')

            if cords is not None:
                pyautogui.click(cords)

    time.sleep(3600)
