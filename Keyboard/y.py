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

    time.sleep(2.5)


day = 1

for i in range(19):

    date = ""

    if day == 7:
        day = 0

    if day == 1:
        date += "Monday, "

    elif day == 2:
        date += "Tuesday, "

    elif day == 3:
        date += "Wednesday, "

    elif day == 4:
        date += "Thursday, "

    elif day == 5:
        date += "Friday, "

    elif day == 6:
        date += "Saturday, "

    elif day == 0:
        date += "Sunday, "


    date += "July " + str(i + 12)
    day += 1

    type(date)
