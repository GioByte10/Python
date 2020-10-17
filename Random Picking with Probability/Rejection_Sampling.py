import random

elements = ['A', 'B', 'C']
probabilities = [0] * len(elements)
maxValue = 0

a = 0
b = 0
c = 0

for i in range(len(elements)):
    probabilities[i] = int(input("Enter the probability for element " + elements[i] + '\n'))
    if probabilities[i] > maxValue:
        maxValue = probabilities[i]


def acceptReject():
    while True:
        selectedIndex = random.randint(0, len(elements) - 1)
        selectedP = probabilities[selectedIndex]
        r = random.random() * maxValue

        if r < selectedP:
            return elements[selectedIndex]


for i in range(10000):
    e = acceptReject()

    if e == 'A':
        a += 1

    elif e == 'B':
        b += 1

    elif e == 'C':
        c += 1

print("Element A: " + str(a) + " element B: " + str(b) + " element C: " + str(c))
