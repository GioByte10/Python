import random

i = int(input("iterations: "))
n = 1

for a in range(i):

    if n % 2 == 0:
        n = (n - 1) / 3

    else:
        n *= 2

    print(n)
