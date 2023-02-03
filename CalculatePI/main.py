import random
from math import sqrt


def randomN():
    return random.random() * 2 - 1


n = 10000000
c = 0

for i in range(n):
    x = randomN()
    y = randomN()

    if sqrt(x*x + y*y) <= 1:
        c = c + 1


pi = (c / n) * 4
print(pi)
