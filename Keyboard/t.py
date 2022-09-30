import random
import time
from pynput.keyboard import Controller

keyboard = Controller()

time.sleep(7)


def type(string):

    for character in string:
        keyboard.type(character)
        delay = 0.15
        time.sleep(delay)



type("""
Well clearly you don't remember
Or that's what you want me to think
You just don't want to chip in fr
""")

#



