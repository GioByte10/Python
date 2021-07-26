import random
import time
from pynput.keyboard import Controller

keyboard = Controller()


time.sleep(3)


def type(string):



    for character in string:
        keyboard.type(character)
        delay = 0.01
        time.sleep(delay)




type("""

""")

