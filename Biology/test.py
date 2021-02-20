import sys
import time
import random


def randomString(soFar, x):

    for i in range(x):
        n = random.randint(0, 30)
        n += 33
        c = chr(n)
        soFar += c

    return soFar


string = ""
toGet = "Testing 109 Hello DNA Is This Working???"

for x in range(len(toGet)):
    soFar = toGet[0:x + 1]
    string = randomString(soFar, len(toGet) - 1 - x)
    sys.stdout.write('\r' + string)
    sys.stdout.flush()
    time.sleep(0.25)
