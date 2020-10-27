import random

elements = ['A', 'B', 'C']
probabilities = [0] * len(elements)
summatory = 0

a = 0
b = 0
c = 0

for i in range(len(elements)):
    probabilities[i] = int(input("Enter the probability for element " + elements[i] + '\n'))
    summatory += probabilities[i]

for i in range(len(elements)):
    probabilities[i] /= summatory


def pickOne():
    i = 0
    r = random.random()

    while r > 0:
        r -= probabilities[i]
        i += 1

    i -= 1

    return elements[i]


for i in range(10000):
    e = pickOne()

    if e == 'A':
        a += 1

    elif e == 'B':
        b += 1

    elif e == 'C':
        c += 1

print("Element A: " + str(a) + " element B: " + str(b) + " element C: " + str(c))
