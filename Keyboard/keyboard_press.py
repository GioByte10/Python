import random
import time

import win32api
import win32con
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)

keyboard.press(Key.ctrl)
keyboard.press('t')
keyboard.release('t')
keyboard.release(Key.ctrl)

time.sleep(1)

keyboard.press(Key.ctrl)
keyboard.press('v')
keyboard.release('v')
keyboard.release(Key.ctrl)

time.sleep(1)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(3)


def type(string):

    for character in string:
        keyboard.type(character)
        delay = random.random() / 3
        time.sleep(delay)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


click(500, 420)
type("I better be getting into MIT because of this")
click(400, 400)

