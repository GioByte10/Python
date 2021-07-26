import random
import time
from pynput.keyboard import Controller

keyboard = Controller()
time.sleep(5)


def type(string):

    for character in string:
        keyboard.type(character)


while True:
    type("abcdefghijklmnopqrstuvwxyz")

