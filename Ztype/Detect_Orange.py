import pyautogui
import time

time.sleep(2)

color = (255, 126, 0)

found = False

s = pyautogui.screenshot()
for x in range(s.width):
    for y in range(s.height):
        if s.getpixel((x, y)) == color:
            pyautogui.moveTo(x, y)
            found = True

        if found:
            found = False
            break
